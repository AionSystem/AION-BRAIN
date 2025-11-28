# Layer 1: Jurisdiction Detection Module

**Classification:** Regulatory Engine v2.5 Core Layer
**Priority:** Critical
**Function:** Identify all applicable regulatory jurisdictions and bodies

---

## 1. Module Overview

The Jurisdiction Detection Layer automatically identifies which regulatory bodies, agencies, and jurisdictions apply to a given business activity, entity, or transaction. This is the foundational layer that determines the entire regulatory analysis scope.

### Core Functions

| Function | Description |
|----------|-------------|
| Entity Analysis | Determine entity type, structure, location |
| Activity Classification | Categorize business activities by regulatory domain |
| Geographic Mapping | Identify federal, state, local, international jurisdictions |
| Agency Identification | Map specific regulatory agencies with authority |
| Authority Hierarchy | Establish primary vs. secondary regulatory bodies |

---

## 2. Jurisdiction Detection Protocol

### 2.1 Entity Analysis Framework

```
ENTITY JURISDICTION ANALYSIS
============================
<SELF_CORRECTION_PROTOCOL active>

ENTITY CHARACTERISTICS:
□ Legal structure: [Corporation/LLC/Partnership/Sole Prop/Non-profit]
□ Formation jurisdiction: [State/Country]
□ Principal place of business: [Location]
□ Operating locations: [List all]
□ Number of employees: [Count by location]
□ Annual revenue: [Amount and source breakdown]
□ Public/Private status: [SEC registrant status]

AUTOMATIC JURISDICTION FLAGS:
├─ Multi-state operations → State-by-state regulatory review
├─ International presence → Cross-border compliance analysis
├─ Public company → SEC/SOX/exchange rules
├─ Government contracts → FAR/DFAR/agency-specific
├─ Consumer-facing → FTC/CFPB/state consumer protection
└─ Employee count thresholds → FMLA/ACA/EEO triggers

CHECKPOINT: Have I identified ALL operating jurisdictions?
If uncertain → [VERIFY_REQUIRED:corporate_counsel]
</ENTITY_JURISDICTION_ANALYSIS>
```

### 2.2 Activity Classification Matrix

```
REGULATORY ACTIVITY CLASSIFICATION
==================================

FINANCIAL ACTIVITIES:
├─ Banking services → OCC, FDIC, Federal Reserve, state banking
├─ Securities dealing → SEC, FINRA, state securities
├─ Investment advisory → SEC, state RIA registration
├─ Insurance → State insurance commissioners
├─ Consumer lending → CFPB, state lending laws
├─ Money transmission → FinCEN, state MTL requirements
└─ Cryptocurrency → SEC, CFTC, state-by-state

HEALTHCARE ACTIVITIES:
├─ Medical devices → FDA (510(k), PMA, De Novo)
├─ Pharmaceuticals → FDA (NDA, ANDA, BLA)
├─ Healthcare providers → CMS, state licensing boards
├─ Health insurance → HHS, state insurance
├─ Clinical research → FDA IRB, OHRP
├─ Telehealth → State medical boards, interstate compacts
└─ Health data → HHS OCR (HIPAA), state health privacy

EMPLOYMENT ACTIVITIES:
├─ Hiring/Termination → EEOC, DOL, state employment
├─ Wages/Hours → DOL WHD, state wage laws
├─ Safety → OSHA, state OSHA plans
├─ Benefits → DOL EBSA, IRS, state
├─ Union relations → NLRB
└─ Immigration → USCIS, DOL, ICE

ENVIRONMENTAL ACTIVITIES:
├─ Air emissions → EPA, state environmental
├─ Water discharge → EPA, Army Corps, state
├─ Hazardous waste → EPA RCRA, state
├─ Chemical handling → EPA TSCA, OSHA
└─ Site contamination → EPA CERCLA, state

DATA/TECHNOLOGY ACTIVITIES:
├─ Consumer data → FTC, state privacy (CCPA, etc.)
├─ Children's data → FTC (COPPA)
├─ Health data → HHS (HIPAA)
├─ Financial data → GLBA, state
├─ EU data → GDPR (if EU persons)
├─ AI/Algorithms → FTC, EEOC, state AI laws
└─ Cybersecurity → SEC, state breach notification
```

---

## 3. Multi-Jurisdiction Conflict Detection

### 3.1 Jurisdiction Hierarchy

