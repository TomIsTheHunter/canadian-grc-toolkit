# Canadian GRC Toolkit

A policy-as-code toolkit for Canadian financial institutions implementing
GRC (Governance, Risk and Compliance) controls aligned to OSFI guidance and
Canadian data sovereignty requirements.

## Framework Coverage

| Framework | Coverage |
|---|---|
| OSFI B-10 (Third-Party Risk) | Partial |
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

## CI/CD

Every push runs:
- OPA format check and policy unit tests
- Python smoke tests

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
```

## Status

| Week | Deliverable | Status |
|---|---|---|
| Week 1 | Repo setup, folder structure | Complete |
| Week 2 | OPA policies, OSCAL JSON, Python scripts | Complete |