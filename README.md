# Canadian GRC Toolkit

Policy-as-code and reporting toolkit for Canadian financial-sector GRC work. This project helps teams validate controls, classify incidents, and produce board-ready risk reporting aligned to OSFI and Canadian privacy expectations.

## Who This Is For

- GRC specialists and technology risk teams at Canadian banks
- Security engineering teams implementing policy-as-code controls
- Compliance and audit teams preparing evidence and management reporting

## What You Can Do

- Validate core policy controls in OPA Rego
- Parse and assess privileged access audit logs
- Classify incidents for OSFI/PIPEDA notification thresholds
- Generate risk register reports and KPI dashboards
- Run FAIR quantitative risk simulations for management reporting

## Quick Start

Prerequisites:

- Python 3.11+
- OPA installed and available in your PATH
- Checkov installed and available in your PATH

Setup:

1. Install Python dependencies

   pip install -r scripts/requirements.txt

2. Run full local quality checks

   python scripts/task_runner.py lint
   python scripts/task_runner.py test

3. Generate all sample reports

   python scripts/task_runner.py all-reports

4. Run full compliance orchestration (single entry point)

   python main.py --iac-dir . --opa-input scripts/fair_scenario.json --vendor-data scripts/sample_vendor_data.json --risk-register scripts/sample_risk_register.json

   The orchestrator now performs a preflight check for required tools (`checkov` and `opa`) and fails fast with install guidance if they are missing.
   If you need to run without these checks, use:

   python main.py --iac-dir . --opa-input scripts/fair_scenario.json --vendor-data scripts/sample_vendor_data.json --risk-register scripts/sample_risk_register.json --skip-preflight

## Typical Commands

Run policy tests:

opa test policies/ -v

Run all Python tests:

python scripts/task_runner.py test

Generate risk register outputs:

python scripts/task_runner.py report-risk

Generate KPI dashboard:

python scripts/task_runner.py report-kpi

Run incident classification:

python scripts/task_runner.py classify-incident

Run FAIR simulation:

python scripts/task_runner.py fair

Run full compliance orchestration from task runner:

python scripts/task_runner.py full-compliance

## Output Files You Should Expect

After running all reports, the reports folder includes:

- reports/risk_register_output.json
- reports/risk_register_report.md
- reports/grc_kpi_dashboard.md
- reports/notification_draft.json
- reports/fair_results.json

After running `main.py`, additional consolidated outputs are generated:

- reports/consolidated_compliance_report.json
- reports/consolidated_compliance_report.md

## Repository Map

| Folder | Purpose |
|---|---|
| policies | OPA Rego policies and tests |
| scripts | Python validation/reporting tools and tests |
| reports | Generated reporting artifacts |
| docs | Supporting walkthroughs and framework documentation |
| oscal | OSCAL-aligned control documentation |

## Contributing

Install contributor hooks:

1. pip install pre-commit
2. pre-commit install
3. pre-commit install --hook-type pre-push
4. pre-commit run --all-files

Windows tip for long-path issues during hook setup:

1. $env:PRE_COMMIT_HOME = ".pcache"
2. $env:VIRTUALENV_OVERRIDE_APP_DATA = ".vappdata"
3. pre-commit run --all-files

## Technical Detail Policy

This README is intentionally usage-first.

Detailed technical specifications, implementation rationale, and edge-case behavior should live in code comments and module docstrings in the scripts and policy files.

## CI Overview

CI runs:

- OPA lint and policy tests
- Python lint with ruff and black
- Python tests and report generation checks
- Golden output snapshot checks
