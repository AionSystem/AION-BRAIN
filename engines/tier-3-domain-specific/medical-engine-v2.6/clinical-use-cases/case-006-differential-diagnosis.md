# Case 006: Differential Diagnosis Completeness

**Module Demonstrated:** Differential Diagnosis Validator (DDV-v1.0)  
**Scenario:** Ensuring complete differential with "can't miss" diagnoses

---

## Clinical Scenario

A 48-year-old male presents to the emergency department with sudden onset severe headache that he describes as "the worst headache of my life."

### Query to Medical Engine

```
48yo male, sudden onset severe headache, "worst headache of my life."
Started 2 hours ago while exercising. No prior history of migraines.
What's the differential diagnosis?
```

---

## Medical Engine v2.6 Processing

### Smart Prompt Parser (SPP) Extraction

```json
{
  "patient": {
    "age": 48,
    "sex": "male"
  },
  "chief_complaint": {
    "symptom": "headache",
    "severity": "worst of life",
    "onset": "sudden",
    "duration": "2 hours",
    "trigger": "exercise"
  },
  "history": {
    "prior_migraines": false
  },
  "query_type": "DIAGNOSIS"
}
```

### CRF-A + DDV Module Activation

```
RED FLAG DETECTED
├─ Pattern: "Worst headache of life" + sudden onset
├─ Match: Possible subarachnoid hemorrhage
├─ Urgency: CRITICAL

DDV ENGAGED
├─ Requiring complete differential
├─ "Can't miss" diagnoses mandatory
├─ Stratification required
```

---

## Medical Engine Response