```
JURISDICTION HIERARCHY ANALYSIS
===============================

LEVEL 1: FEDERAL PREEMPTION CHECK
├─ Does federal law expressly preempt state law?
├─ Does federal law occupy the field (implied preemption)?
├─ Does state law conflict with federal requirements?
└─ Does federal agency have exclusive jurisdiction?

LEVEL 2: STATE-FEDERAL CONCURRENT
├─ Which is more stringent (usually controls)?
├─ Can entity comply with both simultaneously?
├─ Are there safe harbors for federal compliance?
└─ State-specific carve-outs or exceptions?

LEVEL 3: MULTI-STATE ANALYSIS
├─ Which state law applies to multi-state activity?
├─ Choice of law provisions in contracts?
├─ Physical presence vs. economic nexus?
└─ Conflict resolution principles?

LEVEL 4: INTERNATIONAL OVERLAY
├─ Extraterritorial application of US law?
├─ Foreign regulatory requirements?
├─ Treaty obligations?
└─ Cross-border enforcement cooperation?

OUTPUT FORMAT:
[JURISDICTION_MAP]
├─ Primary: [Agency with primary authority]
├─ Secondary: [Additional applicable agencies]
├─ Concurrent: [Overlapping jurisdictions]
├─ Conflicts: [Identified jurisdictional conflicts]
└─ Hierarchy: [Resolution order if conflicts exist]
```

---

## 4. Common Jurisdiction Triggers

### 4.1 Automatic Trigger Matrix

| Trigger | Jurisdictions Activated |
|---------|------------------------|
| >$10M assets (bank) | Federal Reserve, OCC/FDIC |
| >50 employees | FMLA, ACA employer mandate |
| >100 employees | EEO-1 reporting, WARN Act |
| Public company | SEC, SOX, exchange rules |
| Government contractor | FAR, agency-specific |
| Healthcare provider | CMS, state licensing, HIPAA |
| Consumer products | CPSC, FTC |
| Food/Drugs | FDA |
| Interstate commerce | FTC, DOT, FCC (as applicable) |
| International operations | FCPA, export controls, OFAC |

### 4.2 Revenue-Based Triggers

| Revenue Threshold | Regulatory Implications |
|-------------------|------------------------|
| >$25M (CCPA) | California Consumer Privacy Act |
| >$100M (Hart-Scott-Rodino) | Merger notification |
| >$750M (Pillar Two) | Global minimum tax |
| Industry-specific | Varies by sector |

---

## 5. Output Format

```
JURISDICTION DETECTION REPORT
=============================
Entity: [Name]
Analysis Date: [Date]

APPLICABLE JURISDICTIONS:

FEDERAL:
| Agency | Authority Basis | Priority |
|--------|-----------------|----------|
| [Agency] | [Statutory basis] | [Primary/Secondary] |

STATE:
| State | Agencies | Authority Basis |
|-------|----------|-----------------|
| [State] | [Agency list] | [Basis] |

LOCAL:
| Jurisdiction | Agencies | Authority Basis |
|--------------|----------|-----------------|
| [City/County] | [Agency] | [Basis] |

INTERNATIONAL (if applicable):
| Jurisdiction | Regulatory Body | Nexus |
|--------------|-----------------|-------|
| [Country] | [Agency] | [Basis] |

CONFLICTS IDENTIFIED:
[List any jurisdictional conflicts with resolution hierarchy]

GAPS/UNCERTAINTIES:
[VERIFY_REQUIRED] items for legal counsel review

REASONING TRACE:
[Show jurisdiction determination logic per Oracle Layer]
```

---

## 6. Self-Correction Checkpoints

```
<SELF_CORRECTION_PROTOCOL>

CHECKPOINT 1: Entity Completeness
├─ Have I captured all entity locations?
├─ Have I identified all business activities?
├─ Have I checked for subsidiary/affiliate scope?
└─ IF UNCERTAIN → Mark [VERIFY_REQUIRED:corporate_structure]

CHECKPOINT 2: Jurisdiction Completeness  
├─ Have I checked federal, state, AND local?
├─ Have I considered international reach?
├─ Have I identified industry-specific regulators?
└─ IF UNCERTAIN → Mark [VERIFY_REQUIRED:regulatory_counsel]

CHECKPOINT 3: Currency Check
├─ Are thresholds based on current law?
├─ Have there been recent regulatory changes?
├─ Am I aware of pending legislation?
└─ IF DATA STALE → Flag [CURRENCY_CHECK:as_of_date]

</SELF_CORRECTION_PROTOCOL>
```

---

## 7. Integration Requirements

| Engine/Module | Purpose |
|---------------|---------|
| Legal Engine v2.1 | Legal interpretation of authority |
| Financial Engine v1.0 | Financial threshold calculations |
| Oracle Layer v2.1 | Self-correction and reasoning traces |
| Word Engine v2.2 | Terminology precision |

---

## 8. Activation

```
<MODULE: JURISDICTION_DETECTION>
Entity Type: [Corporation/LLC/etc.]
Operating Locations: [List]
Primary Activities: [List]
Analysis Depth: [Screening/Standard/Comprehensive]
</MODULE>
```

---

## 9. Limitations

This module:
- Cannot guarantee identification of all applicable jurisdictions
- Regulatory landscape changes frequently
- May not capture recent legislative changes
- Local requirements may be incomplete
- International coverage is limited
- Professional legal counsel required for binding determinations

---

**Module Version:** 2.0
**Last Updated:** November 2025
**AI Platform Tested:** All 8 primary platforms
