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
- Validates the risk register CLI can generate a template, process a sample register, and produce valid JSON output (rag_status and score fields present on every entry)

Why this matters:
- Prevents untested changes from being merged.
- Provides objective pass/fail evidence per change.
- CLI entrypoint validation catches import errors and wiring problems that unit tests alone may not surface.

Why CI checks instead of trusting local testing only:
- Local runs vary by machine and can be skipped.
- CI gives a standardized, centrally recorded gate.

### F) Risk register

Location: scripts/risk_register.py, scripts/schema/risk_register_schema.json, scripts/sample_risk_register.json

What it contains:
- Structured risk register with JSON schema validation (jsonschema draft-07)
- Inherent risk score: likelihood × impact (1–25 scale) before controls are applied
- Residual risk score: likelihood × impact (1–25 scale) after controls are applied
- Automated RAG status derived from residual score: Green (1–7), Amber (8–14), Red (15–25)
- Five OSFI-aligned risk categories: technology, cyber, third-party, data, operational
- Auto-inferred OSFI guideline reference based on category (B-13, B-10, E-21, Quebec Law 25)
- Export to enriched JSON (with computed score and rag_status fields) and formatted Markdown report
- Blank template generation via --template flag
- Sample register with six realistic risk entries covering all five categories
- Full unit test coverage (score computation, RAG boundaries, schema rejection, JSON and Markdown export)

Why this matters:
- Manual spreadsheet registers cannot enforce field consistency, prevent invalid scores, or guarantee RAG logic is applied uniformly.
- JSON schema validation rejects malformed entries before they enter the record — catching typos, out-of-range scores, and missing required fields at the boundary.
- Computed scores and RAG status are deterministic and reproducible; a human calculating them in a spreadsheet can make different errors on different days.
- The Markdown export gives auditors a human-readable report from the same source of truth as the machine-readable JSON — no copy-paste step that could introduce divergence.
- OSFI reference inference ties every risk directly to a named guideline, reducing the likelihood of undocumented or orphaned risk entries.

Why JSON schema instead of only runtime checks:
- Schema validation provides a declared contract. Anyone reading the schema file knows exactly what a valid risk entry looks like, without reading the processing code.
- It separates data constraints from business logic, making both easier to review independently.

Why not a GRC platform or spreadsheet:
- Spreadsheets: no schema enforcement, no auditability of formula changes, no CI gate.
- Off-the-shelf GRC platforms: licensing cost, vendor lock-in, and reduced transparency for audit evidence generated by opaque calculation engines.
- This approach: open, version-controlled, testable, and fully auditable in the same repository as the controls it documents.

## 5) What has been completed this week

Completed deliverables (cumulative through Week 4):
- Three OPA policies written
- OPA tests written and passing
- OSCAL JSON document created with 3 B-13 controls
- Python config validator written and tested
- Python audit log parser written and tested
- Python Checkov gap report script written (parses passed/failed/skipped checks, filtered console report with tabulate, optional CSV export, --framework and --severity flags)
- Python OSFI B-10 gap assessment tool written and tested (six-domain JSON schema, compliance scoring, supervisory risk detection, template generation, CSV export)
- Python risk register written and tested (inherent/residual risk scoring, RAG status, OSFI-aligned categories, JSON schema validation, JSON and Markdown export, template generation)
- Risk register JSON schema (draft-07) covering all required fields with enum, pattern, range, and format constraints
- Sample risk register with six realistic entries spanning technology, cyber, third-party, data, and operational categories
- CI workflow updated with CLI validation steps for risk register template generation and sample register processing

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
