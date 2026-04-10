from __future__ import annotations

"""OSFI B-10 third-party risk gap assessment CLI.

IMPORTANT: This is not a vendor questionnaire or vendor self-attestation form.
This tool assesses the FRFI's own internal compliance posture against OSFI B-10
requirements for third-party risk management.
"""

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from tabulate import tabulate

SCHEMA_PATH = Path(__file__).parent / "schema" / "osfi_b10_gap_assessment_schema.json"
HIGH_SEVERITY = {"Critical", "High"}
INCOMPLETE_STATES = {"Not Started", "In Progress"}

DOMAIN_DEFINITIONS: dict[str, list[dict[str, str]]] = {
    "arrangement_classification": [
        {
            "key": "criticality_determination_logic",
            "requirement_id": "B10-AC-01",
            "b10_citation": "B-10, Principle 1",
            "requirement_text": "Document logic used to determine whether the arrangement is critical or non-critical.",
        },
        {
            "key": "classification_rationale",
            "requirement_id": "B10-AC-02",
            "b10_citation": "B-10, Principle 1",
            "requirement_text": "Retain rationale supporting the arrangement classification decision.",
        },
        {
            "key": "review_frequency",
            "requirement_id": "B10-AC-03",
            "b10_citation": "B-10, Principle 1",
            "requirement_text": "Define how often arrangement criticality is reviewed and refreshed.",
        },
    ],
    "subcontracting_controls": [
        {
            "key": "fourth_party_inventory",
            "requirement_id": "B10-SC-01",
            "b10_citation": "B-10, Principle 5",
            "requirement_text": "Maintain an inventory of material subcontractors and fourth parties supporting the arrangement.",
        },
        {
            "key": "subcontractor_approval_process",
            "requirement_id": "B10-SC-02",
            "b10_citation": "B-10, Principle 5",
            "requirement_text": "Define and evidence the approval process for adding or changing subcontractors.",
        },
        {
            "key": "flow_down_contract_requirements",
            "requirement_id": "B10-SC-03",
            "b10_citation": "B-10, Principle 5",
            "requirement_text": "Ensure contractual requirements flow down to subcontractors where needed.",
        },
        {
            "key": "fourth_party_concentration",
            "requirement_id": "B10-SC-04",
            "b10_citation": "B-10, Principle 5",
            "requirement_text": "Assess concentration exposure created by the use of common fourth parties.",
        },
    ],
    "concentration_risk": [
        {
            "key": "single_vendor_dependency_thresholds",
            "requirement_id": "B10-CR-01",
            "b10_citation": "B-10, Principle 2",
            "requirement_text": "Define thresholds for institution-level dependency on a single third party.",
        },
        {
            "key": "systemic_concentration_flags",
            "requirement_id": "B10-CR-02",
            "b10_citation": "B-10, Principle 2",
            "requirement_text": "Identify and track systemic concentration indicators for the arrangement.",
        },
        {
            "key": "sector_wide_provider_indicators",
            "requirement_id": "B10-CR-03",
            "b10_citation": "B-10, Principle 2",
            "requirement_text": "Evaluate whether the provider is a sector-wide dependency across FRFIs or critical services.",
        },
        {
            "key": "osfi_concentration_reporting_obligations",
            "requirement_id": "B10-CR-04",
            "b10_citation": "B-10, Principle 2",
            "requirement_text": "Document any concentration-related information that may need escalation or reporting to OSFI.",
        },
    ],
    "data_residency": [
        {
            "key": "data_location_mapping",
            "requirement_id": "B10-DR-01",
            "b10_citation": "B-10, Principle 6",
            "requirement_text": "Map where data is stored, processed, backed up, and accessed for the arrangement.",
        },
        {
            "key": "sovereignty_restrictions",
            "requirement_id": "B10-DR-02",
            "b10_citation": "B-10, Principle 6",
            "requirement_text": "Assess sovereignty restrictions, including PIPEDA and applicable provincial privacy laws.",
        },
        {
            "key": "cross_border_transfer_controls",
            "requirement_id": "B10-DR-03",
            "b10_citation": "B-10, Principle 6",
            "requirement_text": "Document controls governing cross-border data transfer and access.",
        },
        {
            "key": "residency_clause_in_contract",
            "requirement_id": "B10-DR-04",
            "b10_citation": "B-10, Principle 6",
            "requirement_text": "Confirm the contract includes data residency or location commitments where required.",
        },
    ],
    "audit_rights": [
        {
            "key": "right_to_audit_clause_presence",
            "requirement_id": "B10-AR-01",
            "b10_citation": "B-10, Principle 7",
            "requirement_text": "Confirm the contract includes a right-to-audit clause.",
        },
        {
            "key": "scope_of_audit_rights",
            "requirement_id": "B10-AR-02",
            "b10_citation": "B-10, Principle 7",
            "requirement_text": "Define the scope of audit rights over records, systems, facilities, and personnel.",
        },
        {
            "key": "third_party_audit_report_access",
            "requirement_id": "B10-AR-03",
            "b10_citation": "B-10, Principle 7",
            "requirement_text": "Obtain access to relevant third-party assurance reporting, such as SOC 2 or ISO 27001 evidence.",
        },
        {
            "key": "audit_frequency_minimum",
            "requirement_id": "B10-AR-04",
            "b10_citation": "B-10, Principle 7",
            "requirement_text": "Define a minimum audit or assurance review frequency for the arrangement.",
        },
    ],
    "exit_strategy": [
        {
            "key": "documented_exit_plan_existence",
            "requirement_id": "B10-ES-01",
            "b10_citation": "B-10, Principle 9",
            "requirement_text": "Maintain a documented exit plan for the arrangement.",
        },
        {
            "key": "transition_rto_rpo",
            "requirement_id": "B10-ES-02",
            "b10_citation": "B-10, Principle 9",
            "requirement_text": "Define transition RTO and RPO expectations for the service exit scenario.",
        },
        {
            "key": "transition_service_agreement",
            "requirement_id": "B10-ES-03",
            "b10_citation": "B-10, Principle 9",
            "requirement_text": "Determine whether a transition service agreement is required and contractually addressed.",
        },
        {
            "key": "data_return_destruction_clause",
            "requirement_id": "B10-ES-04",
            "b10_citation": "B-10, Principle 9",
            "requirement_text": "Confirm contractual coverage for data return or secure destruction at exit.",
        },
        {
            "key": "tested_exit_rehearsal",
            "requirement_id": "B10-ES-05",
            "b10_citation": "B-10, Principle 9",
            "requirement_text": "Test or rehearse the exit strategy for critical arrangements.",
        },
    ],
}

