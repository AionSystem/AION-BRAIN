# Module 2: Applicable Law Mapping

**Engine:** Legal Engine 2 v1.5  
**Purpose:** Identify specific statutes, regulations, case law, and common law doctrines

---

## Overview

The Applicable Law Mapping module identifies the specific legal authorities that create obligations or rights in the analyzed situation. This builds on Module 1's jurisdiction identification to pinpoint exact statutes, regulations, and legal doctrines.

---

## CEREBRO Frameworks Activated

| Framework | Application |
|-----------|-------------|
| **Shannon** (Information theory) | Signal (applicable law) vs noise (irrelevant) |
| **Pearl** (Causality) | Which laws create which legal duties? |
| **Alexander** (Pattern language) | Recurring legal patterns across domains |
| **Curie** (Anomaly detection) | Unusual situations requiring special analysis |

---

## Oracle Layer Protocols

### Citation Integrity

| Protocol | Requirement |
|----------|-------------|
| Fabrication Blocking | NO invented case names or statutes |
| Citation Format | `[APPLICABLE LAW: description]` with `[VERIFICATION REQUIRED]` |
| Confidence Levels | HIGH/MODERATE/LOW for each identified law |
| Verification | Attorney must confirm applicability |

**CRITICAL:** If unsure of specific citation, state: "Consult attorney for specific statutory reference" rather than fabricating a citation.

---

## Law Categories

### Constitutional Law
- Federal: U.S. Constitution provisions
- State: State constitutional provisions
- Application: Foundational rights and government powers

### Federal Statutory Law
- Source: United States Code (U.S.C.)
- Examples: Title 29 (Labor), Title 42 (Public Health), Title 15 (Commerce)
- Authority: Congress

### State Statutory Law
- Source: State codes (e.g., California Civil Code)
- Varies significantly by state
- Must identify for each applicable state

### Federal Regulations
- Source: Code of Federal Regulations (CFR)
- Agency rules implementing statutes
- Have force of law

### State Regulations
- Source: State administrative codes
- Agency rules at state level
- Varies by state

### Case Law
- Binding precedent: Same court or higher in same jurisdiction
- Persuasive authority: Other jurisdictions, lower courts
- Must note if binding vs. persuasive

### Common Law
- Judge-made law from case decisions
- Contract, tort, property doctrines
- State-specific variations

---

## Search Methodology

### Step 1: Keyword Extraction
```
FROM USER INPUT:
├─ Identify legal domain (employment, privacy, contract, etc.)
├─ Extract key terms and concepts
├─ Note parties and relationships
└─ Identify transaction or conduct type
```

### Step 2: Domain-Specific Database Matching
```
DOMAIN MAPPING:
├─ Employment → 29 U.S.C., state labor codes
├─ Privacy → 15 U.S.C. (FTC), state privacy statutes
├─ Securities → 15 U.S.C. (Securities Acts), state blue sky
├─ Consumer → 15 U.S.C. (FTCA), state UDAP
├─ Healthcare → 42 U.S.C. (HIPAA), state health codes
├─ Environment → 42 U.S.C. (CAA, CWA), state env codes
└─ Tax → 26 U.S.C. (IRC), state tax codes
```

### Step 3: Cross-Reference with Jurisdictions
```
FOR EACH JURISDICTION FROM MODULE 1:
├─ Identify applicable federal statutes
├─ Identify state-specific statutes
├─ Identify local ordinances (if applicable)
├─ Identify international laws (if applicable)
└─ Note regulatory agency rules
```

### Step 4: Confidence Scoring
```
CONFIDENCE LEVELS:
├─ HIGH: Clear statutory text, well-established law
├─ MODERATE: Fact-specific application, interpretation needed
└─ LOW: Novel issue, conflicting authority, expert needed
```

---

## Output Format (Per Law)

```
[APPLICABLE LAW: {Full Citation}]
├─ Jurisdiction: {Geographic/Regulatory scope}
├─ Subject Matter: {What this law covers}
├─ Applicability Trigger: {When/how it applies to this situation}
├─ Key Requirements:
│   • {Requirement 1}
│   • {Requirement 2}
│   • {Requirement 3}
├─ Enforcement: {Agency + private right of action status}
├─ Penalties: {Range of potential penalties}
├─ Confidence: HIGH/MODERATE/LOW
└─ [VERIFICATION REQUIRED: {What attorney should confirm}]
```

---

## Common Statutes by Domain

### Employment

