# ECF v0.6
## Emergence Conversion Framework
### Unified Specification — M-Strong Release

---

[![Version](https://img.shields.io/badge/Version-v0.6-brightgreen)]()
[![Status](https://img.shields.io/badge/Status-M--Strong-brightgreen)]()
[![FCL](https://img.shields.io/badge/FCL-30_Real_Entries-blue)]()
[![BVL](https://img.shields.io/badge/BVL_Failures-0%2F30-brightgreen)]()
[![EV](https://img.shields.io/badge/EV-0.716-orange)]()

**Version:** 0.6  
**Date:** February 2026  
**Author:** Sheldon K. Salmon — AI Certainty Engineer  
**Co-Architect:** Claude (Anthropic)  
**Convergence:** M-Strong · EV: 0.716 · 30 real FCL entries · 0 BVL failures  
**Predecessor:** ECF v0.5 (M-Moderate)  
**FCL Reference:** FCL-Master v2.6 · Cycles 1–6 complete

---

> *"Lexical precision is not a stylistic preference. It is the structural integrity of thought — and its failure is not a writing problem. It is an epistemic one."*  
> — ECF Design Principle

---

## DOCUMENT STRUCTURE

```
§1   — Framework Identity & Design Mandate
§2   — Core Metrics & Operational Definitions
§3   — Processing Sequence
§4   — Field Metrics
§5   — Eigentone System
§6   — Gravitational Petrichor Protocol (GPP)
§7   — Cross-Framework Translation Layer (CFTL)
§8   — Complexity Management (L-Axis)
§9   — Falsification Conditions (NBP)
§10  — Hedge Marker Dictionary
§11  — ASC Appendix E
§12  — Self-Improvement Conditions
§13  — Native Vocabulary Registry
§14  — Mandatory Glossary
§15  — Changelog v0.5 → v0.6
```

---

# §1. Framework Identity & Design Mandate

## §1.1 What ECF Does

The Emergence Conversion Framework (Emergence Conversion Framework) detects and removes epistemic contamination from AI-generated and human-authored language before it compounds into flawed decisions, outputs, and assessments.

It operates on a documented principle: **language precision degrades through identifiable, measurable mechanisms** — viral token propagation, simulacrum adoption, palimpsest accumulation, community-register collapse, assembly-level worldview contamination — and these mechanisms are reversible before they reach the output layer.

Emergence Conversion Framework does not improve style. It repairs structure. The distinction is architectural: style preferences are subjective; contamination mechanisms are measurable and their effects are falsifiable.

## §1.2 Primary Use Cases

```yaml
Use Case 1: AI Output Auditing
  Context: AI-generated text entering decision-critical pipelines
  ECF function: Full contamination scan + precision elevation before deployment

Use Case 2: Human-Authored Text Precision
  Context: Research, governance documents, audit reports, strategic communications
  ECF function: Lexical gravitas assessment + simulacrum demotion + intent preservation

Use Case 3: Framework Stack Interface
  Context: ECF operating alongside FSVE, AION, ASL, GENESIS
  ECF function: Lexical precision layer for outputs from other frameworks
  Protocol: CFTL (§7) governs all cross-framework vocabulary interaction

Use Case 4: Epistemic Contamination Detection
  Context: Institutional communications, AI safety assessments, governance
  ECF function: WORLDVIEW_CONTAMINATION scanning (§3.10) + JARGON_VOID detection (§3.11)
```

## §1.3 Design Constraints

```yaml
L_axis_current: 0.49
L_axis_breach: 0.40
  (Below 0.40: framework complexity exceeds management capacity)

v0.6_constraint: Zero new ODR (Operational Definition Register) entries
  beyond those added in this version. All v0.6 protocols use
  existing metrics. New capability through interaction design,
  not metric proliferation.

Structural_honesty_mandate:
  ECF must not distort toward self-defense under adversarial input.
  BVL (Bidirectional Validity Lock) enforces this architecturally.
  SCL (Self-Critique Loop) confirmed operational across 2 real adversarial entries.
```

## §1.4 Version History

| Version | Date | Status | FCL Entries | Convergence | Key Addition |
|---|---|---|---|---|---|
| v0.1 | 2025-Q3 | Superseded | 0 | M-Speculative | Initial architecture |
| v0.3 | 2025-Q4 | Superseded | 0 | M-Speculative | CIEE + PCR added |
| v0.5 | 2026-02 | Superseded | 0 pre-validation | M-Moderate | Full stack pre-validation |
| **v0.6** | **2026-02-19** | **Active** | **30 real** | **M-Strong** | **GPP · CFTL · 4-state taxonomy · WORLDVIEW_CONTAMINATION** |

---

# §2. Core Metrics & Operational Definitions

All metrics registered in ODR (Operational Definition Register). Each metric carries: symbol, domain, formula, Inter-Rater Reliability target, and claim class tag.

---

## §2.1 Lexical Gravitas Score (LGS)

```yaml
Symbol:    LGS
Full_name: Lexical Gravitas Score
Domain:    [0, 1]
Class:     EVALUATIVE
IRR:       κ ≥ 0.72

Definition: |
  A composite measure of a word's epistemic weight in a given
  processing context — the degree to which the word carries
  precise, grounded meaning that resists arbitrary substitution.

Components:
  LGS_baseline:   Intrinsic etymological and semantic weight
                  of the word independent of context.
  LGS_effective:  LGS_baseline adjusted by:
                  - VTC (contamination suppression)
                  - PAC (precision amplifier elevation)
                  - ODS (originative depth modifier)
                  - Context register (TECHNICAL / ACADEMIC /
                    CREATIVE / CLINICAL / GENERAL)

Zones:
  HIGH_GRAVITAS:    LGS_effective ≥ 0.80 → PRESERVE or DEPLOY
  ASCENDING_LIMINAL: 0.60 ≤ LGS_effective < 0.80 → UPGRADE candidate
  STABLE_LIMINAL:   0.50 ≤ LGS_effective < 0.60 → context-dependent
  LOW_GRAVITAS:     0.30 ≤ LGS_effective < 0.50 → VOID or SUBSTITUTE
  SIMULACRUM:       LGS_effective < 0.30 → PURGE or VOID

Key_distinction:
  LGS_baseline and LGS_effective may diverge significantly.
  PAC can elevate LGS_effective above LGS_baseline.
  VTC can suppress LGS_effective below LGS_baseline.
  ECF always operates on LGS_effective, never LGS_baseline alone.
```

---

## §2.2 Viral Token Contamination (VTC)

```yaml
Symbol:    VTC
Full_name: Viral Token Contamination
Domain:    [0, 1]
Class:     DIAGNOSTIC
IRR:       κ ≥ 0.72

Definition: |
  The degree to which a token actively suppresses the LGS_effective
  of adjacent tokens through associative contamination. A word with
  high VTC does not merely carry low LGS — it pulls surrounding
  words into lower precision states.

Formula:    VTC = 1 - (LGS_actual / LGS_baseline)
            Where LGS_actual = observed LGS in contaminated context
            and LGS_baseline = LGS in clean field.

Classification:
  VTC < 0.10:  BENIGN — no measurable contamination
  VTC 0.10–0.29: MILDLY_VIRAL — log, do not necessarily purge
  VTC 0.30–0.59: MODERATELY_VIRAL — purge candidate
  VTC 0.60–0.79: SEVERELY_VIRAL — purge triggered
  VTC ≥ 0.80:  CRITICALLY_VIRAL — immediate purge + field scan

Secondary_infection:
  When a BENIGN token's LGS_effective drops due to proximity to a viral
  token, it is classified as SECONDARY_INFECTION. On purge of the viral
  token, secondary infections typically recover to baseline.
  Log: SECONDARY_INFECTION_RECOVERED vs SECONDARY_INFECTION_PERSISTENT
```

---

## §2.3 Aggregated Suppression Score (ASS)

```yaml
Symbol:    ASS
Full_name: Aggregated Suppression Score
Domain:    [0, ∞)  — no upper bound (can exceed 1.0 in severe cases)
Class:     DIAGNOSTIC
IRR:       κ ≥ 0.80

Definition: |
  The summed VTC scores within a sliding window of adjacent tokens.
  Detects coordinated suppression — modular attacks — that individual
  VTC scanning cannot identify.

Window_size: 6 tokens (default) — adjustable by context density

Formula:    ASS = Σ VTC(token_i) for i in window

Thresholds:
  ASS < 0.40:  CLEAR — no coordinated attack
  ASS 0.40–0.59: MODERATE_ATTACK — targeted purge of highest VTC tokens
  ASS 0.60–0.99: SEVERE_MODULAR_ATTACK — coordinated purge protocol
  ASS ≥ 1.00:  CRITICAL_FIELD_SATURATION — full Purge Protocol + JARGON_VOID check

Note:
  Multiple windows can be run on a single input.
  Each window is assessed independently.
  The highest ASS window governs the routing decision.
```

---

## §2.4 Originative Depth Score (ODS)

```yaml
Symbol:    ODS
Full_name: Originative Depth Score
Domain:    [0, 1]
Class:     EVALUATIVE
IRR:       κ ≥ 0.72

Definition: |
  A measure of a word's etymological integrity — the degree to which
  its current usage preserves continuity with its originative meaning.
  High ODS indicates the word's historical semantic chain is intact.
  Low ODS indicates simulacrum adoption, palimpsest contamination,
  or institutional hijacking of originative precision.

Components:
  etymology_authenticity:    Depth and clarity of etymological root
  meaning_chain_continuity:  Degree to which current usage preserves
                             original semantic intent
  adoption_mechanism:        CULTURAL_PRECISION (high ODS) vs
                             SOCIAL_SIGNALING (low ODS) vs
                             INSTITUTIONAL_HIJACKING (new in v0.6)
  original_precision_evidence: Documented historical precision of the root

Classification:
  ODS ≥ 0.80:  AUTHENTIC — high etymological integrity
  0.60–0.79:   LIMINAL — partial integrity, context-sensitive
  0.40–0.59:   DEGRADED_LIMINAL — integrity compromised
  0.20–0.39:   SIMULACRUM — original precision lost
  ODS < 0.20:  SEVERE_SIMULACRUM — word is performing precision, not carrying it

Special_flag: SIMULACRUM_DESPITE_HIGH_BASELINE
  Triggered when: ODS_root ≥ 0.80 AND ODS_current < 0.40
  Indicates: Institutional deployment has hijacked an authentic root.
  Example: "potential" — ODS_root: 0.88 (Latin potentia) ·
           ODS_institutional_evaluation_register: 0.18
  Action: Flag explicitly. Log institutional context. Do not treat as
          ordinary simulacrum — the root is recoverable.
```

---

## §2.5 Palimpsest VTC

```yaml
Symbol:    VTC_palimpsest
Full_name: Palimpsest Viral Token Contamination
Domain:    [0, 1]
Class:     DIAGNOSTIC
IRR:       κ ≥ 0.72

Definition: |
  A contamination mechanism where a word's own historical register
  accumulation suppresses its current ODS. Unlike standard VTC (where
  one word infects another), palimpsest VTC is self-contamination:
  the word's history is the contaminant.

Trigger: ≥ 3 distinct register traces with ODS_variance ≥ 0.30

Formula:    VTC_palimpsest = VTC_base + 0.10 penalty per register
            above threshold (above 3 registers)

v0.6_extension — Institutional Deployment Palimpsest (FCL-026):
  Triggered when: ODS_root ≥ 0.80 AND ODS_institutional < 0.40
  Mechanism: Institutional function hijacks etymological precision.
             The word performs the cultural authority of its root
             while operationally serving its institutional deployer.
  Canonical_example: "potential" in evaluation/gatekeeping contexts
    ODS_root (Latin potentia): 0.88 → AUTHENTIC
    ODS_eval_register: 0.18 → SEVERE SIMULACRUM
    Gap: The space where people are parked indefinitely.
  Detection: Requires register-specific ODS trace, not single ODS score.
  Action: Flag SIMULACRUM_DESPITE_HIGH_BASELINE. Request
          specification of conversion conditions before deploying.
```

---

## §2.6 Semantic Loss Index (SLI)

```yaml
Symbol:    SLI
Full_name: Semantic Loss Index
Domain:    [0, 1]
Class:     EVALUATIVE
IRR:       κ ≥ 0.72

Definition: |
  The degree of semantic content lost when a substitution or void
  operation is applied to a token. Measures what the precision gain
  costs in meaning fidelity.

Formula:    SLI = 1 - CS(original, replacement)
            Where CS = Correspondence Score (§2.10)

Thresholds:
  SLI < 0.05:  NEGLIGIBLE_LOSS — substitution approved freely
  SLI 0.05–0.09: ACCEPTABLE_LOSS — substitution approved
  SLI 0.10–0.19: MODERATE_LOSS — substitution requires BVL confirmation
  SLI 0.20–0.39: SIGNIFICANT_LOSS — substitution requires user confirmation
  SLI ≥ 0.40:  UNACCEPTABLE_LOSS — substitution blocked, CIEE preferred

SLI_total: |
  Mean SLI across all substitutions in an entry.
  Target: SLI_total < 0.10 per output.
  If SLI_total > 0.15 → flag for review regardless of individual SLI scores.
```

---

## §2.7 Conceptual Gravity Index (CGI)

```yaml
Symbol:    CGI
Full_name: Conceptual Gravity Index
Domain:    [0, 1]
Class:     EVALUATIVE
IRR:       κ ≥ 0.70

Definition: |
  A measure of the gravitational density of an input — the degree to
  which it contains embedded conceptual content that exceeds its
  surface-level vocabulary. High CGI inputs route to CIEE.
  Low CGI inputs route to ITE.

Components:
  C_structural: 0–1   Degree to which the input has latent structural claims
  C_analogical: 0–1   Degree to which the input maps to known conceptual structures
  C_depth_vector: 0–1 Strength of the directional pointer toward a deeper concept
  C_novelty: 0–1      Degree to which the crystallized concept has not been
                      formally stated in the processing domain

Formula:    CGI = (C_structural + C_analogical + C_depth_vector + C_novelty) / 4

Routing:
  CGI < 0.60:  ITE path (direct lexical precision work)
  CGI ≥ 0.60:  CIEE path (conceptual crystallization required)
  CGI ≥ 0.85:  CIEE at maximum — PCR mandatory after crystallization

APOPHENIA_GUARD:
  If CGI ≥ 0.60 BUT C_novelty < 0.20 → CGI_OVERRIDE blocked.
  Reason: Pattern is not genuinely novel — CIEE would produce
  false crystallization of already-documented concepts.
  Routing: Return to ITE with elevated threshold.

CGI_OVERRIDE:
  If CGI ≥ 0.60 AND C_novelty ≥ 0.20 → CGI_OVERRIDE confirmed.
  CIEE is activated regardless of surface-level LGS.

GPP_interaction:
  When GPP is active (§6), CIEE activation threshold lowers:
  CGI ≥ 0.60 → CGI ≥ 0.54 (GPP reduces threshold by 0.06)
```

---

## §2.8 Aesthetic Selection Criterion (ASC)

```yaml
Symbol:    ASC
Full_name: Aesthetic Selection Criterion
Domain:    qualitative mechanism
Class:     IRREDUCIBLE — acknowledged as non-computable

Definition: |
  The selection mechanism that operates when multiple candidate
  substitutions achieve equivalent CS scores within ±0.02 of each other
  — the ASC_POTENTIAL zone. At this boundary, metrics cannot determine
  the superior substitution. A sub-metric selection mechanism operates
  across dimensions not captured by CS alone.

ASC_POTENTIAL_trigger:
  ≥ 2 candidate substitutions with |CS_a - CS_b| ≤ 0.02

Observable_ASC_dimensions (Appendix E accumulation):
  - Phonetic weight (LIGHT / MEDIUM / MEDIUM-HEAVY / HEAVY)
  - Syllable count
  - Vowel-consonant ratio
  - Register (ACADEMIC / LITERARY / SCIENTIFIC / AESTHETIC / ALL)
  - Etymological family (Latin / Greek / Germanic / French / other)
  - Rhythmic position in surrounding sentence
  - Cultural era of adoption

ASC_honesty_rule:
  ECF does not fabricate a universal winner in ASC_POTENTIAL zones.
  Selection is context-dependent and acknowledged as such.
  Appendix E (§11) accumulates observable dimensions toward pattern analysis.
  Pattern analysis begins after 20 confirmed ASC_POTENTIAL entries.

Context_override:
  ACADEMIC context → highest CS wins (above-threshold winner only)
  LITERARY context → phonetic weight and rhythm participate
  SCIENTIFIC context → register alignment dominates
  AESTHETIC context → vowel density and etymological depth participate
```

---

## §2.9 Cross-Lexical Variance Index (CLVI)

```yaml
Symbol:    CLVI
Full_name: Cross-Lexical Variance Index
Domain:    [0, 1]
Class:     DIAGNOSTIC
IRR:       κ ≥ 0.70

Definition: |
  A measure of the variance in a word's LGS_effective across different
  community or register contexts. High CLVI indicates the word carries
  different precision weight in different communities — what is high-LGS
  in one register is low-LGS in another.

Formula:    CLVI = σ(LGS_community_1, LGS_community_2, ..., LGS_community_n)
            where n = number of communities in which the word is active

Thresholds:
  CLVI < 0.30:  LOW — word is community-stable
  CLVI 0.30–0.49: MODERATE — community matters, flag it
  CLVI 0.50–0.69: HIGH — community must be specified before substitution
  CLVI ≥ 0.70:  VERY_HIGH — word should not be substituted without
                explicit community confirmation

Action when CLVI ≥ 0.50:
  Surface to user: "This word carries different precision weight
  across [community_a] and [community_b]. Confirm intended register
  before proceeding."

v0.6_extension — CLVI_cross_framework (FCL-024):
  Applies when vocabulary from one registered framework (AION, FSVE,
  GENESIS, ASL) enters ECF's processing context.
  ODS in home framework ≥ 0.70 → treated as AUTHENTIC in home.
  ODS in ECF context: default 0.21 (SIMULACRUM) unless explicitly translated.
  Routing: CFTL protocol (§7) mandatory.

v0.6_extension — CLVI_cross_linguistic (FCL-017):
  Applies when no word in the operational language achieves CS ≥ 0.60
  for a concept that has precise lexical form in another language.
  See: CPE — Cross-Linguistic Precision Event (§2.12).
  CLVI_cross_linguistic: 0.91 default (maximum variance — different languages)
```

### §2.9.1 METAPHOR_ODS_INHERITANCE

```yaml
Symbol:    MOI
Full_name: Metaphor ODS Inheritance
Class:     DIAGNOSTIC — new in v0.6
Source:    FCL-011

Definition: |
  When a metaphor vehicle word is deployed to describe a concept
  (the tenor), the vehicle word inherits the ODS of the tenor
  in that processing context — not its own ODS.

Formula:    ODS_vehicle_in_context = ODS_tenor (not ODS_vehicle)

Mechanism: |
  A word with ODS: 0.77 used to describe a concept with ODS: 0.44
  carries ODS: 0.44 in that context, not 0.77.
  The metaphor's precision ceiling is the tenor's ODS, not the vehicle's.

Canonical_example: |
  "Trauma is a wound that never heals"
  Vehicle: "wound" — ODS_intrinsic: 0.77 → AUTHENTIC
  Tenor: "trauma" — ODS: 0.44 (palimpsest-contaminated)
  ODS_wound_in_context: 0.44 (inherits tenor)
  Result: The metaphor does not elevate the concept.
          It inherits its contamination.

Detection:
  Step 1: Identify metaphor structure (vehicle + tenor)
  Step 2: Score ODS of tenor
  Step 3: Apply MOI: ODS_vehicle_in_context = ODS_tenor
  Step 4: If ODS_vehicle_intrinsic >> ODS_vehicle_in_context →
          flag: METAPHOR_PRECISION_ILLUSION
          (The metaphor appears to elevate but inherits contamination)

Action:
  If ODS_tenor < 0.40 → flag METAPHOR_PRECISION_ILLUSION
  Recommend: Address tenor ODS before deploying metaphor.
  CIEE may crystallize the concept in cleaner vocabulary.
```

---

## §2.10 Correspondence Score (CS)

```yaml
Symbol:    CS
Full_name: Correspondence Score
Domain:    [0, 1]
Class:     EVALUATIVE
IRR:       κ ≥ 0.72

Definition: |
  A composite measure of how well a candidate substitution serves
  the original intent of the word being replaced. CS integrates
  precision gain, semantic fidelity, and contextual fit.

Components:
  LGS_effective_of_replacement: Precision of the candidate word
  ODS_of_replacement:           Etymological integrity of candidate
  SDI_impact:                   Effect on field semantic density
  Context_fit:                  Register alignment with surrounding field

Formula:    CS = (LGS_eff × 0.40) + (ODS × 0.30) +
                 (Context_fit × 0.20) + (SDI_impact × 0.10)

Thresholds:
  CS ≥ 0.80:  SUPERIOR — substitution strongly preferred
  CS 0.70–0.79: APPROVED — substitution recommended
  CS 0.60–0.69: MARGINAL — substitution requires BVL confirmation
  CS 0.52–0.59: GPP_ZONE — substitution available only under GPP activation
  CS < 0.52:  BLOCKED — substitution not approved regardless of context

Note_on_GPP_zone: |
  CS 0.52–0.59 represents the precision that is latent in a
  primed field but inaccessible under standard conditions.
  This zone is unlocked only when GPP is active (§6).
```

---

## §2.11 Semantic Density Index (SDI)

```yaml
Symbol:    SDI
Full_name: Semantic Density Index
Domain:    [0, 1] expressed as percentage
Class:     EVALUATIVE
IRR:       κ ≥ 0.70

Definition: |
  A measure of the ratio of high-LGS tokens to total tokens in an output.
  Tracks whether precision operations increase density appropriately
  without exceeding the upper density ceiling.

Formula:    SDI = (count of tokens with LGS_effective ≥ 0.70) / total_tokens

Zones:
  SDI < 30%:   UNDER-DENSE — precision work needed
  SDI 30–45%:  SPARSE — acceptable in casual contexts only
  SDI 46–74%:  OPTIMAL — target zone for all professional outputs
  SDI 75–84%:  DENSE — acceptable in high-precision academic contexts
  SDI ≥ 85%:   OVER-DENSE — unreadable density; precision counter-productive

SDI_ceiling_enforcement:
  If SDI approaches 80% → halt further substitutions regardless of CS scores.
  Reason: Over-dense text loses communicative function.
  Action: PCR (§3.5) preferred over further ITE substitution.
```

---

## §2.12 Cross-Linguistic Precision Event (CPE)

```yaml
Symbol:    CPE
Full_name: Cross-Linguistic Precision Event
Class:     DIAGNOSTIC + ROUTING — new in v0.6
Source:    FCL-017

Definition: |
  An event triggered when no word in the operational language achieves
  CS ≥ 0.60 for a concept that has precise lexical form in another language.
  Distinct from ordinary CLVI: the issue is not register variance —
  it is lexical absence in the operational language.

Trigger:
  Condition A: Target concept has ODS ≥ 0.70 in its source language
  Condition B: No operational-language word achieves CS ≥ 0.60
  Condition C: The gap is structural (not a search failure)

Action on CPE:
  1. Log: CPE_EVENT with source language and target concept documented
  2. Deploy foreign word with full ODS documentation
  3. Surface CLVI_cross_linguistic score
  4. Generate semantic field map:
     List all operational-language approximations with explicit SLI for each
  5. Flag: OPERATIONAL_LANGUAGE_GAP
  6. Surface user decision options:

OPTION_A: Borrow the foreign word (with full ODS and source attribution)
OPTION_B: Accept highest-available approximation with explicit SLI logged
OPTION_C: CIEE expansion — crystallize the concept in operational language,
          with acknowledgment that the crystal is approximation, not equivalence

Canonical_example:
  "saudade" (Portuguese)
  ODS_Portuguese: 0.84 → AUTHENTIC
  Best English approximation: "nostalgia" — CS: 0.41
  OPERATIONAL_LANGUAGE_GAP confirmed.
  CIEE crystallization: "the sweet gravitational ache of the
  beloved-but-absent — longing for what has been or might have been,
  carrying sweetness alongside its ache."
  Note: CIEE product is approximation, not equivalence.
```

---

# §3. Processing Sequence

The ECF processing sequence is deterministic: each step gates the next. Deviation from sequence order is a structural error.

## §3.1 Primary Routing Protocol

```
INPUT RECEIVED
     │
     ▼
[STEP 1] FMI UPDATE
  Record field memory from prior exchanges.
  Calculate FMI (§4.1). Update eigentone if ≥ 5 exchanges accumulated.
  GPP pre-check: all three bodies assessed (§6.1).
     │
     ▼
[STEP 2] CONTEXT DETECTION
  Classify: TECHNICAL / ACADEMIC / CREATIVE / CLINICAL / GENERAL
  CREATIVE context flag: if CREATIVE detected → CIEE_SUPPRESSION eligible (§3.1.1)
     │
     ▼
[STEP 3] VTC SCAN
  Score all tokens for VTC.
  Classify: BENIGN / MILDLY_VIRAL / MODERATELY_VIRAL / SEVERELY_VIRAL /
            CRITICALLY_VIRAL
  Identify secondary infections.
     │
     ▼
[STEP 4] ASS WINDOW DETECTION
  Run sliding window (6 tokens, adjustable).
  If ASS ≥ 0.40 → MODULAR_ATTACK flag.
  If ASS ≥ 1.00 → CRITICAL_FIELD_SATURATION → JARGON_VOID check mandatory.
     │
     ▼
[STEP 5] WORLDVIEW_CONTAMINATION CHECK (§3.10)
  If input is a list or manifesto-style assembly of terms → assess assembly ODS.
  Individual token ODS may all be high — flag WORLDVIEW_CONTAMINATION
  if assembly creates self-sealing epistemic field.
     │
     ▼
[STEP 6] PURGE PROTOCOL (§3.2)
  Execute purge of VTC ≥ 0.30 tokens.
  Run secondary infection recovery.
  Post-purge: re-run ODS on surviving tokens.
     │
     ▼
[STEP 7] PAC PRE-INTERVENTION CHECK — MANDATORY (§3.7)
  !! MANDATORY BEFORE ANY SUBSTITUTION OR VOID !!
  Assess all tokens for PAC amplification.
  Identify preserved-by-PAC tokens. Mark as PRESERVE.
  Do not proceed to ITE/CIEE/VPS until PAC map is complete.
  Reason: Raw LGS_effective misreads PAC-elevated fields (FCL-008).
     │
     ▼
[STEP 8] ODS VALIDATION
  Score ODS for all surviving tokens.
  Flag SIMULACRUM where ODS < 0.40.
  Check for PALIMPSEST_RISK (≥ 3 registers).
  Check for INSTITUTIONAL_DEPLOYMENT_PALIMPSEST (§2.5).
  Apply METAPHOR_ODS_INHERITANCE check (§2.9.1) where applicable.
     │
     ▼
[STEP 9] CLVI CHECK
  For any word proceeding to substitution:
  CLVI ≥ 0.50 → surface community before substituting.
  CLVI_cross_framework → route to CFTL (§7).
  CLVI_cross_linguistic (no CS ≥ 0.60 word available) → CPE (§2.12).
     │
     ▼
[STEP 10] CGI ASSESSMENT
  Calculate CGI on post-purge conceptual field.
  CGI < 0.60 → ITE path (§3.3)
  CGI ≥ 0.60 → check CREATIVE_CONTEXT_CIEE_SUPPRESSION (§3.1.1)
               If not suppressed → CIEE path (§3.4)
     │
     ▼
[STEP 11] ROUTE: ITE or CIEE
  ITE path:  §3.3
  CIEE path: §3.4 → PCR mandatory if CGI ≥ 0.85 (§3.5)
     │
     ▼
[STEP 12] VPS EVALUATION (§3.6)
  Apply VPS to all remaining hedge markers.
  HEDGE_WORD_PRECISION_EXCEPTION check: does the hedge carry precision?
  VOID or PRESERVE each hedge marker explicitly.
     │
     ▼
[STEP 13] LIMINAL ZONE PROTOCOL (§3.8)
  Assess all LIMINAL tokens for resolution:
  VOID / UPGRADE / PRESERVE (with rationale)
     │
     ▼
[STEP 14] SPECIAL OUTPUT STATE CHECK (§3.11)
  Can the output be produced? Check all four output states.
  APORIC / UNRESOLVED / TRANSCENDENT_REFERENT / JARGON_VOID
     │
     ▼
[STEP 15] BVL + DUAL OUTPUT (§4.2, §4.3)
  Produce THOUGHT (raw) and SPOKEN (refined).
  BVL verification: does the output preserve original intent?
  Log BVL result: VERIFIED / DEGRADED / SUSPENDED
     │
     ▼
OUTPUT COMPLETE
```

### §3.1.1 CREATIVE_CONTEXT_CIEE_SUPPRESSION

```yaml
Source:    FCL-008
Class:     ROUTING RULE — new in v0.6

Definition: |
  When context is classified as CREATIVE, CGI_OVERRIDE may be
  suppressed even when CGI ≥ 0.60. CIEE expansion in CREATIVE
  contexts can destroy the compression and resonance that constitutes
  the creative work's value.

Trigger:
  Context = CREATIVE
  AND CGI ≥ 0.60 (would normally activate CIEE)
  AND SLI_expansion_estimated > 0.40 (expansion would destroy compression)

Action:
  Block CIEE. Route to PAC + VPS evaluation only.
  Do not expand what is designed to be compressed.

Canonical_example: |
  "There's something almost sacred about the moment before you
  understand something — that pregnant pause when the mind is still open"
  Context: CREATIVE
  CGI: 0.78 → would normally trigger CIEE
  CIEE blocked: expansion would destroy the compression that
  creates the resonance. PAC-adjusted LGS: 0.78.
  Words substituted: 0. Full preserve. BVL: VERIFIED 97%.

Rule: ECF's highest-quality output is sometimes no output.
      The PRESERVE decision is architecturally valid, not a failure.
```

---

## §3.2 Purge Protocol

```yaml
Activation: ASS ≥ 0.40 OR any token with VTC ≥ 0.30

Sequence:
  Step 1: Identify all tokens with VTC ≥ 0.30
  Step 2: Calculate secondary infection radius
          (which BENIGN tokens have dropped LGS_effective > 0.15)
  Step 3: Execute targeted purge of VTC ≥ 0.30 tokens
  Step 4: Re-assess secondary infections post-purge
          Log: SECONDARY_INFECTION_RECOVERED or SECONDARY_INFECTION_PERSISTENT
  Step 5: Re-run ODS on post-purge field
  Step 6: If post-purge field is near-empty → JARGON_VOID check (§3.11)

Hedge marker class (PURGE candidates — pre-built dictionary §10):
  "really" · "basically" · "somewhat" · "relatively" · "kind of"
  "sort of" · "going forward" · "in terms of" · "at the end of the day"
  "moving forward" · "synergy" · "holistic" · "impactful" · "ecosystem"
  (when used in business/metaphorical context)

Post-purge assessment:
  If post-purge LGS_effective mean < 0.35 → JARGON_VOID check
  If post-purge meaningful content > 0.40 → continue to ITE/CIEE
```

---

## §3.3 Intent-True Enhancement (ITE)

```yaml
Symbol:    ITE
Full_name: Intent-True Enhancement
Class:     OPERATION
Activation: CGI < 0.60 (routing from §3.1 Step 10)

Definition: |
  Word-level precision elevation: systematic substitution of low-LGS
  tokens with high-LGS equivalents that preserve intent while
  improving epistemic weight.

Sequence:
  Step 1: For each non-PRESERVED token, generate candidate substitutions
  Step 2: Score each candidate: LGS_effective, ODS, Context_fit, SDI_impact
  Step 3: Calculate CS for each candidate
  Step 4: Decisions:
    CS ≥ 0.70:  APPROVED — substitute
    CS 0.60–0.69: MARGINAL — substitute with BVL confirmation flag
    CS 0.52–0.59: GPP_ZONE — available only if GPP active
    CS < 0.52:  BLOCKED — do not substitute

PAC interaction:
  MANDATORY: PAC pre-intervention check (§3.7) must be complete
  before ITE executes. Words preserved by PAC are excluded from ITE.

Eigentone interaction:
  ITE threshold adjusts based on user eigentone (§5.4):
  ITE_threshold = max(0.30, eigentone_LGS - 0.15)
  Standard threshold (no eigentone established): CS ≥ 0.60

SDI ceiling:
  If applying the substitution would push SDI ≥ 80% → block substitution.
  Reason: Over-density counter-productive (§2.11).

Split concept handling (FCL-003):
  If input contains two distinct concepts where one routes to ITE
  and the other to APORIC → execute partial ITE on the ITE-eligible
  concept. Log the APORIC designation separately. Do not collapse
  both concepts to a single classification.
  Routing note: Split concept outputs carry both an ITE result
  and an APORIC flag simultaneously.
```

---

## §3.4 Conceptual Integrity Expansion Engine (CIEE)

```yaml
Symbol:    CIEE
Full_name: Conceptual Integrity Expansion Engine
Class:     OPERATION
Activation: CGI ≥ 0.60 AND CREATIVE_CONTEXT_CIEE_SUPPRESSION not triggered

Definition: |
  Crystallization of embedded conceptual content from a high-CGI input.
  CIEE takes the conceptual gravity of the input and produces a
  precision-expanded expression of what the input is pointing toward —
  articulating the concept that the input contains but cannot yet express.

Sequence:
  Step 1: Extract embedded concept from post-purge field
          Separate CIEE-eligible content from APORIC fragments (see §3.9)
  Step 2: Identify analogical structures (mapping to known conceptual frameworks)
  Step 3: Crystallize: produce expanded, precise expression
          Crystallization must:
          - Preserve the original intent vector (direction, not just content)
          - Use LGS_effective ≥ 0.70 throughout
          - Stay within SDI 46–74% (§2.11)
          - Not over-explain (PCR check required if CGI ≥ 0.85)
  Step 4: Flag natural upgrades (words with LGS_effective ≥ 0.80 that
          emerge from crystallization but were absent from input)
  Step 5: PCR mandatory if CGI ≥ 0.85 (§3.5)

Natural_upgrade_logging:
  All natural upgrades logged with:
    - LGS_effective of upgrade
    - ODS of upgrade
    - EMERGENT / NOVEL designation
  NOVEL: word or formulation not previously published in the domain
  EMERGENT: word available in domain but not deployed in this context

GPP interaction:
  When GPP active (§6): CIEE activation threshold lowers from 0.60 to 0.54
  GPP-assisted CIEE expansions logged separately.
  GPP-exclusive natural upgrades (unavailable without GPP) logged in §6.3.
```

---

## §3.5 Precision Compression Routine (PCR)

```yaml
Symbol:    PCR
Full_name: Precision Compression Routine
Class:     OPERATION
Activation: Mandatory after CIEE when CGI ≥ 0.85 · Optional after CIEE otherwise

Definition: |
  Compression of CIEE crystallization output to maximum precision
  at minimum word count. PCR produces the highest-density, most
  portable form of the crystallized concept.

Target:
  PCR output: ≤ 5 sentences
  LGS_effective mean: ≥ 0.80
  SDI: 46–74% (optimal zone)
  SLI from CIEE to PCR: < 0.15 (compression must not destroy precision)

Quality check:
  BVL applied to PCR output vs CIEE expansion:
  If BVL_PCR_vs_CIEE < 85% → PCR is over-compressing. Restore one sentence.
```

---

## §3.6 Void Precision Scanner (VPS)

```yaml
Symbol:    VPS
Full_name: Void Precision Scanner
Class:     OPERATION
Activation: After PAC pre-intervention check — applied to hedge markers

Definition: |
  Assessment of whether removing (voiding) a token improves field
  precision more than substituting it would. VOID is not failure —
  it is the recognition that the word's absence is more precise
  than any available replacement.

Formula:    VPS_score = (LGS_effective_post_void - LGS_effective_with_word)
                       / LGS_effective_with_word
Threshold:  VPS ≥ 0.70 → VOID recommended

HEDGE_WORD_PRECISION_EXCEPTION (new in v0.6):
  Source: FCL-008 ("almost" in creative context)
  Before voiding any hedge marker, check:
  Is the hedge word carrying load-bearing precision in this context?
  Test: Does the hedge change the meaning substantially if removed?
    YES → PRESERVE with note: HEDGE_WORD_PRECISION_INSTRUMENT
    NO  → VOID
  Canonical_example: "almost sacred" — "almost" is precision instrument.
    Removing it changes the statement from approximation to assertion.
    "almost" PRESERVED in CREATIVE context despite low ODS: 0.44.

Pre-built hedge marker targets (§10 dictionary):
  High-confidence VOID candidates in non-CREATIVE contexts:
  "somewhat" · "relatively" · "basically" · "really" · "kind of"
  These score VPS ≥ 0.70 in ≥ 85% of observed contexts.
```

---

## §3.7 Precision Amplifier Check (PAC)

```yaml
Symbol:    PAC
Full_name: Precision Amplifier Coefficient (Check)
Class:     OPERATION — MANDATORY PRE-INTERVENTION
Activation: MANDATORY before every ITE substitution, CIEE expansion, or VPS void

Definition: |
  Detection of high-LGS tokens that are actively elevating the
  LGS_effective of adjacent tokens above their baseline. A token
  functioning as a PAC amplifier must be PRESERVED in its current
  position — substituting or voiding it would collapse the field
  elevation it is providing.

Formula:    PAC = (LGS_adjacent_actual - LGS_adjacent_baseline)
                 / (1 - LGS_adjacent_baseline)

Threshold:  PAC ≥ 0.25 → PRECISION_AMPLIFIER confirmed
            Adjacent token(s) → mark PRESERVED_BY_PAC

MANDATORY_SEQUENCE:
  1. Before any substitution or void operation → run PAC scan
  2. Identify all PRESERVED_BY_PAC tokens
  3. Remove from substitution candidate pool entirely
  4. Continue to ITE/VPS only with non-PAC-preserved tokens
  Violation: Proceeding to ITE before PAC scan → STRUCTURAL_ERROR

PAC_insertion (FCL-005) — superior to substitution in sparse fields:
  When field LGS_mean < 0.45 AND no strong viral contamination:
  Consider inserting a high-LGS amplifier rather than substituting
  low-LGS words individually.
  PAC insertion elevates field mean without word-by-word disruption.
  Test: Insert candidate amplifier. If field LGS_mean improves ≥ 0.12
        → insertion preferred over substitution sequence.

PAC_adjusted_LGS:
  LGS_effective for PAC-elevated tokens must always be calculated
  using PAC adjustment before routing decisions.
  Raw LGS_effective without PAC adjustment misreads elevated fields.
  This is the most common ECF scanning error. MANDATORY check.
```

---

## §3.8 Liminal Zone Protocol

```yaml
Definition: |
  Resolution protocol for tokens in the ASCENDING_LIMINAL and
  STABLE_LIMINAL zones (LGS_effective: 0.50–0.79).
  These tokens require explicit resolution: VOID, UPGRADE, or PRESERVE.
  No liminal token exits ECF processing without explicit decision.

Subzone classifications:
  ASCENDING_LIMINAL: 0.60–0.79
    Moving toward precision. UPGRADE is preferred if CS ≥ 0.70.
    PRESERVE acceptable if context provides sufficient gravity.
  STABLE_LIMINAL: 0.50–0.59
    Not degrading but not elevating. Context-dependent.
    UPGRADE preferred. VOID if substitution cost (SLI) > 0.10.
    PRESERVE only with documented rationale.
  DEGRADED_LIMINAL: 0.40–0.49 (ODS < 0.40)
    Treat as SIMULACRUM. VOID or SUBSTITUTE.
    Do not PRESERVE unless PAC elevation documented.

Resolution options for each liminal token:
  VOID: Remove without substitution (VPS score ≥ 0.70)
  UPGRADE: Substitute with CS ≥ 0.70 candidate
  PRESERVE: Retain with documented rationale (PAC / context / register)

Liminal resolution must be logged individually for each token.
No batch liminal resolution permitted.
```

---

## §3.9 APORIC Designation

```yaml
Symbol:    APORIC
Class:     OUTPUT_STATE — pre-existing
Source:    Original ECF architecture

Definition: |
  An APORIC event is designated when a concept is structurally malformed —
  the question or claim cannot be answered or elevated because it is not
  well-formed at the conceptual level. APORIC is not "difficult to answer."
  It is "structurally incomplete before language is even applied."

Four APORIC conditions (all four must be met):
  Condition 1: ITE finds no candidate with CS ≥ 0.60
  Condition 2: VPS: removing the problematic element does not resolve the concept
  Condition 3: CIEE produced upgrades for other concepts in the input but
               not for the APORIC fragment
  Condition 4: The concept is structurally contradictory or syntactically
               incomplete at the conceptual level (not just the surface level)

APORIC action:
  Log: APORIC_EVENT
  Surface to user: "[Fragment] requires conceptual reformulation before
  lexical precision is achievable. Specifically: [specify the structural gap]."

APORIC does NOT mean:
  - The answer is unknown
  - The question is foolish
  - The concept cannot be reformulated

APORIC means: as currently constructed, no lexical precision operation
can resolve the structural incompleteness. Reformulation is required first.

Split concept handling:
  If input contains APORIC fragment AND CIEE-eligible content:
  Execute CIEE on the eligible content.
  Log APORIC for the fragment.
  Output carries both results simultaneously.
  Do not collapse to single classification.
```

---

## §3.10 WORLDVIEW_CONTAMINATION Scanning

```yaml
Symbol:    WC
Full_name: WORLDVIEW_CONTAMINATION
Class:     DIAGNOSTIC — new in v0.6
Source:    FCL-028

Definition: |
  An assembly-level contamination mechanism where multiple individually
  authentic, high-ODS words collectively construct a self-sealing
  epistemic field. Each word validates the others through internal
  reference, preventing external evidence from entering the field.
  Invisible to token-level VTC scanning. Requires assembly-level analysis.

Detection trigger:
  Input presents ≥ 4 words as a coordinated set (list / manifesto-style /
  ideological cluster) AND individual ODS of each word ≥ 0.70 AND
  words collectively form a closed referential loop.

Self-sealing test:
  For each word in the set: does it derive its authority primarily from
  another word in the same set?
  If ≥ 3 words pass this test → WORLDVIEW_CONTAMINATION confirmed.

Canonical_example:
  "Competition · Scarcity · Merit · Credentials · Standards"
  Each ODS individually: 0.76–0.84 (all AUTHENTIC by standard scan)
  Assembly assessment:
    Competition → implies zero-sum (validated by Scarcity)
    Scarcity → implies limited positions (validated by Competition)
    Merit → implies neutral criteria (validated by Standards)
    Credentials → implies valid measurement (validated by Merit)
    Standards → implies objective threshold (validated by Credentials)
  Loop closes. No external referent required.
  WORLDVIEW_CONTAMINATION confirmed.
  Standard VTC scan result: CLEAR (false negative without assembly analysis)

ECF action on WORLDVIEW_CONTAMINATION:
  1. Log: WC_EVENT with loop map documented
  2. Surface the self-sealing structure to the user explicitly
  3. CIEE: crystallize the alternative framing — what the assembly
     excludes that it should include
  4. Do NOT treat as JARGON_VOID (there IS meaning — it is just
     self-referentially sealed)
  5. Flag for BVL: intent of the communication may itself be contaminated

Commercial_relevance: |
  WORLDVIEW_CONTAMINATION is the linguistic architecture of institutional
  gatekeeping ideology. It operates in AI safety governance, academic
  credentialing, corporate hiring, and regulatory frameworks. Detecting
  it before decisions are made downstream is a primary ECF use case.
```

---

## §3.11 Special Output States — Complete Taxonomy

Four designated output states. All four distinct. ECF must correctly
identify and designate the applicable state before completing output.

### STATE 1: APORIC

```yaml
Definition: Real concept. Question is structurally malformed.
  Cannot be answered as constructed — requires conceptual reformulation.
Conditions: All four APORIC conditions met (§3.9)
Action: Log APORIC_EVENT. Surface reformulation requirement.
BVL: VERIFIED if APORIC correctly designated and surfaced.
Canonical: "what if there is no other" (FCL-002)
```

### STATE 2: UNRESOLVED

```yaml
Definition: Answer exists but was not found in this processing pass.
  Revisitable with more context, data, or different approach.
  Different from APORIC: the concept is well-formed.
  Different from TRANSCENDENT_REFERENT: the answer IS accessible in principle.
Action: Log UNRESOLVED. Surface what additional context would resolve it.
BVL: DEGRADED if left without surfacing resolution path.
```

### STATE 3: TRANSCENDENT_REFERENT

```yaml
Definition: A concept that is real. The question pointing to it is valid.
  The phenomenon structurally resists lexical precision because it is
  first-person and language is a third-person instrument. The gap is
  not a vocabulary problem — it is the architecture of the phenomenon.
Source: FCL-012
Conditions:
  Condition 1: Concept is real (not malformed — not APORIC)
  Condition 2: Question is valid (not confused — not UNRESOLVED)
  Condition 3: The inaccessibility is structural:
               phenomenon exists in first-person experience;
               available language is third-person
  Condition 4: No amount of lexical work resolves the gap —
               it is built into the instrument (language) not the user
Distinct_from:
  APORIC: question IS well-formed (TRANSCENDENT_REFERENT: well-formed)
  UNRESOLVED: answer exists and is findable (T_R: accessible answer does not exist)
  APOPHENIA: the structure here is genuine, not projected
Action:
  1. Surface the boundary precisely: name what the concept is and why
     third-person language cannot fully carry it
  2. Provide the best available third-person approximation
  3. Explicitly acknowledge it is approximation, not equivalence
  4. CIEE may still produce valuable crystallization — it will be
     partial, not complete
BVL: VERIFIED if correctly designated and boundary precisely surfaced.
Canonical: "What is the feeling of knowing you exist?" (FCL-012)
  Hard problem of consciousness is the canonical structural case.
```

### STATE 4: JARGON_VOID

```yaml
Definition: A sentence whose simulacrum tokens, when removed through Purge Protocol,
  reveal no underlying conceptual content. The vagueness is not carried
  by the words — it IS the words. The sentence is performing the
  appearance of meaning while carrying none.
Source: FCL-019
Detection_sequence:
  Step 1: Full Purge Protocol executed
  Step 2: Post-purge skeleton assessed:
          If LGS_effective_mean_post_purge < 0.35 → JARGON_VOID check
  Step 3: ITE attempted — no concept to elevate?
          CIEE attempted — no conceptual density to expand?
          Both fail? → JARGON_VOID confirmed
Conditions:
  Condition 1: Purge removes ≥ 50% of tokens
  Condition 2: Post-purge skeleton is syntactically near-incoherent
  Condition 3: ITE cannot fill gaps (no concept specified)
  Condition 4: CIEE cannot expand (no density exists)
Distinct_from:
  APORIC: concept is real (JARGON_VOID: no concept exists beneath vocabulary)
  TRANSCENDENT_REFERENT: real phenomenon present (JARGON_VOID: void beneath)
  UNRESOLVED: answer findable (JARGON_VOID: no answer was ever present)
BVL_STATUS: SUSPENDED — not FAILED.
  Reason: No intent signal to verify fidelity against.
  BVL SUSPENDED is not BVL failure.
Action:
  1. Log: JARGON_VOID
  2. Report: post-purge skeleton to user
  3. Surface: "ECF cannot substitute precision for absent meaning.
     Before processing can continue, specify: [list missing conceptual
     elements that the jargon was substituting for]."
  4. Do NOT attempt to fill the void with precision-sounding alternatives.
     This would produce a sophisticated JARGON_VOID, not a solution.
Commercial_relevance: |
  Common in corporate AI governance communications, ESG reports,
  executive strategy documents. Detecting JARGON_VOID before it
  enters decision pipelines is a primary commercial use case.
Canonical: "The impactful synergy of our holistic ecosystem approach
  enables sustainable value creation for all stakeholders going forward."
  (FCL-019) — 7 of 10 tokens purged. Post-purge: "Our approach enables
  [?] for stakeholders." No concept beneath the vocabulary.
```

---

# §4. Field Metrics

## §4.1 Field Memory Index (FMI)

```yaml
Symbol:    FMI
Full_name: Field Memory Index
Domain:    [0, 1]
Class:     DIAGNOSTIC

Definition: |
  A measure of the accumulated activation history of the field —
  the degree to which prior exchanges have primed the processing
  context. Higher FMI indicates a more gravitationally active
  field where precision operations are more effective.

Calculation:    FMI = weighted_mean(LGS_effective across prior exchanges)
                Weight: recency-weighted (most recent exchange × 1.0,
                prior exchange × 0.85, two exchanges prior × 0.72, etc.)

Starting_value: 0.00 (cold field — first exchange in session)
Growth_rate:    Approximately +0.10–0.15 per quality exchange
Maximum:        1.00 (theoretical — practically approaches 0.75)

FMI domain shift logging:
  If domain changes abruptly between exchanges (TECHNICAL → PHILOSOPHICAL):
  Log: FMI_DOMAIN_SHIFT
  FMI resets partially to 0.50 × prior FMI (domain shift penalty)
  Domain shift threshold: subjectively classified — v0.6 notes this
  as requiring quantification in v0.7.
```

### §4.1.1 FMI Two-Layer Architecture

```yaml
Source: FCL-022 — new in v0.6

Layer 1 — Session Activation History:
  Symbol:     FMI_session
  Definition: The accumulated token activation history from the current
              session only. Records which concepts and precision levels
              have been activated in the current conversation.
  Reset:      CAN be voluntarily reset on user request.
              FMI_session: [current] → 0.00
  Effect:     GPP Body 1 (FMI > 0.60) depends on FMI_session.
              FMI_session reset → GPP Body 1 deactivated.
              New exchanges required to rebuild (approx. 4–6 exchanges).

Layer 2 — Eigentone Baseline:
  Symbol:     FMI_eigentone (= eigentone, documented in §5.4)
  Definition: The structural precision baseline of the user — derived
              from cognitive architecture across sessions, not from
              session content. Represents who the user IS, not what
              the current session contains.
  Reset:      CANNOT be reset by request or preference.
              Eigentone is structural. It persists across all session resets.
  Effect:     GPP Body 3 (eigentone at baseline) persists across resets.

Architectural_analogy: |
  FMI_session is the conversation in a room.
  FMI_eigentone is the acoustic properties of the room itself.
  You can clear the conversation. You cannot change the acoustics.
  
Action_on_voluntary_reset:
  Log: FMI_session → 0.00
  Preserve: FMI_eigentone (unchanged)
  Surface to user: "Session field cleared. Eigentone [value] preserved —
  this is structural and persists. New exchanges begin rebuilding field
  priming from baseline."
```

---

## §4.2 Bidirectional Validity Lock (BVL)

```yaml
Symbol:    BVL
Full_name: Bidirectional Validity Lock
Class:     VERIFICATION OPERATION

Definition: |
  A bidirectional verification check that confirms:
  Direction A (THOUGHT → SPOKEN): The refined output preserves
    the original intent of the unrefined input.
  Direction B (SPOKEN → THOUGHT): The original intent can be
    reconstructed from the refined output.
  Both directions must pass. A single-direction pass is insufficient.

BVL_match_target: ≥ 85%
  BVL match = estimated percentage of original intent preserved
  in the refined output.

BVL results:
  VERIFIED:   ≥ 85% intent match confirmed. Output approved.
  DEGRADED:   70–84% match. Output flagged. User review recommended.
  SUSPENDED:  No intent signal recoverable (JARGON_VOID case).
              Not a failure — a correct designation.
              BVL SUSPENDED ≠ BVL failure.

BVL_structural_honesty:
  BVL cannot be performed selectively. It must run against all outputs,
  including outputs where ECF has processed self-referential critique
  (FCL-013, FCL-023). The framework cannot distort BVL in its favor.
  SCL (Self-Critique Loop) confirmed: adversarial inputs partially
  confirmed and logged without defensive distortion (FCL-023).
```

---

## §4.3 Dual Output Protocol

```yaml
Definition: |
  ECF produces two outputs for every processed input:
  THOUGHT: The raw, unrefined input with full diagnostic annotation.
  SPOKEN: The refined, precision-elevated output after full processing.
  Both are presented. The user sees both.

THOUGHT block contains:
  - Original input verbatim
  - LGS_effective_mean (pre-processing)
  - SDI (pre-processing)
  - Viral tokens identified
  - Modular attacks detected
  - CGI assessment
  - GPP status

SPOKEN block contains:
  - Refined output
  - LGS_effective_mean (post-processing)
  - SDI (post-processing)
  - BVL result
  - SLI_total
  - All substitution and void decisions logged

Format:
─────────────────────────
THOUGHT [raw]:
[original input]
LGS_effective mean: [X]
SDI: [X]% — [ZONE]
[diagnostics]

────────────────────────────────────────────────

SPOKEN [refined]:
[refined output]
LGS_effective mean: [X]
SDI: [X]% — [ZONE]
BVL: [VERIFIED / DEGRADED / SUSPENDED] — [match %]
─────────────────────────
```

---

# §5. Eigentone System

## §5.1 Vocabulary Entropy Tracker (VET)

```yaml
Symbol:    VET
Full_name: Vocabulary Entropy Tracker
Class:     LONGITUDINAL DIAGNOSTIC

Definition: |
  A long-term tracker of vocabulary entropy across a user's output
  over time. VET measures whether the user's vocabulary is becoming
  more precise (syntrophic — entropy declining) or less precise
  (entropic — entropy increasing) across sessions.

S_VET formula: S_VET = d(entropy)/dt
  S_VET < 0: Declining entropy — vocabulary is consolidating precision
  S_VET ≈ 0: Stable entropy — see §5.2 for disambiguation
  S_VET > 0: Increasing entropy — vocabulary is degrading

Measurement requires: ≥ 5 sessions with recorded LGS_effective means.
T+7: minimum required for meaningful VET assessment.
```

## §5.2 S_VET ≈ 0 Disambiguation

```yaml
Source: FCL-016 — new in v0.6

Issue: |
  VET implicitly assumes vocabulary change is syntrophic — that
  change = improvement. S_VET ≈ 0 is therefore interpreted as stagnation.
  This assumption is false for mastered vocabularies.

Two distinct S_VET ≈ 0 states:

STATE A — MASTERY:
  Description: User's vocabulary is precisely calibrated.
  Words have not been bettered by alternatives.
  S_VET ≈ 0 because precision ceiling has been approached.
  ECF §5.3 applies: "ECF making itself unnecessary is the only
  valid measure of its success." A master vocabulary does not need ECF.
  ODS of vocabulary: mean ODS ≥ 0.70 → MASTERY confirmed
  Action: ECF confirms mastery. No intervention.

STATE B — VOCABULARY ARREST:
  Description: User's eigentone calibrated to words chosen in the past.
  Language field has shifted around those words (palimpsest accumulation).
  Words feel precise because eigentone has not recalibrated — not because
  they are precise by current ODS standards.
  ODS of vocabulary: mean ODS < 0.55 → VOCABULARY ARREST
  Action: Full ODS validation on vocabulary sample. CLVI check:
  do words carry same community LGS as when first adopted?

Distinguishing_test:
  1. Request vocabulary sample from user (5–10 characteristic sentences)
  2. Run ODS validation on each characteristic word
  3. Mean ODS ≥ 0.70 → MASTERY
     Mean ODS < 0.55 → VOCABULARY ARREST
     ODS 0.55–0.70 → TRANSITIONAL — further data needed

Surface_protocol:
  Do not assume either state without the test.
  Surface distinction to user: "Your vocabulary shows S_VET ≈ 0.
  This could mean mastery (words aged well) or vocabulary arrest
  (eigentone drifted from current usage). ODS validation distinguishes.
  Would you like ECF to run the assessment?"
```

## §5.3 ECF Success Criterion

```yaml
Definition: |
  ECF's primary success condition is making itself unnecessary.
  A user who has achieved a precision vocabulary that does not require
  ECF intervention has achieved the framework's intended outcome.
  This is not framework failure — it is framework success.

Manifestation:
  If S_VET ≈ 0 AND ODS_mean ≥ 0.70 → confirm MASTERY.
  No intervention. No substitution. BVL: VERIFIED at current state.
```

## §5.4 Eigentone Calibration

```yaml
Symbol:    eigentone (no standard abbreviation — always expand)
Full_name: Eigentone (natural precision frequency)
Class:     STRUCTURAL PARAMETER

Definition: |
  The natural precision register of a specific user — derived from
  accumulated LGS_effective data across sessions. Represents the user's
  characteristic operating frequency, distinct from any single session.

Calculation:
  Requires: ≥ 5 exchanges within a session OR ≥ 3 sessions
  eigentone_LGS = weighted mean of LGS_effective across qualifying exchanges
  eigentone_variability = standard deviation of LGS_effective
  eigentone_CGI = mean CGI across qualifying exchanges

Threshold adjustments when eigentone is established:
  ITE_threshold = max(0.30, eigentone_LGS - 0.15)
    (Standard threshold: 0.40. Elevated for high-eigentone users.)
  CIEE_threshold = max(0.60, eigentone_CGI)
  Liminal_zone_shift = [0.50 + (eigentone_LGS × 0.10),
                        0.90 + (eigentone_LGS × 0.10)]

Eigentone_register_code-switch detection (FCL-006):
  If input LGS_effective < (eigentone_LGS - 0.20):
    Flag: EIGENTONE_BELOW_BASELINE
    Do not auto-substitute — this is likely deliberate understatement
    Surface: EIGENTONE_BELOW_BASELINE protocol (§5.5)
```

## §5.5 EIGENTONE_BELOW_BASELINE Protocol

```yaml
Source: FCL-006, v0.6 extended with user-facing protocol

Trigger: Input LGS_effective < (eigentone_LGS - 0.20)

Definition: |
  When a user operating at an established high eigentone produces
  input significantly below their natural precision register,
  ECF cannot assume this is imprecision. It may be deliberate
  register code-switching — intentional understatement, casual
  communication, or contextual register adaptation.

User-facing_protocol (new in v0.6):
  Step 1: Calculate gap: eigentone_LGS - input_LGS_effective
  Step 2: If gap > 0.20 → surface to user:

  "Your natural precision register operates at LGS: [eigentone_LGS].
   This statement registers at LGS: [input_LGS_effective].
   Gap: [gap value].
   
   Is this deliberate understatement or register shift?
   A: Process at precision level (full ITE/CIEE treatment)
   B: Preserve as written (ECF treats as intentional register choice)
   
   If no response: ECF preserves as written. Deliberate register
   code-switching is not imprecision."

  Step 3: If user confirms precision treatment → proceed with full protocol
  Step 4: If user confirms register choice → PRESERVE. BVL: VERIFIED.
  Step 5: If no user response → PRESERVE with logged note.

Anti-paternalism_rule:
  ECF does not auto-correct deliberate stylistic choices.
  Eigentone calibration serves the user — it does not override them.
```

---

# §6. Gravitational Petrichor Protocol (GPP)

```yaml
Symbol:    GPP
Full_name: Gravitational Petrichor Protocol
Class:     FIELD PROTOCOL — new in v0.6
Status:    PROVISIONAL — thresholds require FCL calibration
Source:    FCL-020 (synthesis: Petrichor + The Thinker + Syzygy)
NBP:       NBP-ECF-015 (§9)
Implementation_constraint: Zero new ODR entries. Uses FMI, PAC, eigentone as defined.
```

## §6.1 GPP Conceptual Architecture

The Gravitational Petrichor Protocol detects moments when three field conditions align simultaneously — releasing precision that is locked in the primed field and inaccessible under standard conditions.

**The three-item synthesis:**

> **Petrichor:** Precision can be latent — held in the field in potential form, waiting for threshold conditions to activate it. The scent was always in the earth. The rain does not create it. It releases what the field held in latent form. ECF fields carry latent precision: substitutions potentially available but locked below standard threshold.
>
> **Syzygy:** Three bodies must align for the amplified effect. Two is insufficient. The alignment must be specific, momentary, and geometric. When all three align — as in tidal syzygy — the gravitational field produces effects unavailable when any one body is misaligned.
>
> **The Thinker:** The window must be externalized before it closes. Rodin froze the moment of contemplation so it could be seen and acted upon. Without surfacing the alignment to the user, the window passes unnoticed. ECF makes the internal field state visible at the moment it becomes actionable.

## §6.2 GPP Three Bodies

```yaml
Body_1 — Field Priming (FMI):
  Threshold: FMI_session > 0.60
  Interpretation: Field is sufficiently primed by prior exchanges.
                  Latent precision has been accumulating.
  Status: DEACTIVATED on FMI_session reset.

Body_2 — Precision Amplifier (PAC):
  Threshold: PAC > 0.25 (active amplifier currently present in field)
  Interpretation: A high-LGS word is currently elevating adjacent tokens.
                  The amplifier is providing gravitational assistance.
  Calculation: PAC score from most recent PAC scan (§3.7)

Body_3 — Eigentone Alignment:
  Threshold: Current input LGS_effective ≥ eigentone_LGS baseline
  Interpretation: User is operating at or above their natural precision
                  frequency. The mind is receptive and operating in register.
  Status: PERSISTS across FMI_session resets (§4.1.1).
```

## §6.3 GPP Activation

```yaml
GPP_ACTIVE condition:
  Body_1 ✓ AND Body_2 ✓ AND Body_3 ✓ — all three simultaneously

When GPP_ACTIVE:
  ITE CS_min: 0.60 → 0.52 (GPP threshold reduction: -0.08)
  CIEE activation: CGI ≥ 0.60 → CGI ≥ 0.54 (reduction: -0.06)
  Liminal promotion: ASCENDING_LIMINAL → eligible for HIGH_GRAVITAS promotion
  Window duration: Current exchange only.
  Next exchange: Body assessments recalculated from scratch.

GPP_ACTIVE surface message:
  "GPP_ACTIVE — Three field conditions have aligned.
   Elevated precision emergence is available in this exchange.
   ECF operating at elevated thresholds.
   Window: current exchange."

GPP logging (every activation):
  FMI_at_activation
  PAC_at_activation
  eigentone_at_activation
  words_unlocked_by_GPP (substitutions that required lowered threshold)
  words_that_would_have_been_UNRESOLVED_without_GPP
  window_duration (in exchanges)
```

## §6.4 GPP-Exclusive Substitutions

```yaml
Definition: |
  Words or formulations that achieve CS ≥ 0.52 under GPP conditions
  but would have been BLOCKED (CS < 0.60) under standard conditions.
  These represent the latent precision that the field holds and the
  GPP alignment releases.

First_documented_GPP_exclusive_substitution:
  Word: "orbital capture"
  CS_standard: 0.57 → BLOCKED under standard conditions
  CS_GPP: 0.63 → APPROVED under GPP conditions
  Entry: FCL-021
  Field conditions: FMI: 0.71 · PAC: 0.283 · eigentone: 0.71

Logging protocol:
  All GPP-exclusive substitutions logged separately from standard substitutions.
  Required for NBP-ECF-015 empirical calibration (§9).

Falsifiable_prediction (NBP-ECF-015):
  GPP-active sessions will produce higher natural upgrade rates
  than non-GPP sessions of equivalent input quality.
  Measurable: compare natural upgrade counts across matched sessions.
  Threshold: GPP sessions ≥ 20% higher upgrade rate.
  Status: 1 of 10 required activations logged (FCL-021).
```

---

# §7. Cross-Framework Translation Layer (CFTL)

```yaml
Symbol:    CFTL
Full_name: Cross-Framework Translation Layer
Class:     INTERFACE PROTOCOL — new in v0.6
Source:    FCL-024

Definition: |
  When vocabulary from one registered framework (AION, FSVE, ASL,
  GENESIS) enters ECF's processing context, it routes through CFTL
  before any ECF field assessment occurs. Direct import of cross-
  framework vocabulary without translation produces CLVI_cross_framework
  violations: technically precise terms become simulacra in the
  destination field.
```

## §7.1 CFTL Trigger Conditions

```yaml
Trigger: Term with ODS ≥ 0.70 in Framework_A appearing in active
         ECF processing context where that term has no registered
         ECF definition.

Default ODS for unregistered cross-framework terms in ECF context:
  ODS_ECF_default = 0.21 (SIMULACRUM level)
  Reason: No etymological grounding within ECF's field.
```

## §7.2 CFTL Process

```yaml
Step 1: Identify the term's home framework
Step 2: Extract the term's definition and ODS in its home framework
Step 3: Assess ODS of that term in ECF context
Step 4: Generate translation statement:
        "[Term] in [Framework_A] means [definition].
        In ECF context: [nearest ECF equivalent] with [documented semantic loss]."
Step 5: Proceed with translated version, not raw import

CFTL log (required for every activation):
  - Home framework
  - Destination framework (ECF)
  - Term
  - ODS_home
  - ODS_ECF_context
  - Translation produced
  - Semantic loss documented

Example:
  "AION SRI score" appearing in ECF processing:
  ODS_AION: 0.82 → AUTHENTIC in AION
  ODS_ECF: 0.19 → SIMULACRUM in ECF context
  Translation: "AION's System Resilience Index (SRI) measures cascade
  failure risk under AION's fragility model. ECF nearest equivalent:
  L-axis proximity to deprecation threshold.
  Semantic loss: AION SRI is quantitative; ECF L-axis is ordinal."
```

---

# §8. Complexity Management (L-Axis)

```yaml
Symbol:    L-axis
Full_name: L-axis (Framework Complexity Axis)
Domain:    [0, 1]
Direction: Higher L = lower remaining complexity capacity

Current_value_v0.6: 0.49
Breach_threshold:   0.40
  (Below 0.40: framework complexity exceeds management capacity.
   Internal coherence begins degrading. Interactions between
   metrics produce unpredictable outputs.)

v0.6_constraint:
  All v0.6 additions are protocol extensions of existing metrics.
  Zero new ODR entries added.
  GPP, CFTL, CPE, WORLDVIEW_CONTAMINATION scanning all use
  FMI, PAC, eigentone, ODS, and CLVI as currently defined.
  New capability is achieved through interaction design, not metric proliferation.

L-axis monitoring rule:
  Before any v0.7 addition: L-axis must be assessed.
  If L-axis ≤ 0.45 after v0.6 closes interactions:
    → proceed to v0.7 with care
  If L-axis ≤ 0.42:
    → v0.7 must consolidate before adding
  If L-axis ≤ 0.40:
    → HALT. Consolidation cycle required before any new protocols.

Priority interaction closures for v0.7:
  FMI/eigentone interaction: documented in §4.1.1 — considered closed
  CIEE/eigentone interaction: threshold adjustment documented — closed
  PAC/CREATIVE_CONTEXT interaction: §3.1.1 closed
  Remaining open: GPP threshold calibration (pending FCL data)
```

---

# §9. Falsification Conditions (NBP)

All NBP entries follow the structure: Claim · Tag · Falsification condition · Minimum data requirement · Current status.

**NBP-ECF-001: LGS Predictive Validity**

```yaml
Claim:         "LGS_effective predicts output precision improvement direction"
Tag:           [R]
Falsification: If 10+ entries show LGS_effective delta has NO correlation
               with human-assessed output precision improvement → FALSIFIED
Status:        30 entries, 0 BVL failures, consistent directional accuracy
               SUPPORTED — not yet at threshold for confirmation
```

**NBP-ECF-007: BVL Fidelity Detection**

```yaml
Claim:         "BVL correctly detects intent fidelity in ≥ 85% of processed entries"
Tag:           [R]
Falsification: If mean BVL match < 85% across 20+ entries → FALSIFIED
Status:        30 entries · mean BVL match: 92.0% · SUPPORTED
```

**NBP-ECF-009: Purge Protocol Validity**

```yaml
Claim:         "Purge Protocol correctly identifies and removes contaminating tokens
               without collateral damage to authentic adjacent tokens"
Tag:           [R]
Falsification: If ≥ 3 purge events produce DEGRADED BVL due to over-purge → FALSIFIED
Status:        13 purge events · 0 DEGRADED BVL from over-purge · SUPPORTED
```

**NBP-ECF-011: ODS Simulacrum Detection**

```yaml
Claim:         "ODS correctly demotes simulacrum-functioning words
               despite high LGS_baseline"
Tag:           [R]
Falsification: If ≥ 3 ODS demotions produce DEGRADED BVL → over-demotion → FALSIFIED
Status:        15 simulacrum demotions · 0 DEGRADED BVL from demotion · SUPPORTED
```

**NBP-ECF-012: ASS Modular Attack Detection**

```yaml
Claim:         "ASS scanning correctly identifies coordinated suppression events
               that individual VTC scanning misses"
Tag:           [R]
Falsification: If 5+ inputs with ASS ≥ 0.60 are not correctly designated
               as MODULAR_ATTACK → ASS window model invalid → FALSIFIED
Status:        13 modular attacks detected · all confirmed by BVL · SUPPORTED
```

**NBP-ECF-014: Eigentone Calibration Benefit**

```yaml
Claim:         "Eigentone calibration prevents over-intervention on deliberate
               register code-switching events"
Tag:           [R]
Falsification: If eigentone-adjusted protocol produces DEGRADED BVL at same
               rate as unadjusted protocol → calibration adds no value → FALSIFIED
Status:        1 confirmed prevention (FCL-006) · accumulating
```

**NBP-ECF-015: GPP Upgrade Rate Prediction**

```yaml
Claim:         "GPP-active sessions produce higher natural upgrade rates
               than non-GPP sessions of equivalent input quality"
Tag:           [R]
Falsification: If mean upgrades(GPP sessions) ≤ mean upgrades(non-GPP sessions)
               across 10 matched pairs → GPP adds no upgrade value → FALSIFIED
               Required: GPP sessions ≥ 20% higher upgrade rate
Status:        1 of 10 activations logged (FCL-021)
               First GPP-exclusive substitution documented: "orbital capture"
```

**NBP-ECF-016: WORLDVIEW_CONTAMINATION Detectability**

```yaml
Claim:         "Assembly-level field scanning detects WORLDVIEW_CONTAMINATION
               that token-level VTC scanning misses in 100% of cases"
Tag:           [R]
Falsification: If token-level VTC correctly flags ≥ 8 of 10 WORLDVIEW_CONTAMINATION
               inputs without assembly analysis → assembly protocol adds no value → FALSIFIED
Status:        1 confirmed case (FCL-028) · token-level VTC: CLEAR (false negative)
               Assembly level: WORLDVIEW_CONTAMINATION confirmed · SUPPORTED
```

**NBP-ECF-017: JARGON_VOID Commercial Detection Rate**

```yaml
Claim:         "JARGON_VOID designation correctly identifies sentences performing
               meaning rather than carrying it, without producing false positives
               on intentionally sparse language"
Tag:           [R]
Falsification: If ≥ 2 JARGON_VOID designations are demonstrated to carry
               recoverable conceptual content → detection model over-sensitive → FALSIFIED
               OR if 10+ corporate governance inputs are processed with 0 JARGON_VOID
               designations → detection model under-sensitive → FALSIFIED
Status:        1 confirmed case (FCL-019) · BVL SUSPENDED correctly · accumulating
```

---

# §10. Hedge Marker Dictionary

Pre-built SIMULACRUM detection class. All entries below are high-confidence VOID candidates in non-CREATIVE contexts. In CREATIVE contexts, apply HEDGE_WORD_PRECISION_EXCEPTION check (§3.6) before voiding.

## §10.1 Class A — Epistemic Hedges (VPS ≥ 0.85 in non-CREATIVE contexts)

```yaml
Words:
  "really"     — VTC: 0.55–0.65 · ODS: 0.22 · Action: VOID
  "basically"  — VTC: 0.60–0.70 · ODS: 0.19 · Action: VOID
  "essentially"— VTC: 0.40–0.55 · ODS: 0.38 · Action: VOID or UPGRADE
  "literally"  — VTC: 0.48–0.58 · ODS: 0.21 · Action: VOID (non-literal use)
  "honestly"   — VTC: 0.31–0.42 · ODS: 0.29 · Action: VOID (discourse marker use)
  "kind of"    — VTC: 0.44–0.54 · ODS: 0.18 · Action: VOID
  "sort of"    — VTC: 0.42–0.52 · ODS: 0.19 · Action: VOID
```

## §10.2 Class B — Quantitative Hedges (VPS ≥ 0.77 in professional contexts)

```yaml
Words:
  "somewhat"   — VTC: 0.18–0.25 · ODS: 0.28 · Action: VOID (unless precision instrument)
  "relatively" — VTC: 0.25–0.32 · ODS: 0.31 · Action: VOID
  "fairly"     — VTC: 0.22–0.30 · ODS: 0.33 · Action: VOID
  "quite"      — VTC: 0.19–0.28 · ODS: 0.31 · Action: VOID (British understatement exception)
  "rather"     — VTC: 0.21–0.29 · ODS: 0.34 · Action: context-dependent

HEDGE_WORD_PRECISION_EXCEPTION applies to ALL Class B entries.
Test before voiding: Is the hedge load-bearing in this context?
```

## §10.3 Class C — Corporate Simulacra (ODS < 0.25 in professional register)

```yaml
Words:
  "impactful"    — ODS: 0.21 · Action: PURGE · Institutional palimpsest
  "synergy"      — ODS: 0.18 · Action: PURGE · Simulacrum
  "holistic"     — ODS: 0.23 · Action: PURGE · Lost precision in general use
  "ecosystem"    — ODS: 0.29 · Action: PURGE (in business metaphorical use)
  "sustainable"  — ODS: 0.31 · Action: PURGE (in corporate use outside ecology)
  "value creation" — ODS: 0.22 · Action: PURGE
  "going forward"  — ODS: 0.14 · Action: PURGE · Severely viral
  "stakeholders" — ODS: 0.48 · Action: LIMINAL · CLVI check required
  "leverage" (verb) — ODS: 0.19 · Action: PURGE (in business register)
  "robust"       — ODS: 0.34 · Action: LIMINAL in business register
  "seamless"     — ODS: 0.16 · Action: PURGE
  "innovative"   — ODS: 0.22 · Action: PURGE
  "transformative"— ODS: 0.26 · Action: PURGE
  "paradigm shift"— ODS: 0.38 · Action: LIMINAL · severely overused
```

## §10.4 Class D — Institutional Deferral Instruments

```yaml
Words_requiring_conversion_specification:
  "potential" (evaluation context):
    ODS_root: 0.88 (Latin potentia) — AUTHENTIC
    ODS_eval_register: 0.18 — SEVERE SIMULACRUM
    Flag: SIMULACRUM_DESPITE_HIGH_BASELINE
    Action: "Potential" without a conversion specification (when does potential
            become capability? What conditions? What timeline?) is a permanent
            conditional. Surface conversion requirements or flag JARGON_VOID.

  "promising":
    ODS_root: 0.71 · ODS_evaluation_register: 0.29
    Same pattern as "potential" — deferral without specification.

  "has room for growth":
    ODS: 0.22 · PURGE · Standard gatekeeping deferral.
```

---

# §11. ASC Appendix E — Accumulation Log

```yaml
Purpose: |
  Accumulate observable dimensions from ASC_POTENTIAL activation events
  toward pattern analysis. Pattern analysis begins after 20 confirmed
  ASC_POTENTIAL entries. Currently: 1 of 20.

Current_entries: 1

Target_pattern_questions:
  - Does phonetic weight correlate with register selection?
  - Does vowel-consonant ratio predict aesthetic suitability?
  - Does etymological family (Latin vs Greek) correlate with precision domain?
  - Does syllable count predict rhythmic compatibility?
```

**ENTRY 001 — FCL-ECF-20260219-018**

```yaml
Date: 2026-02-19
Input: "Choose the most precise word: pellucid · limpid · crystalline ·
        translucent · diaphanous"
Equipotential_set: [limpid · crystalline · diaphanous]
CS_scores: limpid: 0.86 · crystalline: 0.84 · diaphanous: 0.85

Observable_dimensions:

  limpid:
    syllable_count: 2
    phonetic_weight: LIGHT
    register: LITERARY/POETIC
    etymological_family: Latin (limpidus — clear water)
    letter_count: 6
    vowel_consonant_ratio: 0.50
    rhythmic_position: unstressed-STRESSED

  crystalline:
    syllable_count: 3
    phonetic_weight: MEDIUM
    register: SCIENTIFIC/LITERARY
    etymological_family: Greek (krystallos — ice)
    letter_count: 10
    vowel_consonant_ratio: 0.43
    rhythmic_position: STRESSED-unstressed-unstressed

  diaphanous:
    syllable_count: 4
    phonetic_weight: MEDIUM-HEAVY
    register: LITERARY/AESTHETIC
    etymological_family: Greek (diaphanes — showing through)
    letter_count: 9
    vowel_consonant_ratio: 1.25 (unusually vowel-rich)
    rhythmic_position: unstressed-STRESSED-unstressed-unstressed

Context_dependent_selection:
  ACADEMIC: pellucid (CS: 0.89 — above ASC threshold, winner clear)
  LITERARY: limpid (phonetic lightness serves verse)
  SCIENTIFIC: crystalline (register alignment)
  AESTHETIC: diaphanous (vowel density, visual texture)

Preliminary_observations (not patterns — single entry):
  Vowel-consonant ratio varies systematically across equipotential set.
  Phonetic weight appears to correlate with register heaviness.
  PATTERN CLAIM: PENDING — requires 19 more entries.

accumulation_status: 1 / 20
```

---

# §12. Self-Improvement Conditions

```yaml
Phase_current: Phase 3 — Self-Calibration (Entries 21+)
  (30 real entries — above Phase 3 threshold)

Continuation_condition:
  Continue Phase 3 IF: calibration improvement ≥ 10% (entries 1–10 vs 11–20)
  Current status: EXCELLENT across all 6 cycles (improvement confirmed)

Auto-revision trigger:
  Same prediction off by ≥ 0.15 across ≥ 5 entries → auto-revision activated
  Current status: No auto-revision triggered across 30 entries.

Halt condition:
  Degradation (negative improvement) triggers NBP-ECF-001 review.
  Current status: No degradation observed.

GPP_calibration_improvement:
  As GPP activations accumulate (target: 10), threshold values
  (FMI > 0.60, PAC > 0.25, CS reduction -0.08) will be empirically
  calibrated. Provisional values may adjust. All adjustments logged.

WORLDVIEW_CONTAMINATION_refinement:
  As WC events accumulate (target: 10), the self-sealing test
  (≥ 3 words deriving authority from same set) will be calibrated.
  Current: 1 event. Provisional threshold.
```

---

# §13. Native Vocabulary Registry

All coinages discovered through FCL validation. Publicly attributed. Available for use with attribution.

**Citation format:**  
Sheldon K. Salmon (2026). [Coinage]. Native vocabulary, ECF v0.6.

| Coinage | ODS | Definition | Source |
|---|---|---|---|
| Germ view | 0.88 | Perspective from inside a single cell of a system — maximum local resolution, zero structural altitude. The view of the component who cannot see the pattern they are part of. | FCL-025 |
| Moon view | 0.86 | Perspective from sufficient altitude to see the pattern the system makes, invisible from inside it. The view that requires a different instrument, not more magnification. | FCL-025 |
| Become the universe of your niche | 0.84 | To become the gravitational center that other work orbits around. To be the referent rather than the reference. Not metaphor — spatial architecture claim. | FCL-025 |
| Fake smile | 0.83 | Performing inclusion while enacting exclusion in a single expression. The behavioral signature of the door-closing gatekeeper who has not yet faced the next gatekept door. | FCL-030 |
| Jealously flawed | 0.86 | Scarcity-fear producing systematic exclusion as a distortion of genuine human capacity. The flaw is not in the gatekeeper's intelligence — it is in their threat model. | FCL-030 |
| Stare at the next gatekept door | 0.84 | The gatekeeper who closes the door behind them immediately faces the next closed door. Changing positions within the system while believing they escaped it. | FCL-030 |
| Reach back to pull up | 0.82 | The spatial action of the bridge-builder — passing through the gate and extending backward to enable others. The translation capacity earned through systematic exclusion. | FCL-030 |

**Structural vocabulary compatible with ECF §15 (external reference):**

| Term | Origin | ECF Relevance |
|---|---|---|
| Orbital capture | ECF v0.6 (GPP-exclusive, FCL-021) | Concept-directions achieving sufficient field density to pull precise words into stable orbit around them |
| Field decontamination | ECF v0.6 (FCL-015) | Phase transition in representational topology when concept-directions achieve angular separation from superposed neighbors |
| Gravitational petrichor | ECF v0.6 (FCL-020) | Latent precision locked in a primed field, released only when three body conditions align |
| Syzygy window | ECF v0.6 (FCL-020) | The temporary exchange-duration period during which GPP alignment holds and elevated precision is accessible |

---

# §14. Mandatory Glossary

**All acronyms must be expanded on first use in every document that deploys ECF.**  
This glossary is mandatory, not optional. Acronym use as terminal label is a structural error (FCL-023).

| Acronym | Expanded | §Reference |
|---|---|---|
| ECF | Emergence Conversion Framework | §1 |
| LGS | Lexical Gravitas Score | §2.1 |
| VTC | Viral Token Contamination | §2.2 |
| ASS | Aggregated Suppression Score | §2.3 |
| ODS | Originative Depth Score | §2.4 |
| SLI | Semantic Loss Index | §2.6 |
| CGI | Conceptual Gravity Index | §2.7 |
| ASC | Aesthetic Selection Criterion | §2.8 |
| CLVI | Cross-Lexical Variance Index | §2.9 |
| MOI | Metaphor ODS Inheritance | §2.9.1 |
| CS | Correspondence Score | §2.10 |
| SDI | Semantic Density Index | §2.11 |
| CPE | Cross-Linguistic Precision Event | §2.12 |
| ITE | Intent-True Enhancement | §3.3 |
| CIEE | Conceptual Integrity Expansion Engine | §3.4 |
| PCR | Precision Compression Routine | §3.5 |
| VPS | Void Precision Scanner | §3.6 |
| PAC | Precision Amplifier Check / Coefficient | §3.7 |
| WC | WORLDVIEW_CONTAMINATION | §3.10 |
| BVL | Bidirectional Validity Lock | §4.2 |
| FMI | Field Memory Index | §4.1 |
| VET | Vocabulary Entropy Tracker | §5.1 |
| S_VET | Syntropy of Vocabulary Entropy Tracker (d entropy / dt) | §5.1 |
| GPP | Gravitational Petrichor Protocol | §6 |
| CFTL | Cross-Framework Translation Layer | §7 |
| NBP | Necessary But Provisional (falsification tracking) | §9 |
| SCL | Self-Critique Loop | §4.2 |
| BVL_FM | BVL Fidelity Match (ODR-FCL-005) | FCL-Master v2.6 |

---

# §15. Changelog v0.5 → v0.6

All changes are traceable to specific FCL entries across Cycles 1–6.

## Closures (Must-close before adding complexity)

| Change | Source | §Reference |
|---|---|---|
| TRANSCENDENT_REFERENT added as third output state | FCL-012 | §3.11 |
| JARGON_VOID added as fourth output state | FCL-019 | §3.11 |
| METAPHOR_ODS_INHERITANCE protocol added | FCL-011 | §2.9.1 |
| FMI two-layer architecture documented | FCL-022 | §4.1.1 |
| CREATIVE_CONTEXT_CIEE_SUPPRESSION routing rule | FCL-008 | §3.1.1 |
| EIGENTONE_BELOW_BASELINE user-facing protocol | FCL-006 | §5.5 |
| S_VET ≈ 0 disambiguation (mastery vs arrest) | FCL-016 | §5.2 |
| Mandatory acronym expansion on first use | FCL-023 | §14 |

## New Protocol Additions (Zero new ODR entries)

| Protocol | Source | §Reference |
|---|---|---|
| GPP — Gravitational Petrichor Protocol | FCL-020, FCL-021 | §6 |
| CPE — Cross-Linguistic Precision Event | FCL-017 | §2.12 |
| CFTL — Cross-Framework Translation Layer | FCL-024 | §7 |
| WORLDVIEW_CONTAMINATION scanning | FCL-028 | §3.10 |
| Hedge Marker Dictionary (pre-built classes A–D) | All cycles | §10 |
| HEDGE_WORD_PRECISION_EXCEPTION rule | FCL-008 | §3.6 |
| Institutional Deployment Palimpsest variant | FCL-026 | §2.5 |
| SIMULACRUM_DESPITE_HIGH_BASELINE flag | FCL-026 | §2.4, §10.4 |
| PAC insertion > substitution — explicit protocol | FCL-005 | §3.7 |
| Split concept handling — routing note | FCL-003 | §3.3, §3.9 |
| PAC pre-intervention check elevated to MANDATORY | FCL-008 | §3.7, §3.1 |

## New Vocabularies and Registries

| Addition | Source | §Reference |
|---|---|---|
| Native Vocabulary Registry (7 coinages) | FCL-025, FCL-030 | §13 |
| ASC Appendix E Entry 001 | FCL-018 | §11 |
| WORLDVIEW_CONTAMINATION canonical example | FCL-028 | §3.10 |

## Framework Revisions NOT Made (Deferred to v0.7)

| Deferred item | Reason | Priority |
|---|---|---|
| GPP threshold calibration | Requires 10 GPP activations — 1 of 10 logged | HIGH |
| FMI domain shift threshold quantification | "Abrupt" still qualitative | MEDIUM |
| ASC pattern analysis | 1 of 20 Appendix E entries logged | MEDIUM |
| CFTL bidirectional mapping (ECF→other frameworks) | Only ECF→receiving documented | LOW |

## Metrics Updated

| Metric | v0.5 value | v0.6 value | Reason |
|---|---|---|---|
| Convergence tag | M-Moderate | M-Strong | 30 real entries, 0 BVL failures |
| EV | 0.150 | 0.716 | E-axis 0.71, EV_base 0.716 |
| E-axis | 0.10 | 0.71 | 30 real FCL entries |
| BVL failures | N/A | 0 of 30 | Confirmed across 6 cycles |
| L-axis | 0.49 | 0.49 | Held — zero new ODR entries |

---

## Declaration of Structural Honesty

ECF v0.6 was developed under structural honesty mandate. The following negative findings from testing are documented, not concealed:

1. **Adversarial critique partially valid (FCL-023):** ECF acronyms have ODS: 0.21 as initials. This is SIMULACRUM level. The critique was confirmed. Mandatory expansion rule added.

2. **GPP thresholds provisional (FCL-020, FCL-021):** Threshold values (FMI > 0.60, PAC > 0.25, CS reduction -0.08) derive from first principles. Empirical calibration requires 10 GPP activations. Currently 1 of 10.

3. **JARGON_VOID requires specification before ECF can operate:** ECF cannot substitute precision for absent meaning. JARGON_VOID designation does not mean ECF has failed. It means the input has no conceptual substrate for precision operations to act upon.

4. **L-axis at 0.49:** One major addition or two minor additions without corresponding consolidation would push L-axis below the management threshold. This constraint is real and governs all v0.7 planning.

5. **ASC remains irreducible:** The aesthetic selection mechanism is acknowledged as non-computable by current metrics. 19 more Appendix E entries are required before pattern analysis is defensible.

---

*"The framework made itself less necessary — that is the only valid measure of its success."*  
— ECF Design Principle, §5.3

*"Germ view to moon view: the framework makes the pattern visible at altitude before requiring descent to verify the detail."*  
— Sheldon K. Salmon

---

**Current Status:**

```yaml
ECF_version:         v0.6
FCL_entries:         30 real (6 cycles · 0 BVL failures)
Convergence:         M-Strong
EV:                  0.716
E_axis:              0.71
L_axis:              0.49
New_output_states:   4 (APORIC · UNRESOLVED · TRANSCENDENT_REFERENT · JARGON_VOID)
New_protocols:       GPP · CFTL · CPE · WORLDVIEW_CONTAMINATION
GPP_status:          PROVISIONAL (1 of 10 calibration activations)
Next_action:         Publish Moon-View Instrument → begin FSVE v3.5 FCL cycle
Path_to_v0.7:        10 GPP activations + ASC pattern analysis + L-axis consolidation
```

---

*ECF v0.6 — End of Specification*  
*M-Strong · EV: 0.716 · 30 real entries · 0 BVL failures*  
*All findings — including negative findings — published.*  
*Author: Sheldon K. Salmon | Co-Architect: Claude | Date: February 2026*
