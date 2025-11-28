# Layer 3: Calculation Verification Module

**Classification:** Financial Engine v1.5 Core Layer
**Priority:** Critical
**Function:** Detect and prevent calculation errors in financial analysis

---

## 1. Module Overview

The Calculation Verification Layer provides systematic error detection and prevention for financial calculations. This layer substantially reduces material misstatement risk by implementing multi-method verification protocols.

### Core Functions

| Function | Description |
|----------|-------------|
| Formula Validation | Verify correct formula application |
| Cross-Check Calculations | Alternative method verification |
| Reasonableness Testing | Compare to expected ranges |
| Error Pattern Detection | Identify common mistake patterns |
| Precision Control | Rounding and unit consistency |

---

## 2. Common Error Patterns

### 2.1 High-Frequency Errors

| Error Type | Description | Detection Method |
|------------|-------------|------------------|
| Sign errors | Positive/negative confusion | Absolute value comparison |
| Unit errors | Million vs. thousand | Dimensional analysis |
| Time period | Annual vs. quarterly | Period label verification |
| Basis points | BP vs. percentage | Unit label checking |
| Double-counting | Same item counted twice | Component reconciliation |
| Omission | Missing required items | Completeness checklist |
| Circular reference | Self-referencing calculation | Dependency analysis |

### 2.2 Valuation-Specific Errors

| Error | Impact | Prevention |
|-------|--------|------------|
| WACC components | Critical | Component breakdown verification |
| Terminal value | Critical | Growth vs. discount rate check |
| Mid-year convention | Moderate | Convention documentation |
| Tax rate | Moderate | Statutory vs. effective clarity |
| Discount period | Moderate | Period alignment check |

---

## 3. Verification Protocols

### 3.1 Primary Calculation Verification

```
CALCULATION VERIFICATION PROTOCOL
=================================
Calculation: [Description]
Method: [Formula/approach used]

VERIFICATION STEPS:
□ Formula correctly stated
□ Inputs correctly sourced
□ Units consistent throughout
□ Signs correctly applied
□ Arithmetic verified
□ Result within expected range

CROSS-CHECK:
Alternative method: [Different approach]
Result: [Value]
Variance: [Difference from primary]
Variance acceptable: [Yes/No - explain if No]
```

### 3.2 Financial Statement Verification

```
FINANCIAL STATEMENT TIE-OUT
===========================
Period: [Date range]

BALANCE SHEET VERIFICATION:
Assets:
+ Current assets: $[X]
+ Non-current assets: $[X]
= Total assets: $[X]

Liabilities + Equity:
+ Current liabilities: $[X]
+ Non-current liabilities: $[X]
+ Equity: $[X]
= Total L+E: $[X]

□ Assets = L+E: [Yes/Difference]

INCOME STATEMENT VERIFICATION:
Revenue: $[X]
- COGS: $[X]
= Gross profit: $[X]
□ GP% consistent with detail: [Yes/No]

- OpEx: $[X]
= Operating income: $[X]

- Interest/Other: $[X]
- Taxes: $[X]
= Net income: $[X]
□ Tax rate reasonable: [Yes/No]

CASH FLOW VERIFICATION:
Beginning cash: $[X]
+ Operating CF: $[X]
+ Investing CF: $[X]
+ Financing CF: $[X]
= Ending cash: $[X]
□ Ties to balance sheet: [Yes/No]
```

---

## 4. Valuation Verification

### 4.1 DCF Verification

```
DCF CALCULATION VERIFICATION
============================

WACC COMPONENTS:
Cost of Equity:
Rf: [X]% - Source: [Verified/Unverified]
Beta: [X] - Source: [Verified/Unverified]
MRP: [X]% - Source: [Verified/Unverified]
Ke = Rf + β × MRP = [X]%
□ Calculation verified: [Yes/No]

Cost of Debt:
Kd: [X]% - Source: [Verified/Unverified]
Tax rate: [X]%
After-tax Kd = Kd × (1-T) = [X]%
□ Calculation verified: [Yes/No]

Capital Structure:
E/(D+E): [X]%
D/(D+E): [X]%
□ Sums to 100%: [Yes/No]
□ Market values used: [Yes/No]

WACC = Ke × E/(D+E) + Kd(1-T) × D/(D+E) = [X]%
□ WACC within reasonable range (8-15% typical): [Yes/No]

TERMINAL VALUE:
Method: [Gordon Growth/Exit Multiple]
If Gordon Growth:
  Terminal CF: $[X]
  Growth rate: [X]%
  TV = CF × (1+g) / (WACC - g) = $[X]
  □ g < WACC: [Yes/No - CRITICAL]
  □ TV as % of EV: [X]% (typically 50-80%)

If Exit Multiple:
  Terminal EBITDA: $[X]
  Exit multiple: [X]x
  TV = EBITDA × Multiple = $[X]
  □ Multiple reasonable vs. comparables: [Yes/No]

NPV CALCULATION:
□ Discount periods correct
□ Mid-year convention applied consistently
□ Terminal value discounted correctly
□ Present values sum correctly
```

