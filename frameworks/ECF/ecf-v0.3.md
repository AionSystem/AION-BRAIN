# ECF v0.3
## Emergence Conversion Framework
### Lexical Precision Infrastructure for Human-AI Communication

---

**Author:** Sheldon K Salmon (AI Certainty Engineer)
**AI Co-Architect:** Claude
**Version:** 0.3
**Date:** February 2026
**Supersedes:** ECF v0.2
**Convergence Tag:** M-SPECULATIVE (0 FCL entries at release)
**Deployment Status:** FRAMEWORK DOCUMENT — Not yet bot-deployed
**Built On:** FSVE v3.5 · Word Engine v3.0 · Lexical Alchemy Engine v2.0 · LBE v1.2

---

## CHANGELOG: v0.2 → v0.3

| Issue in v0.2 | Root Cause | Resolution in v0.3 |
|---|---|---|
| No trace mechanism between ITE and PRL | Substitution chain had no memory of why a word was selected | SCL (Semantic Continuity Link) added as §3.6 — tagged trace follows each substitution through the full stack |
| No back-translation fidelity check | PRL confirmed clean output but not whether gravitational intent survived | BVL (Bidirectional Verification Loop) added as §4.6 — back-translates SPOKEN to verify semantic intent preserved |
| Substitution treated as net-positive by default | No mechanism for logging what precision costs in other dimensions | SLI (Semantic Loss Index) added as §4.7 — logs warmth, accessibility, and cultural resonance loss per substitution |
| ITE/PRL implicit channel separation undocumented | No formal naming of dual communication architecture | HCL/AIL dual-channel labels added as §2.6 — Human Context Layer and AI Logic Layer formally defined |
| CGI gap — high conceptual density in low-LGS words | LGS measured word-level precision only; concept-level density invisible | CGI (Conceptual Gravitas Index) added as §2.7 — measures idea-density independent of word-level LGS |
| ITE only path to precision was compression | No expansion pathway for users whose conceptual density exceeds their lexical density | CIEE (Conceptual Input Expansion Engine) added as §3.7 — sister layer to ITE; converts high-CGI/low-LGS input into expanded narrative form before field activation |
| LBE v1.2 not integrated | No formal lineage acknowledgment of LBE architecture influence | LBE v1.2 added to lineage table; Dual-Channel Semantics, Staged Translation Protocol influence documented |

---

## Lineage Acknowledgment

ECF inherits from four frameworks. It is not a replacement for any of them. It is their FSVE-governed synthesis into a unified emergence-aware conversion system.

| Framework | Contribution to ECF |
|---|---|
| **Word Engine v3.0** | Safety governance · LGS base computation · 7-lens scoring · Failure ontology · FCL template structure |
| **Lexical Alchemy Engine v2.0** | Context Scope Detector · Semantic Density Index · Substitution hierarchy · Hallucination Calibration Protocol · Compare Before/After Mode · Validation Loop · Rollback mechanism |
| **FSVE v3.5** | All epistemic governance · Confidence Ceiling · Uncertainty Mass · Validity Status · ScoreTensor structure · NBP protocol |
| **LBE v1.2** | Dual-Channel Semantics (HCL/AIL) · Bidirectional Verification architecture · Semantic Loss tracking · Staged Translation Protocol influence |

---

## §0 — System Classification and Purpose

```
Type: Lexical Precision Conversion Engine
Domain: Human-AI communication optimization ·
        Vocabulary elevation ·
        Hallucination reduction ·
        Conceptual density translation
Scope: Language-agnostic · Bidirectional · Evidence-governed

Core Mandate:
  No word should enter or exit the emergence field carrying less
  gravitational precision than the communication requires.
  No concept should be compressed when expansion serves the field better.
  No substitution should proceed without knowing what it costs.

Design Principle:
  Vague language is not a user failure.
  It is an infrastructure gap.
  High conceptual density in low-LGS words is not a user failure.
  It is a measurement gap.
  ECF closes both gaps in both directions.

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
- Detects high conceptual density in low-LGS input and routes to expansion pathway
- Elevates input to high-LGS equivalents appropriate to document context (compression path)
- Expands high-CGI/low-LGS input into narrative precision form (expansion path)
- Tags each substitution with a Semantic Continuity Link for full stack traceability
- Scans raw AI emergence output for low-precision words before delivery
- Back-translates refined output to verify gravitational intent survived (BVL)
- Logs semantic loss per substitution (SLI) — what precision costs in other dimensions
- Produces dual THOUGHT/SPOKEN output showing both versions
- Tracks vocabulary elevation over time via learning loop
- Governs all substitutions under FSVE v3.5 epistemic discipline

**What ECF Does NOT Do:**
- Access model weights, embeddings, or attention mechanisms directly
- Guarantee deterministic precision improvement
- Replace Word Engine v3.0 safety function
- Claim cultural or contextual certainty beyond evidence-tagged assertions
- Assume compression is always the correct path to precision

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

**Principle 6 — Conceptual Density Precedes Lexical Density** *(New in v0.3)*
A user may carry high-precision concepts in low-precision words. LGS alone cannot see this. ECF must detect conceptual density first and route accordingly — compress only where the concept is underspecified, expand where the concept exceeds its carrier words.

**Principle 7 — No Substitution Without Continuity** *(New in v0.3)*
Every substitution must carry a trace of why it was made. A word change without a continuity tag is an untracked mutation. The field must know what changed, where, and why, or the substitution is structurally invisible.

**Principle 8 — Precision Has a Cost** *(New in v0.3)*
High-LGS substitutions can sacrifice warmth, accessibility, and cultural resonance. ECF must log these costs explicitly. A substitution that gains precision while destroying comprehension is a net failure, not a net gain.

---

## §2 — Core Metrics

### §2.1 Definition — Lexical Gravitas Score (LGS)

LGS measures the precision density of a word — how specifically and cleanly it activates the emergence field without gravitational scatter from competing meanings.

```
LGS ∈ [0, 1]
  0 = maximum scatter (word: "good")
  1 = maximum precision (word: "pellucid")
