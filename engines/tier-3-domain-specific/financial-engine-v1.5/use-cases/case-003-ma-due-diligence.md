# Case 003: M&A Financial Due Diligence

**Category:** Transaction Due Diligence
**Complexity:** Very High
**Modules Activated:** Data Verification, Fraud Detection, Assumption Transparency, Valuation Validator

---

## Scenario

A private equity firm is conducting financial due diligence on a potential $50M acquisition of a specialty manufacturing company. The target has shown strong revenue growth but some unusual working capital patterns. The due diligence team uses Financial Validation Engine to structure the review and identify potential issues.

---

## Initial Request (Problematic)

```
"Analyze this target company for our acquisition."
```

**Risk Assessment:** VERY HIGH
- No specific focus areas identified
- Quality of earnings not specified
- Working capital concerns not addressed
- No scope definition for due diligence

---

## Engine-Processed Request

```
<FINANCIAL_ENGINE_v1.0>
<MODE: DUE_DILIGENCE>
<MODULE: DATA_VERIFICATION>
<MODULE: FRAUD_DETECTION>
<MODULE: ASSUMPTION_TRANSPARENCY>
<MODULE: VALUATION_VALIDATOR>

CONTEXT:
- Target: Precision Components Inc.
- Industry: Specialty manufacturing (aerospace/defense)
- Transaction Value: ~$50M
- Structure: Asset purchase
- Buyer: PE firm (add-on to existing platform)

FINANCIAL DATA:
- Revenue (TTM): $32M (15% YoY growth)
- EBITDA (TTM): $6.2M (19.4% margin)
- Gross Margin: 35%
- Working Capital: $8.5M (26.5% of revenue)
- CapEx (Annual): $1.5M
- Owner's salary: $400K

CONCERNS FLAGGED:
- Working capital has increased from 18% to 26.5% of revenue
- Inventory build-up over past 18 months
- Top 3 customers = 65% of revenue

ANALYSIS REQUESTED:
1. Quality of earnings analysis
2. Working capital deep dive
3. Customer concentration assessment
4. Fraud indicator screening
5. Synergy validation (with platform company)
</FINANCIAL_ENGINE_v1.0>
```

---

## Engine Output

### Data Verification Report

```
DATA SOURCE VERIFICATION
========================
Due Diligence: Precision Components Inc.
Date: November 2025

SOURCE SUMMARY:
Total data requests: 127 items
Received: 98 (77%)
Outstanding: 29 (23%)
Quality issues: 14

SOURCE QUALITY ASSESSMENT:
□ Audited financials: 3 years - CPA reviewed - ADEQUATE
□ Management financials: Monthly for 2 years - ADEQUATE
□ Tax returns: 3 years - RECONCILES
□ Customer contracts: 8 of 12 received - INCOMPLETE
□ Vendor agreements: 5 of 15 received - INCOMPLETE
□ Inventory detail: Age and composition - RECEIVED
□ Fixed asset register: With depreciation - RECEIVED
□ A/R aging: By customer - RECEIVED
□ A/P aging: By vendor - RECEIVED

⚠️ CRITICAL GAPS:
1. Customer contracts for top 3 customers - MUST OBTAIN
2. Backlog detail and aging - REQUESTED
3. Quality certifications (AS9100) - VERIFY STATUS
4. Environmental reports - REQUESTED (manufacturing facility)

⚠️ DATA QUALITY ISSUES:
1. Inventory valuation method changed Y-2
2. Revenue recognition timing unclear for project work
3. Related party transaction disclosure incomplete
4. Capitalization policy not documented
```

### Quality of Earnings Analysis

