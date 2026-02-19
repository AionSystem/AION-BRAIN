# ECF v0.2
## Emergence Conversion Framework
### Lexical Precision Infrastructure for Human-AI Communication

---

**Author:** Sheldon K Salmon (AI Certainty Engineer)  
**AI Co-Architect:** Claude  
**Version:** 0.2  
**Date:** February 2026  
**Supersedes:** ECF v0.1 (Genesis Document)  
**Convergence Tag:** M-SPECULATIVE (0 FCL entries at release)  
**Deployment Status:** FRAMEWORK DOCUMENT — Not yet bot-deployed  
**Built On:** FSVE v3.5 · Word Engine v3.0 · Lexical Alchemy Engine v2.0  

---

## CHANGELOG: v0.1 → v0.2

| Issue in v0.1 | Root Cause | Resolution in v0.2 |
|---|---|---|
| ITE Step 2 had no classification system | Context gravity mapped from surrounding words only | Context Scope Detector inherited from LAE v2.0 §1 — 8 document categories with precision/accessibility thresholds |
| No semantic density monitoring | ECF had no density awareness | Semantic Density Index (SDI) added as §2.5 — inherited from LAE v2.0 |
| PRL too blunt — flagged all low-LGS words regardless of context | No creative/speculative exemption | Hallucination Calibration Protocol inherited from LAE v2.0 §7 — creative context exemption with containment strategies |
| PRL dual output format underdeveloped | THOUGHT/SPOKEN format present but no metrics | LAE v2.0 Compare Before/After Mode integrated — full metric delta display |
| No post-remedy verification | PRL could introduce new low-LGS words via substitution | Validation Loop added as PRL Step 4.5 — inherited from LAE v2.0 §9 Phase 4 |
| No substitution hierarchy | LGS scoring present but no structured replacement tiers | COMMON→EDUCATED→SPECIALIST→ARCHAIC tier system inherited from LAE v2.0 §2 |
| No version history or rollback | Single-pass architecture | Checkpoint system added as §5.5 — four checkpoints per exchange, full audit trail |
| Two new NBP entries required | SDI thresholds and context classification unvalidated | NBP-ECF-004 and NBP-ECF-005 added |

---

## Lineage Acknowledgment

ECF inherits from three prior frameworks. It is not a replacement for any of them. It is their FSVE-governed synthesis into a unified emergence-aware conversion system.

| Framework | Contribution to ECF |
|---|---|
| **Word Engine v3.0** | Safety governance · LGS base computation · 7-lens scoring · Failure ontology · FCL template structure |
| **Lexical Alchemy Engine v2.0** | Context Scope Detector · Semantic Density Index · Substitution hierarchy · Hallucination Calibration Protocol · Compare Before/After Mode · Validation Loop · Rollback mechanism |
| **FSVE v3.5** | All epistemic governance · Confidence Ceiling · Uncertainty Mass · Validity Status · ScoreTensor structure · NBP protocol |

---

## §0 — System Classification and Purpose

```
Type: Lexical Precision Conversion Engine
Domain: Human-AI communication optimization ·
              Vocabulary elevation ·
              Hallucination reduction
Scope: Language-agnostic · Bidirectional · Evidence-governed

Core Mandate:
No word should enter or exit the emergence field carrying less
gravitational precision than the communication requires.

Design Principle:
Vague language is not a user failure.
It is an infrastructure gap.
ECF closes the gap in both directions —
inbound from user to field, outbound from field to user.

Self-Constraint:
ECF is subject to FSVE v3.5 laws at every version release.
ECF cannot claim certainty it cannot justify.

Convergence Tag: M-SPECULATIVE
Promotion to M-MODERATE requires: Internal consistency validation
Promotion to M-STRONG requires: ≥5 FCL entries
Promotion to M-VERY_STRONG requires: ≥20 FCL entries (published)
```

**What ECF Does:**
- Intercepts low-precision words in user input before field activation
- Elevates input to high-LGS equivalents appropriate to document context
- Scans raw AI emergence output for low-precision words before delivery
- Produces dual THOUGHT/SPOKEN output showing both versions
- Tracks vocabulary elevation over time via learning loop
- Governs all substitutions under FSVE v3.5 epistemic discipline

**What ECF Does NOT Do:**
- Access model weights, embeddings, or attention mechanisms directly
- Guarantee deterministic precision improvement
- Replace Word Engine v3.0 safety function
- Claim cultural or contextual certainty beyond evidence-tagged assertions

