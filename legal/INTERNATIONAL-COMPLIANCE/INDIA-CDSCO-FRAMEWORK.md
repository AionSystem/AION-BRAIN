# India CDSCO Regulatory Framework

**Document Classification:** International Regulatory Compliance  
**Version:** 1.0  
**Effective Date:** November 2025  
**Jurisdiction:** Republic of India  
**License:** Apache License 2.0 with NOTICE file  
**Document Governance:** Regulatory Engine v2.5 (Multi-Jurisdictional Intelligence) + Legal Engine 2 v1.5 (Systematic Compliance Analysis)

---

## Purpose

This document provides guidance on regulatory considerations for AION-BRAIN cognitive infrastructure within the Indian regulatory framework, specifically under the Central Drugs Standard Control Organisation (CDSCO) Medical Devices Rules 2017 and the October 2025 Draft Guidance on Medical Device Software.

**FUNDAMENTAL PRINCIPLE:** AION-BRAIN provides research frameworks and prompt engineering resources only. Users deploying applications in India must ensure compliance with all applicable CDSCO regulations and obtain appropriate licenses.

---

## Regulatory Authority

### Central Drugs Standard Control Organisation (CDSCO)

| Aspect | Details |
|--------|---------|
| Authority | Central Drugs Standard Control Organisation under Ministry of Health and Family Welfare |
| Primary Legislation | Medical Devices Rules 2017 (MDR 2017) |
| SaMD Guidance | Draft Guidance on Medical Device Software (October 2025) |
| Data Protection | Digital Personal Data Protection Act 2023 (DPDP Act) |
| Website | https://cdsco.gov.in |

### Key Regulatory Milestones

| Date | Development |
|------|-------------|
| February 2020 | S.O. 648(E) expanded medical device definition to include software |
| September 2021 | Official SaMD classification guidelines (IMDRF-harmonized) |
| 2023 | Digital Personal Data Protection Act enacted |
| 2024 | India joined IMDRF as affiliate member |
| October 2025 | 76-page Draft Guidance on Medical Device Software released |
| November 2025 | FAQ Addendum 03 on import licenses and post-approval changes |

---

## AION-BRAIN Positioning Under Indian Law

### Classification Analysis

| Classification Element | AION-BRAIN Position |
|------------------------|---------------------|
| Software Category | Not SaMD or SiMD - Research framework only |
| Medical Device Status | Not a medical device under MDR 2017 |
| Manufacturer Status | Not a medical device manufacturer |
| Regulatory Pathway | No CDSCO registration required for framework itself |
| User Implementation | Users must independently assess their implementations |

### Regulatory Framework Overview

```
CDSCO MEDICAL DEVICE SOFTWARE CLASSIFICATION

Software in Medical Device (SiMD)          Software as Medical Device (SaMD)
        │                                           │
        ▼                                           ▼
Embedded in physical device              Standalone software performing
(e.g., insulin pump software)            medical functions
        │                                           │
        ▼                                           ▼
    Regulated as                          Risk-based classification:
    medical device                        Class A, B, C, or D
                                                    │
                                                    ▼
                                          AION-BRAIN: Research framework
                                          NOT classified as SaMD
                                          User implementations require
                                          independent classification
```

---

## Risk Classification Under CDSCO

### IMDRF-Harmonized Classification

| Class | Risk Level | Licensing Authority | Examples |
|-------|------------|---------------------|----------|
| Class A | Low risk | State Licensing Authority | Wellness apps, administrative software |
| Class B | Low-to-moderate | State Licensing Authority | Clinical decision support (non-critical) |
| Class C | Moderate-to-high | CDSCO Central Authority | Diagnostic imaging analysis |
| Class D | High risk | CDSCO Central Authority | Life-sustaining device software |

### AION-BRAIN User Implementation Considerations

Users implementing AION-BRAIN frameworks in India must:

1. **Determine Software Category:**
   - Assess if implementation qualifies as SiMD or SaMD
   - AION-BRAIN research frameworks alone are NOT SaMD/SiMD

2. **Classify Risk Level:**
   - Apply IMDRF risk classification matrix
   - Consider intended use and clinical significance

3. **Identify Licensing Authority:**
   - Class A/B: State Licensing Authority
   - Class C/D: CDSCO Central Licensing Authority

---

## AI/ML-Specific Requirements

### Algorithmic Change Protocol (ACP)

The October 2025 guidance introduces mandatory ACP for AI-based medical devices:

| Requirement | Description |
|-------------|-------------|
| Risk Assessment | Document risk assessment plans for algorithm updates |
| Data Collection | Establish protocols for ongoing data collection |
| Quality Assurance | Implement QA processes for model changes |
| Dataset Justification | Document rationale for training, validation, retraining datasets |
| Safety Verification | Ensure changes don't compromise safety or intended use |

### Technical Documentation Requirements

For AI-based SaMD implementations, manufacturers must provide:

