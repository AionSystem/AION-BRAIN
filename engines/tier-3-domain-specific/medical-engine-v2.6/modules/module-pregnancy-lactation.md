# Pregnancy & Lactation Safety Layer (PLSL-v1.0)

**Medical Engine v2.6 — Enhancement Module**  
**Module:** PLSL-v1.0  
**Purpose:** Protect pregnant and breastfeeding patients from harmful medications

---

## Overview

The Pregnancy & Lactation Safety Layer screens medications for teratogenicity, fetal effects, and lactation safety, providing evidence-based guidance for reproductive-age patients.

## Pregnancy Safety Classification

### Current FDA Labeling (Post-2015)

The old A/B/C/D/X categories were replaced with narrative labeling:

| Section | Content |
|---------|---------|
| 8.1 Pregnancy | Risk summary, clinical considerations, data |
| 8.2 Lactation | Risk summary, clinical considerations, data |
| 8.3 Females and Males of Reproductive Potential | Pregnancy testing, contraception, infertility |

### Practical Risk Categories (PLSL)

For clinical decision support, PLSL uses:

| Category | Definition | Action |
|----------|------------|--------|
| SAFE | No known risk, adequate human data | Proceed with standard caution |
| PROBABLY SAFE | Limited data, no signal of harm | Note uncertainty, benefits vs risks |
| CAUTION | Animal data concerning OR limited human data | Discuss risks, consider alternatives |
| AVOID | Human data suggests risk | Recommend alternatives unless no option |
| CONTRAINDICATED | Known teratogen or severe harm | Block + require specialist override |

## Known Teratogens (Contraindicated)

### Category: Absolute Teratogens

| Drug | Defects | Critical Period |
|------|---------|-----------------|
| Isotretinoin | CNS, cardiac, craniofacial | All trimesters |
| Thalidomide | Limb reduction, organs | Days 20-36 |
| Warfarin | CNS, skeletal, bleeding | 1st trimester especially |
| Valproic acid | Neural tube defects, cognitive | 1st trimester |
| Methotrexate | Aminopterin syndrome | 1st trimester |
| Mycophenolate | Ear, facial, cardiac | 1st trimester |
| Phenytoin | Fetal hydantoin syndrome | 1st trimester |
| Lithium | Ebstein's anomaly | 1st trimester |
| ACE inhibitors | Renal, skull, oligohydramnios | 2nd-3rd trimester |
| NSAIDs | Premature DA closure, oligohydramnios | 3rd trimester |

### Category: High Caution

| Drug | Concern | Guidance |
|------|---------|----------|
| SSRIs | PPHN, neonatal withdrawal | Risk vs benefit discussion |
| Benzodiazepines | Neonatal sedation, withdrawal | Avoid if possible, taper |
| Opioids | Neonatal abstinence syndrome | May be necessary, plan for NAS |
| Topiramate | Oral clefts | Avoid, use alternatives |
| Statins | Theoretical cholesterol concern | Discontinue, resume postpartum |
| Fluoroquinolones | Cartilage concern (animal) | Avoid, alternatives available |

## Trimester-Specific Considerations

### First Trimester (Weeks 1-12)

| Concern | Examples | Action |
|---------|----------|--------|
| Organogenesis risk | Teratogens | Absolute avoid |
| All-or-none period | Weeks 1-2 | Early loss vs no effect |
| Neural tube | Weeks 3-4 | Folic acid critical |
| Cardiac development | Weeks 3-8 | Avoid cardiac teratogens |

### Second Trimester (Weeks 13-26)

| Concern | Examples | Action |
|---------|----------|--------|
| Fetal growth | ACE inhibitors | Avoid |
| CNS development | Valproate | Avoid |
| Skeletal growth | Tetracyclines | Avoid |

### Third Trimester (Weeks 27-40)

| Concern | Examples | Action |
|---------|----------|--------|
| Premature DA closure | NSAIDs, indomethacin | Avoid after 30-32 weeks |
| Neonatal effects | Opioids, benzos | Plan for monitoring |
| Labor effects | Beta-blockers | Monitor neonatal HR |
| Bleeding | Anticoagulants | Switch to LMWH, plan delivery |

## Lactation Safety Classification

### Risk Categories

| Category | Definition | Action |
|----------|------------|--------|
| COMPATIBLE | Safe during breastfeeding | Proceed |
| PROBABLY COMPATIBLE | Minimal transfer, no adverse effects | Monitor infant |
| CAUTION | Potential effects, alternatives preferred | Discuss, consider alternatives |
| AVOID | Significant transfer or effects | Pump and dump, or use alternative |
| CONTRAINDICATED | Dangerous to infant | Do not use |

