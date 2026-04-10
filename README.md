# Canadian GRC Toolkit

A policy-as-code toolkit for Canadian financial institutions implementing
GRC (Governance, Risk and Compliance) controls aligned to OSFI guidance and
Canadian data sovereignty requirements.

## Framework Coverage

| Framework | Coverage |
|---|---|
| OSFI B-10 (Third-Party Risk) | Gap assessment tool + JSON schema |
| OSFI Incident Reporting Advisory | Privileged access logging |
| PIPEDA / Law 25 | Data residency enforcement |
| NIST CSF | Encryption-at-rest controls |

## Repository Structure

| Folder | Contents |
|---|---|
| /policies | OPA Rego policy files and unit tests |
| /oscal | OSCAL-formatted control documentation (JSON) |
| /scripts | Python scripts for validation and reporting |
| /docs | Design documentation and control narratives |
| /reports | Generated compliance reports |

## Policies Implemented

- Data Residency: Enforces that all resources are provisioned in Canadian
	regions (ca-central-1, ca-west-1) and that replication destinations are
	also within Canada.

- Privileged Access Logging: Validates that privileged access events contain
	fields required by OSFI incident reporting expectations, including actor
	identity, MFA verification, and approved log destinations.

- Encryption-at-Rest: Checks that persistent resources use approved
	algorithms, that sensitive resources use customer-managed keys (CMK), and
	that key rotation is enabled.

## Python Tooling

- Config Validator: `scripts/config_validator.py` validates YAML policy
	configuration against the OSFI B-13 schema in
	`scripts/schema/osfi_b13_policy_schema.yaml`.

- Audit Log Parser: `scripts/audit_log_parser.py` parses privileged access log
	JSONL files and flags missing requirements aligned with OSFI incident
	reporting expectations.

- Checkov Gap Report: `scripts/checkov_gap_report.py` parses Checkov JSON
	scanner output and produces a formatted gap report with pass rate, failed
	controls, and skipped controls. Supports `--framework`, `--severity`,
	and `--output` flags.

- OSFI B-10 Gap Assessment: `scripts/osfi_b10_gap_assessment.py` assesses the
	FRFI's internal compliance posture across six B-10 domains (arrangement
	classification, subcontracting controls, concentration risk, data residency,
	audit rights, and exit strategy). Generates a blank assessment template with
	`--template`, exports CSV with `--output`, and flags supervisory risk items
	for critical arrangements with incomplete exit or audit-rights coverage.
	This tool is not a vendor questionnaire — it measures internal FRFI posture.

## CI/CD

Every push runs:
- OPA format check and policy unit tests
- Python smoke tests (pytest covers all scripts including B-10 assessment)
- OSFI B-10 CLI entrypoint validation (template generation + JSON parse check)
- Checkov gap report CLI entrypoint validation

Branch protection on main should require all checks to pass before merge.

## Running Locally

Prerequisites: OPA installed, Python 3.11+

```bash
# Run OPA policy tests
opa test policies/ -v

# Evaluate a policy against sample input
opa eval \
	-i input/sample_resource.json \
	-d policies/ \
	-d data/ \
	"data.compliance.report"

# Run Python smoke tests
pip install -r scripts/requirements.txt
python -m pytest scripts/tests/ -v

# Generate a blank OSFI B-10 gap assessment template
python scripts/osfi_b10_gap_assessment.py --template my_assessment_template.json

# Run an OSFI B-10 gap assessment and export CSV
python scripts/osfi_b10_gap_assessment.py my_assessment.json --output gap_report.csv

# Parse Checkov JSON output into a gap report
python scripts/checkov_gap_report.py checkov_results.json
python scripts/checkov_gap_report.py checkov_results.json --framework terraform --severity HIGH --output checkov_gaps.csv
```

## Status

| Week | Deliverable | Status |
|---|---|---|
| Week 1 | Repo setup, folder structure | Complete |
| Week 2 | OPA policies, OSCAL JSON, Python scripts | Complete |
| Week 3 | Checkov gap report, OSFI B-10 gap assessment tool + JSON schema, CI entrypoint validation | Complete |