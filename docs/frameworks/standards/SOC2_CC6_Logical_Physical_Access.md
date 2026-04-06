---
Document:        SOC 2 Trust Services Criteria — CC6 Logical and Physical Access Controls
Issuer:          American Institute of Certified Public Accountants (AICPA)
Effective Date:  Active (current Trust Services Criteria, 2017 edition with 2022 updates)
Last Verified:   April 2, 2026
Status:          Active
Type:            Voluntary / Best Practice — Audit / Assurance Framework
Official URL:    https://www.aicpa-cima.com/resources/landing/system-and-organisation-controls-soc-suite-of-services
---

# SOC 2 — CC6 Logical and Physical Access Controls

> **Document Type:** Audit and Assurance Framework (Trust Services Criteria)
> **Issuer:** AICPA (American Institute of Certified Public Accountants)
> **Applies To:** Service organisations voluntarily seeking SOC 2 attestation; also relevant to FRFIs as a control benchmark and for assessing third-party service providers
> **Framework Version:** Trust Services Criteria (TSC) — 2017 with 2022 updates

---

## Table of Contents

1. [Overview — SOC 2 and Trust Services Criteria](#1-overview--soc-2-and-trust-services-criteria)
2. [CC6 — Logical and Physical Access Controls Overview](#2-cc6--logical-and-physical-access-controls-overview)
3. [CC6.1 — Logical Access Security Measures](#3-cc61--logical-access-security-measures)
4. [CC6.2 — New Access Provisioning](#4-cc62--new-access-provisioning)
5. [CC6.3 — Access Removal and Modification](#5-cc63--access-removal-and-modification)
6. [CC6.4 — Physical Access Restrictions](#6-cc64--physical-access-restrictions)
7. [CC6.5 — Discontinuation of Logical and Physical Access](#7-cc65--discontinuation-of-logical-and-physical-access)
8. [CC6.6 — Boundary Protections](#8-cc66--boundary-protections)
9. [CC6.7 — Encryption of Personal Information in Transit and at Rest](#9-cc67--encryption-of-personal-information-in-transit-and-at-rest)
10. [CC6.8 — Controls to Prevent and Detect Unauthorised Access](#10-cc68--controls-to-prevent-and-detect-unauthorised-access)
11. [CC7 — System Operations (Adjacent Criteria)](#11-cc7--system-operations-adjacent-criteria)
12. [Relevance to OSFI 24-Hour Incident Reporting](#12-relevance-to-osfi-24-hour-incident-reporting)
13. [Cross-References](#13-cross-references)

---

## 1. Overview — SOC 2 and Trust Services Criteria

### 1.1 What is SOC 2?

**SOC 2 (System and Organisation Controls 2)** is an auditing framework developed by the AICPA to assess and attest to the security and privacy controls of service organisations. A SOC 2 report provides independent, third-party assurance that a service organisation's controls meet the AICPA's **Trust Services Criteria (TSC)**.

### 1.2 The Five Trust Services Categories

| Category                 | Description                                                                                            |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| **Security (CC)**        | The system is protected against unauthorised access — **mandatory for all SOC 2 reports**              |
| **Availability**         | The system is available for operation as committed or agreed                                           |
| **Processing Integrity** | System processing is complete, valid, accurate, timely, and authorised                                 |
| **Confidentiality**      | Information designated as confidential is protected                                                    |
| **Privacy**              | Personal information is collected, used, retained, and disclosed per the organisation's privacy notice |

### 1.3 Relevance to FRFIs

FRFIs use SOC 2 in two key ways:
1. **Internal assurance:** Obtaining SOC 2 reports from third-party vendors (cloud providers, SaaS services) to assess their control environments — directly relevant to OSFI B-10 third-party oversight
2. **Benchmarking:** Using the TSC as a control benchmark for their own security programmes — the CC6 criteria align closely with OSFI B-13 P13 (Security Architecture) and the I&S Guideline

---

## 2. CC6 — Logical and Physical Access Controls Overview

**CC6** is the most detailed section of the SOC 2 Security category and covers **eight criteria** addressing how organisations control who can access their systems, data, and physical facilities.

| Criterion | Topic                                                                     |
|-----------|---------------------------------------------------------------------------|
| CC6.1     | Logical access security software, infrastructure, and architectures       |
| CC6.2     | New access credential registration and authorisation                      |
| CC6.3     | Removal of access credentials after personnel changes                     |
| CC6.4     | Physical access restrictions to facilities and systems                    |
| CC6.5     | Logical and physical access discontinuation upon change/termination       |
| CC6.6     | Boundary protections for network access                                   |
| CC6.7     | Encryption of data in transit and at rest                                 |
| CC6.8     | Controls to prevent and detect unauthorised software, malware, and access |

---

## 3. CC6.1 — Logical Access Security Measures

**Criterion:** The entity implements logical access security software, infrastructure, and architectures overprotected information assets to protect them from security events.

### Key Control Expectations

| Control Area                          | Description                                                        |
|---------------------------------------|--------------------------------------------------------------------|
| **Access control policy**             | Formal policy defining how access is granted, managed, and revoked |
| **Role-based access**                 | Access rights based on business roles; least privilege principle   |
| **Multi-factor authentication (MFA)** | Required for remote access and privileged accounts                 |
| **Authentication systems**            | Identity management platforms managing access to systems           |
| **Privileged account management**     | Enhanced controls for admin/privileged accounts                    |
| **Password/credential policies**      | Complexity, rotation, and storage requirements                     |

### FRFI Application

For FRFIs, CC6.1 aligns with OSFI B-13 P13 (Security Architecture) and the I&S Guideline IAM requirements. A SOC 2 audit opinion on CC6.1 provides independent assurance that access controls are operating effectively.

---

## 4. CC6.2 — New Access Provisioning

**Criterion:** Prior to issuing system credentials and granting access to the system, the entity registers and authorises new users and records related data, considers the appropriateness of access, and responds appropriately to access requests.

### Key Control Expectations

- Formal access request process with documented business justification
- Appropriate approval authorisation (manager, system owner)
- Role-based provisioning aligned to the principle of least privilege
- New employee onboarding process includes access provisioning
- Access requests and approvals documented and auditable

### Relevance to Incident Scenarios

Weaknesses in access provisioning commonly surface in incident investigations:
- Over-provisioned accounts exploited in breaches
- Unauthorised access using shared or generic credentials
- Privilege escalation exploiting excessive standing privileges

---

## 5. CC6.3 — Access Removal and Modification

**Criterion:** The entity removes access to protected information assets when appropriate; considers the appropriateness and changes access during role changes; and records related data.

### Key Control Expectations

| Event                              | Control Requirement                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------|
| **Termination**                    | Access revoked promptly (same day or within defined SLA) upon employment termination |
| **Role change**                    | Access adjusted to reflect new role; old access revoked                              |
| **Leave of absence**               | Access suspended during extended leave (e.g., >30 days)                              |
| **Contractor/vendor off-boarding** | Third-party access terminated upon contract expiration                               |
| **Periodic access reviews**        | Regular (at minimum annual) user access recertification                              |

### Common Control Failures

- **Stale accounts:** Former employees retaining active accounts — a leading cause of insider threat incidents
- **Orphaned privileged accounts:** Admin accounts not linked to a current employee
- **Delayed de-provisioning:** HR-to-IT notification gaps allowing access to persist post-termination

---

## 6. CC6.4 — Physical Access Restrictions

**Criterion:** The entity restricts physical access to information assets and data centres to authorised personnel to protect against threats from persons in unauthorised areas.

### Key Control Expectations

- Physical access controls (badge readers, biometric authentication) at data centres and secure areas
- Visitor management — sign-in, escorted access, visitor logs
- Physical access logs reviewed and anomalies investigated
- Security cameras (CCTV) covering entry points and critical areas
- Environmental monitoring (fire, water, temperature) in data centres

### Alignment with OSFI I&S

CC6.4 directly parallels the physical security expectations in the OSFI I&S Guideline. A SOC 2 Type II report provides audit evidence that these controls were operating effectively throughout the audit period.

---

## 7. CC6.5 — Discontinuation of Logical and Physical Access

**Criterion:** The entity discontinues logical and physical access to protected information assets when appropriate, considers the appropriateness of access, and records related data.

This criterion reinforces CC6.3 and CC6.4 with specific focus on the **off-boarding** process:
- Concurrent revocation of both logical (system) and physical (badge) access
- Documented checklists for off-boarding that cover all access types
- Verification that access has been revoked (confirmation step)

---

## 8. CC6.6 — Boundary Protections

**Criterion:** The entity implements logical access security measures to protect against threats from sources outside its system boundaries.

### Key Control Expectations

| Control Area                        | Description                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------|
| **Network perimeter security**      | Firewalls, IDS/IPS, DMZ architectures                                               |
| **Remote access security**          | VPN with MFA; zero trust network access (ZTNA)                                      |
| **Web application firewalls (WAF)** | Protection for internet-facing applications                                         |
| **DDoS protection**                 | Mitigation for distributed denial of service attacks                                |
| **Email security**                  | Anti-phishing, anti-spoofing, email filtering                                       |
| **Third-party connectivity**        | Secure channels for third-party access; segment vendor access from internal network |

### FRFI Application

CC6.6 boundary controls are foundational to preventing external cyberattacks. A DDoS attack (Group B trigger criteria B3 — loss of connectivity) or perimeter breach would first defeat CC6.6 controls.

---

## 9. CC6.7 — Encryption of Personal Information in Transit and at Rest

**Criterion:** The entity restricts the transmission, movement, and removal of information to authorised internal and external users and processes, and protects it during transmission, movement, or removal to meet the entity's objectives.

### Key Control Expectations

- Encryption of sensitive data **in transit** (TLS 1.2+, secure protocols)
- Encryption of sensitive data **at rest** (AES-256 or equivalent for databases, backups, portable media)
- Key management controls — generation, storage, rotation, and destruction
- Data loss prevention (DLP) controls to prevent unauthorised data exfiltration
- Removable media controls — encryption required for portable storage devices
- Data classification policy governing encryption requirements by data sensitivity level

### Privacy Breach Implications

Encryption at rest is a critical factor in PIPEDA DERR harm assessment — encrypted data that is stolen is less likely to create "real risk of significant harm" if the encryption keys were not also compromised.

---

## 10. CC6.8 — Controls to Prevent and Detect Unauthorised Access

**Criterion:** The entity implements controls to prevent or detect and act upon the introduction of unauthorised or malicious software to meet the entity's objectives.

### Key Control Expectations

| Control Area                         | Description                                                       |
|--------------------------------------|-------------------------------------------------------------------|
| **Endpoint protection**              | Antivirus, EDR (Endpoint Detection and Response) on all endpoints |
| **Application allow-listing**        | Restrict execution to approved applications (where feasible)      |
| **Patch management**                 | Timely patching of vulnerabilities; defined SLAs by severity      |
| **Malware detection**                | SIEM/EDR alerting on indicators of compromise                     |
| **Software composition analysis**    | Scanning for vulnerabilities in third-party libraries             |
| **Security configuration baselines** | Hardened system configurations; CIS Benchmarks or equivalent      |

### Connection to Incident Detection

CC6.8 controls are what enable **incident detection** — the starting point for the OSFI 24-hour reporting clock. Gaps in endpoint detection, patching, or malware detection directly delay the moment of detection and compress available response time.

---

## 11. CC7 — System Operations (Adjacent Criteria)

While CC6 governs access controls, **CC7 (System Operations)** governs incident response and is directly relevant to OSFI reporting:

| Criterion | Relevance                                                                           |
|-----------|-------------------------------------------------------------------------------------|
| **CC7.1** | Security event monitoring and detection — detecting incidents quickly               |
| **CC7.2** | Evaluating security events for significance — triage and classification             |
| **CC7.3** | Incident response procedures — responding to confirmed incidents                    |
| **CC7.4** | Incident communication and notification — notifying affected parties and regulators |
| **CC7.5** | Identifying and remediating vulnerabilities — root cause analysis                   |

CC7.4 specifically requires that organisations notify relevant parties (including regulators) in accordance with their obligations — directly including OSFI notification under the Advisory.

---

## 12. Relevance to OSFI 24-Hour Incident Reporting

### 12.1 CC6 Failures Are Primary Incident Scenarios

The majority of cyber incidents that trigger OSFI incident reporting arise from failures of CC6 controls:

| CC6 Failure                                        | OSFI Advisory Trigger                                                  |
|----------------------------------------------------|------------------------------------------------------------------------|
| Unauthorised access (CC6.1/6.3 failure)            | A5 (customer information CIA), D1 (high severity), C1 (IRP activation) |
| Stale/terminated employee account exploited        | A5, C1, D1                                                             |
| Physical breach of data centre (CC6.4 failure)     | B2 (data centre outage), A5, C1                                        |
| Perimeter breach / external attack (CC6.6 failure) | A4, A5, C1, D1                                                         |
| Ransomware (CC6.8 failure)                         | B1 (operations disruption), A6, C1, D1                                 |
| Data exfiltration (CC6.7 failure)                  | A5, D1, D3 (reputational impact)                                       |

### 12.2 SOC 2 Reports as Evidence During Incident Response

When reporting to OSFI, demonstrating the state of controls at the time of the incident is important. SOC 2 Type II reports from third-party service providers:
- Provide audit evidence of whether key controls were operating effectively
- Can be cited in OSFI Incident Reporting Form to demonstrate vendor control posture
- Inform whether a third-party control failure contributed to the incident (B5/B6 triggers)

### 12.3 CC7.4 Notification Criteria Support OSFI Reporting

SOC 2 CC7.4 requires organisations to notify relevant parties, including regulators. For FRFIs, OSFI is a regulatory party. A well-designed SOC 2 CC7 implementation should embed the OSFI 24-hour notification requirement in the incident response procedure — ensuring it is addressed by the standard incident response process.

### 12.4 FRFI Vendor Due Diligence (B-10 Alignment)

Under OSFI B-10, FRFIs must assess the control environments of critical third parties. SOC 2 reports are a primary mechanism for doing so:
- Request and review SOC 2 Type II reports from critical vendors annually
- Assess CC6 criteria for adequacy and identify exceptions
- CC6 exceptions in a vendor's SOC 2 report are potential third-party risk indicators that may require enhanced monitoring (B-10) and, if realised, may trigger OSFI incident reporting (B5/B6)

> 📌 **Summary:** SOC 2 CC6 access controls are the primary preventive and detective controls whose failure leads to cyber incidents triggering OSFI reporting. CC7 incident response criteria embed regulatory notification requirements. FRFIs use SOC 2 reports to assess both their own and their vendors' control environments — providing the evidentiary basis for post-incident reporting.

---

## 13. Cross-References

| Document                             | Relationship                                                                                              |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **OSFI B-13**                        | B-13 P13 (Security Architecture) and P14 (Monitoring) align with CC6.1/6.6/6.8 and CC7.1/7.2 respectively |
| **OSFI I&S Guideline**               | CC6.4 (physical access) and CC6.1 (logical access) align with I&S physical and logical security controls  |
| **OSFI B-10**                        | SOC 2 reports are a key tool for third-party control assessment; CC6 exceptions signal third-party risk   |
| **OSFI Incident Reporting Advisory** | CC6 failures generate incident reporting triggers; CC7.4 requires regulatory notification                 |
| **ISO 27001 / 27002**                | ISO 27002 access management controls (5.15–5.18) and physical security (7.x) align with CC6               |
| **NIST CSF 2.0**                     | NIST Protect (PR.AC) and Detect functions align with CC6 and CC7 respectively                             |

---

*Source: SOC 2 Trust Services Criteria — Logical and Physical Access Controls (CC6)*
*Issuer: AICPA*
*URL: https://www.aicpa-cima.com/resources/landing/system-and-organisation-controls-soc-suite-of-services*
