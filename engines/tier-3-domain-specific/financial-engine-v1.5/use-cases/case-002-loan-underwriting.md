# Case 002: Commercial Loan Underwriting

**Category:** Credit Analysis
**Complexity:** High
**Modules Activated:** Data Verification, Credit Analyzer, Fraud Detection

---

## Scenario

A commercial bank is evaluating a $5M term loan request from a mid-size manufacturing company seeking to finance equipment expansion. The credit analyst uses Financial Validation Engine to support the underwriting process, ensuring thorough analysis and proper documentation.

---

## Initial Request (Problematic)

```
"Analyze this company for a $5M loan. Can they pay it back?"
```

**Risk Assessment:** HIGH
- Insufficient financial context
- No loan structure specified
- Repayment analysis framework unclear
- Cash flow projections undocumented

---

## Engine-Processed Request

```
<FINANCIAL_ENGINE_v1.0>
<MODE: FULL_VALIDATION>
<MODULE: DATA_VERIFICATION>
<MODULE: CREDIT_ANALYZER>
<MODULE: FRAUD_DETECTION>

CONTEXT:
- Borrower: Midwest Manufacturing Inc.
- Industry: Industrial equipment manufacturing
- Loan Request: $5M term loan, 7-year amortization
- Purpose: Equipment expansion
- Collateral: New equipment + existing machinery

FINANCIAL DATA:
- Revenue (LTM): $28M
- EBITDA (LTM): $3.2M (11.4% margin)
- Total Debt (Current): $4.5M
- Cash: $1.2M
- Net Worth: $8.5M
- Years in Business: 15

ANALYSIS REQUESTED:
1. Credit metrics assessment
2. Cash flow adequacy for debt service
3. Collateral coverage analysis
4. Risk rating recommendation
5. Loan structure recommendations
</FINANCIAL_ENGINE_v1.0>
```

---

## Engine Output

### Data Verification Report

```
DATA SOURCE VERIFICATION
========================
Analysis: Midwest Manufacturing Commercial Loan
Date: November 2025

SOURCE SUMMARY:
Total Data Points: 32
Verified: 28 (88%)
Pending: 4 (12%)

VERIFIED SOURCES:
□ Tax returns: 3 years (CPA prepared) - VERIFIED
□ Audited financials: 2 years - VERIFIED
□ Interim financials: YTD 10 months - MANAGEMENT PREPARED
□ A/R aging: Current - REQUIRES VERIFICATION
□ Equipment appraisal: Third-party - VERIFIED

⚠️ ITEMS REQUIRING VERIFICATION:
□ Interim financials: Not reviewed by CPA
□ Inventory valuation: Management estimate
□ Customer concentration: Verify against invoices
□ Related party transactions: Further inquiry needed
```

### Credit Analysis

```
CREDIT METRICS ASSESSMENT
=========================

LEVERAGE ANALYSIS:
Current Debt: $4.5M
Proposed Debt: $5.0M
Pro Forma Debt: $9.5M

                    | Current | Pro Forma | Guideline |
|--------------------|---------|-----------|-----------|
| Debt/EBITDA       | 1.4x    | 3.0x      | <3.5x     | ✓
| Debt/Net Worth    | 0.53x   | 1.12x     | <1.5x     | ✓
| Senior Debt/EBITDA| 1.4x    | 3.0x      | <3.0x     | ⚠️

Leverage Assessment: ACCEPTABLE (at upper end of guidelines)

COVERAGE ANALYSIS:
EBITDA: $3.2M
Interest Expense (Pro Forma): $0.7M
Debt Service (P+I, Year 1): $1.1M

                    | Current | Pro Forma | Guideline |
|--------------------|---------|-----------|-----------|
| Interest Coverage | 8.0x    | 4.6x      | >2.5x     | ✓
| DSCR (P+I)       | N/A     | 2.9x      | >1.25x    | ✓
| Fixed Charge     | 3.2x    | 1.8x      | >1.20x    | ✓

Coverage Assessment: STRONG (comfortable margin)

LIQUIDITY ANALYSIS:
Current Ratio: 1.8x (Acceptable)
Quick Ratio: 0.9x (Adequate for manufacturing)
Working Capital: $2.1M
Days Cash on Hand: 15 days

Liquidity Assessment: ADEQUATE

PROFITABILITY ANALYSIS:
Gross Margin: 32% (Industry avg: 28%)
EBITDA Margin: 11.4% (Industry avg: 10%)
Net Margin: 4.2%
ROE: 14%

Profitability Assessment: ABOVE AVERAGE
```

### Cash Flow Analysis

```
CASH FLOW ADEQUACY ANALYSIS
===========================

HISTORICAL CASH FLOW:
| Item | Year -2 | Year -1 | LTM |
|------|---------|---------|-----|
| EBITDA | $2.6M | $2.9M | $3.2M |
| CapEx | ($0.8M) | ($1.0M) | ($1.2M) |
| Working Capital | ($0.3M) | ($0.4M) | ($0.2M) |
| Free Cash Flow | $1.5M | $1.5M | $1.8M |

PROJECTED CASH FLOW (POST-LOAN):
| Item | Year 1 | Year 2 | Year 3 |
|------|--------|--------|--------|
| EBITDA | $3.5M | $3.8M | $4.1M |
| CapEx | ($0.8M) | ($0.8M) | ($0.9M) |
| Working Capital | ($0.3M) | ($0.3M) | ($0.2M) |
| Debt Service | ($1.1M) | ($1.1M) | ($1.1M) |
| Net Cash Flow | $1.3M | $1.6M | $1.9M |

⚠️ ASSUMPTIONS:
- Revenue growth: 8% annually (management projection)
- EBITDA margin stable at 11.4%
- Maintenance CapEx normalized
- Working capital 7.5% of revenue increase

SENSITIVITY ANALYSIS:
| Scenario | DSCR | Net Cash Flow |
|----------|------|---------------|
| Base Case | 2.9x | $1.3M |
| Revenue -10% | 2.3x | $0.9M |
| Revenue -20% | 1.7x | $0.5M |
| EBITDA Margin -2% | 2.3x | $0.8M |
| Combined Stress | 1.4x | $0.2M |

Cash Flow Assessment: ADEQUATE with cushion
Stress Testing: Survives moderate stress scenarios
```

