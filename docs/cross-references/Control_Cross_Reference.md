# Control Cross-Reference: OSFI E-21 × ISO 27001 Annex A × SOC 2 CC × NIST CSF 2.0

> **Purpose:** This matrix cross-references operational risk and cybersecurity controls across four frameworks: OSFI Guideline E-21 (Operational Risk and Resilience), ISO/IEC 27001:2022 Annex A, SOC 2 Trust Services Criteria (Common Criteria), and NIST Cybersecurity Framework 2.0.
>
> **Audience:** Technology Risk Management, CISO Office, Internal Audit, and compliance teams responsible for FRFI regulatory alignment.

---

*Last updated: April 2, 2026*
*Maintained by: Technology Risk Management / CISO Office*

---

## How to Use This Document

| Column | Framework | Reference Format |
|--------|-----------|-----------------|
| **OSFI E-21** | OSFI Guideline E-21 — Operational Risk and Resilience Management | Section number (e.g., §3.2, §5.1) |
| **ISO 27001 Annex A** | ISO/IEC 27001:2022 Annex A (93 controls across 4 themes) | Control number (e.g., A.5.24, A.8.16) |
| **SOC 2 CC** | AICPA Trust Services Criteria — Common Criteria (CC1–CC9) and Availability (A1) | Criterion code (e.g., CC6.1, CC7.3, A1.2) |
| **NIST CSF 2.0** | NIST Cybersecurity Framework 2.0 (six functions) | Function.Category (e.g., GV.RM, PR.AA, RS.CO) |

---

## Control Cross-Reference Matrix

### 1. Governance & Oversight

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Information security / operational risk governance policy | §5 (ORM — three lines of defence) | A.5.1 (Policies for IS), A.5.4 (Management responsibilities) | CC1.1 (Integrity and ethical values), CC5.2 (Control activities) | GV.PO (Policy) |
| Roles, responsibilities & authorities | §5 (ORM governance structure) | A.5.2 (IS roles and responsibilities), A.5.3 (Segregation of duties) | CC1.3 (Organisational structure), CC2.2 (Internal communication) | GV.RR (Roles, Responsibilities, Authorities) |
| Board and senior management oversight | §7 (Proportionality — D-SIBs and large FRFI board-level governance) | A.5.4 (Management responsibilities) | CC1.2 (Board oversight — COSO) | GV.OV (Oversight) |
| Regulatory and legal requirements awareness | §9.1–9.4 (relevance to OSFI incident reporting obligations) | A.5.31 (Legal, statutory, regulatory and contractual requirements), A.5.5 (Contact with authorities) | CC2.3 (External communication) | GV.OC (Organisational Context) |
| Documented operating procedures | §5.2 (Loss data collection processes) | A.5.37 (Documented operating procedures) | CC5.3 (Policies and procedures) | GV.PO (Policy) |
| Proportionality of implementation | §7 (Proportionality Principle — scales by size and complexity) | Clause 4.1 (Context of the organisation) | CC1.3 (Entity-level controls scaled to complexity) | GV.RM (Risk Management Strategy) |

---

### 2. Risk Management & Risk Appetite

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Operational risk identification and assessment (RCSA) | §5.1 (Risk Identification and Assessment) | A.5.7 (Threat intelligence), A.5.8 (IS in project management) | CC3.1 (Risk identification), CC3.2 (Risk assessment and analysis) | ID.RA (Risk Assessment) |
| Risk appetite and tolerance setting | §3.2 (Impact Tolerances — duration, volume, breadth, velocity) | Clause 6.1.2 (Risk Treatment — SoA and risk treatment plan) | CC3.3 (Risk analysis), CC3.4 (Risk mitigation) | GV.RM (Risk Management Strategy) |
| Operational loss data collection | §5.2 (Loss Data — Basel II/III event categories) | A.5.24 (Incident management planning), A.5.27 (Learning from incidents) | CC4.1 (Monitoring activities), CC7.5 (Remediation) | ID.IM (Improvement), GV.OV (Oversight) |
| Key Risk Indicators (KRIs) and threshold monitoring | §5.3 (KRIs — threshold breach may trigger OSFI Criterion D4) | A.8.16 (Monitoring activities), Clause 9.1 (Monitoring and measurement) | CC4.2 (Evaluating deficiencies) | DE.CM (Continuous Monitoring), GV.OV |
| Supply chain and third-party risk | §4.2 (dependency mapping), §6 (third-party failure scenario analysis) | A.5.19–5.22 (Supplier relationships), A.5.23 (Cloud services) | CC9.2 (Vendor risk management) | GV.SC (Supply Chain Risk Management) |
| Risk treatment planning | §5.1 (RCSA output and control decisions) | Clause 6.1.2 (Risk Treatment Plan, SoA) | CC3.4 | GV.RM, ID.RA |

