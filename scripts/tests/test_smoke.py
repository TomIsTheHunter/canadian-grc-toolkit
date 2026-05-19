"""Minimal smoke test to verify the test harness runs."""


def test_repository_smoke() -> None:
    """Verify that all primary modules are importable."""
    import scripts.audit_log_parser  # noqa: F401
    import scripts.config_validator  # noqa: F401
    import scripts.fair_calculator  # noqa: F401
    import scripts.grc_kpi_report  # noqa: F401
    import scripts.osfi_b10_vendor_risk  # noqa: F401
    import scripts.osfi_incident_classifier  # noqa: F401
    import scripts.risk_register  # noqa: F401
    import scripts.task_runner  # noqa: F401
    import main  # noqa: F401