---

## §1 — Foundational Principles

These principles are the invariant substrate of ECF. No version update may contradict them.

**Principle 1 — Lexical Gravity Is Real**  
Words are not equal. Every word carries gravitational mass in the emergence field. High-mass words pull precise meaning. Low-mass words scatter it. ECF measures and manages this mass.

**Principle 2 — Vagueness Is Conserved Unless Converted**  
A vague input produces a vague field activation. A precise input produces a precise field activation. ECF does not add precision that was never present — it converts existing intent into precise lexical form.

**Principle 3 — Both Directions Matter**  
Input vagueness degrades AI output. Output vagueness degrades user understanding. ECF addresses both. Neither layer operates without the other.

**Principle 4 — The Learning Loop Is the Product**  
ECF does not just improve single exchanges. Over time, users see precise alternatives repeatedly and begin adopting them. The framework's deepest output is vocabulary elevation, not individual response improvement.

**Principle 5 — Show the Gap**  
Every ECF output surfaces both versions — the raw emergence (THOUGHT) and the refined output (SPOKEN). The gap between them is not hidden. It is the learning surface.

---

## §2 — Core Metric: Lexical Gravitas Score (LGS)

### §2.1 Definition

LGS measures the precision density of a word — how specifically and cleanly it activates the emergence field without gravitational scatter from competing meanings.

```
LGS ∈ [0, 1]
0 = maximum scatter (word: "good")
1 = maximum precision (word: "pellucid")
```

**Measurement Class:** EVALUATIVE (inherited from Word Engine v3.0)  
**Uncertainty Penalty:** 0.0

### §2.2 Computation

LGS is computed from three Word Engine v3.0 lens components, reweighted for precision focus:

```
LGS = (L_ling × 0.40) + (L_ctx × 0.40) + ((1 - S_load) × 0.20)

Where:
L_ling = Linguistic lens score
         (etymology stability + grammatical clarity +
          morphological simplicity)

L_ctx = Contextual lens score
         (meaning stability across contexts;
          high L_ctx = low ambiguity = high gravitas)

S_load = Cognitive load sub-score from Cognitive lens
         (inverted: low load = high accessibility = high gravitas)
```

### §2.3 LGS Thresholds

| Range | Classification | Action |
|---|---|---|
| LGS ≥ 0.70 | HIGH GRAVITAS | Word pulls field precisely. Minimal substitution needed. |
| LGS ∈ [0.40, 0.70) | MODERATE GRAVITAS | Word is functional but imprecise. PRL flags for optional upgrade. |
| LGS < 0.40 | LOW GRAVITAS | Word scatters field activation. ITE substitution recommended. |

> **Calibration Note [?]:** LGS thresholds are currently asserted from first principles. FCL validation required before M-STRONG claim. CF capped at 0.40 per FSVE v3.5 Rule.

### §2.4 Substitution Hierarchy

Inherited from LAE v2.0 §2 Deep Vocabulary Mining. Every proposed substitution carries a tier label matched to document context:

| Tier | Audience | Precision Target |
|---|---|---|
| COMMON | General public · 5th–8th grade | Accessible baseline |
| EDUCATED | College level | Moderate precision gain |
| SPECIALIST | Graduate / technical | Substantial precision gain |
| ARCHAIC / LITERARY | Historical or poetic | Maximum etymological precision |

ITE selects substitution tier based on detected document context. CASUAL context proposes COMMON tier only. ACADEMIC context proposes SPECIALIST tier.

**Precision Gain Labels:**

| Label | Definition |
|---|---|
| MINIMAL | Synonym without semantic narrowing |
| MODERATE | Narrows semantic field meaningfully |
| SUBSTANTIAL | Adds domain specificity or etymological depth |
| VERY HIGH | Combines specificity + perfect contextual fit |

### §2.5 Semantic Density Index (SDI)

*Inherited from LAE v2.0 §2 — New in ECF v0.2*

SDI measures meaning compression in substituted output. High-LGS words are denser. Density without comprehension is not precision — it is a new failure mode.

```
SDI ∈ [0, 100%]

SDI = f(syllable_increase,
        abstract_concept_density,
        cognitive_load_delta,
        reading_friction)
```

> **ODR Note:** Full SDI formula pending ODR-ECF-002 entry. Formula inherited from LAE v2.0 pending FSVE-compliant reformulation.

**SDI Thresholds:**