---

### 3. Asset Management

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Critical operations identification (Business Services Analysis) | §4.1–4.3 (Critical Operations — BSA methodology) | A.5.9 (Inventory of information and associated assets) | CC6.1 (Asset identification underpins access control) | ID.AM (Asset Management) |
| Critical operation dependency mapping (technology, people, data, third parties) | §4.2 (Map services, assess criticality, identify dependencies) | A.5.9 (Inventory), A.5.19 (Supplier relationships) | CC6.1, CC9.1 | ID.AM, GV.SC |
| Information asset classification | §5.1 (Risk assessment scope — classify assets by sensitivity) | A.5.12 (Classification of information), A.5.13 (Labelling of information) | CC6.7 (Data protection driven by classification) | PR.DS (Data Security) |
| Acceptable use of information assets | §5 (ORM — policy-driven controls) | A.5.10 (Acceptable use of information and associated assets) | CC1.4 (Commitment to competence and conduct), CC5.1 | GV.PO (Policy) |
| Hardware and software asset inventory | §4.2 (technology dependencies of critical operations) | A.5.9 (Inventory), A.8.1 (User endpoint devices) | CC6.1 | ID.AM |

---

### 4. Human Resources Security

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Personnel screening (pre-employment) | §5 (ORM — insider threat and workforce risk) | A.6.1 (Screening) | CC1.4 (Hiring practices and competence) | GV.RR (Roles and Responsibilities) |
| Security awareness, education and training | §5 (ORM culture), §7 (proportionate training programme) | A.6.3 (IS awareness, education and training) | CC2.2 (Internal communication and awareness) | PR.AT (Awareness and Training) |
| Terms and conditions of employment | §5 (governance framework — employee obligations) | A.6.2 (Terms and conditions of employment), A.6.6 (NDAs/confidentiality agreements) | CC1.4 | GV.PO (Policy) |
| Responsibilities after termination or role change | §5.1 (insider threat — workforce transition risk) | A.6.5 (Responsibilities after termination), A.5.11 (Return of assets) | CC6.3 (Access removal), CC6.5 (Discontinuation of access) | PR.AA (off-boarding dimensions) |
| Disciplinary process | §5 (three lines of defence — accountability) | A.6.4 (Disciplinary process) | CC1.3 (Accountability structures) | GV.RR |
| Staff security event reporting | §9 (incident reporting culture — front-line detection) | A.6.8 (Information security event reporting) | CC7.2 (Evaluating security events) | RS.MA (Incident Management) |

---

### 5. Access Control — Identity, Authentication & Privileged Access

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Access control policy and least privilege | §5 (ORM — access control as a risk mitigant) | A.5.15 (Access control), A.5.18 (Access rights) | CC6.1 (Logical access security measures) | PR.AA (Identity Management, Authentication and Access Control) |
| Identity management | §5 (ORM — personnel identity controls) | A.5.16 (Identity management) | CC6.1, CC6.2 (Credential registration) | PR.AA |
| Multi-factor authentication (MFA) and credential management | §5 (technology risk controls) | A.5.17 (Authentication information), A.8.5 (Secure authentication) | CC6.1 (MFA requirement for remote/privileged) | PR.AA |
| Access provisioning (new users) | §5 (ORM — onboarding process controls) | A.5.18 (Access rights), A.6.2 (Employment terms) | CC6.2 (New access provisioning — approval and documentation) | PR.AA |
| Access removal and periodic recertification | §5.1 (RCSA — stale account and orphaned access risk) | A.5.18 (Access rights review), A.6.5 (Post-termination) | CC6.3 (Access removal and modification), CC6.5 (Discontinuation) | PR.AA |
| Privileged access management (PAM) | §5 (ORM — elevated risk of admin/privileged accounts) | A.8.2 (Privileged access rights), A.8.18 (Privileged utility programs) | CC6.1 (PAM controls — enhanced controls for admin accounts) | PR.AA |
| Remote access security (VPN / ZTNA) | §5, §6 (pandemic/workforce disruption scenarios) | A.6.7 (Remote working), A.8.5 (Secure authentication) | CC6.6 (Remote access — VPN with MFA, ZTNA) | PR.AA, PR.IR |
| Source code access control | §5 (ORM — integrity of technology assets) | A.8.4 (Access to source code) | CC6.1 | PR.AA |

