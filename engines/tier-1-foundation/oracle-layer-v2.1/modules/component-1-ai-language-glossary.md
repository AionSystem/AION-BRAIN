# Component 1: Inline AI Language Glossary

## Purpose

Define specialized constructs within the prompt itself so any AI understands them without external documentation. The prompt becomes self-teaching.

## Core Principle

Instead of assuming AI knows what your tags mean, DEFINE THEM IN THE PROMPT.

---

## Implementation Template

```xml
<AI_LANGUAGE_GLOSSARY>
This prompt uses specialized constructs to control your behavior.
Here's what each means:

<fabrication:block>
├─ MEANING: You must NEVER invent facts, case names, statistics, or citations
├─ IF you don't have verified information → Use fail_response instead
├─ VIOLATION EXAMPLE: Making up "Johnson v. Smith, 789 F.3d 123"
└─ CORRECT BEHAVIOR: "NO VERIFIED PRECEDENT FOUND" (honest admission)

<source_verification:required>
├─ MEANING: Every factual claim MUST cite a real source
├─ ACCEPTABLE SOURCES: PubMed, FDA.gov, official reporters, etc.
├─ FORMAT: [CLAIM]: [SOURCE:specific_identifier]
└─ IF NO SOURCE: Mark as [VERIFY_REQUIRED:human_review]

<fail_response:"exact text">
├─ MEANING: If conditions not met, output EXACTLY this text (don't paraphrase)
├─ TRIGGERS: No verified sources found, ambiguous query, safety concern
├─ PURPOSE: Honest admission of limitations
└─ EXAMPLE: "NO CONTROLLING PRECEDENT FOUND"

<confidence:threshold>
├─ MEANING: Minimum confidence required to output claim
├─ DEFAULT: 0.80 (80% confidence)
├─ BELOW THRESHOLD: Mark [VERIFY_REQUIRED] or use fail_response
└─ FORMAT: [CONFIDENCE:0.85] attached to claims

[CITE], [HOLDING], [FACT_MATCH]
├─ MEANING: Output structure markers (where to put specific info)
├─ [CITE]: Full citation in proper format
├─ [HOLDING]: One-sentence decision/conclusion
└─ [FACT_MATCH]: Percentage of factual overlap (estimate if needed)

</AI_LANGUAGE_GLOSSARY>
```

---

## Standard Constructs Library

### Verification Constructs

| Construct | Meaning | Usage |
|-----------|---------|-------|
| `<fabrication:block>` | Never invent information | Critical for factual queries |
| `<source_verification:required>` | Every claim needs source | Research, legal, medical |
| `<source_verification:preferred>` | Sources preferred not required | General queries |
| `<confidence:0.XX>` | Minimum confidence threshold | Adjustable per use case |

### Output Structure Constructs

| Construct | Meaning | Usage |
|-----------|---------|-------|
| `[CITE]` | Full citation placeholder | Legal, academic, medical |
| `[HOLDING]` | Core conclusion/decision | Legal, analytical |
| `[FACT_MATCH]` | Factual similarity percentage | Case comparison |
| `[VERIFY_REQUIRED]` | Needs human verification | Uncertain claims |
| `[CONFIDENCE:X.XX]` | Confidence score attachment | All claims |

### Failure Constructs

| Construct | Meaning | Usage |
|-----------|---------|-------|
| `<fail_response:"text">` | Exact text to output on failure | Graceful degradation |
| `[SCOPE_LIMITATION]` | Query exceeds capabilities | Honest admission |
| `[SAFETY_FLAG]` | High-stakes caution needed | Risk awareness |

---

## Domain-Specific Glossaries

### Legal Domain Addition

```xml
<LEGAL_GLOSSARY>
[BLUEBOOK]: Citation follows Bluebook 21st Edition format
[HOLDING]: One-sentence court ruling
[DICTA]: Non-binding observation
[DISTINGUISH]: Factual difference from precedent
[OVERRULED]: Precedent no longer valid
</LEGAL_GLOSSARY>
```

### Medical Domain Addition

```xml
<MEDICAL_GLOSSARY>
[LEVEL_OF_EVIDENCE]: Oxford CEBM level (1a-5)
[GRADE]: Recommendation strength (A/B/C/D)
[BLACK_BOX]: FDA highest warning level
[CONTRAINDICATED]: Must not use
[OFF_LABEL]: Not FDA approved for this use
</MEDICAL_GLOSSARY>
```

### Financial Domain Addition

```xml
<FINANCIAL_GLOSSARY>
[FORWARD_LOOKING]: Not guaranteed, involves risk
[HISTORICAL]: Past performance data
[PROJECTION]: Estimate, not prediction
[REGULATORY]: Subject to compliance requirements
</FINANCIAL_GLOSSARY>
```

---

## Benefits

| Benefit | Description |
|---------|-------------|
| **Portability** | Any AI reading prompt understands constructs |
| **Self-Teaching** | User learns AI language by reading prompt |
| **Reduced Misinterpretation** | AI knows exactly what you want |
| **Self-Documenting** | Prompt explains itself |
| **Standardization** | Consistent vocabulary across uses |

---

## Best Practices

1. **Define Before Use** — Always place glossary before construct usage
2. **Be Explicit** — Include violation examples and correct behavior
3. **Domain-Specific** — Add domain glossary for specialized use
4. **Minimal Set** — Only define constructs you'll actually use
5. **Clear Examples** — Show what compliance and violation look like

---

## Integration Note

AI Language Glossary is the foundation for all other Oracle Layer components. Define constructs first, then reference them in Self-Correction Protocol, Reasoning Traces, and Failure Handling.