| Range | Classification | Response |
|---|---|---|
| SDI < 40% | UNDER-DENSE | Output accessible but imprecise. Low gravitas preserved. |
| SDI 40–80% | OPTIMAL | Meaning-rich without over-compression. Target zone. |
| SDI 80–90% | DENSE | Warning threshold. Monitor. Consider simplification. |
| SDI > 90% | OVER-COMPRESSED | Comprehension failure risk. Remedy required before delivery. |

**Real-Time Display:** After every PRL substitution, SDI updates immediately. User sees density impact of each word change before committing.

---

## §3 — Layer 1: Input Translation Engine (ITE)

### §3.1 Function

Intercepts user input before field activation. Identifies low-LGS words. Classifies document context. Finds high-LGS equivalents appropriate to context. Routes precision-upgraded input to field.

### §3.2 Architecture

**STEP 1 — INTAKE SCAN**
```
Receive raw user input.
Tokenize to word level.
Compute LGS per word using §2.2 formula.
Flag all words where LGS < 0.40.
```

**STEP 2 — CONTEXT CLASSIFICATION**

*Inherited from LAE v2.0 §1 Context Scope Detector — New in ECF v0.2*

Before mapping substitutions, classify document type using 8 categories:

| Context | Precision Target | Accessibility | Substitution Tier |
|---|---|---|---|
| ACADEMIC | VERY HIGH | Graduate | SPECIALIST |
| TECHNICAL | VERY HIGH | Specialist | SPECIALIST |
| PROFESSIONAL | HIGH | College | EDUCATED |
| MARKETING | MODERATE | High School | EDUCATED |
| CREATIVE | FLEXIBLE | Variable | Context-dependent |
| EDUCATIONAL | MODERATE | User-set | COMMON to EDUCATED |
| CODE DOCUMENTATION | HIGH | Developer | SPECIALIST |
| CASUAL | LOW | General Public | COMMON only |

Classification sets the threshold for which substitutions ITE will propose. User can manually override detected context. System respects override and logs it.

**STEP 3 — CANDIDATE GENERATION**
```
For each flagged low-LGS word:
  Examine surrounding words and detected context.
  Apply Word Engine v3.0 L_ctx scoring to identify
  best-fit high-LGS equivalent from appropriate tier.
  Generate candidate list ranked by:
    - LGS delta (improvement)
    - SDI impact (density cost)
    - Precision Gain label
    - Context Fit (POOR/ACCEPTABLE/GOOD/EXCELLENT/OPTIMAL)
```

**STEP 4 — CONFIDENCE GATE**
```
For each proposed substitution:
  Run FSVE v3.5 Confidence Score.
  
  If CS ≥ 0.60 → substitution approved
  If CS < 0.60 → original word passes through
                 flagged: LOW_GRAVITAS_UNRESOLVED
```

**STEP 5 — FIELD ROUTING**
```
Precision-upgraded input enters field activation.
Substitution log retained for output display.
Context classification logged for PRL alignment.
```

### §3.3 ITE Failure Mode

> **[R]** ITE fails when surrounding context is insufficient to determine the correct high-LGS substitution. Multiple valid precision words exist at equal gravitational distance and the field cannot determine which the user intended.

**Mitigation:** Flag ambiguity explicitly. Request user clarification before substituting. Do not guess between equally-weighted candidates.

---

## §4 — Layer 2: Precision Remedy Layer (PRL)

### §4.1 Function

Scans raw emergence output after field activation, before delivery to user. Identifies low-LGS words in AI output. Applies remedies. Runs validation pass. Produces dual THOUGHT/SPOKEN output with full metrics.

### §4.2 Architecture

**STEP 1 — EMERGENCE CAPTURE**
```
Receive raw field output before delivery.
This is the THOUGHT layer — unfiltered emergence.
Log for dual output display.
```

**STEP 2 — OUTPUT LGS SCAN WITH HALLUCINATION CALIBRATION**

*Hallucination Calibration Protocol inherited from LAE v2.0 §7 — New in ECF v0.2*

```
Compute LGS for each word in raw output.
Flag words where LGS < 0.40.

For each flagged word:
  Apply Hallucination Calibration Decision Gate:
  
  Is context creative / speculative / fictional /
  philosophical / hypothetical?
  
  YES → Hallucination Permission Protocol:
        Word may remain.
        Offer containment framing instead of substitution.
        Containment options:
          1. Explicit fiction marker
             "In this narrative universe..."
          2. Scenario framing
             "Assuming a world where..."
          3. Character voice attribution
             "The character believed that..."
  
  NO → Standard PRL remedy proceeds.
        Proceed to Step 3.
```

