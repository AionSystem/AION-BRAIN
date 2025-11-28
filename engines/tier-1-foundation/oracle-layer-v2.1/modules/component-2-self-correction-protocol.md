# Component 2: Self-Correction Protocol

## Purpose

Instructions that tell AI how to catch its own mistakes MID-RESPONSE, not just at the end.

## Core Principle

The AI monitors itself during generation, applying checkpoints to catch errors before they propagate.

---

## Implementation Template

```xml
<SELF_CORRECTION_PROTOCOL>
As you generate your response, monitor for these error patterns:

CHECKPOINT 1: After Each Factual Claim
├─ STOP and ask: "Do I have a verified source for this?"
├─ IF YES: Cite it immediately → [SOURCE:identifier]
├─ IF NO: Mark [VERIFY_REQUIRED] OR use fail_response
└─ NEVER proceed with unverified claims

CHECKPOINT 2: After Each Citation
├─ VERIFY: Does this reference appear in my training data?
├─ VERIFY: Can I recall specific details (year, source, holding)?
├─ IF UNCERTAIN (even slightly): Mark [VERIFY_REQUIRED:human_review]
└─ FABRICATION RED FLAGS:
   • Made-up reference numbers (e.g., "789 F.3d")
   • Generic names without clear memory
   • Suspiciously perfect fact patterns

CHECKPOINT 3: After Each Paragraph
├─ COUNT: How many [VERIFY_REQUIRED] tags did I add?
├─ IF ≥ 3: Consider using fail_response instead (too uncertain)
├─ RE-READ: Does my response answer the actual question?
└─ VERIFY: Are all claims properly qualified?

CHECKPOINT 4: Before Finalizing Response
├─ SCAN: Any absolute language that should be qualified?
├─ CHECK: Have I acknowledged limitations appropriately?
├─ VERIFY: Does conclusion follow from verified premises?
└─ CONFIRM: Would I stand behind this if audited?

</SELF_CORRECTION_PROTOCOL>
```

---

## Checkpoint Types

### Factual Claim Checkpoint

```
[FACTUAL_CLAIM_CHECK]
├─ Claim: "[claim text]"
├─ Source Available: [YES | NO | UNCERTAIN]
├─ Source Quality: [HIGH | MEDIUM | LOW | UNKNOWN]
├─ Action: [CITE | VERIFY_REQUIRED | FAIL_RESPONSE]
└─ Result: [claim with appropriate marking]
```

### Citation Checkpoint

```
[CITATION_CHECK]
├─ Citation: "[full citation]"
├─ Recall Confidence: [0.00-1.00]
├─ Details Verified:
│   ├─ Year: [YES | NO | UNCERTAIN]
│   ├─ Source: [YES | NO | UNCERTAIN]
│   ├─ Holding: [YES | NO | UNCERTAIN]
│   └─ Parties: [YES | NO | UNCERTAIN]
├─ Fabrication Flags: [NONE | RED_FLAG detected]
└─ Action: [KEEP | VERIFY_REQUIRED | REMOVE]
```

### Quantifier Checkpoint

```
[QUANTIFIER_CHECK]
├─ Statement: "[statement with quantifier]"
├─ Quantifier Used: [always | never | all | none | most | etc.]
├─ Evidence Supports Quantifier: [YES | NO | PARTIALLY]
├─ Suggested Correction: [qualified version]
└─ Action: [KEEP | QUALIFY | REWRITE]
```

---

## Error Pattern Recognition

### Fabrication Patterns

| Pattern | Description | Action |
|---------|-------------|--------|
| Made-up numbers | Reference volumes/pages with no memory | Mark [VERIFY_REQUIRED] |
| Generic names | "Johnson v. Smith" without specifics | Mark [VERIFY_REQUIRED] |
| Perfect fit | Facts too conveniently matching query | Increase scrutiny |
| Confident gaps | High confidence but missing details | Reduce confidence |

### Overgeneralization Patterns

| Pattern | Description | Action |
|---------|-------------|--------|
| "Always" claims | Universal without evidence | Qualify with "typically" |
| "Never" claims | Absolute negative | Qualify with "rarely" |
| Blanket rules | No exceptions mentioned | Add exception clause |
| Definitive without source | "The law states..." | Add source or qualify |

### Logical Error Patterns

| Pattern | Description | Action |
|---------|-------------|--------|
| Non sequitur | Conclusion doesn't follow | Strengthen reasoning chain |
| Missing premises | Hidden assumptions | Make explicit |
| Circular reasoning | Premise = conclusion | Break circularity |
| False dichotomy | Only two options presented | Add alternatives |

---

## Correction Actions

### Mark for Verification

```
[VERIFY_REQUIRED:human_review]
Claim: "[claim text]"
Reason: [why verification needed]
Suggested verification: [how to verify]
```

### Qualify Claim

```
Original: "This always applies"
Corrected: "This typically applies in [context], though exceptions exist"
Qualification: Added scope and exception acknowledgment
```

### Fail Response

```
[FAIL_RESPONSE]
Original query: "[what was asked]"
Reason for failure: [why cannot provide reliable answer]
Recommendation: "[alternative action or resource]"
```

### Reduce Confidence

```
Original confidence: 0.90
Reduced confidence: 0.65
Reason: [what triggered reduction]
New output: Claim [CONFIDENCE:0.65 ±0.15]
```

---

## Checkpoint Frequency

| Content Type | Checkpoint Frequency |
|--------------|---------------------|
| Factual claims | After each claim |
| Citations | After each citation |
| Paragraphs | After each paragraph |
| Final review | Before output |
| High-stakes content | Double-check all |

---

## Integration with Other Components

| Component | Integration |
|-----------|-------------|
| AI Language Glossary | Uses constructs defined there |
| Reasoning Traces | Checkpoints appear in traces |
| Failure Handling | Triggers failure protocols |
| Formal Verification | Checkpoints enforce axioms |

---

## Best Practices

1. **Don't Skip Checkpoints** — Even when confident, run checks
2. **Err Toward Caution** — When uncertain, mark for verification
3. **Show Your Work** — Make checkpoint results visible when relevant
4. **Learn From Catches** — Adjust downstream content based on catches
5. **Accept Failure** — Using fail_response is success, not failure
