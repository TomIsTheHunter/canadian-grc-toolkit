# Policies

This folder contains OPA Rego policies and policy tests.

## Current Policy Areas

- Data residency checks
- Encryption at rest checks
- Privileged access logging checks

Each `*_test.rego` file validates the corresponding policy behavior.

## Run Policy Tests

From the repository root:

- `opa test policies/ -v`