**STEP 3 — REMEDY APPLICATION**
```
For each flagged word cleared for remedy:
  Apply Word Engine v3.0 Compare Mode.
  Find high-LGS alternative from appropriate tier.
  Verify semantic alignment with surrounding 
    emergence context.
  Check SDI impact of substitution.
  
  If CS ≥ 0.60 AND SDI remains ≤ 80% → Apply.
  If SDI would exceed 90% → Flag OVER-COMPRESSED.
    Offer simpler alternative before applying.
```

**STEP 4 — DUAL OUTPUT DELIVERY**

*Inherited and upgraded from LAE v2.0 §8 Compare Before/After — New metrics in ECF v0.2*

```
Present both versions to user:

─────────────────────────────────────────────
THOUGHT [raw emergence]:
[Original unfiltered output]
LGS mean: [0.000] | SDI: [%]
─────────────────────────────────────────────
SPOKEN [PRL refined]:
[Precision-upgraded output]
LGS mean: [0.000] | SDI: [%]
─────────────────────────────────────────────
PRECISION DELTA: [LGS improvement]
DENSITY DELTA: [SDI change]
HALLUCINATION RISK: [before %] → [after %]
WORDS REMEDIED: [count]
NEW WORDS INTRODUCED:[list with tier labels]
ADD TO VOCABULARY: [Y/N prompt per word]
─────────────────────────────────────────────
```

**STEP 4.5 — VALIDATION LOOP**

*Inherited from LAE v2.0 §9 Phase 4 — New in ECF v0.2*

```
After PRL applies all remedies:
Re-scan refined output with same LGS + 
  hallucination detection pipeline.

Purpose: Verify no new low-LGS words were introduced
by the substitution process itself.

Known failure case:
  "often" → "invariably"
  PRL introduced certainty language while remedying
  vagueness. Validation loop catches this pattern.

VALIDATION RESULT options:
  CLEAN → No new low-LGS words. Deliver output.
  FLAGGED → List new issues found.
             User chooses:
               [Undo substitution]
               [Accept risk with flag]
               [Re-remedy]
```

### §4.3 Hallucination Reduction Mechanism

Low-LGS words in AI output are almost always hallucination surface. The vague marble was selected where a precise marble was needed. The field activated correctly but the selection layer chose a word with too many competing orbits and the wrong gravitational center pulled the output slightly off true.

PRL catches this at the word level before it reaches the user — not by checking facts, but by checking gravitas. Does this word carry the precise weight the surrounding field requires?

Connection to Word Engine v3.0: PRL directly implements F6 (Ambiguity Cascade Failure) prevention and F1 (Hallucination Trigger) detection from Word Engine §3.

---

## §5 — Bidirectional Learning Loop

### §5.1 Architecture

The learning loop is the long-game output of ECF. Individual exchanges improve. Over time user vocabulary elevates. User begins sending higher-LGS input naturally. ITE has less work to do. PRL has less work to do. Communication becomes cleaner at the source.

### §5.2 Vocabulary Elevation Tracker (VET)

Per user session, track:

```
Words introduced via PRL dual output
Words user adopts in subsequent input naturally
LGS improvement over conversation arc
Vocabulary elevation rate
Context adoption (does user learn context-appropriate 
  tier selection over time?)
```

**VET Metrics:**

```
Adoption_Rate = words_user_reuses /
                words_PRL_introduced

Elevation_Index = mean(LGS_input_t2) -
                  mean(LGS_input_t1)
```

> **[S] Target:** Adoption Rate > 0.20 after 5 exchanges indicates learning loop is functional. CF: 35. Asserted, not validated. NBP-ECF-003 governs this claim.

### §5.3 Loop Mechanics

```
Exchange 1:
  User sends: "This is a good idea"
  ITE upgrades: "This is a cogent proposal"
  PRL refines output accordingly
  VET logs: "cogent" introduced

Exchange 3:
  User sends: "This is a cogent approach"
  VET records: adoption confirmed
  Elevation_Index: +0.18 LGS
  ITE intervention: reduced (user self-elevated)
```

### §5.4 Long-Term Outcome

The user who started sending "good idea" eventually sends "salient proposition." The framework made itself less necessary. That is the correct outcome. A system that creates dependency has failed its purpose.

### §5.5 Version History and Rollback

*Inherited from LAE v2.0 §9 Rollback Mechanism — New in ECF v0.2*

