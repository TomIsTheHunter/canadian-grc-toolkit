---
Document:        NIST Cybersecurity Framework 2.0 (CSF 2.0)
Issuer:          National Institute of Standards and Technology (NIST), U.S. Department of Commerce
Effective Date:  February 26, 2024
Last Verified:   April 2, 2026
Status:          Active
Type:            Voluntary / Best Practice — Industry Framework
Official URL:    https://www.nist.gov/cyberframework
---

# NIST Cybersecurity Framework 2.0 (CSF 2.0)

> **Document Type:** Industry Framework
> **Issuer:** National Institute of Standards and Technology (NIST)
> **Version:** CSF 2.0 (released February 26, 2024; supersedes CSF 1.1 from 2018)
> **Applies To:** Voluntary adoption by any organisation; widely used by FRFIs as a cybersecurity maturity benchmark and OSFI CSSA reference

---

## Table of Contents

1. [Overview — What Changed from CSF 1.1 to CSF 2.0](#1-overview--what-changed-from-csf-11-to-csf-20)
2. [The Six Functions](#2-the-six-functions)
3. [GOVERN Function (New in CSF 2.0)](#3-govern-function-new-in-csf-20)
4. [IDENTIFY Function](#4-identify-function)
5. [PROTECT Function](#5-protect-function)
6. [DETECT Function](#6-detect-function)
7. [RESPOND Function](#7-respond-function)
8. [RECOVER Function](#8-recover-function)
9. [CSF 2.0 and OSFI B-13 Alignment](#9-csf-20-and-osfi-b-13-alignment)
10. [CSF as a Maturity Benchmark for Incident Response Capability](#10-csf-as-a-maturity-benchmark-for-incident-response-capability)
11. [Relevance to OSFI 24-Hour Incident Reporting](#11-relevance-to-osfi-24-hour-incident-reporting)
12. [Cross-References](#12-cross-references)

---

## 1. Overview — What Changed from CSF 1.1 to CSF 2.0

CSF 2.0 is a significant revision of the original framework, reflecting a decade of implementation experience and the evolution of the threat landscape.

### Key Changes from CSF 1.1

| Change                      | Description                                                                                                                                                         |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New GOVERN Function**     | A sixth function was added (GOVERN) to address cybersecurity governance, risk management strategy, and supply chain risk — previously spread across other functions |
| **Expanded scope**          | CSF 2.0 is designed for all organisations, not just critical infrastructure (as originally scoped)                                                                  |
| **Supply chain risk**       | Explicitly addressed in GOVERN; CSF 2.0 acknowledges the role of third-party risks                                                                                  |
| **Implementation Examples** | New implementation examples and quick-start guides for different organisation types                                                                                 |
| **Community Profiles**      | Standardised profiles for common organisation types to support comparative benchmarking                                                                             |

---

## 2. The Six Functions

CSF 2.0 organises cybersecurity activities into **six core functions**:

| Function     | Acronym | Description                                                                                               |
|--------------|---------|-----------------------------------------------------------------------------------------------------------|
| **Govern**   | GV      | Establish and monitor the organisation's cybersecurity risk management strategy, expectations, and policy |
| **Identify** | ID      | Understand the organisation's cybersecurity risk to systems, people, assets, data, and capabilities       |
| **Protect**  | PR      | Implement safeguards to manage cybersecurity risks                                                        |
| **Detect**   | DE      | Find and analyse possible cybersecurity attacks and compromises                                           |
| **Respond**  | RS      | Take action regarding a detected cybersecurity incident                                                   |
| **Recover**  | RC      | Restore assets and operations affected by a cybersecurity incident                                        |

Each function is subdivided into **Categories** (higher-level outcomes) and **Subcategories** (specific technical and process-level activities).

---

## 3. GOVERN Function (New in CSF 2.0)

The GOVERN function is the most significant structural change in CSF 2.0. It addresses the organisational context and governance structures that enable effective cybersecurity:

| Category                                               | Description                                                                                                                                                   |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GV.OC — Organisational Context**                     | The organisation's mission, stakeholder expectations, dependencies, and legal/regulatory requirements are understood and inform cybersecurity risk management |
| **GV.RM — Risk Management Strategy**                   | Priorities, constraints, risk tolerance, and assumptions are established to support cybersecurity risk decisions                                              |
| **GV.RR — Roles, Responsibilities, Authorities**       | Cybersecurity roles and responsibilities are established, communicated, and enforced                                                                          |
| **GV.PO — Policy**                                     | Cybersecurity policy is established, communicated, and enforced                                                                                               |
| **GV.OV — Oversight**                                  | Results of organisation-wide cybersecurity risk management activities inform and improve the programme                                                        |
| **GV.SC — Cybersecurity Supply Chain Risk Management** | Cyber supply chain risk is identified, prioritised, managed, and monitored throughout the supply chain lifecycle                                              |

### GOVERN and OSFI B-13

The GOVERN function maps directly to **OSFI B-13 Domain 1 (Governance and Risk Management)**, Principles 1–5. The OSFI Annual Cybersecurity Self-Assessment (CSSA) governance section aligns closely with GV categories.

---

## 4. IDENTIFY Function

The IDENTIFY function helps organisations understand their cybersecurity risk environment:

| Category                     | Key Subcategories                                                                                      | B-13 Alignment                                                   |
|------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| **ID.AM — Asset Management** | Inventory of hardware, software, data, and network assets                                              | B-13 P6 (Technology Asset Management)                            |
| **ID.RA — Risk Assessment**  | Identify and prioritise cybersecurity threats and vulnerabilities                                      | B-13 P2 (Risk Appetite), P12 (Threat & Vulnerability Management) |
| **ID.IM — Improvement**      | Improvements are identified and prioritised through evaluations, lessons learned, and risk assessments | B-13 P16 (Recovery and Lessons Learned)                          |

---

## 5. PROTECT Function

The PROTECT function implements safeguards to reduce the likelihood and impact of cybersecurity events:

| Category                                                         | Key Subcategories                                                       | B-13 Alignment                                            |
|------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| **PR.AA — Identity Management, Authentication & Access Control** | Identity management, MFA, least privilege, PAM                          | B-13 P13 (Security Architecture)                          |
| **PR.AT — Awareness and Training**                               | Security awareness training; role-based training for privileged users   | B-13 P5 (Talent and Culture)                              |
| **PR.DS — Data Security**                                        | Encryption, DLP, data classification, backup                            | B-13 P10 (Data Management)                                |
| **PR.PS — Platform Security**                                    | Configuration management, patch management, secure software development | B-13 P8 (Change Management), P12 (Threat & Vulnerability) |
| **PR.IR — Technology Infrastructure Resilience**                 | BCP/DR, redundancy, network segmentation                                | B-13 P9 (BCP/DR), P13 (Security Architecture)             |

---

## 6. DETECT Function

The DETECT function enables timely discovery of cybersecurity events:

| Category                           | Key Subcategories                                                        | B-13 Alignment                                                    |
|------------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------|
| **DE.AE — Adverse Event Analysis** | SIEM, log analysis, correlation of events from multiple sources          | B-13 P14 (Cybersecurity Monitoring)                               |
| **DE.CM — Continuous Monitoring**  | Network, endpoint, and user behaviour monitoring; vulnerability scanning | B-13 P14 (Cybersecurity Monitoring), P12 (Threat & Vulnerability) |

### Why DETECT Matters for 24-Hour Reporting

The 24-hour OSFI clock starts at **detection**. DE.AE and DE.CM capabilities directly determine:
- How quickly an incident is identified (T+0h)
- Whether an incident is detected at all (detection gaps can result in extended dwell time before OSFI notification is even possible)

A mature DETECT function dramatically improves the organisation's ability to meet the 24-hour reporting window.

---

## 7. RESPOND Function

The response function takes action regarding a detected cybersecurity incident:

| Category                                                  | Key Subcategories                                                 | B-13 / Advisory Alignment                                |
|-----------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------|
| **RS.MA — Incident Management**                           | Execute incident response plan; coordinate with stakeholders      | B-13 P15 (Incident Response); Advisory Appendix II       |
| **RS.AN — Incident Analysis**                             | Forensic analysis; root cause investigation; impact assessment    | Advisory mandatory fields (root cause, affected systems) |
| **RS.CO — Incident Response Reporting and Communication** | Report incidents to stakeholders, regulators, and law enforcement | **OSFI Advisory 24-hour reporting obligation**           |
| **RS.MI — Incident Mitigation**                           | Contain the incident; reduce further impact                       | Advisory daily updates                                   |

### RS.CO — Regulatory Communication is a CSF Core Category

**RS.CO** (Response Communications) explicitly includes regulatory notification as a subcategory. CSF 2.0 recognises that **notifying regulators promptly is a core incident response activity** — not an afterthought. This directly reinforces the OSFI Advisory 24-hour reporting expectation.

---

## 8. RECOVER Function

The RECOVER function restores affected assets and operations:

| Category                                     | Key Subcategories                                             | B-13 / Advisory Alignment                    |
|----------------------------------------------|---------------------------------------------------------------|----------------------------------------------|
| **RC.RP — Incident Recovery Plan Execution** | Execute recovery plan; prioritise critical system restoration | B-13 P9 (BCP/DR), P16 (Recovery)             |
| **RC.CO — Incident Recovery Communication**  | Communicate recovery status to stakeholders and regulators    | Advisory daily updates; post-incident report |

### RECOVER and Post-Incident Review

RC.CO includes communicating with regulators during the recovery phase — corresponding to the OSFI Advisory's requirement for daily updates and the post-incident review report. A mature RECOVER function will have a structured process for submitting these updates.

---

## 9. CSF 2.0 and OSFI B-13 Alignment

The table below maps NIST CSF 2.0 functions to OSFI B-13 domains and principles:

| CSF 2.0 Function | OSFI B-13 Domain / Principle                                                             |
|------------------|------------------------------------------------------------------------------------------|
| **GOVERN**       | Domain 1 (Governance and Risk Management) — P1–P5                                        |
| **IDENTIFY**     | P6 (Asset Management), P2 (Risk Appetite), P12 (Threat & Vulnerability)                  |
| **PROTECT**      | Domain 2 (Technology Operations & Resilience) — P8, P9, P10; P13 (Security Architecture) |
| **DETECT**       | P14 (Cybersecurity Monitoring and Detection)                                             |
| **RESPOND**      | P15 (Incident Response)                                                                  |
| **RECOVER**      | P16 (Recovery and Lessons Learned)                                                       |

### OSFI Cybersecurity Self-Assessment (CSSA)

OSFI's **annual Cybersecurity Self-Assessment** uses a maturity model that closely parallels the NIST CSF functions. FRFIs completing the CSSA essentially assess their maturity against NIST CSF-aligned capabilities. CSF 2.0 can serve as the underlying framework that FRFIs use to **improve their CSSA scores** by building capability in each function.

---

## 10. CSF as a Maturity Benchmark for Incident Response Capability

CSF 2.0 provides a **maturity tiering** concept (formerly "Tiers") that organisations can use to assess and improve their cybersecurity posture:

| Maturity Level             | Description                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------------|
| **Partial (Tier 1)**       | Ad hoc, reactive practices; limited awareness of risk; no formal incident response plan                      |
| **Risk-Informed (Tier 2)** | Risk management practices exist but are not consistently applied; incident response exists but is not tested |
| **Repeatable (Tier 3)**    | Formal, consistently applied risk management and incident response; regularly tested; reported to governance |
| **Adaptive (Tier 4)**      | Continuously improving; learns from incidents; integrates threat intelligence; adaptive to changing threats  |

For OSFI regulatory compliance, FRFIs should target at least **Tier 3** (Repeatable) for incident response capabilities:
- Formal, documented, and tested Cyber Incident Response Plan
- Defined escalation procedures including regulatory notification
- Regular tabletop exercises simulating OSFI notification scenarios
- Lessons learned integrated into programme improvements

---

## 11. Relevance to OSFI 24-Hour Incident Reporting

### 11.1 DETECT → RESPOND → 24-Hour Window

The CSF functions create a clear cause-and-effect chain for OSFI reporting:

```
DETECT (DE.AE, DE.CM)
    ↓ Incident detected (T+0h — starts the 24-hour clock)
RESPOND (RS.MA)
    ↓ Incident confirmed and IRP activated (Criterion C1)
RESPOND (RS.AN)
    ↓ Initial assessment: severity, scope, impacted systems
RESPOND (RS.CO)
    ↓ OSFI notification sent (≤ 24 hours, target ≤ 12 hours internal)
RECOVER (RC.CO)
    ↓ Daily updates to OSFI during recovery
RECOVER (RC.CO) + IDENTIFY (ID.IM)
    ↓ Post-incident review and lessons learned report to OSFI
```

### 11.2 RS.CO — The CSF Category for Regulatory Notification

NIST CSF 2.0 RS.CO (Incident Response Reporting and Communication) explicitly addresses regulatory notification:
- RS.CO-3: Information is shared with designated internal and external stakeholders
- This directly includes OSFI (as the FRFI's primary prudential regulator) under the 24-hour Advisory

### 11.3 CSF Maturity Gaps Create Regulatory Reporting Risk

An organisation that is only **Tier 1 or Tier 2** in DETECT and RESPOND functions faces significant OSFI regulatory risk:
- Weak detection means incidents may not be discovered quickly (compressing or missing the 24-hour window)
- Informal response procedures mean regulatory notification may be overlooked or delayed
- Absence of tested escalation procedures means the 12-hour internal threshold and 24-hour OSFI deadline may not be met

OSFI's CSSA supervisory assessment effectively measures CSF maturity — a CSSA result indicating weak DETECT/RESPOND capability is a supervisory concern that could affect the FRFI's composite risk rating.

> 📌 **Summary:** NIST CSF 2.0 provides the maturity benchmark framework within which OSFI B-13 and the Incident Reporting Advisory operate. Strong DETECT and RESPOND function maturity (Tier 3–4) is the practical prerequisite for consistently meeting the 24-hour OSFI reporting obligation. FRFIs should map their IRP directly to CSF RESPOND function categories, with RS.CO explicitly embedding the OSFI notification requirement.

---

## 12. Cross-References

| Document                             | Relationship                                                                                                         |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **OSFI B-13**                        | B-13 maps closely to CSF 2.0 functions; OSFI CSSA uses CSF-aligned maturity assessment                               |
| **OSFI Incident Reporting Advisory** | RS.CO (Response Communications) directly embeds the 24-hour OSFI notification requirement                            |
| **OSFI E-21**                        | RECOVER function aligns with E-21 operational resilience and critical operations continuity                          |
| **OSFI Corporate Governance**        | GOVERN function aligns with OSFI Corporate Governance Guideline and B-13 governance domain                           |
| **ISO 27001 / 27002**                | NIST CSF and ISO 27001 are complementary; both can be used simultaneously; mapping documents are available from NIST |
| **SOC 2**                            | NIST CSF DETECT function aligns with SOC 2 CC7 (System Operations); PROTECT function aligns with CC6                 |
| **Bill C-26**                        | CCSPA Cybersecurity Programme requirements can be structured using the NIST CSF as an organising framework           |

---

*Source: NIST Cybersecurity Framework 2.0 (CSF 2.0)*
*Released: February 26, 2024*
*URL: https://www.nist.gov/cyberframework*
