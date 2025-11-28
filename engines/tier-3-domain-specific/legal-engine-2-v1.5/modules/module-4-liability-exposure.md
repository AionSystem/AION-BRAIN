# Module 4: Liability Exposure Assessment

**Engine:** Legal Engine 2 v1.5  
**Purpose:** Quantify financial, reputational, and criminal liability exposure

---

## Overview

The Liability Exposure Assessment module translates identified compliance gaps into concrete risk metrics, enabling prioritization based on potential impact rather than just legal technicality.

---

## CEREBRO Frameworks Activated

| Framework | Application |
|-----------|-------------|
| **Taleb** (Anti-fragility) | Black swan liability events |
| **Pearl** (Causality) | Exposure → Harm pathways |
| **Kahneman** (Decision theory) | Expected value calculations |
| **Rawls/Singer** (Ethics) | Stakeholder harm analysis |

---

## Exposure Categories

### Financial Exposure

| Component | Description | Quantification |
|-----------|-------------|----------------|
| Statutory Penalties | Per-violation fines set by law | Range from statute |
| Private Damages | Compensation to harmed parties | Historical data, case analysis |
| Treble/Punitive | Multiplied or punitive damages | If statute/conduct allows |
| Legal Fees | Defense costs | Complexity-based estimate |
| Remediation Costs | Cost to fix the problem | Scope-based estimate |
| Settlement Value | Likely settlement range | Discount from max exposure |

### Reputational Exposure

| Factor | Assessment Method |
|--------|-------------------|
| Public Disclosure Risk | Regulatory action = public record |
| Media Interest | Industry, company size, novelty |
| Customer Impact | Loyalty, alternatives, B2B vs B2C |
| Investor Impact | Materiality, disclosure requirements |
| Talent Impact | Recruitment, retention effects |

### Criminal Exposure

| Factor | Assessment |
|--------|------------|
| Personal Liability | Which individuals at risk |
| Potential Charges | Specific criminal provisions |
| Likelihood | Prosecutorial priorities, evidence |
| Severity | Sentencing ranges if convicted |

### Operational Exposure

| Factor | Assessment |
|--------|------------|
| Business Interruption | Duration, scope of disruption |
| License/Permit Risk | Professional, regulatory licenses |
| Market Access | Ability to operate in markets |
| Contractual Triggers | Defaults, termination rights |

---

## Financial Exposure Calculation

### Penalty Research Framework

```
FOR EACH APPLICABLE LAW:

STEP 1: Identify Statutory Penalty Structure
├─ Per-violation penalty: $[amount]
├─ Per-day penalty: $[amount]
├─ Percentage penalty: [%] of [base]
├─ Caps: Maximum penalty amount
└─ Minimums: If mandatory minimums exist

STEP 2: Estimate Violation Count
├─ Time period of non-compliance
├─ Number of affected individuals
├─ Number of transactions/incidents
└─ Calculation: [violations] × [penalty]

STEP 3: Assess Aggravating/Mitigating Factors
├─ Willful vs. negligent conduct
├─ Prior violations
├─ Cooperation with regulators
├─ Remediation efforts
└─ Adjust penalty range accordingly

STEP 4: Calculate Range
├─ LOW: Best case (mitigation applied)
├─ MID: Most likely scenario
└─ HIGH: Worst case (aggravation applied)
```

### Common Penalty Ranges

| Law | Penalty Per Violation | Notes |
|-----|----------------------|-------|
| CCPA | $2,500 - $7,500 | Per consumer, per violation |
| GDPR | Up to €20M or 4% revenue | Whichever is greater |
| HIPAA | $100 - $50,000 | Up to $1.5M per category/year |
| FLSA | Back wages + liquidated (2x) | 2-3 year lookback |
| Title VII | $50K - $300K caps | Based on employer size |
| FTC | Up to $50,120 | Per violation, per day |
| ADA | $75K - $150K | First vs. subsequent violation |

### Private Litigation Exposure

```
PRIVATE DAMAGES ESTIMATION:

INDIVIDUAL CLAIMS:
├─ Compensatory: Actual damages suffered
├─ Statutory: If statute provides minimum
├─ Punitive: If willful/egregious (multiplier)
├─ Attorney Fees: If fee-shifting statute
└─ Per-Claimant Range: $[low] - $[high]

CLASS ACTION POTENTIAL:
├─ Class Size: [Estimated affected individuals]
├─ Per-Person Damages: $[amount]
├─ Aggregate: $[total]
├─ Settlement Discount: 10-40% of max
└─ Class Exposure: $[range]

MULTIPLIERS:
├─ Treble damages (antitrust, some consumer)
├─ PAGA penalties (California labor)
├─ Liquidated damages (FLSA, FMLA)
└─ Apply where applicable
```

---

## Exposure Assessment Template