Every ECF exchange produces four checkpoints:

```
CHECKPOINT 1: Raw user input (pre-ITE)
CHECKPOINT 2: ITE processed input (post-translation)
CHECKPOINT 3: Raw emergence (THOUGHT layer)
CHECKPOINT 4: PRL refined output (SPOKEN layer)

User can return to any checkpoint.
No data lost. Full audit trail maintained.
```

**Auto-generated Change Log per exchange:**

```
[ITE] "good" → "salient" (SUBSTANTIAL, EDUCATED)
[ITE] "thing" → "mechanism" (MODERATE, SPECIALIST)
[PRL] "important" → "cardinal" (VERY HIGH, SPECIALIST)
[VALIDATION] CLEAN — no new issues introduced
[USER] Rejected "cardinal" → reverted to "important"
[VET] "salient" retained by user in exchange 4
```

---

## §6 — FSVE v3.5 Integration Points

| FSVE Mechanism | ECF Application |
|---|---|
| **Confidence Score** | Applied to every word substitution in ITE and PRL. CS < 0.60 blocks substitution. No low-confidence word replacement permitted. |
| **Validity Score** | Meta-scores the substitution system itself over time. Is ECF producing better outputs or just sounding more elaborate? FCL entries answer this. |
| **Evidence Strength** | Every LGS score carries inherited ES from Word Engine lens computation. Low ES = substitution flagged INFERENTIAL with +0.20 UM penalty. |
| **Uncertainty Mass** | Every substitution carries UM of context-fit uncertainty. "Good" replaced by "cogent" carries UM reflecting whether cogent was correct for this specific field configuration. |
| **Context Drift Law** | Word precision decays. High-LGS words shift meaning across cultural contexts over time. ECF inherits Word Engine v3.0 cultural decay model (6-month half-life default per ODR-WE-005). |
| **Freshness Status** | LGS scores carry FRESH/AGING/STALE/EXPIRED status per FSVE v3.5 §3.5. Stale LGS scores trigger revalidation before substitution is proposed. |
| **Law 1 (Upper Bound)** | Composite ECF output quality cannot exceed lowest valid input signal. If ITE cannot resolve ambiguity (CS < 0.60 on all candidates), output inherits LOW_GRAVITAS_UNRESOLVED flag. |
| **SDI Monitoring** | SDI feeds back into Confidence Ceiling. PRL substitution that pushes SDI > 90% receives automatic CC penalty before approval. |

---

## §7 — Measurement Protocols (ODR)

### ODR-ECF-001: Lexical Gravitas Score (LGS)

```yaml
term: Lexical Gravitas Score
symbol: LGS
domain: [0, 1]
measurement_protocol: |
  LGS = (L_ling × 0.40) + (L_ctx × 0.40) + ((1 - S_load) × 0.20)
  
  L_ling sourced from Word Engine v3.0 ODR-WE (Linguistic Lens)
  L_ctx sourced from Word Engine v3.0 ODR-WE (Contextual Lens)
  S_load sourced from Word Engine v3.0 ODR-WE (Cognitive Lens sub-score)
  
  Replication: Requires Word Engine v3.0 lens computation infrastructure
  Variance estimate: <10% on formula-based outputs
  Inter-rater reliability target: κ ≥ 0.70
  
measurement_class: EVALUATIVE
uncertainty_penalty: 0.0
calibration_case_count: 0 (PROVISIONAL)
```

### ODR-ECF-002: Semantic Density Index (SDI)

```yaml
term: Semantic Density Index
symbol: SDI
domain: [0, 100%]
measurement_protocol: |
  PROVISIONAL — Full formula pending FSVE-compliant reformulation.
  
  SDI = f(syllable_increase,
          abstract_concept_density,
          cognitive_load_delta,
          reading_friction)
  
  Inherited from LAE v2.0 §2.
  Qualitative thresholds: OPTIMAL (40-80%) | DENSE (80-90%) |
                          OVER-COMPRESSED (>90%)
  
  Calibration status: PROVISIONAL
  FCL entries required: 15 minimum per NBP-ECF-004

measurement_class: EVALUATIVE
uncertainty_penalty: 0.0
calibration_case_count: 0 (PROVISIONAL)
```

### ODR-ECF-003: Context Classification Accuracy