| Documentation | Content |
|---------------|---------|
| Dataset Documentation | Selection rationale, representativeness, bias assessment |
| Validation Protocols | Clinical validation methodology and results |
| Clinical Performance | Evidence of clinical efficacy and safety |
| Cybersecurity | Security architecture and vulnerability management |
| Post-Market Surveillance | Monitoring plan for real-world performance |

---

## Digital Personal Data Protection Act 2023 (DPDP)

### Data Protection Framework

| Principle | Requirement |
|-----------|-------------|
| Lawful Processing | Valid legal basis for data processing |
| Purpose Limitation | Data used only for specified purposes |
| Data Minimization | Collect only necessary data |
| Accuracy | Maintain data accuracy and currency |
| Storage Limitation | Retain data only as long as necessary |
| Security | Implement appropriate technical safeguards |
| Accountability | Demonstrate compliance with DPDP principles |

### Health Data Considerations

| Aspect | DPDP Requirement |
|--------|------------------|
| Sensitive Personal Data | Health data requires explicit consent |
| Data Principal Rights | Right to access, correction, erasure |
| Cross-Border Transfer | Permitted subject to government notification |
| Data Fiduciary Obligations | Maintain security, respond to requests |
| Breach Notification | Notify Data Protection Board of breaches |

---

## Applicable Standards

### Technical Standards for Medical Device Software

| Standard | Application |
|----------|-------------|
| IEC 62304 | Software lifecycle processes |
| IEC 60601-1 | Embedded software in hardware devices |
| IEC 82304-1 | Standalone SaMD health software |
| ISO 13485:2016 | Quality Management System (recommended) |
| ISO 14971 | Risk management for medical devices |

### Quality Management Requirements

| Requirement | Details |
|-------------|---------|
| QMS Documentation | Quality manual, procedures, records |
| Design Controls | Design input, output, verification, validation |
| Risk Management | Hazard identification, risk analysis, mitigation |
| Post-Market Surveillance | Vigilance reporting, trend analysis |

---

## Licensing Pathways

### Application Portals

| Purpose | Portal |
|---------|--------|
| Test Licenses | National Single Window System (NSWS) |
| Manufacturing/Import Licenses | CDSCO Medical Device Online Portal (cdscomdonline.gov.in) |

### Compliance Steps for User Implementations

| Step | Action |
|------|--------|
| 1 | Determine if software qualifies as SiMD or SaMD |
| 2 | Classify risk category (A, B, C, or D) |
| 3 | Prepare technical documentation including ACP (for AI) |
| 4 | Apply through appropriate portal |
| 5 | Implement Quality Management System |
| 6 | Establish post-market surveillance |

---

## Exclusions from Medical Device Regulation

The following are NOT regulated as medical devices:

- Hospital billing systems
- Appointment management software
- Administrative/non-clinical software
- General wellness applications (without medical claims)
- Research frameworks without direct clinical use (including AION-BRAIN)

---

## User Responsibilities

### Deploying AION-BRAIN in India

| Responsibility | Details |
|----------------|---------|
| Regulatory Classification | Independently assess whether implementation requires CDSCO registration |
| Clinical Validation | Conduct validation appropriate to intended use |
| Quality Management | Implement QMS if manufacturing medical device software |
| Professional Oversight | Engage licensed healthcare professionals for clinical applications |
| Data Protection | Comply with DPDP Act for personal data processing |
| Adverse Event Reporting | Report vigilance events to CDSCO |

### Insurance and Liability

| Coverage Type | Recommendation |
|---------------|----------------|
| Product Liability | Coverage for software-related claims |
| Professional Liability | Coverage for clinical advice/decisions |
| Cyber Liability | Data breach and security incident coverage |
| Regulatory Defense | Coverage for CDSCO investigations |

---

## Market Context

### India Digital Health Market

| Metric | Projection |
|--------|------------|
| Market Size (2032-2033) | USD 39.7-47.8 billion |
| CAGR | 17-29% |
| Medical Device Sector (2025) | USD 14+ billion |
| Focus Areas | AI diagnostics, telemedicine, wearables |

### Government Initiatives

- Production-Linked Incentive (PLI) schemes for medical devices
- Dedicated medical device manufacturing parks
- Make in India initiatives for healthcare technology
- National Digital Health Mission (NDHM)

---

## Resources

### Official Links

| Resource | URL |
|----------|-----|
| CDSCO Portal | https://cdsco.gov.in |
| Medical Device Online Portal | https://www.cdscomdonline.gov.in |
| NSWS (Test Licenses) | https://www.nsws.gov.in |
| DPDP Act Information | https://meity.gov.in |

---

## Document Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2025 | Initial release covering CDSCO MDR 2017, October 2025 Draft Guidance, DPDP Act 2023 |

---

*This document is part of the AION-BRAIN legal framework. All materials are provided under Apache License 2.0. See [LICENSE-EXPLANATION.md](../LICENSE-EXPLANATION.md) for licensing details. This is not legal advice; consult qualified Indian legal counsel for jurisdiction-specific guidance.*
