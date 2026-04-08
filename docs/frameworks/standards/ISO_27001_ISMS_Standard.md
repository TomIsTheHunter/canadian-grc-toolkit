---
Document:        ISO/IEC 27001:2022 – Information Security Management Systems – Requirements
Issuer:          International Organisation for Standardisation (ISO) / International Electrotechnical Commission (IEC)
Effective Date:  October 25, 2022 (supersedes ISO/IEC 27001:2013)
Last Verified:   April 2, 2026
Status:          Active
Type:            Voluntary / Best Practice — International Standard (certifiable)
Official URL:    https://www.iso.org/standard/27001
---

# ISO/IEC 27001:2022 — Information Security Management Systems (ISMS)

> **Document Type:** International Standard
> **Issuer:** ISO / IEC Joint Technical Committee (JTC 1), Subcommittee SC 27
> **Version:** ISO/IEC 27001:2022 (released October 2022; transition deadline October 2025)
> **Applies To:** Any organisation seeking to establish, implement, maintain, and continually improve an Information Security Management System (ISMS)

---

## Table of Contents

1. [Overview — What is ISO 27001?](#1-overview--what-is-iso-27001)
2. [2022 Revision — Key Changes](#2-2022-revision--key-changes)
3. [ISMS Scope and Certification](#3-isms-scope-and-certification)
4. [ISO 27001 Clause Structure](#4-iso-27001-clause-structure)
5. [Clause 6.1.2 — Information Security Risk Treatment](#5-clause-612--information-security-risk-treatment)
6. [Clause 9 — Performance Evaluation](#6-clause-9--performance-evaluation)
7. [Clause 10 — Continual Improvement](#7-clause-10--continual-improvement)
8. [Annex A — Information Security Controls (93 Controls)](#8-annex-a--information-security-controls-93-controls)
9. [ISMS and Incident Management (ISO 27001 + 27002 Controls 5.24–5.28)](#9-isms-and-incident-management-iso-27001--27002-controls-524528)
10. [ISMS Certification and Its Value for FRFIs](#10-isms-certification-and-its-value-for-frfis)
11. [Relevance to OSFI 24-Hour Incident Reporting](#11-relevance-to-osfi-24-hour-incident-reporting)
12. [Cross-References](#12-cross-references)

---

## 1. Overview — What is ISO 27001?

**ISO/IEC 27001:2022** is the internationally recognised standard for **Information Security Management Systems (ISMS)**. It specifies the requirements for establishing, implementing, maintaining, and continually improving an ISMS within the context of an organisation's overall business risks.

### What are an ISMS?

An **Information Security Management System (ISMS)** is a systematic approach to managing information security risks. It encompasses:
- Policies and procedures
- Risk assessment and treatment processes
- Technical and organisational controls
- Governance and accountability structures
- Internal audit and management review processes
- Continual improvement mechanisms

### ISO 27001 in the Canadian Financial Sector

While ISO 27001 certification is **voluntary** in Canada, it is increasingly adopted by FRFIs and their service providers as:
- **Evidence of security control maturity** for OSFI supervisory purposes
- **Third-party assurance** for B-10 vendor oversight (certificates of conformity)
- **A framework** for structuring the B-13 cybersecurity programme
- **Competitive differentiation** for FRFIs and vendors

---

## 2. 2022 Revision — Key Changes

The ISO/IEC 27001:2022 revision includes updates to the main body clauses and a restructured Annex A:

| Change Area               | Description                                                                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Annex A restructuring** | Reduced from 114 controls in 14 domains (2013) to 93 controls in 4 themes (2022), aligned to ISO 27002:2022                            |
| **New Annex A controls**  | 11 new controls added, including threat intelligence, cloud services security, ICT readiness for business continuity, and data masking |
| **Clause 6.3**            | New clause on planning of changes to the ISMS                                                                                          |
| **Clause 9.3**            | Management review inputs expanded                                                                                                      |

**Transition deadline:** Organisations certified to ISO 27001:2013 had until **October 31, 2025** to transition to the 2022 version. As of April 2026, all active certifications should be on ISO 27001:2022.

---

## 3. ISMS Scope and Certification

### 3.1 Defining the ISMS Scope

One of the most important decisions in implementing ISO 27001 is defining the **scope** of the ISMS — the organisational boundaries, systems, locations, and information assets covered by the management system:

- Scope can be organisation-wide or limited to specific business units, systems, or services
- Scope must be documented and justified
- Exclusions from the scope must not affect the ability to meet ISMS requirements

For FRFIs, a common scope includes:
- Core banking operations and associated infrastructure
- Customer-facing digital channels
- Data centre operations
- Critical third-party managed services (where the FRFI has sufficient oversight)

### 3.2 Certification Process

ISO 27001 certification is awarded by **accredited third-party certification bodies** through:

1. **Stage 1 Audit:** Documentation review — assessing whether the ISMS documentation meets ISO 27001 requirements
2. **Stage 2 Audit:** Certification audit — on-site assessment of ISMS implementation and effectiveness
3. **Surveillance Audits:** Annual audits to verify continued conformity
4. **Recertification Audit:** Every 3 years for full re-certification

### 3.3 Statement of Applicability (SoA)

A key ISO 27001 artefact is the **Statement of Applicability (SoA)** — a document listing all 93 Annex A controls, indicating which are applicable (and implemented) and which are excluded (with justification). The SoA is reviewed during every audit and serves as the primary evidence of control implementation.

---

## 4. ISO 27001 Clause Structure

ISO 27001 uses the **Annex SL / ISO Harmonised Structure** common to all ISO management system standards. The main body clauses are:

| Clause | Title                       | Summary                                                                         |
|--------|-----------------------------|---------------------------------------------------------------------------------|
| **4**  | Context of the Organisation | Understand internal/external issues; identify stakeholders; define ISMS scope   |
| **5**  | Leadership                  | Board/Executive commitment; information security policy; ISMS roles             |
| **6**  | Planning                    | Risk assessment; risk treatment; security objectives; planning of changes (6.3) |
| **7**  | Support                     | Resources; competence; awareness; communication; documented information         |
| **8**  | Operation                   | Operational planning; risk assessment and treatment implementation              |
| **9**  | Performance Evaluation      | Monitoring and measurement; internal audit; management review                   |
| **10** | Improvement                 | Nonconformity and corrective action; continual improvement                      |

---

## 5. Clause 6.1.2 — Information Security Risk Treatment

**Clause 6.1.2** governs how the organisation treats identified information security risks. This is the bridge between risk assessment and control selection:

### Risk Treatment Options

| Option                | Description                                                             |
|-----------------------|-------------------------------------------------------------------------|
| **Modify (Mitigate)** | Apply controls to reduce the risk to an acceptable level                |
| **Retain (Accept)**   | Accept the risk where it is within the organisation's risk appetite     |
| **Avoid**             | Eliminate the risk by removing the activity or condition creating it    |
| **Share (Transfer)**  | Transfer the risk to a third party (e.g., cyber insurance, outsourcing) |

### Risk Treatment Plan and SoA

For each risk selected for treatment by modification:
- A **Risk Treatment Plan** documents the controls to be applied, responsible parties, and timelines
- Selected controls are cross-referenced to **Annex A controls** (ISO 27002:2022)
- The SoA records which controls are implemented and which are excluded

### Connection to OSFI B-13

ISO 27001 Clause 6.1.2 risk treatment directly corresponds to **OSFI B-13 P2 (Risk Appetite and Tolerance)** and the requirement to assess and treat technology and cyber risks within a documented risk management framework.

---

## 6. Clause 9 — Performance Evaluation

Clause 9 establishes the **monitoring, measurement, internal audit, and management review** requirements:

### 9.1 Monitoring, Measurement, Analysis, and Evaluation

- Organisations must determine what needs to be monitored and measured
- Metrics include: number of incidents, control effectiveness KPIs, vulnerability patching SLA compliance
- Results must be documented and used to drive improvement

### 9.2 Internal Audit

- Internal audit of the ISMS must be conducted at planned intervals
- Audit programme must consider the processes and risk areas included
- Results must be reported to management

### 9.3 Management Review

The management review must include consideration of:
- Status of actions from previous reviews
- Changes in the external and internal issues relevant to the ISMS
- Feedback on the information security performance — including incidents
- Nonconformists and corrective actions
- Results of risk assessment and status of the risk treatment plan

### Connection to Incident Reporting

**Clause 9 requires that incidents feed into management review.** This means the management review process should include review of:
- All security incidents during the period
- Whether OSFI reporting obligations were met
- Root causes and lessons learned
- ISMS improvements resulting from incidents

---

## 7. Clause 10 — Continual Improvement

### 10.1 Nonconformity and Corrective Action

When a nonconformity occurs (including a security incident), the organisation must:
1. Determine the root cause
2. Implement corrective actions to prevent recurrence
3. Review the effectiveness of actions taken
4. Update the ISMS documentation as necessary

### 10.2 Continual Improvement

The organisation must continually improve the suitability, adequacy, and effectiveness of the ISMS. This is rationalised through:
- Lessons learned from incidents
- Updated threat and risk assessments
- Improvements to controls and procedures
- Training and awareness updates

### Connection to OSFI Post-Incident Review

OSFI's requirement for a **post-incident review and lessons learned report** is directly analogous to ISO 27001 Clause 10 continual improvement. Organisations with a mature ISO 27001 ISMS will have existing processes for documenting and implementing lessons learned — making the OSFI post-incident report a natural output of the ISMS improvement cycle.

---

## 8. Annex A — Information Security Controls (93 Controls)

ISO/IEC 27001:2022 Annex A specifies 93 information security controls organised into **4 themes** (aligned with ISO 27002:2022):

| Theme                             | Controls    | Examples                                                                                        |
|-----------------------------------|-------------|-------------------------------------------------------------------------------------------------|
| **Organisational Controls (A.5)** | 37 controls | Information security policies, incident management, threat intelligence, supplier relationships |
| **People Controls (A.6)**         | 8 controls  | Background screening, information security responsibilities, remote working                     |
| **Physical Controls (A.7)**       | 14 controls | Physical security perimeters, equipment security, clear desk/clear screen                       |
| **Technological Controls (A.8)**  | 34 controls | Access control, encryption, vulnerability management, secure coding, SIEM, data backup          |

### Key Annex A Controls for Incident Management

| Control    | Title                                                             | Relevance                                               |
|------------|-------------------------------------------------------------------|---------------------------------------------------------|
| **A.5.24** | Information security incident management planning and preparation | Documented IRP; roles and escalation procedures         |
| **A.5.25** | Assessment and decision on information security events            | Triage and classification of events as incidents        |
| **A.5.26** | Response to information security incidents                        | Execute IRP; contain, eradicate, and recover            |
| **A.5.27** | Learning from information security incidents                      | Post-incident review; lessons learned; ISMS improvement |
| **A.5.28** | Collection of evidence                                            | Forensic evidence preservation; chain of custody        |

These five controls (A.5.24–5.28) represent the **incident management lifecycle** within ISO 27001 and are the primary Annex A controls relevant to OSFI reporting.

---

## 9. ISMS and Incident Management (ISO 27001 + 27002 Controls 5.24–5.28)

The five incident management controls collectively establish:

### A.5.24 — Planning and Preparation

- Documented Incident Response Plan covering classification, escalation, communication, and regulatory notification
- Defined roles and responsibilities (incident commander, CISO, legal, communications)
- Contact lists for internal and external notification (including OSFI TRD and Lead Supervisor)
- Training and awareness for incident response team members

### A.5.25 — Assessment and Decision

- Criteria for classifying events as incidents vs. non-incidents
- Severity classification matrix (P1/P2/P3/P4 or equivalent)
- Assessment against OSFI trigger criteria as part of the classification process

### A.5.26 — Response

- Containment, eradication, and recovery procedures
- Communication protocols including regulatory notification
- Evidence preservation procedures
- Integration with OSFI Appendix II Incident Reporting Form

### A.5.27 — Learning from Incidents

- Mandatory post-incident review for all significant incidents
- Lessons learned documented and shared with relevant teams
- ISMS improvements resulting from lessons learned
- This corresponds directly to the OSFI post-incident review requirement

### A.5.28 — Collection of Evidence

- Forensic evidence handling and preservation (chain of custody)
- Log preservation to support investigation
- Evidence to support post-incident analysis and root cause determination

---

## 10. ISMS Certification and Its Value for FRFIs

### For FRFIs Seeking Certification

ISO 27001 certification demonstrates:
- A structured, audited approach to information security governance
- Evidence of control implementation for OSFI supervisory purposes (supports B-13 compliance narrative)
- Due diligence capability for managing third-party risk (B-10)

### For FRFIs Assessing Third-Party Vendors

ISO 27001 certification of a vendor:
- Provides third-party assurance that the vendor maintains an audited ISMS
- Is evidence of security maturity for B-10 vendor oversight
- Annual surveillance audits provide ongoing assurance (more current than point-in-time assessments)
- Note: Certification scope must be verified — a certificate does not cover all of a vendor's services

### Limitations of Certification

- Certification does not guarantee absence of incidents — it demonstrates a management system is in place
- The ISMS scope may not cover the specific services being procured
- Surveillance audits occur annually; conditions may change between audits (supplement with SOC 2 and direct monitoring)

---

## 11. Relevance to OSFI 24-Hour Incident Reporting

### 11.1 ISMS Clause 6.1.2 Risk Treatment Identifies Reportable Scenarios

An ISO 27001 risk assessment under Clause 6.1.2 that is properly aligned with OSFI B-13 should include risk scenarios that correspond to OSFI Advisory trigger criteria. The risk treatment plan should include:
- Detection controls (feeding Criterion C1 IRP activation)
- Escalation procedures (feeding Criterion C2 Board notification)
- Regulatory notification procedures (feeding the 24-hour reporting obligation directly)

### 11.2 Annex A Controls Support Detection and Response

| Annex A Control                | OSFI Reporting Connection                                        |
|--------------------------------|------------------------------------------------------------------|
| A.5.24 (IRP planning)          | Establishes the CIRP that, when activated, triggers Criterion C1 |
| A.5.25 (event classification)  | The severity classification triggers Criterion D1                |
| A.5.26 (incident response)     | The response procedure should include OSFI notification step     |
| A.8.16 (monitoring activities) | SIEM/SOC capabilities enabling incident detection (T+0h)         |

### 11.3 Post-Incident Review (A.5.27) Maps to OSFI PIR Requirement

ISO 27001 Annex A.5.27 requires learning from incidents and improving the ISMS. OSFI's post-incident review requirement is functionally identical. Organisations with a mature A.5.27 process will naturally produce an OSFI-compliant post-incident report as part of their standard ISMS improvement cycle.

### 11.4 ISMS Certification as Evidence for OSFI Supervisory Review

During OSFI supervisory reviews, a valid ISO 27001 certificate:
- Provides independent assurance that the FRFI's security controls meet an international standard
- Demonstrates that incident management procedures have been audited by an accredited body
- Supports the narrative that the FRFI has a systematic approach to security governance (consistent with B-13)

> 📌 **Summary:** ISO 27001 creates the ISMS governance structure — including risk treatment, incident management controls (A.5.24–5.28), and continual improvement — that enables FRFIs to systematically meet the OSFI 24-hour incident reporting obligation. Certification provides independent assurance of control maturity. The post-incident improvement cycle (Clause 10) maps directly to the OSFI post-incident review requirement.

---

## 12. Cross-References

| Document                             | Relationship                                                                                                                            |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **ISO 27002:2022**                   | Annex A of ISO 27001 references ISO 27002 for control guidance; the two standards are used together                                     |
| **OSFI B-13**                        | ISO 27001 provides a certifiable ISMS framework that supports B-13 compliance across all three domains                                  |
| **OSFI Incident Reporting Advisory** | A.5.24–5.28 incident management controls operationalise the 24-hour reporting obligation                                                |
| **OSFI I&S Guideline**               | Physical controls (Theme A.7) and access management (A.5.15–5.18, A.8.2–8.4) align with I&S requirements                                |
| **OSFI B-10**                        | ISO 27001 vendor certificates are evidence for B-10 third-party oversight; A.5.19–5.22 supplier relationships                           |
| **NIST CSF 2.0**                     | NIST and ISO 27001 are complementary; NIST provides the function-level framework; ISO 27001 provides the management system structure    |
| **SOC 2**                            | ISO 27001 and SOC 2 are often obtained together; ISO 27001 provides the management system, SOC 2 provides operational control assurance |
| **PIPEDA DERR / Quebec Law 25**      | ISMS privacy controls support breach prevention; A.5.24–5.28 incident management supports breach notification compliance                |

---

*Source: ISO/IEC 27001:2022 — Information Security Management Systems — Requirements*
*Published: October 25, 2022*
*URL: https://www.iso.org/standard/27001*