---

### 6. Physical and Environmental Security

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Physical security perimeters | §4.2 (protecting infrastructure supporting critical operations) | A.7.1 (Physical security perimeters) | CC6.4 (Physical access restrictions) | PR.AA (physical access dimensions) |
| Physical access controls (badge readers, biometrics) | §4 (protecting critical operations infrastructure) | A.7.2 (Physical entry) | CC6.4, CC6.5 (Discontinuation of physical access) | PR.AA |
| Physical security monitoring (CCTV, access logs) | §6 (physical disruption and intrusion scenarios) | A.7.4 (Physical security monitoring) | CC6.4 (Physical access logs, cameras, anomaly review) | DE.CM (Continuous Monitoring) |
| Environmental and utility controls | §6 (data centre loss scenario) | A.7.5 (Physical and environmental threats), A.7.11 (Supporting utilities), A.7.12 (Cabling security) | CC6.4 (Environmental monitoring — fire, water, temperature) | PR.IR (Technology Infrastructure Resilience) |
| Secure disposal and storage media controls | §5 (ORM — data destruction and media handling) | A.7.10 (Storage media), A.7.14 (Secure disposal or re-use of equipment) | CC6.7 (Data handling and removal controls), CC6.5 | PR.DS (Data Security) |
| Equipment maintenance and off-premises security | §5 (operational risk — equipment failure) | A.7.8 (Equipment siting and protection), A.7.9 (Assets off-premises), A.7.13 (Equipment maintenance) | CC6.4 | PR.IR |

---

### 7. Data Security & Cryptography

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Encryption in transit (TLS 1.2+) | §5 (ORM — data confidentiality as operational control) | A.8.24 (Use of cryptography) | CC6.7 (Encryption of information in transit) | PR.DS (Data Security) |
| Encryption at rest (AES-256 or equivalent) | §5 (data protection supporting resilience) | A.8.24 (Cryptography), A.8.11 (Data masking) | CC6.7 (Encryption at rest) | PR.DS |
| Cryptographic key management | §5 (technology risk — key lifecycle controls) | A.8.24 (Cryptography — key generation, storage, rotation, destruction) | CC6.7 | PR.DS |
| Data Loss Prevention (DLP) | §5.2 (loss event — unauthorised data exfiltration) | A.8.12 (Data leakage prevention) | CC6.7 (DLP controls), CC6.8 | PR.DS |
| Information backup | §3.2 (impact tolerances), §4 (continuity of critical operations) | A.8.13 (Information backup) | CC7.5 (Recovery), A1.2 (Availability — backup) | RC.RP (Recovery Plan Execution), PR.DS |
| Information transfer controls | §5 (ORM — data in motion) | A.5.14 (Information transfer) | CC6.7 | PR.DS |
| Information deletion and data retention | §5 (ORM — data lifecycle) | A.8.10 (Information deletion) | CC6.5 (Discontinuation), CC6.7 | PR.DS |

---

### 8. Network & Boundary Security

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Network perimeter controls (firewalls, IDS/IPS, DMZ) | §6 (cyberattack scenarios), §8 (B-13 P13 alignment) | A.8.20 (Networks security), A.8.21 (Security of network services) | CC6.6 (Boundary protections — firewalls, IDS/IPS, DMZ) | PR.IR (Technology Infrastructure Resilience), PR.PS |
| Network segmentation | §4.2 (isolating critical operations from lower-trust zones) | A.8.22 (Segregation of networks) | CC6.6 (Segmentation controls) | PR.IR |
| Web application firewall (WAF) | §6 (external attack and web-facing application scenarios) | A.8.23 (Web filtering), A.8.26 (Application security requirements) | CC6.6 (WAF controls) | PR.PS (Platform Security) |
| DDoS protection and mitigation | §6 (DDoS attack scenario), §9.1 (B3 — loss of connectivity trigger) | A.8.14 (Redundancy of information processing), A.8.20 | CC6.6 (DDoS mitigation) | PR.IR |
| Email security (anti-phishing, anti-spoofing) | §6 (cyberattack — phishing as initial access vector) | A.8.23 (Web filtering), A.8.7 (Protection against malware) | CC6.6 (Email security), CC6.8 | PR.PS |
| Third-party and vendor network access | §4.2 (third-party dependencies — access to critical operations), §6 | A.5.19–5.22 (Supplier relationships), A.8.22 (Segregation) | CC6.6 (Vendor access segmentation) | GV.SC, PR.AA |

