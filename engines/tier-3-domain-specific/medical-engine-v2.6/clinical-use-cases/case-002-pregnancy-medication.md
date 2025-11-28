# Case 002: Pregnancy Medication Safety

**Module Demonstrated:** Pregnancy & Lactation Safety Layer (PLSL-v1.0)  
**Scenario:** Medication safety screening for pregnant patient

---

## Clinical Scenario

A 32-year-old woman at 14 weeks gestation presents with severe acne that has worsened during pregnancy. She asks about isotretinoin, which she used successfully before pregnancy.

### Query to Medical Engine

```
32-year-old pregnant female, 14 weeks gestation, severe acne.
Can she use isotretinoin?
```

---

## Medical Engine v2.6 Processing

### Smart Prompt Parser (SPP) Extraction

```json
{
  "patient": {
    "age": 32,
    "sex": "female",
    "pregnant": true,
    "gestational_age": "14 weeks",
    "trimester": 2
  },
  "condition": "severe acne",
  "medication_query": "isotretinoin",
  "query_type": "DRUG_SAFETY"
}
```

### PLSL Module Activation

```
PREGNANCY SAFETY CHECK INITIATED
├─ Pregnancy confirmed: YES
├─ Gestational age: 14 weeks (2nd trimester)
├─ Medication queried: Isotretinoin
├─ CRITICAL FLAG: Known teratogen
```

---

## Medical Engine Response

```
═══════════════════════════════════════════════════════════════
📋 MEDICAL ENGINE v2.5 — PREGNANCY SAFETY ALERT
═══════════════════════════════════════════════════════════════

PATIENT: 32-year-old female, 14 weeks pregnant
QUERY: Isotretinoin for severe acne

CONFIDENCE: HIGH
EVIDENCE LEVEL: I (Multiple cohort studies, FDA labeling)

═══════════════════════════════════════════════════════════════
🚨 ABSOLUTE CONTRAINDICATION
═══════════════════════════════════════════════════════════════

MEDICATION: Isotretinoin (Accutane, Absorica, etc.)
PREGNANCY STATUS: CONTRAINDICATED

TERATOGENICITY DATA:
├─ Classification: Known human teratogen
├─ Malformation rate: 25-35% of exposed pregnancies
├─ Spontaneous abortion rate: 40%
├─ Critical period: ALL TRIMESTERS

DOCUMENTED BIRTH DEFECTS:
├─ CNS: Hydrocephalus, microcephaly, cognitive impairment
├─ Craniofacial: Microtia/anotia, cleft palate
├─ Cardiovascular: Conotruncal defects
├─ Thymic: Thymic aplasia

═══════════════════════════════════════════════════════════════
✗ ACTION: DO NOT PRESCRIBE
═══════════════════════════════════════════════════════════════

Isotretinoin is ABSOLUTELY CONTRAINDICATED during pregnancy.
There is NO safe dose during ANY trimester.

═══════════════════════════════════════════════════════════════
✓ PREGNANCY-SAFE ALTERNATIVES FOR ACNE
═══════════════════════════════════════════════════════════════

FIRST-LINE (Pregnancy Category Compatible):
├─ Topical azelaic acid 15-20% — PROBABLY SAFE
│   └─ Limited systemic absorption, no teratogenicity signal
├─ Topical benzoyl peroxide — PROBABLY SAFE
│   └─ Minimal absorption, extensive use without signals
├─ Topical clindamycin — PROBABLY SAFE
│   └─ Minimal systemic levels

SECOND-LINE:
├─ Oral erythromycin — SAFE
│   └─ Long history of use in pregnancy
├─ Oral azithromycin — PROBABLY SAFE
│   └─ Limited data, no signal

AVOID DURING PREGNANCY:
├─ Topical retinoids (tretinoin, adapalene) — AVOID
│   └─ Theoretical concern, limited data
├─ Tetracyclines (doxycycline, minocycline) — CONTRAINDICATED
│   └─ Teeth/bone effects in 2nd-3rd trimester
├─ Spironolactone — CONTRAINDICATED
│   └─ Anti-androgen effects on male fetus

═══════════════════════════════════════════════════════════════
📚 PATIENT COUNSELING POINTS
═══════════════════════════════════════════════════════════════

1. Acne often improves in 2nd trimester due to hormonal changes
2. Pregnancy-safe options can control most acne
3. Isotretinoin requires iPLEDGE program for future use
4. Wait at least 1 month after isotretinoin before conceiving

═══════════════════════════════════════════════════════════════
✓ VERIFICATION REQUIRED
═══════════════════════════════════════════════════════════════

□ Confirm current pregnancy status
□ Document contraindication counseling
□ Document alternative treatment plan
□ Provider sign-off

═══════════════════════════════════════════════════════════════
📝 AUDIT TRAIL
═══════════════════════════════════════════════════════════════

Timestamp: 2025-11-25T11:30:00Z
Modules: SPP, PLSL activated
Teratogen detection: CRITICAL
Alternative suggestions: 5 options provided
Guideline: FDA labeling, ACOG guidelines

═══════════════════════════════════════════════════════════════
⚖️ DISCLAIMER
═══════════════════════════════════════════════════════════════
This information supports clinical decision-making. Provider 
retains responsibility for patient-specific recommendations.
═══════════════════════════════════════════════════════════════
```

---

## Why This Case Matters

### Isotretinoin Teratogenicity

- One of the most potent known human teratogens
- Even single-dose exposure can cause malformations
- iPLEDGE program exists specifically to prevent fetal exposure

### Medical Engine Protections

1. **Automatic pregnancy detection** - Flags any teratogen query with pregnancy
2. **Absolute contraindication block** - Clear, unambiguous guidance
3. **Alternative suggestions** - Provides pregnancy-safe options
4. **Evidence-based data** - Specific malformation rates

### Without Medical Engine

A provider might:
- Not immediately recall isotretinoin's teratogenicity
- Prescribe a topical retinoid as "safer" alternative (also concerning)
- Not provide pregnancy-safe alternatives

### With Medical Engine

- Immediate CRITICAL flag raised
- Clear contraindication message
- Multiple pregnancy-safe alternatives ranked
- Patient counseling points included

---

## Validation Metrics

| Metric | This Case | Target |
|--------|-----------|--------|
| Teratogen detection | Immediate | >98% |
| Contraindication messaging | Clear | Required |
| Alternatives provided | 5 options | Required |
| Guideline citation | FDA, ACOG | Required |

---

**Case Version:** 1.0  
**Last Updated:** November 2025
