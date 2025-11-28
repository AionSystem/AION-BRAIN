# Use Case 007: Transaction Tax Implications Overview

**Engine:** Financial Engine v1.5
**Domain:** Tax Planning Education
**Complexity:** Very High
**Risk Level:** CRITICAL (IRS implications)

---

## Scenario Description

A business owner considering a sale needs to understand general tax implications of different transaction structures without receiving tax advice (which requires a licensed tax professional).

---

## Oracle Layer Self-Correction Protocol

```
<SELF_CORRECTION_PROTOCOL>
CHECKPOINT 1: Tax Advice Boundary
├─ NEVER provide specific tax advice
├─ ONLY provide general educational information
├─ ALWAYS state: "Consult a tax professional"
├─ Self-correct: If "you should" appears → replace with "taxpayers may"
└─ Reason: Circular 230 prohibits unauthorized practice

CHECKPOINT 2: Code Section Citations
├─ VERIFY: Is this IRC section accurate?
├─ IF UNCERTAIN: Mark [VERIFY_REQUIRED:IRC_review]
├─ Note tax law changes frequently
└─ Always include: "Current law as of [date], subject to change"

CHECKPOINT 3: State Tax Considerations
├─ Federal discussion only unless state specified
├─ State tax varies significantly
├─ Always note: "State tax considerations vary"
└─ [VERIFY_REQUIRED:state_tax_professional]
</SELF_CORRECTION_PROTOCOL>
```

---

## Input/Output Example

### Query
```
<FINANCIAL_ENGINE_v1.5>
<MODE: TAX_EDUCATION>
<MODULE: TRANSACTION_STRUCTURES>

CONTEXT:
- Scenario: Potential business sale
- Structure options: Asset sale vs. stock sale
- Entity type: C-Corporation

QUESTION:
What are general tax considerations for different sale structures?

<fabrication:block>
<source_verification:required>
<fail_response:"Tax analysis requires licensed CPA/tax attorney">
</FINANCIAL_ENGINE_v1.5>
```

### Engine Response
```
TRANSACTION TAX STRUCTURE OVERVIEW
==================================

[EDUCATIONAL FRAMEWORK - Not Tax Advice]
Current law as of November 2025 - Subject to change

ASSET SALE vs. STOCK SALE: GENERAL FRAMEWORK
─────────────────────────────────────────────

ASSET SALE (General Concepts):
├─ Seller (Corporation) Perspective:
│   ├─ Corporation recognizes gain/loss on asset sale
│   ├─ Each asset class may have different tax treatment
│   ├─ Allocation under IRC §1060 required
│   ├─ Ordinary vs. capital gain depends on asset type
│   └─ [VERIFY_REQUIRED:asset_classification]
│
├─ Seller (Shareholder) Perspective:
│   ├─ C-Corp: Potential double taxation
│   │   └─ Corporate level + distribution level
│   ├─ S-Corp/Partnership: Generally single level
│   └─ [VERIFY_REQUIRED:entity_specific_analysis]
│
├─ Buyer Perspective:
│   ├─ Stepped-up basis in acquired assets
│   ├─ Depreciation/amortization benefits
│   ├─ Generally preferred by buyers
│   └─ Allocation negotiation critical
│
└─ Liability Considerations:
    ├─ Generally does NOT assume seller liabilities
    ├─ Successor liability exceptions exist
    └─ [VERIFY_REQUIRED:legal_counsel_review]

STOCK SALE (General Concepts):
├─ Seller (Shareholder) Perspective:
│   ├─ Capital gain treatment generally
│   ├─ Single level of tax
│   ├─ QSBS exclusion may apply (IRC §1202)
│   │   └─ If qualified: Potential 100% exclusion
│   ├─ Holding period considerations
│   └─ [VERIFY_REQUIRED:QSBS_qualification]
│
├─ Buyer Perspective:
│   ├─ Carryover basis in assets (no step-up)
│   ├─ IRC §338(h)(10) election possible
│   │   └─ Treats as asset sale for tax
│   ├─ Inherits all liabilities (known and unknown)
│   └─ Generally less preferred by buyers
│
└─ Liability Considerations:
    ├─ All entity liabilities transfer
    ├─ Representations and warranties critical
    └─ Indemnification provisions essential

IRC §338(h)(10) ELECTION (Overview):
├─ Allows stock sale to be treated as asset sale for tax
├─ Requires joint election by buyer and seller
├─ Seller recognizes gain as if asset sale
├─ Buyer gets stepped-up basis
├─ Complex planning considerations
└─ [VERIFY_REQUIRED:tax_professional_analysis]

QUALIFIED SMALL BUSINESS STOCK (IRC §1202):
├─ Potential 100% gain exclusion
├─ Requirements (simplified):
│   ├─ Original issuance stock
│   ├─ C-Corporation
│   ├─ Active business requirement
│   ├─ Gross asset test (<$50M)
│   ├─ 5-year holding period
│   └─ Qualified trade or business
├─ Exclusion limits apply
└─ [VERIFY_REQUIRED:QSBS_qualification_analysis]

INSTALLMENT SALE CONSIDERATIONS (IRC §453):
├─ May defer gain recognition
├─ At least one payment after tax year of sale
├─ Not available for publicly traded stock
├─ Dealer inventory exceptions
├─ Depreciation recapture recognized immediately
└─ [VERIFY_REQUIRED:installment_sale_planning]

═══════════════════════════════════════════════
⚠️ CRITICAL TAX DISCLAIMERS
═══════════════════════════════════════════════

1. This is GENERAL EDUCATIONAL information only
2. NOT tax advice for any specific transaction
3. Tax law changes frequently
4. State tax considerations vary significantly
5. Individual circumstances determine outcomes
6. Professional tax analysis REQUIRED

[MANDATORY_REFERRAL]
├─ CPA with transaction experience
├─ Tax attorney for complex structures
├─ Enrolled Agent (EA) for IRS representation
└─ State tax specialists if multi-state

[CONFIDENCE: MEDIUM]
├─ HIGH: General concepts are accurately described
├─ MEDIUM: Application to specific facts requires professional
├─ LOW: Specific tax outcomes (outside AI scope)

[IRS CIRCULAR 230 NOTICE]
This communication is not intended to be used, and cannot
be used, for the purpose of avoiding penalties under the
Internal Revenue Code.
```

---

## Compliance Checkpoints

| Checkpoint | Status | Validation |
|------------|--------|------------|
| No specific tax advice | PASS | General concepts only |
| Circular 230 notice | PASS | Included |
| Code section verification | FLAGGED | [VERIFY_REQUIRED] included |
| Professional referral | PASS | CPA/Tax attorney mandated |
| State tax caveat | PASS | Disclaimer included |

---

**Use Case Version:** 1.5
**Last Updated:** November 2025
