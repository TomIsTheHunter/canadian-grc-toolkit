# OSFI Technology and Cybersecurity Incident Reporting — Trigger Criteria

> **Document Type:** Internal Compliance Reference
> **Regulatory Source:** OSFI Technology and Cybersecurity Incident Reporting Advisory (August 2021)
> **Audience:** Technology Risk, Cybersecurity, Operational Risk, Compliance, and Governance teams
> **Last Reviewed:** April 2, 2026
> **Owner:** Chief Information Security Officer (CISO) / Technology Risk Management

---

## Table of Contents

1. [Overview](#1-overview)
2. [Definition of a Reportable Incident](#2-definition-of-a-reportable-incident)
3. [Reporting Timeline](#3-reporting-timeline)
4. [Trigger Criteria](#4-trigger-criteria)
5. [Reporting Procedure](#5-reporting-procedure)
6. [Subsequent Reporting](#6-subsequent-reporting)
7. [When in Doubt](#7-when-in-doubt)
8. [Consequences of Non-Reporting](#8-consequences-of-non-reporting)
9. [Related Frameworks](#9-related-frameworks)

---

## 1. Overview

### 1.1 Purpose

This document provides a structured reference for federally regulated financial institutions (FRFIs) to identify, escalate, and report technology and cybersecurity incidents to the Office of the Superintendent of Financial Institutions (OSFI) in accordance with the **OSFI Technology and Cybersecurity Incident Reporting Advisory** (issued August 2021).

The advisory establishes a consistent, proactive reporting expectation across the federal financial sector, ensuring that OSFI has timely situational awareness of technology and cyber threats that could impact FRFIs, the broader financial system, or Canadian consumers.

### 1.2 Applicability

This advisory and the obligations contained herein apply to **all federally regulated financial institutions**, including:

| Institution Type             | Examples                                                                                |
|------------------------------|-----------------------------------------------------------------------------------------|
| **Banks**                    | Schedule I, II, and III banks under the *Bank Act*                                      |
| **Insurance Companies**      | Life, property and casualty, and fraternal insurers under the *Insurance Companies Act* |
| **Trust and Loan Companies** | Entities regulated under the *Trust and Loan Companies Act*                             |
| **Pension Plans**            | Federal pension plans under the *Pension Benefits Standards Act, 1985*                  |

### 1.3 Regulatory Authority

**OSFI** (Office of the Superintendent of Financial Institutions Canada) issues this advisory under its mandate to supervise and regulate FRFIs in order to protect depositors, policyholders, financial institution creditors, and pension plan members, while allowing institutions to compete effectively and take reasonable risks.

- OSFI does **not** require regulatory approval before reporting; reporting is a **mandatory obligation**
- The advisory supplements, but does not replace, existing supervisory communication requirements

### 1.4 Relationship to Other OSFI Guidelines

This advisory operates within a broader OSFI supervisory framework. It should be read and applied in conjunction with:

| Guideline                                            | Relevance to Incident Reporting                                                                                                                              |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **OSFI B-13** — Technology and Cyber Risk Management | Establishes the overarching governance, risk management, and control expectations for technology and cyber risk, within which incident reporting is embedded |
| **OSFI B-10** — Third Party Risk Management          | Governs third-party risk; incidents at vendors or service providers that impact the FRFI are reportable                                                      |
| **OSFI E-21** — Operational Risk Management          | Provides the operational risk framework; technology/cyber incidents are a subset of operational risk events                                                  |
| **OSFI I&S Guideline** — Integrity and Security      | Sets expectations for physical and information security; security breaches triggering this guideline may also require advisory reporting                     |

---

## 2. Definition of a Reportable Incident

### 2.1 Regulatory Definition

The August 2021 advisory defines a reportable technology and cybersecurity incident as:

> **"An incident that has an impact, or the potential to have an impact on the operations of a FRFI, including its confidentiality, integrity, or the availability of its systems and information."**

This definition is intentionally **broad**. Reportability is determined by *actual or potential* impact — not solely by confirmed, realised harm.

### 2.2 Key Change from 2019 Advisory

> ⚠️ **Important:** The August 2021 advisory **removed the "material impact" threshold** that was present in the previous 2019 version of the advisory.

| Advisory Version            | Impact Threshold                                              |
|-----------------------------|---------------------------------------------------------------|
| 2019 Advisory               | Required "material impact" before reporting was triggered     |
| **2021 Advisory (current)** | **Any impact, or *potential* impact** — no materiality filter |

This is a deliberate regulatory shift toward **earlier, precautionary reporting**. FRFIs should not delay reporting while assessing whether an incident is "material."

### 2.3 The CIA Triad in Context

Incidents affecting any element of the **CIA Triad** are within scope:

- **Confidentiality** — Unauthorised access to, or disclosure of, systems or customer data
- **Integrity** — Unauthorised modification, corruption, or destruction of data or systems
- **Availability** — Disruption, degradation, or outage of systems or services

---

## 3. Reporting Timeline

### 3.1 Regulatory Minimum

> 📌 **Regulatory Requirement:** Incidents meeting the trigger criteria **must be reported to OSFI within 24 hours of detection, or sooner if possible.**

This 24-hour window begins at the point of **incident detection** — not confirmation of root cause or full scope assessment.

### 3.2 Internal Organisational Threshold

> 🏦 **Organisational Policy (Internal — Not a Regulatory Requirement):** This organisation has adopted an internal escalation threshold of **12 hours** from detection to OSFI notification preparation. This internal target is stricter than the regulatory minimum and is designed to ensure the organisation comfortably meets the 24-hour regulatory deadline while allowing adequate time for initial information gathering and senior management notification.

| Threshold                             | Hours                  | Owner                      | Authority                    |
|---------------------------------------|------------------------|----------------------------|------------------------------|
| Internal Escalation to CISO / Exec    | ≤ 4 hours              | Incident Manager           | Organisational Policy        |
| **Internal OSFI Notification Target** | **≤ 12 hours**         | **CISO / Technology Risk** | **Organisational Policy**    |
| **Regulatory Reporting Deadline**     | **≤ 24 hours**         | **CISO / Technology Risk** | **OSFI Advisory (Aug 2021)** |
| Subsequent Daily Updates              | Every 24 hours         | Technology Risk            | OSFI Advisory (Aug 2021)     |
| Post-Incident Review Report           | Within agreed timeline | Technology Risk / CISO     | OSFI Advisory (Aug 2021)     |

### 3.3 Incident Timeline Diagram

```
─────────────────────────────────────────────────────────────────────────────────
 INCIDENT LIFECYCLE — OSFI REPORTING TIMELINE
─────────────────────────────────────────────────────────────────────────────────

  T+0h             T+4h           T+12h              T+24h
   │                │               │                  │
   ▼                ▼               ▼                  ▼
[DETECTION]──►[INTERNAL ESC.]──►[OSFI NOTIF.]──►[REGULATORY]──►[DAILY UPDATES]
               CISO + ExecMgmt    Prep & Send        DEADLINE      until resolved
               Trigger IRP        Initial Form                          │
                                  (Appendix II)                         ▼
                                                                [POST-INCIDENT]
                                                                 Review & Lessons
                                                                 Learned Report
─────────────────────────────────────────────────────────────────────────────────
 ◄──── Organisational Policy (12hr) ────►◄── Regulatory Minimum (24hr) ────────►
─────────────────────────────────────────────────────────────────────────────────
```

---

## 4. Trigger Criteria

### 4.1 Summary Table

The following table summarises the trigger criteria groupings. The presence of **one or more** of these characteristics — individually or in combination — triggers the reporting obligation.

> 📌 This list is **non-exhaustive**. An incident need not match every criterion in a group. A single applicable characteristic is sufficient to trigger reporting.

| Group | Category                         | # of Criteria |
|-------|----------------------------------|---------------|
| **A** | Impact-Based Criteria            | 6             |
| **B** | Operational Disruption Criteria  | 6             |
| **C** | Escalation & Governance Criteria | 4             |
| **D** | Severity & Scale Criteria        | 4             |

---

### 4.2 Group A — Impact-Based Criteria

These criteria focus on the *consequences* of the incident — what systems, data, or stakeholders are affected.

| #  | Trigger                                                                                        | Notes                                                                                      |
|----|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| A1 | Potential consequences to other FRFIs or the Canadian financial system                         | Systemic risk indicator; applies even if internal impact is contained                      |
| A2 | Impact to FRFI systems affecting financial market settlement, confirmations, or payments (FMI) | Includes connections to LVTS, ACSS, CDS Clearing, or other Financial Market Infrastructure |
| A3 | Impact to payment services                                                                     | Includes retail payment systems, wire transfers, EFT, card processing                      |
| A4 | Impact to FRFI operations, infrastructure, data, and/or systems                                | Broad operational impact; encompasses core banking, back-office, and support systems       |
| A5 | Impact to confidentiality, integrity, or availability of customer information                  | Privacy-sensitive; may also trigger PIPEDA DERR and/or Quebec Law 25 obligations           |
| A6 | Operational impact to key/critical systems, infrastructure, or data                            | Applies to systems designated as critical in the FRFI's Business Impact Analysis (BIA)     |

**Detailed Bullets:**

- **A1:** Consider whether the incident could cascade to interconnected institutions, financial market infrastructures, or shared service providers.
- **A2:** Any disruption to settlement finality, trade confirmation, or payment clearing systems requires immediate escalation.
- **A3:** Retail payment disruptions affecting customers, merchants, or counterparties — including mobile banking or debit/credit card processing outages.
- **A4:** Incidents impacting corporate networks, data centres, cloud environments, or enterprise applications (ERP, CRM, core banking platform).
- **A5:** Unauthorised access to, exfiltration of, or corruption of personal information or account data. Note: privacy breach reporting to the OPC under PIPEDA may run concurrently.
- **A6:** Refer to the organisation's Critical System Register and BIA for the list of systems designated as "key" or "critical."

---

### 4.3 Group B — Operational Disruption Criteria

These criteria focus on *disruptions to operations* — service outages, infrastructure failures, and third-party impacts.

| #  | Trigger                                                                 | Notes                                                                                                    |
|----|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| B1 | Disruptions to business systems and/or operations                       | Includes partial or full outages of any business-facing application or service                           |
| B2 | Utility or data centre outages                                          | Power, cooling, physical facility failures affecting IT operations                                       |
| B3 | Loss or degradation of connectivity                                     | Network failures, ISP outages, WAN/LAN disruptions affecting business continuity                         |
| B4 | Disaster recovery (DR) teams or plans have been activated               | DR activation is itself an explicit trigger — report upon activation                                     |
| B5 | Disaster declaration made by a third-party vendor that impacts the FRFI | Third-party DR declarations that affect services or data the FRFI relies upon                            |
| B6 | Impact to a third party affecting the FRFI                              | Incidents at outsourced service providers, cloud providers, or SaaS vendors that degrade FRFI operations |

**Detailed Bullets:**

- **B1:** Applies regardless of whether customers are directly affected. Internal system disruptions impacting staff processing or back-office operations are included.
- **B2:** Includes co-location and cloud data centre incidents; consider vendor-reported incidents for hosted environments.
- **B3:** Evaluate both primary and backup connectivity. Sustained degradation (not just momentary packet loss) is in scope.
- **B4:** The act of activating DR plans — regardless of whether systems have fully failed — constitutes a trigger event.
- **B5:** Obtain and monitor third-party vendor contractual obligations to notify of disaster declarations; these must be flowed up to OSFI promptly.
- **B6:** Consistent with OSFI B-10 obligations; FRFIs remain responsible for the technology and cyber risks introduced by their third-party ecosystem.

---

### 4.4 Group C — Escalation & Governance Criteria

These criteria are triggered by the *internal escalation posture* of the organisation — how the institution has responded to the incident.

| #  | Trigger                                                                                                             | Notes                                                                                                           |
|----|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| C1 | FRFI's technology or cyber incident management team or protocols have been activated                                | Activation of the IRP, Cyber Incident Response Plan, or equivalent is a standalone trigger                      |
| C2 | Incident reported to the Board of Directors or Senior/Executive Management                                          | Board/Exec notification signals recognised severity; report to OSFI at the same time                            |
| C3 | Reported to the Office of the Privacy Commissioner and/or other local or foreign regulatory or supervisory agencies | Concurrent regulatory reporting to other bodies (e.g., OPC, FINTRAC, SEC, FCA) triggers OSFI notification       |
| C4 | Cyber insurance claim has been initiated                                                                            | Insurance claim initiation signals assessed impact severity sufficient to warrant external financial engagement |

**Detailed Bullets:**

- **C1:** "Protocols activated" includes convening a war room, calling in the incident response retainer, or issuing an incident ticket classified at high/critical severity.
- **C2:** Do not wait for the board/executive briefing to conclude before notifying OSFI. Concurrent notification is expected.
- **C3:** If the organisation is required to notify any other domestic or international regulator, OSFI must be notified at the same time or earlier.
- **C4:** The mere act of initiating a claim — not awaiting insurer approval — is the trigger event.

---

### 4.5 Group D — Severity & Scale Criteria

These criteria relate to the *assessed severity* of the incident or its *scale of impact*.

| #  | Trigger                                                                                                 | Notes                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| D1 | FRFI-assessed high or critical severity; Priority/Severity/Tier 1 or 2 based on internal classification | Use the organisation's formal incident severity matrix; P1/P2 or Sev1/Sev2 are explicit triggers           |
| D2 | Number of external customers impacted is growing                                                        | A dynamic, expanding blast radius is a key trigger — report before full scope is known                     |
| D3 | Negative reputational impact is imminent (e.g., public and/or media disclosure expected)                | Proactive media or social media coverage, or anticipated press queries, must be reported before disclosure |
| D4 | Breach of internal risk appetite or thresholds                                                          | Incidents that breach documented risk appetite statements, KRIs, or control thresholds require reporting   |

**Detailed Bullets:**

- **D1:** The organisation's Incident Severity Classification Matrix (Tier 1/Sev1 = most severe) provides the authoritative classification. Any P1 or P2 incident must be assessed against these criteria.
- **D2:** "Growing" customer impact — even if current numbers are small — signals potential systemic exposure. Report while numbers are still low; do not wait for stabilisation.
- **D3:** If communications teams are preparing press statements or social media responses, OSFI notification should already have occurred.
- **D4:** Reference the organisation's Risk Appetite Statement (RAS) and Key Risk Indicators (KRIs). A breach of any technology or cyber risk threshold is a reporting trigger.

---

## 5. Reporting Procedure

### 5.1 Who to Notify

Reports must be submitted to **both** of the following:

| Recipient                               | Contact                                                                             |
|-----------------------------------------|-------------------------------------------------------------------------------------|
| **OSFI Technology Risk Division (TRD)** | [TRD-DRT@osfi-bsif.gc.ca](mailto:TRD-DRT@osfi-bsif.gc.ca)                           |
| **OSFI Lead Supervisor**                | As assigned to the FRFI (contact information on file with Chief Compliance Officer) |

> ⚠️ Reporting to only one recipient does **not** satisfy the obligation. Both contacts must be notified simultaneously.

### 5.2 Reporting Form

Use the **Incident Reporting and Resolution Form** provided in **Appendix II** of the OSFI Technology and Cybersecurity Incident Reporting Advisory (August 2021).

- The form must accompany or follow the initial notification
- All fields marked with an **asterisk (\*)** are mandatory on the initial report

### 5.3 Mandatory Fields on Initial Report

The following fields are required on the initial report submission (marked `*` in Appendix II):

| Field                                                 | Description                                                                            |
|-------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Incident Severity / Priority**                      | Assessed severity level (e.g., P1/Critical, P2/High) using internal classification     |
| **Business Lines, Technologies & Locations Affected** | Identify affected business units, systems, applications, geographies                   |
| **Current State & Response Activities**               | Describe the current incident status and what has been done so far                     |
| **Root Cause (if known)**                             | Provide best available root cause; mark as "under investigation" if not yet determined |
| **Internal & External Notifications**                 | List all parties notified: insurers, law enforcement, regulators, legal counsel        |
| **External Resources Engaged**                        | Indicate if external forensics, a breach coach, or legal counsel has been engaged      |

> 📌 **If information is unavailable at time of initial reporting:** Do **not** delay submission. Indicate *"information not yet available"* for unknown fields and provide best estimates with expected timelines for follow-up details.

---

## 6. Subsequent Reporting

### 6.1 Daily Updates

Following the initial report, the FRFI must provide **regular updates — typically daily** — to both the TRD and the Lead Supervisor as new information becomes available.

Updates should address:
- Changes to the severity assessment or scope of impact
- Additional systems, data, or customers affected
- Progress on containment, eradication, and recovery activities
- Revised root cause analysis
- External notifications made since the last update
- Estimated time to full resolution

### 6.2 Continuation of Reporting

Subsequent reporting obligations continue **until:**

- All mandatory fields in the Incident Reporting and Resolution Form have been completed with full details; **and**
- The incident has been fully **contained and resolved**

### 6.3 Post-Incident Review Report

Upon resolution, the FRFI must submit a **Post-Incident Review (PIR) and Lessons Learned Report** to OSFI. This report should include:

- Confirmed root cause analysis
- Full timeline of the incident and response
- Effectiveness of controls that failed or were bypassed
- Remediation actions taken and planned
- Control improvements and prevention measures
- Lessons learned and organisational takeaways

> 🏦 **Organisational Policy:** The post-incident review report should be submitted within **30 calendar days** of incident resolution, unless OSFI specifies an earlier deadline.

---

## 7. When in Doubt

> 📌 *"For incidents that do not align with or contain the specific criteria listed above, or when a FRFI is uncertain, **notification to OSFI is encouraged as a precaution**."*
> — OSFI Technology and Cybersecurity Incident Reporting Advisory, August 2021

### 7.1 Guiding Principle

The regulatory expectation is a **bias toward reporting**. The cost of over-reporting is significantly lower than the supervisory and reputational consequences of under-reporting. When assessing whether an incident meets trigger criteria:

- **Err on the side of reporting** when uncertain
- **Do not delay** pending full root cause determination
- **Consult your Lead Supervisor** proactively — OSFI welcomes early, informal dialogue

### 7.2 Escalation Path When Uncertain

```
Incident Identified → Trigger Criteria Review → Uncertain?
                                                      │
                                              ┌───────┴────────┐
                                              │                │
                                     Consult CISO /     Contact Lead
                                     Technology Risk    Supervisor
                                     Team               (OSFI)
                                              │                │
                                              └───────┬────────┘
                                                      │
                                              Report as Precaution
                                              (No penalty for
                                               precautionary reporting)
```

---

## 8. Consequences of Non-Reporting

Failure to report a qualifying incident within the required timeframe, or failure to report at all, may result in OSFI taking the following supervisory actions:

| Consequence                         | Description                                                                                                                          |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Increased Supervisory Oversight** | OSFI may increase the frequency and intensity of supervisory activities, including on-site reviews and targeted examinations         |
| **Enhanced Monitoring Activities**  | Additional regulatory monitoring requirements, including more frequent reporting obligations on technology and cyber risk management |
| **Watch-Listing**                   | The FRFI may be placed on OSFI's internal watch list, indicating elevated supervisory concern                                        |
| **Staging**                         | The FRFI's Composite Risk Rating (CRR) may be adversely staged, affecting overall supervisory assessment and public ratings          |

> ⚠️ Non-reporting or late reporting may also affect the FRFI's OSFI supervisory rating and could be cited in supervisory letters or OSFI's annual assessment of the institution.

---

## 9. Related Frameworks

The following table cross-references the OSFI Technology and Cybersecurity Incident Reporting Advisory to related regulatory frameworks, guidelines, and standards applicable to federally regulated financial institutions in Canada.

| Framework / Standard                                                                            | Type                           | Relevance to Incident Reporting                                                                                           | Key Alignment                                                                                                            |
|-------------------------------------------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **OSFI B-13** — Technology and Cyber Risk Management                                            | OSFI Guideline                 | Primary governance framework within which incident reporting operates                                                     | Domain 6: Cybersecurity; incident response and reporting obligations embedded in B-13 expectations                       |
| **OSFI B-10** — Third Party Risk Management                                                     | OSFI Guideline                 | Third-party incidents (B-criteria) must be managed and reported per B-10 obligations                                      | Requires FRFIs to ensure third parties notify of incidents; FRFI remains accountable for reporting to OSFI               |
| **OSFI E-21** — Operational Risk Management                                                     | OSFI Guideline                 | Technology/cyber incidents are operational risk events; loss data reporting obligations may run concurrently              | Incident classification, escalation, and root cause are shared processes                                                 |
| **OSFI I&S Guideline** — Integrity and Security                                                 | OSFI Guideline                 | Physical security and personnel-related incidents that affect technology systems may trigger advisory reporting           | Cross-cutting obligation for insider threat or physical breach scenarios                                                 |
| **Bill C-27** — Consumer Privacy Protection Act                                                 | Federal Legislation (proposed) | Proposes enhanced breach notification obligations for private-sector organisations                                        | Aligns with and strengthens PIPEDA breach notification; concurrent reporting may be required                             |
| **Bill C-26** — Critical Cyber Systems Protection Act                                           | Federal Legislation (proposed) | Establishes mandatory cyber incident reporting for operators of critical cyber systems (CCS) in designated sectors        | FRFIs operating critical cyber systems will have parallel federal reporting obligations under C-26                       |
| **PIPEDA DERR** — Breach of Security Safeguards Regulations                                     | Federal Regulation             | Mandatory notification to OPC and affected individuals for breaches posing "real risk of significant harm"                | Incidents meeting OSFI reporting criteria (esp. A5) may simultaneously trigger PIPEDA DERR reporting                     |
| **Quebec Law 25** — Act Respecting the Protection of Personal Information in the Private Sector | Provincial Legislation         | Mandatory 72-hour breach notification to Commission d'accès à l'information (CAI) for "confidentiality incidents"         | Incidents affecting Quebec residents' personal data trigger provincial obligations concurrently                          |
| **ISO 27001** — ISMS Standard                                                                   | International Standard         | Provides the Information Security Management System framework; incident management is a core control domain               | Clause 6.1.2 (risk treatment), Annex A.16 (Information Security Incident Management)                                     |
| **ISO 27002** — Security Controls                                                               | International Standard         | Control guidance for incident detection, response, and learning from incidents                                            | Controls 5.24–5.28 cover incident management planning, reporting, assessment, response, and lessons learned              |
| **NIST CSF** — Cybersecurity Framework                                                          | Industry Framework             | Maps incident reporting to the Respond and Recover functions                                                              | RS.CO (Response Communications) and RC.CO (Recovery Communications) functions directly address regulatory notification   |
| **SOC 2 CC6** — Logical and Physical Access Controls                                            | Audit Standard                 | SOC 2 Trust Service Criteria; security incidents must be identified, documented, and reported per CC7 (System Operations) | CC7.3–CC7.5 cover incident response and notification; audit evidence of OSFI reporting supports SOC 2 compliance posture |

---

*This document is maintained by the Technology Risk Management function and should be reviewed annually or following any material change to the regulatory reporting framework. For questions, contact the Chief Information Security Officer or the Compliance team.*

*Source: OSFI Technology and Cybersecurity Incident Reporting Advisory, August 2021 — [https://www.osfi-bsif.gc.ca](https://www.osfi-bsif.gc.ca)*