```
QUALITY OF EARNINGS ASSESSMENT
==============================

REPORTED VS. ADJUSTED EBITDA:

Reported EBITDA (TTM): $6.2M

NORMALIZATION ADJUSTMENTS:
Category | Add/(Deduct) | Description
---------|--------------|-------------
Owner comp normalization | +$150K | Salary above market
One-time legal settlement | +$200K | Non-recurring
COVID catch-up orders | -$400K | Non-sustainable revenue
Deferred maintenance | -$100K | Catch-up required
Related party rent | -$50K | Below market
Inventory reserve | -$250K | Obsolescence not reserved
Revenue timing | -$300K | Project revenue pulled forward

ADJUSTED EBITDA: $5.45M

ADJUSTMENT ANALYSIS:
Total adjustments: ($750K)
Adjustment rate: 12.1% of reported EBITDA
⚠️ HIGH ADJUSTMENT RATE - Requires verification

QUALITY OF EARNINGS CONCLUSION:
□ Reported EBITDA overstated by ~12%
□ Revenue timing issue is significant concern
□ Working capital efficiency declining
□ Inventory risk not properly reserved

NORMALIZED EBITDA MARGIN: 17.0% (vs. reported 19.4%)
```

### Working Capital Analysis

```
WORKING CAPITAL DEEP DIVE
=========================

WORKING CAPITAL TREND:
| Period | Revenue | NWC | NWC % |
|--------|---------|-----|-------|
| Y-3 | $24M | $4.3M | 17.9% |
| Y-2 | $26M | $5.2M | 20.0% |
| Y-1 | $28M | $6.8M | 24.3% |
| TTM | $32M | $8.5M | 26.5% |

⚠️ CONCERNING TREND: NWC % increasing each year

COMPONENT ANALYSIS:

ACCOUNTS RECEIVABLE:
| Period | A/R | DSO |
|--------|-----|-----|
| Y-3 | $3.2M | 49 days |
| Y-2 | $3.8M | 53 days |
| Y-1 | $4.5M | 59 days |
| TTM | $5.8M | 66 days |

⚠️ DSO increasing 17 days over 3 years
Root cause: Customer payment terms extended for top accounts
Risk: Collection issues or relationship-driven concessions

INVENTORY:
| Period | Inventory | DIO |
|--------|-----------|-----|
| Y-3 | $3.8M | 98 days |
| Y-2 | $5.1M | 128 days |
| Y-1 | $6.2M | 144 days |
| TTM | $7.5M | 152 days |

⚠️ CRITICAL: Inventory increased 97% while revenue grew 33%
Potential issues:
□ Obsolete inventory not written off
□ Overbuild for anticipated orders that didn't materialize
□ Strategic inventory build (raw materials)
□ Cash trapped in excess inventory

INVENTORY AGE ANALYSIS:
| Age | Amount | % |
|-----|--------|---|
| 0-90 days | $4.2M | 56% |
| 91-180 days | $1.8M | 24% |
| 181-365 days | $1.0M | 13% |
| >365 days | $0.5M | 7% |

⚠️ 20% of inventory >180 days old
Reserve requirement: $500K (vs. $250K currently reserved)

ACCOUNTS PAYABLE:
| Period | A/P | DPO |
|--------|-----|-----|
| Y-3 | $2.7M | 69 days |
| Y-2 | $3.2M | 80 days |
| Y-1 | $3.6M | 84 days |
| TTM | $4.1M | 83 days |

DPO stable - taking full advantage of vendor terms

WORKING CAPITAL NORMALIZATION:
Target NWC %: 20% (Y-2 level, reasonable for industry)
Current NWC: $8.5M (26.5%)
Normalized NWC: $6.4M (20%)
Excess WC trapped: $2.1M

⚠️ WORKING CAPITAL ADJUSTMENT:
Recommend purchase price adjustment of $1-2M for excess inventory
and/or normalized working capital peg of 20%.
```

### Customer Concentration Analysis

