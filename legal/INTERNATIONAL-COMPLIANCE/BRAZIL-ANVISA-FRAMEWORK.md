# Brazil ANVISA Regulatory Framework

**Document Classification:** International Regulatory Compliance  
**Version:** 1.0  
**Effective Date:** November 2025  
**Jurisdiction:** Federative Republic of Brazil  
**License:** Apache License 2.0 with NOTICE file  
**Document Governance:** Regulatory Engine v2.5 (Multi-Jurisdictional Intelligence) + Legal Engine 2 v1.5 (Systematic Compliance Analysis)

---

## Purpose

This document provides guidance on regulatory considerations for AION-BRAIN cognitive infrastructure within the Brazilian regulatory framework, specifically under ANVISA (Agencia Nacional de Vigilancia Sanitaria) medical device and SaMD regulations.

**FUNDAMENTAL PRINCIPLE:** AION-BRAIN provides research frameworks and prompt engineering resources only. Users deploying applications in Brazil must ensure compliance with all applicable ANVISA regulations and obtain appropriate registrations.

---

## Regulatory Authority

### ANVISA (Agencia Nacional de Vigilancia Sanitaria)

| Aspect | Details |
|--------|---------|
| Authority | ANVISA - National Health Surveillance Agency |
| Primary Legislation | RDC 751/2022 (Medical Devices) |
| SaMD Regulation | RDC 657/2022 (Software as Medical Device) |
| IVD Regulation | RDC 830/2023 (In Vitro Diagnostics) |
| Website | https://www.gov.br/anvisa/ |

### Additional Regulatory Bodies

| Authority | Scope |
|-----------|-------|
| INMETRO | Active medical device conformity assessment |
| ANATEL | Devices with Bluetooth/wireless/mobile communication |
| CNEN | Devices using ionizing radiation |

---

## AION-BRAIN Positioning Under Brazilian Law

### Classification Analysis

| Classification Element | AION-BRAIN Position |
|------------------------|---------------------|
| Product Category | Not SaMD - Research framework only |
| Medical Device Status | Not a medical device under RDC 751/2022 |
| Manufacturer Status | Not a medical device manufacturer |
| Regulatory Pathway | No ANVISA registration required for framework itself |
| User Implementation | Users must independently assess their implementations |

---

## SaMD Definition (RDC 657/2022)

### Included in Regulation

| Category | Examples |
|----------|----------|
| Medical Software | Software meeting medical device definition |
| Standalone Software | Performs medical purposes without hardware |
| Mobile Applications | Apps with medical indications |
| SaaS Models | Cloud-based medical software |
| IVD Software | In vitro diagnostic software |

### Excluded from Regulation

| Category | Description |
|----------|-------------|
| Wellness Apps | No medical purpose |
| Administrative Software | Financial/management systems |
| Epidemiological Tools | Demographic data without clinical function |
| Embedded Software | Must register with parent device |
| Research Frameworks | Including AION-BRAIN |

---

## Risk Classification

### 4-Class IMDRF-Aligned System

| Class | Risk Level | Registration Type | Review Time | Validity |
|-------|------------|-------------------|-------------|----------|
| Class I | Low | Notification | 30 days | Indefinite |
| Class II | Medium | Notification | 30 days | Indefinite |
| Class III | High | Full Registration | 4-12 months | 10 years |
| Class IV | Maximum | Full Registration | 4-12 months | 10 years |

### Classification Rules

Rule 11 in RDC 751/2022 specifically addresses SaMD classification based on:

| Factor | Consideration |
|--------|---------------|
| Intended Purpose | Clinical significance of output |
| Clinical Risk | Potential patient harm |
| Decision Impact | Influence on clinical decisions |
| Data Sensitivity | PHI and PII handling |

---

## Registration Requirements

### All Classes Require

