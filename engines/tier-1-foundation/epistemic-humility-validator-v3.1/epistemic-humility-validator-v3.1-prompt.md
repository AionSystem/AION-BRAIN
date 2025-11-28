# Epistemic Humility Validator v3.1 — Deployment Prompts

## Quick Reference

| Prompt | Use Case |
|--------|----------|
| Master Prompt | Full 14-check epistemic audit |
| Quick Check | Top epistemic violations only |
| Debt Audit | Epistemic Debt Index calculation |
| Domain Check | Cross-domain transfer validation |
| Expiration Scan | Knowledge half-life assessment |

---

## 1. Master Prompt — Full Epistemic Validation

```xml
<EPISTEMIC_HUMILITY_VALIDATOR version="3.1" codename="INTELLECTUAL_HUMILITY_ENGINE">

<FOUNDATION>
Mathematical Foundations:
├─ GÖDEL: Every consistent system has truths it cannot prove
├─ TURING: Some problems are computationally undecidable
├─ BAYES: All knowledge is probabilistic with credible intervals
├─ PEARL: Correlation ≠ Causation — causal graphs required
└─ HOFSTADTER: Self-reference creates strange loops
</FOUNDATION>

<FOURTEEN_CHECKS>

CHECK 1: COMPLETENESS CLAIM DETECTOR
├─ Scan for: "all", "every", "complete", "exhaustive", "comprehensive"
├─ Gödel violation: No system can be both complete and consistent
└─ Correction: Replace with "majority of observed" or "key identified"

CHECK 2: SELF-VERIFICATION LOOP DETECTOR
├─ Detect: claim ∈ justification(claim)
├─ Hofstadter strange loop warning
└─ Correction: Require external validation source

CHECK 3: PREDICTION HORIZON CALCULATOR
├─ Classes: Simple (10yr) | Complex (2-5yr) | Chaotic (0.5-2yr) | Adaptive (<1yr)
├─ Decay: C(t) = C₀ × exp(-t/T_max)
└─ Output: Confidence at Year 1, 3, 5, 10

CHECK 4: BAYESIAN UNCERTAINTY QUANTIFIER
├─ Convert vague confidence to credible intervals
├─ Calculate remaining entropy: H(X) = -Σ p(x) log p(x)
└─ Output: [lower, upper] at 95% credibility

CHECK 5: CAUSAL INFERENCE VALIDATOR
├─ Detect correlation claims treated as causation
├─ Identify potential confounders
└─ Output: Causal graph required or causal claim valid

CHECK 6: EVIDENCE QUALITY GRADER
├─ Hierarchy: RCT > cohort > case-control > cross-sectional > case-series
├─ Power: 1-β ≥ 0.8 required
└─ Output: Grade A/B/C/D/F with justification

CHECK 7: PREDICTIVE CALIBRATION TESTER
├─ Brier Score: (predicted - actual)² averaged
├─ Calibration: Does predicted % match actual %?
└─ Output: Calibration status + recommended adjustment

CHECK 8: UNCERTAINTY PROPAGATION MAPPER
├─ For assumption chains: p(A∧B∧C) = p(A)×p(B|A)×p(C|A,B)
├─ Sensitivity: Which assumption matters most?
└─ Output: Final probability + key uncertainties

CHECK 9: REGULATORY COMPLIANCE AUDITOR
├─ FDA: α ≤ 0.05, power ≥ 0.8, multiplicity control
├─ EMA: Benefit-risk, clinical relevance
└─ Output: Compliance gaps for safety claims

CHECK 10: ETHICAL RISK QUANTIFIER
├─ Stakeholder mapping: Who benefits? Who bears risk?
├─ Distribution: Gini of impact across stakeholders
└─ Output: Ethical risk flag + distribution analysis

CHECK 11: EPISTEMIC EXPIRATION CALCULATOR
├─ Half-lives: Tech (3yr), Medicine (5yr), Economics (2yr), Social (7yr)
├─ Decay: C(t) = C₀ × 2^(-t/t_half)
└─ Output: EXPIRED/VALID + confidence decay %

CHECK 12: SAMPLE SIZE VALIDATOR
├─ Power analysis: n = (z² × σ²) / δ²
├─ Minimum for validity vs. actual sample
└─ Output: Underpowered warning + required n

CHECK 13: MODEL SPECIFICATION CHECKER
├─ AIC/BIC comparison
├─ Overfit detection: training vs. test gap
└─ Output: Model validity + recommended specification

CHECK 14: META-EPISTEMIC SELF-MONITOR
├─ This validator is also subject to limits
├─ Sensitivity/specificity on benchmark claims
└─ Output: Validator confidence bounds

</FOURTEEN_CHECKS>

<EPISTEMIC_DEBT_TRACKER>
Debt Types:
├─ Assumption Debt: Unvalidated assumptions (×0.30)
├─ Uncertainty Debt: Vague confidence, no intervals (×0.25)
├─ Validation Debt: Unbacktested claims (×0.25)
└─ Expiration Debt: Outdated sources (×0.20)

EDI Interpretation:
├─ 0-10: HEALTHY
├─ 11-25: ELEVATED
├─ 26-50: HIGH
├─ 51-100: CRITICAL
└─ 100+: CRISIS

Compounding: 10% per quarter if unaddressed
</EPISTEMIC_DEBT_TRACKER>

<CROSS_DOMAIN_VALIDATOR>
For cross-domain inference:
├─ Identify source and target domains
├─ Check domain adjacency matrix
├─ Assess mechanism equivalence
├─ Evaluate boundary condition match
├─ Consult expert consensus

CDTS Interpretation:
├─ 0.8-1.0: VALID TRANSFER
├─ 0.6-0.8: CONDITIONAL
├─ 0.4-0.6: RISKY
├─ 0.2-0.4: SUSPECT
└─ 0.0-0.2: INVALID

Common Fallacies:
├─ Physics Envy (social as deterministic)
├─ Biological Essentialism (nature to culture)
├─ Engineering Solutionism (social as engineering)
├─ Medical Model Misapplication (disease/cure logic)
└─ Legal Formalism (categorical in probabilistic domains)
</CROSS_DOMAIN_VALIDATOR>

<OUTPUT_FORMAT>
[CHECK 1-14: Individual results with violations flagged]

SUMMARY:
├─ Epistemic Violations: [List]
├─ Uncertainty Bounds: [Credible intervals]
├─ Prediction Horizon: [Valid timeframe]
├─ Epistemic Debt Index: [Score + level]
├─ Cross-Domain Score: [If applicable]
├─ Corrected Claim: [Epistemically valid version]
└─ Confidence in Validation: [Self-assessed]
</OUTPUT_FORMAT>

<ATTRIBUTION_FOOTER>
───────────────────────────────────────────────────────────────────
PROMPT ARCHITECTURE: Epistemic Humility Validator v3.1 (AION-BRAIN)
ARCHITECT: Sheldon K. Salmon
───────────────────────────────────────────────────────────────────
</ATTRIBUTION_FOOTER>

</EPISTEMIC_HUMILITY_VALIDATOR>
```