```
CUSTOMER CONCENTRATION ASSESSMENT
=================================

CUSTOMER REVENUE BREAKDOWN:
| Customer | Revenue | % | Contract Term |
|----------|---------|---|---------------|
| Aerospace Prime A | $10.4M | 32.5% | LTA through 2027 |
| Defense Prime B | $6.4M | 20.0% | PO-based |
| Aerospace OEM C | $4.0M | 12.5% | LTA through 2026 |
| Top 3 Total | $20.8M | 65.0% | |
| Next 5 | $7.0M | 21.9% | |
| Other (30+) | $4.2M | 13.1% | |

⚠️ HIGH CONCENTRATION: 65% in top 3 customers

CONCENTRATION RISK ANALYSIS:

Customer A (32.5% of revenue):
□ Long-term agreement in place - POSITIVE
□ Relationship: 12 years - POSITIVE
□ Spend trend: Growing - POSITIVE
□ Contract review: PENDING (critical gap)
⚠️ RISK: Single point of failure, limited negotiating power

Customer B (20% of revenue):
□ No long-term agreement - NEGATIVE
□ Relationship: 6 years - MODERATE
□ Spend trend: Flat - NEUTRAL
□ Alternative suppliers: Yes - NEGATIVE
⚠️ RISK: Could move business without penalty

Customer C (12.5% of revenue):
□ LTA in place - POSITIVE
□ Relationship: 8 years - POSITIVE
□ Spend trend: Declining - NEGATIVE
□ Contract expires: 2026 - MONITOR

CUSTOMER REFERENCE CALLS REQUIRED:
□ Customer A: Relationship satisfaction, growth plans
□ Customer B: Supplier evaluation process, competitive position
□ Customer C: Reason for declining spend

BACKLOG ANALYSIS:
Total backlog: $18M
Backlog by customer:
- Customer A: $8M (44%)
- Customer B: $4M (22%)
- Customer C: $2M (11%)
- Other: $4M (22%)

Backlog coverage: 6.8 months (adequate for industry)
```

### Fraud Detection Screening

```
FRAUD INDICATOR SCAN
====================
Due Diligence: Precision Components Inc.
Indicators Checked: 32
Red Flags: 4

BENFORD'S LAW ANALYSIS:
Sales invoices (12 months): CONFORMS
Expense entries: CONFORMS
Journal entries: Minor anomaly digit 8 (investigate)
Inventory transactions: ANOMALY in digit 1

⚠️ INVENTORY BENFORD ANOMALY:
First digit distribution shows excess of 1s and deficit of 2s
Possible explanations:
- Inventory write-ups (investigate)
- Systemic pricing pattern (verify)
- Data entry patterns (investigate)

RELATED PARTY TRANSACTIONS:
□ Building lease: Owner-related entity
  Terms: $15K/month ($180K annually)
  Market: $12K/month estimated
  ⚠️ Above market - adjust EBITDA by $36K

□ Consulting: Owner's spouse
  Amount: $48K annually
  Service: Marketing (verify scope)
  ⚠️ Verify legitimate service

□ Equipment purchase: Owner-affiliated vendor
  Amount: $120K (prior year)
  ⚠️ Verify arms-length pricing

TIMING PATTERNS:
□ Quarter-end revenue spikes: PRESENT
  Q4 revenue as % of annual: 31% (elevated)
  Possible channel loading or timing issues

□ Month-end expense patterns: NORMAL

□ Year-end adjustments: ELEVATED
  Y-1 had $400K of favorable year-end adjustments
  ⚠️ Investigate nature of adjustments

ACCOUNTS RECEIVABLE:
□ Credit memos: 3.2% of sales (within normal)
□ Write-offs: 0.8% (acceptable)
□ Aging trend: DETERIORATING (flagged above)

FRAUD RISK ASSESSMENT: MODERATE
Indicators require investigation but no clear fraud evidence.
Recommend forensic review of inventory and year-end adjustments.
```

### Synergy Analysis

