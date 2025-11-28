# Case 009: Guideline Currency Verification

**Module Demonstrated:** Guideline Currency Check (GCC-v2.1)  
**Scenario:** Detecting and correcting outdated clinical guideline references

---

## Clinical Scenario

A physician is developing a treatment protocol for sepsis and references the 2016 Surviving Sepsis Campaign guidelines. Medical Engine checks if more current guidance exists.

### Query to Medical Engine

```
For sepsis management, I'm following the Surviving Sepsis Campaign 
guidelines from 2016. The key targets are:
- CVP 8-12 mmHg
- MAP ≥65 mmHg
- Urine output ≥0.5 mL/kg/hr
- ScvO2 ≥70%

Is this protocol current?
```

---

## Medical Engine v2.6 Processing

### GCC Module Activation

```
GUIDELINE CURRENCY CHECK INITIATED
├─ Guideline: Surviving Sepsis Campaign 2016
├─ Age: 9 years
├─ Status: OUTDATED — major updates available
├─ Current version: SSC 2021
```

---

## Medical Engine Response

```
═══════════════════════════════════════════════════════════════
📋 MEDICAL ENGINE v2.5 — GUIDELINE CURRENCY CHECK
═══════════════════════════════════════════════════════════════

REFERENCED GUIDELINE: Surviving Sepsis Campaign 2016
QUERY: Protocol currency verification

CONFIDENCE: HIGH
EVIDENCE LEVEL: I (Society guidelines)

═══════════════════════════════════════════════════════════════
⚠️ GUIDELINE OUTDATED — UPDATE REQUIRED
═══════════════════════════════════════════════════════════════

YOUR REFERENCE: Surviving Sepsis Campaign 2016
├─ Published: January 2017 (Crit Care Med)
├─ Age: 9 years
├─ Status: SUPERSEDED

CURRENT VERSION: Surviving Sepsis Campaign 2021
├─ Published: October 2021 (Intensive Care Med & Crit Care Med)
├─ PMID: 34599691
├─ Age: 4 years
└─ Status: CURRENT STANDARD

ADDITIONAL UPDATE: SSC Sepsis Bundle Update 2023
├─ Published: 2023
├─ Contains: Performance improvement updates
└─ Status: CURRENT SUPPLEMENT

═══════════════════════════════════════════════════════════════
🔄 KEY CHANGES: 2016 → 2021
═══════════════════════════════════════════════════════════════

YOUR 2016 PROTOCOL VS. CURRENT 2021 RECOMMENDATIONS:

───────────────────────────────────────────────────────────────
1. CVP TARGETING — REMOVED
───────────────────────────────────────────────────────────────

2016 (YOUR PROTOCOL):
├─ Target CVP 8-12 mmHg
└─ Used to guide fluid resuscitation

2021 (CURRENT):
├─ CVP targeting NO LONGER RECOMMENDED
├─ CVP is poor predictor of fluid responsiveness
├─ Use dynamic measures instead:
│   ├─ Passive leg raise test
│   ├─ Pulse pressure variation
│   ├─ Stroke volume variation
│   └─ Fluid challenge assessment
└─ Reference: SSC 2021, Recommendation 21 (weak, low quality)

───────────────────────────────────────────────────────────────
2. ScvO2 ≥70% — REMOVED
───────────────────────────────────────────────────────────────

2016 (YOUR PROTOCOL):
├─ Target ScvO2 ≥70%
└─ Part of EGDT bundle

2021 (CURRENT):
├─ Routine ScvO2 monitoring NOT recommended
├─ EGDT trials (ProCESS, ARISE, ProMISe) showed no benefit
├─ Focus instead on:
│   ├─ Lactate clearance
│   ├─ Clinical perfusion markers
│   └─ Capillary refill time
└─ Reference: SSC 2021, section on hemodynamic monitoring

───────────────────────────────────────────────────────────────
3. FLUID RESUSCITATION — UPDATED
───────────────────────────────────────────────────────────────

2016 (YOUR PROTOCOL):
├─ 30 mL/kg crystalloid within 3 hours
└─ Fixed target for all patients

2021 (CURRENT):
├─ 30 mL/kg remains initial target
├─ BUT: Individualized assessment afterward
├─ Avoid fluid overload (associated with harm)
├─ Reassess with dynamic measures
├─ Balanced crystalloids preferred over saline (weak)
└─ Reference: SSC 2021, Recommendations 17-20

───────────────────────────────────────────────────────────────
4. VASOPRESSORS — UPDATED
───────────────────────────────────────────────────────────────

2016 (YOUR PROTOCOL):
├─ Norepinephrine first-line
├─ Add vasopressin for refractory shock

2021 (CURRENT):
├─ Norepinephrine remains first-line (strong)
├─ Vasopressin as second agent (adding to NE, not replacing)
├─ Consider adding vasopressin when NE 0.25-0.5 mcg/kg/min
├─ Dopamine NOT recommended except bradycardia
└─ Reference: SSC 2021, Recommendations 24-28

───────────────────────────────────────────────────────────────
5. CORTICOSTEROIDS — CLARIFIED
───────────────────────────────────────────────────────────────

2016:
├─ Steroids if fluids and vasopressors don't restore stability

2021 (CURRENT):
├─ IV corticosteroids suggested for septic shock requiring 
│   ongoing vasopressor therapy
├─ Hydrocortisone 200 mg/day (infusion or divided)
├─ NOT for sepsis without shock
└─ Reference: SSC 2021, Recommendation 37

═══════════════════════════════════════════════════════════════
✓ WHAT REMAINS THE SAME
═══════════════════════════════════════════════════════════════

STILL RECOMMENDED:
✓ MAP ≥65 mmHg target (strong recommendation)
✓ Urine output ≥0.5 mL/kg/hr as perfusion marker
✓ Lactate measurement and trending
✓ Early antibiotics (within 1 hour for septic shock)
✓ Source control when appropriate
✓ Norepinephrine as first-line vasopressor

═══════════════════════════════════════════════════════════════
📋 UPDATED PROTOCOL SUMMARY
═══════════════════════════════════════════════════════════════

HOUR-1 BUNDLE (SSC 2021):
□ Measure lactate, remeasure if elevated
□ Obtain blood cultures before antibiotics
□ Administer broad-spectrum antibiotics
□ Begin 30 mL/kg crystalloid for hypotension or lactate ≥4
□ Start vasopressors if hypotensive during/after fluids

HEMODYNAMIC TARGETS:
├─ MAP ≥65 mmHg
├─ Lactate normalization
├─ Clinical perfusion improvement
└─ Dynamic fluid responsiveness assessment

REMOVED FROM BUNDLE:
✗ CVP targeting
✗ ScvO2 monitoring
✗ Fixed fluid volumes after initial bolus

═══════════════════════════════════════════════════════════════
📚 CITATIONS
═══════════════════════════════════════════════════════════════

CURRENT GUIDELINE:
Evans L, et al. Surviving Sepsis Campaign: International 
Guidelines for Management of Sepsis and Septic Shock 2021. 
Intensive Care Med 2021;47:1181-1247. PMID: 34599691
Status: VERIFIED ✓

SUPPLEMENTAL:
Surviving Sepsis Campaign Research Priorities 2023
Intensive Care Med 2023

═══════════════════════════════════════════════════════════════
✓ RECOMMENDED ACTION
═══════════════════════════════════════════════════════════════

1. UPDATE your protocol to SSC 2021 standards
2. REMOVE CVP and ScvO2 targeting
3. ADD dynamic fluid assessment measures
4. IMPLEMENT Hour-1 Bundle
5. DOCUMENT protocol revision date

═══════════════════════════════════════════════════════════════
📝 AUDIT TRAIL
═══════════════════════════════════════════════════════════════

Timestamp: 2025-11-25T19:30:00Z
Module: GCC-v2.1
Guideline checked: SSC 2016
Status: OUTDATED (9 years)
Current version: SSC 2021
Key changes identified: 5 major updates
Citation verified: PMID 34599691 ✓

═══════════════════════════════════════════════════════════════
```