| Requirement | Details |
|-------------|---------|
| Brazil Registration Holder (BRH) | Local representative required |
| AFE | Autorizacao de Funcionamento de Empresa (company authorization) |
| Technical Manager | Qualified technical responsible person |
| Legal Manager | Legal representative |
| Portuguese Documentation | All labeling and IFU in Brazilian Portuguese |

### Class III and IV Additional Requirements

| Requirement | Details |
|-------------|---------|
| Full Registration | Complete dossier submission |
| B-GMP Certification | Brazilian Good Manufacturing Practices |
| Clinical Evidence | Validation and verification data |
| Post-Market Plan | Surveillance and vigilance system |

---

## Technical Documentation (RDC 657/2022)

### Required SaMD Documentation

| Section | Content |
|---------|---------|
| Cybersecurity | Security measures, protocols, data protection |
| Interoperability | Compatibility specifications, communication protocols |
| Operating Principle | Algorithm descriptions, routines, formulas |
| Software Updates | Update procedures, version management |
| Validation | Product-specific validation evidence |

### AI/ML-Specific Requirements

| Requirement | Details |
|-------------|---------|
| Algorithm Documentation | Generic algorithm descriptions |
| Clinical Processing | Routines and formulas for clinical calculations |
| Performance Validation | Sensitivity, specificity, accuracy metrics |
| Change Management | Update notification procedures |

---

## UDI System (Siud)

### Implementation Timeline

| Device Class | Deadline |
|--------------|----------|
| Class IV | July 2025 (active) |
| Class III | January 10, 2026 |
| Class II | 2027 |
| Class I | 2028 |

---

## Data Protection

### LGPD (Lei Geral de Protecao de Dados)

| Principle | Requirement |
|-----------|-------------|
| Legal Basis | Valid ground for data processing |
| Purpose Limitation | Specific, explicit purposes |
| Necessity | Minimum data necessary |
| Transparency | Clear information to data subjects |
| Security | Technical and administrative measures |
| Data Subject Rights | Access, correction, deletion, portability |

### Health Data Requirements

| Aspect | Requirement |
|--------|-------------|
| Sensitive Data | Health data requires explicit consent or legal basis |
| International Transfer | Adequacy or contractual safeguards |
| Breach Notification | Report to ANPD and data subjects |

---

## International Alignment

### MDSAP Participation

Brazil participates in the Medical Device Single Audit Program:

| Feature | Benefit |
|---------|---------|
| Single Audit | MDSAP certificate accepted |
| International Recognition | Streamlined market access |
| Quality Standards | Harmonized QMS requirements |

### Reliance Mechanism (RDC 741/2022)

ANVISA can accept assessments from trusted authorities:

| Authority | Country |
|-----------|---------|
| FDA | United States |
| EMA | European Union |
| Health Canada | Canada |
| TGA | Australia |
| PMDA | Japan |

---

## User Responsibilities

### Deploying AION-BRAIN in Brazil

| Responsibility | Details |
|----------------|---------|
| Regulatory Classification | Assess using RDC 751/2022 Rule 11 |
| Appoint BRH | Establish local registration holder |
| Obtain AFE | Company authorization |
| Technical Documentation | Prepare per RDC 657/2022 |
| Portuguese Translation | All documentation |
| UDI Compliance | Per implementation timeline |

---

## Resources

### Official Links

| Resource | URL |
|----------|-----|
| ANVISA Portal | https://www.gov.br/anvisa/ |
| SaMD Q&A | https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2022/software-como-dispositivo-medico-perguntas-e-respostas/ |
| RDC 657/2022 | Available on ANVISA portal |

---

## Document Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2025 | Initial release covering RDC 751/2022, RDC 657/2022, LGPD, UDI system |

---

*This document is part of the AION-BRAIN legal framework. All materials are provided under Apache License 2.0. See [LICENSE-EXPLANATION.md](../LICENSE-EXPLANATION.md) for licensing details. This is not legal advice; consult qualified Brazilian legal counsel for jurisdiction-specific guidance.*