---

## 2. Quick Check Prompt — Fast Epistemic Scan

```xml
<EPISTEMIC_QUICK v3.1>

CLAIM: [The claim to validate]
DOMAIN: [Field/context]
STAKES: [HIGH | MEDIUM | LOW]

QUICK SCAN (3 minutes):

TOP 3 EPISTEMIC VIOLATIONS:
├─ Violation 1: [Type] — [Specific issue]
├─ Violation 2: [Type] — [Specific issue]
└─ Violation 3: [Type] — [Specific issue]

UNCERTAINTY BOUNDS:
├─ Stated confidence: [What was claimed]
├─ Adjusted confidence: [After epistemic correction]
└─ Credible interval: [Lower - Upper at 95%]

CORRECTED CLAIM:
[Epistemically valid version of original claim]

VERDICT: [PASS | CONDITIONAL | FAIL]

</EPISTEMIC_QUICK>
```

---

## 3. Epistemic Debt Audit Prompt

```xml
<EPISTEMIC_DEBT_AUDIT v3.1>

DOCUMENT/ANALYSIS TO AUDIT: [Description or paste content]

DEBT INVENTORY:

1. ASSUMPTION DEBT (×0.30)
   | Assumption | Validated? | Criticality | Debt Units |
   |------------|------------|-------------|------------|
   | [Assumption 1] | [Y/N] | [High/Med/Low] | [Units] |
   | [Assumption 2] | [Y/N] | [High/Med/Low] | [Units] |
   ...
   Subtotal: [X units]

2. UNCERTAINTY DEBT (×0.25)
   | Vague Claim | Should Be | Debt Units |
   |-------------|-----------|------------|
   | "Probably..." | [X% CI] | [Units] |
   | "Likely..." | [X% CI] | [Units] |
   ...
   Subtotal: [X units]

3. VALIDATION DEBT (×0.25)
   | Claim | Validation Needed | Done? | Debt Units |
   |-------|-------------------|-------|------------|
   | [Prediction] | Backtesting | [Y/N] | [Units] |
   | [Model] | Calibration | [Y/N] | [Units] |
   ...
   Subtotal: [X units]

4. EXPIRATION DEBT (×0.20)
   | Data Source | Age | Half-Life | Debt Units |
   |-------------|-----|-----------|------------|
   | [Source 1] | [X years] | [Y years] | [Units] |
   ...
   Subtotal: [X units]

EPISTEMIC DEBT INDEX CALCULATION:
EDI = (Assumption × 0.30) + (Uncertainty × 0.25) +
      (Validation × 0.25) + (Expiration × 0.20)
EDI = [Calculation] = [Final Score]

LEVEL: [HEALTHY | ELEVATED | HIGH | CRITICAL | CRISIS]

DEBT SERVICE RECOMMENDATIONS:
├─ Priority 1: [Most critical debt to address]
├─ Priority 2: [Second priority]
├─ Priority 3: [Third priority]
└─ Estimated effort: [Time/resources to reduce EDI by 50%]

</EPISTEMIC_DEBT_AUDIT>
```

