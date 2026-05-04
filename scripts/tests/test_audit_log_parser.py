from pathlib import Path

from scripts.audit_log_parser import parse_audit_log


def test_audit_log_parser_passes_compliant_events(tmp_path: Path) -> None:
    audit_file = tmp_path / "audit.jsonl"
    audit_file.write_text(
        """
{"actor_id":"admin-01","event_type":"privileged-login","timestamp":"2026-04-09T12:00:00Z","mfa_verified":true,"log_destination":"siem-prod"}
""".strip()
        + "\n",
        encoding="utf-8",
    )

    findings = parse_audit_log(audit_file)

    assert findings == []


def test_audit_log_parser_flags_missing_and_invalid_fields(tmp_path: Path) -> None:
    audit_file = tmp_path / "audit.jsonl"
    audit_file.write_text(
        """
{"actor_id":"admin-01","event_type":"privileged-login","timestamp":"2026-04-09T12:00:00Z","mfa_verified":false,"log_destination":"local-disk"}
{"actor_id":"admin-02","event_type":"privileged-command","mfa_verified":true}
""".strip()
        + "\n",
        encoding="utf-8",
    )

    findings = parse_audit_log(audit_file)

    assert any(f.get("issue") == "invalid_mfa" for f in findings)
    assert any(f.get("issue") == "unapproved_log_destination" for f in findings)
    assert any(
        f.get("issue") == "missing_required_field" and f.get("field") == "timestamp"
        for f in findings
    )
    assert any(
        f.get("issue") == "missing_required_field"
        and f.get("field") == "log_destination"
        for f in findings
    )


def test_audit_log_parser_flags_invalid_json(tmp_path: Path) -> None:
    audit_file = tmp_path / "audit.jsonl"
    audit_file.write_text("{not-valid-json}\n", encoding="utf-8")

    findings = parse_audit_log(audit_file)

    assert len(findings) == 1
    assert findings[0]["issue"] == "invalid_json"
