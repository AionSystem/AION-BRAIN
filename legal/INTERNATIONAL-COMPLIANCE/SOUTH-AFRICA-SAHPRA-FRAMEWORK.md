# South Africa SAHPRA Regulatory Framework

**Document Classification:** International Regulatory Compliance  
**Version:** 1.0  
**Effective Date:** November 2025  
**Jurisdiction:** Republic of South Africa  
**License:** Apache License 2.0 with NOTICE file  
**Document Governance:** Regulatory Engine v2.5 (Multi-Jurisdictional Intelligence) + Legal Engine 2 v1.5 (Systematic Compliance Analysis)

---

## Purpose

This document provides guidance on regulatory considerations for AION-BRAIN cognitive infrastructure within the South African regulatory framework, specifically under SAHPRA (South African Health Products Regulatory Authority) AI/ML medical device guidance issued September 2025.

**FUNDAMENTAL PRINCIPLE:** AION-BRAIN provides research frameworks and prompt engineering resources only. Users deploying applications in South Africa must ensure compliance with all applicable SAHPRA regulations and obtain appropriate authorizations.

---

## Regulatory Authority

### SAHPRA (South African Health Products Regulatory Authority)

| Aspect | Details |
|--------|---------|
| Authority | South African Health Products Regulatory Authority |
| Primary Legislation | Medicines and Related Substances Act (Act 101 of 1965) |
| Device Regulations | Medical Devices Regulations 2016 |
| AI/ML Guidance | Communication MD08-2025/2026 (September 2025) |
| Website | https://www.sahpra.org.za/ |

### Key Guidelines

| Guideline | Purpose |
|-----------|---------|
| SAHPGL-MD-04 v5 | Classification of Medical Devices and IVDs |
| SAHPGL-MD-03 v4 | Adverse Event Reporting |
| MD08-2025/2026 | AI/ML Medical Device Requirements |

---

## AION-BRAIN Positioning Under South African Law

### Classification Analysis

| Classification Element | AION-BRAIN Position |
|------------------------|---------------------|
| Product Category | Not SaMD or SiMD - Research framework only |
| Medical Device Status | Not a medical device under SAHPRA regulations |
| Manufacturer Status | Not a medical device manufacturer |
| Regulatory Pathway | No SAHPRA authorization required for framework itself |
| User Implementation | Users must independently assess their implementations |

---

## AI/ML Medical Device Requirements (September 2025)

### Authorization Requirements

| Requirement | Details |
|-------------|---------|
| SAHPRA Authorization | Required before market entry for all AI/ML devices |
| Establishment Licence | Section 22C Medical Device Establishment Licence |
| Device Listing | All devices must be listed on establishment licence |

### Scope of Guidance

| Included | Description |
|----------|-------------|
| SaMD | Software as Medical Device |
| SiMD | Software in Medical Device |
| AI/ML Enabled | Devices using artificial intelligence/machine learning |
| IVDs | In vitro diagnostic devices with AI/ML |

---

## Risk Classification

### 4-Tier Classification System

| Class | Risk Level | Description |
|-------|------------|-------------|
| Class A | Lowest | Low-risk devices |
| Class B | Low/Moderate | Some clinical risk |
| Class C | Moderate/High | Significant clinical impact |
| Class D | Highest | Life-critical applications |

### AI/ML Classification Considerations

| Factor | Impact |
|--------|--------|
| Clinical Decision Influence | Direct influence typically Class C or D |
| Incorrect Output Consequences | Significant patient harm potential elevates class |
| Autonomous Operation | Higher autonomy may increase classification |
| Intended Use | Clinical significance determines risk level |

---

## Quality Management System

### ISO 13485:2016 Requirements

| Area | Requirement |
|------|-------------|
| Software Lifecycle | IEC 62304 compliance |
| Design Controls | Validation and verification |
| Risk Management | ISO 14971 |
| Data Management | Model training governance |
| Complaints | Field action handling |

### MDSAP Participation

| Status | Details |
|--------|---------|
| Affiliate Status | SAHPRA joined MDSAP in 2024 |
| Certificate Acceptance | MDSAP certificates accepted for QMS evaluation |
| Benefit | Streamlined international market access |

---

## Technical Documentation

### Technical File Requirements