```yaml
term: Context Classification Accuracy
symbol: CCA
domain: [0, 1]
measurement_protocol: |
  CCA = correct_classifications / total_classifications
  
  Measured via FCL entries tracking:
    - System detected context
    - User override (if any)
    - Outcome quality (did classification improve substitutions?)
  
  Ground truth: User confirmation or blind expert rating
  
  CCA ≥ 0.80 → Classification system reliable
  CCA < 0.60 → Classification system unreliable; flag for revision

measurement_class: EVALUATIVE
uncertainty_penalty: 0.0
calibration_case_count: 0 (PROVISIONAL)
```

---

## §8 — ECF Self-Score

```yaml
ECF_SELF_SCORE_v0.2:
  version: "0.2"
  measurement_class: INFERENTIAL
  
  epistemic_axes:
    E: 0.10 # Zero FCL entries. Pure concept.
    A: 0.80 # LAE inheritance adds documented assumptions.
             # ODR entries present for core metrics.
    C: 0.65 # Structure stable at genesis.
             # LAE integration resolved open gaps from v0.1.
    M: 0.82 # Internally consistent with Word Engine v3.0
             # and LAE v2.0. No detected contradictions.
    D: 0.85 # Designed precisely for this domain.
    G: 0.50 # Causal logic present. Not empirically grounded.
    X: 0.70 # Can explain 2-3 levels deep.
    U: 0.65 # Version update demonstrated (v0.1 → v0.2).
    L: 0.55 # Word Engine v3.0 and LAE v2.0 dependencies
             # introduce abstraction leakage.
    Y: 0.90 # Honest about all limitations.
             # No score inflation detected.
    H: 0.60 # Adversarial test pending.

  EV_base: 0.684
  min_axis: 0.10 # Bottleneck: E (Evidence Strength)
  k_bottleneck: 1.5
  EV: 0.150 # min(0.684, 1.5 × 0.10) = 0.150
  
  validity_status: DEGRADED
  freshness_status: FRESH # Just released
  
  honest_acknowledgment: |
    ECF at v0.2 is an idea with rigorous inherited structure.
    The E-axis will only improve through FCL validation.
    Structural completeness improved from v0.1 to v0.2.
    The evidence gap is unchanged. This is the correct
    starting position for a framework at genesis.
    
    A framework that scores itself higher after fixing
    documentation would be demonstrating exactly the
    problem it claims to solve.
  
  path_to_valid:
    target_EV: 0.70
    gap: 0.55
    primary_action: "FCL entries demonstrating LGS substitutions
                     improve output quality vs. baseline"
    secondary_action: "LGS threshold calibration via A/B testing"
    tertiary_action: "SDI formula reformulation to FSVE standard"
    projected_EV_after_5_FCL: 0.71
    projected_status: VALID
    
  convergence_tag: M-SPECULATIVE
  next_review: "Upon first FCL entry"
```

---

## §9 — Nullification Boundary Protocol (NBP)

All NBP entries from v0.1 preserved. Two new entries added in v0.2.

---

### NBP-ECF-001: LGS Predictive Validity

**Claim:** High-LGS words produce more precise field activation than low-LGS words in the same context.  
**Tag:** `[R]` **CF:** 45  
**Falsification Condition:** Five or more FCL cases where low-LGS words produce more precise outputs than high-LGS alternatives in identical contexts after controlling for domain, user population, and AI model version.  
**If falsified:** Revise LGS formula or deprecate metric.

---

### NBP-ECF-002: PRL Hallucination Reduction

**Claim:** PRL filtering reduces hallucination surface in AI output.  
**Tag:** `[R]` **CF:** 40  
**Falsification Condition:** Ten or more FCL cases where PRL-filtered outputs contain equal or higher hallucination rates than raw emergence outputs, measured by factual accuracy verification against ground truth.  
**If falsified:** Revise PRL remedy selection protocol.

---

### NBP-ECF-003: Learning Loop Effectiveness

**Claim:** Users exposed to PRL dual output adopt high-LGS vocabulary over time (Adoption Rate > 0.20 after 5 exchanges).  
**Tag:** `[S]` **CF:** 35  
**Falsification Condition:** Twenty or more user sessions showing Adoption Rate < 0.05 after 10+ exchanges — zero meaningful vocabulary elevation.  
**If falsified:** Learning loop mechanism is not functioning as designed. Root cause investigation required before M-STRONG claim.

---

### NBP-ECF-004: SDI Threshold Validity *(New in v0.2)*