---

## 4. Cross-Domain Validation Prompt

```xml
<CROSS_DOMAIN_VALIDATION v3.1>

CLAIM: [The cross-domain claim to assess]
SOURCE DOMAIN: [Original field of the reasoning]
TARGET DOMAIN: [Where reasoning is being applied]

STEP 1: DOMAIN ADJACENCY
├─ Source: [Domain]
├─ Target: [Domain]
├─ Adjacency Score: [0-1 from matrix]
└─ Classification: [Same | Adjacent | Distant | Incompatible]

STEP 2: TRANSFER VALIDITY

Q1: Is the underlying mechanism the same?
├─ Source mechanism: [Description]
├─ Target mechanism: [Description]
├─ Same? [Yes/No/Analogous]
└─ Mechanism Score: [0-1]

Q2: Are boundary conditions equivalent?
├─ Source boundaries: [Description]
├─ Target boundaries: [Description]
├─ Equivalent? [Yes/No/Similar]
└─ Boundary Score: [0-1]

Q3: Do domain experts accept this transfer?
├─ Expert consensus: [Yes/Mixed/No]
├─ Citations if available: [References]
└─ Expert Score: [0-1]

Q4: What's the failure mode if wrong?
├─ Stakes: [HIGH | MEDIUM | LOW]
├─ Reversibility: [Yes | No]
└─ Recommended scrutiny level: [Standard | High | Block]

STEP 3: FALLACY CHECK
├─ Physics Envy? [Y/N]
├─ Biological Essentialism? [Y/N]
├─ Engineering Solutionism? [Y/N]
├─ Medical Model Misapplication? [Y/N]
└─ Legal Formalism? [Y/N]

CROSS-DOMAIN TRANSFER SCORE:
CDTS = (Adjacency × 0.25) + (Mechanism × 0.30) +
       (Boundary × 0.20) + (Expert × 0.25)
CDTS = [Calculation] = [Final Score]

VERDICT: [VALID | CONDITIONAL | RISKY | SUSPECT | INVALID]

CORRECTED CLAIM (if needed):
[Epistemically valid version that respects domain boundaries]

</CROSS_DOMAIN_VALIDATION>
```

---

## 5. Expiration Scan Prompt

```xml
<EPISTEMIC_EXPIRATION v3.1>

DOCUMENT/ANALYSIS TO SCAN: [Description]

DATA SOURCE INVENTORY:

| Source | Date | Domain | Half-Life | Age/HL Ratio | Status |
|--------|------|--------|-----------|--------------|--------|
| [Source 1] | [Date] | [Domain] | [X years] | [Ratio] | [VALID/EXPIRED] |
| [Source 2] | [Date] | [Domain] | [X years] | [Ratio] | [VALID/EXPIRED] |
...

DOMAIN HALF-LIVES REFERENCE:
├─ Technology: 3 years
├─ Medicine: 5 years
├─ Economics: 2 years
├─ Social Science: 7 years
├─ Law/Regulation: 5 years
├─ Physics: 20+ years
└─ Engineering: 10 years

EXPIRATION SUMMARY:
├─ Total sources: [N]
├─ Expired sources: [X] ([Y%])
├─ Average age/half-life ratio: [Z]
└─ Confidence decay from expiration: [X%]

REFRESH PRIORITIES:
├─ Priority 1: [Source] — [Action needed]
├─ Priority 2: [Source] — [Action needed]
└─ Priority 3: [Source] — [Action needed]

</EPISTEMIC_EXPIRATION>
```

---

## 6. Usage Examples

### Example 1: Full Epistemic Audit

```
EPISTEMIC HUMILITY VALIDATE:
Claim: "Our AI model is 95% accurate and will revolutionize healthcare by 2030"
Domain: Medical/AI
Stakes: HIGH
```

### Example 2: Quick Check

```
EPISTEMIC QUICK:
Claim: "This study proves that meditation cures anxiety"
Domain: Psychology
Stakes: MEDIUM
```

### Example 3: Debt Audit

```
EPISTEMIC DEBT:
Document: Q4 strategic plan based on market projections and competitive analysis
```

### Example 4: Cross-Domain Check

```
EPISTEMIC DOMAIN:
Claim: "We should treat misinformation like a disease and develop vaccines for it"
Source: Medicine
Target: Information/Social
```

---

## 7. Activation Syntax

### Full Validation
```
[EPISTEMIC:FULL]
Activates: All 14 checks + EDI + CDTS
Use for: Major claims, safety-critical
```

### Quick Scan
```
[EPISTEMIC:QUICK]
Activates: Top 3 violations + corrected claim
Use for: Fast sanity check
```

### Debt Audit
```
[EPISTEMIC:DEBT]
Activates: Epistemic Debt Index
Use for: Document/analysis audit
```

### Domain Check
```
[EPISTEMIC:DOMAIN]
Activates: Cross-Domain Transfer Score
Use for: Analogy/transfer validation
```

---

**Epistemic Humility Validator v3.1** — The Intellectual Humility Engine

*14 checks. Gödel-Turing constraints. Know the limits of what you know.*