| Section | Content |
|---------|---------|
| Device Description | Software documentation |
| Risk Analysis | ISO 14971 risk management |
| Validation Results | Verification and validation evidence |
| Cybersecurity | Security architecture and measures |
| Algorithm Documentation | Architecture, training data, performance metrics |

### Clinical Evidence Requirements

| Requirement | Details |
|-------------|---------|
| Validation Studies | Real-world validation |
| Subgroup Analysis | Performance across populations |
| Bias Mitigation | Strategies for algorithmic bias |
| Diverse Populations | Performance across demographics |

---

## Reference Jurisdiction Requirements

### Class C and D Devices

SAHPRA requires prior approval from at least one reference regulator:

| Authority | Country |
|-----------|---------|
| FDA | United States |
| TGA | Australia |
| Health Canada | Canada |
| EMA | European Union |
| PMDA | Japan |
| ANVISA | Brazil |
| WHO Prequalification | International |

---

## Algorithm Change Control

### Update Requirements

| Requirement | Details |
|-------------|---------|
| Change Control Plan | Documented plan required |
| SAHPRA Engagement | Before implementing significant updates |
| Safety Impact | Changes affecting safety or performance |
| Predetermined Changes | Aligned with FDA PCCP framework |

---

## Data Protection

### POPIA (Protection of Personal Information Act)

| Principle | Requirement |
|-----------|-------------|
| Processing Limitation | Lawful and minimum necessary |
| Purpose Specification | Collected for specific purposes |
| Further Processing | Compatible with original purpose |
| Information Quality | Complete, accurate, current |
| Openness | Documented processing activities |
| Security Safeguards | Technical and organizational measures |
| Data Subject Rights | Access, correction, deletion |

### Health Data Requirements

| Aspect | Requirement |
|--------|-------------|
| Special Personal Information | Health data requires explicit consent |
| Cross-Border Transfer | Adequacy or consent requirements |
| Model Training | Privacy-compliant data governance |
| Post-Market Monitoring | Anonymization where possible |

---

## Post-Market Surveillance

### Vigilance Requirements

| Requirement | Guideline |
|-------------|-----------|
| Adverse Event Reporting | SAHPGL-MD-03 v4 |
| Incident Documentation | Detailed records required |
| SAHPRA Notification | Timely reporting obligations |
| Corrective Actions | SAHPRA-directed when necessary |

---

## International Alignment

SAHPRA guidance aligns with:

| Framework | Organization |
|-----------|--------------|
| IMDRF | International Medical Device Regulators Forum |
| FDA Guidance | US AI/ML documents |
| EU MDR/IVDR | European regulations |
| UK MHRA | United Kingdom guidance |
| Singapore HSA | Health Sciences Authority |
| WHO | World Health Organization |

---

## Strategic Context

### SAHPRA 2025-2030 Strategic Plan

| Priority | Details |
|----------|---------|
| AI Guidelines | Clear guidance for AI-based health technologies |
| Legislative Updates | Updated legislation where necessary |
| Safe Integration | AI integration into South African healthcare |
| Innovation Support | Enabling local and international innovation |

---

## User Responsibilities

### Deploying AION-BRAIN in South Africa

| Responsibility | Details |
|----------------|---------|
| Regulatory Classification | Assess using SAHPGL-MD-04 v5 |
| Establishment Licence | Obtain Section 22C licence |
| QMS Implementation | ISO 13485:2016 + IEC 62304 |
| Clinical Evidence | Validation studies and bias analysis |
| Reference Approval | Obtain approval from reference regulator (Class C/D) |
| Change Control | Document algorithm update procedures |
| POPIA Compliance | Data protection measures |
| Adverse Event Reporting | Per SAHPGL-MD-03 |

---

## Resources

### Official Links

| Resource | URL |
|----------|-----|
| SAHPRA Portal | https://www.sahpra.org.za/ |
| Medical Devices | https://www.sahpra.org.za/medical-devices/ |
| AI/ML Communication | MD08-2025/2026 on SAHPRA website |
| Classification Guideline | SAHPGL-MD-04 v5 |

---

## Document Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2025 | Initial release covering SAHPRA AI/ML guidance, POPIA, reference jurisdiction requirements |

---

*This document is part of the AION-BRAIN legal framework. All materials are provided under Apache License 2.0. See [LICENSE-EXPLANATION.md](../LICENSE-EXPLANATION.md) for licensing details. This is not legal advice; consult qualified South African legal counsel for jurisdiction-specific guidance.*
