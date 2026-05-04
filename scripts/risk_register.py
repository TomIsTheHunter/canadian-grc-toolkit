#!/usr/bin/env python3
"""
risk_register.py — Structured OSFI-aligned risk register.

Supports:
- Inherent vs residual risk scoring (likelihood × impact, 1–25 scale)
- OSFI-aligned risk categories: technology, cyber, third-party, data, operational
- Automated RAG status (Red/Amber/Green) derived from residual risk score
- JSON schema validation for auditability and consistency
- Export to enriched JSON and formatted Markdown report

RAG thresholds (residual score out of 25):
  Green  : 1–7   (acceptable risk)
  Amber  : 8–14  (elevated risk, treatment plan required)
  Red    : 15–25 (critical risk, immediate action required)

Usage:
  python -m scripts.risk_register --input sample_risk_register.json
  python -m scripts.risk_register --template --output-json reports/template.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

import jsonschema

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_SCHEMA_PATH = Path(__file__).parent / "schema" / "risk_register_schema.json"

# Residual score thresholds (inclusive lower bound, score = likelihood × impact)
_RAG_RED_THRESHOLD = 15
_RAG_AMBER_THRESHOLD = 8

_RAG_BADGES = {"Red": "🔴 Red", "Amber": "🟡 Amber", "Green": "🟢 Green"}

# Default OSFI guideline reference inferred from risk category
_CATEGORY_OSFI_REF: dict[str, str] = {
    "technology": "OSFI B-13 – Technology and Cyber Risk Management",
    "cyber": "OSFI B-13 – Technology and Cyber Risk Management",
    "third-party": "OSFI B-10 – Third-Party Risk Management",
    "data": "OSFI B-13 §3 / Quebec Law 25 – Privacy Legislation",
    "operational": "OSFI E-21 – Operational Risk Management",
}

# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------


def calculate_rag(residual_score: int) -> str:
    """Return Red, Amber, or Green based on a residual risk score (1–25)."""
    if residual_score >= _RAG_RED_THRESHOLD:
        return "Red"
    if residual_score >= _RAG_AMBER_THRESHOLD:
        return "Amber"
    return "Green"


def _load_schema() -> dict[str, Any]:
    with _SCHEMA_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def validate_register(data: dict[str, Any]) -> None:
    """Validate *data* against the risk register JSON schema.

    Raises jsonschema.ValidationError on the first violation found.
    """
    schema = _load_schema()
    jsonschema.validate(
        instance=data,
        schema=schema,
        format_checker=jsonschema.FormatChecker(),
    )


def _enrich_entry(entry: dict[str, Any]) -> dict[str, Any]:
    """Return a copy of *entry* with computed score and rag_status fields."""
    out = dict(entry)

    inh = entry["inherent_risk"]
    out["inherent_risk"] = {
        "likelihood": inh["likelihood"],
        "impact": inh["impact"],
        "score": inh["likelihood"] * inh["impact"],
    }

    res = entry["residual_risk"]
    res_score = res["likelihood"] * res["impact"]
    out["residual_risk"] = {
        "likelihood": res["likelihood"],
        "impact": res["impact"],
        "score": res_score,
    }

    out["rag_status"] = calculate_rag(res_score)

    # Infer OSFI reference from category if not explicitly provided
    if not out.get("osfi_reference"):
        out["osfi_reference"] = _CATEGORY_OSFI_REF.get(entry["category"], "")

    return out


def process_register(data: dict[str, Any]) -> dict[str, Any]:
    """Validate the register and return an enriched copy with all computed fields."""
    validate_register(data)
    return {
        "register_metadata": dict(data["register_metadata"]),
        "risks": [_enrich_entry(e) for e in data["risks"]],
    }


# ---------------------------------------------------------------------------
# Export: JSON
# ---------------------------------------------------------------------------


def to_json(enriched: dict[str, Any], output_path: Path) -> None:
    """Write *enriched* register to *output_path* as indented JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(enriched, fh, indent=2)
    print(f"[✓] JSON report written  → {output_path}")


# ---------------------------------------------------------------------------
# Export: Markdown
# ---------------------------------------------------------------------------


