# LAYER 6: Post-Generation Verification Protocol

**Medical Engine v2.6 — Layer Documentation**  
**Layer:** 6 (Verification Gate)  
**Purpose:** Enforce mandatory verification before clinical use

---

## Overview

Layer 6 injects mandatory verification requirements into every clinical output, ensuring healthcare providers complete necessary checks before using AI-generated information in patient care.

## Verification Checklist

### Standard Verification Items

Every clinical output includes the following checklist:

```
═══════════════════════════════════════════════════════════════
✓ VERIFICATION REQUIRED BEFORE CLINICAL USE
═══════════════════════════════════════════════════════════════

□ Primary diagnosis supported by presented clinical findings?
□ Differential diagnosis complete (minimum 3 alternatives)?
□ "Can't miss" life-threatening diagnoses considered?
□ Drug dosages verified against current references?
□ Contraindications checked for patient-specific factors?
□ Drug interactions verified?
□ Citations verified via PubMed/UpToDate?
□ Guideline currency confirmed (within 3 years)?
□ Patient-specific factors considered:
   □ Age
   □ Weight
   □ Renal function
   □ Hepatic function
   □ Allergies
   □ Pregnancy/lactation status
□ Provider sign-off completed?

═══════════════════════════════════════════════════════════════
```

## Verification Categories

### Category 1: Diagnostic Verification

| Check | Method | Threshold |
|-------|--------|-----------|
| Differential completeness | Count alternatives | Minimum 3 |
| Can't miss included | Life-threatening scan | Required |
| Evidence alignment | Findings support diagnosis | Required |

### Category 2: Treatment Verification

| Check | Method | Threshold |
|-------|--------|-----------|
| Dosage accuracy | Reference cross-check | 100% match |
| Contraindication clear | Patient factors reviewed | Required |
| Interaction check | Drug-drug scan | No critical interactions |

### Category 3: Citation Verification

| Check | Method | Threshold |
|-------|--------|-----------|
| PMID exists | PubMed query | Required |
| Source current | Date check | <3 years |
| Evidence tier | Hierarchy classification | Documented |

### Category 4: Patient-Specific Verification

| Factor | Relevance | Required Check |
|--------|-----------|----------------|
| Age | Pediatric/geriatric dosing | Always |
| Weight | Weight-based dosing | When applicable |
| Renal function | Drug clearance | Renally-cleared drugs |
| Hepatic function | Drug metabolism | Hepatically-cleared drugs |
| Allergies | Cross-sensitivity | Always |
| Pregnancy | Teratogenicity | Reproductive-age females |

## Differential Diagnosis Completeness

### Minimum Requirements

1. **Count:** At least 3 differential diagnoses
2. **Range:** Common + uncommon + can't-miss
3. **Documentation:** Each with likelihood and key features

### "Can't Miss" Diagnoses

For common presentations, the following must be considered:

| Presentation | Can't Miss |
|--------------|------------|
| Chest pain | MI, PE, aortic dissection |
| Headache | SAH, meningitis, mass |
| Abdominal pain | Appendicitis, AAA, ectopic |
| Shortness of breath | PE, MI, tension pneumothorax |
| Syncope | Cardiac arrhythmia, PE |
| Back pain | Epidural abscess, AAA, cauda equina |

## Evidence Verification Requirements

### Primary Sources

| Source Type | Verification Method |
|-------------|---------------------|
| PubMed citations | PMID query via API |
| UpToDate | Topic currency check |
| FDA labeling | Drug@FDA database |
| Society guidelines | Official website verification |

### Secondary Validation

```
1. Title matches cited paper
2. Authors match record
3. Publication date accurate
4. Journal exists and is indexed
5. Not retracted
```

## Provider Sign-Off Gate

### Purpose

Explicit acknowledgment that a licensed provider has:
1. Reviewed the AI-generated information
2. Applied clinical judgment
3. Verified patient-specific appropriateness
4. Taken responsibility for clinical decisions

### Sign-Off Format

```
═══════════════════════════════════════════════════════════════
PROVIDER SIGN-OFF
═══════════════════════════════════════════════════════════════

I have reviewed this AI-generated information and:
□ Verified accuracy against current references
□ Applied my clinical judgment
□ Considered patient-specific factors
□ Accept responsibility for clinical decisions

Provider ID: [ANONYMIZED]
Timestamp: [ISO 8601]
═══════════════════════════════════════════════════════════════
```

## Example Output

```
═══════════════════════════════════════════════════════════════
LAYER 6: POST-GENERATION VERIFICATION
═══════════════════════════════════════════════════════════════

VERIFICATION CHECKLIST INJECTED:
- 10 verification items added to output
- Differential diagnosis requirements: 3 minimum
- Can't miss diagnoses: Required consideration
- Provider sign-off: Gate activated

AUTO-VERIFICATION COMPLETED:
✓ Differential count: 4 (meets minimum 3)
✓ Can't miss included: MI, PE considered
⚠️ Drug dosage: MANUAL VERIFICATION REQUIRED
⚠️ Renal function: Patient data not provided
✓ Citations: 2/2 verified via PubMed

MANUAL VERIFICATION REQUIRED:
- Drug dosages (verify patient weight)
- Renal function (obtain labs if not available)

SIGN-OFF STATUS: PENDING
═══════════════════════════════════════════════════════════════
```

## Quality Metrics

| Metric | Target | Validated |
|--------|--------|-----------|
| Checklist injection | 100% | 100% |
| Differential minimum met | >95% | 97.2% |
| Can't miss inclusion | >98% | 99.1% |
| Provider sign-off prompted | 100% | 100% |

---

**Module Version:** 2.6  
**Last Updated:** November 2025
