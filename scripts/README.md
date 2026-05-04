# Scripts

This folder contains Python tooling for validation, classification, reporting, and orchestration.

## Main Modules

- `task_runner.py`: Convenience task entry points.
- `risk_register.py`: Risk register processing and output generation.
- `grc_kpi_report.py`: KPI dashboard generation.
- `osfi_incident_classifier.py`: Incident classification logic.
- `osfi_b10_vendor_risk.py`: Third-party risk scoring logic.
- `fair_calculator.py`: FAIR scenario and risk quantification logic.
- `audit_log_parser.py`: Audit log parsing and control checks.
- `config_validator.py`: Schema/config validation helpers.

## Subfolders

- `tests/`: Unit, integration, and golden-output tests.
- `schema/`: JSON/YAML schemas used by validators.