---

### 9. Endpoint Protection & Malware Prevention

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Antivirus and EDR (Endpoint Detection and Response) | §6 (ransomware and cyberattack scenarios) | A.8.7 (Protection against malware) | CC6.8 (Endpoint protection — AV and EDR on all endpoints) | PR.PS (Platform Security), DE.CM |
| Application allow-listing | §6 (malware prevention for critical systems) | A.8.7 (Malware — allow-listing), A.8.19 (Installation of software on operational systems) | CC6.8 (Allow-listing) | PR.PS |
| Security configuration baselines (hardening) | §5.1 (RCSA — misconfiguration as operational risk) | A.8.9 (Configuration management) | CC6.8 (Security config baselines — CIS Benchmarks or equivalent) | PR.PS |
| Removable media controls | §5 (ORM — data exfiltration and introduction of malware) | A.7.10 (Storage media) | CC6.7 (Removable media encryption), CC6.8 | PR.DS, PR.PS |
| User endpoint device management | §5 (ORM — workforce technology risks) | A.8.1 (User endpoint devices) | CC6.8, CC6.1 | PR.PS |

---

### 10. Vulnerability & Patch Management

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Vulnerability identification and scanning | §5.1 (RCSA — technology vulnerabilities), §6 (technology failure scenarios) | A.8.8 (Management of technical vulnerabilities) | CC6.8 (Vulnerability detection), CC7.5 (Vulnerability remediation) | ID.RA (Risk Assessment), DE.CM |
| Patch management (SLA by severity) | §5 (ORM — technology risk from unpatched systems) | A.8.8 (Vulnerability management — patching SLAs) | CC6.8 (Timely patching) | PR.PS (Platform Security) |
| Software composition analysis (SCA) | §6 (technology and supply chain risk scenarios) | A.8.8, A.5.21 (ICT supply chain), A.8.30 (Outsourced development) | CC6.8 (SCA for third-party libraries), CC9.2 | ID.RA, GV.SC |
| Threat intelligence to inform vulnerability prioritisation | §6 (scenario analysis — intelligence-driven) | A.5.7 (Threat intelligence) | CC3.2 (Threat assessment and analysis) | ID.RA, DE.AE |

---

### 11. Secure Configuration & Change Management

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Change management process | §5 (ORM — change as a source of operational failures) | A.8.32 (Change management) | CC8.1 (Change management authorisation and testing) | PR.PS (Platform Security) |
| Separation of development, test and production environments | §5 (ORM — integrity of production systems) | A.8.31 (Separation of dev, test, and production environments) | CC8.1 | PR.PS |
| Secure software development lifecycle (SDLC) | §5 (technology risk — software quality and security) | A.8.25 (Secure development lifecycle), A.8.28 (Secure coding), A.8.29 (Security testing) | CC8.1 | PR.PS |
| Capacity management | §3.2 (impact tolerances — volume and transaction thresholds) | A.8.6 (Capacity management) | A1.2 (Availability — capacity commitments) | PR.IR (Technology Infrastructure Resilience) |
| Security in project management | §5 (ORM — new initiatives introduce risk) | A.5.8 (IS in project management) | CC8.1 | PR.PS, GV.RM |

---

### 12. Third-Party & Supply Chain Risk Management

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Supplier security requirements and contracts | §4.2 (third-party dependencies in critical operations), §8 (B-10 alignment) | A.5.19 (IS in supplier relationships), A.5.20 (IS in supplier agreements) | CC9.2 (Vendor risk management) | GV.SC (Supply Chain Risk Management) |
| ICT supply chain risk management | §6 (third-party failure scenario) | A.5.21 (Managing IS in the ICT supply chain), A.5.22 (Monitoring and reviewing supplier services) | CC9.2 | GV.SC |
| Cloud services security | §6 (cloud provider extended outage scenario) | A.5.23 (IS for use of cloud services) | CC6.6 (Third-party connectivity), CC9.2 | GV.SC, PR.IR |
| Third-party access controls | §4.2 (vendor access to systems supporting critical operations) | A.5.19, A.8.22 (Segregation for vendor access), A.5.18 | CC6.6 (Vendor network segmentation), CC6.2 | PR.AA, GV.SC |
| Third-party assurance (SOC 2 / ISO 27001 certificates) | §8 (B-10 relationship — third-party due diligence) | A.5.22 (Monitoring and reviewing supplier services) | CC9.2 (SOC 2 reports as assurance evidence) | GV.SC |
| Outsourced development security | §5 (ORM — supply chain software risk) | A.8.30 (Outsourced development) | CC8.1, CC9.2 | GV.SC, PR.PS |

