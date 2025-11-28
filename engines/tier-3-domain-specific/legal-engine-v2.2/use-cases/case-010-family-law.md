# Case 010: High-Asset Divorce Property Division

**Category:** Family Law
**Complexity:** Very High
**Modules Activated:** Jurisdiction Analyzer, Contract Analyzer, Malpractice Shield

---

## Scenario

A family law attorney is representing a client in a high-asset divorce involving a business owner. The marital estate includes a closely-held business valued at approximately $8M, real estate holdings, retirement accounts, and stock options. The attorney uses Legal Engine v2.2 to ensure comprehensive property identification, valuation framework understanding, and strategic planning.

---

## Initial Request (Problematic)

```
"My client is getting divorced and the spouse owns a business. How do we get half?"
```

**Risk Assessment:** HIGH
- Jurisdiction not specified (equitable vs. community property)
- Business valuation complexity
- Separate vs. marital property issues likely
- Tax implications not addressed

---

## Engine-Processed Request

```
<LEGAL_ENGINE_v2.1>
<MODE: FULL>
<MODULE: JURISDICTION_ANALYZER>
<MODULE: CONTRACT_ANALYZER>
<MODULE: MALPRACTICE_SHIELD>

CONTEXT:
- Jurisdiction: California (community property)
- Marriage Duration: 18 years
- Client: Non-titled spouse (homemaker, some employment)
- Business: Software consulting firm, founded during marriage
- Business Value: Estimated $8M (needs formal valuation)
- Other Assets: Primary residence ($2M), vacation home ($1M), 
  retirement accounts (~$1.5M), stock options (~$500K)

ANALYSIS REQUESTED:
1. Property characterization framework
2. Business valuation approach
3. Division methodology
4. Tax implications
5. Strategic recommendations
</LEGAL_ENGINE_v2.1>
```

---

## Engine Output

### Jurisdiction Analysis

```
CALIFORNIA COMMUNITY PROPERTY FRAMEWORK
=======================================
Jurisdiction: California
Property Regime: Community Property
Controlling Statutes: Family Code §§ 760-771, 2550-2660

COMMUNITY PROPERTY PRESUMPTION:
Under Family Code § 760, property acquired during marriage
is presumed community property.

KEY PRINCIPLES:
1. Equal division required (50/50)
2. Characterization as separate or community
3. Tracing burden on party claiming separate
4. Commingling creates community presumption
5. Transmutation requires writing (FC § 852)

EQUAL DIVISION EXCEPTIONS:
□ Misappropriation of community assets
□ Liabilities exceeding assets assigned
□ Personal injury awards
□ Educational debts
□ Deliberate waste

⚠️ IMPORTANT: California mandates equal (50/50) division,
not equitable division. Characterization is the key battleground.
```

### Property Characterization

