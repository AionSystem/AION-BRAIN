# v2.1 Enhancement: Compact Runtime Mode (CRM)

**Enhancement Type:** Operational Mode  
**Purpose:** Run core engine using condensed instruction set

---

## Overview

Compact Runtime Mode (CRM) allows users to run the core Legal Engine without loading the full 50+ page system. It retains all critical safeguards while removing verbose explanations.

---

## Activation

```
<MODE: COMPACT_RUNTIME>
```

---

## Features

| Feature | Behavior |
|---------|----------|
| Verbose explanations | REMOVED |
| Compliance rules | RETAINED |
| Ethics safeguards | RETAINED |
| Citation integrity | RETAINED |
| Short-form output | ENABLED |
| Speed priority | ENABLED |

---

## Core Logic Preserved

Even in Compact Mode, these rules are non-negotiable:

1. **Hallucination Prevention**
   - No fabricated citations
   - [CITE NEEDED] markers required
   - Epistemic qualifiers applied

2. **Mandatory Citation Verification**
   - All citations require Shepardize/KeyCite
   - Verification checklist output

3. **Model Rules Compliance**
   - Ethical constraints enforced
   - Professional judgment preserved
   - Confidentiality protected

4. **Post-Generation Verification**
   - Verification requirements stated
   - Attorney sign-off reminder

---

## Compact Output Format

```
[CONFIDENCE LEVEL: HIGH/MODERATE/LOW]

[Concise legal analysis without layer explanations]

[CITE NEEDED: proposition 1]
[CITE NEEDED: proposition 2]

[VERIFICATION REQUIRED: 
- Shepardize all citations
- Confirm jurisdiction applies
- Apply professional judgment]
```

---

## Comparison: Full vs. Compact

| Aspect | Full Engine | Compact Runtime |
|--------|-------------|-----------------|
| Layer explanations | Detailed | Suppressed |
| Warning verbosity | Extended | Brief |
| Audit trail | Comprehensive | Condensed |
| Output length | Longer | Concise |
| Safeguards | All 8 layers | All 8 layers |
| Risk reduction | 75-85% | 75-85% |

---

## Use Cases

### Ideal For

- Routine legal research queries
- Quick analysis during drafting
- Experienced users familiar with safeguards
- High-volume query sessions
- Integration into workflows

### Not Ideal For

- First-time users (use full mode first)
- High-stakes matters (use full mode for audit trail)
- Training purposes (full mode explains better)
- Complex novel issues (need full context)

---

## Sample Prompt

```
<MODE: COMPACT_RUNTIME>

What are the elements of promissory estoppel?
```

## Sample Output

```
[CONFIDENCE LEVEL: HIGH]

Promissory estoppel generally requires:

1. Clear and unambiguous promise
2. Reasonable and foreseeable reliance by promisee
3. Actual reliance to promisee's detriment
4. Injustice can only be avoided by enforcement

[CITE NEEDED: Restatement (Second) of Contracts § 90]

Some jurisdictions require additional elements or have modified standards.

[VERIFICATION REQUIRED:
- Confirm elements in your jurisdiction
- Check for state-specific modifications
- Shepardize any cases used in application]
```

---

## Activation with Document Type

```
<MODE: COMPACT_RUNTIME>
<DOCUMENT_TYPE: CLIENT_LETTER>

[Your prompt here]
```

This combines compact output with plain English mode for client communications.

---

**Enhancement Version:** 2.2  
**Last Updated:** November 2025
