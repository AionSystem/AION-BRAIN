# Case 004: Contract Risk Review

**Scenario:** SaaS vendor agreement analysis  
**Modules Demonstrated:** Contract-focused analysis

---

## Scenario

A company is reviewing a SaaS vendor agreement for a critical business system. They need to identify risks before signing.

### Query to Legal Engine 2

```
Reviewing a SaaS vendor agreement for our CRM system. 3-year term,
$120K/year. They want us to sign their standard form. What should
we look out for?
```

---

## Legal Engine 2 Response

```
═══════════════════════════════════════════════════════════════
LEGAL ENGINE 2 v1.0 — CONTRACT RISK REVIEW
═══════════════════════════════════════════════════════════════

⚠️ DISCLAIMER: This is not legal advice. Attorney review before signing.

CONTRACT TYPE: SaaS Vendor Agreement
VALUE: $360,000 (3 years × $120K)
RISK LEVEL: HIGH (standard form = vendor-favorable terms)

═══════════════════════════════════════════════════════════════
KEY RISK AREAS IN SaaS AGREEMENTS
═══════════════════════════════════════════════════════════════

CRITICAL CLAUSES TO REVIEW:

1. DATA OWNERSHIP & PRIVACY
├─ ⚠️ WHO OWNS YOUR DATA?
│   ├─ Look for: "Customer retains all rights to Customer Data"
│   ├─ Red flag: Vendor claims license to use your data
│   ├─ Red flag: Data used for "product improvement" broadly
│   └─ Negotiate: Clear customer ownership, limited vendor use
├─ ⚠️ DATA SECURITY OBLIGATIONS
│   ├─ Look for: Specific security standards (SOC 2, ISO 27001)
│   ├─ Red flag: "Commercially reasonable" with no specifics
│   └─ Negotiate: Defined security requirements, audit rights
├─ ⚠️ DATA PROCESSING AGREEMENT
│   ├─ Required: If personal data processed (CCPA, GDPR)
│   ├─ Look for: DPA as exhibit or incorporated
│   └─ Negotiate: GDPR-compliant DPA with SCCs if needed

2. SERVICE LEVELS (SLA)
├─ ⚠️ UPTIME COMMITMENT
│   ├─ Industry standard: 99.9% (8.7 hours downtime/year)
│   ├─ Red flag: No SLA or weak commitment
│   ├─ Red flag: Excessive exclusions (maintenance, force majeure)
│   └─ Negotiate: Specific uptime %, defined measurement
├─ ⚠️ SLA REMEDIES
│   ├─ Look for: Service credits for downtime
│   ├─ Red flag: Credits as sole remedy (cap your damages)
│   ├─ Red flag: Must claim within short window
│   └─ Negotiate: Meaningful credits, termination if chronic failure
├─ ⚠️ SUPPORT RESPONSE TIMES
│   ├─ Look for: Defined response times by severity
│   ├─ Red flag: No response time commitments
│   └─ Negotiate: Severity definitions, response and resolution times

3. LIMITATION OF LIABILITY
├─ ⚠️ LIABILITY CAP
│   ├─ Standard: 12 months of fees ($120K in your case)
│   ├─ Red flag: Very low cap (e.g., $10K)
│   ├─ Red flag: Cap applies to their breach, not yours
│   └─ Negotiate: At least 12-24 months of fees
├─ ⚠️ EXCLUSION OF DAMAGES
│   ├─ Standard: Mutual exclusion of consequential damages
│   ├─ Red flag: One-sided (only you excluded)
│   ├─ Red flag: Includes data breach in exclusion
│   └─ Negotiate: Carve-outs for data breach, IP infringement
├─ ⚠️ SUPER CAP ITEMS
│   ├─ Should be UNCAPPED or higher cap:
│   ├─ Their indemnification obligations
│   ├─ Data breach / security failure
│   ├─ IP infringement
│   ├─ Gross negligence / willful misconduct
│   └─ Negotiate: Explicit super cap carve-outs

4. INDEMNIFICATION
├─ ⚠️ VENDOR INDEMNIFICATION (they protect you)
│   ├─ Should cover: IP infringement claims
│   ├─ Should cover: Their negligence / breach
│   ├─ Red flag: Narrow scope, many exclusions
│   └─ Negotiate: Broad IP indemnity, reasonable exclusions only
├─ ⚠️ YOUR INDEMNIFICATION (you protect them)
│   ├─ Standard: Your breach, your data, your use
│   ├─ Red flag: Overly broad (their failures become your liability)
│   ├─ Red flag: Indemnify for their sub-processors
│   └─ Negotiate: Limited to matters within your control

5. TERMINATION & EXIT
├─ ⚠️ TERMINATION FOR CONVENIENCE
│   ├─ Look for: Your right to terminate with notice
│   ├─ Red flag: No termination right (locked in 3 years)
│   ├─ Red flag: Heavy termination penalties
│   └─ Negotiate: 30-90 day termination right, pro-rata refund
├─ ⚠️ DATA RETURN/DELETION
│   ├─ Look for: Return data in usable format upon termination
│   ├─ Red flag: No data export provision
│   ├─ Red flag: Data deleted immediately upon termination
│   └─ Negotiate: 30-90 day transition period, standard format
├─ ⚠️ TRANSITION ASSISTANCE
│   ├─ Look for: Vendor assistance during migration
│   └─ Negotiate: Reasonable transition services included

6. PRICING & PAYMENT
├─ ⚠️ PRICE INCREASES
│   ├─ Look for: Cap on renewal price increases
│   ├─ Red flag: Unlimited increases at renewal
│   └─ Negotiate: Cap at CPI or 5%, whichever less
├─ ⚠️ AUTO-RENEWAL
│   ├─ Standard: Auto-renews unless notice given
│   ├─ Red flag: Short notice window (30 days)
│   └─ Negotiate: 60-90 day notice, reminder obligation

7. IP RIGHTS
├─ ⚠️ OWNERSHIP
│   ├─ Your data: You own it
│   ├─ Your customizations: Clarify ownership
│   ├─ Their platform: They own it
│   └─ Negotiate: Clear ownership of your inputs/outputs
├─ ⚠️ LICENSE SCOPE
│   ├─ Look for: Clear grant of rights you need
│   ├─ Red flag: Restrictions on normal use
│   └─ Negotiate: Flexibility for reasonable business use

═══════════════════════════════════════════════════════════════
RISK MATRIX FOR THIS CONTRACT
═══════════════════════════════════════════════════════════════

| Issue | Typical Vendor Position | Your Risk | Priority |
|-------|------------------------|-----------|----------|
| Liability cap | 12 mo fees | MODERATE | HIGH |
| Data ownership | Broad license to vendor | HIGH | CRITICAL |
| SLA | Weak or none | MODERATE | HIGH |
| Termination | No convenience right | HIGH | HIGH |
| Data exit | Not addressed | HIGH | CRITICAL |
| Price increases | Unlimited | MODERATE | MODERATE |
| Indemnification | One-sided | HIGH | HIGH |

═══════════════════════════════════════════════════════════════
NEGOTIATION PRIORITIES
═══════════════════════════════════════════════════════════════

P1 - MUST CHANGE (Deal-breakers):
├─ Clear customer data ownership
├─ Data return provision at termination
├─ Reasonable liability cap (not <12 months fees)
├─ Data breach carve-out from liability exclusions
└─ IP indemnification from vendor

P2 - SHOULD CHANGE (Significant concerns):
├─ Termination for convenience right
├─ Defined SLA with meaningful remedies
├─ Mutual indemnification (not one-sided)
├─ Price increase cap for renewals
└─ Reasonable notice period for auto-renewal

P3 - NICE TO HAVE (Improvements):
├─ Extended transition assistance
├─ Audit rights for security
├─ Escrow for source code
└─ More favorable payment terms

═══════════════════════════════════════════════════════════════
EXPOSURE IF SIGNED AS-IS
═══════════════════════════════════════════════════════════════

WORST CASE SCENARIOS:

SCENARIO 1: Vendor goes out of business
├─ Without data export clause: Data trapped or lost
├─ Without source escrow: No access to continue operations
├─ Without transition terms: Emergency migration under duress
└─ Exposure: $50K - $200K (emergency migration + lost data)

SCENARIO 2: Security breach at vendor
├─ With broad liability exclusion: No recovery
├─ Without breach notification: Delayed response
├─ Without security standards: Weak protection
└─ Exposure: Your regulatory liability ($100K - $1M+)

SCENARIO 3: Vendor significantly increases price at renewal
├─ Without cap: Could double or triple
├─ With short renewal notice: Locked in before you can respond
└─ Exposure: $120K - $240K+ annual increase

SCENARIO 4: You need to switch vendors
├─ Without termination right: Stuck for 3 years
├─ Without data export: Can't migrate data
├─ With termination penalty: Pay remaining term
└─ Exposure: $240K+ (remaining term)

TOTAL POTENTIAL EXPOSURE: $400K - $1.5M+

═══════════════════════════════════════════════════════════════
REMEDIATION ROADMAP
═══════════════════════════════════════════════════════════════

BEFORE SIGNING:

STEP 1: Mark up the agreement (0-3 days)
├─ Owner: Legal/Procurement
├─ Action: Identify all issues, propose changes
├─ Use: Redline with your requested changes
└─ Attorney: RECOMMENDED for $360K contract

STEP 2: Negotiate (3-14 days)
├─ Focus on P1 items first
├─ Be prepared to walk away on data ownership/exit
├─ Document what you couldn't change
└─ Escalate to vendor management if needed

STEP 3: Final review (1-3 days)
├─ Ensure all agreed changes in final version
├─ Compare to original marked-up version
├─ Confirm signature authority
└─ Attorney: Final review before execution

═══════════════════════════════════════════════════════════════
ATTORNEY CONSULTATION TRIGGERS
═══════════════════════════════════════════════════════════════

⚠️ REQUIRED: Contract value >$100K (you're at $360K)
⚠️ REQUIRED: Data processing agreement (CCPA/GDPR)
⚠️ REQUIRED: Indemnification provisions
⚠️ REQUIRED: Limitation of liability negotiation
⚠️ RECOMMENDED: Full contract markup and negotiation

ESTIMATED LEGAL COST: $5,000 - $15,000 (worth it for $360K contract)

═══════════════════════════════════════════════════════════════
```

---

## Why This Case Matters

Vendor contracts often contain one-sided terms because:
- Standard forms are drafted by vendor's lawyers
- "Take it or leave it" is often a negotiating tactic
- Customers don't read or negotiate
- Real costs appear later (exit, breach, disputes)

$360K contract deserves attorney review.

---

**Case Version:** 1.0  
**Last Updated:** November 2025
