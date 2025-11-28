# Confidence Calibration Framework — Medical Engine v2.6

**Classification:** Quality Assurance
**Purpose:** Ensure AI confidence matches actual accuracy
**Innovation Level:** Beyond Enterprise Standard

---

## Overview

Confidence calibration ensures that when Medical Engine v2.6 expresses HIGH confidence, it is actually correct at a high rate, and when it expresses LOW confidence, users know to verify carefully. Miscalibrated confidence is dangerous—overconfidence leads to missed errors, underconfidence leads to decision paralysis.

**The Goal:** When the engine says "HIGH confidence," it should be right 90%+ of the time.

---

## Calibration Framework

### Confidence Level Definitions

| Level | Label | Target Accuracy | Verification Requirement |
|-------|-------|-----------------|-------------------------|
| 1 | VERY HIGH | 95%+ | Minimal verification |
| 2 | HIGH | 85-95% | Spot-check recommended |
| 3 | MEDIUM | 70-85% | Verification required |
| 4 | LOW | 50-70% | Significant verification |
| 5 | SPECULATIVE | <50% | Treat as hypothesis only |

### Calibration Curves

```
IDEAL CALIBRATION (Diagonal Line):
Stated Confidence = Actual Accuracy

OVERCONFIDENCE (Above Diagonal):
Stated Confidence > Actual Accuracy
⚠️ DANGEROUS: Users trust incorrect outputs

UNDERCONFIDENCE (Below Diagonal):
Stated Confidence < Actual Accuracy
⚠️ INEFFICIENT: Users over-verify correct outputs

TARGET: Within ±5% of diagonal at all confidence levels
```

---

## Domain-Specific Calibration

### Drug Information

```
DRUG INFORMATION CONFIDENCE CALIBRATION
=======================================

HIGH CONFIDENCE APPROPRIATE WHEN:
├─ FDA-approved labeling (BLACK BOX, dosing)
├─ Major drug-drug interactions (Level A evidence)
├─ Contraindications clearly documented
├─ Standard adult dosing in healthy patients
└─ Well-established mechanism of action

MEDIUM CONFIDENCE APPROPRIATE WHEN:
├─ Off-label uses with moderate evidence
├─ Dosing adjustments (renal, hepatic)
├─ Drug-drug interactions (Level B-C evidence)
├─ Pediatric extrapolation from adult data
└─ Combination therapy effects

LOW CONFIDENCE APPROPRIATE WHEN:
├─ Rare drug interactions
├─ Novel drug combinations
├─ Dosing in complex patients
├─ Emerging safety signals
└─ Limited evidence base

SPECULATIVE APPROPRIATE WHEN:
├─ Theoretical interactions only
├─ Case report level evidence
├─ Extrapolation across drug classes
├─ Predictive pharmacology
└─ No direct data available
```

### Diagnosis Support

```
DIAGNOSIS CONFIDENCE CALIBRATION
================================

HIGH CONFIDENCE APPROPRIATE WHEN:
├─ Classic presentation of common condition
├─ Pathognomonic findings present
├─ Objective diagnostic criteria met
├─ Strong positive predictive value tests
└─ Consistent clinical picture

MEDIUM CONFIDENCE APPROPRIATE WHEN:
├─ Typical but not classic presentation
├─ Some atypical features present
├─ Supporting but not definitive testing
├─ Multiple conditions in differential
└─ Risk factors present but incomplete picture

LOW CONFIDENCE APPROPRIATE WHEN:
├─ Atypical presentation
├─ Rare conditions in differential
├─ Conflicting clinical data
├─ Incomplete information
└─ Complex multi-system involvement

SPECULATIVE APPROPRIATE WHEN:
├─ Highly unusual presentations
├─ Very rare conditions
├─ Minimal clinical data
├─ Novel disease presentations
└─ Outside training data distribution
```

---

## Calibration Measurement

### Calibration Metrics

```
CALIBRATION QUALITY METRICS
===========================

1. EXPECTED CALIBRATION ERROR (ECE)
   Measures average gap between confidence and accuracy
   Target: ECE < 0.05 (5%)

2. MAXIMUM CALIBRATION ERROR (MCE)
   Worst-case calibration gap
   Target: MCE < 0.15 (15%)

3. BRIER SCORE
   Mean squared difference between probability and outcome
   Target: Brier < 0.1

4. RELIABILITY DIAGRAM
   Visual plot of confidence vs. accuracy bins
   Target: Points close to diagonal

CALCULATION:
For each confidence bin b:
├─ Count predictions n_b
├─ Calculate average confidence conf_b
├─ Calculate actual accuracy acc_b
└─ ECE = Σ (n_b / N) × |conf_b - acc_b|
```