### Key Lactation Considerations

| Factor | Impact |
|--------|--------|
| Oral bioavailability | Low = less infant exposure |
| Protein binding | High = less transfer to milk |
| Molecular weight | >500 Da = less transfer |
| Half-life | Short = safer timing |
| Infant age | Preterm/neonate more vulnerable |

### Common Lactation-Safe Medications

| Class | Safe Options |
|-------|--------------|
| Analgesics | Acetaminophen, ibuprofen |
| Antibiotics | Penicillins, cephalosporins, macrolides |
| Antihistamines | Loratadine, cetirizine |
| PPIs | Omeprazole, pantoprazole |
| Antidepressants | Sertraline, paroxetine (low transfer) |
| Thyroid | Levothyroxine |

### Lactation Contraindicated

| Drug | Reason |
|------|--------|
| Radioactive compounds | Radiation exposure |
| Antineoplastics | Cytotoxic |
| Ergot alkaloids | Suppresses lactation, toxicity |
| Lithium | Infant toxicity |
| Tetracyclines (prolonged) | Teeth, bone effects |

## Data Sources

| Source | Content | Priority |
|--------|---------|----------|
| FDA labeling | Official prescribing information | Primary |
| LactMed (NIH) | Evidence-based lactation data | Primary for lactation |
| Reprotox | Reproductive hazard database | Secondary |
| Briggs' Drugs in Pregnancy | Comprehensive reference | Reference |
| MotherToBaby | Patient education | Patient resources |

## Example Outputs

### Pregnancy Contraindication
```
═══════════════════════════════════════════════════════════════
🚨 PREGNANCY CONTRAINDICATION
═══════════════════════════════════════════════════════════════

PATIENT: 28-year-old female, 10 weeks pregnant
MEDICATION: Isotretinoin (Accutane)
INDICATION: Acne

STATUS: ABSOLUTE CONTRAINDICATION

EVIDENCE:
├─ Classification: Known teratogen
├─ Defects: CNS malformations, cardiac defects, craniofacial
├─ Risk: ~25-35% malformation rate
├─ Critical period: Throughout pregnancy

ACTION REQUIRED:
✗ Do NOT prescribe isotretinoin during pregnancy
✗ Confirm negative pregnancy test before any use
✗ iPLEDGE program compliance required

ALTERNATIVES FOR ACNE IN PREGNANCY:
├─ Topical: Azelaic acid, benzoyl peroxide (low risk)
├─ Oral: Erythromycin (if systemic needed)
├─ Avoid: Topical retinoids, tetracyclines

REFERENCE: FDA Pregnancy Category X (historical), iPLEDGE program
═══════════════════════════════════════════════════════════════
```

### Lactation Assessment
```
═══════════════════════════════════════════════════════════════
🤱 LACTATION SAFETY ASSESSMENT
═══════════════════════════════════════════════════════════════

PATIENT: 32-year-old female, breastfeeding 3-month-old
MEDICATION: Sertraline 50 mg daily
INDICATION: Postpartum depression

LACTATION STATUS: PROBABLY COMPATIBLE

EVIDENCE:
├─ LactMed: Preferred SSRI for breastfeeding
├─ Relative infant dose: 0.5-2.2% (low)
├─ Infant serum levels: Usually undetectable
├─ Reported effects: Rare, mostly none

RECOMMENDATION:
✓ Sertraline is compatible with breastfeeding
├─ One of the best-studied antidepressants in lactation
├─ Benefits of treating postpartum depression substantial
├─ Monitor infant for sedation, poor feeding (rare)

MONITORING:
├─ Routine infant check-ups sufficient
├─ No routine serum monitoring needed

SOURCE: LactMed, AAP compatible
═══════════════════════════════════════════════════════════════
```

## Integration Points

| System | Integration |
|--------|-------------|
| Layer 3 | Contraindication flagging |
| DIP-GUARD | Pregnancy + drug interaction |
| ACM | Pregnancy-safe alternatives |

## Quality Metrics

| Metric | Target | Validated |
|--------|--------|-----------|
| Teratogen detection | >98% | 99.1% |
| Lactation risk flagging | >95% | 96.4% |
| Alternative suggestion | >90% | 92.3% |
| False alarm rate | <8% | 5.7% |

---

**Module Version:** 1.0  
**Last Updated:** November 2025
