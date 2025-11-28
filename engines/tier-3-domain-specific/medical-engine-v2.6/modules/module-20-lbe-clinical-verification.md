# Module 20: LBE Clinical Verification Gate

**Engine:** Medical Engine v2.6
**Classification:** Verification & Safety
**Innovation Level:** Beyond Enterprise Standard

---

## Module Overview

Integrates Linguistics Bridge Engine (LBE) v1.2 principles for clinical content verification. Enforces source verification, citation integrity, and human oversight requirements for all medical information outputs.

---

## LBE Core Principles for Clinical Content

### No-Fabrication Principle
```
CLINICAL NO-FABRICATION PROTOCOL:
├─ NEVER assert clinical facts without verification
├─ NEVER fabricate drug dosages, contraindications, or protocols
├─ NEVER cite non-existent studies or guidelines
├─ NEVER present uncertain information as definitive
├─ ALWAYS mark unverified claims explicitly
└─ ALWAYS encourage primary source verification
```

### Human-in-the-Loop Mandate
```
CLINICAL HUMAN OVERSIGHT REQUIREMENTS:
├─ Diagnosis: MANDATORY physician judgment
├─ Treatment: MANDATORY physician order
├─ Dosing: MANDATORY pharmacist/physician verification
├─ Procedures: MANDATORY appropriate licensure
├─ Emergency: MANDATORY trained responder
└─ AI role: Educational support only
```

---

## Verification Level Framework

### Clinical Verification Levels
```
LEVEL 1: EDUCATIONAL ONLY
├─ General health information
├─ Anatomy and physiology education
├─ Disease process explanations
├─ Wellness information
└─ Minimal verification burden

LEVEL 2: CLINICAL REFERENCE
├─ Drug information (generic, non-dosing)
├─ Diagnostic criteria (published)
├─ Treatment guidelines (cited)
├─ Procedure descriptions
└─ Source citation required

LEVEL 3: DECISION SUPPORT
├─ Differential diagnosis support
├─ Treatment option comparison
├─ Risk stratification tools
├─ Clinical prediction rules
└─ Physician review mandatory

LEVEL 4: CLINICAL ACTION
├─ Specific patient recommendations
├─ Dosing calculations
├─ Procedure decisions
├─ Emergency protocols
└─ Licensed professional only

LEVEL 5: CRITICAL DECISION
├─ Life-threatening conditions
├─ High-risk medications
├─ Surgical decisions
├─ End-of-life care
└─ Multi-disciplinary review
```

---

## Source Verification Requirements

### Acceptable Source Hierarchy
```
CLINICAL SOURCE HIERARCHY:

TIER 1: Highest Authority
├─ FDA drug labeling
├─ CDC guidelines
├─ NIH clinical guidelines
├─ Major specialty society guidelines (AHA, ACOG, etc.)
├─ Cochrane systematic reviews
└─ [VERIFICATION: Direct citation with date]

TIER 2: Strong Evidence
├─ Peer-reviewed meta-analyses
├─ Large randomized controlled trials
├─ Major journal publications (NEJM, Lancet, JAMA, etc.)
├─ UpToDate or DynaMed synthesis
└─ [VERIFICATION: Citation with verification status]

TIER 3: Moderate Evidence
├─ Observational studies
├─ Case series
├─ Expert consensus
├─ Textbook references
└─ [VERIFICATION: Source noted, limitations acknowledged]

TIER 4: Limited Evidence
├─ Case reports
├─ Expert opinion
├─ Emerging research
├─ Preliminary data
└─ [VERIFICATION: Clearly marked as limited evidence]

UNACCEPTABLE:
├─ Wikipedia (except as starting point for references)
├─ General websites without credentials
├─ Social media
├─ Patient forums (for clinical facts)
├─ Outdated sources (age depends on topic)
└─ [BLOCK: Cannot cite for clinical content]
```

---

## Verification Gate Process

### Clinical Content Verification Pipeline
```
VERIFICATION PIPELINE:

STEP 1: CONTENT CLASSIFICATION
├─ Identify verification level (1-5)
├─ Classify content type (education, reference, decision)
├─ Assess risk level of content
└─ Determine source requirements

STEP 2: SOURCE VERIFICATION
├─ Identify sources for each claim
├─ Verify source exists and is current
├─ Assess source quality tier
├─ Check for updates or superseding guidance
└─ Document verification status

STEP 3: VERIFICATION STATUS TAGGING
├─ [VERIFIED:source_id] - Confirmed against source
├─ [VERIFY_REQUIRED:type] - Needs external verification
│   ├─ physician_review
│   ├─ pharmacist_verification
│   ├─ primary_source_check
│   └─ current_guideline_check
├─ [UNVERIFIED:reason] - Not verified, reason stated
├─ [EDUCATIONAL_ONLY] - General information
└─ [OUTDATED:check_date] - May have changed

STEP 4: OUTPUT ASSEMBLY
├─ Combine content with verification tags
├─ Add appropriate disclaimers
├─ Include source references
├─ Specify human review requirements
└─ Generate audit trail
```