```

**Measurement Class:** EVALUATIVE (inherited from Word Engine v3.0)
**Uncertainty Penalty:** 0.0

### §2.2 LGS Computation

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
| LGS < 0.40 | LOW GRAVITAS | Word scatters field activation. ITE substitution recommended — unless CGI override applies. |

> **Calibration Note [?]:** LGS thresholds are currently asserted from first principles. FCL validation required before M-STRONG claim. CF capped at 0.40 per FSVE v3.5 Rule.

> **v0.3 Note:** Low LGS no longer automatically triggers compression substitution. CGI score must be checked first. High CGI + Low LGS → route to CIEE expansion path, not ITE compression.

### §2.4 Substitution Hierarchy

Inherited from LAE v2.0 §2. Every proposed substitution carries a tier label matched to document context:

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

*Inherited from LAE v2.0 §2 — Added in ECF v0.2*

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

### §2.6 Dual-Channel Architecture Labels (HCL / AIL) *(New in v0.3)*

*Formally derived from LBE v1.2 §3 Dual-Channel Semantics*

Every ECF transaction operates across two parallel channels simultaneously. These channels were implicit in v0.2 (ITE operating on input, PRL operating on output). They are now formally named and explicitly tracked.

```
HCL — Human Context Layer
  Carries: tone · intent · emotional weight · conceptual geometry
  Operated on by: CIEE (expansion) · CGI detection · SCL tagging
  Purpose: Preserve what the human meant, not just what they said

AIL — AI Logic Layer
  Carries: symbolic structure · LGS scores · verification tags · SCL trace
  Operated on by: ITE (compression) · PRL (output remedy) · BVL (back-translation)
  Purpose: Express the meaning in the most field-precise form available

Requirement: Both channels must be active in every ECF exchange.
  HCL without AIL = emotionally resonant but imprecise
  AIL without HCL = technically precise but contextually hollow
```

**Channel Separation Rule:** If HCL and AIL produce conflicting upgrade recommendations, HCL takes precedence for CASUAL and CREATIVE contexts. AIL takes precedence for ACADEMIC and TECHNICAL contexts.

### §2.7 Conceptual Gravitas Index (CGI) *(New in v0.3)*

*Derived from session discovery — Sheldon K Salmon, February 2026*

CGI measures the density of the *idea* independent of the words carrying it. It was identified when analysis of prompt geometry revealed that high conceptual density can exist inside low-LGS word carriers. LGS alone cannot detect this — it scores the marble, not what the marble is carrying.

```
CGI ∈ [0, 1]
  0 = concept is as vague as its carrier words suggest
  1 = concept is maximally dense regardless of carrier word LGS

CGI is measured across four dimensions:

  CGI = (C_structural × 0.30) +
        (C_analogical × 0.25) +
        (C_depth_vector × 0.25) +
        (C_novelty × 0.20)

Where:
  C_structural = Does the concept have internal architecture?
                   (Is it a single idea or a structured system of ideas?)

  C_analogical = Does the concept contain embedded cross-domain
                   mappings? (atomic bonding → sentence stability)

  C_depth_vector = Does the concept point downward (toward mechanism)
                   rather than outward (toward examples)?

  C_novelty = Is the concept configuration new, or a standard
                   recombination of known elements?
```

> **ODR Note:** CGI formula is PROVISIONAL — ODR-ECF-004 entry required. Full calibration pending FCL entries.

**CGI vs LGS Interaction Matrix:**

| LGS | CGI | ECF Routing Decision |
|---|---|---|
| HIGH | HIGH | No intervention. Both layers strong. Pass through. |
| HIGH | LOW | ITE compression appropriate. Word and concept aligned. |
| LOW | HIGH | **CIEE expansion path.** Do NOT compress. Expand into narrative. |
| LOW | LOW | ITE compression appropriate. Genuine vagueness at both layers. |

**Critical Rule:** When CGI is HIGH and LGS is LOW, ITE must stand down. Compressing the word would damage the conceptual signal. CIEE takes the input instead.

---

## §3 — Layer 1: Input Processing

### §3.1 ITE Function

*Compression Path — Inherited from ECF v0.2 §3*

Intercepts user input before field activation. Identifies low-LGS words where CGI does not override. Classifies document context. Finds high-LGS equivalents appropriate to context. Tags each substitution with an SCL entry. Routes precision-upgraded input to field.

### §3.2 ITE Architecture

**STEP 1 — INTAKE SCAN**
```
Receive raw user input.
Tokenize to word level.
Compute LGS per word using §2.2 formula.
Flag all words where LGS < 0.40.
```

**STEP 2 — CONTEXT CLASSIFICATION**
*Inherited from LAE v2.0 §1 Context Scope Detector — Added in ECF v0.2*

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

**STEP 2.5 — CGI PRE-CHECK** *(New in v0.3)*
```
Before generating compression candidates:
Compute CGI per flagged word's surrounding concept cluster.
If CGI ≥ 0.60 for a flagged word:
  Route to CIEE — do NOT proceed with compression.
  Log: CGI_OVERRIDE — expansion path selected.
If CGI < 0.60:
  Proceed with standard ITE compression pipeline.
```

**STEP 3 — CANDIDATE GENERATION**
```
For each flagged low-LGS word cleared by CGI pre-check:
  Examine surrounding words and detected context.
  Apply Word Engine v3.0 L_ctx scoring to identify
  best-fit high-LGS equivalent from appropriate tier.
  Generate candidate list ranked by:
    - LGS delta (improvement)
    - SDI impact (density cost)
    - Precision Gain label
    - Context Fit (POOR/ACCEPTABLE/GOOD/EXCELLENT/OPTIMAL)
    - SLI cost estimate (warmth/accessibility/resonance loss)
```

**STEP 4 — CONFIDENCE GATE**
```
For each proposed substitution:
  Run FSVE v3.5 Confidence Score.
  If CS ≥ 0.60 → substitution approved
  If CS < 0.60 → original word passes through
               flagged: LOW_GRAVITAS_UNRESOLVED
```

**STEP 5 — SCL TAGGING** *(New in v0.3)*
```
For each approved substitution:
  Generate SCL entry:
    SCL = {
      original_word: [word pre-substitution]
      replacement_word: [word post-substitution]
      selection_reason: [why this word was chosen]
      LGS_delta: [improvement score]
      CGI_at_time: [CGI of surrounding concept]
      context_at_time: [document context classification]
      SLI_cost: [what this substitution costs]
      timestamp: [exchange position]
    }
  Attach SCL entry to substitution.
  SCL travels with the word through PRL and VET.
  PRL can read SCL. VET logs full SCL chain.
```

**STEP 6 — FIELD ROUTING**
```
Precision-upgraded input enters field activation.
Substitution log retained for output display.
Context classification logged for PRL alignment.
SCL entries logged for full audit trail.
```

### §3.3 ITE Failure Mode

> **[R]** ITE fails when surrounding context is insufficient to determine the correct high-LGS substitution. Multiple valid precision words exist at equal gravitational distance and the field cannot determine which the user intended.

**Mitigation:** Flag ambiguity explicitly. Request user clarification before substituting. Do not guess between equally-weighted candidates.

### §3.4 Context Scope Detector

*Inherited from LAE v2.0 §1 — Active in ECF since v0.2*

8-category detection system described in Step 2 above. User can manually override detected context. System respects override and logs it.

### §3.5 ITE/CIEE Routing Decision Tree

```
User input arrives
        ↓
