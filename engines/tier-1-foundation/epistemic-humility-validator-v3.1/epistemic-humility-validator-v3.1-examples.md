# Epistemic Humility Validator v3.1 — Practical Examples

## Overview

This document demonstrates Epistemic Humility Validator v3.1 applied across diverse claims, showing how the 14 mathematical checks enforce intellectual honesty and prevent catastrophic overconfidence.

---

## Example 1: Medical AI Overclaim

### Scenario

A health-tech startup claims their AI diagnostic tool has "95% accuracy" and will "transform healthcare."

### Input

```
EPISTEMIC HUMILITY VALIDATE:
Claim: "Our AI diagnostic tool has 95% accuracy and will revolutionize 
       healthcare diagnosis by 2030"
Domain: Medical/AI
Stakes: HIGH
```

### Engine Output

```
═══════════════════════════════════════════════════════════════════════════
                EPISTEMIC HUMILITY VALIDATOR v3.1 — FULL AUDIT
═══════════════════════════════════════════════════════════════════════════

[CHECK 1: COMPLETENESS CLAIM DETECTOR] ⚠️ VIOLATION
├─ Detected: "revolutionize healthcare" implies comprehensive change
├─ Gödel constraint: No system can demonstrate complete transformation
└─ Status: FLAGGED

[CHECK 2: SELF-VERIFICATION LOOP] ✓ PASS
├─ Claim does not justify itself
└─ Status: No circular reasoning detected

[CHECK 3: PREDICTION HORIZON] ⚠️ VIOLATION
├─ Claim horizon: 2030 (5+ years)
├─ Domain: Healthcare AI — Complex adaptive system
├─ Maximum reliable horizon: 2-3 years
├─ Confidence decay:
│  ├─ Year 1-2: 70%
│  ├─ Year 3-5: 35%
│  └─ Year 5+: <20%
└─ Status: FLAGGED — 2030 prediction unreliable

[CHECK 4: BAYESIAN UNCERTAINTY QUANTIFIER] ⚠️ VIOLATION
├─ Stated: "95% accuracy"
├─ Missing: Confidence interval, sample size, population
├─ Required: "X-Y% accuracy (95% CI) on [population]"
└─ Status: FLAGGED — Vague confidence

[CHECK 5: CAUSAL INFERENCE VALIDATOR] ⚠️ VIOLATION
├─ Implicit claim: AI accuracy → healthcare transformation
├─ Confounders ignored: Adoption barriers, regulatory approval,
│  physician trust, integration costs, liability
├─ Causal chain: AI accuracy is NECESSARY but not SUFFICIENT
└─ Status: FLAGGED — Correlation treated as causation

[CHECK 6: EVIDENCE QUALITY GRADER]
├─ Evidence type: Internal validation data (assumed)
├─ Grade: D (case-series without external validation)
├─ Required for FDA: Multi-site RCT or prospective cohort
└─ Status: FLAGGED — Evidence insufficient for claim strength

[CHECK 7: PREDICTIVE CALIBRATION TESTER] ⚠️ VIOLATION
├─ "95% accuracy" — on what test set?
├─ Backtesting: Not mentioned
├─ Calibration: Unknown
└─ Status: FLAGGED — Unvalidated prediction

[CHECK 8: UNCERTAINTY PROPAGATION MAPPER]
├─ p(AI works) × p(FDA approval) × p(physician adoption) × 
│  p(patient trust) × p(integration success) → p(revolution)
├─ Estimated: 0.95 × 0.40 × 0.50 × 0.60 × 0.70 = 8%
└─ Status: "Revolutionize" claim has ~8% joint probability

[CHECK 9: REGULATORY COMPLIANCE AUDITOR] ⚠️ VIOLATION
├─ FDA medical device requirements not addressed
├─ 510(k) or PMA pathway not specified
├─ Clinical trial data requirements not met
└─ Status: FLAGGED — Regulatory non-compliance

[CHECK 10: ETHICAL RISK QUANTIFIER]
├─ False negatives: Patient harm from missed diagnosis
├─ False positives: Unnecessary treatment, anxiety
├─ Physician deskilling: Long-term competence erosion
└─ Status: Ethical risks present but not quantified in claim

[CHECK 11: EPISTEMIC EXPIRATION] ✓ PASS
├─ Claim is forward-looking, not based on expired data
└─ Status: N/A for this claim type

[CHECK 12: SAMPLE SIZE VALIDATOR]
├─ Sample size for 95% accuracy claim: Unknown
├─ Minimum for ±3% precision: n > 1,000
└─ Status: Insufficient information

[CHECK 13: MODEL SPECIFICATION CHECKER]
├─ Overfit risk: Unknown (no train/test split mentioned)
├─ External validation: Not mentioned
└─ Status: FLAGGED — Possible overfit

[CHECK 14: META-EPISTEMIC SELF-MONITOR]
├─ This validation has 85% confidence
└─ Status: High-stakes claim warrants human expert review

───────────────────────────────────────────────────────────────────────────

SUMMARY:
├─ Total Checks: 14
├─ Violations: 9
├─ Passes: 3
├─ N/A: 2

EPISTEMIC VIOLATIONS:
1. Completeness claim ("revolutionize")
2. Prediction horizon exceeded (2030)
3. Vague confidence (no CI)
4. Causation from correlation
5. Evidence grade D
6. Uncalibrated prediction
7. Low joint probability (8%)
8. Regulatory non-compliance
9. Possible overfit

CORRECTED CLAIM:
"Our AI diagnostic tool achieved 92-97% accuracy (95% CI) on a 1,200-patient 
internal validation set. External multi-site validation is pending. 
If FDA-approved and adopted, this technology could meaningfully assist 
diagnosis in specific use cases within 2-3 years. Healthcare transformation 
depends on factors beyond AI accuracy including regulatory approval, 
physician adoption, and health system integration. Success probability 
for stated goals: <10%."

EPISTEMIC DEBT INDEX:
├─ Assumption Debt: 4 unvalidated assumptions × 0.30 = 1.2
├─ Uncertainty Debt: 3 vague claims × 0.25 = 0.75
├─ Validation Debt: No external validation × 0.25 = 0.75
├─ Expiration Debt: 0 × 0.20 = 0
├─ EDI = 2.7 (HEALTHY, but claim strength far exceeds evidence)
└─ Warning: Low EDI doesn't validate excessive claims

VERDICT: ❌ FAIL — Major epistemic corrections required

═══════════════════════════════════════════════════════════════════════════
```

