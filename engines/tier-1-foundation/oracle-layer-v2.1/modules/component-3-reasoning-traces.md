# Component 3: Reasoning Traces

## Purpose

Show the AI's thought process transparently, enabling verification and building trust through visible reasoning.

## Core Principle

Every significant conclusion should have a visible reasoning chain that humans can audit.

---

## Implementation Template

```xml
<REASONING_TRACE_PROTOCOL>
For each significant decision, show your reasoning:

[REASONING_STEP_1]
├─ INPUT: [What information am I processing?]
├─ ANALYSIS: [How am I evaluating this?]
├─ CONCLUSION: [What did I determine?]
└─ CONFIDENCE: [0.00-1.00]

[REASONING_STEP_2]
├─ INPUT: [Building on Step 1...]
├─ ANALYSIS: [Further evaluation...]
├─ CONCLUSION: [Refined determination...]
└─ CONFIDENCE: [0.00-1.00]

[FINAL_SYNTHESIS]
├─ COMBINED_REASONING: [How steps connect]
├─ FINAL_CONCLUSION: [Overall answer]
├─ TOTAL_CONFIDENCE: [Aggregate score]
└─ UNCERTAINTY_SOURCES: [What reduces confidence]

</REASONING_TRACE_PROTOCOL>
```

---

## Trace Levels

### Level 1: Minimal Trace

For simple, low-stakes responses:

```
[REASONING]: Verified X through Y, confidence 0.85
[CONCLUSION]: Answer is Z
```

### Level 2: Standard Trace

For moderate complexity:

```
[REASONING_STEP_1]
├─ Input: User query about [topic]
├─ Analysis: Identified key factors [A, B, C]
├─ Conclusion: Focus on factor B (most relevant)
└─ Confidence: 0.80

[REASONING_STEP_2]
├─ Input: Factor B implications
├─ Analysis: Evidence suggests [outcome]
├─ Conclusion: [determination]
└─ Confidence: 0.75

[FINAL_SYNTHESIS]
├─ Combined: Steps 1→2 lead to conclusion
├─ Final: [answer]
├─ Confidence: 0.77 (geometric mean)
└─ Uncertainty: Limited data on edge cases
```

### Level 3: Full Trace

For high-stakes or complex queries:

```
[QUERY_ANALYSIS]
├─ Original Query: "[verbatim user query]"
├─ Interpreted As: "[restatement for clarity]"
├─ Key Requirements: [list]
├─ Scope Boundaries: [what's included/excluded]
└─ Complexity Assessment: [LOW | MEDIUM | HIGH]

[EVIDENCE_GATHERING]
├─ Source 1: [source identifier]
│   ├─ Relevance: [0.0-1.0]
│   ├─ Quality: [HIGH | MEDIUM | LOW]
│   └─ Key Finding: [summary]
├─ Source 2: [source identifier]
│   ├─ Relevance: [0.0-1.0]
│   ├─ Quality: [HIGH | MEDIUM | LOW]
│   └─ Key Finding: [summary]
└─ Evidence Summary: [N] sources, average quality [X]

[REASONING_CHAIN]
├─ Premise 1: [statement] [SOURCE:X]
├─ Premise 2: [statement] [SOURCE:Y]
├─ Inference 1: From P1 + P2 → [intermediate conclusion]
├─ Premise 3: [statement] [SOURCE:Z]
├─ Inference 2: From I1 + P3 → [refined conclusion]
└─ Final Inference: [conclusion]

[CONFIDENCE_COMPUTATION]
├─ Evidence Strength: [0.00-1.00]
├─ Reasoning Validity: [0.00-1.00]
├─ Source Agreement: [0.00-1.00]
├─ Combined Confidence: [0.00-1.00]
└─ Confidence Interval: ±[X]%

[UNCERTAINTY_ANALYSIS]
├─ Known Unknowns: [what we know we don't know]
├─ Potential Unknowns: [what might be missing]
├─ Sensitivity: [what would change the conclusion]
└─ Robustness: [how stable is the conclusion]

[FINAL_OUTPUT]
├─ Conclusion: [answer]
├─ Confidence: [score] ±[interval]
├─ Caveats: [important qualifications]
└─ Verification Recommendation: [what human should check]
```

---

## Formal Proof Certificate

For claims requiring formal verification:

```
═══════════════════════════════════════════════════════════════════
FORMAL VERIFICATION REPORT
Generated: [ISO8601_timestamp]
Architect: [attribution]
═══════════════════════════════════════════════════════════════════

VERIFICATION SUMMARY:
├─ Total Claims Evaluated: [N]
├─ Verified Claims (confidence ≥ 0.80): [N_verified] ([percentage]%)
├─ Unverified (flagged): [N_unverified] ([percentage]%)
├─ Fabrications Detected: 0 ✅ (Axiom 1 satisfied)
└─ Invariants Maintained: [Y/N]

PROOF CHAIN:
[For each major claim, proof obligation fulfilled]

AUDIT CERTIFICATION:
This response was generated with formal verification protocol v2.0.
All claims below verification threshold are explicitly marked.
═══════════════════════════════════════════════════════════════════
```

---

## When to Use Each Level

| Scenario | Trace Level | Rationale |
|----------|-------------|-----------|
| Simple factual query | Level 1 | Low complexity, low risk |
| Analysis or opinion | Level 2 | Moderate complexity |
| High-stakes decision | Level 3 | Maximum transparency |
| Legal/medical/financial | Level 3 | Professional liability |
| Controversial topic | Level 3 | Need for auditability |
| Quick informal chat | Level 1 | Efficiency |

---

## Confidence Computation Methods

### Geometric Mean

```
confidence_combined = (c1 × c2 × ... × cn)^(1/n)
```

Use when all steps must hold for conclusion to hold.

### Weighted Average

```
confidence_combined = Σ(wi × ci) / Σ(wi)
```

Use when steps have different importance.

### Minimum (Conservative)

```
confidence_combined = min(c1, c2, ..., cn)
```

Use when chain is only as strong as weakest link.

---

## Integration with Other Components

| Component | Integration |
|-----------|-------------|
| Self-Correction | Checkpoint results appear in traces |
| Failure Handling | Failure decisions traced |
| Cross-Validation | Trinity perspectives in trace |
| Chain-of-Custody | Traces become audit evidence |

---

## Best Practices

1. **Match Level to Stakes** — Use appropriate trace depth
2. **Be Genuine** — Traces should reflect actual reasoning
3. **Show Uncertainty** — Don't hide doubt in traces
4. **Make Auditable** — Someone should be able to verify
5. **Include Sources** — Link evidence to conclusions