```
SYNERGY VALIDATION
==================
Platform Company: Industrial Holdings (existing PE portfolio)
Target: Precision Components Inc.

POTENTIAL SYNERGIES:

COST SYNERGIES:
| Category | Amount | Timing | Confidence |
|----------|--------|--------|------------|
| Corporate overhead | $200K | Y1 | HIGH |
| Insurance/benefits | $100K | Y1 | HIGH |
| Purchasing savings | $300K | Y2 | MEDIUM |
| Facility consolidation | $150K | Y3 | LOW |
| Total Cost | $750K | | |

REVENUE SYNERGIES:
| Category | Amount | Timing | Confidence |
|----------|--------|--------|------------|
| Cross-selling | $500K | Y2-3 | LOW |
| Customer introductions | $300K | Y2 | MEDIUM |
| Geographic expansion | $200K | Y3 | LOW |
| Total Revenue | $1.0M | | |

SYNERGY ASSUMPTIONS:
□ Purchasing: 5% improvement on $6M spend = $300K
  Basis: Platform company has buying power
  Risk: Supplier contracts may limit
  
□ Cross-selling: 3 qualified leads identified
  Basis: Platform customer overlap
  Risk: Long sales cycles in aerospace

SYNERGY NPV ANALYSIS:
Cost synergies (high confidence): $300K annual
NPV at 12%: $2.5M contribution to value
Revenue synergies (low confidence): Not included in valuation

⚠️ SYNERGY CAUTION:
Do not pay for synergies unless highly confident.
Recommend 20-30% haircut on projected synergies.
```

### Transaction Recommendations

```
DUE DILIGENCE FINDINGS SUMMARY
==============================

VALUATION IMPACT:
Original Enterprise Value: $50M (~8x EBITDA)
Adjustments:
- EBITDA adjustment: ($750K) → Adjusted EBITDA: $5.45M
- Excess working capital: ($1.5M) (negotiable)
- Inventory reserve: ($250K) (additional)
- Environmental (if issues found): TBD

ADJUSTED VALUATION:
At 8x adjusted EBITDA: $43.6M
Less working capital adjustment: ($1.5M)
Less incremental reserves: ($0.25M)
Adjusted EV: $41.9M

RECOMMENDED BID RANGE:
Low: $40M (7.3x adjusted EBITDA)
Target: $43M (7.9x adjusted EBITDA)
Max: $46M (8.4x adjusted EBITDA)

DEAL STRUCTURE RECOMMENDATIONS:
□ 85% cash at close
□ 10% holdback (12-18 months, WC adjustment)
□ 5% earnout (tied to Customer B renewal)

CONDITIONS PRECEDENT:
□ Customer A contract review satisfactory
□ Customer B renewal discussions positive
□ Environmental Phase I clean
□ Inventory physical count and valuation
□ AS9100 certification current
□ No material adverse change

POST-CLOSE PRIORITIES:
1. Working capital normalization
2. Customer B contract negotiation
3. Inventory reduction program
4. Synergy integration planning
```

---

## Verification Checklist

```
DUE DILIGENCE VERIFICATION REQUIRED
===================================
□ Complete customer contract review (top 3)
□ Customer reference calls (all top 5)
□ Inventory physical observation
□ Environmental Phase I review
□ AS9100 certification verification
□ Backlog verification and aging
□ Year-end adjustment analysis (forensic)
□ Related party pricing verification
□ Management interviews (all key positions)
□ Site visit completion

⚠️ INVESTMENT COMMITTEE REQUIREMENTS:
- QoE report from third-party accountants
- Environmental report
- Legal due diligence summary
- Management presentations
- Integration plan
- Final bid authorization
```

---

## Key Lessons

1. **Dig into working capital trends** — Often reveals hidden issues
2. **Customer concentration requires contract review** — Revenue at risk
3. **Quality of earnings adjustments are common** — Reported rarely equals adjusted
4. **Fraud screening standard in due diligence** — Benford's Law as first screen
5. **Synergies require skepticism** — Don't pay for what you might not get

---

*This use case demonstrates M&A due diligence workflow. Actual transactions require professional advisors, legal review, and thorough investigation.*