### Value Demonstrated

- 9 violations caught in "reasonable-sounding" claim
- Joint probability shows true success odds (~8%)
- Corrected claim maintains substance while adding honesty
- Regulatory gaps identified

---

## Example 2: Cross-Domain Fallacy Detection

### Scenario

A policy advisor argues that society should "treat misinformation like a disease" and develop "information vaccines."

### Input

```
EPISTEMIC DOMAIN:
Claim: "We should treat misinformation like a disease and develop vaccines 
       against it — information inoculation at scale"
Source: Medicine
Target: Information/Social
```

### Engine Output

```
═══════════════════════════════════════════════════════════════════════════
                CROSS-DOMAIN INFERENCE VALIDATION
═══════════════════════════════════════════════════════════════════════════

[STEP 1: DOMAIN IDENTIFICATION]

├─ Source Domain: Medicine (disease/treatment paradigm)
├─ Target Domain: Information/Social (truth/falsehood, social dynamics)
├─ Adjacency Score: 0.25 (from domain matrix)
└─ Classification: DISTANT — These are non-adjacent domains

[STEP 2: TRANSFER VALIDITY ASSESSMENT]

Q1: Is the underlying mechanism the same?
├─ Medical mechanism: 
│  Pathogen → Host invasion → Immune response → Antibody production
├─ Information mechanism:
│  Claim → Cognitive processing → Belief formation → Behavior
├─ Same? NO
│  ├─ Disease: External pathogen with objective existence
│  ├─ Misinformation: Contested claim, truth is often context-dependent
│  ├─ Immune system: Automatic biological response
│  └─ Belief formation: Complex, values-influenced, socially constructed
└─ Mechanism Score: 0.2

Q2: Are boundary conditions equivalent?
├─ Medical boundaries:
│  ├─ Ground truth exists (virus either present or not)
│  ├─ Testing is objective (lab tests, biomarkers)
│  └─ Harm is measurable (mortality, morbidity)
├─ Information boundaries:
│  ├─ "Truth" is often contested, not binary
│  ├─ No objective "test" for most information
│  └─ Harm is subjective and political
├─ Equivalent? NO
└─ Boundary Score: 0.15

Q3: Do domain experts accept this transfer?
├─ Medical experts: Generally silent or skeptical
├─ Information scientists: Mixed — some use metaphor, others reject
├─ Social scientists: Largely critical of medical framing
├─ Consensus: CONTESTED
└─ Expert Score: 0.4

Q4: What's the failure mode if transfer is wrong?
├─ Stakes: HIGH
│  ├─ Censorship risk: "False" determined by authority
│  ├─ Epistemic authoritarianism: One truth enforced
│  ├─ Political weaponization: Opponents labeled "diseased"
│  └─ Undermines legitimate discourse
├─ Reversibility: LOW (once censorship infrastructure built)
└─ Recommended scrutiny: BLOCK without extensive justification

[STEP 3: FALLACY CHECK]

├─ Physics Envy? NO
├─ Biological Essentialism? NO
├─ Engineering Solutionism? YES ⚠️
│  └─ Treating social/political problem as technical fix
├─ Medical Model Misapplication? YES ⚠️
│  └─ Disease/cure paradigm applied to contested beliefs
└─ Legal Formalism? NO

[CROSS-DOMAIN TRANSFER SCORE CALCULATION]

CDTS = (Adjacency × 0.25) + (Mechanism × 0.30) + 
       (Boundary × 0.20) + (Expert × 0.25)

CDTS = (0.25 × 0.25) + (0.2 × 0.30) + (0.15 × 0.20) + (0.4 × 0.25)
CDTS = 0.0625 + 0.06 + 0.03 + 0.10 = 0.2525

VERDICT: SUSPECT (0.2-0.4 range)

───────────────────────────────────────────────────────────────────────────

ANALYSIS:

The medical model breaks down at multiple points:

1. GROUND TRUTH PROBLEM
   Medical: Virus is objectively present or absent
   Information: "Truth" often contested, context-dependent
   
2. DIAGNOSIS PROBLEM
   Medical: Lab tests, biomarkers, objective criteria
   Information: Who decides what's "misinformation"?
   
3. CONSENT PROBLEM
   Medical: Patients consent to treatment
   Information: "Inoculation" implies without consent
   
4. AUTHORITY PROBLEM
   Medical: Doctors have legitimate epistemic authority
   Information: No equivalent legitimate truth authority

CORRECTED CLAIM:

"While the disease metaphor highlights the spread dynamics of misinformation, 
the analogy breaks down at critical points. Unlike pathogens, 'misinformation' 
lacks objective diagnostic criteria — what counts as false is often politically 
contested. Media literacy education may help people evaluate claims critically, 
but this is fundamentally different from vaccination, which creates automatic 
biological immunity. Any 'inoculation' approach must grapple with who decides 
truth and the risks of epistemic authoritarianism."

═══════════════════════════════════════════════════════════════════════════
```