```
═══════════════════════════════════════════════════════════════
LIABILITY EXPOSURE ASSESSMENT
═══════════════════════════════════════════════════════════════

GAP REFERENCE: [Gap ID from Module 3]
LEGAL AUTHORITY: [Applicable law]

───────────────────────────────────────────────────────────────
FINANCIAL EXPOSURE
───────────────────────────────────────────────────────────────

REGULATORY PENALTIES:
├─ Statutory Range: $[min] - $[max] per violation
├─ Estimated Violations: [count]
├─ Aggravating Factors: [list if any]
├─ Mitigating Factors: [list if any]
├─ LOW Estimate: $[amount]
├─ MID Estimate: $[amount]
└─ HIGH Estimate: $[amount]

PRIVATE DAMAGES:
├─ Affected Individuals: [count]
├─ Per-Person Range: $[min] - $[max]
├─ Class Action Risk: LOW / MODERATE / HIGH
├─ LOW Estimate: $[amount]
├─ MID Estimate: $[amount]
└─ HIGH Estimate: $[amount]

LEGAL FEES (Defense):
├─ Complexity: LOW / MODERATE / HIGH
├─ Duration: [months]
├─ Estimate: $[amount]

REMEDIATION COSTS:
├─ Internal Resources: $[amount]
├─ External Consultants: $[amount]
├─ Technology/Systems: $[amount]
└─ Total Remediation: $[amount]

TOTAL FINANCIAL EXPOSURE:
├─ LOW: $[total low]
├─ MID: $[total mid]
└─ HIGH: $[total high]

───────────────────────────────────────────────────────────────
REPUTATIONAL EXPOSURE
───────────────────────────────────────────────────────────────

PUBLIC DISCLOSURE RISK: LOW / MODERATE / HIGH
├─ Regulatory actions become public record
├─ Media coverage likelihood: [assessment]
└─ Social media amplification risk: [assessment]

CUSTOMER IMPACT:
├─ Customer notification required: YES / NO
├─ Estimated customer attrition: [%]
├─ Revenue at risk: $[amount]
└─ Customer recovery cost: $[amount]

INVESTOR/STAKEHOLDER IMPACT:
├─ Material disclosure required: YES / NO
├─ Valuation impact: [assessment]
└─ Financing implications: [assessment]

TALENT IMPACT:
├─ Recruitment difficulty increase: [assessment]
├─ Retention risk: [assessment]
└─ Morale impact: [assessment]

OVERALL REPUTATIONAL RISK: LOW / MODERATE / HIGH / CRITICAL

───────────────────────────────────────────────────────────────
CRIMINAL EXPOSURE
───────────────────────────────────────────────────────────────

PERSONAL LIABILITY:
├─ Individuals at Risk: [roles]
├─ Basis: [why personal liability possible]
└─ Likelihood: LOW / MODERATE / HIGH

POTENTIAL CHARGES:
├─ Federal: [if applicable]
├─ State: [if applicable]
└─ Penalties if Convicted: [fines, incarceration]

CRIMINAL EXPOSURE LEVEL: NONE / LOW / MODERATE / HIGH

───────────────────────────────────────────────────────────────
OPERATIONAL EXPOSURE
───────────────────────────────────────────────────────────────

BUSINESS INTERRUPTION:
├─ Potential Disruption: [description]
├─ Duration: [estimate]
├─ Revenue Impact: $[amount]
└─ Recovery Time: [estimate]

LICENSE/PERMIT RISK:
├─ Licenses at Risk: [list]
├─ Suspension/Revocation Likelihood: [assessment]
└─ Impact if Lost: [description]

MARKET ACCESS:
├─ Markets at Risk: [list]
├─ Regulatory Bars Possible: YES / NO
└─ Contract Termination Rights Triggered: YES / NO

═══════════════════════════════════════════════════════════════
EXPOSURE SUMMARY
═══════════════════════════════════════════════════════════════

CATEGORY          | LOW        | MID        | HIGH
───────────────────────────────────────────────────────────────
Financial         | $[amount]  | $[amount]  | $[amount]
Reputational      | [level]    | [level]    | [level]
Criminal          | [level]    | [level]    | [level]
Operational       | [level]    | [level]    | [level]
───────────────────────────────────────────────────────────────
OVERALL EXPOSURE  | [level]    | [level]    | [level]

ATTORNEY ESCALATION: REQUIRED / RECOMMENDED / OPTIONAL
REASON: [explanation]

═══════════════════════════════════════════════════════════════
```

---

## Risk Matrix Visualization

```
                    LIKELIHOOD
                    Low    Med    High
           High   │  M   │  H   │  C   │
SEVERITY   Med    │  L   │  M   │  H   │
           Low    │  L   │  L   │  M   │

L = Low Priority
M = Moderate Priority
H = High Priority
C = Critical Priority
```

---

## Aggregated Exposure Summary

```
═══════════════════════════════════════════════════════════════
TOTAL LIABILITY EXPOSURE SUMMARY
═══════════════════════════════════════════════════════════════

ALL GAPS COMBINED:

TOTAL FINANCIAL EXPOSURE:
├─ LOW Scenario: $[sum of all lows]
├─ MID Scenario: $[sum of all mids]
└─ HIGH Scenario: $[sum of all highs]

HIGHEST RISK GAPS:
1. [Gap with highest exposure]
2. [Second highest]
3. [Third highest]

CRIMINAL EXPOSURE PRESENT: YES / NO
├─ If YES: [specific gaps with criminal risk]

REPUTATIONAL TIPPING POINTS:
├─ [Gaps that could cause significant reputational harm]

OPERATIONAL CONTINUITY RISKS:
├─ [Gaps that could disrupt operations]

═══════════════════════════════════════════════════════════════
```

---

**Module Version:** 1.0  
**Last Updated:** November 2025
