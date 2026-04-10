import json
from pathlib import Path

from scripts.osfi_b10_gap_assessment import (
    SCHEMA_PATH,
    build_template_assessment,
    calculate_domain_scores,
    critical_high_findings,
    flatten_assessment,
    supervisory_risks,
    validate_assessment,
)


def test_template_conforms_to_schema() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    template = build_template_assessment()

    findings = validate_assessment(template, schema)

    assert findings == []


def test_domain_scores_and_supervisory_risk_detection() -> None:
    assessment = build_template_assessment()
    assessment["assessment_metadata"]["arrangement_classification"] = "critical"
    assessment["audit_rights"]["right_to_audit_clause_presence"]["severity"] = "Critical"
    assessment["audit_rights"]["right_to_audit_clause_presence"]["gap_description"] = "Contract lacks an explicit right-to-audit clause."
    assessment["audit_rights"]["right_to_audit_clause_presence"]["current_state"] = "Not Started"
    assessment["exit_strategy"]["tested_exit_rehearsal"]["severity"] = "High"
    assessment["exit_strategy"]["tested_exit_rehearsal"]["gap_description"] = "Exit rehearsal has not been performed."
    assessment["exit_strategy"]["tested_exit_rehearsal"]["current_state"] = "In Progress"

    rows = flatten_assessment(assessment)
    summary = calculate_domain_scores(rows)
    findings = critical_high_findings(rows)
    risks = supervisory_risks(assessment, rows)

    audit_summary = next(row for row in summary if row["domain"] == "Audit Rights")
    exit_summary = next(row for row in summary if row["domain"] == "Exit Strategy")

    assert audit_summary["compliance_score"] == "75.0%"
    assert exit_summary["compliance_score"] == "80.0%"
    assert {row["requirement_id"] for row in findings} == {"B10-AR-01", "B10-ES-05"}
    assert len(risks) == 2


def test_validation_flags_missing_required_field(tmp_path: Path) -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assessment = build_template_assessment()
    del assessment["data_residency"]["data_location_mapping"]["status"]

    findings = validate_assessment(assessment, schema)

    assert any("data_residency.data_location_mapping" in finding for finding in findings)