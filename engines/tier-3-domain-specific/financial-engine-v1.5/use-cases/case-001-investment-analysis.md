# Case 001: Investment Analysis Due Diligence

**Category:** Investment Analysis
**Complexity:** High
**Modules Activated:** Data Verification, Assumption Transparency, Valuation Validator

---

## Scenario

A private equity fund is evaluating a potential acquisition of a mid-market software company. The investment team needs to validate the company's financial performance, assess the quality of earnings, and develop a valuation range for bid pricing. The transaction value is approximately $200M.

---

## Initial Request (Problematic)

```
"Analyze this company for acquisition. What's it worth?"
```

**Risk Assessment:** HIGH
- No financial data context provided
- Valuation without methodology specification
- Quality of earnings not addressed
- Key assumptions undocumented

---

## Engine-Processed Request

```
<FINANCIAL_ENGINE_v1.0>
<MODE: DUE_DILIGENCE>
<MODULE: DATA_VERIFICATION>
<MODULE: ASSUMPTION_TRANSPARENCY>
<MODULE: VALUATION_VALIDATOR>

CONTEXT:
- Target: CloudSoft Inc. (B2B SaaS)
- Transaction: Control acquisition (100%)
- Enterprise Value Range: $180-220M
- Investment Thesis: Platform for add-on acquisitions

FINANCIAL DATA PROVIDED:
- Revenue (LTM): $45M
- EBITDA (LTM): $8M (17.8% margin)
- Revenue Growth (3-yr CAGR): 25%
- Net Revenue Retention: 115%
- Gross Margin: 75%

ANALYSIS REQUESTED:
1. Validate financial data quality
2. Assess quality of earnings
3. Develop DCF and multiples valuation
4. Identify key risks and sensitivities
5. Recommend bid range
</FINANCIAL_ENGINE_v1.0>
```

---

## Engine Output

### Data Verification Report

```
DATA SOURCE VERIFICATION
========================
Analysis: CloudSoft Inc. Acquisition Due Diligence
Date: November 2025

SOURCE SUMMARY:
Total Data Points Analyzed: 47
Fully Sourced: 38 (81%)
Pending Verification: 9 (19%)
Stale Data: 0

⚠️ VERIFICATION REQUIRED:

Financial Statements:
□ Audited financials: Last 3 years available - VERIFIED
□ LTM financials: Management prepared - REQUIRES CPA REVIEW
□ Revenue detail: By customer/product - REQUIRES AGING ANALYSIS

Key Metrics:
□ Net Revenue Retention: Management calculation - RECALCULATE INDEPENDENTLY
□ Customer count: Management representation - VERIFY AGAINST CONTRACTS
□ ARR: Defined differently than industry standard - NORMALIZE

THIRD-PARTY VERIFICATION NEEDED:
□ Top 10 customer contracts (60% of revenue)
□ Deferred revenue schedule
□ Customer churn data by cohort
```

### Quality of Earnings Analysis

```
QUALITY OF EARNINGS ASSESSMENT
==============================

REPORTED VS. ADJUSTED EBITDA:

Reported EBITDA (LTM): $8.0M

ADJUSTMENTS:
+ Stock-based compensation: $1.2M (Add back)
+ Non-recurring legal fees: $0.3M (Add back)
+ One-time implementation costs: $0.5M (Add back)
- Owner compensation normalization: ($0.4M) (Deduct)
- Related party rent adjustment: ($0.1M) (Deduct)
- Revenue timing adjustment: ($0.8M) (Deduct - see below)

ADJUSTED EBITDA: $8.7M

⚠️ QUALITY OF EARNINGS CONCERNS:

REVENUE TIMING (HIGH CONCERN):
Q4 revenue as % of annual: 35%
Industry average: 27%
Analysis: Potential channel stuffing or aggressive recognition
Impact: ($0.8M) revenue may not be sustainable

CUSTOMER CONCENTRATION:
Top customer: 18% of revenue
Top 5 customers: 42% of revenue
Churn risk on top customer: ELEVATED (contract renewal in 6 months)

DEFERRED REVENUE TREND:
Current period: $12M
Prior period: $9M
Growth: 33% (HEALTHY - indicates forward bookings)

ADJUSTED EBITDA MARGIN: 19.3% (vs. reported 17.8%)
```

### Valuation Analysis