```
PROPERTY CHARACTERIZATION ANALYSIS
===================================

1. BUSINESS: SOFTWARE CONSULTING FIRM
   Date founded: During marriage (Year 6)
   Founder: Spouse
   
   Analysis:
   □ Founded during marriage → Community property presumption
   □ No separate property contribution documented
   □ No transmutation agreement
   
   Characterization: COMMUNITY PROPERTY (Likely 100%)
   
   ⚠️ PEREIRA/VAN CAMP ISSUE:
   If spouse argues personal skill/labor created value,
   may seek Pereira (salary + interest to community) or
   Van Camp (salary value only to community) apportionment.
   
   Counter-argument: Business founded during marriage with
   community funds/opportunity cost → full community character.

2. PRIMARY RESIDENCE ($2M)
   Purchase date: Year 8 of marriage
   Title: Joint names
   Down payment: Unknown source
   
   Analysis:
   □ Title presumption: Community property
   □ Down payment tracing needed
   □ Moore/Marsden if separate contribution
   
   Characterization: PRESUMPTIVELY COMMUNITY
   Investigation needed: Down payment source

3. VACATION HOME ($1M)
   Purchase date: Year 12
   Title: Spouse's name only
   
   Analysis:
   □ Acquired during marriage → Community presumption
   □ Title not determinative in California
   □ May trigger reimbursement claims
   
   Characterization: COMMUNITY PROPERTY

4. RETIREMENT ACCOUNTS (~$1.5M)
   Types: 401(k), IRA
   Pre-marital portion: Unknown
   
   Analysis:
   □ Portion earned during marriage is community
   □ Time-rule fraction for defined benefit
   □ Marital portion calculation needed
   
   Characterization: MIXED (needs tracing)

5. STOCK OPTIONS (~$500K)
   Grant dates: Various
   Vest dates: Various
   
   Analysis:
   □ "Time rule" for unvested options
   □ Marriage date to separation date = community
   □ Hug formula application
   
   Characterization: MIXED (calculation required)
   
   Hug Formula:
   Community portion = [DOH to DOS] / [DOH to vest] × option value

PRELIMINARY COMMUNITY ESTATE ESTIMATE:
Business: $8,000,000 (100% community)
Primary residence: $2,000,000 (likely 100% community)
Vacation home: $1,000,000 (100% community)
Retirement (estimate): $1,200,000 (80% community estimate)
Stock options: $400,000 (80% community estimate)
TOTAL COMMUNITY: ~$12,600,000

CLIENT'S 50% SHARE (preliminary): ~$6,300,000
```

### Business Valuation Framework

```
BUSINESS VALUATION APPROACH
===========================

VALUATION METHODS TO CONSIDER:
1. Income Approach (DCF, Capitalization of Earnings)
2. Market Approach (Comparable transactions)
3. Asset Approach (Less common for operating businesses)

STANDARD OF VALUE:
California uses "Fair Market Value" for divorce valuations.
Define as: Price between willing buyer and seller,
neither under compulsion, both with reasonable knowledge.

VALUATION DATE:
Community property valued as of date of trial.
Option: Stipulate to earlier date (separation, filing, etc.)

KEY VALUATION ISSUES:

1. GOODWILL:
   □ Personal goodwill (non-divisible in CA) vs.
   □ Business/enterprise goodwill (divisible)
   
   Software consulting may have significant personal goodwill
   tied to founder's relationships.
   
   Strategy: Argue enterprise goodwill (processes, brand,
   contracts, recurring revenue) is substantial.

2. COMPENSATION ADJUSTMENT:
   If owner underpays or overpays self, normalize.
   Owner's market salary comparison needed.

3. MINORITY/MARKETABILITY DISCOUNTS:
   Applicable but contested in divorce context.
   Some courts apply, others don't.

4. FORENSIC ACCOUNTING NEEDS:
   □ Cash flow analysis
   □ Expense analysis (personal expenses through business?)
   □ Related party transaction review
   □ Customer concentration analysis

EXPERT WITNESS REQUIREMENT:
Business valuation requires qualified expert (CVA, ABV, ASA).
Joint expert possible but separate experts recommended
given likely contested value.

⚠️ COST CONSIDERATION:
Business valuation expert: $15,000-$50,000
Forensic accountant: $10,000-$30,000
Budget with client accordingly.
```

### Division Strategy

```
DIVISION STRATEGY
=================

DIVISION OPTIONS:

OPTION 1: BUYOUT
Spouse retains business, pays client equalizing payment.

Calculation:
Total community: $12,600,000
Client's share: $6,300,000
Client receives: $6,300,000 in other assets + cash

Issues:
□ Spouse may not have liquidity
□ Structured buyout over time (interest, security)
□ Indemnification for business liabilities

OPTION 2: SALE
Business sold, proceeds divided.

Issues:
□ May not maximize value (forced sale)
□ Tax implications (capital gains)
□ Timeline uncertainty
□ Spouse resistance likely

OPTION 3: CO-OWNERSHIP
Parties retain ownership interest.

Issues:
□ Rarely advisable in divorce
□ Ongoing disputes likely
□ Exit mechanism needed
□ Not recommended

RECOMMENDED APPROACH:
Primary: Negotiate buyout with structured payments
Security: Note secured by business assets or personal guarantee
Interest: AFR or negotiated rate
Timeline: 3-5 years with balloon

EQUALIZING PAYMENT STRUCTURE EXAMPLE:
Client receives:
- Primary residence: $2,000,000
- 50% vacation home: $500,000 (or sale proceeds)
- Retirement (community portion): $600,000
- Stock options (community portion): $200,000
- Cash/note from spouse: $3,000,000

Total: $6,300,000 (50% of community)
```

