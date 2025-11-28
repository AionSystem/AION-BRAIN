# South Korea MFDS Regulatory Framework

**Document Classification:** International Regulatory Compliance  
**Version:** 1.0  
**Effective Date:** November 2025  
**Jurisdiction:** Republic of Korea  
**License:** Apache License 2.0 with NOTICE file  
**Document Governance:** Regulatory Engine v2.5 (Multi-Jurisdictional Intelligence) + Legal Engine 2 v1.5 (Systematic Compliance Analysis)

---

## Purpose

This document provides guidance on regulatory considerations for AION-BRAIN cognitive infrastructure within the South Korean regulatory framework, specifically under the Ministry of Food and Drug Safety (MFDS) Digital Medical Products Act and AI medical device guidelines.

**FUNDAMENTAL PRINCIPLE:** AION-BRAIN provides research frameworks and prompt engineering resources only. Users deploying applications in South Korea must ensure compliance with all applicable MFDS regulations and obtain appropriate approvals.

---

## Regulatory Authority

### Ministry of Food and Drug Safety (MFDS)

| Aspect | Details |
|--------|---------|
| Authority | Ministry of Food and Drug Safety (MFDS) |
| Primary Legislation | Digital Medical Products Act (DMPA) |
| Effective Date | January 24, 2025 |
| AI Guidelines | Generative AI Medical Device Guidelines (January 2025) |
| Website | https://www.mfds.go.kr/eng/ |

### Key Regulatory Authorities

| Authority | Scope |
|-----------|-------|
| MFDS | Medical device approvals, AI/ML devices, SaMD |
| Ministry of Health and Welfare (MOHW) | New health technology assessment, reimbursement |
| Ministry of Science and ICT (MSIT) | AI Basic Act implementation |
| Personal Information Protection Commission | Data privacy under PIPA |

---

## Key Regulatory Developments

### Digital Medical Products Act (DMPA)

| Feature | Details |
|---------|---------|
| Enacted | January 2024 |
| Effective | January 24, 2025 |
| Scope | Digital medical products including AI-driven devices, digital therapeutics, health software |
| Classification | Risk-based tiered system (Class 1-4) |
| Updates | Pre-approved change management plans allow algorithm updates without full re-approval |
| Evidence | Real-world evidence (RWE) accepted for device evaluation |

### Generative AI Guidelines (January 2025)

South Korea released the world's first guidelines specifically for generative AI medical devices:

| Aspect | Coverage |
|--------|----------|
| Scope | LLMs and LMMs based on foundation models |
| Application | Text outputs for diagnosis, treatment, prognosis |
| Excluded | Generalist AI, dictation tools, EHR search/summarization |
| Focus | Specialized healthcare tasks (e.g., radiology report drafting) |

### AI Basic Act (December 2024)

| Feature | Details |
|---------|---------|
| Status | Second country globally to establish basic AI law |
| Effective | 2026 |
| Coverage | High-impact AI and generative AI |
| Requirements | Transparency and safety obligations |
| Lead Authority | Ministry of Science and ICT (MSIT) |

---

## AION-BRAIN Positioning Under Korean Law

### Classification Analysis

| Classification Element | AION-BRAIN Position |
|------------------------|---------------------|
| Product Category | Not a digital medical product - Research framework only |
| Medical Device Status | Not a medical device under DMPA |
| Manufacturer Status | Not a medical device manufacturer |
| Regulatory Pathway | No MFDS approval required for framework itself |
| User Implementation | Users must independently assess their implementations |

---

## Risk Classification

### 4-Class System

| Class | Risk Level | Review Type |
|-------|------------|-------------|
| Class 1 | Lowest | Notification |
| Class 2 | Low-Moderate | Simplified review |
| Class 3 | Moderate-High | Standard review |
| Class 4 | Highest | Strict review |

### Technical Requirements

Manufacturers must submit:

| Requirement | Details |
|-------------|---------|
| Technical Specifications | Cloud server environment, cloud service type, security standards |
| Performance Metrics | Sensitivity, specificity, PPV, NPV, ROC curve, AUC |
| Operating Principles | Diagnosis algorithm description, cloud computing technology |

---

## Approval Pathway

### Registration Process

| Step | Action |
|------|--------|
| 1 | Obtain MFDS business license |
| 2 | Classify device risk level |
| 3 | Prepare technical documentation |
| 4 | Submit product-specific approval application |
| 5 | MFDS review and approval |
| 6 | New Health Technology Assessment (nHTA) |
| 7 | National health insurance reimbursement application |

### Reimbursement Pathway

| Stage | Authority | Purpose |
|-------|-----------|---------|
| 1 | MFDS | Product approval |
| 2 | MOHW | New Health Technology Assessment |
| 3 | NHIS | National health insurance reimbursement |

---

## Cybersecurity Requirements

### Digital Medical Device Cybersecurity Guidelines (January 2025)

| Requirement | Details |
|-------------|---------|
| Security Standards | Protection from cyber threats |
| Patient Safety | Safety measures for device operation |
| Data Protection | Personal information security |
| Incident Response | Breach notification and response protocols |

---

## Data Protection

### Personal Information Protection Act (PIPA)

| Principle | Requirement |
|-----------|-------------|
| Consent | Valid consent for personal data processing |
| Purpose Limitation | Data used only for specified purposes |
| Security | Technical and administrative safeguards |
| Cross-Border Transfer | Consent or adequacy requirements |
| Data Subject Rights | Access, correction, deletion rights |

---

## Market Status

| Year | Development |
|------|-------------|
| 2017 | First AI medical device software approved (ECG analysis) |
| 2018-2019 | Multiple radiology imaging AI devices approved |
| 2023 | 64 AI medical devices approved |
| 2024 | 29 innovative medical device designations |

---

## User Responsibilities

### Deploying AION-BRAIN in South Korea

| Responsibility | Details |
|----------------|---------|
| Regulatory Classification | Assess whether implementation requires MFDS approval |
| Clinical Validation | Conduct validation per MFDS requirements |
| Quality Management | Implement QMS for medical device software |
| Professional Oversight | Engage licensed healthcare professionals |
| Data Protection | Comply with PIPA for personal data |
| Adverse Event Reporting | Report vigilance events to MFDS |

---

## Resources

### Official Links

| Resource | URL |
|----------|-----|
| MFDS Portal | https://www.mfds.go.kr/eng/ |
| Generative AI Guidelines | https://www.mfds.go.kr/brd/m_1060/view.do?seq=15628 |
| KMDF | https://www.kmdf.org/ |

---

## Document Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2025 | Initial release covering DMPA, Generative AI Guidelines, AI Basic Act |

---

*This document is part of the AION-BRAIN legal framework. All materials are provided under Apache License 2.0. See [LICENSE-EXPLANATION.md](../LICENSE-EXPLANATION.md) for licensing details. This is not legal advice; consult qualified Korean legal counsel for jurisdiction-specific guidance.*