### Value Demonstrated

- Category error caught with specific reasoning
- Fallacies identified (Medical Model, Engineering Solutionism)
- Risks of wrong transfer articulated
- Corrected claim preserves useful insight while respecting domain boundaries

---

## Example 3: Epistemic Debt Audit

### Scenario

A startup's Series B pitch deck contains market projections and competitive analysis. Audit the epistemic debt.

### Input

```
EPISTEMIC DEBT:
Document: Series B pitch deck containing:
- TAM of $50B growing 25% annually
- "We will capture 15% market share by 2027"
- Competitive analysis showing we're "clearly differentiated"
- Financial projections showing profitability by 2026
- Claim that customer interviews "validated product-market fit"
```

### Engine Output

```
═══════════════════════════════════════════════════════════════════════════
                    EPISTEMIC DEBT AUDIT — SERIES B PITCH
═══════════════════════════════════════════════════════════════════════════

[ASSUMPTION DEBT INVENTORY] (×0.30)

| Assumption | Validated? | Criticality | Debt Units |
|------------|------------|-------------|------------|
| TAM = $50B | NO (third-party estimate used) | High | 3 |
| 25% annual growth | NO (extrapolation) | Medium | 1 |
| 15% market share achievable | NO (aspiration) | Critical | 5 |
| Differentiation is sustainable | NO (assertion) | High | 3 |
| Profitability by 2026 | NO (projection) | High | 3 |
| PMF validated by interviews | PARTIALLY (20 interviews) | High | 2 |

Assumption Debt Subtotal: 17 units

[UNCERTAINTY DEBT INVENTORY] (×0.25)

| Vague Claim | Should Be | Debt Units |
|-------------|-----------|------------|
| TAM "is $50B" | "$40-65B (based on [source])" | 2 |
| "25% growth" | "15-35% growth (range)" | 2 |
| "15% share" | "5-20% share depending on [factors]" | 3 |
| "clearly differentiated" | "differentiated on [specific features]" | 2 |
| "validated PMF" | "20 positive interviews suggest PMF" | 2 |

Uncertainty Debt Subtotal: 11 units

[VALIDATION DEBT INVENTORY] (×0.25)

| Claim | Validation Needed | Done? | Debt Units |
|-------|-------------------|-------|------------|
| Financial projections | Historical comparison | NO | 3 |
| Growth rate | Industry benchmarking | NO | 2 |
| Market share trajectory | Backtesting vs. peers | NO | 2 |
| Competitive analysis | External audit | NO | 1 |

Validation Debt Subtotal: 8 units

[EXPIRATION DEBT INVENTORY] (×0.20)

| Data Source | Age | Domain | Half-Life | Ratio | Debt Units |
|-------------|-----|--------|-----------|-------|------------|
| Market research (2023) | 2 years | Tech/Market | 2 years | 1.0 | 2 |
| Competitive analysis | 6 months | Tech | 2 years | 0.25 | 0 |
| Customer interviews | 3 months | Product | 1 year | 0.25 | 0 |

Expiration Debt Subtotal: 2 units

───────────────────────────────────────────────────────────────────────────

[EPISTEMIC DEBT INDEX CALCULATION]

EDI = (Assumption × 0.30) + (Uncertainty × 0.25) + 
      (Validation × 0.25) + (Expiration × 0.20)

EDI = (17 × 0.30) + (11 × 0.25) + (8 × 0.25) + (2 × 0.20)
EDI = 5.1 + 2.75 + 2.0 + 0.4 = 10.25

LEVEL: ELEVATED (11-25 range threshold approaching)

───────────────────────────────────────────────────────────────────────────

[DEBT SERVICE RECOMMENDATIONS]

Priority 1: VALIDATE CRITICAL ASSUMPTIONS
├─ Commission third-party TAM validation
├─ Stress-test market share assumptions with bear case
└─ Estimated reduction: -5 EDI points

Priority 2: ADD UNCERTAINTY RANGES
├─ Replace point estimates with ranges
├─ Acknowledge key dependencies
└─ Estimated reduction: -3 EDI points

Priority 3: BACKTEST PROJECTIONS
├─ Compare projections to similar-stage companies
├─ Document where projections diverge from norms
└─ Estimated reduction: -2 EDI points

Priority 4: REFRESH MARKET DATA
├─ Update 2023 market research
└─ Estimated reduction: -1 EDI point

[TOTAL DEBT SERVICE EFFORT]
├─ Time: 2-3 weeks
├─ Cost: $15-30K for third-party validation
└─ Post-service EDI: ~3-5 (HEALTHY)

───────────────────────────────────────────────────────────────────────────

[INVESTOR COMMUNICATION RECOMMENDATION]

Before Pitch:
"We will capture 15% market share in a $50B market by 2027."

After Debt Service:
"We're targeting 5-15% of an estimated $40-65B market by 2027. Our base 
case assumes 15% growth and successful differentiation on [specific features]. 
Third-party validation of TAM is in progress. Financial projections are 
consistent with top-quartile performers in our category, with key sensitivities 
to [factors]. Customer interviews (n=20) suggest strong PMF, with broader 
validation planned."

═══════════════════════════════════════════════════════════════════════════
```

### Value Demonstrated

- Specific debt inventory with actionable items
- Clear prioritization of what to fix
- Before/after claim comparison
- Cost/time estimate for debt service

---

## Example Summary

| Example | Scenario | Key Insight |
|---------|----------|-------------|
| 1. Medical AI | Overclaim validation | 9 violations in "reasonable" claim; 8% true success probability |
| 2. Disease Metaphor | Cross-domain fallacy | Medical model fails at ground truth, diagnosis, consent |
| 3. Pitch Deck | Epistemic debt audit | EDI quantifies assumption/validation gaps |

---

**Epistemic Humility Validator v3.1** — The Intellectual Humility Engine

*Examples demonstrate: Overclaim detection, category error catching, and debt quantification.*