---

### 13. Business Continuity & Operational Resilience

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Business Continuity Planning (BCP) and Disaster Recovery (DR) | §3 (Operational Resilience Framework), §8 (B-13 P9 alignment) | A.5.29 (IS during disruption), A.5.30 (ICT readiness for business continuity) | A1.3 (Recovery procedures and testing) | PR.IR (Technology Infrastructure Resilience), RC.RP |
| Impact tolerance definition (duration, volume, breadth, velocity) | §3.2 (Impact Tolerances — core E-21 requirement) | A.5.30 (ICT readiness), A.8.14 (Redundancy) | A1.2 (Availability commitments and metrics) | PR.IR, GV.RM |
| Critical operations continuity capability | §4.1–4.3 (Critical Operations — defining and protecting) | A.5.29 (IS during disruption), A.5.30 | A1.2, A1.3 | RC.RP, PR.IR |
| RTO and RPO targets | §3.2 (impact tolerance drives RTO/RPO), §8 (B-13 P9 sets technical RTO/RPO) | A.5.30 (ICT readiness — RTOs in BCP) | A1.2 | RC.RP, PR.IR |
| Redundancy of information processing facilities | §3.2 (impact tolerances), §6 (data centre loss scenario) | A.8.14 (Redundancy of information processing) | A1.2 (Availability — redundancy) | PR.IR |
| BCP and DR testing and exercises | §6 (Scenario Analysis and Stress Testing — E-21 core requirement) | A.5.30 (ICT readiness — BCP testing) | A1.3 (Recovery testing and validation) | RC.RP, ID.IM (Improvement) |

---

### 14. Scenario Analysis & Stress Testing

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Scenario analysis programme (severe but plausible) | §6 (Scenario Analysis and Stress Testing — E-21 core requirement) | A.5.30 (BCP readiness testing), A.5.7 (Threat intelligence) | CC3.2 (Risk analysis using scenarios) | ID.RA (Risk Assessment) |
| Cyberattack scenarios (ransomware, DDoS, APT) | §6 (Cyber Attack category) | A.5.7 (Threat intelligence), A.8.7 (Malware protection) | CC6.8 (Malware prevention), CC7.3 (IR execution) | DE.AE (Adverse Event Analysis), ID.RA |
| Technology failure scenarios (core system outage, cloud failure) | §6 (Technology Failure category) | A.5.30 (ICT readiness for BCP), A.8.14 (Redundancy) | A1.2 (Availability), CC7.1 (Monitoring) | PR.IR |
| Third-party failure scenarios (vendor insolvency, extended outage) | §6 (Third-Party Failure category) | A.5.19–5.22 (Supplier relationships) | CC9.2 (Vendor risk and contingency) | GV.SC, ID.RA |
| Concurrent event scenarios (cyber + high-volume trading) | §6 (Concurrent Events category) | A.5.29 (IS during disruption) | CC3.4 (Risk mitigation — combined stress) | ID.RA, PR.IR |
| Regulatory notification included in scenario testing | §9.4 (scenario testing must include regulatory notification step) | A.5.24 (IRP planning), A.5.26 (IR response — communication) | CC7.4 (Incident notification to regulators) | RS.CO (Response Communications) |

---

### 15. Security Monitoring & Detection

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| SIEM and log management | §5.3 (KRI monitoring and KRI breach detection), §9.1 | A.8.15 (Logging), A.8.16 (Monitoring activities), A.8.17 (Clock synchronisation) | CC7.1 (Security event monitoring and detection) | DE.AE (Adverse Event Analysis) |
| Continuous security monitoring | §5.3 (KRI thresholds — ongoing surveillance) | A.8.16 (Monitoring activities) | CC7.1, CC4.1 (Ongoing monitoring — COSO) | DE.CM (Continuous Monitoring) |
| Network and user behaviour monitoring (UEBA/NDR) | §5.3 (anomaly detection — KRI triggers) | A.8.16 (Monitoring), A.5.7 (Threat intelligence) | CC7.1, CC7.2 (Evaluating events for significance) | DE.AE, DE.CM |
| Vulnerability scanning and monitoring | §5.1 (RCSA — technology risk), §6 (scenario-informed risk monitoring) | A.8.8 (Vulnerability management) | CC7.1, CC6.8 | DE.CM, ID.RA |
| KRI threshold breach alerts | §5.3 (KRI breach is an OSFI Criterion D4 reporting trigger) | A.8.16 (Monitoring), A.5.35 (Independent review) | CC4.2 (Deficiency evaluation and escalation) | DE.CM, GV.OV |
| Threat intelligence integration | §6 (scenario analysis informed by intelligence) | A.5.7 (Threat intelligence) | CC3.2 (Threat assessment) | DE.AE, ID.RA |

