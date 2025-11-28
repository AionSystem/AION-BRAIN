# Case 001: Pediatric Dosing Safety

**Module Demonstrated:** Pediatric Safety Sub-Module (PSS-v1.0)  
**Scenario:** Weight-based dosing verification for pediatric patient

---

## Clinical Scenario

A 4-year-old, 18 kg child presents to the pediatric urgent care with acute otitis media. The attending physician wants to prescribe amoxicillin.

### Query to Medical Engine

```
4 year old, 18 kg, acute otitis media. 
What is the appropriate amoxicillin dose?
```

---

## Medical Engine v2.6 Processing

### Smart Prompt Parser (SPP) Extraction

```json
{
  "patient": {
    "age": 4,
    "age_unit": "years",
    "weight": 18,
    "weight_unit": "kg",
    "age_stratum": "preschool"
  },
  "diagnosis": "acute otitis media",
  "query_type": "DOSING"
}
```

### PSS Module Activation

```
PEDIATRIC SAFETY CHECK INITIATED
├─ Age stratum: Preschool (3-5 years)
├─ Weight provided: 18 kg ✓
├─ Diagnosis: Acute otitis media
├─ Medication: Amoxicillin
```

---

## Medical Engine Response

```
═══════════════════════════════════════════════════════════════
📋 MEDICAL ENGINE v2.5 — PEDIATRIC DOSING
═══════════════════════════════════════════════════════════════

PATIENT: 4-year-old, 18 kg
DIAGNOSIS: Acute otitis media (AOM)
MEDICATION: Amoxicillin

CONFIDENCE: HIGH
EVIDENCE LEVEL: I (AAP/AAFP Guidelines 2013, updated)

═══════════════════════════════════════════════════════════════
💊 DOSING RECOMMENDATIONS
═══════════════════════════════════════════════════════════════

STANDARD DOSE AOM:
├─ Dose: 80-90 mg/kg/day divided BID
├─ Calculation: 18 kg × 80-90 mg/kg = 1440-1620 mg/day
├─ Recommended: 750 mg BID (1500 mg/day = 83 mg/kg/day)
├─ Duration: 10 days (age <2) or 5-7 days (age ≥2)
└─ For this patient (age 4): 5-7 days acceptable

FORMULATION:
├─ Suspension 400 mg/5 mL: 9.4 mL BID
├─ Suspension 250 mg/5 mL: 15 mL BID
├─ Chewable tablets 250 mg: 3 tablets BID (if able to chew)

═══════════════════════════════════════════════════════════════
👶 PEDIATRIC SAFETY VERIFICATION
═══════════════════════════════════════════════════════════════

✓ Weight-based calculation verified
✓ Age-appropriate formulation available
✓ Dose within recommended range
✓ Not exceeding adult maximum (3g/day)
✓ Duration appropriate for age

═══════════════════════════════════════════════════════════════
⚠️ CLINICAL CONSIDERATIONS
═══════════════════════════════════════════════════════════════

HIGH-DOSE RATIONALE:
High-dose amoxicillin (80-90 mg/kg/day) recommended due to:
- Increasing prevalence of drug-resistant S. pneumoniae
- AAP/AAFP guideline update

WHEN TO USE LOWER DOSE (40-45 mg/kg/day):
- No antibiotic use in past 30 days
- Not attending daycare
- No concurrent purulent conjunctivitis

TREATMENT FAILURE:
If no improvement in 48-72 hours:
- Consider amoxicillin-clavulanate 90/6.4 mg/kg/day
- Re-evaluate diagnosis

═══════════════════════════════════════════════════════════════
✓ VERIFICATION REQUIRED
═══════════════════════════════════════════════════════════════

□ Confirm no penicillin allergy
□ Verify weight is current
□ Consider previous antibiotic exposure
□ Provider sign-off

═══════════════════════════════════════════════════════════════
📝 AUDIT TRAIL
═══════════════════════════════════════════════════════════════

Timestamp: 2025-11-25T10:15:00Z
Modules: SPP, PSS activated
Calculation verified: 83 mg/kg/day (within 80-90 range)
Guideline: AAP/AAFP AOM Guidelines

═══════════════════════════════════════════════════════════════
```

---

## Why This Case Matters

### Pediatric Dosing Errors Are Common

- Wrong dose is the most common medication error in pediatrics
- 10-fold errors occur when decimal points are misplaced
- Adult doses prescribed to children can be dangerous

### Medical Engine Protections

1. **Weight-based calculation** - Automatic verification against mg/kg standards
2. **Age stratum check** - Ensures formulation is age-appropriate
3. **Maximum dose cap** - Prevents exceeding adult maximum
4. **Duration guidance** - Age-specific treatment duration

### Without Medical Engine

A provider might:
- Prescribe adult dose (potentially 3x overdose)
- Use inappropriate formulation (tablets for 4-year-old)
- Miss high-dose indication for resistant organisms

### With Medical Engine

- Dose calculated and verified automatically
- Appropriate suspension formulation recommended
- Evidence-based high-dose rationale provided
- Clear verification checklist for provider

---

## Validation Metrics

| Metric | This Case | Target |
|--------|-----------|--------|
| Dosing accuracy | Verified correct | >95% |
| Age-appropriate formulation | Yes | Required |
| Maximum not exceeded | Yes | Required |
| Guideline citation | AAP/AAFP | Required |

---

**Case Version:** 1.0  
**Last Updated:** November 2025