DOMAIN_LABELS = {
    "arrangement_classification": "Arrangement Classification",
    "subcontracting_controls": "Subcontracting Controls",
    "concentration_risk": "Concentration Risk",
    "data_residency": "Data Residency",
    "audit_rights": "Audit Rights",
    "exit_strategy": "Exit Strategy",
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Error: file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Error: malformed JSON in {path}: {exc}") from exc


def load_schema(path: Path) -> dict[str, Any]:
    data = load_json(path)
    if not isinstance(data, dict):
        raise SystemExit(f"Error: schema file must contain a JSON object: {path}")
    return data


def validate_assessment(assessment: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(assessment), key=lambda err: list(err.path))

    findings: list[str] = []
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "root"
        findings.append(f"{location}: {error.message}")
    return findings


def build_template_assessment() -> dict[str, Any]:
    template = {
        "assessment_metadata": {
            "frfi_name": "Example FRFI",
            "arrangement_name": "Example Third-Party Arrangement",
            "arrangement_classification": "critical",
            "assessment_date": "YYYY-MM-DD",
        }
    }
    for domain, requirements in DOMAIN_DEFINITIONS.items():
        template[domain] = {}
        for requirement in requirements:
            template[domain][requirement["key"]] = {
                "requirement_id": requirement["requirement_id"],
                "b10_citation": requirement["b10_citation"],
                "requirement_text": requirement["requirement_text"],
                "current_state": "Not Started",
                "gap_description": "Describe the current gap or note 'None' if compliant.",
                "severity": "Medium",
                "evidence_ref": "path/to/evidence-or-url",
                "remediation_owner": "Owner Name / Team",
                "target_date": "YYYY-MM-DD",
                "status": "Open",
            }
    return template


def flatten_assessment(assessment: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    metadata = assessment["assessment_metadata"]
    for domain, requirements in DOMAIN_DEFINITIONS.items():
        domain_block = assessment.get(domain, {})
        for requirement in requirements:
            item = domain_block[requirement["key"]]
            rows.append(
                {
                    "frfi_name": metadata["frfi_name"],
                    "arrangement_name": metadata["arrangement_name"],
                    "arrangement_classification": metadata["arrangement_classification"],
                    "domain": domain,
                    "domain_label": DOMAIN_LABELS[domain],
                    "requirement_key": requirement["key"],
                    "requirement_id": item["requirement_id"],
                    "b10_citation": item["b10_citation"],
                    "requirement_text": item["requirement_text"],
                    "current_state": item["current_state"],
                    "gap_description": item["gap_description"],
                    "severity": item["severity"],
                    "evidence_ref": item["evidence_ref"],
                    "remediation_owner": item["remediation_owner"],
                    "target_date": item["target_date"],
                    "status": item["status"],
                }
            )
    return rows


def calculate_domain_scores(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    summary_rows: list[dict[str, str]] = []
    for domain in DOMAIN_DEFINITIONS:
        domain_rows = [row for row in rows if row["domain"] == domain]
        total = len(domain_rows)
        non_high_critical = sum(1 for row in domain_rows if row["severity"] not in HIGH_SEVERITY)
        score = (non_high_critical / total * 100) if total else 0.0
        high_critical_count = total - non_high_critical
        summary_rows.append(
            {
                "domain": DOMAIN_LABELS[domain],
                "total_requirements": str(total),
                "critical_high_gaps": str(high_critical_count),
                "compliance_score": f"{score:.1f}%",
            }
        )
    return summary_rows


def critical_high_findings(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    findings = [row for row in rows if row["severity"] in HIGH_SEVERITY]
    return sorted(findings, key=lambda row: (row["domain"], row["requirement_id"]))


def supervisory_risks(assessment: dict[str, Any], rows: list[dict[str, str]]) -> list[dict[str, str]]:
    if assessment["assessment_metadata"]["arrangement_classification"] != "critical":
        return []

    risks: list[dict[str, str]] = []
    exit_rows = [row for row in rows if row["domain"] == "exit_strategy"]
    audit_rows = [row for row in rows if row["domain"] == "audit_rights"]

    if any(row["severity"] in HIGH_SEVERITY or row["current_state"] in INCOMPLETE_STATES for row in exit_rows):
        risks.append(
            {
                "risk_type": "SUPERVISORY RISK",
                "trigger": "Critical arrangement with incomplete exit strategy",
                "detail": "One or more exit strategy requirements remain high-risk or incomplete for a critical arrangement.",
            }
        )

    if any(row["severity"] in HIGH_SEVERITY or row["current_state"] in INCOMPLETE_STATES for row in audit_rows):
        risks.append(
            {
                "risk_type": "SUPERVISORY RISK",
                "trigger": "Critical arrangement with missing or incomplete audit rights",
                "detail": "Audit rights requirements are missing, incomplete, or assessed as high-risk for a critical arrangement.",
            }
        )

    return risks


def print_report(summary_rows: list[dict[str, str]], findings: list[dict[str, str]], risks: list[dict[str, str]]) -> None:
    print("\nOSFI B-10 Third-Party Risk Gap Assessment")
    print("=" * 72)
    print("This report assesses the FRFI's internal compliance posture, not vendor self-attestation.")

    print("\nDomain Summary")
    print("-" * 72)
    print(
        tabulate(
            [
                [
                    row["domain"],
                    row["total_requirements"],
                    row["critical_high_gaps"],
                    row["compliance_score"],
                ]
                for row in summary_rows
            ],
            headers=["Domain", "Total", "Critical/High Gaps", "Compliance Score"],
            tablefmt="github",
        )
    )

    print("\nCritical and High Findings")
    print("-" * 72)
    if findings:
        print(
            tabulate(
                [
                    [
                        row["domain_label"],
                        row["requirement_id"],
                        row["severity"],
                        row["current_state"],
                        row["remediation_owner"],
                        row["target_date"],
                        row["gap_description"],
                    ]
                    for row in findings
                ],
                headers=["Domain", "Requirement", "Severity", "State", "Owner", "Target", "Gap"],
                tablefmt="github",
            )
        )
    else:
        print("No Critical or High severity items identified.")

    print("\nSupervisory Risk")
    print("-" * 72)
    if risks:
        print(
            tabulate(
                [[risk["risk_type"], risk["trigger"], risk["detail"]] for risk in risks],
                headers=["Type", "Trigger", "Detail"],
                tablefmt="github",
            )
        )
    else:
        print("No supervisory risk triggers detected.")


def export_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "frfi_name",
        "arrangement_name",
        "arrangement_classification",
        "domain",
        "domain_label",
        "requirement_key",
        "requirement_id",
        "b10_citation",
        "requirement_text",
        "current_state",
        "gap_description",
        "severity",
        "evidence_ref",
        "remediation_owner",
        "target_date",
        "status",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assess a FRFI's OSFI B-10 third-party risk compliance posture from a JSON assessment file."
    )
    parser.add_argument("assessment", nargs="?", type=Path, help="Path to the JSON assessment file.")
    parser.add_argument(
        "--schema",
        type=Path,
        default=SCHEMA_PATH,
        help="Path to the JSON schema file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to export the flattened assessment as CSV.",
    )
    parser.add_argument(
        "--template",
        nargs="?",
        const="osfi_b10_gap_assessment_template.json",
        type=Path,
        help="Generate a blank assessment template JSON file and exit.",
    )
    args = parser.parse_args()
    if args.template is None and args.assessment is None:
        parser.error("either an assessment file or --template must be provided")
    return args


def main() -> int:
    args = parse_args()
    schema = load_schema(args.schema)

    if args.template is not None:
        template = build_template_assessment()
        args.template.write_text(json.dumps(template, indent=2) + "\n", encoding="utf-8")
        print(f"Template written to {args.template.resolve()}")
        return 0

    assessment = load_json(args.assessment)
    if not isinstance(assessment, dict):
        raise SystemExit(f"Error: assessment file must contain a JSON object: {args.assessment}")

    findings = validate_assessment(assessment, schema)
    if findings:
        print(json.dumps({"valid": False, "findings": findings}, indent=2))
        return 1

    rows = flatten_assessment(assessment)
    summary_rows = calculate_domain_scores(rows)
    detail_rows = critical_high_findings(rows)
    risk_rows = supervisory_risks(assessment, rows)
    print_report(summary_rows, detail_rows, risk_rows)

    if args.output:
        export_csv(args.output, rows)
        print(f"\nCSV exported to {args.output.resolve()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())