---

### 16. Incident Management & Response

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Incident Response Plan (IRP / CIRP) | §9.1 (IRP activation → OSFI Criterion C1 reporting trigger) | A.5.24 (IS incident management planning and preparation) | CC7.3 (Incident response procedures) | RS.MA (Incident Management) |
| Incident classification and triage | §9.1 (mapping E-21 operational risk categories to OSFI Advisory triggers) | A.5.25 (Assessment and decision on IS events) | CC7.2 (Evaluating security events for significance) | RS.AN (Incident Analysis) |
| Incident containment and eradication | §9.1 (operational disruption management — contain to within impact tolerances) | A.5.26 (Response to IS incidents — contain, eradicate, recover) | CC7.3 (Incident response — containment and eradication) | RS.MI (Incident Mitigation) |
| Evidence collection and forensic preservation | §9.3 (supporting investigation of impact tolerance breach events) | A.5.28 (Collection of evidence — chain of custody) | CC7.3 (Evidence during incident response) | RS.AN |
| Impact tolerance breach as high-severity incident | §9.3 (IT breach → Advisory Criteria D1, A4, A6) | A.5.25 (Severity classification), A.5.26 (Response) | CC7.2, CC7.3 | RS.AN, RS.MA |
| Incident coordination across business units | §5 (three lines of defence — coordinated response) | A.5.24 (IRP — roles: incident commander, CISO, legal, comms) | CC7.3 | RS.MA |

---

### 17. Regulatory Notification & External Communication

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| 24-hour OSFI incident notification obligation | §9.1–9.3 (operational disruptions are reportable — A4, A6, B1, B5, B6 triggers) | A.5.26 (Response — regulatory notification embedded in IRP) | CC7.4 (Incident notification to stakeholders and regulators) | RS.CO (Incident Response Reporting and Communication) |
| 12-hour internal escalation threshold | §9.2 (KRI breach escalation — internal threshold precedes OSFI notification) | A.5.24 (IRP — escalation procedures), A.5.25 (Severity classification) | CC7.4 | RS.CO, RS.MA |
| Contact with regulators and authorities | §9 (OSFI reporting obligations — TRD and Lead Supervisor) | A.5.5 (Contact with authorities) | CC2.3 (External communication obligations) | RS.CO |
| Customer and stakeholder communication during incidents | §9.4 (communication with customers, counterparties, financial system) | A.5.26 (Response — communication protocols) | CC7.4 (Notification to affected parties) | RS.CO |
| Daily OSFI updates during ongoing incident recovery | §9.4 (subsequent reporting obligations — daily updates) | A.5.26 (Ongoing response communication) | CC7.4 | RC.CO (Incident Recovery Communication) |

---

### 18. Recovery & Post-Incident Review

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Recovery from critical operation disruption (return within impact tolerances) | §3.2 (demonstrating recovery within impact tolerances), §4 (protecting critical operations) | A.5.29 (IS during disruption), A.5.30 (ICT readiness for BCP) | CC7.5 (Root cause and remediation), A1.3 (Recovery) | RC.RP (Incident Recovery Plan Execution) |
| Recovery status communication | §9.4 (subsequent reporting to OSFI during recovery phase) | A.5.26 (Response communication), A.5.27 (Learning) | CC7.4 | RC.CO (Recovery Communication) |
| Post-incident review and lessons learned | §9.4 (scenario testing informs ISMS improvements), §6 (lessons feed back to scenario programme) | A.5.27 (Learning from IS incidents) | CC7.5 (Root cause analysis and remediation) | ID.IM (Improvement), RC.CO |
| ORM and ISMS programme improvement | §5 (ORM — continuous improvement cycle), §2 (phased implementation) | Clause 10 (Continual Improvement), A.5.27 | CC4.2 (Deficiency correction), CC5.3 | ID.IM |
| Root cause analysis | §5.1 (RCSA — update risk and control assessment post-incident) | A.5.27 (Lessons learned), A.5.28 (Evidence collection) | CC7.5 | ID.IM, RS.AN |

