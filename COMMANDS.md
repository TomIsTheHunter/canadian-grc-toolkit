# Project Command Cheat Sheet

This is the quick reference for running the Canadian GRC Toolkit from the repository root.

## Prerequisites

- Python 3.11+
- OPA installed and available on PATH
- Checkov installed and available on PATH

## Environment Setup

Create and activate a virtual environment, then install dependencies.

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
pip install -r scripts/requirements.txt
```

## Fastest Commands

Use these when you just want the most common workflows.

| Goal | Command |
|---|---|
| Run lint checks | `python scripts/task_runner.py lint` |
| Run tests | `python scripts/task_runner.py test` |
| Generate all report artifacts | `python scripts/task_runner.py all-reports` |
| Run full end-to-end orchestration | `python scripts/task_runner.py full-compliance` |
| Run OPA policy tests | `opa test policies/ -v` |

## End-to-End Orchestration

Primary CLI for the full project workflow.

```bash
python main.py --iac-dir . --opa-input scripts/fair_scenario.json --vendor-data scripts/sample_vendor_data.json --risk-register scripts/sample_risk_register.json --policy-dir policies
```

Arguments:

- `--iac-dir`: Directory to scan with Checkov
- `--opa-input`: Input file used for OPA evaluation
- `--vendor-data`: Vendor JSON file for OSFI B-10 scoring
- `--risk-register`: Risk register JSON file
- `--policy-dir`: Rego policy directory, default is `policies`
- `--skip-preflight`: Skip tool availability checks for `opa` and `checkov`
- `--output-json`: Output path for consolidated JSON report
- `--output-md`: Output path for consolidated Markdown report

Example with explicit outputs:

```bash
python main.py --iac-dir . --opa-input scripts/fair_scenario.json --vendor-data scripts/sample_vendor_data.json --risk-register scripts/sample_risk_register.json --policy-dir policies --output-json reports/consolidated_compliance_report.json --output-md reports/consolidated_compliance_report.md
```

## Task Runner Shortcuts

These wrap the most common project workflows.

```bash
python scripts/task_runner.py test
python scripts/task_runner.py lint
python scripts/task_runner.py report-risk
python scripts/task_runner.py report-kpi
python scripts/task_runner.py classify-incident
python scripts/task_runner.py fair
python scripts/task_runner.py all-reports
python scripts/task_runner.py full-compliance
```

What each task does:

| Task | Purpose |
|---|---|
| `test` | Run the Python test suite |
| `lint` | Run Ruff and Black checks |
| `report-risk` | Generate risk register JSON and Markdown outputs |
| `report-kpi` | Generate the KPI dashboard |
| `classify-incident` | Generate OSFI/PIPEDA notification draft output |
| `fair` | Run the FAIR simulation |
| `all-reports` | Run all report-generation tasks |
| `full-compliance` | Run the main orchestrator with sample inputs |

## Direct Tooling Commands

### Python Tests

Run the same test command used by the task runner:

```bash
python -m pytest scripts/tests/ -v --tb=short
```

### Linting and Formatting Checks

Run the same lint commands used by the task runner:

```bash
python -m ruff check scripts
python -m black --check scripts
```

### OPA Policy Tests

Run all Rego policy tests:

```bash
opa test policies/ -v
```

## Individual Project CLIs

### Risk Register Processor

Process a risk register into enriched JSON and Markdown:

```bash
python -m scripts.risk_register --input scripts/sample_risk_register.json --output-json reports/risk_register_output.json --output-md reports/risk_register_report.md
```

Generate a blank template instead:

```bash
python -m scripts.risk_register --template --output-json reports/risk_register_template.json
```

Arguments:

- `--input`: Input JSON risk register file
- `--output-json`: Enriched JSON output path
- `--output-md`: Markdown report output path
- `--template`: Write a blank template and exit

### KPI Dashboard Generator

Generate the board-ready KPI dashboard:

```bash
python scripts/grc_kpi_report.py --input scripts/sample_risk_register.json --output reports/grc_kpi_dashboard.md --as-of 2026-10-21
```

Arguments:

- `--input`: Risk register JSON file
- `--output`: Output Markdown file
- `--as-of`: Reporting date in `YYYY-MM-DD`

### Incident Classifier

Classify mock events and generate a structured notification draft:

```bash
python scripts/osfi_incident_classifier.py --input scripts/mock_security_logs.csv --output reports/notification_draft.json --institution "Maple Bank" --prepared-by "Cyber Incident Response Team"
```

Arguments:

- `--input`: Input CSV or JSON event file
- `--format`: `auto`, `csv`, or `json`
- `--output`: Output JSON file
- `--institution`: Institution name for draft output
- `--prepared-by`: Person or team preparing the draft

### FAIR Quantitative Calculator

Run the FAIR model using the sample scenario:

```bash
python scripts/fair_calculator.py --scenario scripts/fair_scenario.json --iterations 2000 --output reports/fair_results.json
```

Run the built-in demo scenario instead:

```bash
python scripts/fair_calculator.py --demo --iterations 5000 --output reports/fair_demo_results.json
```

Arguments:

- `--scenario`: Scenario JSON file
- `--demo`: Run built-in demo scenario
- `--iterations`: Number of Monte Carlo iterations
- `--seed`: Random seed for reproducibility
- `--output`: Optional JSON output path

### Audit Log Parser

Validate privileged access audit logs:

```bash
python scripts/audit_log_parser.py --input scripts/mock_security_logs.json
```

Write findings to a file:

```bash
python scripts/audit_log_parser.py --input scripts/mock_security_logs.json --output reports/audit_log_findings.json
```

Arguments:

- `--input`: JSONL audit log file
- `--output`: Optional JSON output file

### Config Validator

Validate a YAML config against the OSFI B-13 schema:

```bash
python scripts/config_validator.py --config your-config.yaml
```

Use a custom schema path:

```bash
python scripts/config_validator.py --config your-config.yaml --schema scripts/schema/osfi_b13_policy_schema.yaml
```

Arguments:

- `--config`: YAML config file to validate
- `--schema`: Schema file path

## Common Workflows

### 1. Validate the codebase before sharing

```bash
python scripts/task_runner.py lint
python scripts/task_runner.py test
opa test policies/ -v
```

### 2. Generate all sample outputs

```bash
python scripts/task_runner.py all-reports
```

Expected artifacts include:

- `reports/risk_register_output.json`
- `reports/risk_register_report.md`
- `reports/grc_kpi_dashboard.md`
- `reports/notification_draft.json`
- `reports/fair_results.json`

### 3. Run the full compliance orchestration flow

```bash
python scripts/task_runner.py full-compliance
```

Or directly:

```bash
python main.py --iac-dir . --opa-input scripts/fair_scenario.json --vendor-data scripts/sample_vendor_data.json --risk-register scripts/sample_risk_register.json --policy-dir policies
```

### 4. Build a risk register report only

```bash
python scripts/task_runner.py report-risk
```

### 5. Build KPI dashboard only

```bash
python scripts/task_runner.py report-kpi
```

### 6. Build notification draft only

```bash
python scripts/task_runner.py classify-incident
```

### 7. Run FAIR only

```bash
python scripts/task_runner.py fair
```

## Contributor Commands

Install and use pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type pre-push
pre-commit run --all-files
```

Windows long-path workaround used in the repo README:

```powershell
$env:PRE_COMMIT_HOME = ".pcache"
$env:VIRTUALENV_OVERRIDE_APP_DATA = ".vappdata"
pre-commit run --all-files
```

## Notes

- Run commands from the repository root unless noted otherwise.
- The main orchestrator checks for `checkov` and `opa` before running unless `--skip-preflight` is provided.
- Most generated outputs are written into the `reports` folder.