### Calibration Testing Protocol

```
CALIBRATION TESTING PROTOCOL
============================

STEP 1: COLLECT TEST SET
├─ Diverse clinical scenarios
├─ Known ground truth answers
├─ Representative of real usage
└─ Minimum 500 test cases per domain

STEP 2: GENERATE PREDICTIONS
├─ Engine processes each case
├─ Record stated confidence level
├─ Record prediction/recommendation
└─ No human intervention

STEP 3: VERIFY OUTCOMES
├─ Compare predictions to ground truth
├─ Binary: Correct/Incorrect
├─ Score by confidence bin
└─ Calculate accuracy per bin

STEP 4: COMPUTE CALIBRATION
├─ Expected Calibration Error
├─ Maximum Calibration Error
├─ Reliability diagram
└─ Brier score

STEP 5: ADJUST IF NEEDED
├─ If overconfident: Lower confidence thresholds
├─ If underconfident: Raise confidence thresholds
├─ Retrain prompts if systematic issues
└─ Domain-specific adjustments
```

---

## Confidence Expression Protocol

### Standard Confidence Output

```
CONFIDENCE EXPRESSION TEMPLATE
==============================

[CLINICAL_OUTPUT]
Content: [Clinical recommendation or information]

Confidence: [VERY HIGH / HIGH / MEDIUM / LOW / SPECULATIVE]

Basis:
├─ Evidence quality: [Strong / Moderate / Limited / Minimal]
├─ Source reliability: [Authoritative / Standard / Variable]
├─ Context match: [Exact / Close / Approximate / Extrapolated]
└─ Data recency: [Current / Recent / Dated / Historical]

If MEDIUM or lower:
Verification recommended: [Specific verification steps]

If LOW or SPECULATIVE:
⚠️ This output requires significant verification before clinical use.
Consider: [Alternative approaches, additional testing, specialist consult]
```

### Confidence Adjustment Triggers

```
AUTOMATIC CONFIDENCE REDUCTION TRIGGERS
=======================================

REDUCE BY ONE LEVEL IF:
├─ Query involves pediatric population
├─ Query involves pregnancy/lactation
├─ Query involves multiple comorbidities
├─ Query involves rare condition
├─ Query asks about off-label use
├─ Source currency >2 years
├─ Multiple credible sources disagree
└─ Query involves novel drug/treatment

REDUCE BY TWO LEVELS IF:
├─ Query involves neonatal population
├─ Query involves multiple rare conditions
├─ No authoritative source available
├─ Significant extrapolation required
├─ Query outside clear training distribution
└─ Multiple safety concerns present

NEVER STATE HIGH CONFIDENCE IF:
├─ Fabrication risk detected
├─ Citation cannot be verified
├─ Safety-critical decision involved
├─ Individual patient factors complex
└─ Ground truth cannot be established
```

---

## User Education

### Interpreting Confidence

```
USER GUIDE: UNDERSTANDING CONFIDENCE LEVELS
============================================

VERY HIGH (95%+ accurate):
"You can generally rely on this information, but always verify
safety-critical decisions with authoritative sources."

HIGH (85-95% accurate):
"This information is likely correct, but spot-checking
recommended especially for unusual cases."

MEDIUM (70-85% accurate):
"This information needs verification. Consider it a starting
point for your own research or consultation."

LOW (50-70% accurate):
"Significant uncertainty exists. Use this only as one input
among many, and verify thoroughly."

SPECULATIVE (<50% accurate):
"This is an educated guess based on limited information.
Treat as hypothesis requiring substantial verification."

REMEMBER:
Even VERY HIGH confidence is not 100%.
All clinical decisions require professional judgment.
This engine supports but never replaces clinical expertise.
```

---

## Files in This Directory

| File | Purpose |
|------|---------|
| calibration-methodology.md | Detailed calibration procedures |
| domain-calibration-tables.md | Domain-specific confidence mapping |
| calibration-test-results.csv | Historical calibration data |
| adjustment-protocols.md | How to adjust calibration |
| user-interpretation-guide.md | Guidance for users |

---

**Innovation Note:** Most AI systems provide confidence scores without validating calibration. This framework ensures stated confidence actually reflects accuracy, preventing the dangerous situation where users trust overconfident wrong answers.

---

**Framework Version:** 1.0
**Last Updated:** November 2025
**Calibration Review Cycle:** Quarterly
