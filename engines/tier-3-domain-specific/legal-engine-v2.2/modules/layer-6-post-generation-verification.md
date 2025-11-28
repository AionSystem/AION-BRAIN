# LAYER 6: Post-Generation Verification Protocol

**Layer Position:** 6  
**Purpose:** Require mandatory verification before relying on AI output

---

## Function

Layer 6 injects mandatory verification checklists into AI outputs, ensuring attorneys complete due diligence before relying on or submitting AI-generated legal content.

---

## Verification Checklist

Every AI legal output includes this mandatory checklist:

```
═══════════════════════════════════════════════════════════════════
POST-GENERATION VERIFICATION — ATTORNEY REQUIRED
═══════════════════════════════════════════════════════════════════

Before relying on this analysis, you MUST verify:

CITATION VERIFICATION:
☐ Shepardize or KeyCite every case citation
☐ Verify each case exists in reporter at volume/page cited
☐ Read each case to confirm holding matches AI summary
☐ Verify case is good law (not overruled, distinguished)
☐ Confirm case is from controlling or persuasive jurisdiction

STATUTORY VERIFICATION:
☐ Check statute currency (not amended or repealed)
☐ Verify section numbers are correct
☐ Confirm effective dates
☐ Check for relevant regulations or agency guidance

LEGAL REASONING VERIFICATION:
☐ Review reasoning against treatises/hornbooks
☐ Verify elements of legal tests are complete
☐ Check for overlooked exceptions or defenses
☐ Confirm analysis applies to your jurisdiction

PROFESSIONAL JUDGMENT:
☐ Apply independent judgment to client's specific situation
☐ Consider facts AI doesn't know about
☐ Make strategic decisions yourself (don't delegate to AI)
☐ Evaluate risk tolerance and client preferences

FINAL REVIEW:
☐ Review as if you drafted it entirely yourself
☐ You are professionally responsible for every word
☐ Sign and date verification in audit trail

═══════════════════════════════════════════════════════════════════
```

---

## Shepardize/KeyCite Requirements

For every case citation, verify:

| Check | What to Look For |
|-------|------------------|
| Existence | Case exists at reporter/volume/page |
| Treatment | Positive, negative, distinguished, overruled |
| Currency | Still good law |
| History | Subsequent history (affirmed, reversed, etc.) |
| Citing References | How other courts have treated it |

### Red Flags

- **Overruled:** Case is no longer good law
- **Distinguished:** Courts have limited its application
- **Criticized:** Reasoning questioned by later courts
- **Superseded:** Statute or rule changed
- **Abrogated:** Later cases reject the reasoning

---

## Citation Verification Workflow

```
1. EXISTENCE CHECK
   └─ Search case name in Westlaw/Lexis
   └─ Verify reporter, volume, page
   └─ If not found: DO NOT USE

2. HOLDING CHECK
   └─ Read the actual case
   └─ Compare holding to AI summary
   └─ If different: CORRECT or REMOVE

3. TREATMENT CHECK
   └─ Shepardize (LexisNexis) or KeyCite (Westlaw)
   └─ Review negative treatment
   └─ If bad law: DO NOT USE

4. JURISDICTION CHECK
   └─ Confirm controlling or persuasive
   └─ Check for more recent authority in your jurisdiction
   └─ Note circuit or state variations

5. CURRENCY CHECK
   └─ Verify case hasn't been superseded
   └─ Check for legislative changes
   └─ Confirm current applicability
```

---

## Statutory Verification Workflow

```
1. CURRENCY CHECK
   └─ Verify statute hasn't been amended
   └─ Check effective dates
   └─ Look for recent session laws

2. SECTION CHECK
   └─ Confirm section numbers are correct
   └─ Verify subsection references
   └─ Check for renumbering

3. REGULATION CHECK
   └─ Look for implementing regulations
   └─ Check agency guidance documents
   └─ Review informal interpretations

4. CASE LAW CHECK
   └─ Find cases interpreting the statute
   └─ Check for circuit splits on interpretation
   └─ Verify AI's interpretation aligns with precedent
```

---

## Attorney Sign-Off Gate

Before finalizing any AI-assisted work product:

```
ATTORNEY CERTIFICATION

I, _________________________, Bar No. _____________, certify that:

☐ I have reviewed this AI-generated content in its entirety

☐ I have independently verified all legal citations using
  Shepard's or KeyCite

☐ I have read the cited cases and confirmed the holdings are
  accurately represented

☐ I have verified all statutes are current and correctly cited

☐ I have applied my independent professional judgment to the
  legal analysis

☐ I have considered client-specific facts and circumstances not
  reflected in the AI prompt

☐ I take full professional responsibility for this work product
  as if I had drafted it personally

☐ I understand that AI assistance does not diminish my duties
  under the Model Rules of Professional Conduct

Signature: ______________________ Date: _______________
```

---

## Verification Documentation

### For Matter File

```
VERIFICATION RECORD

Matter: [Matter number/name]
Document: [Description]
AI Tool Used: [Name/version]
Date Generated: [Date]
Date Verified: [Date]

CITATIONS VERIFIED:
├─ [Citation 1]: ✓ Verified [Date] via [Westlaw/Lexis]
├─ [Citation 2]: ✓ Verified [Date] via [Westlaw/Lexis]
└─ [Citation 3]: ✓ Verified [Date] via [Westlaw/Lexis]

STATUTES VERIFIED:
├─ [Statute 1]: ✓ Current as of [Date]
└─ [Statute 2]: ✓ Current as of [Date]

ATTORNEY REVIEW:
├─ Independent judgment applied: ✓
├─ Client-specific facts considered: ✓
└─ Full professional responsibility accepted: ✓

Attorney: _________________ Date: _________________
```

---

## Verification Reminders

Layer 6 adds reminders to AI output:

### For Citations

```
[VERIFICATION REQUIRED: Shepardize/KeyCite this citation before use]
```

### For Legal Propositions

```
[VERIFICATION REQUIRED: Confirm this rule applies in your jurisdiction]
```

### For Novel Issues

```
[VERIFICATION REQUIRED: This may involve unsettled law requiring
additional research]
```

### For Fact-Dependent Analysis

```
[VERIFICATION REQUIRED: This analysis depends on facts stated in prompt.
Verify facts and consider unstated circumstances.]
```

---

## Malpractice Defense Utility

Completed verification records may demonstrate:

- **Reasonable care standard met** — Attorney didn't blindly rely on AI
- **Due diligence performed** — Citations independently verified
- **Professional judgment preserved** — Attorney made final decisions
- **Model Rule compliance** — Supervision duties fulfilled

---

## Activation

```
<LAYER_6: POST_GENERATION_VERIFICATION>
# Activates verification checklist injection
```

Standalone module activation:
```
<MODULE: VERIFICATION_PROTOCOL>
[Your prompt here]
```

---

**Module Version:** 2.2  
**Last Updated:** November 2025