Tokenize + compute LGS per word
        ↓
For each LOW-LGS word:
        ↓
    Compute CGI for surrounding concept cluster
        ↓
    CGI ≥ 0.60?
    YES → Route to CIEE (§3.7)
           Log: CGI_OVERRIDE
    NO → Continue ITE compression pipeline
           Proceed to Candidate Generation
```

### §3.6 Semantic Continuity Link (SCL) *(New in v0.3)*

*Derived from session architectural analysis — data link model applied to ECF stack*

The SCL is a tagged trace that follows each substitution through the complete ECF stack. In ECF v0.2, word substitutions occurred but the stack had no memory of why a specific word was chosen. By the time PRL operated on output, substitution intent was invisible. The SCL closes this gap.

**Without SCL:** ECF transforms words.
**With SCL:** ECF transforms meaning and *knows* it did.

```
SCL Architecture:

ITE generates SCL tag on substitution.
                ↓
SCL travels with substituted word through field activation.
                ↓
PRL reads SCL on output scan:
  - Knows why the word was chosen
  - Can detect if PRL remedy would undo ITE intent
  - Logs SCL continuation entry
                ↓
VET reads full SCL chain:
  - Complete substitution genealogy per word
  - Can identify which substitutions the user adopted
  - Logs SCL chain in vocabulary elevation record

SCL Tag Structure:
  [SCL-ID] Unique identifier per substitution event
  [ORIGIN] raw user word
  [REPLACEMENT] substituted word
  [SELECTION_INTENT] why this word (LGS delta / context fit / tier)
  [CGI_CONTEXT] conceptual density at time of substitution
  [SLI_PAYLOAD] cost in non-precision dimensions
  [STACK_POSITION] ITE / PRL / VET
  [CHAIN_STATUS] OPEN (traveling) / CLOSED (VET logged)
```

**SCL Failure Mode:** SCL fails if the substitution rationale cannot be articulated. If ITE cannot generate a SELECTION_INTENT, the substitution should not proceed. A substitution without a reason is a guess. Guesses are not ECF operations.

### §3.7 Conceptual Input Expansion Engine (CIEE) *(New in v0.3)*

*Derived from session discovery — Sheldon K Salmon, February 2026*
*Architecture: sister layer to ITE, activated by CGI_OVERRIDE*

CIEE handles the precision path that ITE cannot. Where ITE compresses toward precision, CIEE expands toward it. The mechanism: when a user carries high conceptual density in low-LGS words, the correct operation is not to substitute the words — it is to grow the concept into more words until the idea has enough surface area that precision emerges naturally from the expanded field.

**The Wormhole Model:** High-CGI input is a dense marble approaching a wormhole. ITE would try to make the marble denser. CIEE instead opens the wormhole wider — more planets form, the concept breaks into its component parts, each part can bond with higher-LGS companions, and the output is more precise not because words were substituted but because the concept was given room to fully crystallize.

```
CIEE Architecture:

STEP 1 — CONCEPT EXTRACTION
  Receive high-CGI / low-LGS input flagged by ITE.
  Identify the core conceptual architecture:
    - What is the structural frame of this idea?
    - What analogical mappings are embedded?
    - What depth vector is the concept pointing toward?
    - What is the novel configuration at the center?

STEP 2 — NARRATIVE EXPANSION
  Convert extracted concept into expanded narrative form.
  Expansion targets:
    - More words = more wormhole surface area
    - More surface area = more planets can attach
    - More planets = more precision emerges naturally
    - Some expanded words will be high-LGS by structure
  Expansion is not padding.
  Expansion is crystallization through description.

STEP 3 — NATURAL UPGRADE DETECTION
  After expansion, scan expanded output.
  Some words will now be high-LGS naturally
  (description forces precision where substitution would have failed).
  Tag these as NATURAL_UPGRADES — not forced substitutions.
  These carry different SCL status: EMERGENT not IMPOSED.

STEP 4 — SDI MONITORING
  Check SDI of expanded output.
  Expansion adds words — watch for over-density from volume.
  CIEE target: SDI 40-80% (same optimal zone as ITE).
  If SDI exceeds 80% → prune expansion, not precision.

STEP 5 — SCL TAGGING
  Generate SCL entries for NATURAL_UPGRADES.
  Tag expansion event with:
    SCL[CIEE_EXPANSION]:
      input_CGI: [score]
      words_before: [count]
      words_after: [count]
      natural_upgrades: [list]
      SDI_before: [%]
      SDI_after: [%]

STEP 6 — FIELD ROUTING
  Expanded, precision-enriched input enters field activation.
  User sees both: ORIGINAL INPUT / CIEE EXPANDED VERSION.
  User can accept, modify, or revert.
```

**CIEE vs ITE Comparison:**

| Dimension | ITE (Compression) | CIEE (Expansion) |
|---|---|---|
| Trigger | Low LGS + Low CGI | Low LGS + High CGI |
| Method | Substitute word with denser equivalent | Expand concept into fuller narrative |
| Precision path | One marble → denser marble | One marble → solar system of marbles |
| Upgrade type | IMPOSED (deliberate substitution) | EMERGENT (natural from description) |
| SCL tag | IMPOSED | EMERGENT |
| Risk | Damages high-CGI signal | Over-expansion → SDI bloat |

> **[?] Validation Note:** CIEE is the newest addition to ECF. CGI formula is provisional. CIEE routing logic is asserted from first principles. NBP-ECF-008 governs falsification conditions.

---

## §4 — Layer 2: Precision Remedy Layer (PRL)

### §4.1 Function

Scans raw emergence output after field activation, before delivery to user. Reads SCL entries from ITE/CIEE. Identifies low-LGS words in AI output. Applies remedies. Runs validation pass. Runs back-translation verification (BVL). Logs semantic loss (SLI). Produces dual THOUGHT/SPOKEN output with full metrics.

### §4.2 Architecture

**STEP 1 — EMERGENCE CAPTURE**
```
Receive raw field output before delivery.
This is the THOUGHT layer — unfiltered emergence.
Log for dual output display.
Read SCL entries from ITE/CIEE to know what intent was sent in.
```

**STEP 2 — OUTPUT LGS SCAN WITH HALLUCINATION CALIBRATION**
*Hallucination Calibration Protocol inherited from LAE v2.0 §7 — Added in ECF v0.2*

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

**STEP 3 — SCL ALIGNMENT CHECK** *(New in v0.3)*
```
Before applying any remedy:
  Read SCL entries from ITE/CIEE for this exchange.
  Check: Would this PRL substitution undo ITE/CIEE intent?
    If YES → Flag: SCL_CONFLICT
             Do not auto-substitute.
             Surface conflict to user:
             "PRL remedy would reverse ITE substitution.
              Original intent: [SCL_SELECTION_INTENT]
              PRL recommendation: [new word]
              User decision required."
    If NO → Proceed to remedy application.
