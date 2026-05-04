#!/usr/bin/env python3
"""Single CLI entry point for end-to-end compliance-as-code checks.

Pipeline:
1. Run Checkov against IaC
2. Evaluate OPA policies against configuration input
3. Run OSFI B-10 vendor risk assessment
4. Score risk register and derive RAG statuses
5. Produce consolidated compliance report (JSON + Markdown)
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts.osfi_b10_vendor_risk import assess_vendor_risk_file
from scripts.risk_register import process_register


@dataclass
class CommandResult:
    """Execution metadata for an external command invocation."""

    command: list[str]
    exit_code: int | None
    stdout: str
    stderr: str
    ok: bool
    error: str | None = None


def _existing_path(value: str) -> Path:
    """Argparse type helper that validates a path exists."""

    path = Path(value)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"Path not found: {path}")
    return path


def _run_command(command: list[str]) -> CommandResult:
    """Run a command and return structured output without raising on failure."""

    try:
        proc = subprocess.run(command, capture_output=True, text=True, check=False)
        return CommandResult(
            command=command,
            exit_code=proc.returncode,
            stdout=proc.stdout or "",
            stderr=proc.stderr or "",
            ok=proc.returncode == 0,
        )
    except FileNotFoundError as exc:
        return CommandResult(
            command=command,
            exit_code=None,
            stdout="",
            stderr="",
            ok=False,
            error=str(exc),
        )


def _tool_install_hint(tool: str) -> str:
    """Return operator guidance for installing a missing external dependency."""

    if tool == "checkov":
        return "Install with 'pip install checkov' (or pipx) and ensure it is in PATH"
    if tool == "opa":
        return "Install from openpolicyagent.org and ensure 'opa' is in PATH"
    return "Install tool and ensure it is in PATH"


def run_preflight_stage() -> dict[str, Any]:
    """Validate required external tools before running compliance stages."""

    required_tools = ["checkov", "opa"]
    checks: list[dict[str, Any]] = []

    for tool in required_tools:
        resolved = shutil.which(tool)
        checks.append(
            {
                "tool": tool,
                "available": resolved is not None,
                "resolved_path": resolved,
                "install_hint": _tool_install_hint(tool) if resolved is None else None,
            }
        )

    missing = [item["tool"] for item in checks if not item["available"]]
    compliant = len(missing) == 0

    return {
        "stage": "preflight",
        "ok": compliant,
        "compliant": compliant,
        "checks": checks,
        "error": (
            "Missing required tool(s): " + ", ".join(missing)
            if missing
            else None
        ),
    }


def _discover_opa_packages(policy_dir: Path) -> list[str]:
    """Extract package names declared in Rego files under policy_dir."""

    package_pattern = re.compile(r"^\s*package\s+([^\s]+)\s*$")
    packages: set[str] = set()
    for file_path in policy_dir.rglob("*.rego"):
        for line in file_path.read_text(encoding="utf-8").splitlines():
            match = package_pattern.match(line)
            if match:
                packages.add(match.group(1))
                break
    return sorted(packages)


def _extract_opa_value(payload: dict[str, Any]) -> Any:
    """Return the first OPA expression value from a JSON eval payload."""

    result = payload.get("result", [])
    if not result:
        return None
    expressions = result[0].get("expressions", [])
    if not expressions:
        return None
    return expressions[0].get("value")


def run_checkov_stage(iac_dir: Path) -> dict[str, Any]:
    """Execute Checkov against IaC and return stage status plus summary metrics."""

    command = ["checkov", "-d", str(iac_dir), "--output", "json", "--soft-fail"]
    cmd = _run_command(command)

    stage: dict[str, Any] = {
        "stage": "checkov_iac_scan",
        "ok": cmd.ok,
        "error": cmd.error,
        "command": cmd.command,
        "exit_code": cmd.exit_code,
        "summary": None,
        "compliant": None,
    }

    if cmd.error:
        stage["compliant"] = False
        return stage

    try:
        payload = json.loads(cmd.stdout)
        summary = payload.get("summary", {})
        failed = int(summary.get("failed", 0))
        passed = int(summary.get("passed", 0))
        skipped = int(summary.get("skipped", 0))
        stage["summary"] = {"passed": passed, "failed": failed, "skipped": skipped}
        stage["compliant"] = failed == 0
    except json.JSONDecodeError:
        # If parsing fails, treat command success as technical success but compliance unknown.
        stage["summary"] = {"raw_stdout_preview": cmd.stdout[:500]}
        stage["compliant"] = False

    return stage


def _derive_opa_compliance(value: Any) -> bool | None:
    """Normalize common OPA decision payload shapes into a compliance boolean."""

    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        if isinstance(value.get("allow"), bool):
            return value["allow"]
        deny = value.get("deny")
        if isinstance(deny, list):
            return len(deny) == 0
    return None


def run_opa_stage(policy_dir: Path, config_input: Path) -> dict[str, Any]:
    """Evaluate policy decisions for discovered Canada-scoped Rego packages."""

    packages = [p for p in _discover_opa_packages(policy_dir) if p.startswith("canada.")]
    decisions: list[dict[str, Any]] = []
    stage_ok = True

    for package in packages:
        query = f"data.{package}.allow"
        command = [
            "opa",
            "eval",
            "--format",
            "json",
            "-d",
            str(policy_dir),
            "-i",
            str(config_input),
            query,
        ]
        cmd = _run_command(command)

        if cmd.error:
            stage_ok = False
            decisions.append(
                {
                    "package": package,
                    "query": query,
                    "allow": None,
                    "compliant": False,
                    "ok": False,
                    "error": cmd.error,
                }
            )
            continue

        try:
            payload = json.loads(cmd.stdout)
            value = _extract_opa_value(payload)
            compliant = _derive_opa_compliance(value)
            decisions.append(
                {
                    "package": package,
                    "query": query,
                    "allow": value,
                    "compliant": compliant,
                    "ok": cmd.ok,
                }
            )
        except json.JSONDecodeError:
            stage_ok = False
            decisions.append(
                {
                    "package": package,
                    "query": query,
                    "allow": None,
                    "compliant": False,
                    "ok": False,
                    "error": "Unable to parse OPA JSON output",
                }
            )

    compliant_values = [d["compliant"] for d in decisions if d["compliant"] is not None]
    stage_compliant = all(compliant_values) if compliant_values else False

    return {
        "stage": "opa_policy_evaluation",
        "ok": stage_ok,
        "packages_evaluated": len(decisions),
        "decisions": decisions,
        "compliant": stage_compliant,
    }


def run_vendor_stage(vendor_data: Path) -> dict[str, Any]:
    """Run OSFI B-10 vendor risk assessment and convert to stage format."""

    assessment = assess_vendor_risk_file(vendor_data)
    return {
        "stage": "osfi_b10_vendor_risk_assessment",
        "ok": True,
        "compliant": assessment["summary"]["high_or_critical_count"] == 0,
        "assessment": assessment,
    }


def run_risk_register_stage(risk_register: Path) -> dict[str, Any]:
    """Score a risk register and summarize Red/Amber/Green distribution."""

    with risk_register.open(encoding="utf-8") as handle:
        raw = json.load(handle)

    enriched = process_register(raw)
    rag_counts = {
        "Red": sum(1 for r in enriched["risks"] if r["rag_status"] == "Red"),
        "Amber": sum(1 for r in enriched["risks"] if r["rag_status"] == "Amber"),
        "Green": sum(1 for r in enriched["risks"] if r["rag_status"] == "Green"),
    }

    return {
        "stage": "risk_register_scoring",
        "ok": True,
        "compliant": rag_counts["Red"] == 0,
        "summary": {
            "risk_count": len(enriched["risks"]),
            "rag_counts": rag_counts,
        },
        "enriched_register": enriched,
    }


def _stage_result_with_error(stage_name: str, exc: Exception) -> dict[str, Any]:
    """Return a normalized failed stage payload for unexpected exceptions."""

    return {
        "stage": stage_name,
        "ok": False,
        "compliant": False,
        "error": str(exc),
    }


def orchestrate(
    iac_dir: Path,
    opa_input: Path,
    vendor_data: Path,
    risk_register: Path,
    policy_dir: Path,
    skip_preflight: bool = False,
) -> dict[str, Any]:
    """Run all compliance stages and assemble a consolidated report payload."""

    stages: list[dict[str, Any]] = []

    if not skip_preflight:
        preflight = run_preflight_stage()
        stages.append(preflight)
        if not preflight["ok"]:
            return {
                "generated_at_utc": datetime.now(timezone.utc).isoformat(),
                "inputs": {
                    "iac_dir": str(iac_dir),
                    "opa_input": str(opa_input),
                    "vendor_data": str(vendor_data),
                    "risk_register": str(risk_register),
                    "policy_dir": str(policy_dir),
                },
                "overall": {
                    "ok": False,
                    "compliant": False,
                },
                "stages": stages,
            }

    try:
        stages.append(run_checkov_stage(iac_dir))
    except Exception as exc:  # pragma: no cover
        stages.append(_stage_result_with_error("checkov_iac_scan", exc))

    try:
        stages.append(run_opa_stage(policy_dir=policy_dir, config_input=opa_input))
    except Exception as exc:  # pragma: no cover
        stages.append(_stage_result_with_error("opa_policy_evaluation", exc))

    try:
        stages.append(run_vendor_stage(vendor_data))
    except Exception as exc:
        stages.append(_stage_result_with_error("osfi_b10_vendor_risk_assessment", exc))

    try:
        stages.append(run_risk_register_stage(risk_register))
    except Exception as exc:
        stages.append(_stage_result_with_error("risk_register_scoring", exc))

    overall_compliant = all(stage.get("compliant") is True for stage in stages)
    overall_ok = all(stage.get("ok") is True for stage in stages)

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "iac_dir": str(iac_dir),
            "opa_input": str(opa_input),
            "vendor_data": str(vendor_data),
            "risk_register": str(risk_register),
            "policy_dir": str(policy_dir),
        },
        "overall": {
            "ok": overall_ok,
            "compliant": overall_compliant,
        },
        "stages": stages,
    }


def _render_markdown(report: dict[str, Any]) -> str:
    """Render the consolidated report as a markdown summary table."""

    lines = [
        "# Consolidated Compliance Report",
        "",
        f"Generated at (UTC): {report['generated_at_utc']}",
        "",
        "## Overall Status",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Execution OK | {report['overall']['ok']} |",
        f"| Compliance OK | {report['overall']['compliant']} |",
        "",
        "## Stage Summary",
        "",
        "| Stage | Execution OK | Compliance OK | Notes |",
        "|---|---:|---:|---|",
    ]

    for stage in report["stages"]:
        notes = stage.get("error", "")
        if not notes and stage["stage"] == "checkov_iac_scan" and stage.get("summary"):
            summary = stage["summary"]
            if "failed" in summary:
                notes = f"passed={summary['passed']} failed={summary['failed']} skipped={summary['skipped']}"
        if not notes and stage["stage"] == "opa_policy_evaluation":
            notes = f"packages={stage.get('packages_evaluated', 0)}"
        if not notes and stage["stage"] == "preflight":
            missing = [
                item["tool"]
                for item in stage.get("checks", [])
                if item.get("available") is False
            ]
            notes = (
                "all required tools available"
                if not missing
                else f"missing tools: {', '.join(missing)}"
            )
        if (
            not notes
            and stage["stage"] == "osfi_b10_vendor_risk_assessment"
            and stage.get("assessment")
        ):
            notes = (
                f"vendors={stage['assessment']['summary']['vendor_count']} "
                f"high_or_critical={stage['assessment']['summary']['high_or_critical_count']}"
            )
        if (
            not notes
            and stage["stage"] == "risk_register_scoring"
            and stage.get("summary")
        ):
            rag = stage["summary"]["rag_counts"]
            notes = f"risks={stage['summary']['risk_count']} red={rag['Red']} amber={rag['Amber']} green={rag['Green']}"

        lines.append(
            f"| {stage['stage']} | {stage.get('ok')} | {stage.get('compliant')} | {notes} |"
        )

    return "\n".join(lines) + "\n"


def _write_report(report: dict[str, Any], output_json: Path, output_md: Path) -> None:
    """Persist consolidated outputs to JSON and markdown files."""

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)

    output_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    output_md.write_text(_render_markdown(report), encoding="utf-8")


def _build_parser() -> argparse.ArgumentParser:
    """Construct CLI argument parser for end-to-end orchestration."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iac-dir", type=_existing_path, required=True)
    parser.add_argument("--opa-input", type=_existing_path, required=True)
    parser.add_argument("--vendor-data", type=_existing_path, required=True)
    parser.add_argument("--risk-register", type=_existing_path, required=True)
    parser.add_argument("--policy-dir", type=_existing_path, default=Path("policies"))
    parser.add_argument(
        "--skip-preflight",
        action="store_true",
        help="Skip required external tool checks for checkov and opa.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("reports") / "consolidated_compliance_report.json",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("reports") / "consolidated_compliance_report.md",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for running and exporting consolidated checks."""

    parser = _build_parser()
    args = parser.parse_args(argv)

    report = orchestrate(
        iac_dir=args.iac_dir,
        opa_input=args.opa_input,
        vendor_data=args.vendor_data,
        risk_register=args.risk_register,
        policy_dir=args.policy_dir,
        skip_preflight=args.skip_preflight,
    )
    _write_report(report, output_json=args.output_json, output_md=args.output_md)

    print(f"[✓] Consolidated JSON report written → {args.output_json}")
    print(f"[✓] Consolidated Markdown report written → {args.output_md}")

    if report["overall"]["ok"] and report["overall"]["compliant"]:
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())