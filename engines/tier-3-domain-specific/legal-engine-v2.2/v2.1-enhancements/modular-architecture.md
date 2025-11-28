# v2.1 Enhancement: Modular Architecture Update (MAU)

**Enhancement Type:** System Architecture  
**Purpose:** Enable selective execution of individual safety layers

---

## Overview

The Modular Architecture Update (MAU) allows selective execution of legal-safety layers instead of forcing all layers to run. This enables targeted interventions for specific use cases.

---

## Available Modules

Each module can be called independently:

| Module ID | Layer | Function |
|-----------|-------|----------|
| `PII_DETECTION` | Layer 1 | Detect and redact confidential information |
| `CITATION_INTEGRITY` | Layer 2 | Prevent citation fabrication |
| `VALIDATION_GATE` | Layer 3 | Remove absolute language, add qualifiers |
| `ETHICAL_BOUNDARY` | Layer 4 | Enforce Model Rules compliance |
| `LEGAL_PRECISION` | Layer 5 | Elevate vocabulary, apply Bluebook |
| `VERIFICATION_PROTOCOL` | Layer 6 | Inject verification requirements |
| `AUDIT_TRAIL` | Layer 7 | Generate malpractice defense documentation |
| `EPISTEMIC_TRANSPARENCY` | Meta-Layer | Inject uncertainty quantification |

---

## Single Module Activation

```
<MODULE: PII_DETECTION>
[Your prompt here]
```

```
<MODULE: CITATION_INTEGRITY>
[Your prompt here]
```

```
<MODULE: ETHICAL_BOUNDARY>
[Your prompt here]
```

---

## Multi-Module Activation

Combine specific modules:

```
<MODULES: PII_DETECTION, CITATION_INTEGRITY>
[Your prompt here]
```

```
<MODULES: VALIDATION_GATE, LEGAL_PRECISION, VERIFICATION_PROTOCOL>
[Your prompt here]
```

---

## Full Engine Activation

Run all modules (equivalent to standard Legal Engine v2.2):

```
<ENGINE: LEGAL_v2.1>
[Your prompt here]
```

Or explicitly:
```
<MODULES: ALL>
[Your prompt here]
```

---

## Module Combinations by Use Case

### Quick Confidentiality Check

For scanning a prompt for PII before submission:

```
<MODULE: PII_DETECTION>
[Prompt to scan]
```

Output: PII detection report only

---

### Citation Risk Assessment

For evaluating citation fabrication risk:

```
<MODULE: CITATION_INTEGRITY>
[Legal research prompt]
```

Output: Risk level and rewrite recommendations

---

### Brief Writing Support

For drafting legal briefs:

```
<MODULES: CITATION_INTEGRITY, LEGAL_PRECISION, VERIFICATION_PROTOCOL>
<DOCUMENT_TYPE: APPELLATE_BRIEF>
[Drafting prompt]
```

Output: Precision-enhanced analysis with citation markers and verification

---

### Client Communication

For drafting client letters:

```
<MODULES: PII_DETECTION, ETHICAL_BOUNDARY, LEGAL_PRECISION>
<DOCUMENT_TYPE: CLIENT_LETTER>
[Client communication prompt]
```

Output: Plain English with confidentiality protection

---

### Ethics Check Only

For evaluating ethical boundaries:

```
<MODULE: ETHICAL_BOUNDARY>
[Prompt to evaluate]
```

Output: Model Rules analysis and any concerns

---

### Audit Documentation

For generating audit trails on demand:

```
<MODULE: AUDIT_TRAIL>
<INCLUDE: [prior session ID]>
```

Output: Full audit trail for specified session

---

## Module Dependencies

Some modules work best together:

| Primary Module | Recommended Companions |
|----------------|----------------------|
| CITATION_INTEGRITY | VALIDATION_GATE, VERIFICATION_PROTOCOL |
| LEGAL_PRECISION | VALIDATION_GATE |
| ETHICAL_BOUNDARY | PII_DETECTION |
| VERIFICATION_PROTOCOL | CITATION_INTEGRITY |

---

## Module Processing Order

When multiple modules are activated, they execute in layer order:

```
1. META-LAYER: EPISTEMIC_TRANSPARENCY (if included)
2. LAYER 1: PII_DETECTION (if included)
3. LAYER 2: CITATION_INTEGRITY (if included)
4. LAYER 3: VALIDATION_GATE (if included)
5. LAYER 4: ETHICAL_BOUNDARY (if included)
6. LAYER 5: LEGAL_PRECISION (if included)
7. LAYER 6: VERIFICATION_PROTOCOL (if included)
8. LAYER 7: AUDIT_TRAIL (if included)
```

---

## Minimum Recommended Modules

For any legal work product, minimum recommended:

```
<MODULES: CITATION_INTEGRITY, VALIDATION_GATE, VERIFICATION_PROTOCOL>
```

These provide:
- Citation fabrication prevention
- Epistemic humility
- Verification requirements

---

## API/Integration Syntax

For programmatic use:

```json
{
  "engine": "LEGAL_v2.1",
  "modules": ["PII_DETECTION", "CITATION_INTEGRITY", "VERIFICATION_PROTOCOL"],
  "document_type": "TRIAL_MOTION",
  "prompt": "..."
}
```

---

## Performance Considerations

| Configuration | Processing Time | Thoroughness |
|---------------|-----------------|--------------|
| Single module | Fastest | Targeted |
| 3-4 modules | Fast | Balanced |
| All modules | Standard | Comprehensive |
| Full engine + audit | Slowest | Maximum protection |

---

## Error Handling

If an invalid module is specified:

```
⚠️ MODULE ERROR: [invalid_module] not recognized.

Available modules:
- PII_DETECTION
- CITATION_INTEGRITY
- VALIDATION_GATE
- ETHICAL_BOUNDARY
- LEGAL_PRECISION
- VERIFICATION_PROTOCOL
- AUDIT_TRAIL
- EPISTEMIC_TRANSPARENCY

Use <MODULES: [valid_module1], [valid_module2]> syntax.
```

---

**Enhancement Version:** 2.2  
**Last Updated:** November 2025