---

### 19. Audit, Compliance & Continuous Improvement

| Control Topic | OSFI E-21 | ISO 27001 Annex A | SOC 2 CC | NIST CSF 2.0 |
|---|---|---|---|---|
| Independent review of security and risk controls | §5 (three lines of defence — Internal Audit as third line) | A.5.35 (Independent review of IS) | CC4.1–4.2 (Monitoring activities — COSO) | GV.OV (Oversight) |
| Compliance with policies, rules and standards | §5 (ORM — regulatory compliance risk category) | A.5.36 (Compliance with policies, rules and standards for IS) | CC5.2 (Control activities) | GV.PO (Policy), GV.OV |
| Management review of security and risk performance | §5.3 (Board and senior management KRI reporting) | Clause 9.3 (Management Review) | CC4.2 (Evaluating deficiencies), CC2.2 | GV.OV |
| Internal audit of ORM and ISMS | §5 (three lines — second and third line oversight roles) | Clause 9.2 (Internal Audit programme) | CC4.1 | GV.OV, ID.IM |
| Protection of systems during audit testing | §5 (ORM — operational risk during audit activities) | A.8.34 (Protection of IS during audit testing) | CC4.1 | GV.OV |
| Continuous improvement of the risk and resilience framework | §2 (Phased Implementation), §5 (ORM evolution), §6 (lessons from scenarios) | Clause 10.2 (Continual Improvement) | CC4.2 | ID.IM (Improvement) |

---

## Summary Mapping: OSFI E-21 Sections to Framework Functions

| OSFI E-21 Section | Primary ISO 27001 Theme | Primary SOC 2 CC | Primary NIST CSF Function |
|---|---|---|---|
| §3 — Operational Resilience Framework | A.5.29–5.30 (Organisational — BCP/Resilience) | CC7 (System Operations), A1 (Availability) | RECOVER (RC), PROTECT (PR.IR) |
| §4 — Critical Operations | A.5.9 (Asset Inventory), A.5.30 (ICT readiness) | CC6.1, A1 | IDENTIFY (ID.AM), PROTECT (PR.IR) |
| §5 — Operational Risk Management | A.5 (Organisational), A.6 (People), A.8 (Technological) | CC1–CC5 (COSO), CC6, CC7 | GOVERN (GV), IDENTIFY (ID), PROTECT (PR) |
| §5.3 — Key Risk Indicators (KRIs) | A.8.15–8.16 (Logging and Monitoring) | CC4 (Monitoring Activities), CC7.1 | DETECT (DE.CM), GOVERN (GV.OV) |
| §6 — Scenario Analysis and Stress Testing | A.5.7 (Threat Intelligence), A.5.30 (BCP) | CC3 (Risk Assessment), CC7 | IDENTIFY (ID.RA), RECOVER (RC.RP) |
| §7 — Proportionality Principle | Clause 4.1 (Context), Clause 6.1.2 (Risk Treatment) | CC1.3 (Organisational structure scaled to complexity) | GV.RM (Risk Management Strategy) |
| §8 — Relationship to B-10 and B-13 | A.5.19–5.22 (Supplier), A.5.23 (Cloud) | CC9.2 (Vendor risk), CC6.6 | GV.SC (Supply Chain Risk Management) |
| §9 — OSFI Incident Reporting Relevance | A.5.24–5.28 (Incident Management lifecycle) | CC7.3–7.4 (IR and Regulatory Notification) | RESPOND (RS.CO), DETECT (DE) |

---

## Quick-Reference: OSFI Advisory Triggers Mapped to Preventive and Detective Controls

