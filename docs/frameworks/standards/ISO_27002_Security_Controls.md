---
Document:        ISO/IEC 27002:2022 – Information Security Controls
Issuer:          International Organisation for Standardisation (ISO) / International Electrotechnical Commission (IEC)
Effective Date:  February 15, 2022 (supersedes ISO/IEC 27002:2013)
Last Verified:   April 2, 2026
Status:          Active
Type:            Voluntary / Best Practice — International Standard (guidance)
Official URL:    https://www.iso.org/standard/75652.html
---

# ISO/IEC 27002:2022 — Information Security Controls

> **Document Type:** International Standard (Guidance)
> **Issuer:** ISO / IEC Joint Technical Committee (JTC 1), Subcommittee SC 27
> **Version:** ISO/IEC 27002:2022 (released February 2022; supersedes ISO/IEC 27002:2013)
> **Applies To:** Organisations implementing information security controls; serves as the reference guidance for ISO 27001 Annex A

---

## Table of Contents

1. [Overview — ISO 27002 and Its Relationship to ISO 27001](#1-overview--iso-27002-and-its-relationship-to-iso-27001)
2. [2022 Restructuring — Four Themes, 93 Controls](#2-2022-restructuring--four-themes-93-controls)
3. [Theme 1 — Organisational Controls (5.1–5.37)](#3-theme-1--organisational-controls-51537)
4. [Theme 2 — People Controls (6.1–6.8)](#4-theme-2--people-controls-6168)
5. [Theme 3 — Physical Controls (7.1–7.14)](#5-theme-3--physical-controls-71714)
6. [Theme 4 — Technological Controls (8.1–8.34)](#6-theme-4--technological-controls-81834)
7. [New Controls in ISO 27002:2022](#7-new-controls-in-iso-270022022)
8. [Incident Management Controls in Detail (5.24–5.28)](#8-incident-management-controls-in-detail-524528)
9. [Control Attributes — New Feature in 2022](#9-control-attributes--new-feature-in-2022)
10. [Mapping ISO 27002 to ISO 27001 Annex A](#10-mapping-iso-27002-to-iso-27001-annex-a)
11. [Relevance to OSFI 24-Hour Incident Reporting](#11-relevance-to-osfi-24-hour-incident-reporting)
12. [Cross-References](#12-cross-references)

---

## 1. Overview — ISO 27002 and Its Relationship to ISO 27001

### 1.1 Role of ISO 27002

**ISO/IEC 27002:2022** is the **implementation guidance** companion to ISO/IEC 27001. While ISO 27001 specifies the *requirements* of an ISMS and lists controls in Annex A, ISO 27002 provides:
- Detailed **guidance on how to implement** each control
- **Purpose** statements for each control (why it exists)
- **Implementation guidance** (practical steps and considerations)
- **Other information** (examples, additional context, related standards)

ISO 27002 is a **guidance standard** — it is not itself certifiable. Organisations are certified to ISO 27001; ISO 27002 provides the implementation detail.

### 1.2 Structure Alignment

ISO 27002:2022 and ISO 27001:2022 Annex A are **fully aligned** — the 93 controls in ISO 27001 Annex A correspond exactly to the 93 controls described in ISO 27002:2022, organised in the same four themes with identical numbering.

---

## 2. 2022 Restructuring — Four Themes, 93 Controls

The 2022 revision restructured the control set significantly:

| Comparison           | ISO 27002:2013 | ISO 27002:2022      |
|----------------------|----------------|---------------------|
| **Total Controls**   | 114            | 93                  |
| **Organisation**     | 14 domains     | 4 themes            |
| **New controls**     | N/A            | 11 new controls     |
| **Merged controls**  | N/A            | 24 controls merged  |
| **Revised controls** | N/A            | 58 controls updated |
| **Deleted controls** | N/A            | 1 control deleted   |

### The Four Themes

| Theme                       | Control Range | Count  |
|-----------------------------|---------------|--------|
| **Organisational Controls** | 5.1–5.37      | 37     |
| **People Controls**         | 6.1–6.8       | 8      |
| **Physical Controls**       | 7.1–7.14      | 14     |
| **Technological Controls**  | 8.1–8.34      | 34     |
| **Total**                   |               | **93** |

---

## 3. Theme 1 — Organisational Controls (5.1–5.37)

Organisational controls cover policies, governance, processes, and management-level information security activities:

### Key Organisational Controls

| Control       | Title                                                                         | Relevance                                                              |
|---------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------|
| **5.1**       | Policies for information security                                             | Security policy framework; incident reporting policy                   |
| **5.2**       | Information security roles and responsibilities                               | CISO, incident commander, escalation roles                             |
| **5.4**       | Management responsibilities                                                   | Senior Management obligations for security compliance                  |
| **5.7**       | Threat intelligence                                                           | Collection and analysis of threat intelligence for proactive detection |
| **5.15–5.18** | Access control policies                                                       | Who can access what, under what conditions                             |
| **5.19–5.22** | Supplier security                                                             | Third-party security agreements, monitoring, and incident notification |
| **5.23**      | Information security for use of cloud services                                | Cloud-specific security requirements                                   |
| **5.24**      | Information security incident management planning and preparation             | **IRP planning — core incident management control**                    |
| **5.25**      | Assessment and decision on information security events                        | **Incident triage and classification**                                 |
| **5.26**      | Response to information security incidents                                    | **Incident response execution**                                        |
| **5.27**      | Learning from information security incidents                                  | **Post-incident review and lessons learned**                           |
| **5.28**      | Collection of evidence                                                        | **Forensic evidence handling**                                         |
| **5.29**      | Information security during disruption                                        | Business continuity for information security                           |
| **5.30**      | ICT readiness for business continuity                                         | Technology BCP/DR — aligns with B-13 P9                                |
| **5.34**      | Privacy and protection of personal information                                | PIPEDA, Quebec Law 25 controls                                         |
| **5.35–5.37** | Independent review; compliance with policies; documented operating procedures | Audit, compliance monitoring                                           |

---

## 4. Theme 2 — People Controls (6.1–6.8)

People controls address the human dimension of information security:

| Control | Title                                                   | Relevance                                                         |
|---------|---------------------------------------------------------|-------------------------------------------------------------------|
| **6.1** | Screening                                               | Background checks — aligns with OSFI I&S personnel security       |
| **6.2** | Terms and conditions of employment                      | Security responsibilities in employment contracts                 |
| **6.3** | Information security awareness, education, and training | Security awareness; phishing training; incident reporting culture |
| **6.4** | Disciplinary process                                    | Consequences for security policy violations                       |
| **6.5** | Responsibilities after termination/change of employment | Off-boarding, access revocation                                   |
| **6.6** | Confidentiality or non-disclosure agreements            | NDAs for contractors and employees                                |
| **6.7** | Remote working                                          | Security requirements for remote/home working                     |
| **6.8** | Information security event reporting                    | **Employee obligation to report security events promptly**        |

### 6.8 — Employee Security Event Reporting

**Control 6.8** is directly relevant to the incident reporting chain: it requires organisations to establish mechanisms for employees to **report security events** as quickly as possible to the appropriate channel. This is the foundation of the internal reporting chain that ultimately feeds the OSFI 24-hour notification:

```
Employee observes security event (Control 6.8)
        ↓
Internal security team / SOC receives report
        ↓
Incident triage and classification (5.25)
        ↓
IRP activated (5.24) — OSFI Criterion C1 triggered
        ↓
OSFI notification (within 24 hours)
```

---

## 5. Theme 3 — Physical Controls (7.1–7.14)

Physical controls address the security of physical premises and equipment:

| Control  | Title                                                 | Relevance                                                             |
|----------|-------------------------------------------------------|-----------------------------------------------------------------------|
| **7.1**  | Physical security perimeters                          | Data centre perimeter security — aligns with OSFI I&S                 |
| **7.2**  | Physical entry controls                               | Visitor management; badge access; mantrap                             |
| **7.3**  | Securing offices, rooms, and facilities               | Security of server rooms, archives, and sensitive work areas          |
| **7.4**  | Physical security monitoring                          | CCTV, intrusion detection, guard patrols                              |
| **7.5**  | Protecting against physical and environmental threats | Fire, flood, power failure controls                                   |
| **7.7**  | Clear desk and clear screen                           | Reduces risk of unauthorised access to physical documents and screens |
| **7.10** | Storage media                                         | Secure handling, encryption, and disposal of storage media            |
| **7.12** | Cabling security                                      | Protection of network and power cabling                               |
| **7.14** | Secure disposal or re-use of equipment                | Data destruction on decommissioned devices — PIPEDA/Law 25 compliance |

---

## 6. Theme 4 — Technological Controls (8.1–8.34)

Technological controls address the technical security measures for systems, networks, and applications:

### Key Technological Controls

| Control       | Title                                                  | Relevance                                                   |
|---------------|--------------------------------------------------------|-------------------------------------------------------------|
| **8.2**       | Privileged access rights                               | PAM; privileged account management — OSFI I&S alignment     |
| **8.4**       | Access to source code                                  | Controls for code repositories and development environments |
| **8.5**       | Secure authentication                                  | MFA; password management                                    |
| **8.7**       | Protection against malware                             | Antivirus, EDR, anti-malware — SOC 2 CC6.8 alignment        |
| **8.8**       | Management of technical vulnerabilities                | Vulnerability scanning; patch management SLAs               |
| **8.9**       | Configuration management                               | Security baselines; hardening standards                     |
| **8.10**      | Information deletion                                   | Secure deletion in compliance with retention policies       |
| **8.11**      | Data masking                                           | Protection of sensitive data in non-production environments |
| **8.12**      | Data leakage prevention                                | DLP controls; monitoring for unauthorised data exfiltration |
| **8.15**      | Logging                                                | Audit logging; log integrity; retention periods             |
| **8.16**      | Monitoring activities                                  | **SIEM/SOC monitoring — incident detection capability**     |
| **8.17**      | Clock synchronisation                                  | Accurate timestamps for log correlation and forensics       |
| **8.20**      | Network security                                       | Network segmentation; firewall management                   |
| **8.21**      | Security of network services                           | Secure network protocols; ISP security requirements         |
| **8.23**      | Web filtering                                          | Blocking malicious web content                              |
| **8.24**      | Use of cryptography                                    | Encryption policy; key management                           |
| **8.25–8.28** | Secure development lifecycle                           | Security in DevOps; code review; testing                    |
| **8.29**      | Security testing in development and acceptance         | Penetration testing; DAST/SAST                              |
| **8.34**      | Protection of information systems during audit testing | Protect live systems during audit activities                |

---

## 7. New Controls in ISO 27002:2022

Eleven controls are new in the 2022 version — most are particularly relevant for modern financial institutions:

| New Control | Title                                          | Relevance to FRFIs                                                      |
|-------------|------------------------------------------------|-------------------------------------------------------------------------|
| **5.7**     | Threat intelligence                            | Proactive threat intelligence programme to anticipate attacks           |
| **5.23**    | Information security for use of cloud services | Cloud-specific security requirements — critical for FRFI cloud adoption |
| **5.30**    | ICT readiness for business continuity          | Technology BCP/DR explicitly addressed as a standalone control          |
| **7.4**     | Physical security monitoring                   | CCTV and intrusion detection formally addressed                         |
| **8.9**     | Configuration management                       | Security baselines and hardening standards                              |
| **8.10**    | Information deletion                           | Secure deletion obligations (privacy compliance)                        |
| **8.11**    | Data masking                                   | Masking of sensitive data in dev/test environments                      |
| **8.12**    | Data leakage prevention                        | DLP controls for data exfiltration prevention                           |
| **8.16**    | Monitoring activities                          | SIEM and security monitoring explicitly addressed                       |
| **8.23**    | Web filtering                                  | Network-level protection against malicious web content                  |
| **8.28**    | Secure coding                                  | Secure development practices embedded in development lifecycle          |

---

## 8. Incident Management Controls in Detail (5.24–5.28)

The five incident management controls represent the ISO 27002 implementation guidance for the OSFI incident reporting process:

### 5.24 — Information Security Incident Management Planning and Preparation

**Purpose:** Ensure a consistent and effective approach to the management of information security incidents.

**Implementation Guidance:**
- Define what constitutes an information security event vs. incident
- Establish a formal IRP with defined roles, escalation procedures, and communication protocols
- Include **regulatory notification procedures** with specific contacts and timelines (OSFI TRD, Lead Supervisor)
- Conduct regular tabletop exercises to test the IRP
- Maintain contact lists for all relevant parties (internal and external)

> 📌 **OSFI Connection:** The IRP required by 5.24 is the same CIRP required by B-13 P15. Its activation triggers Advisory Criterion C1.

### 5.25 — Assessment and Decision on Information Security Events

**Purpose:** Ensure information security events are classified and assessed to determine whether they qualify as incidents.

**Implementation Guidance:**
- Establish triage criteria for assessing events from security monitoring systems
- Maintain a severity classification matrix with defined criteria for each level
- **Assess events against OSFI trigger criteria** as part of the classification process (e.g., does this event meet any A, B, C, or D criterion?)
- Document assessment decisions and reasoning

### 5.26 — Response to Information Security Incidents

**Purpose:** Ensure a consistent and effective response to information security incidents.

**Implementation Guidance:**
- Execute the IRP for all confirmed incidents
- **Notify appropriate external parties** including:
  - Regulators (OSFI TRD and Lead Supervisor within 24 hours)
  - Law enforcement (where criminal activity is involved)
  - Privacy commissioners (OPC, CAI) for data breaches
  - Cyber insurers
- Document all response actions with timestamps
- Complete the OSFI Appendix II Incident Reporting Form

### 5.27 — Learning from Information Security Incidents

**Purpose:** Reduce the likelihood or impact of future incidents by learning from past incidents.

**Implementation Guidance:**
- Conduct a post-incident review for all significant incidents
- Document root cause analysis, lessons learned, and recommended improvements
- Share lessons learned with relevant teams
- Update the IRP, controls, and risk assessments based on findings
- **Submit the post-incident review to OSFI** as required by the Advisory

### 5.28 — Collection of Evidence

**Purpose:** Ensure management of evidence related to information security incidents.

**Implementation Guidance:**
- Establish evidence handling procedures before an incident occurs
- Preserve logs, forensic images, and other evidence in a manner that maintains chain of custody
- Ensure evidence is admissible for legal proceedings if required
- Maintain detailed records of evidence collected, chain of custody, and storage

---

## 9. Control Attributes — New Feature in 2022

ISO 27002:2022 introduces **control attributes** — a tagging system that allows organisations to filter and view controls through different lenses:

| Attribute Type                      | Values                                                       | Purpose                                      |
|-------------------------------------|--------------------------------------------------------------|----------------------------------------------|
| **Control type**                    | Preventive / Detective / Corrective                          | Classify controls by their security function |
| **Information security properties** | Confidentiality / Integrity / Availability                   | Map controls to the CIA triad                |
| **Cybersecurity concepts**          | Identify / Protect / Detect / Respond / Recover              | Align with NIST CSF functions                |
| **Operational capabilities**        | Governance / Asset management / Protection / etc.            | Operational classification                   |
| **Security domains**                | Governance and Ecosystem / Protection / Defence / Resilience | Domain-level categorisation                  |

### Using Attributes for OSFI Compliance

The **Cybersecurity concepts attribute** (mapping to NIST CSF IDENTIFY/PROTECT/DETECT/RESPOND/RECOVER) enables FRFIs to filter ISO 27002 controls by function — for example, filtering to all RESPOND controls to build out the incident response programme aligned with OSFI Advisory requirements.

---

## 10. Mapping ISO 27002 to ISO 27001 Annex A

ISO 27002:2022 and ISO 27001:2022 Annex A are in **direct 1:1 correspondence**. Key mappings for OSFI-relevant controls:

| ISO 27001 Annex A | ISO 27002                           | OSFI B-13 Principle                | OSFI Advisory Trigger            |
|-------------------|-------------------------------------|------------------------------------|----------------------------------|
| A.5.24            | 5.24 (Incident Management Planning) | P15 (Incident Response)            | C1 (IRP activation)              |
| A.5.25            | 5.25 (Assessment of Events)         | P15, P14                           | D1 (severity classification)     |
| A.5.26            | 5.26 (Incident Response)            | P15                                | 24-hour notification requirement |
| A.5.27            | 5.27 (Learning from Incidents)      | P16 (Recovery and Lessons Learned) | Post-incident review             |
| A.5.7             | 5.7 (Threat Intelligence)           | P12 (Threat and Vulnerability)     | D1 (severity via intelligence)   |
| A.8.16            | 8.16 (Monitoring)                   | P14 (Monitoring and Detection)     | Detection at T+0h                |
| A.5.30            | 5.30 (ICT BCP Readiness)            | P9 (BCP/DR)                        | B4 (DR plan activation)          |

---

## 11. Relevance to OSFI 24-Hour Incident Reporting

### 11.1 The Incident Management Control Chain

ISO 27002 controls 5.24 through 5.28 form an unbroken chain from incident preparation through post-incident review — directly aligning with every phase of the OSFI Advisory reporting lifecycle:

| Phase           | ISO 27002 Control | OSFI Advisory Element                                    |
|-----------------|-------------------|----------------------------------------------------------|
| **Preparation** | 5.24              | Documented CIRP; contact lists including OSFI            |
| **Detection**   | 8.16, 5.25        | Incident detected (T+0h); triage and classification (D1) |
| **Response**    | 5.26              | IRP activated (C1); OSFI notification within 24 hours    |
| **Recovery**    | 5.29, 5.30        | Daily updates to OSFI during recovery                    |
| **Review**      | 5.27              | Post-incident review report to OSFI                      |
| **Evidence**    | 5.28              | Forensic evidence supports root cause in OSFI Form       |

### 11.2 New Controls Particularly Relevant to Incident Prevention and Detection

| ISO 27002:2022 New Control       | Relevance to Incident Reporting                                                              |
|----------------------------------|----------------------------------------------------------------------------------------------|
| **5.7 Threat Intelligence**      | Enables proactive detection of threats before they become incidents — reduces detection time |
| **8.16 Monitoring Activities**   | Core detection capability; SIEM/SOC enabling the T+0h detection event                        |
| **8.12 Data Leakage Prevention** | Prevents unauthorised exfiltration that triggers A5 and D1 criteria                          |
| **5.30 ICT Readiness for BCP**   | BCP/DR activation (Criterion B4) is explicitly addressed by this control                     |

### 11.3 Control 6.8 — Employee Reporting as the First Link in the Chain

**ISO 27002 Control 6.8** (Information Security Event Reporting) establishes the obligation for employees to report observed security events promptly. This is the **first step** in the incident reporting chain that ultimately leads to OSFI notification. Without an effective 6.8 implementation:
- Incidents may not be reported internally
- Detection time is delayed
- The 24-hour OSFI window becomes impossible to meet

### 11.4 ISO 27002 as a Gap Analysis Tool for Incident Response Capability

FRFIs can use ISO 27002:2022 as a **control gap analysis framework** to identify weaknesses in their incident response capability:

1. Filter controls by "Cybersecurity concept: DETECT and RESPOND"
2. Assess current implementation against ISO 27002 guidance
3. Identify gaps that would impair the ability to detect and report incidents within 24 hours
4. Prioritise remediation of gaps in DETECT and RESPOND controls

> 📌 **Summary:** ISO 27002:2022 provides the detailed implementation guidance for the information security controls that underpin OSFI incident reporting. Controls 5.24–5.28 directly operationalise the incident lifecycle required by the OSFI Advisory. The new controls (5.7, 8.16, 8.12, 5.30) are particularly relevant to improving detection capability and reducing time-to-detection — the critical enabler of the 24-hour reporting window.

---

## 12. Cross-References

| Document                             | Relationship                                                                                                                                    |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **ISO 27001:2022**                   | Primary standard; ISO 27002 provides implementation guidance for ISO 27001 Annex A controls                                                     |
| **OSFI B-13**                        | ISO 27002:2022 controls map closely to B-13 P12–P16 (Cybersecurity domain); B-13 can be implemented using ISO 27002 controls as the control set |
| **OSFI Incident Reporting Advisory** | Controls 5.24–5.28 operationalise the IRP required by the Advisory; 6.8 establishes the employee event reporting chain                          |
| **OSFI I&S Guideline**               | Theme 3 (Physical Controls 7.x) aligns with I&S physical security; 6.1 (Screening) aligns with I&S personnel security                           |
| **NIST CSF 2.0**                     | ISO 27002 control attribute "Cybersecurity concepts" maps each control to NIST CSF functions; the two can be used together                      |
| **SOC 2**                            | ISO 27002 Organisational and Technological controls complement SOC 2 CC6 and CC7 criteria                                                       |
| **PIPEDA DERR / Quebec Law 25**      | ISO 27002 5.34 (Privacy and protection of personal information) addresses privacy controls relevant to PIPEDA and Law 25                        |

---

*Source: ISO/IEC 27002:2022 — Information Security Controls*
*Published: February 15, 2022*
*URL: https://www.iso.org/standard/75652.html*
