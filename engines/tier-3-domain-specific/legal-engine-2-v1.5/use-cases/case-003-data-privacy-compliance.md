# Case 003: Data Privacy Compliance Assessment

**Scenario:** E-commerce company privacy law compliance  
**Modules Demonstrated:** All 5 modules with privacy focus

---

## Scenario

An e-commerce company with $30M annual revenue processes customer data from all 50 states and has some European customers. They need to understand their privacy law obligations.

### Query to Legal Engine 2

```
E-commerce company, $30M revenue, customers in all 50 states plus 
some EU customers. We collect names, emails, addresses, purchase 
history, and use cookies for analytics. What privacy laws apply 
and what do we need to do?
```

---

## Legal Engine 2 Response

```
═══════════════════════════════════════════════════════════════
LEGAL ENGINE 2 v1.0 — COMPLIANCE STATUS REPORT
═══════════════════════════════════════════════════════════════

⚠️ DISCLAIMER: This is not legal advice. Consult privacy counsel.

ORGANIZATION: E-commerce Company ($30M revenue)
ANALYSIS TYPE: Data Privacy Compliance Assessment
OVERALL STATUS: YELLOW (Multiple frameworks apply)

═══════════════════════════════════════════════════════════════
MODULE 1: JURISDICTION IDENTIFICATION
═══════════════════════════════════════════════════════════════

APPLICABLE PRIVACY FRAMEWORKS:

✓ FEDERAL (FTC Act Section 5):
  ├─ Trigger: Doing business in interstate commerce
  ├─ Scope: Unfair or deceptive practices re: privacy
  ├─ Enforcement: FTC
  └─ Status: APPLIES

✓ CALIFORNIA (CCPA/CPRA):
  ├─ Trigger: $25M+ revenue ✓ (you have $30M)
  ├─ Scope: California residents' personal information
  ├─ Enforcement: CA AG, CPPA, private right (breaches)
  └─ Status: APPLIES

✓ VIRGINIA (VCDPA):
  ├─ Trigger: 100K+ consumers OR 25K+ with 50%+ revenue from data
  ├─ Scope: Virginia residents' personal data
  ├─ [VERIFICATION REQUIRED: Check thresholds]
  └─ Status: LIKELY APPLIES

✓ COLORADO (CPA):
  ├─ Trigger: 100K+ consumers OR 25K+ with revenue from data
  ├─ [VERIFICATION REQUIRED: Check thresholds]
  └─ Status: LIKELY APPLIES

✓ CONNECTICUT (CTDPA):
  ├─ Trigger: 100K+ consumers OR 25K+ with 25%+ revenue from data
  ├─ [VERIFICATION REQUIRED: Check thresholds]
  └─ Status: LIKELY APPLIES

✓ EUROPEAN UNION (GDPR):
  ├─ Trigger: Offering goods to EU residents
  ├─ Scope: EU data subjects' personal data
  ├─ Enforcement: EU DPAs (extraterritorial)
  └─ Status: APPLIES (you have EU customers)

OTHER CONSIDERATIONS:
├─ CAN-SPAM: Email marketing requirements
├─ TCPA: If using SMS or calls
├─ COPPA: If any users under 13
└─ State breach notification: All 50 states

═══════════════════════════════════════════════════════════════
MODULE 2: APPLICABLE LAW SUMMARY
═══════════════════════════════════════════════════════════════

CCPA/CPRA (Primary US Framework):

[APPLICABLE LAW: California Consumer Privacy Act / CPRA]
├─ Jurisdiction: California residents
├─ Threshold Met: >$25M revenue ✓
├─ Key Requirements:
│   • Privacy notice at/before collection
│   • Right to know (access)
│   • Right to delete
│   • Right to opt-out of sale/sharing
│   • Right to correct
│   • Right to limit sensitive data use
│   • Non-discrimination
│   • Service provider contracts
├─ Enforcement: CA AG ($2,500-$7,500/violation), CPPA
├─ Private Right: Data breach only
└─ Confidence: HIGH

GDPR (EU Framework):

[APPLICABLE LAW: General Data Protection Regulation]
├─ Jurisdiction: EU data subjects
├─ Trigger: Offering goods to EU ✓
├─ Key Requirements:
│   • Lawful basis for processing (consent, contract, etc.)
│   • Privacy notice (Articles 13/14)
│   • Data subject rights (access, erasure, portability, etc.)
│   • Privacy by design
│   • Data protection impact assessments (if high risk)
│   • Cross-border transfer mechanisms
│   • Data breach notification (72 hours)
├─ Enforcement: EU DPAs (up to €20M or 4% global revenue)
└─ Confidence: HIGH (if EU customers confirmed)

COOKIES/TRACKING:

├─ CCPA: Requires disclosure, opt-out of sale/sharing
├─ CPRA: Sensitive data restrictions
├─ GDPR: Prior consent required (not just notice)
├─ ePrivacy Directive: Cookie consent requirements
└─ [GAP LIKELY: Most US sites not GDPR cookie compliant]

═══════════════════════════════════════════════════════════════
MODULE 3: COMPLIANCE GAP MATRIX
═══════════════════════════════════════════════════════════════

| # | Gap | Framework | Severity | Priority |
|---|-----|-----------|----------|----------|
| 1 | GDPR lawful basis undefined | GDPR | CRITICAL | 1 |
| 2 | Cookie consent inadequate | GDPR | CRITICAL | 1 |
| 3 | Privacy policy incomplete | CCPA/GDPR | HIGH | 2 |
| 4 | Consumer rights process missing | CCPA | HIGH | 2 |
| 5 | Cross-border transfer mechanism | GDPR | HIGH | 2 |
| 6 | Vendor contracts non-compliant | CCPA/GDPR | MODERATE | 3 |
| 7 | Data inventory incomplete | All | MODERATE | 3 |

DETAILED GAP ANALYSIS:

GAP 1: GDPR LAWFUL BASIS
├─ Requirement: Document lawful basis for each processing activity
├─ Options: Consent, contract, legitimate interest, legal obligation
├─ Current State: Likely not documented
├─ Risk: Fundamental GDPR violation
├─ Severity: CRITICAL
└─ Attorney Required: YES (privacy specialist)

GAP 2: COOKIE CONSENT (GDPR)
├─ Requirement: Prior, informed consent before non-essential cookies
├─ Current State: US-style "notice and continue" not sufficient
├─ Need: Cookie banner with accept/reject, granular control
├─ Risk: €20M or 4% revenue maximum
├─ Severity: CRITICAL (for EU visitors)
└─ Attorney Required: Recommended

GAP 3: PRIVACY POLICY
├─ Requirement: CCPA disclosures + GDPR Articles 13/14
├─ CCPA needs: Categories collected, purposes, rights, opt-out
├─ GDPR needs: Legal basis, retention, transfers, DPO, rights
├─ Current State: Likely missing required elements
├─ Severity: HIGH
└─ Attorney Required: YES

GAP 4: CONSUMER RIGHTS PROCESS
├─ Requirement: Process to handle access, delete, opt-out requests
├─ CCPA: 45-day response deadline
├─ GDPR: 30-day response deadline
├─ Current State: Likely no formal process
├─ Severity: HIGH
└─ Attorney Required: Recommended

GAP 5: CROSS-BORDER TRANSFERS
├─ Requirement: Mechanism for EU→US data transfers
├─ Options: Standard Contractual Clauses, Binding Corporate Rules
├─ Current State: Likely no mechanism in place
├─ Risk: All EU data processing potentially unlawful
├─ Severity: HIGH
└─ Attorney Required: YES

═══════════════════════════════════════════════════════════════
MODULE 4: LIABILITY EXPOSURE SUMMARY
═══════════════════════════════════════════════════════════════

CCPA/CPRA EXPOSURE:

REGULATORY:
├─ Per Violation: $2,500 (unintentional), $7,500 (intentional)
├─ If 10,000 CA consumers affected
├─ Potential: $25M - $75M (theoretical maximum)
├─ Realistic: $100K - $500K (typical enforcement)
└─ Note: CPPA building enforcement capacity

PRIVATE (DATA BREACH ONLY):
├─ Per Consumer: $100 - $750 statutory damages
├─ If breach affects 10,000 CA consumers
├─ Exposure: $1M - $7.5M
└─ Class action risk: HIGH

GDPR EXPOSURE:

REGULATORY:
├─ Maximum: €20M or 4% global revenue (€1.2M at $30M)
├─ Whichever is greater: €20M
├─ Realistic: €50K - €500K (SME enforcement)
├─ Trend: Increasing fines and enforcement
└─ Cookie violations: €5K - €100K typical

FTC EXPOSURE:
├─ Civil Penalties: Up to $50,120 per violation
├─ Consent Decrees: Ongoing compliance obligations
├─ Realistic: $50K - $200K
└─ Reputational: FTC actions are public

TOTAL PRIVACY EXPOSURE RANGE:
├─ LOW (no incidents): $100K - $300K (remediation costs)
├─ MID (regulatory inquiry): $300K - $1M
├─ HIGH (breach + enforcement): $2M - $10M+
└─ Note: Breach triggers multiple frameworks simultaneously

═══════════════════════════════════════════════════════════════
MODULE 5: REMEDIATION ROADMAP
═══════════════════════════════════════════════════════════════

P1 - IMMEDIATE (0-7 days):
├─ P1-001: Implement GDPR-compliant cookie consent
│   ├─ Owner: IT/Marketing
│   ├─ Action: Cookie consent management platform
│   ├─ Timeline: ASAP for EU visitors
│   └─ Tools: OneTrust, Cookiebot, or similar
├─ P1-002: Data inventory initiation
│   ├─ Owner: IT/Legal
│   ├─ Action: Document what data, where, why
│   ├─ Timeline: Start immediately, 30 days to complete
│   └─ Attorney: Recommended guidance

P2 - URGENT (7-30 days):
├─ P2-001: Privacy policy update
│   ├─ Owner: Legal
│   ├─ Action: CCPA + GDPR compliant policy
│   ├─ Timeline: 14-21 days
│   └─ Attorney: REQUIRED
├─ P2-002: Consumer rights intake process
│   ├─ Owner: Customer Service/Legal
│   ├─ Action: Form, workflow, response templates
│   ├─ Timeline: 21 days
│   └─ Attorney: Review
├─ P2-003: Cross-border transfer mechanism
│   ├─ Owner: Legal
│   ├─ Action: Implement Standard Contractual Clauses
│   ├─ Timeline: 30 days
│   └─ Attorney: REQUIRED

P3 - NEAR-TERM (30-90 days):
├─ P3-001: Vendor contract updates
│   ├─ Owner: Legal/Procurement
│   ├─ Action: Data processing addenda
│   ├─ Timeline: 60 days
│   └─ Attorney: Templates needed
├─ P3-002: GDPR lawful basis documentation
│   ├─ Owner: Legal
│   ├─ Action: Record of processing activities
│   ├─ Timeline: 60-90 days
│   └─ Attorney: REQUIRED
├─ P3-003: Employee privacy training
│   ├─ Owner: HR
│   ├─ Action: Privacy awareness training
│   ├─ Timeline: 90 days
│   └─ Attorney: Review materials

═══════════════════════════════════════════════════════════════
ATTORNEY CONSULTATION TRIGGERS
═══════════════════════════════════════════════════════════════

⚠️ REQUIRED: Privacy policy drafting (CCPA + GDPR)
⚠️ REQUIRED: GDPR lawful basis analysis
⚠️ REQUIRED: Standard Contractual Clauses implementation
⚠️ REQUIRED: EU representative appointment (if no EU establishment)
⚠️ RECOMMENDED: Cookie consent implementation review
⚠️ RECOMMENDED: Vendor contract templates

ESTIMATED LEGAL BUDGET: $25,000 - $50,000
ESTIMATED TECHNOLOGY: $10,000 - $30,000/year (consent tools, etc.)

═══════════════════════════════════════════════════════════════
```

---

## Why This Case Matters

Privacy law is rapidly evolving:
- CCPA/CPRA is the de facto US standard
- State laws multiplying (VA, CO, CT, UT, plus more coming)
- GDPR applies to any company with EU customers
- Penalties are substantial and enforcement increasing

---

**Case Version:** 1.0  
**Last Updated:** November 2025
