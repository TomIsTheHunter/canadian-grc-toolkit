# Walkthrough: Canadian GRC Toolkit

Audience: Non-technical readers, project stakeholders, and new team members.
Purpose: Explain what this project does, why each part exists, and why we chose these approaches over common alternatives.

## 1) What this project is in plain language

This project is a compliance toolkit for Canadian financial institutions.
It helps teams prove they are following important cyber and privacy expectations by turning policy rules into checks that can be tested automatically.

Think of it as:
- A policy library (the rules)
- A test lab (proof the rules work)
- A reporting package (documents and machine-readable control records)
- A quality gate (CI checks before changes are accepted)

## 2) What problem we are solving

Compliance teams often rely on manual reviews and spreadsheets. That is slow and can miss things.
This toolkit makes key controls testable and repeatable so teams can:
- Detect issues earlier
- Reduce manual effort
- Show auditors concrete evidence
- Keep rule logic consistent across environments

## 3) High-level architecture

The repository has five major parts:

1. Policy-as-code rules (OPA/Rego)
2. Control documentation and cross-reference content
3. OSCAL control encoding (machine-readable controls)
4. Python tooling for validation and log analysis
5. CI workflow to enforce tests before merge

## 4) Component-by-component walkthrough

### A) Policies folder

Location: policies

What it contains:
- Data residency rule (data must stay in approved Canadian regions)
- Privileged access logging rule (required fields and logging expectations)
- Encryption-at-rest rule (encryption enabled, approved algorithms, key controls)
- Unit tests for each policy

Why this matters:
- These rules are the enforceable controls.
- Unit tests prove each control catches failures and allows valid cases.

Why OPA/Rego instead of alternatives:
- Why not ad hoc scripts only: scripts become inconsistent and harder to audit.
- Why not manual checklist only: manual checks are hard to repeat and easy to miss.
- Why OPA: policy-focused language, clean separation between policy logic and application code, broad ecosystem in governance/compliance.

### B) OSCAL folder

Location: oscal

What it contains:
- A JSON control catalog with three OSFI B-13 controls

Why this matters:
- OSCAL is a structured format intended for machine-readable compliance exchange.
- It helps future automation, evidence mapping, and integration with governance tools.

Why OSCAL JSON instead of a PDF-only control list:
- PDF or Word is easy for humans but hard for systems.
- OSCAL enables automation while still allowing human-friendly docs elsewhere.

### C) Python scripts folder

Location: scripts

What it contains:
- Config validator: checks YAML config against an OSFI B-13 schema
- Audit log parser: scans privileged access logs for missing required details
- Checkov gap report: parses Checkov JSON scanner output into a formatted compliance gap report
- OSFI B-10 gap assessment tool: assesses the FRFI's internal compliance posture across six B-10 domains
- Unit tests for each script
- Schema files used by the validator and B-10 assessment

Why this matters:
- The validator prevents bad or incomplete configuration from silently entering operations.
- The parser identifies logging gaps tied to incident reporting obligations.
- The Checkov gap report turns raw infrastructure-as-code scan output into an audit-ready summary showing failed controls, skipped controls (with suppression reasons), and overall pass rate.
- The B-10 gap assessment tool provides a structured, machine-readable way to evaluate the FRFI's own third-party risk management posture — not vendor self-attestation — across arrangement classification, subcontracting, concentration, data residency, audit rights, and exit strategy. It flags supervisory risk items for critical arrangements and generates a completed or blank assessment file on demand.

Why Python for these tools:
- Easy readability for mixed teams.
- Strong libraries for YAML and schema validation.
- Low operational overhead for quick compliance utilities.

Why not use only shell scripts:
- Shell is less maintainable for structured validation logic.
- Error handling and testability are weaker for this use case.

### D) Documentation folders

Locations: docs and README

What they contain:
- Framework references and cross-mappings
- Project purpose, scope, and structure

Why this matters:
- Non-technical and audit stakeholders need traceability, not only code.
- It explains what controls map to which framework expectations.

Why not keep this only in issue tickets or chat history:
- Tickets/chats are fragmented and not durable as audit evidence.
- Repository docs provide versioned, reviewable history.

### E) CI workflow

Location: .github/workflows/ci.yml

What it does:
- Runs OPA formatting and policy tests
- Runs Python tests (covers config validator, audit log parser, Checkov gap report, and all B-10 assessment logic)
- Validates the OSFI B-10 CLI can generate a template and produces valid JSON
- Validates the Checkov gap report CLI accepts its arguments without error

Why this matters:
- Prevents untested changes from being merged.
- Provides objective pass/fail evidence per change.
- CLI entrypoint validation catches import errors and wiring problems that unit tests alone may not surface.

Why CI checks instead of trusting local testing only:
- Local runs vary by machine and can be skipped.
- CI gives a standardized, centrally recorded gate.

## 5) What has been completed this week

Completed deliverables:
- Three OPA policies written
- OPA tests written and passing
- OSCAL JSON document created with 3 B-13 controls
- Python config validator written and tested
- Python audit log parser written and tested
- Python Checkov gap report script written (parses passed/failed/skipped checks, filtered console report with tabulate, optional CSV export, --framework and --severity flags)
- Python OSFI B-10 gap assessment tool written and tested (six-domain JSON schema, compliance scoring, supervisory risk detection, template generation, CSV export)
- CI workflow updated with CLI entrypoint validation steps for both new scripts
- README updated with B-10 framework coverage, new tooling descriptions, and example commands

## 6) Why we did not choose other broader paths yet

1. Full enterprise GRC platform integration now
- Not chosen yet because it increases setup complexity and cost before baseline controls are stable.

2. Building everything in a single large service
- Not chosen because this project benefits from small, modular artifacts that are easier to review and audit.

3. Covering all OSFI controls immediately
- Not chosen because phased delivery reduces risk and allows quality validation as scope expands.

4. Replacing policy engine with custom code
- Not chosen because policy engines are purpose-built for declarative controls and auditability.

## 7) How to explain this to leadership in one minute

This project turns key cyber and privacy controls into testable rules.
It combines policy checks, evidence-oriented documentation, machine-readable control records, and automated testing gates.
The result is better consistency, faster validation, and clearer audit evidence with less manual effort.

## 8) Governance setup status and limits

Already in repository scope:
- Rules, tests, scripts, and CI workflow

Requires GitHub repository settings (outside regular files):
- Branch protection and required checks on main
- Required approvals and review settings
- Push restrictions and merge restrictions

These settings are controlled in GitHub repository administration and are not fully enforceable from source files alone.
