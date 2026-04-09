from pathlib import Path

from scripts.config_validator import validate_config


def test_config_validator_accepts_valid_config(tmp_path: Path) -> None:
    config = tmp_path / "valid.yaml"
    config.write_text(
        """
institution_name: Example Bank
controls:
  data_residency:
    allowed_regions:
      - ca-central-1
  privileged_access_logging:
    required_fields:
      - actor_id
      - event_type
      - timestamp
      - mfa_verified
      - log_destination
    approved_destinations:
      - siem-prod
  encryption_at_rest:
    approved_algorithms:
      - AES256
    require_cmk_for_sensitive: true
""".strip()
        + "\n",
        encoding="utf-8",
    )

    schema = Path("scripts/schema/osfi_b13_policy_schema.yaml")
    findings = validate_config(config, schema)

    assert findings == []


def test_config_validator_flags_schema_violations(tmp_path: Path) -> None:
    config = tmp_path / "invalid.yaml"
    config.write_text(
        """
institution_name: Example Bank
controls:
  data_residency:
    allowed_regions: []
  privileged_access_logging:
    required_fields:
      - actor_id
    approved_destinations: []
  encryption_at_rest:
    approved_algorithms:
      - AES256
""".strip()
        + "\n",
        encoding="utf-8",
    )

    schema = Path("scripts/schema/osfi_b13_policy_schema.yaml")
    findings = validate_config(config, schema)

    assert any("allowed_regions" in finding for finding in findings)
    assert any("approved_destinations" in finding for finding in findings)
    assert any("require_cmk_for_sensitive" in finding for finding in findings)