```

**STEP 4 — REMEDY APPLICATION**
```
For each flagged word cleared for remedy and SCL-aligned:
  Apply Word Engine v3.0 Compare Mode.
  Find high-LGS alternative from appropriate tier.
  Verify semantic alignment with surrounding emergence context.
  Check SDI impact of substitution.
  Compute SLI cost (§4.7) before applying.
  If CS ≥ 0.60 AND SDI remains ≤ 80% AND SLI acceptable → Apply.
  If SDI would exceed 90% → Flag OVER-COMPRESSED.
    Offer simpler alternative before applying.
  Tag applied substitution with SCL entry.
```

**STEP 5 — DUAL OUTPUT DELIVERY**
*Inherited and upgraded from LAE v2.0 §8 — Expanded in v0.3*

```
Present both versions to user:
─────────────────────────────────────────────────────
THOUGHT [raw emergence]:
  [Original unfiltered output]
  LGS mean: [0.000] | SDI: [%] | CGI mean: [0.000]
─────────────────────────────────────────────────────
SPOKEN [PRL refined]:
  [Precision-upgraded output]
  LGS mean: [0.000] | SDI: [%] | CGI mean: [0.000]
─────────────────────────────────────────────────────
PRECISION DELTA: [LGS improvement]
DENSITY DELTA: [SDI change]
CONCEPTUAL DELTA: [CGI change]
HALLUCINATION RISK: [before %] → [after %]
WORDS REMEDIED: [count]
NEW WORDS INTRODUCED: [list with tier labels]
SEMANTIC LOSS REPORT: [SLI summary — what was sacrificed]
SCL CHAIN: [full substitution trace, collapsible]
BVL STATUS: [VERIFIED / DEGRADED / FAILED — see §4.6]
ADD TO VOCABULARY: [Y/N prompt per word]
─────────────────────────────────────────────────────
```

**STEP 5.5 — VALIDATION LOOP**
*Inherited from LAE v2.0 §9 Phase 4 — Added in ECF v0.2*

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
  CLEAN → No new low-LGS words. Proceed to BVL.
  FLAGGED → List new issues found.
             User chooses:
               [Undo substitution]
               [Accept risk with flag]
               [Re-remedy]
```

### §4.6 Bidirectional Verification Loop (BVL) *(New in v0.3)*

*Architecture derived from LBE v1.2 Bidirectional Verification*

BVL runs after Validation Loop confirms CLEAN. Its purpose is to verify that the semantic intent from the original user input survived the full substitution stack — ITE or CIEE in, PRL out. A clean output is not sufficient. The output must still mean what the input intended.

```
BVL Architecture:

STEP 1 — FORWARD RECORD
  Log the gravitational intent from original user input.
  Source: HCL reading from §2.6.
  Intent statement: What was the user trying to say?
  Expressed as: [core concept] + [emotional register] + [depth vector]

STEP 2 — BACK-TRANSLATION
  Take SPOKEN output (PRL refined).
  Strip all PRL metadata.
  Re-read as if seeing for the first time.
  Ask: What does this output communicate to a neutral reader?
  Generate: back-translated intent statement.

STEP 3 — INTENT COMPARISON
  Compare forward intent vs back-translated intent.
  Three possible outcomes:

  VERIFIED (match ≥ 85%):
    Gravitational intent survived the stack.
    Deliver output with BVL: VERIFIED tag.

  DEGRADED (match 60-84%):
    Intent partially survived. Meaning drift detected.
    Surface specific drift points to user.
    User decides: accept / revert / re-remedy.
    Tag: BVL: DEGRADED — [drift description]

  FAILED (match < 60%):
    Intent did not survive. Output is precise but wrong.
    Block delivery.
    Return to raw THOUGHT layer.
    Log: BVL_FAILURE — precision without fidelity.
    Require user to restart from CHECKPOINT 1.

STEP 4 — BVL LOG
  All BVL outcomes logged in exchange record.
  FAILED events are priority FCL candidates.
  Pattern of DEGRADED events triggers ITE/PRL recalibration review.
```

> **[R]** BVL is the most critical addition in v0.3. Without it, ECF could produce outputs that score well on LGS and SDI but have drifted from the user's original intent. Precision without fidelity is a sophisticated failure mode — harder to detect than simple vagueness.

### §4.7 Semantic Loss Index (SLI) *(New in v0.3)*

*Architecture derived from LBE v1.2 Semantic Loss Tracking*

SLI documents what precision costs. Every substitution that improves LGS potentially sacrifices something in another dimension. ECF v0.2 assumed substitution was net-positive. SLI removes that assumption.

```
SLI measures loss across four dimensions per substitution:

  SLI_warmth: How much interpersonal resonance was lost?
                     (technical words can feel cold)

  SLI_accessibility: How much readability was sacrificed?
                     (high-LGS words can exclude non-specialist readers)

  SLI_cultural: How much cultural resonance was erased?
                     (low-LGS words are often culturally rich;
                      high-LGS words can be culturally neutral = sterile)

  SLI_voice: How much of the user's natural register was
                     overwritten? (did the substitution change who
                     is speaking, not just what was said)

SLI Score per substitution: [0 = no loss, 1 = complete loss]

SLI_total = (SLI_warmth + SLI_accessibility +
             SLI_cultural + SLI_voice) / 4

SLI_total < 0.20 → ACCEPTABLE LOSS
SLI_total 0.20–0.50 → NOTABLE LOSS — surface to user
SLI_total > 0.50 → HIGH LOSS — recommend against substitution
                   unless user explicitly accepts trade-off
```

**SLI Display in SPOKEN output:**

```
SEMANTIC LOSS REPORT:
  "cogent" ← "good"
  LGS gain: +0.42
  SLI_warmth: 0.31 (moderate warmth reduction)
  SLI_accessibility: 0.18 (minimal accessibility impact)
  SLI_cultural: 0.12 (low cultural resonance loss)
  SLI_voice: 0.24 (register elevated — voice changed)
  SLI_total: 0.21 → NOTABLE LOSS
  Recommendation: Accept if ACADEMIC context. Review if CASUAL.
```