```
VALUATION ANALYSIS
==================

METHODOLOGY 1: DISCOUNTED CASH FLOW

Key Assumptions:
| Assumption | Value | Sensitivity | Basis |
|------------|-------|-------------|-------|
| Revenue growth (Yr 1-3) | 22% | HIGH | Guided down from 25% historical |
| Revenue growth (Yr 4-5) | 15% | MEDIUM | Industry maturity pattern |
| Terminal growth | 3% | HIGH | GDP + inflation |
| EBITDA margin (terminal) | 25% | MEDIUM | SaaS industry benchmark |
| WACC | 12% | HIGH | PE required return |
| Exit multiple | 10x EBITDA | HIGH | Current market conditions |

DCF OUTPUT:
Enterprise Value Range: $165M - $220M
Base Case: $190M
Implied LTM EBITDA Multiple: 21.8x (on adjusted EBITDA)

METHODOLOGY 2: COMPARABLE COMPANIES

Comparable Set:
| Company | EV/Revenue | EV/EBITDA | Growth |
|---------|------------|-----------|--------|
| Peer 1 | 5.5x | 22x | 20% |
| Peer 2 | 4.8x | 18x | 18% |
| Peer 3 | 6.2x | 25x | 28% |
| Peer 4 | 4.5x | 16x | 15% |
| Median | 5.2x | 20x | 19% |

Applied to CloudSoft:
EV/Revenue: 4.5x-5.5x × $45M = $202M-$248M
EV/EBITDA: 18x-22x × $8.7M = $157M-$191M

METHODOLOGY 3: PRECEDENT TRANSACTIONS

Recent B2B SaaS Transactions (2024-2025):
| Transaction | EV/Revenue | EV/EBITDA | Growth |
|-------------|------------|-----------|--------|
| Deal 1 | 5.0x | 20x | 22% |
| Deal 2 | 4.2x | 17x | 18% |
| Deal 3 | 5.8x | 24x | 30% |
| Median | 5.0x | 20x | 22% |

Applied to CloudSoft:
Implied EV: $175M-$225M

VALUATION SUMMARY:
| Methodology | Low | Mid | High |
|-------------|-----|-----|------|
| DCF | $165M | $190M | $220M |
| Comparables | $157M | $195M | $248M |
| Precedents | $175M | $200M | $225M |
| WEIGHTED | $165M | $195M | $230M |
```

### Sensitivity Analysis

```
SENSITIVITY ANALYSIS
====================

DCF SENSITIVITY TO KEY ASSUMPTIONS:

WACC vs. Terminal Growth:
|           | 2% TG | 3% TG | 4% TG |
|-----------|-------|-------|-------|
| 10% WACC | $225M | $250M | $285M |
| 12% WACC | $180M | $195M | $215M |
| 14% WACC | $150M | $160M | $175M |

Revenue Growth vs. EBITDA Margin:
|              | 23% Margin | 25% Margin | 27% Margin |
|--------------|------------|------------|------------|
| 18% Growth | $165M | $180M | $195M |
| 22% Growth | $180M | $195M | $210M |
| 26% Growth | $200M | $220M | $240M |

⚠️ HIGH-IMPACT ASSUMPTIONS:
1. WACC: ±2% = ±$30M valuation impact
2. Terminal growth: ±1% = ±$25M valuation impact
3. Revenue growth (Y1-3): ±4% = ±$20M valuation impact
```

### Risk Assessment

```
KEY RISKS IDENTIFIED
====================

HIGH RISK:
□ Customer concentration - Top customer renewal in 6 months
  Mitigation: Negotiate contract extension pre-close
  Impact if lost: ~$8M revenue, ~$2M EBITDA

□ Revenue timing concerns - Q4 concentration above peers
  Mitigation: Detailed monthly revenue analysis
  Impact: Potential $2-3M revenue adjustment

□ Key person risk - CEO/CTO own 60% of equity
  Mitigation: Rollover equity and employment agreements
  Impact: Technology and customer relationships at risk

MEDIUM RISK:
□ Competitive dynamics - Two well-funded competitors
  Mitigation: Assess switching costs and NRR stability
  
□ Integration complexity - 3 prior acquisitions not fully integrated
  Mitigation: Integration plan and budget pre-close

□ Technology stack - Some legacy code, technical debt
  Mitigation: Technology due diligence, development roadmap
```

### Bid Recommendation

```
BID RECOMMENDATION
==================

Based on the analysis above:

VALUATION CONCLUSION:
- Fair value range: $180M - $210M
- Implied multiples: 4.0x-4.7x revenue, 20x-24x adjusted EBITDA

BID STRATEGY:
- Initial bid: $175M (3.9x revenue)
- Target price: $195M (4.3x revenue)
- Walk-away: $215M (4.8x revenue)

PRICE ADJUSTMENTS:
+ Premium if: Customer contract secured, earn-out accepted
- Discount if: Q4 revenue concerns confirmed, key person issues

DEAL STRUCTURE RECOMMENDATIONS:
□ 80% cash at close
□ 10% rollover equity (management alignment)
□ 10% earn-out tied to 2-year revenue targets

⚠️ CONDITIONS PRECEDENT:
□ Completion of customer contract review
□ Technology due diligence satisfactory
□ Key employee agreements executed
□ Quality of earnings confirmed by CPA
```

---

## Verification Checklist

```
PROFESSIONAL VERIFICATION REQUIRED
==================================
□ Engage third-party accounting firm for QoE
□ Complete customer reference calls (top 10)
□ Technology assessment by CTO/advisors
□ Legal due diligence on contracts and IP
□ Verify all management representations
□ Confirm WACC calculation with investment committee
□ Market check on comparable transaction multiples

⚠️ INVESTMENT COMMITTEE APPROVAL REQUIRED:
Final bid price and deal terms must be approved before submission.
```

---

## Key Lessons

1. **Quality of earnings analysis is essential** — Reported EBITDA rarely equals adjusted
2. **Revenue quality matters** — Timing, concentration, and retention are key
3. **Sensitivity analysis reveals value drivers** — WACC and growth dominate
4. **Risk quantification supports negotiation** — Price adjustments for specific risks
5. **Professional verification is mandatory** — Engine output requires expert confirmation

---

*This use case demonstrates investment analysis workflow. Actual transactions require professional due diligence and investment committee approval.*
