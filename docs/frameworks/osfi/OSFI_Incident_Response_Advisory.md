---
Document:        OSFI Technology and Cybersecurity Incident Reporting Advisory
Issuer:          Office of the Superintendent of Financial Institutions (OSFI)
Effective Date:  August 13, 2021
Last Verified:   April 2, 2026
Status:          Active
Type:            Mandatory – FRFI
Official URL:    https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/technology-cyber-security-incident-reporting
---

# OSFI Technology and Cybersecurity Incident Reporting Advisory

> **Document Type:** Regulatory Advisory
> **Issuer:** OSFI
> **Applies To:** All federally regulated financial institutions (FRFIs)
> **Effective Date:** August 13, 2021 (supersedes the 2019 Advisory)

> 📌 **For the full operational reference document** covering trigger criteria, reporting procedures, timelines, and cross-framework mapping for this Advisory, see:
> [`OSFI_Incident_Reporting_Trigger_Criteria.md`](../OSFI_Incident_Reporting_Trigger_Criteria.md)

---

## Table of Contents

1. [Overview and Purpose](#1-overview-and-purpose)
2. [Key Change from 2019 Advisory](#2-key-change-from-2019-advisory)
3. [Definition of a Reportable Incident](#3-definition-of-a-reportable-incident)
4. [Trigger Criteria Summary](#4-trigger-criteria-summary)
5. [Reporting Timeline](#5-reporting-timeline)
6. [Incident Reporting and Resolution Form — Appendix II](#6-incident-reporting-and-resolution-form--appendix-ii)
7. [Subsequent Reporting Requirements](#7-subsequent-reporting-requirements)
8. [Post-Incident Review](#8-post-incident-review)
9. [When in Doubt](#9-when-in-doubt)
10. [Relevance to OSFI 24-Hour Incident Reporting](#10-relevance-to-osfi-24-hour-incident-reporting)
11. [Cross-References](#11-cross-references)

---

## 1. Overview and Purpose

The OSFI Technology and Cybersecurity Incident Reporting Advisory establishes a **mandatory obligation** for all FRFIs to promptly notify OSFI of technology and cybersecurity incidents that have or could have an impact on their operations.

The Advisory's purpose is to ensure OSFI has **timely situational awareness** of:
- Emerging cyber and technology threats affecting the Canadian financial sector
- Systemic or sector-wide vulnerabilities revealed by individual FRFI incidents
- FRFIs' capacity to detect, respond to, and recover from technology disruptions

The Advisory reinforces OSFI's supervisory mandate and complements the risk management expectations set out in B-13, B-10, and E-21.

---

## 2. Key Change from 2019 Advisory

> ⚠️ **Critical Change:** The August 2021 Advisory **removed the "material impact" threshold** from the 2019 predecessor Advisory.

| Version                     | Threshold for Reporting                                                                             |
|-----------------------------|-----------------------------------------------------------------------------------------------------|
| **2019 Advisory**           | Reporting required only for incidents with a **material impact** on operations                      |
| **2021 Advisory (current)** | Reporting required for incidents with **any impact, or *potential* impact** — no materiality filter |

This change intentionally lowers the bar for reporting, reflecting OSFI's desire for earlier, precautionary notification rather than delayed reports of confirmed significant harm.

---

## 3. Definition of a Reportable Incident

> **"An incident that has an impact, or the potential to have an impact on the operations of a FRFI, including its confidentiality, integrity, or the availability of its systems and information."**

Key elements:
- **"Impact or potential to have an impact"** — reporting does not require confirmed harm
- **"Operations"** — broadly includes systems, processes, and services
- **CIA Triad reference** — confidentiality, integrity, *and* availability are all in scope

---

## 4. Trigger Criteria Summary

The Advisory provides a **non-exhaustive** list of characteristics that trigger the reporting obligation, organised into four groups:

### Group A — Impact-Based Criteria

| ID | Trigger                                                                                  |
|----|------------------------------------------------------------------------------------------|
| A1 | Potential consequences to other FRFIs or the Canadian financial system                   |
| A2 | Impact to FRFI systems affecting financial market settlement, confirmations, or payments |
| A3 | Impact to payment services                                                               |
| A4 | Impact to FRFI operations, infrastructure, data, and/or systems                          |
| A5 | Impact to confidentiality, integrity, or availability of customer information            |
| A6 | Operational impact to key/critical systems, infrastructure, or data                      |

### Group B — Operational Disruption Criteria

| ID | Trigger                                                                 |
|----|-------------------------------------------------------------------------|
| B1 | Disruptions to business systems and/or operations                       |
| B2 | Utility or data centre outages                                          |
| B3 | Loss or degradation of connectivity                                     |
| B4 | Disaster recovery teams or plans have been activated                    |
| B5 | Disaster declaration made by a third-party vendor that impacts the FRFI |
| B6 | Impact to a third party affecting the FRFI                              |

### Group C — Escalation & Governance Criteria

| ID | Trigger                                                                              |
|----|--------------------------------------------------------------------------------------|
| C1 | FRFI's technology or cyber incident management team or protocols have been activated |
| C2 | Incident reported to the Board of Directors or Senior/Executive Management           |
| C3 | Reported to the Office of the Privacy Commissioner and/or other regulatory agencies  |
| C4 | Cyber insurance claim has been initiated                                             |

### Group D — Severity & Scale Criteria

| ID | Trigger                                                                |
|----|------------------------------------------------------------------------|
| D1 | FRFI-assessed high or critical severity; Priority/Severity/Tier 1 or 2 |
| D2 | Number of external customers impacted is growing                       |
| D3 | Negative reputational impact is imminent                               |
| D4 | Breach of internal risk appetite or thresholds                         |

> 📌 **A single trigger criterion is sufficient** to trigger the reporting obligation. Criteria are evaluated individually and in combination.

---

## 5. Reporting Timeline

> 📌 **Regulatory Requirement:** Report to OSFI **within 24 hours of detection, or sooner if possible.**

| Milestone                  | Timeframe                                       | Nature                                |
|----------------------------|-------------------------------------------------|---------------------------------------|
| **OSFI Notification**      | ≤ 24 hours from detection                       | **Regulatory Requirement**            |
| Internal escalation target | ≤ 12 hours from detection                       | Organisational Policy (FRFI-specific) |
| Subsequent updates         | Daily (or as new information becomes available) | Regulatory Requirement                |
| Post-incident review       | Within agreed timeline after resolution         | Regulatory Requirement                |

The 24-hour clock starts at **incident detection** — not at root cause determination or full scope confirmation.

### Reporting Recipients

Reports must be sent to **both**:

1. **OSFI Technology Risk Division (TRD):** [TRD-DRT@osfi-bsif.gc.ca](mailto:TRD-DRT@osfi-bsif.gc.ca)
2. **OSFI Lead Supervisor** (FRFI's assigned supervisor)

---

## 6. Incident Reporting and Resolution Form — Appendix II

The mandatory reporting form is the **Incident Reporting and Resolution Form** found in **Appendix II** of the Advisory.

### Mandatory Fields on Initial Report (marked `*` in the form)

| Field                                                     | Notes                                             |
|-----------------------------------------------------------|---------------------------------------------------|
| Incident severity / priority                              | Use internal classification (P1/P2 or equivalent) |
| Business lines, technologies, and locations affected      | List all affected units and systems               |
| Current state and response activities completed           | Summary of what has been done                     |
| Root cause (if known)                                     | Mark "under investigation" if unknown             |
| Internal and external notifications made                  | Insurers, law enforcement, other regulators       |
| External forensics / breach coach / legal counsel engaged | Yes/No + details                                  |

> 📌 **Unknown fields:** Enter *"information not yet available"* and provide best estimates with expected timelines. Do **not** delay submission waiting for complete information.

---

## 7. Subsequent Reporting Requirements

Following the initial report, FRFIs must provide **regular updates** (typically daily) until:

- All mandatory fields in the form have been completed with full, confirmed details; **and**
- The incident is fully **contained and resolved**

Updates should cover:
- Revised severity and scope assessments
- Additional systems, customers, or data affected
- Containment and eradication progress
- Changes to external notifications or resource engagement
- Estimated time to full resolution

---

## 8. Post-Incident Review

Upon full resolution, the FRFI must submit a **Post-Incident Review (PIR) and Lessons Learned Report** to OSFI. The PIR must include:

- Confirmed root cause analysis
- Complete incident timeline
- Effectiveness of detection, response, and recovery actions
- Control failures or gaps exploited
- Remediation actions taken and planned
- Lessons learned and control improvements

> 🏦 **Organisational Policy:** Submit the PIR within **30 calendar days** of incident resolution (unless OSFI specifies an earlier deadline).

---

## 9. When in Doubt

> 📌 *"For incidents that do not align with or contain the specific criteria listed above, or when a FRFI is uncertain, **notification to OSFI is encouraged as a precaution**."*
> — OSFI Incident Reporting Advisory, August 2021

Key principle: **There is no penalty for precautionary reporting.** The regulatory expectation is a bias toward notification. Consult the Lead Supervisor when uncertain.

---

## 10. Relevance to OSFI 24-Hour Incident Reporting

This document **is** the OSFI 24-hour incident reporting obligation. It establishes:

- The legal and supervisory basis for the reporting requirement
- The definition of what must be reported
- The trigger criteria that activate the obligation
- The timeline (24 hours) and process
- The form (Appendix II) to use
- The subsequent and post-incident reporting obligations

> 📌 **This advisory is the primary source document.** All other frameworks (B-13, B-10, E-21, PIPEDA, etc.) intersect with and support this reporting obligation, but the Advisory itself is the definitive statement of the 24-hour requirement.

For the full operational reference, including the 12-hour internal threshold, trigger criteria with detailed guidance, and cross-framework mapping, see:
**[`OSFI_Incident_Reporting_Trigger_Criteria.md`](../OSFI_Incident_Reporting_Trigger_Criteria.md)**

---

## 11. Cross-References

| Document                                | Relationship                                                                         |
|-----------------------------------------|--------------------------------------------------------------------------------------|
| **OSFI B-13**                           | Governs the incident response capability (P15) that operationalises this Advisory    |
| **OSFI B-10**                           | Third-party incidents (B5, B6 criteria) are governed by B-10 contractual obligations |
| **OSFI E-21**                           | Operational resilience; operational risk events that trigger Advisory reporting      |
| **OSFI I&S Guideline**                  | Physical/personnel security incidents may trigger Advisory reporting                 |
| **OSFI Corporate Governance Guideline** | Board escalation expectations feed Criterion C2                                      |
| **PIPEDA DERR**                         | Concurrent reporting obligations to OPC; OPC notification is a C3 trigger criterion  |
| **Quebec Law 25**                       | Concurrent 72-hour CAI notification obligation for Quebec personal data incidents    |
| **Bill C-26**                           | Parallel cyber incident reporting obligation for critical cyber system operators     |

---

*Source: OSFI Technology and Cybersecurity Incident Reporting Advisory (August 13, 2021)*
*URL: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/technology-cyber-security-incident-reporting*