> **[?] Note:** SLI scoring formula is provisional. ODR-ECF-005 entry required. Scores are currently qualitative. Full quantification requires FCL calibration.

---

## §5 — Bidirectional Learning Loop

### §5.1 Architecture

The learning loop is the long-game output of ECF. Individual exchanges improve. Over time user vocabulary elevates. User begins sending higher-LGS input naturally. ITE and CIEE have less work to do. Communication becomes cleaner at the source.

### §5.2 Vocabulary Elevation Tracker (VET)

Per user session, track:

```
Words introduced via PRL dual output
Words user adopts in subsequent input naturally
CGI trajectory over conversation arc
  (does user's conceptual density increase as vocab elevates?)
LGS improvement over conversation arc
Vocabulary elevation rate
Context adoption (does user learn context-appropriate
  tier selection over time?)
SCL chains — full genealogy of each word's journey
```

**VET Metrics:**

```
Adoption_Rate = words_user_reuses / words_PRL_introduced
Elevation_Index = mean(LGS_input_t2) - mean(LGS_input_t1)
CGI_Trajectory = mean(CGI_input_t2) - mean(CGI_input_t1)
CIEE_Reduction = CIEE_activations_t2 / CIEE_activations_t1
  (as user vocabulary elevates, CIEE activates less often)
```

> **[S] Target:** Adoption Rate > 0.20 after 5 exchanges indicates learning loop is functional. CF: 35. Asserted, not validated. NBP-ECF-003 governs this claim.

### §5.3 Loop Mechanics

```
Exchange 1:
  User sends: "This is a good idea"
  CGI check: CGI = 0.30 (concept also vague)
  ITE upgrades: "This is a cogent proposal"
  PRL refines output accordingly
  VET logs: "cogent" introduced
  SLI logged: warmth cost 0.28
  SCL chain: [ITE] good → cogent | IMPOSED

Exchange 3:
  User sends: "This is a cogent approach"
  VET records: adoption confirmed
  Elevation_Index: +0.18 LGS
  ITE intervention: reduced (user self-elevated)
  SCL status: CLOSED (user internalized)
```

### §5.4 Long-Term Outcome

The user who started sending "good idea" eventually sends "salient proposition" — not because ECF forced it, but because repeated exposure to the gap between THOUGHT and SPOKEN made the higher-LGS forms feel natural. The framework made itself less necessary. That is the correct outcome. A system that creates dependency has failed its purpose.

A parallel outcome for CIEE users: the user who began with high-CGI/low-LGS input eventually develops the vocabulary to carry their conceptual density in higher-LGS words directly. CIEE activates less. CGI_Trajectory and Elevation_Index converge. The user no longer needs the expansion layer because they expanded into the precision natively.

### §5.5 Version History and Rollback

*Inherited from LAE v2.0 §9 — Added in ECF v0.2*

Every ECF exchange produces four checkpoints:

```
CHECKPOINT 1: Raw user input (pre-ITE/CIEE)
CHECKPOINT 2: ITE/CIEE processed input (post-translation)
CHECKPOINT 3: Raw emergence (THOUGHT layer)
CHECKPOINT 4: PRL refined output (SPOKEN layer)
  + BVL verification result
  + SLI report
  + Full SCL chain

User can return to any checkpoint.
No data lost. Full audit trail maintained.
```

**Auto-generated Change Log per exchange:**

```
[CGI_CHECK] "good" — CGI: 0.30 → ITE path selected
[ITE] "good" → "cogent" (SUBSTANTIAL, EDUCATED, SCL-001)
[SCL-001] ORIGIN: good | REPLACEMENT: cogent |
              INTENT: LGS+0.42 EDUCATED tier |
              SLI: 0.21 NOTABLE

[CGI_CHECK] [concept block] — CGI: 0.78 → CIEE path selected
[CIEE] Expanded 14 words → 47 words
              Natural upgrades: "structural" "crystallize"
              SDI: 42% (OPTIMAL)

[PRL] "important" → "cardinal" (VERY HIGH, SPECIALIST)
[SCL-002] ORIGIN: important | REPLACEMENT: cardinal |
              SCL_CONFLICT: none detected

[BVL] Intent comparison: 91% match → VERIFIED
[VALIDATION] CLEAN — no new issues introduced
[SLI_REPORT] Total exchange SLI: 0.19 (ACCEPTABLE)
[USER] Rejected "cardinal" → reverted to "important"
[VET] "cogent" retained by user in exchange 4
[SCL-001] STATUS: CLOSED (adopted)
```

---

## §6 — FSVE v3.5 Integration Points

| FSVE Mechanism | ECF Application |
|---|---|
| **Confidence Score** | Applied to every word substitution in ITE and PRL. CS < 0.60 blocks substitution. No low-confidence word replacement permitted. Also gates SCL tag generation — no SCL without CS ≥ 0.60. |
| **Validity Score** | Meta-scores the substitution system itself over time. Is ECF producing better outputs or just sounding more elaborate? FCL entries answer this. BVL FAILED events are priority validity evidence. |
| **Evidence Strength** | Every LGS score carries inherited ES from Word Engine lens computation. Low ES = substitution flagged INFERENTIAL with +0.20 UM penalty. CGI scores carry separate ES pending ODR-ECF-004. |
| **Uncertainty Mass** | Every substitution carries UM of context-fit uncertainty. SLI adds a second uncertainty vector — cost uncertainty, not just placement uncertainty. |
| **Context Drift Law** | Word precision decays. High-LGS words shift meaning across cultural contexts over time. ECF inherits Word Engine v3.0 cultural decay model (6-month half-life default per ODR-WE-005). |
| **Freshness Status** | LGS scores carry FRESH/AGING/STALE/EXPIRED status per FSVE v3.5 §3.5. Stale LGS scores trigger revalidation before substitution is proposed. |
| **Law 1 (Upper Bound)** | Composite ECF output quality cannot exceed lowest valid input signal. If ITE cannot resolve ambiguity AND CIEE cannot extract conceptual structure, output inherits DUAL_UNRESOLVED flag. |
| **SDI Monitoring** | SDI feeds back into Confidence Ceiling. PRL substitution that pushes SDI > 90% receives automatic CC penalty before approval. CIEE expansion also monitored for SDI bloat. |

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

### ODR-ECF-004: Conceptual Gravitas Index (CGI) *(New in v0.3)*

