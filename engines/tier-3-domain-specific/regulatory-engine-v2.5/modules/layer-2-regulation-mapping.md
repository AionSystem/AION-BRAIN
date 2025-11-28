# Layer 2: Regulation Mapping Module

**Classification:** Regulatory Engine v2.5 Core Layer
**Priority:** Critical
**Function:** Map specific regulations to business activities and requirements

---

## 1. Module Overview

The Regulation Mapping Layer takes jurisdiction detection output and maps specific statutes, regulations, rules, and guidance documents to the entity's business activities. This creates a comprehensive regulatory inventory.

### Core Functions

| Function | Description |
|----------|-------------|
| Statute Identification | Identify applicable statutes (USC, state codes) |
| Regulation Mapping | Map CFR, state regulations to activities |
| Guidance Integration | Include agency guidance, interpretations |
| Rule Inventory | Create complete regulatory requirement list |
| Obligation Extraction | Extract specific compliance obligations |

---

## 2. Regulatory Hierarchy

### 2.1 Federal Regulatory Stack

```
FEDERAL REGULATORY HIERARCHY
============================

LEVEL 1: CONSTITUTION
├─ Commerce Clause authority
├─ Supremacy Clause (preemption analysis)
└─ Due Process requirements

LEVEL 2: STATUTES (U.S. Code)
├─ Enabling legislation (agency authority)
├─ Substantive requirements
├─ Penalty provisions
└─ Private right of action

LEVEL 3: REGULATIONS (C.F.R.)
├─ Notice-and-comment rules (binding)
├─ Interim final rules
├─ Direct final rules
└─ Regulatory text interpretation

LEVEL 4: AGENCY GUIDANCE
├─ Policy statements
├─ Interpretive rules
├─ Staff guidance letters
├─ FAQ documents
├─ No-action letters
└─ Enforcement priorities

LEVEL 5: CASE LAW
├─ Supreme Court precedent
├─ Circuit court interpretations
├─ District court decisions
├─ Agency adjudications
└─ Administrative law judge decisions

AUTHORITY WEIGHT:
Constitution > Statute > Regulation > Binding Guidance > Non-binding Guidance
```

---

## 3. Regulation Mapping Protocol

### 3.1 Activity-to-Regulation Mapping

```
REGULATION MAPPING FRAMEWORK
============================
<SELF_CORRECTION_PROTOCOL active>

FOR EACH BUSINESS ACTIVITY:

STEP 1: IDENTIFY GOVERNING STATUTES
├─ Search U.S. Code sections
├─ Identify state statutory equivalents
├─ Note enabling vs. substantive provisions
└─ Document penalty provisions

STEP 2: MAP TO REGULATIONS
├─ Identify C.F.R. title and parts
├─ Map state administrative code sections
├─ Note effective dates
└─ Check for amendments/revisions

STEP 3: INCORPORATE GUIDANCE
├─ Agency guidance documents
├─ Enforcement policy statements
├─ Industry-specific interpretations
└─ Recent enforcement actions (precedent)

STEP 4: EXTRACT OBLIGATIONS
├─ Registration/licensing requirements
├─ Disclosure obligations
├─ Recordkeeping requirements
├─ Reporting obligations
├─ Prohibited conduct
├─ Affirmative requirements
└─ Timing/deadline requirements

CHECKPOINT: Have I mapped ALL applicable regulations?
If regulation is unclear → [VERIFY_REQUIRED:regulatory_counsel]
If regulation is recent → [CURRENCY_CHECK:effective_date]
```

### 3.2 Obligation Extraction Template

```
REGULATORY OBLIGATION EXTRACTION
================================

OBLIGATION ID: [REG-YYYY-XXXX]
Source: [Statute/Regulation citation]
Agency: [Regulatory body]
Effective Date: [Date]

OBLIGATION TYPE:
□ Registration/Licensing
□ Disclosure/Reporting
□ Recordkeeping
□ Prohibited Conduct
□ Affirmative Requirement
□ Procedural Requirement

OBLIGATION TEXT:
[Exact regulatory language or accurate paraphrase]

APPLICABILITY:
├─ Entity types: [Which entities must comply]
├─ Thresholds: [Size, revenue, activity thresholds]
├─ Exceptions: [Exemptions or safe harbors]
└─ Effective date: [When obligation begins]

COMPLIANCE REQUIREMENTS:
├─ What must be done: [Specific actions required]
├─ When: [Timing, frequency, deadlines]
├─ How: [Format, method, documentation]
├─ To whom: [Filing location, reporting party]
└─ Evidence: [How to demonstrate compliance]

PENALTIES FOR NON-COMPLIANCE:
├─ Civil penalties: [$ amounts, per violation]
├─ Criminal penalties: [If applicable]
├─ Administrative sanctions: [License revocation, etc.]
├─ Private litigation: [If private right of action]
└─ Reputational: [Public disclosure of violations]

RELATED OBLIGATIONS:
[Cross-reference to related regulatory requirements]
```

---

## 4. Major Regulatory Frameworks

### 4.1 Financial Services

