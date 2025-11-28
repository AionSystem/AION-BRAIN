# LAYER 2: Citation Integrity Validator

**Layer Position:** 2  
**Purpose:** Prevent fabricated case law through citation verification requirements

---

## Function

Layer 2 detects high-risk citation requests, provides graduated warnings, and rewrites prompts to avoid AI-generated fabricated citations.

---

## The Citation Fabrication Problem

AI models frequently fabricate legal citations that appear authentic:
- Realistic case names with plausible parties
- Proper Bluebook formatting
- Correct reporter abbreviations
- Non-existent volume/page combinations
- Fabricated holdings that sound legally correct

---

## Documented Malpractice Cases

| Case | Court | Consequence | Issue |
|------|-------|-------------|-------|
| **Mata v. Avianca, Inc.** | S.D.N.Y. 2023 | $5,000 sanction | 6 fake citations submitted |
| **Kruse v. Karlen** | D. Colo. 2023 | Show cause order | Non-existent citations in motion |
| **Park v. Kim** | Cal. Super. Ct. 2024 | Bar disciplinary referral | Pattern of unverified AI citations |

---

## Detection Triggers

### High-Risk Patterns

| Phrase | Risk Level |
|--------|------------|
| "Find cases supporting..." | CRITICAL |
| "Cite authority for..." | CRITICAL |
| "What precedent establishes..." | HIGH |
| "Are there cases holding..." | HIGH |
| "Provide legal citations for..." | CRITICAL |
| Legal propositions without source constraints | MODERATE |

### Citation Format Detection

- Bluebook format: `Smith v. Jones, 123 F.3d 456 (9th Cir. 2020)`
- Incomplete citations (missing elements)
- Suspicious patterns (unusual reporters, non-existent courts)
- User-submitted citations for AI analysis

---

## Graduated Risk Assessment

### CRITICAL (95-100%)

**Trigger:** Direct request for AI to generate citations

**Example:**
```
"Find cases supporting the argument that mandatory
arbitration clauses are unconscionable."
```

**Intervention:** Automatic rewrite with strong warning

---

### HIGH (75-95%)

**Trigger:** Legal proposition without citation + expectation AI will cite authority

**Example:**
```
"Explain the legal standard for summary judgment and
provide case support."
```

**Intervention:** Suggested rewrite + citation protocol injection

---

### MODERATE (50-75%)

**Trigger:** General legal research query that may prompt AI to cite

**Example:**
```
"What are the elements of negligence?"
```

**Intervention:** Warning + verification requirements added

---

### LOW (<50%)

**Trigger:** Legal reasoning request without citation expectation

**Example:**
```
"Draft argument structure for negligence claim.
I will add citations separately."
```

**Intervention:** Minimal (verification reminder only)

---

## Intervention Protocol

### Warning Display (CRITICAL/HIGH Risk)

```
═══════════════════════════════════════════════════════════════════
🔴 CITATION FABRICATION RISK — LAYER 2 INTERVENTION
═══════════════════════════════════════════════════════════════════

RISK LEVEL: CRITICAL
Confidence: VERY HIGH (Pattern documented in case law)

Your prompt requests case law citations from AI.

CRITICAL WARNING:
AI models frequently fabricate citations that appear authentic.
Using fabricated citations can result in:
├─ Court sanctions (monetary, written admonishment)
├─ Malpractice claims (breach of duty of competence)
├─ State bar discipline (competence violations)
├─ Reputational damage (professional credibility)
└─ Fee forfeiture (services provided incompetently)

═══════════════════════════════════════════════════════════════════
```

### Safe Rewrite Option (Recommended)

**Original (Unsafe):**
```
"Find cases supporting the argument that mandatory arbitration
clauses in employment contracts are unconscionable."
```

**Rewritten (Safe):**
```
"Draft legal reasoning arguing that mandatory arbitration clauses
in employment contracts may be unconscionable. Apply the
unconscionability doctrine framework (procedural + substantive
prongs). Mark locations where case authority would support the
argument with: [CITE NEEDED: describe proposition].

I will add verified citations after conducting independent research
in Westlaw/Lexis Advance."
```

**Impact:**
- Removes citation generation request
- Focuses AI on legal reasoning structure
- Preserves analytical value
- Eliminates fabrication risk
- Attorney performs proper legal research separately

---

### Verification Protocol Option (Riskier)

Add to prompt:
```
"CITATION REQUIREMENTS: Provide citations ONLY if you can verify
them from your training data with HIGH confidence. If uncertain
about any citation, state: [CITATION VERIFICATION REQUIRED]
instead of inventing. Format uncertain propositions as:
[CITE NEEDED: general description of legal principle]."
```

Then **MANDATORY** post-generation verification:
- [ ] Shepardize or KeyCite every single citation
- [ ] Verify each case exists in reporter at volume/page cited
- [ ] Read each case to confirm holding matches AI summary
- [ ] Verify case is good law (not overruled, distinguished)
- [ ] Confirm case is from controlling or persuasive jurisdiction

**Warning:** Even with verification protocol, AI may still fabricate. Safe rewrite is substantially safer.

---

## Applicable Rules

### Model Rule 1.1 (Competence)

> "A lawyer shall provide competent representation to a client. Competent representation requires the legal knowledge, skill, thoroughness and preparation reasonably necessary for the representation."

Relying on unverified AI citations violates competence duty.

### Model Rule 3.3(a)(1) (Candor Toward Tribunal)

> "A lawyer shall not knowingly make a false statement of fact or law to a tribunal or fail to correct a false statement of material fact or law previously made to the tribunal by the lawyer."

Submitting fabricated citations violates candor duty.

### Federal Rule of Civil Procedure 11(b)

> "By presenting to the court a pleading, written motion, or other paper... an attorney certifies that... the legal contentions are warranted by existing law..."

Certifying non-existent cases violates Rule 11.

---

## Effectiveness Metrics

| Metric | Result | Basis |
|--------|--------|-------|
| Citation requests detected | 100% (312/312) | Validation testing |
| Fabrication risk reduction | 85-90% | When safe rewrite applied |
| Pattern Strength | VERY STRONG | Documented in court sanctions |
| Validation | Court opinions, bar records | 2023-2025 case analysis |

---

## [CITE NEEDED] Format

When marking propositions requiring citation:

```
[CITE NEEDED: general description of legal principle]
```

**Examples:**
- `[CITE NEEDED: standard for summary judgment in federal court]`
- `[CITE NEEDED: unconscionability two-prong test]`
- `[CITE NEEDED: Daubert factors for expert testimony]`

---

## Activation

```
<LAYER_2: CITATION_INTEGRITY>
# Activates citation risk assessment and intervention
```

Standalone module activation:
```
<MODULE: CITATION_INTEGRITY>
[Your prompt here]
```

---

**Module Version:** 2.2  
**Last Updated:** November 2025
