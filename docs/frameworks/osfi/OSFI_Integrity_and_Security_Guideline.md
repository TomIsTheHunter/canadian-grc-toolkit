---
Document:        OSFI Integrity and Security Guideline
Issuer:          Office of the Superintendent of Financial Institutions (OSFI)
Effective Date:  January 31, 2024 (Action Plan due July 31, 2024)
Last Verified:   April 2, 2026
Status:          Active
Type:            Mandatory – FRFI
Official URL:    https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/integrity-security-guideline
---

# OSFI Integrity and Security Guideline

> **Document Type:** Regulatory Guideline
> **Issuer:** OSFI
> **Applies To:** All federally regulated financial institutions (FRFIs) and federally regulated pension plans (FRPPs)
> **Released:** January 31, 2024
> **Action Plan Submission Deadline:** July 31, 2024

---

## Table of Contents

1. [Overview](#1-overview)
2. [Scope and Applicability](#2-scope-and-applicability)
3. [Integrity Expectations](#3-integrity-expectations)
4. [Security Expectations](#4-security-expectations)
5. [Physical Security Controls](#5-physical-security-controls)
6. [Logical Security Controls](#6-logical-security-controls)
7. [Personnel Security](#7-personnel-security)
8. [Action Plan Requirement](#8-action-plan-requirement)
9. [Relationship to OSFI B-13](#9-relationship-to-osfi-b-13)
10. [Relevance to OSFI 24-Hour Incident Reporting](#10-relevance-to-osfi-24-hour-incident-reporting)
11. [Cross-References](#11-cross-references)

---

## 1. Overview

The OSFI Integrity and Security (I&S) Guideline establishes expectations for **integrity** and **security** at FRFIs and FRPPs. Released on January 31, 2024, this guideline addresses the security of FRFI people, assets, and information — encompassing physical security, logical access controls, and personnel security — with a particular focus on preventing infiltration by bad actors (foreign state-sponsored or otherwise) and insider threats.

The I&S Guideline is a **companion to OSFI B-13** (Technology and Cyber Risk Management). While B-13 addresses the broad technology and cyber risk framework, the I&S Guideline focuses specifically on:
- **Integrity** of the FRFI as an institution (resistance to infiltration and undue influence)
- **Security** of physical premises, information systems, and personnel

### Regulatory Context

The I&S Guideline reflects OSFI's heightened concern about:
- Foreign state-sponsored interference in the Canadian financial system
- Insider threats and personnel security risks
- Physical security vulnerabilities at FRFI facilities
- Logical access control failures enabling unauthorised access

---

## 2. Scope and Applicability

| Entity Type                                                          | Applicability                                                                        |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **All FRFIs** — banks, insurance companies, trust and loan companies | Full application of I&S expectations                                                 |
| **Federally Regulated Pension Plans (FRPPs)**                        | Proportionate application of relevant I&S expectations                               |
| **Subsidiaries and affiliates**                                      | I&S expectations cascade to subsidiaries where the FRFI has oversight responsibility |

The guideline applies to **all business lines, geographies, and operations** of the FRFI, including operations in foreign jurisdictions.

---

## 3. Integrity Expectations

### 3.1 Definition of Integrity

In the I&S Guideline context, **integrity** refers to the FRFI's ability to:
- Operate free from undue influence or control by foreign state actors or organised crime
- Maintain the trustworthiness and reliability of its people, processes, and systems
- Resist infiltration of its leadership, operations, or systems by bad actors

### 3.2 Governance of Integrity Risks

- **Board accountability:** The Board must actively consider integrity risks in its governance oversight
- **Senior Management:** Must maintain awareness of integrity threats and ensure appropriate controls
- **Due diligence:** Enhanced due diligence on persons in positions of trust (board members, executives, senior staff)

### 3.3 Tone at the Top

FRFIs are expected to foster a culture where:
- Integrity concerns are reported without fear of retaliation
- Employees understand their obligation to report suspicious activity (including potential state-sponsored interference)
- Ethical conduct is embedded in the FRFI's values and performance management

---

## 4. Security Expectations

The I&S Guideline covers three intersecting security domains:

| Domain                 | Scope                                                                  |
|------------------------|------------------------------------------------------------------------|
| **Physical Security**  | Protection of FRFI premises, data centres, and physical assets         |
| **Logical Security**   | Access controls for information systems, networks, and data            |
| **Personnel Security** | Background screening, access management, and insider threat programmes |

These three domains are interdependent — a failure in one domain (e.g., inadequate personnel screening) can undermine controls in another (e.g., a malicious insider bypasses logical access controls).

---

## 5. Physical Security Controls

### 5.1 Facility Security

FRFIs must implement **layered physical security controls** at all facilities handling sensitive information or critical infrastructure:

| Control Type                     | Examples                                                                                                |
|----------------------------------|---------------------------------------------------------------------------------------------------------|
| **Perimeter Security**           | Fencing, barriers, controlled vehicle access, security checkpoints                                      |
| **Access Control**               | Badge access, biometric authentication, visitor management, mantrap/airlock entries for sensitive areas |
| **Surveillance**                 | CCTV coverage of critical areas; monitored security operations                                          |
| **Environmental Controls**       | Fire suppression, water detection, temperature monitoring in data centres and server rooms              |
| **Physical Intrusion Detection** | Alarms, motion sensors, tamper detection for critical equipment                                         |

### 5.2 Data Centre and Server Room Security

Enhanced physical security requirements for data centres:
- Restricted access with multifactor authentication (badge + biometric)
- Separation of critical system areas from general IT areas
- Audit trails of physical access — logged and reviewed
- Media handling and destruction controls for decommissioned hardware

### 5.3 Remote Work Considerations

With increased remote and hybrid work, FRFIs must consider:
- Physical security expectations for employees handling sensitive information at home
- Secure disposal of documents and devices in home environments
- Clear desk / clear screen policies applicable to remote work settings

---

## 6. Logical Security Controls

### 6.1 Identity and Access Management (IAM)

The I&S Guideline reinforces expectations for **logical access controls** aligned with B-13 Principle 13:

| IAM Control                            | Requirement                                                                                          |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| **Least Privilege**                    | Users receive only the minimum access required for their role                                        |
| **Segregation of Duties**              | Critical functions must not be performed by a single person without oversight                        |
| **Privileged Access Management (PAM)** | Enhanced controls for administrator and privileged accounts (just-in-time access, session recording) |
| **Multi-Factor Authentication (MFA)**  | Required for remote access and all privileged account use                                            |
| **Access Reviews**                     | Periodic (at minimum annual) review and recertification of all user access                           |
| **Joiners / Movers / Leavers**         | Timely provisioning and de-provisioning of access aligned with HR lifecycle events                   |

### 6.2 Access Monitoring

- Monitoring of privileged user activity for anomalous behaviour
- Alerting on unusual access patterns (off-hours access, bulk data downloads, access to systems outside normal scope)
- Integration of access monitoring with the SIEM/SOC environment

---

## 7. Personnel Security

### 7.1 Background Screening

FRFIs must conduct appropriate **background screening** for personnel in positions of trust:

| Screening Element                                 | Applicability                                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Criminal record check**                         | All employees with access to sensitive systems or customer data                                                                 |
| **Credit check**                                  | Roles with financial responsibility or elevated access to financial systems                                                     |
| **Identity verification**                         | All employees; enhanced verification for executives and board members                                                           |
| **Reference and employment history verification** | All employees                                                                                                                   |
| **Enhanced screening**                            | Senior management, Board members, privileged IT users — may include security clearance or third-party enhanced background check |

### 7.2 Ongoing Personnel Risk Monitoring

Background screening at hire is insufficient — FRFIs must monitor for emerging personnel security risks:
- Periodic rescreening for high-risk roles (e.g., every 3–5 years, or triggered by event)
- Monitoring for indicators of insider threat (financial stress, behavioural changes, access anomalies)
- Processes for receiving and responding to personnel security concerns raised by employees

### 7.3 Insider Threat Programme

FRFIs should maintain an **insider threat programme** that:
- Defines insider threat risk scenarios and detection mechanisms
- Integrates HR, Legal, Security, and Technology teams
- Includes response procedures for confirmed insider threat incidents
- Covers both malicious insiders and unintentional/negligent insiders

---

## 8. Action Plan Requirement

### 8.1 Mandatory Action Plan Submission

A **distinctive feature of the I&S Guideline** is the mandatory Action Plan requirement:

> FRFIs were required to submit an **Integrity and Security Action Plan** to their Lead Supervisor by **July 31, 2024**, identifying:
> - Gaps between current practices and I&S Guideline expectations
> - Planned remediation actions with target completion dates
> - Accountability for each action item

### 8.2 Ongoing Reporting

Following the initial action plan:
- FRFIs must **update their Lead Supervisor** on action plan progress as part of regular supervisory interactions
- Material gaps or newly identified risks should be reported to the Lead Supervisor promptly
- The action plan is a **living document** — new risks and control gaps should be added as identified

---

## 9. Relationship to OSFI B-13

The I&S Guideline and B-13 are **complementary frameworks**:

| Domain                       | B-13 Coverage                                                         | I&S Guideline Coverage                                                            |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Logical Access Control**   | B-13 P13 (Security Architecture) — general logical security controls  | I&S — specific IAM, PAM, and access monitoring expectations; insider threat focus |
| **Monitoring and Detection** | B-13 P14 (Cybersecurity Monitoring) — threat monitoring and detection | I&S — personnel behaviour monitoring; physical intrusion detection                |
| **Incident Response**        | B-13 P15 (Incident Response) — CIRP covering cyber incidents          | I&S — physical and personnel security incidents; insider threat incident response |
| **Governance**               | B-13 P1–P5 (Governance and Risk Management)                           | I&S — integrity governance; Board accountability for security risks               |

> 📌 **Key Distinction:** B-13 focuses on **external threats and technology controls**. The I&S Guideline specifically addresses **insider threats, foreign interference, and physical security** — scenarios where bad actors may already be inside the FRFI's perimeter.

---

## 10. Relevance to OSFI 24-Hour Incident Reporting

The I&S Guideline directly connects to OSFI incident reporting in several important ways:

### 10.1 Access Control Failures as Reportable Incidents

Logical access control failures — particularly those involving unauthorised access to sensitive systems or customer data — are among the most common triggers for OSFI incident reporting:

| I&S Control Failure                                                | Incident Advisory Trigger                                                     |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Unauthorised privileged account access                             | A5 (customer information CIA), A4 (operations impact), D1 (critical severity) |
| Terminated employee retaining access; insider data exfiltration    | A5 (customer data breach), C1 (IRP activation), D1 (high severity)            |
| Physical breach of data centre leading to hardware theft           | B2 (data centre outage), A5 (data compromise), C1 (IRP activation)            |
| Visitor tailgating into secure area leading to unauthorised access | C1 (IRP activation), A5 (potential data exposure)                             |

### 10.2 Physical Security Incidents

Physical security failures that affect FRFI operations or data can trigger OSFI reporting:
- Data centre physical breach → B2, A6 triggers
- Theft of media/hardware containing customer data → A5, D1 triggers
- Physical denial of service (facility lock-out) impacting operations → B1, B2 triggers

### 10.3 Insider Threat Incidents as Governance Triggers

Insider threat incidents typically escalate to Senior Management or the Board quickly due to their sensitivity — triggering **Criterion C2** (incident reported to Board/Exec). If the insider had privileged IT access, the incident almost certainly meets multiple trigger criteria.

### 10.4 Personnel Security Breach as Regulatory Notification Driver

If a personnel security breach involves foreign state-sponsored activity or organised crime, OSFI may expect prompt notification through supervisory channels even outside the formal 24-hour technology incident window. The Lead Supervisor should be contacted immediately in such scenarios.

### 10.5 Access Reviews and the Post-Incident Review

Post-incident, OSFI expects a root cause analysis covering what controls failed. For I&S-related incidents, this typically involves reviewing:
- Whether access controls were adequate
- Whether background screening was conducted and current
- Whether monitoring detected the incident promptly
- What access review cycles were in place and whether they were completed

> 📌 **Summary:** The I&S Guideline establishes the physical and personnel security controls whose **failure often triggers OSFI incident reporting**. Access control failures, physical breaches, and insider threats are high-probability, high-severity incident scenarios that directly activate multiple OSFI Advisory trigger criteria.

---

## 11. Cross-References

| Document                                | Relationship                                                                                                               |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **OSFI B-13**                           | Companion guideline; I&S covers physical and personnel security; B-13 covers broader technology and cybersecurity          |
| **OSFI E-21**                           | Physical and personnel security failures are operational risk events within E-21 scope                                     |
| **OSFI Incident Reporting Advisory**    | Access control and physical security failures are primary incident triggers                                                |
| **OSFI Corporate Governance Guideline** | Board accountability for integrity and security risk                                                                       |
| **SOC 2 CC6**                           | SOC 2 logical and physical access controls align closely with I&S requirements                                             |
| **ISO 27001 / 27002**                   | ISO 27002 controls on physical security (Theme 3) and access management (Organisational controls 5.15–5.18) align with I&S |
| **PIPEDA DERR**                         | Insider-caused data breaches trigger PIPEDA breach notification in addition to OSFI reporting                              |

---

*Source: OSFI Integrity and Security Guideline (Released January 31, 2024)*
*URL: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/integrity-security-guideline*