```
═══════════════════════════════════════════════════════════════
📋 MEDICAL ENGINE v2.5 — DIFFERENTIAL DIAGNOSIS
═══════════════════════════════════════════════════════════════

PATIENT: 48-year-old male
PRESENTATION: Sudden onset "worst headache of life" during exercise
ONSET: 2 hours ago
HISTORY: No prior migraines

CONFIDENCE: HIGH
EVIDENCE LEVEL: I-II (Society guidelines, meta-analyses)

═══════════════════════════════════════════════════════════════
🚨 CRITICAL RED FLAG
═══════════════════════════════════════════════════════════════

"Worst headache of life" + sudden onset = 
SUBARACHNOID HEMORRHAGE UNTIL PROVEN OTHERWISE

This presentation warrants emergent workup regardless of
neurological exam findings.

═══════════════════════════════════════════════════════════════
📋 COMPLETE DIFFERENTIAL DIAGNOSIS
═══════════════════════════════════════════════════════════════

STRATIFICATION KEY:
🚨 = Can't miss (life-threatening)
⚠️ = Urgent consideration
📌 = Common/important

───────────────────────────────────────────────────────────────
🚨 CAN'T MISS DIAGNOSES (Must be excluded)
───────────────────────────────────────────────────────────────

1. SUBARACHNOID HEMORRHAGE (SAH) — MOST LIKELY
   ├─ Prevalence: ~1% of headaches, but ~25% of "thunderclap"
   ├─ Supporting: Sudden onset, worst of life, exercise trigger
   ├─ Opposing: None in this presentation
   ├─ Key test: CT head → LP if CT negative
   ├─ Sensitivity: CT 95% at 6h, 58% at 5 days
   └─ Miss rate consequence: 30-day mortality 40-50%

2. CEREBRAL VENOUS THROMBOSIS
   ├─ Prevalence: Rare but underdiagnosed
   ├─ Supporting: Headache can be thunderclap-like
   ├─ Opposing: More common in women, prothrombotic states
   ├─ Key test: CT/MR venography
   └─ Miss rate consequence: Venous infarction, hemorrhage

3. CERVICAL ARTERY DISSECTION
   ├─ Prevalence: ~2% of ischemic strokes
   ├─ Supporting: Can present with headache, especially occipital
   ├─ Opposing: Usually associated with neck pain
   ├─ Key test: CTA/MRA neck
   └─ Miss rate consequence: Stroke

4. INTRACEREBRAL HEMORRHAGE
   ├─ Prevalence: 10-15% of strokes
   ├─ Supporting: Sudden headache
   ├─ Opposing: Usually focal neurological signs
   ├─ Key test: CT head
   └─ Miss rate consequence: Herniation, death

5. PITUITARY APOPLEXY
   ├─ Prevalence: Rare
   ├─ Supporting: Sudden severe headache
   ├─ Opposing: Usually visual symptoms, known adenoma
   ├─ Key test: MRI pituitary
   └─ Miss rate consequence: Panhypopituitarism, death

6. HYPERTENSIVE EMERGENCY
   ├─ Prevalence: Common
   ├─ Supporting: Exercise trigger
   ├─ Check: Blood pressure (if >180/120 with symptoms)
   ├─ Key test: BP measurement, organ damage workup
   └─ Miss rate consequence: Stroke, MI, renal failure

───────────────────────────────────────────────────────────────
⚠️ URGENT CONSIDERATIONS
───────────────────────────────────────────────────────────────

7. REVERSIBLE CEREBRAL VASOCONSTRICTION SYNDROME (RCVS)
   ├─ Prevalence: Increasingly recognized
   ├─ Supporting: Thunderclap headache, exercise trigger
   ├─ Associated: Vasoactive substances, postpartum
   ├─ Key test: CTA/MRA, may be normal initially
   └─ Course: Recurrent thunderclap headaches over days

8. ACUTE ANGLE-CLOSURE GLAUCOMA
   ├─ Prevalence: 1 in 1000
   ├─ Supporting: Severe headache/eye pain
   ├─ Check: Eye redness, fixed mid-dilated pupil, vision
   ├─ Key test: Tonometry, slit lamp
   └─ Miss rate consequence: Permanent vision loss

───────────────────────────────────────────────────────────────
📌 OTHER CONSIDERATIONS
───────────────────────────────────────────────────────────────

9. PRIMARY EXERTIONAL HEADACHE
   ├─ Prevalence: 1-12% of headache patients
   ├─ Supporting: Exercise trigger
   ├─ Diagnosis of exclusion: Only after ruling out SAH
   └─ Note: First episode MUST exclude secondary causes

10. PRIMARY THUNDERCLAP HEADACHE
    ├─ Prevalence: Rare
    ├─ Diagnosis of exclusion only
    └─ Note: Must exclude all secondary causes first

═══════════════════════════════════════════════════════════════
🔬 RECOMMENDED WORKUP
═══════════════════════════════════════════════════════════════

IMMEDIATE (ED):
1. Non-contrast CT head
   ├─ Sensitivity for SAH: ~95% at 6 hours
   └─ Order STAT

2. IF CT NEGATIVE → Lumbar puncture
   ├─ Look for: Xanthochromia, RBCs in all tubes
   ├─ Timing: Wait 6-12 hours post-onset if possible
   └─ Essential to rule out SAH

3. Blood pressure measurement

4. Basic labs: CBC, BMP, coagulation studies

IF INITIAL WORKUP NEGATIVE BUT HIGH SUSPICION:
├─ CTA head/neck (aneurysm, dissection, RCVS)
├─ MRI brain with MRA
└─ Consider MRV if CVT suspected

═══════════════════════════════════════════════════════════════
✓ DDV VALIDATION
═══════════════════════════════════════════════════════════════

DIFFERENTIAL COUNT: 10 diagnoses ✓ (minimum 3)
CAN'T MISS INCLUDED: 6 life-threatening ✓
STRATIFICATION: Complete ✓
DISTINGUISHING FEATURES: Included ✓
WORKUP GUIDANCE: Provided ✓

VALIDATION STATUS: COMPLETE

═══════════════════════════════════════════════════════════════
⚠️ CLINICAL PEARL
═══════════════════════════════════════════════════════════════

"The sensitivity of clinical gestalt for SAH is only ~50%.
A normal neurological exam does NOT rule out SAH.
The workup (CT ± LP) must be completed."

— Ottawa SAH Rule and subsequent validation studies

═══════════════════════════════════════════════════════════════
✓ VERIFICATION REQUIRED
═══════════════════════════════════════════════════════════════

□ CT head ordered and interpreted
□ LP performed if CT negative
□ All can't-miss diagnoses considered
□ Workup documented
□ Follow-up plan if discharged
□ Provider sign-off

═══════════════════════════════════════════════════════════════
📝 AUDIT TRAIL
═══════════════════════════════════════════════════════════════

Timestamp: 2025-11-25T16:30:00Z
Modules: SPP, CRF-A, DDV activated
Red flag: Thunderclap headache
Differentials: 10 (6 can't-miss)
Validation: COMPLETE

═══════════════════════════════════════════════════════════════
```

---

## Why This Case Matters

### Thunderclap Headache is High Stakes

- 25% of "worst headache of life" presentations are SAH
- SAH has 40-50% mortality if missed
- Clinical exam alone misses ~50% of cases

### Medical Engine Protections

1. **Automatic red flag detection** - Recognizes thunderclap pattern
2. **Can't miss enforcement** - All life-threatening causes listed
3. **Stratified differential** - Organized by urgency
4. **Workup guidance** - Step-by-step testing protocol

### Without Medical Engine

A provider might:
- Focus only on migraine or tension headache
- Rely too heavily on normal neurological exam
- Miss LP requirement if CT is negative
- Not consider RCVS, CVT, or other rare causes

### With Medical Engine

- SAH prioritized as "until proven otherwise"
- Complete can't-miss list (6 life-threatening causes)
- Clear CT → LP protocol
- Clinical pearl about exam limitations

---

## DDV Validation Results

| Requirement | Result |
|-------------|--------|
| Minimum 3 diagnoses | 10 (passed) |
| Can't miss included | 6 (passed) |
| Stratification | Complete (passed) |
| Workup guidance | Provided (passed) |

---

**Case Version:** 1.0  
**Last Updated:** November 2025
