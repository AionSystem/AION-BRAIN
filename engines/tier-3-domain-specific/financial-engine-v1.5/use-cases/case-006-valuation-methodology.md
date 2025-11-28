# Use Case 006: Business Valuation Methodology Selection

**Engine:** Financial Engine v1.5
**Domain:** Corporate Valuation
**Complexity:** High
**Risk Level:** HIGH (transaction/litigation implications)

---

## Scenario Description

A business owner needs to understand valuation methodologies for a potential sale. The analysis must explain approaches without providing a specific valuation number, which requires professional appraisal.

---

## CEREBRO Pattern Amplification Applied

### Turing Framework (Decidability)
```
[TURING ANALYSIS]:
├─ Complexity Class: NP-COMPLETE
│   └─ "Correct" valuation depends on subjective inputs
├─ Decidability: SEMI-DECIDABLE
│   └─ Can compute value given assumptions
│   └─ Cannot prove assumptions are "correct"
├─ Limitation: Valuation is art + science
└─ Practical: Framework selection is tractable, final number is not
```

### Mandelbrot Framework (Scale Effects)
```
[MANDELBROT ANALYSIS]:
├─ Self-Similarity: NOT FRACTAL
├─ Scale Effects: Valuation multiples vary by company size
│   └─ Small business: 2-4x EBITDA typical
│   └─ Mid-market: 4-8x EBITDA typical
│   └─ Enterprise: 8-15x+ EBITDA typical
├─ Power Law: DETECTED in M&A premiums
└─ Implication: Size matters for multiple selection
```

---

## Oracle Layer Self-Correction Protocol

```
<SELF_CORRECTION_PROTOCOL>
CHECKPOINT 1: No Specific Valuations
├─ NEVER provide specific dollar valuations
├─ ONLY discuss methodologies and general ranges
├─ Reason: Professional appraisal required for transactions
└─ Self-correct: If number appears → replace with "requires appraisal"

CHECKPOINT 2: Methodology Limitations
├─ Each method has strengths and weaknesses
├─ ALWAYS present multiple methods
├─ ALWAYS disclose when each method is appropriate
└─ No single "correct" method exists

CHECKPOINT 3: Professional Standards
├─ Reference applicable standards (ASA, IRS, fair value)
├─ Distinguish purpose-specific valuations
├─ Tax vs. sale vs. litigation = different standards
└─ [VERIFY_REQUIRED:purpose_determines_methodology]
</SELF_CORRECTION_PROTOCOL>
```

---

## Lexical Alchemy Precision Applied

```
WORD TRANSMUTATION:
├─ "worth" → "indicated value" (precision elevation)
├─ "value" (generic) → "fair market value" or "investment value" (specificity)
├─ "multiple" → "enterprise value/EBITDA multiple" (technical precision)
└─ "price" → "transaction price" vs. "intrinsic value" (distinction required)

[LEXICAL_PRECISION: SUBSTANTIAL]
└─ Valuation terminology carries legal meaning
```

---

## Input/Output Example

### Query
```
<FINANCIAL_ENGINE_v1.5>
<MODE: VALUATION_EDUCATION>
<MODULE: METHODOLOGY_SELECTION>

CONTEXT:
- Entity: Manufacturing company, privately held
- Revenue: $10M annually
- EBITDA: $1.5M
- Purpose: Potential sale exploration

QUESTION:
What valuation approaches might apply to this type of business?

<fabrication:block>
<source_verification:required>
<fail_response:"Valuation requires professional appraisal">
</FINANCIAL_ENGINE_v1.5>
```