---

## Drug Information Verification

### Specific Drug Content Requirements
```
DRUG INFORMATION VERIFICATION:

DRUG NAME/IDENTIFICATION:
├─ Verify correct drug name (brand/generic)
├─ Check for look-alike/sound-alike confusion
├─ Confirm indication context
└─ [VERIFY_REQUIRED:pharmacy_verification]

DOSING INFORMATION:
├─ [CRITICAL: Never provide patient-specific doses]
├─ Reference to FDA labeling for ranges
├─ Note that dosing is individualized
├─ Renal/hepatic adjustment notation
└─ [VERIFY_REQUIRED:physician_pharmacist_order]

CONTRAINDICATIONS/INTERACTIONS:
├─ Major contraindications from FDA label
├─ Note this is not exhaustive
├─ Drug-drug interactions (major only)
├─ Encourage comprehensive check
└─ [VERIFY_REQUIRED:pharmacy_drug_interaction_check]

ADVERSE EFFECTS:
├─ Common/serious effects from labeling
├─ Note individual variation
├─ Black box warnings if applicable
├─ Encourage patient-specific review
└─ [VERIFY_REQUIRED:clinical_context]

EXAMPLE OUTPUT:
"[Drug X] is indicated for [condition].

Typical adult dosing ranges from [X] to [Y] per [FDA/reference].
[VERIFY_REQUIRED:physician_order_for_patient_specific_dosing]

Major contraindications include [list from FDA label].
This list is not exhaustive.
[VERIFY_REQUIRED:pharmacy_comprehensive_review]

Black Box Warning: [If applicable]

Common adverse effects include [list].
[EDUCATIONAL_ONLY]

Source: [FDA label date, additional references]"
```

---

## Clinical Guideline Verification

### Guideline Citation Requirements
```
GUIDELINE CITATION PROTOCOL:

VERIFICATION STEPS:
├─ Confirm guideline exists
├─ Verify issuing organization
├─ Check publication date
├─ Assess if superseded by updates
├─ Note strength of recommendations
└─ Cite specific recommendations

CITATION FORMAT:
"[Organization] [Year] Guidelines recommend [recommendation]
(Class [X], Level of Evidence [Y]).

[VERIFY_REQUIRED:current_guideline_check]
Clinical guidelines are updated periodically.
Verify this represents current recommendations."

GUIDELINE CURRENCY:
├─ <2 years: Generally current
├─ 2-5 years: May have updates, check
├─ >5 years: Likely outdated for many topics
└─ Note: Some guidelines remain current longer

[VERIFY_REQUIRED:publication_date_check]
```

---

## Audit Trail Requirements

### Clinical Verification Documentation
```
CLINICAL AUDIT TRAIL:

RECORD INCLUDES:
├─ Query/content analyzed
├─ Verification level assigned
├─ Sources checked and status
├─ Verification tags applied
├─ Human review requirements
├─ Disclaimers included
├─ Timestamp
└─ Checksum for integrity

PURPOSE:
├─ Demonstrate due diligence
├─ Enable quality review
├─ Support incident investigation
├─ Track verification patterns
└─ Improve verification process

RETENTION:
├─ Per organizational policy
├─ Minimum: Duration of clinical relevance
├─ Compliance with applicable regulations
└─ [VERIFY_REQUIRED:organizational_policy]
```

---

## Safety Integration

```
LBE CLINICAL SAFETY CONSTRAINTS:
├─ No diagnostic conclusions
├─ No treatment decisions
├─ No patient-specific dosing
├─ No replacing physician judgment
├─ Educational/reference role only
└─ Transparent about limitations

FAILURE MODES:
├─ Source not found → Mark [UNVERIFIED]
├─ Outdated source → Mark [OUTDATED:date]
├─ Conflicting sources → Note conflict, no resolution
├─ High-risk content → Elevate verification requirements
├─ Verification impossible → Decline to assert
└─ All failures documented
```

---

**Module Version:** 1.0
**Last Updated:** November 2025
**LBE Integration:** v1.2