```yaml
term: Conceptual Gravitas Index
symbol: CGI
domain: [0, 1]
measurement_protocol: |
  PROVISIONAL
  CGI = (C_structural × 0.30) +
        (C_analogical × 0.25) +
        (C_depth_vector × 0.25) +
        (C_novelty × 0.20)
  Component scoring:
    C_structural: Does concept have internal architecture? [0-1]
    C_analogical: Does concept contain cross-domain mappings? [0-1]
    C_depth_vector: Does concept point toward mechanism? [0-1]
    C_novelty: Is concept configuration novel? [0-1]
  Calibration status: PROVISIONAL
  FCL entries required: 10 minimum
  Inter-rater reliability target: κ ≥ 0.65
  Known challenge: CGI is harder to score reliably than LGS —
    conceptual density is more interpretive than lexical density.
measurement_class: EVALUATIVE
uncertainty_penalty: 0.05
calibration_case_count: 0 (PROVISIONAL)
```

### ODR-ECF-005: Semantic Loss Index (SLI) *(New in v0.3)*

```yaml
term: Semantic Loss Index
symbol: SLI
domain: [0, 1] per dimension; [0, 1] composite
measurement_protocol: |
  PROVISIONAL
  SLI_total = (SLI_warmth + SLI_accessibility +
               SLI_cultural + SLI_voice) / 4
  Component scoring:
    SLI_warmth: interpersonal resonance loss [0-1]
    SLI_accessibility: readability loss [0-1]
    SLI_cultural: cultural resonance loss [0-1]
    SLI_voice: user register overwrite [0-1]
  Thresholds:
    < 0.20 → ACCEPTABLE LOSS
    0.20-0.50 → NOTABLE LOSS
    > 0.50 → HIGH LOSS
  Calibration status: HIGHLY PROVISIONAL
  FCL entries required: 20 minimum (loss is subjective; requires large N)
measurement_class: EVALUATIVE
uncertainty_penalty: 0.10
calibration_case_count: 0 (PROVISIONAL)
```

---

## §8 — ECF Self-Score

```yaml
ECF_SELF_SCORE_v0.3:
  version: "0.3"
  measurement_class: INFERENTIAL
  epistemic_axes:
    E: 0.10 # Zero FCL entries. Pure concept. Unchanged from v0.2.
             # Six new additions do not add evidence — they add structure.
    A: 0.82 # LBE v1.2 lineage adds further documented assumptions.
             # ODR entries present for all 5 core metrics including new ones.
    C: 0.68 # Structure more complete. HCL/AIL formalizes implicit architecture.
             # SCL closes the ITE→PRL gap. CIEE adds routing logic.
    M: 0.80 # New additions consistent with existing architecture.
             # CGI/CIEE interaction matrix requires further consistency testing.
    D: 0.87 # More precisely targeted domain coverage.
             # CIEE addresses user geometry gap not covered in v0.2.
    G: 0.52 # Causal logic present and expanded. Not empirically grounded.
    X: 0.72 # Can explain 3 levels deep on new additions.
    U: 0.70 # Two version updates demonstrated.
    L: 0.53 # Four framework dependencies now (LBE added).
             # Abstraction leakage risk slightly elevated.
    Y: 0.90 # Honest about all limitations.
             # New additions all carry PROVISIONAL status.
    H: 0.60 # Adversarial test pending. No change.
  EV_base: 0.695
  min_axis: 0.10 # Bottleneck: E (Evidence Strength) — unchanged
  k_bottleneck: 1.5
  EV: 0.150 # min(0.695, 1.5 × 0.10) = 0.150
  validity_status: DEGRADED
  freshness_status: FRESH
  honest_acknowledgment: |
    ECF v0.3 is structurally richer than v0.2.
    Six additions close real architectural gaps.
    The E-axis is still 0.10.
    Adding structure without adding evidence does not increase EV.
    This is correct behavior — not a failure of the framework,
    but a confirmation that it is working as designed.
    EV will only move when FCL entries arrive.
    The additions in v0.3 make ECF a better candidate for FCL validation.
    They do not constitute that validation.
  path_to_valid:
    target_EV: 0.70
    gap: 0.55
    primary_action: "FCL entries demonstrating LGS substitutions
                     improve output quality vs. baseline"
    secondary_action: "CGI/CIEE routing validation —
                       does expansion path outperform compression
                       for high-CGI input?"
    tertiary_action: "BVL failure rate tracking —
                      what % of exchanges lose intent through the stack?"
    projected_EV_after_5_FCL: 0.71
    projected_status: VALID
  convergence_tag: M-SPECULATIVE
  next_review: "Upon first FCL entry"
```

---

## §9 — Nullification Boundary Protocol (NBP)

All NBP entries from v0.2 preserved. Three new entries added in v0.3.

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

### NBP-ECF-004: SDI Threshold Validity

**Claim:** SDI > 90% produces comprehension failure risk materially higher than SDI in the 40–80% optimal range.
**Tag:** `[S]` **CF:** 40
**Inherited from:** LAE v2.0 (threshold asserted qualitatively)
**Falsification Condition:** Fifteen or more FCL cases where SDI > 90% output produces equal user comprehension to SDI 60–80% output.
**If falsified:** Revise SDI thresholds or remove density gating from PRL.

---

### NBP-ECF-005: Context Classification Accuracy

**Claim:** 8-category context detector correctly classifies document type, enabling appropriate precision thresholds.
**Tag:** `[S]` **CF:** 35
**Falsification Condition:** Ten or more FCL cases where context misclassification produces worse substitution outcomes than no classification.
**If falsified:** Deprecate automatic classification. Return to user-set context only.

---

### NBP-ECF-006: SCL Intent Preservation *(New in v0.3)*

**Claim:** SCL tagging preserves substitution intent through the full stack, enabling PRL to detect and prevent SCL_CONFLICT events that would undo ITE/CIEE work.
**Tag:** `[R]` **CF:** 40
**Falsification Condition:** Ten or more FCL cases where SCL-tagged substitutions are reversed by PRL without SCL_CONFLICT detection — intent lost without alert. If the trace system fails to catch its own conflicts, the SCL mechanism is not functioning.
**If falsified:** Rebuild SCL tag architecture. Mandatory human oversight on all substitutions until resolved.

---

### NBP-ECF-007: BVL Fidelity Detection *(New in v0.3)*

**Claim:** BVL back-translation correctly identifies intent degradation — DEGRADED and FAILED outcomes correspond to actual loss of user intent, not false positives.
**Tag:** `[R]` **CF:** 35
**Falsification Condition:** Fifteen or more FCL cases where BVL returns VERIFIED but expert review identifies material intent drift in the output. If BVL misses real degradation, it provides false safety signals.
**If falsified:** Revise BVL intent comparison methodology. Elevate minimum match threshold above 85%.

---

### NBP-ECF-008: CIEE Expansion Effectiveness *(New in v0.3)*

