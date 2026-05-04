# GRC KPI Dashboard — Golden Register

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Created by | Golden Tests |
| Review cycle | quarterly |
| Reporting date | 2026-10-21 |

> Deterministic fixture for golden output tests.

> Assumptions: risks are treated as open monitoring items, control effectiveness is measured as weighted residual risk reduction, finding age is inferred from the review cycle, and prior-period trend values are mock baselines for demonstration only.

## Executive Summary

| KPI | Current Period |
|-----|----------------|
| Control effectiveness rate | 61.3% |
| Open findings | 2 |
| High / critical findings | 0 |
| Overdue review items | 2 |
| Average treatment completion | 60.9% |

## Control Effectiveness

| Category | Risks | Avg treatment completion | Portfolio risk reduction | Complete | In progress | Planned | Behind schedule |
|----------|------:|-------------------------:|-------------------------:|---------:|------------:|--------:|----------------:|
| cyber | 1 | 46.7% | 46.7% | 0 | 0 | 0 | 1 |
| operational | 1 | 75.0% | 75.0% | 1 | 0 | 0 | 0 |

## Open Findings By Severity And Age

| Severity | 0-30 days | 31-60 days | 61-90 days | >90 days | Total |
|----------|----------:|-----------:|-----------:|----------:|------:|
| Critical | 0 | 0 | 0 | 0 | 0 |
| High | 0 | 0 | 0 | 0 | 0 |
| Medium | 0 | 0 | 0 | 1 | 1 |
| Low | 0 | 0 | 0 | 1 | 1 |

## Overdue Items

| ID | Title | Category | Owner | Review date | Days overdue | Residual score | Flag |
|----|-------|----------|-------|-------------|-------------:|---------------:|------|
| RISK-001 | Credential Stuffing | cyber | VP Cybersecurity | 2026-06-30 | 113 | 8 | Owner action required |
| RISK-002 | Privileged Access Abuse | operational | Director IAM | 2026-09-30 | 21 | 4 | Owner action required |

## Trend Vs Prior Period

| Metric | Current | Prior period (mock) | Delta | Direction |
|--------|--------:|--------------------:|------:|-----------|
| Control effectiveness rate | 61.3% | 53.9% | +7.4 pts | Improved |
| High / critical findings | 0 | 1 | -1 | Improved |
| Overdue review items | 2 | 4 | -2 | Improved |
| Average treatment completion | 60.9% | 51.3% | +9.6 pts | Improved |