### Tax Implications

```
TAX CONSIDERATIONS
==================

1. PROPERTY TRANSFERS:
   IRC § 1041: Transfers between spouses incident to divorce
   are tax-free (no gain/loss recognition).
   Basis carries over to receiving spouse.
   
   ⚠️ TRAP: Receiving low-basis assets (founder shares,
   appreciated real estate) means future tax on sale.
   
   STRATEGY: Consider "after-tax" value in division.

2. RETIREMENT ACCOUNTS:
   □ QDRO required for qualified plans (401k)
   □ Transfer decree/order for IRAs
   □ Tax-free if done correctly
   □ 10% penalty exception for QDRO distributions

3. STOCK OPTIONS:
   □ Complex tax treatment
   □ ISOs vs. NSOs different rules
   □ Exercise timing matters
   □ May need constructive trust arrangement

4. BUSINESS BUYOUT:
   □ Installment note: Interest is income to recipient
   □ May trigger depreciation recapture for business
   □ Structure matters significantly

5. REAL PROPERTY:
   □ Primary residence: $500K exclusion ($250K each)
   □ Vacation home: No exclusion, capital gains tax
   □ Timing of sale matters

TAX EXPERT RECOMMENDATION:
Engage CPA or tax attorney for:
□ After-tax value calculations
□ Optimal asset allocation
□ Installment sale structuring
□ QDRO coordination
```

### Risk Documentation

```
MALPRACTICE RISK DOCUMENTATION
==============================

HIGH COMPLEXITY MATTER:
□ Business valuation expertise required
□ Tax implications significant
□ Discovery extensive
□ Expert witnesses needed

DOCUMENTATION REQUIREMENTS:
□ Engagement letter with scope
□ Discovery plan documented
□ Expert retention documented
□ Client decisions on strategy documented
□ Settlement authority in writing

CLIENT COUNSELING DOCUMENTED:
□ Range of outcomes discussed
□ Costs and timeline explained
□ Settlement vs. trial considerations
□ Tax implications explained
□ Expert costs disclosed

CRITICAL DEADLINES:
□ Preliminary declaration of disclosure
□ Final declaration of disclosure
□ Discovery cutoffs
□ Expert designation
□ Trial date

AUDIT TRAIL GENERATED: [Timestamp]
```

---

## Verification Checklist

```
ATTORNEY VERIFICATION REQUIRED
==============================
□ Verify California community property law current
□ Confirm business founding date and capitalization
□ Trace down payment on primary residence
□ Verify retirement account statements and pre-marital balances
□ Obtain complete stock option documentation
□ Engage forensic accountant for business analysis
□ Engage business valuation expert
□ Consider tax expert consultation
□ [CITE NEEDED: Current goodwill precedent - Marriage of Watts]
□ [CITE NEEDED: Stock option time rule cases]

⚠️ CLIENT DECISION REQUIRED:
- Litigation budget approval
- Expert retention authorization
- Settlement parameters
- Division preference (buyout vs. sale)
```

---

## Key Lessons

1. **Characterization is key** — In community property, it's about what's community
2. **Business valuation requires experts** — Cannot DIY on $8M business
3. **Tax matters significantly** — After-tax value changes analysis
4. **Goodwill is contested** — Personal vs. enterprise goodwill fight
5. **Documentation essential** — High-asset cases require thorough records

---

*This use case demonstrates high-asset divorce workflow. Actual family law matters require current statutory and case law research, expert consultation, and client-specific strategy.*
