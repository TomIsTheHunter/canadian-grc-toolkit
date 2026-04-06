---
Document:        OSFI Guideline E-23 – Model Risk Management
Issuer:          Office of the Superintendent of Financial Institutions (OSFI)
Effective Date:  Active (see OSFI guidance library for current version date)
Last Verified:   April 2, 2026
Status:          Active
Type:            Mandatory – FRFI
Official URL:    https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/model-risk-management-guideline
---

# OSFI Guideline E-23 — Model Risk Management

> **Document Type:** Regulatory Guideline
> **Issuer:** OSFI
> **Applies To:** All federally regulated financial institutions (FRFIs) that use models for risk measurement, financial reporting, decision-making, or regulatory capital purposes

---

## Table of Contents

1. [Overview](#1-overview)
2. [Definition of a Model](#2-definition-of-a-model)
3. [Model Risk Governance](#3-model-risk-governance)
4. [Model Development and Implementation](#4-model-development-and-implementation)
5. [Model Validation](#5-model-validation)
6. [Model Inventory and Tiering](#6-model-inventory-and-tiering)
7. [Ongoing Monitoring and Model Performance](#7-ongoing-monitoring-and-model-performance)
8. [Model Failure and Operational / Cyber Risk Intersection](#8-model-failure-and-operational--cyber-risk-intersection)
9. [Relevance to OSFI 24-Hour Incident Reporting](#9-relevance-to-osfi-24-hour-incident-reporting)
10. [Cross-References](#10-cross-references)

---

## 1. Overview

OSFI Guideline E-23 establishes the framework for **model risk management (MRM)** at FRFIs — the identification, assessment, mitigation, and governance of risks arising from the use of models in business decision-making, risk management, financial reporting, and regulatory capital calculation.

Model risk is the potential for adverse consequences of decisions based on incorrect or misused model output. As FRFIs increasingly rely on sophisticated quantitative models (including AI/ML models), model risk management has grown in importance as a cross-cutting operational risk discipline.

### Why Models Matter for Technology and Cyber Risk

While E-23 is primarily a quantitative risk guideline, it intersects with technology and cyber risk management through:
- **Model infrastructure:** Models run on IT systems whose availability and integrity are critical
- **Model data:** Models depend on data whose confidentiality and integrity must be protected
- **AI/ML models:** Machine learning models introduce novel failure modes that overlap with cybersecurity concerns (adversarial attacks, data poisoning)
- **Operational impact:** Model failures can cause significant operational disruptions triggering incident reporting obligations

---

## 2. Definition of a Model

E-23 defines a **model** as a quantitative method, system, or approach that:
- Applies statistical, economic, financial, or mathematical theories or techniques
- Processes input data into quantitative estimates or classifications
- Is used in business decision-making, risk assessment, financial reporting, or regulatory capital calculation

### Scope of Model Types

| Model Category                   | Examples                                                                                   |
|----------------------------------|--------------------------------------------------------------------------------------------|
| **Risk Models**                  | Credit scoring, market risk VaR, operational risk AMA models, stress testing models        |
| **Financial Models**             | Loan pricing, IFRS 9 impairment (ECL), fair value models                                   |
| **Regulatory Capital Models**    | IRB credit risk, advanced IMA market risk, AMA operational risk                            |
| **AI / Machine Learning Models** | Fraud detection, anti-money laundering (AML) transaction monitoring, customer segmentation |
| **Decision Models**              | Automated lending decisions, investment recommendation engines                             |

---

## 3. Model Risk Governance

### 3.1 Board and Senior Management Accountability

- **Board** approves the MRM framework and risk appetite for model risk
- **Senior Management** is accountable for implementing the MRM framework and ensuring adequate resources
- The **Chief Risk Officer (CRO)** or equivalent typically owns the MRM function at the enterprise level

### 3.2 Three Lines of Defence for Model Risk

| Line            | Role                                                                                                                                      |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **First Line**  | Model developers and business owners; responsible for model documentation, development quality, and day-to-day performance monitoring     |
| **Second Line** | Model validation / MRM function; independent of model development; responsible for challenging models and maintaining the model inventory |
| **Third Line**  | Internal audit; provides independent assurance over the MRM framework                                                                     |

### 3.3 Model Risk Committee

Best practice under E-23 is a dedicated **Model Risk Committee (MRC)** or equivalent governance body that:
- Approves material models before production deployment
- Reviews validation findings and tracks remediation
- Escalates model risk concerns to the Board Risk Committee
- Oversees the model inventory and tiering process

---

## 4. Model Development and Implementation

E-23 establishes expectations for the **model development lifecycle**:

### Development Standards
- Models must be developed by qualified staff with appropriate expertise
- Development must follow documented standards including conceptual soundness review, data quality assessment, and assumption documentation
- Model documentation must be comprehensive and updated with each material change

### Implementation Controls
- Pre-production testing and parallel run (where feasible)
- User acceptance testing (UAT) with documented results
- Change management controls for model modifications (aligns with B-13 P8)
- Version control for model code and parameters

### AI/ML-Specific Expectations
For AI/ML models, E-23 (read alongside OSFI's broader expectations) requires:
- Explainability and interpretability documentation
- Bias and fairness assessment
- Data provenance and lineage documentation
- Concept drift monitoring plans
- Adversarial robustness assessment for models with significant decision impact

---

## 5. Model Validation

**Model validation** is the process of independently assessing whether a model is conceptually sound, performs as intended, and is being used appropriately.

### Validation Requirements

| Requirement       | Description                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Independence**  | Validation must be performed by personnel independent of model development (second line or external validator)                       |
| **Scope**         | Covers conceptual soundness, data quality, model performance, and implementation integrity                                           |
| **Frequency**     | Initial validation before production; periodic revalidation (at minimum annually for material models, or following material changes) |
| **Documentation** | Formal validation reports with findings, limitations, and recommendations                                                            |
| **Follow-up**     | Findings must be tracked and remediated; outstanding issues escalated to MRC                                                         |

### Validation Findings and Compensating Controls

When validation reveals material weaknesses:
- **Restrictions on use** may be imposed pending remediation
- **Compensating controls** (e.g., conservative buffers, manual overrides) must be documented
- **Escalation to Senior Management** required for high-severity findings

---

## 6. Model Inventory and Tiering

FRFIs must maintain a **complete, current model inventory** covering all models in production:

### Tiering Framework

| Tier                | Description                                                                                      | Governance                                                        |
|---------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| **Tier 1 (High)**   | Material impact on financial results, regulatory capital, or critical decisions; high complexity | Full validation, senior governance oversight, annual revalidation |
| **Tier 2 (Medium)** | Moderate operational or financial impact                                                         | Regular validation cycle, MRC oversight                           |
| **Tier 3 (Low)**    | Limited scope, impact, or complexity                                                             | Periodic review, streamlined validation                           |

The model inventory integrates with:
- B-13 technology asset management (P6) — models are technology assets
- Change management processes (B-13 P8) — model changes go through change control
- BCP/DR planning (B-13 P9) — Tier 1 models may be designated as critical systems

---

## 7. Ongoing Monitoring and Model Performance

FRFIs must monitor model performance on an ongoing basis:

### Performance Monitoring
- **Outcome analysis / backtesting:** Compare model predictions to actual outcomes
- **Population stability monitoring:** Detect drift in the data distribution used for predictions
- **Sensitivity analysis:** Assess model behaviour under changing conditions
- **Limit and threshold monitoring:** Trigger alerts when performance degrades below acceptable thresholds

### Model Risk KRIs
Common model risk KRIs include:
- Number of Tier 1 models with outstanding high-severity validation findings
- Number of models past their scheduled revalidation date
- Model performance (e.g., Gini coefficient for credit models) relative to benchmark
- Percentage of models with complete, current documentation

---

## 8. Model Failure and Operational / Cyber Risk Intersection

### 8.1 Model Failures as Operational Risk Events

Model failures (incorrect outputs, system failures, data errors) are classified as **operational risk events** under E-21. Material model failures may:
- Cause erroneous financial calculations affecting financial statements
- Lead to incorrect regulatory capital measurements
- Result in credit or investment decisions with significant financial loss
- Affect customers (e.g., erroneous credit decisions, incorrect charges)

### 8.2 Model Infrastructure as a Cyberattack Target

Models — particularly AI/ML models — represent high-value targets for sophisticated cyber adversaries:

| Attack Vector                | Description                                                                        | Relevance                                                                   |
|------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Data poisoning**           | Manipulation of training data to corrupt model outputs                             | Affects model integrity; may be an unreported cyber incident                |
| **Adversarial examples**     | Carefully crafted inputs designed to fool ML models (e.g., fraud detection bypass) | Operational and financial loss; may not trigger traditional security alerts |
| **Model theft / extraction** | Querying a model to reconstruct its logic                                          | Intellectual property and competitive risk                                  |
| **Model inversion**          | Reconstructing training data from model outputs                                    | Privacy risk; may trigger PIPEDA/Quebec Law 25 breach obligations           |
| **Infrastructure attack**    | Cyber attack on the systems running models                                         | Availability impact; triggers OSFI incident reporting                       |

### 8.3 Model Failure Scenarios Triggering Incident Reporting

The following model failure scenarios may individually trigger OSFI incident reporting:

| Scenario                                                                      | Incident Reporting Trigger                                                    |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| AML/fraud detection model failure enabling undetected fraud                   | A4 (impact to FRFI operations), A5 (customer information), D1 (high severity) |
| Core banking interest calculation model error affecting all customer accounts | A5 (customer information), D2 (growing customer impact), D1 (high severity)   |
| Regulatory capital model failure causing material misstatement                | D1 (critical severity), C2 (Board/Exec notification)                          |
| Cyber attack causing model infrastructure outage                              | B1 (system disruption), A6 (key/critical system), C1 (CIRP activation)        |

---

## 9. Relevance to OSFI 24-Hour Incident Reporting

### 9.1 Model Failures Are Operational Risk Events

E-23 model risk events that cause significant operational or financial impact may directly trigger OSFI incident reporting under the Advisory. The connection runs through E-21 (operational risk) and B-13 (technology/cyber):

- **Model infrastructure failures** (system outages affecting model availability) → B1, A6 triggers
- **Model output failures causing customer harm** → A4, A5, D2 triggers
- **Cyber attacks targeting model systems** → A4, A6, C1 triggers

### 9.2 AI/ML Models and Emerging Cyber Threat Vectors

As FRFIs increasingly deploy AI/ML models for critical functions (AML, fraud, credit), cyberattacks targeting these models (data poisoning, adversarial examples) may not trigger traditional security monitoring alerts, creating a **detection gap**. FRFIs must ensure their B-13 Principle 14 monitoring capabilities are extended to cover AI/ML model integrity monitoring.

### 9.3 Board Escalation for Material Model Events

Material model failures typically require escalation to the Board Risk Committee or Senior Management under E-23 governance expectations. Such escalation is itself an OSFI incident reporting trigger under **Criterion C2** (incident reported to Board/Senior Management).

### 9.4 Integration with Incident Response Planning

FRFIs should include **Tier 1 model failure scenarios** in their B-13 Cyber Incident Response Plan (P15) and E-21 scenario analysis. The response plan should include:
- Criteria for declaring a model incident
- Escalation path from the MRM function to the incident response team
- Criteria for triggering OSFI notification for model-related incidents
- Communication protocols for model incidents affecting customers

> 📌 **Summary:** E-23 intersects with incident reporting primarily through (a) model infrastructure failures as technology incidents, (b) model-caused customer harm as reportable operational events, and (c) AI/ML model integrity attacks as emerging cyber threats. FRFIs must ensure their incident response and monitoring programmes encompass model risk scenarios.

---

## 10. Cross-References

| Document                             | Relationship                                                                                                                               |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **OSFI B-13**                        | Model systems are technology assets (P6); model changes require change management (P8); critical model infrastructure requires BCP/DR (P9) |
| **OSFI E-21**                        | Model failures are operational risk events; loss data collection covers model failures                                                     |
| **OSFI Incident Reporting Advisory** | Material model failures may trigger reporting under multiple criteria                                                                      |
| **OSFI Corporate Governance**        | Board accountability for model risk appetite and oversight                                                                                 |
| **PIPEDA DERR / Quebec Law 25**      | Model inversion attacks may constitute a privacy breach                                                                                    |
| **ISO 27001**                        | ISMS controls protect model infrastructure and data integrity                                                                              |

---

*Source: OSFI Guideline E-23 — Model Risk Management*
*URL: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/model-risk-management-guideline*
