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

## Control Coverage Table

This table maps implemented checks to framework-aligned control areas so reviewers can quickly understand coverage intent.

| Check | Implementation | OSFI B-13 | OSFI B-10 | OSFI Incident Reporting Advisory | PIPEDA DERR | ISO 27001/27002 | NIST CSF 2.0 |
|---|---|---|---|---|---|---|---|
| Data residency policy validation | `policies/data_residency.rego` + tests | Data governance, information lifecycle, and legal/regulatory control alignment | Third-party data location considerations in outsourcing context | Supports impact scoping for reportable incidents involving data movement | Supports breach context and records-at-risk analysis | Information classification and data handling controls | `GV`, `PR.DS`, `ID` |
| Encryption at rest policy validation | `policies/encryption_at_rest.rego` + tests | Cryptographic protection expectations for sensitive information | Contractual expectations for vendor encryption controls | Improves incident severity reduction and defensibility | Supports safeguard expectations for personal information | Cryptography and key management controls | `PR.DS` |
| Privileged access logging checks | `policies/privileged_access_logging.rego` + `scripts/audit_log_parser.py` | Security monitoring, logging, and access governance controls | Third-party access oversight and monitoring evidence | Enables faster detection/escalation for reportable cyber events | Supports breach investigation and evidence retention | Logging, monitoring, and privileged access controls | `DE`, `PR.AA`, `RS` |
| Third-party risk scoring | `scripts/osfi_b10_vendor_risk.py` | Third-party cyber risk integration with enterprise technology risk | Core B-10 due diligence, concentration, resilience, and exit planning themes | Flags vendor incidents likely to trigger reporting criteria | Supports vendor-breach impact and notification triage | Supplier relationship and third-party assurance controls | `GV`, `ID.SC` |
| Incident classification and draft notifications | `scripts/osfi_incident_classifier.py` | Technology/cyber incident management capability | Vendor-involved incident escalation support | 24-hour trigger assessment and deadline tracking | OPC notification indicator assessment support | Incident response and communications controls | `RS`, `RC` |
| Risk register scoring and markdown reporting | `scripts/risk_register.py` | Ongoing technology risk identification, assessment, and treatment tracking | Third-party risks can be represented and monitored in register outputs | Supports governance evidence for incident and resilience oversight | Documents residual privacy risk posture and treatment progress | Risk assessment and risk treatment process controls | `ID.RA`, `GV.RM` |
| Board KPI dashboard generation | `scripts/grc_kpi_report.py` | Management and board-level cyber risk reporting evidence | Third-party treatment progress visibility at governance level | Supports escalation readiness and supervisory communication quality | Shows trend and remediation evidence for privacy-relevant risks | Performance measurement and continuous improvement controls | `GV`, `RS` |
| FAIR quantitative simulation | `scripts/fair_calculator.py` | Quantitative cyber risk analysis for control investment decisions | Supports risk-based vendor oversight prioritization | Improves materiality assessment discipline during incidents | Supports financial impact framing for significant harm analysis | Risk quantification support for ISMS decision-making | `ID.RA` |
| End-to-end orchestration and IaC scan | `main.py` + Checkov + OPA stages | Integrated control assurance workflow and evidence generation | Includes vendor and policy control checks in one run | Consolidates incident, control, and compliance signals for supervisors | Consolidates policy/privacy-relevant outputs for reporting workflows | Continuous compliance and control validation practices | `GV`, `DE`, `RS` |

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

## Folder Guides

Use this root README as the primary entry point. Each major folder also has a local README with folder-specific details.

- docs/README.md
- docs/frameworks/README.md
- docs/frameworks/osfi/README.md
- docs/frameworks/legislation/README.md
- docs/frameworks/standards/README.md
- docs/cross-references/README.md
- policies/README.md
- scripts/README.md
- scripts/tests/README.md
- scripts/schema/README.md
- reports/README.md
- oscal/README.md

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