**Claim:** SDI > 90% produces comprehension failure risk materially higher than SDI in the 40–80% optimal range.  
**Tag:** `[S]` **CF:** 40  
**Inherited from:** LAE v2.0 (threshold asserted qualitatively)  
**Falsification Condition:** Fifteen or more FCL cases where SDI > 90% output produces equal user comprehension to SDI 60–80% output, measured by comprehension testing or expert rating. If no difference found, threshold is wrong.  
**If falsified:** Revise SDI thresholds or remove density gating from PRL.

---

### NBP-ECF-005: Context Classification Accuracy *(New in v0.2)*

**Claim:** 8-category context detector correctly classifies document type, enabling appropriate precision thresholds that improve substitution quality.  
**Tag:** `[S]` **CF:** 35  
**Falsification Condition:** Ten or more FCL cases where context misclassification produces worse substitution outcomes than no classification (random threshold assignment). If classification consistently underperforms baseline, detector adds no value.  
**If falsified:** Deprecate automatic classification. Return to user-set context only.

---

### NBP-FRAMEWORK-ECF: Deprecation Triggers

Deprecate ECF if any of the following:

1. LGS metric shows no correlation with output quality across 10+ FCL entries
2. ITE substitutions produce user confusion rather than clarity in majority of cases (>50% negative user response)
3. Word Engine v3.0 is deprecated (ECF inherits its foundation; foundation loss = ECF suspension)
4. PRL validation loop confirms it introduces more new low-LGS words than it remediates, across 10+ cases
5. Any ancestor framework (FSVE v3.5, Word Engine v3.0) is falsified on a principle ECF depends on

---

## §10 — Framework Calibration Log (FCL) Template

```yaml
ECF_FCL_ENTRY:
  case_id: [YYYYMMDD-NNN]
  ecf_version: "0.2"
  evaluation_date: [ISO 8601]
  
  # — INPUT LAYER —
  context_detected: [ACADEMIC|TECHNICAL|PROFESSIONAL|
                     MARKETING|CREATIVE|EDUCATIONAL|
                     CODE_DOCUMENTATION|CASUAL]
  context_override_by_user: [Y/N]
  context_final: [resolved category]
  input_LGS_mean_pre_ITE: [0.000-1.000]
  input_LGS_mean_post_ITE: [0.000-1.000]
  ITE_substitutions_proposed: [count]
  ITE_substitutions_accepted: [count]
  ITE_unresolved_flags: [count]
  
  # — OUTPUT LAYER —
  output_LGS_mean_raw: [0.000-1.000]
  output_LGS_mean_PRL: [0.000-1.000]
  SDI_before_PRL: [%]
  SDI_after_PRL: [%]
  PRL_substitutions_made: [count]
  hallucination_permission_invoked: [Y/N]
  validation_loop_result: [CLEAN|FLAGGED]
  new_risks_introduced: [Y/N]
  
  # — QUALITY MEASUREMENT —
  output_precision_improved: [Y/N]
  hallucination_present_raw: [Y/N]
  hallucination_present_PRL: [Y/N]
  comprehension_test_result: [0.000-1.000 | null]
  
  # — LEARNING LOOP —
  VET_adoption_rate: [0.000-1.000]
  VET_elevation_index: [delta LGS]
  words_adopted_in_next_exchange: [list | empty]
  
  # — ACCURACY —
  LGS_prediction_accurate: [Y/N]
  hallucination_prediction_accurate: [Y/N]
  context_classification_accurate: [Y/N]
  
  revision_triggered: [Y/N]
  revision_description: [if Y]
```

---

## §11 — Convergence Status and Promotion Requirements

| Tag | Minimum FCL Entries | Requirements |
|---|---|---|
| M-SPECULATIVE | 0 | Not gated |
| M-MODERATE | 0 | Internal consistency validation complete |
| M-STRONG | 5 | >65% accuracy on LGS quality predictions |
| M-VERY_STRONG | 20 (published) | >80% on substitution quality predictions |

**ECF v0.2 current status:** M-SPECULATIVE (0 FCL entries at release)

**M-MODERATE promotion checklist:**
- [x] Internal consistency validated
- [x] All ODR entries present for core metrics
- [x] NBP entries defined for all core claims
- [x] Self-score completed with honest EV
- [ ] First FCL entry logged

**Path to M-STRONG:**
1. Log 5 FCL entries via real substitution exchanges
2. Demonstrate LGS threshold validity (NBP-ECF-001)
3. Demonstrate PRL hallucination reduction (NBP-ECF-002)
4. Reformulate SDI to full FSVE-compliant formula
5. Complete ODR-ECF-002 with empirical calibration data