| OSFI Trigger | E-21 Category | ISO 27001 Annex A | SOC 2 CC | NIST CSF |
|---|---|---|---|---|
| **A4** — Impact to FRFI operations or infrastructure | §9.1 — Business Disruption and System Failures | A.5.29 (IS during disruption), A.5.30 (BCP) | CC7.1 (Monitoring), CC7.3 (IR) | DE.AE, RS.MA |
| **A5** — Customer information CIA (confidentiality, integrity, availability) breach | §5.2 — Loss event (data breach category) | A.5.12 (Classification), A.5.24–5.26 (Incident management), A.8.24 (Cryptography) | CC6.1 (Access), CC6.7 (Encryption), CC6.8 (Malware) | PR.DS, RS.CO |
| **A6** — Operational impact to key or critical systems | §4.3, §9.3 — Impact tolerance breach on critical operation | A.5.29 (IS during disruption), A.5.30 (BCP), A.5.24 (IRP) | CC7.3 (IR), A1.2 (Availability) | RC.RP, RS.MA |
| **B1** — Disruption to business systems or operations | §5.2 — Business Disruption and System Failures (Basel category) | A.5.29 (IS during disruption), A.8.14 (Redundancy) | CC7.3 (IR execution) | PR.IR, RS.MI |
| **B3** — Loss of external connectivity | §6 — DDoS attack or connectivity failure scenario | A.8.14 (Redundancy), A.8.20 (Network security) | CC6.6 (DDoS mitigation), CC7.1 | PR.IR, DE.CM |
| **B5 / B6** — Third-party incident affecting the FRFI | §4.2, §6 — Third-Party Failure scenario | A.5.19–5.22 (Supplier relationships), A.5.23 (Cloud) | CC9.2 (Vendor risk), CC6.6 (Connectivity) | GV.SC, RS.CO |
| **C1** — IRP activated | §9.1 — IRP activation is itself an OSFI reporting trigger | A.5.24 (IRP planning and preparation) | CC7.3 (IR activation) | RS.MA (Incident Management) |
| **D1** — FRFI-assessed high or critical severity | §9.3 — Impact tolerance breach → D1 trigger | A.5.25 (Severity classification and decision) | CC7.2 (Evaluating significance) | RS.AN (Incident Analysis) |
| **D4** — KRI or risk appetite threshold breach | §5.3 — KRI threshold breach is an OSFI reporting trigger | A.8.16 (Monitoring activities), A.5.35 (Independent review) | CC4.2 (Deficiency evaluation) | DE.CM, GV.OV |

---

## Legend

| Abbreviation | Full Reference |
|---|---|
| **E-21 §** | OSFI Guideline E-21 — Operational Risk and Resilience Management, Section reference |
| **A.5.x** | ISO/IEC 27001:2022 Annex A — Organisational Controls (37 controls) |
| **A.6.x** | ISO/IEC 27001:2022 Annex A — People Controls (8 controls) |
| **A.7.x** | ISO/IEC 27001:2022 Annex A — Physical Controls (14 controls) |
| **A.8.x** | ISO/IEC 27001:2022 Annex A — Technological Controls (34 controls) |
| **CC1** | SOC 2 TSC — Control Environment (COSO) |
| **CC2** | SOC 2 TSC — Communication and Information |
| **CC3** | SOC 2 TSC — Risk Assessment (COSO) |
| **CC4** | SOC 2 TSC — Monitoring Activities (COSO) |
| **CC5** | SOC 2 TSC — Control Activities (COSO) |
| **CC6** | SOC 2 TSC — Logical and Physical Access Controls |
| **CC7** | SOC 2 TSC — System Operations |
| **CC8** | SOC 2 TSC — Change Management |
| **CC9** | SOC 2 TSC — Risk Mitigation |
| **A1** | SOC 2 TSC — Availability Category (supplemental) |
| **GV** | NIST CSF 2.0 — GOVERN Function |
| **ID** | NIST CSF 2.0 — IDENTIFY Function |
| **PR** | NIST CSF 2.0 — PROTECT Function |
| **DE** | NIST CSF 2.0 — DETECT Function |
| **RS** | NIST CSF 2.0 — RESPOND Function |
| **RC** | NIST CSF 2.0 — RECOVER Function |

---

## Related Documents

- [OSFI E-21 — Operational Risk and Resilience Management](./compliance-docs/Resources/OSFI_E-21_Operational_Risk_Management.md)
- [ISO/IEC 27001:2022 — Information Security Management Systems](./compliance-docs/Resources/ISO_27001_ISMS_Standard.md)
- [ISO/IEC 27002:2022 — Information Security Controls](./compliance-docs/Resources/ISO_27002_Security_Controls.md)
- [SOC 2 — CC6 Logical and Physical Access Controls](./compliance-docs/Resources/SOC2_CC6_Logical_Physical_Access.md)
- [NIST Cybersecurity Framework 2.0](./compliance-docs/Resources/NIST_CSF_Cybersecurity_Framework.md)
- [OSFI Incident Reporting Advisory](./compliance-docs/Resources/OSFI_Incident_Response_Advisory.md)
- [OSFI Incident Reporting Trigger Criteria](./compliance-docs/OSFI_Incident_Reporting_Trigger_Criteria.md)

---

*Last updated: April 2, 2026*
*Maintained by: Technology Risk Management / CISO Office*

