---
Document:        OSFI Guideline B-13 – Technology and Cyber Risk Management
Issuer:          Office of the Superintendent of Financial Institutions (OSFI)
Effective Date:  January 1, 2024
Last Verified:   April 2, 2026
Status:          Active
Type:            Mandatory – FRFI
Official URL:    https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/technology-cyber-risk-management-guideline
---

# OSFI Guideline B-13 — Technology and Cyber Risk Management

> **Document Type:** Regulatory Guideline
> **Issuer:** OSFI
> **Applies To:** All federally regulated financial institutions (FRFIs)
> **Effective Date:** January 1, 2024 (supersedes the 2013 Technology and Cyber Risk Management Advisory)

---

## Table of Contents

1. [Overview](#1-overview)
2. [Structure — Three Domains, 16 Principles, 57 Controls](#2-structure--three-domains-16-principles-57-controls)
3. [Domain 1 — Governance and Risk Management](#3-domain-1--governance-and-risk-management)
4. [Domain 2 — Technology Operations and Resilience](#4-domain-2--technology-operations-and-resilience)
5. [Domain 3 — Cybersecurity](#5-domain-3--cybersecurity)
6. [Proportionality and Sizing Expectations](#6-proportionality-and-sizing-expectations)
7. [Relationship to B-10, E-21, and I&S](#7-relationship-to-b-10-e-21-and-is)
8. [Relevance to OSFI 24-Hour Incident Reporting](#8-relevance-to-osfi-24-hour-incident-reporting)
9. [Cross-References](#9-cross-references)

---

## 1. Overview

OSFI Guideline B-13 is the **primary technology and cyber risk management framework** for all FRFIs. It establishes principles-based expectations for how FRFIs must govern, manage, and control their technology and cyber risks across all operations, business lines, and third-party arrangements.

B-13 reflects the increasing digitalisation of financial services and the sophistication of cyber threats. It is deliberately **outcomes-focused** rather than prescriptive, recognising that technology risk management practices must evolve continuously.

### Foundational Expectations

- Technology and cyber risk management is a **first-line and second-line responsibility**, overseen by the Board and Senior Management
- Controls must be **commensurate with the risk profile** and size/complexity of the FRFI
- **Continuous improvement** of the security posture is expected — static compliance is insufficient
- B-13 operates in conjunction with B-10 (third-party risk) and E-21 (operational resilience)

---

## 2. Structure — Three Domains, 16 Principles, 57 Controls

B-13 is organised into **three domains**, each subdivided into **principles** that are further supported by specific **controls**:

| Domain                                      | Principles | Controls     |
|---------------------------------------------|------------|--------------|
| **1. Governance and Risk Management**       | 1–5        | ~18 controls |
| **2. Technology Operations and Resilience** | 6–11       | ~21 controls |
| **3. Cybersecurity**                        | 12–16      | ~18 controls |
| **Total**                                   | **16**     | **57**       |

> 📌 The control count of 57 refers to the numbered control expectations within the guideline. Individual controls may encompass multiple sub-requirements.

---

## 3. Domain 1 — Governance and Risk Management

### Principles 1–5

| Principle | Topic                       | Key Expectations                                                                                                               |
|-----------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **P1**    | Risk Governance             | Board accountability for technology and cyber risk appetite; designated technology risk oversight function                     |
| **P2**    | Risk Appetite and Tolerance | Documented technology and cyber risk appetite integrated into enterprise risk management (ERM); KRIs established and monitored |
| **P3**    | Roles and Responsibilities  | Clear delineation of first-line (IT/business), second-line (risk management), and third-line (internal audit) responsibilities |
| **P4**    | Policies and Standards      | Comprehensive technology and cybersecurity policy framework, regularly reviewed and updated                                    |
| **P5**    | Talent and Culture          | Adequate staffing, skills, and training for technology and cyber roles; Board and Senior Management cyber awareness            |

### Key Governance Controls

- Board must approve the technology and cyber risk appetite and receive regular reporting on risk posture
- A designated Senior Management role (e.g., CIO, CISO, or equivalent) must have clear accountability
- Technology risk must be integrated into the FRFI's overall ERM framework
- Third-party technology risk is explicitly included within the governance scope (cross-reference to B-10)

---

## 4. Domain 2 — Technology Operations and Resilience

### Principles 6–11

| Principle | Topic                                       | Key Expectations                                                                                                            |
|-----------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **P6**    | Technology Asset Management                 | Complete, accurate inventory of technology assets (hardware, software, data, cloud); lifecycle management                   |
| **P7**    | Technology Architecture                     | Sound, documented architecture; technology debt management; cloud and hybrid environment governance                         |
| **P8**    | Change Management                           | Formal change management processes; change risk assessment; emergency change protocols                                      |
| **P9**    | Business Continuity and Disaster Recovery   | Documented, tested BCP/DR plans with defined RTO/RPO for critical systems; regular testing including cyber-attack scenarios |
| **P10**   | Data Management                             | Data quality, integrity, classification, and retention; backup and recovery; data lineage for critical data                 |
| **P11**   | Technology Project and Programme Management | Governance of material technology projects; risk identification during development; Agile/DevSecOps security integration    |

### Critical System Designation

B-13 requires FRFIs to maintain a **Critical System Register** — a documented inventory of systems whose failure would cause significant harm. This register directly feeds into:
- BCP/DR recovery prioritisation
- Enhanced monitoring and controls
- OSFI incident reporting (Criterion A6 — operational impact to key/critical systems)

### Recovery Time Objectives

FRFIs must define and test RTO and RPO for critical systems, with expectations that:
- Critical systems can be recovered within timeframes consistent with business continuity requirements
- Recovery capabilities are validated through **regular, documented DR testing**
- Cyber-attack recovery scenarios (e.g., ransomware) are specifically included in DR testing programmes

---

## 5. Domain 3 — Cybersecurity

### Principles 12–16

| Principle | Topic                                  | Key Expectations                                                                                                                                                     |
|-----------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **P12**   | Threat and Vulnerability Management    | Threat intelligence, vulnerability scanning, penetration testing, patch management with defined SLAs                                                                 |
| **P13**   | Security Architecture and Controls     | Defence-in-depth architecture; network segmentation; endpoint protection; identity and access management (IAM)                                                       |
| **P14**   | Cybersecurity Monitoring and Detection | 24/7 security monitoring capability (SIEM or equivalent); detection use cases for key threat scenarios; SOC function                                                 |
| **P15**   | Incident Response                      | Documented Cyber Incident Response Plan (CIRP); defined roles, escalation procedures, and communication protocols; regular testing (tabletop exercises, simulations) |
| **P16**   | Recovery and Lessons Learned           | Cyber resilience capabilities; post-incident review; integration of lessons learned into security programme improvements                                             |

### Cybersecurity Self-Assessment (CSSA)

B-13 is supported by OSFI's **Cybersecurity Self-Assessment (CSSA)** tool, which FRFIs submit annually. The CSSA maps to the B-13 principles and controls and provides OSFI with a baseline view of each FRFI's cyber maturity. The CSSA maps closely to the NIST CSF functions.

### Incident Response Requirements (Principle 15)

B-13 Principle 15 directly governs the organisational incident response capability that supports the OSFI Advisory reporting obligation:

- **CIRP must be documented and approved** by Senior Management
- Must define escalation triggers to the Board and Executive Management (which are themselves OSFI reporting triggers under Criterion C2)
- Must be **tested at least annually**, including simulation of a regulatory notification scenario
- Must include procedures for **external notification** including to OSFI, regulators, law enforcement, and affected parties

---

## 6. Proportionality and Sizing Expectations

B-13 applies to all FRFIs but acknowledges that implementation must be **proportional** to the size, complexity, and risk profile of the institution:

| FRFI Size                | Expectation                                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Large, complex FRFIs** | Full implementation of all 57 controls; dedicated CISO function; 24/7 SOC; advanced threat intelligence                          |
| **Mid-size FRFIs**       | Risk-based implementation; may use managed security service providers (MSSPs) for some functions; CISO may be a dual-hatted role |
| **Small FRFIs**          | Simplified implementation appropriate to scale; foundational controls in all three domains must still be present                 |

OSFI uses proportionality in supervisory assessment — smaller FRFIs are assessed against expectations appropriate to their scale, but the **core principles remain universal**.

---

## 7. Relationship to B-10, E-21, and I&S

| Guideline         | Integration Point with B-13                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **B-10**          | Third-party technology and cyber risk management is embedded within B-13; B-10 governs the contractual and lifecycle aspects, B-13 governs the ongoing risk management and control expectations             |
| **E-21**          | Operational resilience (E-21) provides the overarching framework; B-13 technology operations and resilience domain (P6–P11) is the technology-specific operationalisation of E-21 expectations              |
| **I&S Guideline** | Physical and logical security controls in I&S complement the cybersecurity domain (P12–P16) of B-13; B-13 cybersecurity applies to digital/logical controls, I&S applies to physical and personnel security |

The three guidelines (**B-10**, **B-13**, **E-21**) are designed to be **read and implemented together** as an integrated framework.

---

## 8. Relevance to OSFI 24-Hour Incident Reporting

B-13 is the primary governance framework within which the OSFI incident reporting obligation is embedded. Multiple principles directly govern activities that intersect with reporting:

### 8.1 Incident Response Plan as the Activation Trigger

B-13 Principle 15 requires a documented CIRP. Under the OSFI Incident Reporting Advisory, **activation of the FRFI's incident management team or protocols is a standalone reporting trigger (Criterion C1)**. B-13 compliance requires having a CIRP; activating it triggers OSFI reporting.

### 8.2 Monitoring and Detection (P14) Enables Timely Reporting

The 24/7 monitoring capability required by B-13 P14 is what enables FRFIs to **detect incidents promptly** — which is the starting point of the 24-hour reporting clock. Weak detection capabilities directly risk breach of the reporting timeline.

| B-13 Requirement                       | Reporting Connection                                                                        |
|----------------------------------------|---------------------------------------------------------------------------------------------|
| 24/7 monitoring and detection          | Enables timely incident detection (T+0h); gaps here compress available response time        |
| Security alerting and triage processes | Determines how quickly an incident is elevated from a security alert to a declared incident |
| Threat intelligence integration        | Supports rapid classification of incident type and severity (feeds D1 trigger criterion)    |

### 8.3 Critical System Register (P6) Feeds Trigger Criteria

B-13 requires a Critical System Register. The OSFI Advisory Criterion A6 (operational impact to key/critical systems) and Criterion D1 (P1/P2 severity based on internal classification) both require the FRFI to have a documented baseline of what constitutes a "critical" or "key" system. B-13 creates this baseline.

### 8.4 Board Escalation Procedures (P1, P15) Feed Criterion C2

B-13's governance requirements (P1, P15) establish when and how incidents are escalated to the Board and Senior Management. The Incident Reporting Advisory Criterion C2 (incident reported to Board or Senior/Executive Management) is triggered by these same escalation procedures.

### 8.5 Post-Incident Review (P16) Satisfies OSFI's Post-Incident Reporting Requirement

B-13 P16 requires post-incident review and lessons learned. This directly aligns with OSFI's requirement for a post-incident review report submitted following resolution of a reported incident.

> 📌 **Summary:** B-13 creates the governance, monitoring, response, and review capabilities that are the **operational foundation** of the OSFI 24-hour incident reporting obligation. A FRFI with strong B-13 compliance is better positioned to detect, escalate, and report incidents within the required timeframe.

---

## 9. Cross-References

| Document                             | Relationship                                                                                                        |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **OSFI B-10**                        | Third-party risk management; technology vendor oversight                                                            |
| **OSFI E-21**                        | Operational resilience; critical operations continuity                                                              |
| **OSFI I&S Guideline**               | Physical and personnel security complementing B-13 cyber domain                                                     |
| **OSFI Incident Reporting Advisory** | B-13 P15 (Incident Response) directly governs the operational capability for OSFI reporting                         |
| **OSFI E-23**                        | AI/model risk intersects with B-13 P6 (technology asset management) and P8 (change management)                      |
| **NIST CSF 2.0**                     | NIST CSF functions (Govern, Identify, Protect, Detect, Respond, Recover) map closely to B-13 domains and principles |
| **ISO 27001 / 27002**                | ISO 27002 controls align with B-13 cybersecurity domain; ISO 27001 certification provides evidence of ISMS maturity |
| **SOC 2 CC6**                        | SOC 2 access control criteria complement B-13 P13 (Security Architecture and Controls)                              |

---

*Source: OSFI Guideline B-13 — Technology and Cyber Risk Management (January 1, 2024)*
*URL: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/technology-cyber-risk-management-guideline*
