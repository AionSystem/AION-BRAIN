# Use Case 008: Commercial Credit Analysis Framework

**Engine:** Financial Engine v1.5
**Domain:** Credit Risk Assessment
**Complexity:** High
**Risk Level:** HIGH (lending decision implications)

---

## Scenario Description

A commercial lender needs to analyze creditworthiness of a business loan applicant using the Five C's framework and ratio analysis without making the lending decision (which requires underwriter judgment and policy compliance).

---

## CEREBRO Pattern Amplification Applied

### Shannon Framework (Information Integration)
```
[SHANNON ANALYSIS]:
├─ Information Density: VERY HIGH
├─ Sources: Financial statements, credit reports, collateral appraisals
├─ Redundancy: Cross-validate ratios across sources
├─ Signal: Payment history patterns, cash flow trends
└─ Noise: One-time adjustments, non-recurring items
```

### Curie Framework (Risk Anomalies)
```
[CURIE ANALYSIS]:
├─ Baseline: Industry benchmark ratios
├─ Deviations to Investigate:
│   ├─ Debt service coverage declining trend
│   ├─ Working capital volatility
│   ├─ Revenue concentration risk
│   └─ Owner withdrawal patterns
└─ Hypothesis: Generate for underwriter review
```

---

## Input/Output Example

### Engine Response
```
COMMERCIAL CREDIT ANALYSIS FRAMEWORK
====================================

[ANALYTICAL FRAMEWORK - Underwriter Decision Required]

THE FIVE C's OF CREDIT
──────────────────────

1. CHARACTER (Payment Willingness)
├─ Indicators:
│   ├─ Personal credit history of guarantors
│   ├─ Trade payment history (D&B, Experian)
│   ├─ Previous loan performance
│   ├─ Business tenure and stability
│   └─ Reference checks
├─ Red Flags:
│   ├─ Recent bankruptcies (personal or business)
│   ├─ Judgments or liens
│   ├─ Deteriorating payment patterns
│   └─ Evasive information requests
└─ [VERIFY_REQUIRED:credit_bureau_verification]

2. CAPACITY (Payment Ability)
├─ Key Ratios:
│   ├─ Debt Service Coverage Ratio (DSCR)
│   │   └─ Formula: (Net Income + Depreciation + Interest) / Debt Service
│   │   └─ Minimum: Typically 1.20x+ (policy dependent)
│   ├─ Fixed Charge Coverage Ratio
│   ├─ Cash Flow to Current Maturities
│   └─ Operating Cash Flow trends
├─ Pro Forma Analysis:
│   ├─ Post-loan debt service capability
│   ├─ Stress testing (revenue decline scenarios)
│   └─ Seasonal cash flow considerations
└─ [VERIFY_REQUIRED:financial_statement_verification]

3. CAPITAL (Owner Investment)
├─ Equity Indicators:
│   ├─ Tangible Net Worth
│   ├─ Debt-to-Equity ratio
│   ├─ Owner injection history
│   └─ Retained earnings trend
├─ Minimum Equity:
│   ├─ Policy dependent (often 20-30% minimum)
│   ├─ Higher for riskier industries
│   └─ SBA: 10-20% for guaranteed loans
└─ [VERIFY_REQUIRED:balance_sheet_analysis]

4. COLLATERAL (Secondary Repayment)
├─ Types:
│   ├─ Real estate (appraised value)
│   ├─ Equipment (orderly liquidation value)
│   ├─ Accounts receivable (aged analysis)
│   ├─ Inventory (by type: raw, WIP, finished)
│   └─ Personal guarantees
├─ Advance Rates (Typical Ranges):
│   ├─ Real estate: 75-80% of appraised value
│   ├─ Equipment: 50-80% of OLV
│   ├─ A/R (<90 days): 70-85%
│   ├─ Inventory: 30-50%
│   └─ [VERIFY_REQUIRED:policy_advance_rates]
├─ Collateral Margin:
│   └─ Loan / Collateral Value = LTV
└─ [VERIFY_REQUIRED:collateral_appraisal]

5. CONDITIONS (External Factors)
├─ Macro Factors:
│   ├─ Industry outlook
│   ├─ Economic cycle position
│   ├─ Interest rate environment
│   └─ Regulatory changes
├─ Micro Factors:
│   ├─ Competitive position
│   ├─ Customer concentration
│   ├─ Supplier dependence
│   └─ Technology disruption risk
└─ [VERIFY_REQUIRED:industry_analysis]

KEY RATIO ANALYSIS
──────────────────

Liquidity Ratios:
├─ Current Ratio: Current Assets / Current Liabilities
│   └─ Benchmark: Generally 1.5-2.0x healthy
├─ Quick Ratio: (CA - Inventory) / CL
│   └─ Benchmark: Generally 1.0x+ healthy
└─ Working Capital: CA - CL

Leverage Ratios:
├─ Debt-to-Equity: Total Debt / Equity
│   └─ Industry-specific benchmarks apply
├─ Debt-to-Assets: Total Debt / Total Assets
└─ Interest Coverage: EBIT / Interest Expense

Profitability Ratios:
├─ Gross Margin: (Revenue - COGS) / Revenue
├─ Operating Margin: Operating Income / Revenue
├─ Net Margin: Net Income / Revenue
└─ Return on Assets: Net Income / Total Assets

Activity Ratios:
├─ Days Sales Outstanding (DSO)
├─ Days Inventory Outstanding (DIO)
├─ Days Payables Outstanding (DPO)
└─ Cash Conversion Cycle: DSO + DIO - DPO

[ANALYTICAL_NOTE]
Ratios must be compared to:
├─ Industry benchmarks (RMA, industry studies)
├─ Historical trends (3-5 years)
├─ Peer companies
└─ Post-loan projections

═══════════════════════════════════════════════
⚠️ UNDERWRITING DISCLAIMER
═══════════════════════════════════════════════

This framework provides analytical structure only.

Lending decisions require:
├─ Underwriter judgment
├─ Policy compliance review
├─ Committee approval (if applicable)
├─ Regulatory compliance verification
└─ Complete documentation

[CONFIDENCE: HIGH for framework accuracy]
[CONFIDENCE: N/A for lending decision - human required]
```

---

**Use Case Version:** 1.5
**Last Updated:** November 2025