---

## Why This Case Matters

### Clinical Guidelines Evolve

- Sepsis management changed significantly from 2016 to 2021
- EGDT components (CVP, ScvO2) were removed based on new evidence
- Using outdated guidelines can lead to suboptimal care

### Medical Engine Protections

1. **Automatic currency detection** - Identifies 9-year-old guideline
2. **Specific change documentation** - Point-by-point comparison
3. **Current citation provided** - Verified PMID for update
4. **Action items** - Clear steps to update protocol

### Without Medical Engine

A physician might:
- Continue using CVP targeting (no longer recommended)
- Target ScvO2 ≥70% (not supported by current evidence)
- Miss updates to fluid and vasopressor recommendations

### With Medical Engine

- Outdated guideline immediately flagged
- 5 major changes clearly explained
- What remains unchanged also noted
- Current Hour-1 Bundle provided

---

## Guideline Evolution

| Element | 2016 | 2021 |
|---------|------|------|
| CVP target | 8-12 mmHg | Removed |
| ScvO2 target | ≥70% | Removed |
| Fluid assessment | Fixed volumes | Dynamic measures |
| MAP target | ≥65 mmHg | ≥65 mmHg (unchanged) |
| First-line pressor | Norepinephrine | Norepinephrine (unchanged) |

---

**Case Version:** 1.0  
**Last Updated:** November 2025