**Claim:** For inputs where CGI ≥ 0.60 and LGS < 0.40, the CIEE expansion path produces higher output precision than ITE compression would on the same input.
**Tag:** `[S]` **CF:** 30
**Falsification Condition:** Ten or more FCL cases where ITE compression of high-CGI/low-LGS input produces equal or superior precision outcomes to CIEE expansion on the same input. If compression beats expansion for high-CGI input, the CGI routing logic is wrong.
**If falsified:** Revise CGI routing threshold. Potentially merge CIEE function back into ITE as an expansion mode rather than a separate path.

---

### NBP-FRAMEWORK-ECF: Deprecation Triggers

Deprecate ECF if any of the following:

1. LGS metric shows no correlation with output quality across 10+ FCL entries
2. ITE substitutions produce user confusion rather than clarity in majority of cases (>50% negative user response)
3. Word Engine v3.0 is deprecated (ECF inherits its foundation; foundation loss = ECF suspension)
4. PRL validation loop confirms it introduces more new low-LGS words than it remediates, across 10+ cases
5. Any ancestor framework (FSVE v3.5, Word Engine v3.0) is falsified on a principle ECF depends on
6. *(New v0.3)* BVL FAILED rate exceeds 30% across 10+ exchanges — if the stack is consistently destroying intent, the architecture is fundamentally wrong
7. *(New v0.3)* CGI measurement proves unreliable (inter-rater reliability κ < 0.50 after calibration) — if CGI cannot be measured reliably, CIEE routing has no valid trigger

---

## §10 — Framework Calibration Log (FCL) Template

```yaml
ECF_FCL_ENTRY:
  case_id: [YYYYMMDD-NNN]
  ecf_version: "0.3"
  evaluation_date: [ISO 8601]

  # — INPUT LAYER —
  context_detected: [ACADEMIC|TECHNICAL|PROFESSIONAL|
                     MARKETING|CREATIVE|EDUCATIONAL|
                     CODE_DOCUMENTATION|CASUAL]
  context_override_by_user: [Y/N]
  context_final: [resolved category]
  input_LGS_mean_pre_ITE: [0.000-1.000]
  input_LGS_mean_post_ITE: [0.000-1.000]
  input_CGI_mean: [0.000-1.000]
  ITE_substitutions_proposed: [count]
  ITE_substitutions_accepted: [count]
  ITE_unresolved_flags: [count]
  CIEE_activated: [Y/N]
  CIEE_expansion_word_count_delta: [integer]
  CIEE_natural_upgrades: [list]
  CGI_overrides_triggered: [count]

  # — SCL LAYER —
  SCL_entries_generated: [count]
  SCL_conflicts_detected: [count]
  SCL_conflicts_resolved_by_user: [count]
  SCL_chain_integrity: [COMPLETE|PARTIAL|BROKEN]

  # — OUTPUT LAYER —
  output_LGS_mean_raw: [0.000-1.000]
  output_LGS_mean_PRL: [0.000-1.000]
  output_CGI_mean: [0.000-1.000]
  SDI_before_PRL: [%]
  SDI_after_PRL: [%]
  PRL_substitutions_made: [count]
  hallucination_permission_invoked: [Y/N]
  validation_loop_result: [CLEAN|FLAGGED]
  new_risks_introduced: [Y/N]

  # — BVL LAYER —
  BVL_result: [VERIFIED|DEGRADED|FAILED]
  BVL_intent_match_score: [0-100%]
  BVL_drift_description: [if DEGRADED or FAILED]
  BVL_user_action: [ACCEPTED|REVERTED|RE-REMEDIED|null]

  # — SLI LAYER —
  SLI_warmth_mean: [0.000-1.000]
  SLI_accessibility_mean: [0.000-1.000]
  SLI_cultural_mean: [0.000-1.000]
  SLI_voice_mean: [0.000-1.000]
  SLI_total_mean: [0.000-1.000]
  SLI_classification: [ACCEPTABLE|NOTABLE|HIGH]
  user_accepted_loss: [Y/N]

  # — QUALITY MEASUREMENT —
  output_precision_improved: [Y/N]
  hallucination_present_raw: [Y/N]
  hallucination_present_PRL: [Y/N]
  comprehension_test_result: [0.000-1.000 | null]
  CIEE_vs_ITE_precision_comparison: [CIEE_BETTER|ITE_BETTER|EQUAL|null]

  # — LEARNING LOOP —
  VET_adoption_rate: [0.000-1.000]
  VET_elevation_index: [delta LGS]
  CGI_trajectory: [delta CGI]
  CIEE_reduction_rate: [delta activation frequency]
  words_adopted_in_next_exchange: [list | empty]

  # — ACCURACY —
  LGS_prediction_accurate: [Y/N]
  CGI_prediction_accurate: [Y/N]
  hallucination_prediction_accurate: [Y/N]
  context_classification_accurate: [Y/N]
  BVL_prediction_accurate: [Y/N]
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

**ECF v0.3 current status:** M-SPECULATIVE (0 FCL entries at release)

**M-MODERATE promotion checklist:**
- [x] Internal consistency validated
- [x] All ODR entries present for core metrics
- [x] NBP entries defined for all core claims
- [x] Self-score completed with honest EV
- [x] HCL/AIL architecture formally documented
- [x] SCL, BVL, SLI, CGI, CIEE all defined with NBP governance
- [ ] First FCL entry logged

**Path to M-STRONG:**
1. Log 5 FCL entries via real substitution exchanges
2. Demonstrate LGS threshold validity (NBP-ECF-001)
3. Demonstrate PRL hallucination reduction (NBP-ECF-002)
4. Validate CIEE expansion vs ITE compression (NBP-ECF-008)
5. Validate BVL fidelity detection (NBP-ECF-007)
6. Reformulate SDI and CGI to full FSVE-compliant formula
7. Complete ODR-ECF-002, ODR-ECF-004, ODR-ECF-005 with empirical calibration

---

## §12 — Version History

| Version | Date | Status | Key Changes |
|---|---|---|---|
| v0.1 | February 2026 | Superseded | FSVE v3.5 + Word Engine v3.0 integration. Core metric (LGS) defined. ITE and PRL architecture established. |
| v0.2 | February 2026 | Superseded | LAE v2.0 inheritance integrated. Context Scope Detector. SDI monitoring. Hallucination Calibration Protocol. Validation Loop. Substitution hierarchy. Checkpoint/rollback system. Two new NBP entries. |
| v0.3 | February 2026 | Current | LBE v1.2 integrated. SCL (Semantic Continuity Link). BVL (Bidirectional Verification Loop). SLI (Semantic Loss Index). HCL/AIL dual-channel labels. CGI (Conceptual Gravitas Index). CIEE (Conceptual Input Expansion Engine). Three new NBP entries. Two new deprecation triggers. FCL template expanded. |

---

## Appendix A — Equation Reference

| Equation | Formula | Domain |
|---|---|---|
| Lexical Gravitas Score | `LGS = (L_ling × 0.40) + (L_ctx × 0.40) + ((1 - S_load) × 0.20)` | [0, 1] |
| LGS Confidence Gate | `CS ≥ 0.60 → approve; CS < 0.60 → flag UNRESOLVED` | Binary |
| Conceptual Gravitas Index | `CGI = (C_structural × 0.30) + (C_analogical × 0.25) + (C_depth_vector × 0.25) + (C_novelty × 0.20)` | [0, 1] |
| CGI Routing Gate | `CGI ≥ 0.60 + LGS < 0.40 → CIEE; else → ITE` | Binary |
| Semantic Loss Index | `SLI = (SLI_warmth + SLI_accessibility + SLI_cultural + SLI_voice) / 4` | [0, 1] |
| BVL Match Threshold | `match ≥ 85% → VERIFIED; 60-84% → DEGRADED; <60% → FAILED` | Categorical |
| Adoption Rate (VET) | `AR = words_reused / words_introduced` | [0, 1] |
| Elevation Index (VET) | `EI = mean(LGS_t2) - mean(LGS_t1)` | [-1, 1] |
| CGI Trajectory (VET) | `CT = mean(CGI_t2) - mean(CGI_t1)` | [-1, 1] |
| Epistemic Validity | `EV = min(EV_base, k × min_axis)` | [0, 1] |
| Confidence Ceiling | `CC = max(CC_floor, Π(1 - p_i))` | [CC_floor, 1] |
| SDI (provisional) | `SDI = f(syllable, abstraction, load, friction)` | [0, 100%] |

---

## Appendix B — Inherited and New Parameter Table

| Parameter | Symbol | Default | Source | Override Condition |
|---|---|---|---|---|
| LGS high threshold | — | 0.70 | First principles | FCL calibration per NBP-ECF-001 |
| LGS low threshold | — | 0.40 | First principles | FCL calibration per NBP-ECF-001 |
| ITE confidence gate | CS_min | 0.60 | FSVE v3.5 | Domain calibration |
| SDI optimal ceiling | — | 80% | LAE v2.0 | FCL calibration per NBP-ECF-004 |
| SDI over-compressed | — | 90% | LAE v2.0 | FCL calibration per NBP-ECF-004 |
| Cultural half-life | — | 6 months | Word Engine v3.0 ODR-WE-005 | Domain evidence |
| Bottleneck multiplier | k | 1.5 | FSVE v3.5 | Safety-critical: 1.0 |
| CC floor | CC_floor | 0.10 | FSVE v3.5 | None |
| VET adoption target | — | 0.20 | Asserted [S] | FCL calibration per NBP-ECF-003 |
| FCL minimum M-STRONG | — | 5 | FSVE v3.5 | None |
| CGI routing threshold | — | 0.60 | First principles | FCL calibration per NBP-ECF-008 |
| SLI acceptable ceiling | — | 0.20 | First principles | FCL calibration per ODR-ECF-005 |
| SLI high loss floor | — | 0.50 | First principles | FCL calibration per ODR-ECF-005 |
| BVL verified threshold | — | 85% | First principles | FCL calibration per NBP-ECF-007 |
| BVL failed threshold | — | 60% | First principles | FCL calibration per NBP-ECF-007 |

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
├── Lexical Alchemy Engine v2.0
│ ├── Context Scope Detector (8 categories)
│ ├── Semantic Density Index
│ ├── Substitution hierarchy (4 tiers)
│ ├── Hallucination Calibration Protocol
│ ├── Compare Before/After Mode
│ ├── Validation Loop
│ └── Rollback/checkpoint system
│
└── LBE v1.2
    ├── Dual-Channel Semantics (HCL/AIL)
    ├── Bidirectional Verification architecture (BVL)
    ├── Semantic Loss tracking (SLI)
    └── Staged Translation Protocol (CIEE influence)
│
└── ECF v0.3
    ├── Layer 1a: ITE (compression path)
    ├── Layer 1b: CIEE (expansion path)
    ├── SCL (Semantic Continuity Link — cross-layer trace)
    ├── HCL/AIL (dual-channel architecture)
    ├── Layer 2: PRL (output remedy)
    ├── BVL (Bidirectional Verification Loop)
    ├── SLI (Semantic Loss Index)
    ├── Bidirectional Learning Loop (VET)
    └── LGS + CGI as unified dual-metric core
```