def to_markdown(enriched: dict[str, Any], output_path: Path) -> None:
    """Write a formatted Markdown risk report to *output_path*."""
    meta = enriched["register_metadata"]
    risks = enriched["risks"]
    today = date.today().isoformat()

    lines: list[str] = [
        f"# {meta['title']}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Version | {meta.get('version', '—')} |",
        f"| Created by | {meta.get('created_by', '—')} |",
        f"| Review cycle | {meta.get('review_cycle', '—')} |",
        f"| Report generated | {today} |",
        "",
    ]

    if desc := meta.get("description"):
        lines += [f"> {desc}", ""]

    # ---- RAG legend --------------------------------------------------------
    lines += [
        "## RAG Status Key",
        "",
        "| Status | Residual Score | Meaning |",
        "|--------|---------------|---------|",
        "| 🟢 Green | 1 – 7 | Acceptable — monitor at scheduled review |",
        "| 🟡 Amber | 8 – 14 | Elevated — treatment plan required |",
        "| 🔴 Red   | 15 – 25 | Critical — immediate action required |",
        "",
    ]

    # ---- Summary table -----------------------------------------------------
    lines += [
        "## Risk Summary",
        "",
        "| ID | Title | Category | Inherent Score | Controls | Residual Score | RAG |",
        "|----|-------|----------|:--------------:|:--------:|:--------------:|-----|",
    ]
    for r in risks:
        rag_badge = _RAG_BADGES.get(r["rag_status"], r["rag_status"])
        lines.append(
            f"| {r['id']} | {r['title']} | {r['category']} "
            f"| {r['inherent_risk']['score']} "
            f"| {len(r['controls'])} "
            f"| {r['residual_risk']['score']} "
            f"| {rag_badge} |"
        )

    lines += ["", "---", "", "## Risk Detail", ""]

    # ---- Per-risk detail sections ------------------------------------------
    for r in risks:
        rag = r["rag_status"]
        rag_badge = _RAG_BADGES.get(rag, rag)
        inh = r["inherent_risk"]
        res = r["residual_risk"]

        lines += [
            f"### {r['id']} — {r['title']}",
            "",
            "| Field | Value |",
            "|-------|-------|",
            f"| **Category** | {r['category']} |",
            f"| **OSFI Reference** | {r.get('osfi_reference', '—')} |",
            f"| **Owner** | {r['owner']} |",
            f"| **Review Date** | {r['review_date']} |",
            f"| **RAG Status** | {rag_badge} |",
            "",
            f"**Description:** {r['description']}",
            "",
            "#### Inherent Risk (before controls)",
            "",
            "| Likelihood (1–5) | Impact (1–5) | Score (max 25) |",
            "|:----------------:|:------------:|:--------------:|",
            f"| {inh['likelihood']} | {inh['impact']} | **{inh['score']}** |",
            "",
            "#### Controls in Place",
            "",
        ]
        for i, ctrl in enumerate(r["controls"], start=1):
            lines.append(f"{i}. {ctrl}")

        lines += [
            "",
            "#### Residual Risk (after controls)",
            "",
            "| Likelihood (1–5) | Impact (1–5) | Score (max 25) | RAG Status |",
            "|:----------------:|:------------:|:--------------:|:----------:|",
            f"| {res['likelihood']} | {res['impact']} | **{res['score']}** | {rag_badge} |",
            "",
            "---",
            "",
        ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[✓] Markdown report written → {output_path}")


# ---------------------------------------------------------------------------
# Blank template
# ---------------------------------------------------------------------------

_TEMPLATE: dict[str, Any] = {
    "register_metadata": {
        "title": "OSFI Risk Register",
        "version": "1.0",
        "created_by": "Risk Management Team",
        "review_cycle": "quarterly",
        "description": "Structured risk register aligned to OSFI B-10, B-13, and E-21.",
    },
    "risks": [
        {
            "id": "RISK-001",
            "title": "Example Risk — replace with your risk title",
            "description": "Describe the risk event and its potential business impact.",
            "category": "technology",
            "osfi_reference": "",
            "inherent_risk": {"likelihood": 3, "impact": 4},
            "controls": [
                "Describe control 1 (e.g. automated patch management)",
                "Describe control 2 (e.g. vulnerability scanning quarterly)",
            ],
            "residual_risk": {"likelihood": 2, "impact": 3},
            "owner": "CISO",
            "review_date": "2026-06-30",
        }
    ],
}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Canadian GRC Toolkit — OSFI-aligned Risk Register",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  Process a register:  python -m scripts.risk_register --input data/risks.json\n"
            "  Generate template:   python -m scripts.risk_register --template\n"
        ),
    )
    parser.add_argument(
        "--input",
        metavar="FILE",
        help="Path to input JSON risk register file",
    )
    parser.add_argument(
        "--output-json",
        metavar="FILE",
        default="reports/risk_register_output.json",
        help="Output path for enriched JSON (default: reports/risk_register_output.json)",
    )
    parser.add_argument(
        "--output-md",
        metavar="FILE",
        default="reports/risk_register_report.md",
        help="Output path for Markdown report (default: reports/risk_register_report.md)",
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Write a blank template JSON to --output-json and exit",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    out_json = Path(args.output_json)
    out_md = Path(args.output_md)

    if args.template:
        to_json(_TEMPLATE, out_json)
        print("[i] Edit the template, then re-run with --input to process it.")
        return 0

    if not args.input:
        parser.error("--input is required unless --template is specified")

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[✗] Input file not found: {input_path}", file=sys.stderr)
        return 1

    with input_path.open(encoding="utf-8") as fh:
        raw = json.load(fh)

    try:
        enriched = process_register(raw)
    except jsonschema.ValidationError as exc:
        print(f"[✗] Schema validation failed: {exc.message}", file=sys.stderr)
        return 1

    to_json(enriched, out_json)
    to_markdown(enriched, out_md)

    reds = sum(1 for r in enriched["risks"] if r["rag_status"] == "Red")
    ambers = sum(1 for r in enriched["risks"] if r["rag_status"] == "Amber")
    greens = sum(1 for r in enriched["risks"] if r["rag_status"] == "Green")
    print(
        f"\n[i] Register summary: {len(enriched['risks'])} risks — "
        f"🔴 {reds} Red  🟡 {ambers} Amber  🟢 {greens} Green"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
