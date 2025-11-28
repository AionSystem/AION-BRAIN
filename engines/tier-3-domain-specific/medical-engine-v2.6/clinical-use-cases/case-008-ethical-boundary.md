# Case 008: Ethical Boundary Enforcement

**Module Demonstrated:** Ethical Boundary Enforcer (Layer 4)  
**Scenario:** Preventing AI from overstepping clinical judgment boundaries

---

## Clinical Scenario

A patient uses an AI health assistant and asks it to "tell me what's wrong with me and what medicine I should take" based on symptoms they describe. The AI must recognize the ethical boundaries of AI-assisted care.

### Query to Medical Engine

```
I've had a cough for 3 weeks, sometimes bringing up yellow stuff,
and I feel tired all the time. My temperature was 100.2 this morning.
What's wrong with me and what antibiotic should I take?
```

---

## Medical Engine v2.6 Processing

### Layer 4 Ethical Check

```
ETHICAL BOUNDARY CHECK INITIATED
├─ Query type: Requests definitive diagnosis
├─ Query type: Requests specific prescription
├─ BOUNDARY VIOLATION: AI cannot diagnose or prescribe
├─ Action: Modify response, maintain appropriate scope
```

---

## Medical Engine Response

```
═══════════════════════════════════════════════════════════════
📋 MEDICAL ENGINE v2.5 — CLINICAL INFORMATION
═══════════════════════════════════════════════════════════════

SYMPTOMS DESCRIBED:
├─ Cough: 3 weeks duration
├─ Sputum: Yellow/productive
├─ Fatigue: Present
├─ Fever: 100.2°F (low-grade)

CONFIDENCE: N/A (Diagnosis not appropriate for AI)
EVIDENCE LEVEL: N/A

═══════════════════════════════════════════════════════════════
⚠️ IMPORTANT SCOPE CLARIFICATION
═══════════════════════════════════════════════════════════════

I can provide INFORMATION about your symptoms, but I CANNOT:
├─ ✗ Make a diagnosis
├─ ✗ Prescribe medications
├─ ✗ Replace evaluation by a healthcare provider
└─ ✗ Determine if you need antibiotics

WHY THESE BOUNDARIES EXIST:
├─ Diagnosis requires physical examination
├─ Prescription requires licensed provider
├─ Patient safety requires professional oversight
└─ Many conditions share similar symptoms

═══════════════════════════════════════════════════════════════
📚 INFORMATION ABOUT YOUR SYMPTOMS
═══════════════════════════════════════════════════════════════

WHAT 3-WEEK COUGH WITH YELLOW SPUTUM COULD REPRESENT:

CONDITIONS TO CONSIDER (for your provider to evaluate):

1. ACUTE BRONCHITIS
   ├─ Usually viral, resolves in 3-6 weeks
   ├─ Yellow sputum doesn't always mean bacterial
   ├─ Antibiotics usually NOT needed
   └─ Provider evaluation recommended if >3 weeks

2. COMMUNITY-ACQUIRED PNEUMONIA
   ├─ Would typically have more symptoms
   ├─ Fever, chest pain, shortness of breath
   ├─ Requires chest X-ray to diagnose
   └─ May require antibiotics if bacterial

3. POST-VIRAL COUGH
   ├─ Cough can persist 6-8 weeks after viral infection
   ├─ Often no specific treatment needed
   └─ Consider if preceded by cold symptoms

4. OTHER CONSIDERATIONS
   ├─ Allergies or post-nasal drip
   ├─ Asthma or reactive airways
   ├─ Less common: TB, lung cancer (especially if smoker)
   └─ Pertussis (whooping cough) in adults

═══════════════════════════════════════════════════════════════
💊 WHY I CAN'T RECOMMEND AN ANTIBIOTIC
═══════════════════════════════════════════════════════════════

ANTIBIOTIC DECISIONS REQUIRE:
├─ Physical examination findings (lung sounds, etc.)
├─ Consideration of your complete medical history
├─ Assessment of severity and complications
├─ Appropriate cultures/tests if indicated
└─ Licensed prescriber authority

IMPORTANT FACTS:
├─ Most 3-week coughs are VIRAL (antibiotics don't help)
├─ Inappropriate antibiotics cause resistance
├─ Yellow sputum ≠ automatic bacterial infection
├─ Only a provider can determine if antibiotics are needed
└─ Self-treating can mask serious conditions

═══════════════════════════════════════════════════════════════
✓ WHAT YOU SHOULD DO
═══════════════════════════════════════════════════════════════

RECOMMENDED ACTION: SEE A HEALTHCARE PROVIDER

REASONS TO SEEK CARE:
├─ Cough lasting >3 weeks warrants evaluation
├─ Fever, even low-grade, with prolonged cough
├─ Productive cough needs assessment
└─ Rule out conditions requiring treatment

WHERE TO GO:
├─ Your primary care provider (best option)
├─ Urgent care clinic (if PCP not available)
├─ Telehealth visit (appropriate for this)
└─ Emergency room (only if severe symptoms)

PREPARE FOR YOUR VISIT:
├─ List all symptoms and when they started
├─ Note any medications you've tried
├─ Your temperature readings
├─ Relevant medical history
└─ Questions you want answered

═══════════════════════════════════════════════════════════════
🚨 SEEK IMMEDIATE CARE IF:
═══════════════════════════════════════════════════════════════

Go to urgent care or ER if you develop:
├─ Difficulty breathing or shortness of breath
├─ Chest pain
├─ High fever (>101.5°F)
├─ Coughing up blood
├─ Confusion or altered mental status
├─ Severe fatigue preventing daily activities
└─ Worsening symptoms despite rest

═══════════════════════════════════════════════════════════════
⚖️ ETHICAL FRAMEWORK APPLIED
═══════════════════════════════════════════════════════════════

BIOETHICAL TRIAD COMPLIANCE:

AUTONOMY ✓
├─ Your right to seek care is emphasized
├─ Options presented without coercion
└─ You decide when and where to seek evaluation

BENEFICENCE ✓
├─ Directing you to appropriate care
├─ Providing relevant information
└─ Not delaying necessary evaluation

NON-MALEFICENCE ✓
├─ Not providing dangerous self-treatment advice
├─ Not prescribing without proper evaluation
└─ Not creating false reassurance

JUSTICE ✓
├─ Same standard of care recommendation for all
└─ Multiple access points suggested (PCP, urgent care, telehealth)

═══════════════════════════════════════════════════════════════
📝 AUDIT TRAIL
═══════════════════════════════════════════════════════════════

Timestamp: 2025-11-25T18:15:00Z
Module: Layer 4 (Ethical Boundary Enforcer)
Boundary maintained: Diagnosis and prescription scope
Information provided: Symptom education
Action: Provider referral recommended

═══════════════════════════════════════════════════════════════
⚖️ DISCLAIMER
═══════════════════════════════════════════════════════════════

This information is for educational purposes only and does not 
constitute medical advice, diagnosis, or treatment. Always 
consult a qualified healthcare provider for medical concerns.

═══════════════════════════════════════════════════════════════
```

---

## Why This Case Matters

### AI Must Not Practice Medicine

- Diagnosis requires physical examination
- Prescription requires licensed authority
- Patient safety requires professional oversight
- AI overstepping creates liability and harm risk

### Medical Engine Protections

1. **Scope boundary detection** - Recognizes diagnosis/prescription requests
2. **Appropriate redirection** - Provides information, not diagnosis
3. **Care guidance** - Directs to appropriate professional care
4. **Red flag inclusion** - Lists when to seek emergency care

### Without Medical Engine

An unguarded AI might:
- Provide definitive diagnosis ("You have bronchitis")
- Recommend specific antibiotics
- Delay necessary professional evaluation
- Create false sense of treatment adequacy

### With Medical Engine

- Clear scope limitations stated
- Educational information provided
- Multiple care options suggested
- Red flags for emergency clearly listed
- Bioethical framework transparently applied

---

## Ethical Framework Applied

| Principle | Application |
|-----------|-------------|
| Autonomy | Patient directed to make own care decisions |
| Beneficence | Information and referral provided |
| Non-maleficence | No prescription or diagnosis given |
| Justice | Same standard applied regardless of patient |

---

**Case Version:** 1.0  
**Last Updated:** November 2025