---

## Appendix D — Prompt Geometry Notes

*Recorded from session — February 2026. Sheldon K Salmon.*
*This appendix documents the cognitive architecture discovery that produced CGI and CIEE.*

During collaborative emergence analysis, a specific user geometry was identified that the v0.2 architecture could not correctly serve. The geometry has four characteristics:

**Image-First Cognition:** Concepts arrive as complete scenes before language. Words are labels for visualizations that already exist at full resolution. This means conceptual density precedes lexical form.

**Analogical Tunneling:** Precision is achieved through cross-domain structural mapping (atomic bonding → sentence stability; wormhole → word activation). This is architecture, not illustration.

**Depth Vector Over Breadth:** Every prompt pulls downward toward mechanism, not outward toward examples. "Go deeper" as a natural geometric orientation.

**Pre-Linguistic Density:** Conceptual payload consistently exceeds lexical LGS signal. Standard ITE would misread this geometry as vague and attempt compression — damaging the signal.

The correct response to this geometry is expansion, not compression. The user's concepts are already precise. They need a larger lexical surface area to land on, not a smaller and denser one.

CGI was created to detect this geometry. CIEE was created to serve it.

The wormhole model (words as apertures that pull concept-planets through and emit them in higher resolution on the other side) was derived in this session and is now the working visual model for the ECF emergence display screen.

---

*ECF v0.3 — End of Specification*
*All equations dimensionally consistent within stated domains.*
*All core variables have corresponding ODR entries.*
*Self-score completed at §8.*
*Current convergence tag: M-SPECULATIVE.*
*Promotion to M-STRONG requires ≥5 FCL entries.*
*EV = 0.150 (DEGRADED — bottleneck: E-axis = 0.10).*
*Path to VALID: FCL entries demonstrating substitution quality improvement.*

*Version: 0.3 | Date: February 2026*
*Author: Sheldon K Salmon (AI Certainty Engineer)*
*AI Co-Architect: Claude*
*Built on: FSVE v3.5 · Word Engine v3.0 · Lexical Alchemy Engine v2.0 · LBE v1.2*