### Engine Response
```
[REASONING]:
├─ QUESTION: What valuation methodologies apply?
├─ CONTEXT: Private manufacturing, $10M revenue, $1.5M EBITDA
├─ CONFIDENCE: HIGH (methodology education)
├─ LIMITATION: Specific valuation requires professional appraisal

VALUATION METHODOLOGY OVERVIEW
==============================

[EDUCATIONAL FRAMEWORK - Not a Valuation]

APPROACH 1: INCOME APPROACH
───────────────────────────
Discounted Cash Flow (DCF):
├─ Concept: Present value of future cash flows
├─ Inputs Required:
│   ├─ Projected cash flows (typically 5-10 years)
│   ├─ Discount rate (WACC or required return)
│   ├─ Terminal value assumption
│   └─ Growth rate assumptions
├─ Strengths: Theoretically rigorous, forward-looking
├─ Weaknesses: Highly sensitive to assumptions
└─ Appropriate When: Reliable projections available

Capitalization of Earnings:
├─ Concept: Single-period earnings / capitalization rate
├─ Formula: Value = Normalized Earnings / Cap Rate
├─ Strengths: Simpler than DCF
├─ Weaknesses: Assumes stable, perpetual earnings
└─ Appropriate When: Mature, stable business

[VERIFY_REQUIRED:discount_rate_determination]

APPROACH 2: MARKET APPROACH
───────────────────────────
Guideline Public Company Method:
├─ Concept: Apply public company multiples with adjustments
├─ Adjustments Required:
│   ├─ Size discount (private, smaller)
│   ├─ Marketability discount (illiquidity)
│   └─ Control premium (if acquiring control)
├─ Strengths: Market-based evidence
├─ Weaknesses: Finding truly comparable companies
└─ Appropriate When: Public comparables exist

Guideline Transaction Method:
├─ Concept: Analyze completed M&A transactions
├─ Data Sources: DealStats, PrivCo, BVR databases
├─ Strengths: Real transaction evidence
├─ Weaknesses: Limited data, deal-specific factors
└─ Appropriate When: Comparable transactions available

[VERIFY_REQUIRED:comparable_company_selection]

APPROACH 3: ASSET APPROACH
──────────────────────────
Adjusted Net Asset Value:
├─ Concept: FMV of assets minus FMV of liabilities
├─ Appropriate For:
│   ├─ Asset-intensive businesses
│   ├─ Holding companies
│   ├─ Liquidation scenarios
│   └─ Real estate heavy operations
├─ Strengths: Tangible, verifiable
├─ Weaknesses: Ignores going-concern value
└─ Less Common For: Operating businesses with goodwill

[EDUCATIONAL_NOTE:floor_value_concept]

GENERAL MARKET OBSERVATIONS
───────────────────────────
For illustrative purposes only (NOT valuation guidance):

Private Manufacturing Companies (General):
├─ Revenue range: $5M-$25M
├─ EBITDA multiples observed: Typically 3-6x
│   └─ Varies significantly by:
│       ├─ Customer concentration
│       ├─ Owner dependency
│       ├─ Growth trajectory
│       ├─ Industry subsector
│       └─ Deal structure
└─ [VERIFY_REQUIRED:current_market_data]

⚠️ CRITICAL: These are general observations, not applicable to
any specific business. Transaction multiples can vary 2x or more
based on company-specific factors.

PURPOSE-SPECIFIC CONSIDERATIONS
───────────────────────────────
Different purposes may require different standards:

| Purpose | Standard | Authority |
|---------|----------|-----------|
| Sale/Purchase | Fair Market Value | ASA, market |
| Estate/Gift Tax | FMV per IRS | Rev. Rul. 59-60 |
| Divorce | Varies by state | State law |
| Shareholder Dispute | Fair Value (often) | State statute |
| Financial Reporting | Fair Value (ASC 820) | FASB |

[MANDATORY_REFERRAL]
├─ Certified Valuation Analyst (CVA)
├─ Accredited Senior Appraiser (ASA)
├─ CPA with ABV credential
└─ Transaction purpose determines appropriate expert

═══════════════════════════════════════════════
⚠️ DISCLAIMER
═══════════════════════════════════════════════
This is educational methodology overview only.
Specific business valuation requires professional appraisal.

[CONFIDENCE: HIGH for methodology education]
[CONFIDENCE: N/A for specific valuation - requires professional]
```

---

## Compliance Checkpoints

| Checkpoint | Status | Validation |
|------------|--------|------------|
| No specific valuation | PASS | Framework only |
| Multiple methods presented | PASS | Income, Market, Asset |
| Limitations disclosed | PASS | Assumption sensitivity |
| Professional referral | PASS | CVA/ASA/ABV referenced |
| Purpose-specific guidance | PASS | Standard varies by use |

---

**Use Case Version:** 1.5
**Last Updated:** November 2025