### Collateral Analysis

```
COLLATERAL COVERAGE ANALYSIS
============================

PROPOSED COLLATERAL:
| Asset | Appraised Value | Advance Rate | Loan Value |
|-------|-----------------|--------------|------------|
| New Equipment | $5.0M | 80% | $4.0M |
| Existing Equipment | $3.5M | 60% | $2.1M |
| Inventory | $4.2M | 50% | $2.1M |
| Receivables | $3.8M | 80% | $3.0M |
| Total | $16.5M | — | $11.2M |

COVERAGE CALCULATION:
Loan Amount: $5.0M
Total Collateral (Loan Value): $11.2M
Coverage Ratio: 2.24x

Collateral Assessment: STRONG COVERAGE

COLLATERAL QUALITY:
□ Equipment appraisal: Third-party, current - VERIFIED
□ Inventory: Saleable, not obsolete - VERIFY WITH SITE VISIT
□ Receivables: <90 days, diversified - VERIFY AGING
□ UCC filing: Clear search required

⚠️ COLLATERAL RISKS:
- Equipment specialized (limited secondary market)
- Inventory subject to obsolescence
- Key customer concentration in A/R (verify)
```

### Fraud Detection Screening

```
FRAUD INDICATOR SCAN
====================
Indicators Checked: 24
Red Flags Identified: 2

BENFORD'S LAW ANALYSIS:
Sales invoices: Conforms to expected distribution
Expense reports: Conforms to expected distribution
Journal entries: Minor anomaly in digit 5 (investigate)

FINANCIAL STATEMENT ANALYSIS:
□ Revenue vs. receivables growth: Aligned
□ Inventory growth vs. COGS: Aligned
□ Unusual margin improvements: None
□ Quarter-end spikes: Not observed

⚠️ ITEMS REQUIRING FOLLOW-UP:
1. Related party transactions noted in footnotes
   - Sales to company owned by CEO's brother
   - Amount: $1.2M annually (4% of revenue)
   - Recommendation: Verify arms-length pricing

2. Journal entry pattern
   - Higher frequency of entries ending in 5
   - Likely rounding practice, not fraud indicator
   - Recommendation: Discuss with CFO

FRAUD RISK ASSESSMENT: LOW (normal manufacturing indicators)
```

### Credit Recommendation

```
CREDIT RECOMMENDATION
=====================

RISK RATING: 4 (Acceptable Risk)
Rating Scale: 1 (Excellent) to 10 (Loss)

RECOMMENDATION: APPROVE WITH CONDITIONS

LOAN STRUCTURE:
| Element | Recommendation |
|---------|----------------|
| Amount | $5,000,000 |
| Term | 7 years |
| Amortization | 7 years, level P+I |
| Rate | Prime + 2.00% (currently 9.50%) |
| Fee | 1.00% ($50,000) |
| Collateral | New equipment (1st lien), blanket UCC |

COVENANTS:
Financial Covenants:
□ Minimum DSCR: 1.25x (tested quarterly)
□ Maximum Debt/Net Worth: 1.5x (tested quarterly)
□ Minimum Net Worth: $7.5M (tested quarterly)

Reporting Covenants:
□ Annual audited financials within 120 days
□ Quarterly management financials within 45 days
□ Annual borrowing base certificate
□ Prompt notice of material events

Negative Covenants:
□ No additional debt without consent
□ No dividends exceeding 50% of net income
□ No change of control without consent
□ No disposal of collateral without consent

CONDITIONS PRECEDENT:
□ Updated equipment appraisal
□ UCC search and filing
□ Insurance certificates (lender as loss payee)
□ Personal guaranty from principal owners (>20%)
□ Verification of related party transaction pricing
□ Site visit completion

RISK MITIGANTS:
+ Strong historical cash flow
+ Established business (15 years)
+ Experienced management team
+ Strong collateral coverage
+ Industry expertise in market

RISK FACTORS:
- Leverage at upper end of guidelines
- Customer concentration (verify)
- Related party transactions (verify pricing)
- Equipment has limited secondary market
```

---

## Verification Checklist

```
UNDERWRITING VERIFICATION REQUIRED
===================================
□ Complete site visit and management interview
□ Verify customer concentration against invoices
□ Confirm related party transaction pricing
□ Order updated equipment appraisal
□ Complete UCC search
□ Verify insurance coverage
□ Obtain personal financial statements from guarantors
□ Review industry outlook and company positioning
□ Complete OFAC/BSA screening
□ Obtain loan committee approval

⚠️ APPROVAL AUTHORITY:
This loan requires Senior Credit Officer approval based on:
- Loan amount ($5M exceeds branch authority)
- Leverage at upper guidelines
```

---

## Key Lessons

1. **Comprehensive metrics** — Leverage, coverage, liquidity all assessed
2. **Cash flow focus** — Debt service coverage is primary determinant
3. **Stress testing** — Understand downside scenarios
4. **Collateral as backup** — Not primary repayment source
5. **Fraud screening** — Standard even for established companies

---

*This use case demonstrates commercial loan underwriting workflow. All credit decisions require appropriate approval authority.*