```
[APPLICABLE LAW: Fair Labor Standards Act, 29 U.S.C. § 201 et seq.]
├─ Jurisdiction: Federal (employers in interstate commerce)
├─ Subject Matter: Minimum wage, overtime, child labor
├─ Applicability Trigger: Employer engaged in interstate commerce
├─ Key Requirements:
│   • Minimum wage: $7.25/hour federal
│   • Overtime: 1.5x for hours over 40/week
│   • Exemptions: Executive, administrative, professional
├─ Enforcement: DOL Wage and Hour Division + private action
├─ Penalties: Back wages, liquidated damages, attorney fees
├─ Confidence: HIGH
└─ [VERIFICATION REQUIRED: Confirm exemption status]

[APPLICABLE LAW: Title VII, Civil Rights Act of 1964, 42 U.S.C. § 2000e]
├─ Jurisdiction: Federal (15+ employees)
├─ Subject Matter: Employment discrimination
├─ Applicability Trigger: 15+ employees in 20+ weeks
├─ Key Requirements:
│   • No discrimination: race, color, religion, sex, national origin
│   • Harassment prohibited
│   • Retaliation prohibited
├─ Enforcement: EEOC + private action (after exhaustion)
├─ Penalties: Back pay, compensatory/punitive damages (capped)
├─ Confidence: HIGH
└─ [VERIFICATION REQUIRED: Confirm employee count]

[APPLICABLE LAW: Americans with Disabilities Act, 42 U.S.C. § 12101]
├─ Jurisdiction: Federal (15+ employees)
├─ Subject Matter: Disability discrimination
├─ Applicability Trigger: 15+ employees in 20+ weeks
├─ Key Requirements:
│   • Non-discrimination against qualified individuals
│   • Reasonable accommodation (unless undue hardship)
│   • Interactive process for accommodations
├─ Enforcement: EEOC + private action
├─ Penalties: Same as Title VII
├─ Confidence: HIGH
└─ [VERIFICATION REQUIRED: Confirm employee count]
```

### Data Privacy

```
[APPLICABLE LAW: California Consumer Privacy Act, Cal. Civ. Code § 1798.100]
├─ Jurisdiction: California (businesses meeting thresholds)
├─ Subject Matter: Consumer data privacy rights
├─ Applicability Thresholds (meet ONE):
│   • Annual gross revenue >$25M
│   • Buy/sell/share data of 100,000+ consumers/households
│   • 50%+ revenue from selling personal information
├─ Key Requirements:
│   • Privacy notice at/before collection
│   • Right to know, delete, opt-out of sale
│   • Non-discrimination for exercising rights
│   • Service provider contracts
├─ Enforcement: CA AG + private right for breaches
├─ Penalties: $2,500/violation, $7,500/intentional
├─ Confidence: HIGH (if thresholds met)
└─ [VERIFICATION REQUIRED: Confirm threshold applicability]

[APPLICABLE LAW: General Data Protection Regulation (EU) 2016/679]
├─ Jurisdiction: EU (processing EU resident data)
├─ Subject Matter: Personal data protection
├─ Applicability Trigger: Offering goods/services to EU or monitoring EU behavior
├─ Key Requirements:
│   • Lawful basis for processing
│   • Data subject rights (access, erasure, portability)
│   • Privacy by design
│   • Data protection impact assessments
│   • Cross-border transfer restrictions
├─ Enforcement: EU Data Protection Authorities
├─ Penalties: Up to €20M or 4% global revenue
├─ Confidence: HIGH (if EU data subjects present)
└─ [VERIFICATION REQUIRED: Confirm EU applicability]
```

### Consumer Protection

```
[APPLICABLE LAW: FTC Act Section 5, 15 U.S.C. § 45]
├─ Jurisdiction: Federal (most US businesses)
├─ Subject Matter: Unfair or deceptive trade practices
├─ Applicability Trigger: Engaged in commerce
├─ Key Requirements:
│   • No unfair acts or practices
│   • No deceptive acts or practices
│   • Privacy commitments must be honored
├─ Enforcement: FTC (no private right of action)
├─ Penalties: Civil penalties up to $50,120/violation
├─ Confidence: HIGH
└─ [VERIFICATION REQUIRED: Specific practice analysis]
```

---

## State Law Variation Notes

### Employment
- California: Stricter wage/hour, meal/rest breaks, PAGA
- New York: NYC Human Rights Law broader protections
- Massachusetts: Independent contractor test differs

### Privacy
- California: CCPA/CPRA most comprehensive
- Virginia, Colorado, Connecticut, Utah: Own privacy laws
- Illinois: BIPA for biometrics

### Consumer Protection
- Each state has UDAP/UTPA statute
- Private rights of action vary
- Penalty structures differ

---

## Summary Table Template

```
═══════════════════════════════════════════════════════════════
APPLICABLE LAW SUMMARY
═══════════════════════════════════════════════════════════════

| Authority | Subject | Confidence | Attorney Review |
|-----------|---------|------------|-----------------|
| [Law 1]   | [Area]  | HIGH       | [Specific item] |
| [Law 2]   | [Area]  | MODERATE   | [Specific item] |
| [Law 3]   | [Area]  | LOW        | [Specific item] |

TOTAL LAWS IDENTIFIED: [Count]
HIGH CONFIDENCE: [Count]
REQUIRING ATTORNEY VERIFICATION: [Count]

═══════════════════════════════════════════════════════════════
```

---

**Module Version:** 1.0  
**Last Updated:** November 2025