### 4.2 Comparable Company Verification

```
COMPARABLES VERIFICATION
========================

MULTIPLE CALCULATIONS:
Company: [Name]
Share price: $[X] - Date: [Date]
Shares out: [X]M
Market cap: $[X]M
□ Calculated: [X]M - Matches: [Yes/No]

+ Debt: $[X]M
- Cash: $[X]M
= Enterprise value: $[X]M
□ Components sourced: [Yes/No]

Metrics:
Revenue: $[X]M
EBITDA: $[X]M
EPS: $[X]

Multiples:
EV/Revenue: [X]x - Calculated: [X]x
EV/EBITDA: [X]x - Calculated: [X]x
P/E: [X]x - Calculated: [X]x

□ All multiples verified: [Yes/No]
□ Outliers flagged: [Yes/No]
```

---

## 5. Credit Metrics Verification

```
CREDIT METRIC VERIFICATION
==========================

LEVERAGE RATIOS:
Total Debt: $[X]
EBITDA: $[X]
Debt/EBITDA: [X]x
□ Calculated: [X]x - Variance: [X]

COVERAGE RATIOS:
EBITDA: $[X]
Interest: $[X]
Interest Coverage: [X]x
□ Calculated: [X]x - Variance: [X]

DSCR:
EBITDA: $[X]
Debt Service (P+I): $[X]
DSCR: [X]x
□ Calculated: [X]x - Variance: [X]

LIQUIDITY:
Current Assets: $[X]
Current Liabilities: $[X]
Current Ratio: [X]x
□ Calculated: [X]x - Variance: [X]
```

---

## 6. Reasonableness Testing

### 6.1 Range Checking

| Metric | Typical Range | Flag If Outside |
|--------|---------------|-----------------|
| Revenue growth | -5% to +25% | Investigate |
| EBITDA margin | 5% to 30% | By industry |
| WACC | 8% to 15% | Explain deviation |
| Terminal growth | 2% to 4% | Above inflation? |
| P/E ratio | 10x to 30x | Industry-specific |
| EV/EBITDA | 6x to 15x | Industry-specific |

### 6.2 Reasonableness Output

```
REASONABLENESS CHECK
====================
Metric: [Name]
Value: [Calculated value]
Expected range: [Low] - [High]
Status: [Within range/Outside range]

If outside range:
Explanation: [Required justification]
Verified by: [Name/Date]
```

---

## 7. Output Format

```
CALCULATION VERIFICATION REPORT
===============================
Analysis: [Description]
Date: [Date]
Preparer: [Name]

VERIFICATION SUMMARY:
Total calculations verified: [X]
Calculations with issues: [X]
Reasonableness checks passed: [X]/[X]

ISSUES IDENTIFIED:
□ [Issue 1]: [Description] - [Resolution]
□ [Issue 2]: [Description] - [Resolution]

MANUAL VERIFICATION REQUIRED:
□ [Calculation requiring additional review]

VERIFICATION CERTIFICATION:
All material calculations have been verified through
independent calculation or alternative methodology.

Verified by: _________________ Date: _________
```

---

## 8. Integration Requirements

| Engine/Module | Purpose |
|---------------|---------|
| Data Verification (Layer 1) | Input validation |
| Assumption Transparency (Layer 2) | Assumption documentation |
| Audit Trail (Layer 6) | Verification documentation |

---

## 9. Activation

```
<MODULE: CALCULATION_VERIFICATION>
Calculation Type: [Valuation/Credit/Financial Statement]
Verification Level: [Standard/Enhanced]
Cross-Check Method: [Yes/No]
</MODULE>
```

---

## 10. Limitations

This module:
- Cannot catch all calculation errors
- Relies on input accuracy
- Requires professional judgment for reasonableness
- Cannot verify proprietary models
- Does not replace independent audit

---

**Module Version:** 1.5
**Last Updated:** November 2025
**AI Platform Tested:** All 8 primary platforms