| Framework | Statute | Regulations | Agency |
|-----------|---------|-------------|--------|
| Securities | Securities Act, Exchange Act | 17 CFR 200-299 | SEC |
| Banking | National Bank Act, FDI Act | 12 CFR | OCC, FDIC, Fed |
| Consumer Finance | TILA, FCRA, ECOA | 12 CFR 1000s | CFPB |
| Anti-Money Laundering | BSA | 31 CFR 1000s | FinCEN |
| Broker-Dealer | Exchange Act | 17 CFR, FINRA Rules | SEC, FINRA |

### 4.2 Healthcare

| Framework | Statute | Regulations | Agency |
|-----------|---------|-------------|--------|
| Medical Devices | FD&C Act | 21 CFR 800-898 | FDA |
| Pharmaceuticals | FD&C Act | 21 CFR 200-499 | FDA |
| Privacy | HIPAA | 45 CFR 160, 164 | HHS OCR |
| Medicare/Medicaid | SSA | 42 CFR | CMS |
| Clinical Labs | CLIA | 42 CFR 493 | CMS |

### 4.3 Employment

| Framework | Statute | Regulations | Agency |
|-----------|---------|-------------|--------|
| Discrimination | Title VII, ADA, ADEA | 29 CFR 1600s | EEOC |
| Wages/Hours | FLSA | 29 CFR 500s, 700s | DOL WHD |
| Safety | OSH Act | 29 CFR 1900s | OSHA |
| Benefits | ERISA | 29 CFR 2500s | DOL EBSA |
| Immigration | INA | 8 CFR | USCIS, DOL |

### 4.4 Environmental

| Framework | Statute | Regulations | Agency |
|-----------|---------|-------------|--------|
| Air | Clean Air Act | 40 CFR 50-99 | EPA |
| Water | Clean Water Act | 40 CFR 100-149 | EPA |
| Waste | RCRA | 40 CFR 239-282 | EPA |
| Chemicals | TSCA | 40 CFR 700-799 | EPA |
| Cleanup | CERCLA | 40 CFR 300s | EPA |

---

## 5. Cross-Regulation Analysis

### 5.1 Overlap Detection

```
REGULATORY OVERLAP ANALYSIS
===========================

SCENARIO: Activity triggers multiple regulations

OVERLAP TYPE 1: COMPLEMENTARY
├─ Different aspects of same activity
├─ Compliance with one doesn't satisfy other
├─ Must comply with ALL applicable requirements
└─ Example: HIPAA + state health privacy

OVERLAP TYPE 2: HARMONIZED
├─ Federal and state with safe harbor
├─ Federal compliance satisfies state
├─ Check for state-specific additions
└─ Example: Federal OSHA + state OSHA plan

OVERLAP TYPE 3: CONFLICTING
├─ Requirements cannot both be satisfied
├─ Preemption analysis required
├─ May need agency guidance
└─ Example: State law vs. federal preemption

RESOLUTION HIERARCHY:
1. Constitutional supremacy
2. Express statutory preemption
3. Implied preemption (field/conflict)
4. Most stringent requirement (absent preemption)
5. Agency coordination (if available)
```

---

## 6. Output Format

```
REGULATION MAPPING REPORT
=========================
Entity: [Name]
Activity: [Description]
Analysis Date: [Date]

APPLICABLE REGULATIONS INVENTORY:

FEDERAL STATUTES:
| Citation | Title | Relevance |
|----------|-------|-----------|
| [USC cite] | [Title] | [How applies] |

FEDERAL REGULATIONS:
| Citation | Title | Key Requirements |
|----------|-------|------------------|
| [CFR cite] | [Title] | [Summary] |

AGENCY GUIDANCE:
| Document | Date | Relevance |
|----------|------|-----------|
| [Title] | [Date] | [How applies] |

STATE REQUIREMENTS:
| State | Statute/Reg | Key Requirements |
|-------|-------------|------------------|
| [State] | [Citation] | [Summary] |

OBLIGATION SUMMARY:
Total obligations identified: [Count]
├─ Registration/Licensing: [Count]
├─ Disclosure/Reporting: [Count]
├─ Recordkeeping: [Count]
├─ Prohibited Conduct: [Count]
└─ Affirmative Requirements: [Count]

OVERLAPS/CONFLICTS:
[Identified regulatory overlaps with resolution]

GAPS/UNCERTAINTIES:
[VERIFY_REQUIRED items for counsel review]
```

---

## 7. Integration Requirements

| Engine/Module | Purpose |
|---------------|---------|
| Jurisdiction Detection (Layer 1) | Scope of regulation search |
| Citation Integrity (Layer 3) | Verify regulatory citations |
| Currency Validation (Layer 4) | Check regulation effective dates |
| Legal Engine v2.1 | Legal interpretation support |

---

## 8. Activation

```
<MODULE: REGULATION_MAPPING>
Jurisdictions: [From Layer 1 output]
Activities: [Business activities list]
Depth: [Overview/Standard/Comprehensive]
Include Guidance: [Yes/No]
</MODULE>
```

---

## 9. Limitations

This module:
- Cannot guarantee complete regulatory identification
- Regulations change frequently (check effective dates)
- Guidance documents may not be comprehensive
- State/local regulations may be incomplete
- Industry-specific requirements may be specialized
- Legal interpretation required for complex analysis

---

**Module Version:** 2.0
**Last Updated:** November 2025
**AI Platform Tested:** All 8 primary platforms
