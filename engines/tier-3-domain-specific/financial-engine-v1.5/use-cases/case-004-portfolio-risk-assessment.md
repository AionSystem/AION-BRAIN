# Use Case 004: Portfolio Risk Assessment

**Engine:** Financial Engine v1.5
**Domain:** Investment Risk Analysis
**Complexity:** High
**Risk Level:** HIGH (fiduciary implications)

---

## Scenario Description

An investment adviser needs to assess portfolio risk for a client approaching retirement. The analysis must identify concentration risks, volatility exposure, and sequence-of-returns vulnerability without providing personalized investment advice.

---

## CEREBRO Pattern Amplification Applied

### Shannon Framework (Information Density)
```
[SHANNON ANALYSIS]:
├─ Information Density: HIGH
├─ Portfolio complexity: Multi-asset, multi-sector
├─ Redundancy Detected: Overlapping sector exposure in ETFs
├─ Signal-to-Noise Ratio: MEDIUM (market noise vs. structural risk)
└─ Compression Potential: Risk can be summarized via factor exposure
```

### Mandelbrot Framework (Self-Similarity)
```
[MANDELBROT ANALYSIS]:
├─ Self-Similarity: APPROXIMATE FRACTAL
├─ Power Law: DETECTED in drawdown distribution (α ≈ 2.3)
├─ Scale Invariance: Volatility clusters at multiple timeframes
├─ Fat Tails: Present (extreme events more likely than normal distribution)
└─ Implication: Standard deviation understates true risk
```

---

## Oracle Layer Self-Correction Protocol

```
<SELF_CORRECTION_PROTOCOL>
CHECKPOINT 1: After Each Risk Metric
├─ STOP and ask: "Is this calculation methodology standard?"
├─ IF YES: Cite methodology source
├─ IF NO: Mark [VERIFY_REQUIRED:methodology_review]
└─ NEVER present non-standard risk metrics without disclosure

CHECKPOINT 2: After Risk Assessment
├─ VERIFY: Did I avoid personalized advice?
├─ VERIFY: Did I disclose all material assumptions?
├─ IF UNCERTAIN: Add [EDUCATIONAL_ONLY] disclaimer
└─ FABRICATION RED FLAGS:
  • Precise percentage predictions
  • Guarantees about future performance
  • Specific buy/sell recommendations
</SELF_CORRECTION_PROTOCOL>
```

---

## Word Engine Semantic Safety Applied

### Lens 5: Directional Layer
```
WORD: "recommend"
DIRECTIONAL ANALYSIS:
├─ AVOID: Implies personalized advice
├─ REPLACE WITH: "illustrate", "demonstrate", "analyze"
├─ Reason: Fiduciary duty triggers on advice language
└─ Safe Alternative: "This analysis illustrates risk factors..."
```

---

## Input/Output Example

### Query
```
<FINANCIAL_ENGINE_v1.5>
<MODE: PORTFOLIO_RISK_ANALYSIS>
<MODULE: RISK_ASSESSMENT>

CONTEXT:
- Portfolio: 60% equities, 40% bonds
- Client age: 62, retiring in 3 years
- Portfolio value: $1.2M
- Income need: $50,000/year in retirement

QUESTION:
What risk factors should be considered for this portfolio allocation?

<fabrication:block>
<source_verification:required>
<fail_response:"Risk assessment requires verified market data">
</FINANCIAL_ENGINE_v1.5>
```

### Engine Response
```
[REASONING]:
├─ QUESTION: What risk factors apply to this allocation?
├─ DATA CONSIDERED: Asset allocation, time horizon, income needs
├─ CONFIDENCE: MEDIUM-HIGH (general principles, not personalized)
├─ GAPS: Actual holdings, tax situation, other income sources

PORTFOLIO RISK ANALYSIS (Educational Only)
=========================================

1. SEQUENCE-OF-RETURNS RISK
   ├─ Definition: Order of returns matters near/in retirement
   ├─ Relevance: 3-year horizon places client in "risk zone"
   ├─ Consideration: Early losses + withdrawals = accelerated depletion
   └─ [VERIFY_REQUIRED:financial_adviser_assessment]

2. CONCENTRATION RISK
   ├─ Question: Is equity allocation concentrated in sectors/stocks?
   ├─ Analysis Needed: Holdings-level breakdown
   ├─ General Principle: Single-sector concentration amplifies volatility
   └─ [VERIFY_REQUIRED:holdings_analysis]

3. INTEREST RATE SENSITIVITY
   ├─ Bond allocation: 40%
   ├─ Duration exposure: Unknown without holdings data
   ├─ General Principle: Rising rates = bond price decline
   └─ [VERIFY_REQUIRED:duration_analysis]

4. INFLATION RISK
   ├─ Fixed income vulnerability to purchasing power erosion
   ├─ Long retirement horizon (potentially 30+ years)
   ├─ Real return consideration critical
   └─ [EDUCATIONAL_NOTE:not_investment_advice]

5. WITHDRAWAL RATE SUSTAINABILITY
   ├─ $50K / $1.2M = 4.17% initial withdrawal rate
   ├─ Historical research (Trinity Study) suggests 4% as baseline
   ├─ Individual circumstances vary significantly
   └─ [VERIFY_REQUIRED:personalized_planning_needed]

[ETHICAL_BOUNDARY:no_personalized_advice]
This analysis is educational. A registered investment adviser
can provide personalized assessment for your specific situation.

⚠️ CONFIDENCE: MEDIUM
├─ HIGH confidence on general risk factors
├─ MEDIUM confidence on applicability to specific situation
└─ LOW confidence without complete holdings data
```

---

## Compliance Checkpoints

| Checkpoint | Status | Validation |
|------------|--------|------------|
| No personalized advice | PASS | Educational framing maintained |
| No performance guarantees | PASS | Probabilistic language used |
| Suitability disclaimer | PASS | Adviser referral included |
| Source verification | PASS | [VERIFY_REQUIRED] tags present |
| Fiduciary boundary | PASS | No specific recommendations |

---

## LBE Verification Gate Status

```
VERIFICATION STATUS:
├─ verified_automated: 0 claims
├─ verified_human: 0 claims (requires adviser review)
├─ unverified: 5 risk factors (general principles)
├─ no_evidence_found: N/A (educational content)
└─ end_state: CLEARED (educational use only)
```

---

**Use Case Version:** 1.5
**Last Updated:** November 2025