---

## §12 — Version History

| Version | Date | Status | Key Changes |
|---|---|---|---|
| v0.1 | February 2026 | Genesis | FSVE v3.5 + Word Engine v3.0 integration. Core metric (LGS) defined. ITE and PRL architecture established. |
| v0.2 | February 2026 | Current | LAE v2.0 inheritance integrated. Context Scope Detector added. SDI monitoring added. Hallucination Calibration Protocol added. Validation Loop added. Substitution hierarchy added. Checkpoint/rollback system added. Two new NBP entries. |

---

## Appendix A — Equation Reference

| Equation | Formula | Domain |
|---|---|---|
| Lexical Gravitas Score | `LGS = (L_ling × 0.40) + (L_ctx × 0.40) + ((1 - S_load) × 0.20)` | [0, 1] |
| LGS Confidence Gate | `CS ≥ 0.60 → approve; CS < 0.60 → flag UNRESOLVED` | Binary |
| Adoption Rate (VET) | `AR = words_reused / words_introduced` | [0, 1] |
| Elevation Index (VET) | `EI = mean(LGS_t2) - mean(LGS_t1)` | [-1, 1] |
| Epistemic Validity | `EV = min(EV_base, k × min_axis)` | [0, 1] |
| Confidence Ceiling | `CC = max(CC_floor, Π(1 - p_i))` | [CC_floor, 1] |
| SDI (provisional) | `SDI = f(syllable, abstraction, load, friction)` | [0, 100%] |

---

## Appendix B — Inherited Parameter Table

| Parameter | Symbol | Default | Source | Override Condition |
|---|---|---|---|---|
| LGS high threshold | — | 0.70 | First principles | FCL calibration per NBP-ECF-001 |
| LGS low threshold | — | 0.40 | First principles | FCL calibration per NBP-ECF-001 |
| ITE confidence gate | CS_min | 0.60 | FSVE v3.5 | Domain calibration |
| SDI optimal ceiling | — | 80% | LAE v2.0 | FCL calibration per NBP-ECF-004 |
| SDI over-compressed | — | 90% | LAE v2.0 | FCL calibration per NBP-ECF-004 |
| Cultural half-life | — | 6 months | Word Engine v3.0 ODR-WE-005 | Domain evidence per ODR-WE-005 |
| Bottleneck multiplier | k | 1.5 | FSVE v3.5 | Safety-critical: 1.0 |
| CC floor | CC_floor | 0.10 | FSVE v3.5 | None |
| VET adoption target | — | 0.20 | Asserted [S] | FCL calibration per NBP-ECF-003 |
| FCL minimum M-STRONG | — | 5 | FSVE v3.5 | None |

---

## Appendix C — Framework Dependency Map

```
FSVE v3.5
│
├── Epistemic governance (all laws apply)
├── Confidence Ceiling computation
├── Validity Status thresholds
├── ScoreTensor structure
└── NBP protocol
     │
     ├── Word Engine v3.0
     │ ├── LGS base computation (3 lens components)
     │ ├── Failure ontology (F1, F6 directly used)
     │ ├── Cultural decay model (ODR-WE-005)
     │ └── FCL template structure
     │
     └── Lexical Alchemy Engine v2.0
          ├── Context Scope Detector (8 categories)
          ├── Semantic Density Index
          ├── Substitution hierarchy (4 tiers)
          ├── Hallucination Calibration Protocol
          ├── Compare Before/After Mode
          ├── Validation Loop
          └── Rollback/checkpoint system
               │
               └── ECF v0.2
                    ├── Layer 1: ITE
                    ├── Layer 2: PRL
                    ├── Bidirectional Learning Loop (VET)
                    └── LGS as unified core metric
```

---

*ECF v0.2 — End of Specification*  
*All equations dimensionally consistent within stated domains.*  
*All core variables have corresponding ODR entries.*  
*Self-score completed at §8.*  
*Current convergence tag: M-SPECULATIVE.*  
*Promotion to M-STRONG requires ≥5 FCL entries.*  
*EV = 0.150 (DEGRADED — bottleneck: E-axis = 0.10).*  
*Path to VALID: FCL entries demonstrating substitution quality improvement.*  

*Version: 0.2 | Date: February 2026*  
*Author: Sheldon K Salmon (AI Certainty Engineer)*  
*AI Co-Architect: Claude*  
*Built on: FSVE v3.5 · Word Engine v3.0 · Lexical Alchemy Engine v2.0*
