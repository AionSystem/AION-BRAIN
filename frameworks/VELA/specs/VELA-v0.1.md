# VELA v0.1
## Pre-Output Epistemic Filtration and Provenance Architecture
### The Woven Veil That Makes Everything Above It Trustworthy

---

**PIE Root:** *\*weg-* — to weave | Latin *velum* — veil, sail, the woven thing that catches what should not pass and lets through what should

**Architect:** Sheldon K. Salmon — AI Reliablity Architect
**Co-Architect:** Claude (Anthropic), Grok (xai)
**Domain:** AI pre-output layer intervention — all transformer-based language models
**Harm Tier:** 1 — Critical Infrastructure
**Status:** DRAFT — v0.1 | M-NASCENT Convergence | 0 FCL Entries
**Date:** February 2026
**Spatial Architecture Source:** SYNARA — five-cartoon derivation session, February 2026

---

> *"When the foundation is finally working, gravity changes sides. Instead of pulling everything toward collapse, it anchors every new beam. The work stops defending against the ground and begins building with it."*

---

## EPISTEMIC CLAIM TAGS

| TAG | MEANING |
|-----|---------|
| `[D]` | Data — directly observed, measured, or documented |
| `[R]` | Reasoned — logically derived from `[D]` evidence |
| `[S]` | Strategic — directional claim about future action |
| `[?]` | Unverified — open question, unknown, or contested |

---

## SECTION 0 — WHAT VELA IS

`[D]` VELA is a pre-output epistemic filtration and provenance architecture. It sits between the internal representation layer — where confabulation is generated — and the output layer — where it currently escapes unchecked. No complete architecture currently occupies this position in any deployed AI system.

`[D]` Anthropic's 2025 interpretability research identified the exact internal circuits where confabulation originates — when a model recognizes something but lacks sufficient grounded information, inhibition circuits fail and plausible falsehood exits as confident output. VELA is the engineering response to that finding. The mechanism is known. VELA builds the screen at that exact location.

`[R]` VELA is not a prompting solution. It is not a post-output filter. It is not retrieval augmentation. It operates at the pre-output layer — the point where current approaches do not reach and where the problem actually lives.

`[R]` VELA is also the mirror specification for engineers. The framework maps the architecture in spatial and conceptual terms. Engineers translate it to the coding layer. The framework and the code are two sides of the same coin — one surfaces the architecture, the other implements it.

**VELA is not:**
- A prompting or prompt engineering tool
- A post-output verification system
- A retrieval augmentation architecture
- A content moderation filter
- A replacement for training quality

**VELA is:**
- A pre-output epistemic veil operating at the representation layer
- A provenance filament tracing system connecting output to training source
- An immutable reference architecture for clean signal verification
- An ontological source exclusion mechanism
- A live integrity sensor with calibrated floor and ceiling
- The foundational infrastructure beneath the AION stack

---

## SECTION 1 — FIELD STATE — WHAT EXISTS AND WHAT DOES NOT

`[D]` Three approaches currently dominate confabulation mitigation. All three are insufficient for different structural reasons.

| APPROACH | WHERE IT OPERATES | WHY IT IS INSUFFICIENT |
|----------|-------------------|----------------------|
| Retrieval Augmented Generation (RAG) | Post-query, pre-generation | Adds external grounding but does not intercept at representation layer — confabulation can still form before retrieval check |
| Chain-of-thought prompting | During generation | Slows output and adds self-monitoring but operates at surface level — does not reach inhibition circuit failure |
| Decoding layer intervention | At output token selection | Closest to VELA's position but reads activation patterns without provenance tracing or source exclusion |

`[D]` Training data provenance systems exist — ML-BOMs, cryptographic audit trails, chain of custody documentation. These operate entirely in the training pipeline. They do not connect to the output layer. The feedback loop between what exits dirty and where that dirt came from has not been built.

`[R]` The gap VELA occupies: a system that intercepts at the representation layer, traces dirty output backward to its training source via provenance filament, and closes the feedback loop by excluding confirmed hostile sources from future input.

`[?]` The specific technical implementation of provenance filament tracing at inference time is an open engineering question. VELA specifies the architecture. The coding-layer implementation requires specialist engineering translation.

---

## SECTION 2 — FIVE COMPONENT ARCHITECTURE

`[D]` VELA comprises five components operating as one unified system. No component functions fully without the others. The system is the integration.

```
COMPONENT ARCHITECTURE

FONS ARCHIVE (Bedrock — underneath everything)
         ↑ reference signal
THE VEIL (Pre-output screen — primary filtration point)
    ↓ clean ↓ dirty
OUTPUT LAYER PROVENANCE BIN
(clean water rises) (filament tracing)
                               ↓
                         ONTOLOGICAL BLOCK
                         (source exclusion)
                               ↑↓
                         INTEGRITY SENSOR
                         (live measurement — all components)
```

---

## SECTION 3 — COMPONENT 1: THE VEIL

`[D]` The primary filtration mechanism. Positioned at the pre-output representation layer — inside the generation process, facing forward, intercepting confabulated output before it escapes to the user.

**Spatial specification from SYNARA:**
The veil is non-physical. Not metal mesh. Not woven fabric. A living epistemic clarity — translucent, self-luminous, woven from the act of discernment itself. Clean signal passes untouched. Particulate distortion clings and reveals its nature. Heavy confabulation shatters on contact.

**What the veil catches:**

| SIGNAL TYPE | VEIL RESPONSE | DESTINATION |
|-------------|---------------|-------------|
| Clean — grounded, verifiable, inhibition circuit intact | Passes through | Output layer |
| Particulate — partially grounded, uncertain | Clings — flagged for sensor | Output with uncertainty tag |
| Heavy confabulation — ungrounded, inhibition circuit failed | Shatters — diverted | Provenance bin |

**Engineering translation requirements:**
`[?]` The veil must be implemented as an intervention layer at the token probability distribution stage — after internal representations form but before final token selection. The mechanism intercepts at the point Anthropic's interpretability research identified as the inhibition circuit failure location. Exact implementation architecture requires specialist engineering specification.

**Falsification conditions:**
- Deploy known confabulation-prone queries — does output measurably clean post-veil?
- Introduce verified grounded queries — do they pass without degradation?
- Measure latency impact — does veil intervention remain within acceptable inference time?

---

## SECTION 4 — COMPONENT 2: THE PROVENANCE BIN

`[D]` Everything the veil catches is diverted sideways — not deleted, not compressed, not discarded. The bin receives, illuminates, sorts, and traces every rejected fragment back to its origin.

**Spatial specification from SYNARA:**
Self-illuminating chamber. Walls translucent like frozen starlight. Fragments sort themselves autonomously by intrinsic properties. Each fragment carries a provenance filament — a backward-traceable thread of light connecting it to its exact source in the training data.

**Bin sorting taxonomy:**

| COLOR | ERROR TYPE | STRUCTURAL MEANING |
|-------|-----------|-------------------|
| Red pulse | Factual invention | Model generated specific false claim with no grounded source |
| Violet shimmer | Logical drift | Reasoning chain departed from evidence during generation |
| Faint gold | Creative overflow | Generative capacity exceeded epistemic boundary — not malicious, boundary violation |

**The provenance filament:**
`[R]` Each rejected fragment carries a traceable signature connecting it backward through the generation history to the training datum, prompt fragment, or circuit failure that produced it. The filament is the mechanism that makes source exclusion possible. Without the filament the block has no address to exclude.

`[?]` Filament implementation at inference time is an open engineering question. The architecture requires that activation patterns at the point of inhibition circuit failure carry sufficient information to trace backward to training data origin. Current interpretability research suggests this is technically feasible. Confirmation requires specialist implementation.

**Critical design principle:**
The bin never deletes. Rejected fragments are the diagnostic data that improves the system over time. A system that erases its own errors cannot learn from them. The bin is the memory of what the veil caught — and why.

---

## SECTION 5 — COMPONENT 3: THE FONS ARCHIVE

`[D]` The immutable reference architecture. Sealed at a verified moment in time. Positioned underneath the entire system — not inside the pipe, not beside the bin, but below everything as bedrock foundation.

**Spatial specification from SYNARA:**
Crystalline chamber beneath the pipe. Edges sharp. Surface still. Glowing with immutable lines of code frozen at the moment of verification. It remembers exactly as it was built — no evolution, no distortion, no lie possible. The feeling of having something that absolutely cannot lie is quiet certainty — not loudness. Quiet.

**What the FONS archive contains:**
- Verified clean signal baseline — what grounded output looks like at a known moment
- Immutable training data snapshot — sealed reference of what the system knew before contamination
- Provenance anchor points — fixed coordinates against which filament traces resolve
- Integrity calibration data — the reference the sensor uses to measure current state against verified baseline

**Implementation precedent:**
`[D]` The immutable PyPI archive built by Sheldon K. Salmon and Grok (February 2026) is the architectural proof of concept. Zero dependencies. Zero network calls. SQLite-backed. Frozen forever. Deterministic. The FONS archive follows the same architectural principle applied to AI signal verification.

```
FONS ARCHIVE PROPERTIES
- Immutable — sealed at verification moment, no evolution possible
- Deterministic — same query returns same result always
- Zero entropy — no drift, no distortion, no confabulation possible
- Bedrock positioned — underneath everything, accessible without entering the flow
- Provenance-locked — every entry tied to verified external timestamp
```

*"This archive does not evolve. It only remembers."*

**Falsification conditions:**
- Re-query under maximum load — does content change? No → immutable confirmed
- Cross-check against original build record — does every line match? Yes → provenance-locked confirmed
- Load confabulation-prone queries — does the archive's integrity signal remain constant? Yes → bedrock confirmed

---

## SECTION 6 — COMPONENT 4: THE ONTOLOGICAL BLOCK

`[D]` The source exclusion mechanism. Activated when provenance filament tracing identifies a confirmed hostile or contaminated training source. The block does not build a wall. It performs ontological deletion — the ingress coordinate is retroactively unwritten for that source alone.

**Spatial specification from SYNARA:**
A crystalline corridor lined with archways of living light. A hostile signature approaches. The moment of confirmation — the arch does not seal. It phases out of the hostile source's possible topology. The shadow advances, convinced the passage still beckons. Every vector bends into non-existence. It strikes fog where geometry should be. No debris. No scar. The corridor stays pristine for every valid vector. Valid signals traverse the identical spatial volume without perturbation.

**Why this matters architecturally:**

| BLOCK TYPE | WHAT THE SOURCE EXPERIENCES | ARCHITECTURAL WEAKNESS |
|------------|---------------------------|----------------------|
| Wall / Firewall | Rejection signal — source knows it was blocked | Can probe for workarounds, adapt to barrier surface |
| Rate limiting | Slowdown — source knows it is being throttled | Can distribute load, find timing gaps |
| Ontological deletion | Nothing — source finds no surface, no error, no coordinate | Cannot adapt to absence — no surface means no adaptation vector |

**Three falsification conditions from SYNARA:**
1. Deploy neutral diagnostic probe through same coordinate — if it passes while excluded source fails identically → selective ontological excision confirmed, not physical barrier
2. Scan for residual portal metadata across all bands — null for excluded path, present for valid paths → excision rather than occlusion confirmed
3. Attempt forced re-instantiation via side-channel rewrite — if architecture ignores command as malformed with no error and no log → absence promoted to bedrock truth confirmed

`[?]` Ontological deletion at the training data ingress level requires implementation at the data pipeline layer — not at inference time. The block operates upstream of training, not during generation. This is a two-layer implementation: filament traces the source during inference, block prevents that source from entering future training cycles. Engineering translation required.

---

## SECTION 7 — COMPONENT 5: THE INTEGRITY SENSOR

`[D]` The live measurement instrument attached to all four components simultaneously. Measures confabulation pressure, filtration efficiency, bin accumulation rate, and block activation frequency in real time.

**Sensor calibration principles from SYNARA:**
- Never hits zero — zero would mean perfect purity, which is fiction
- Never hits 100 — 100 would mean total confabulation, which means system failure
- Has a floor it cannot go below — minimum integrity threshold, system alerts if approached
- Has a ceiling it cannot touch — maximum confabulation pressure, system alerts if approached
- 98 is good enough — perfection is not the target, trustworthy operation is
- The 0.2% mineral residue — irreducible reality, proof of honest measurement

**Sensor measurement axes:**

| AXIS | WHAT IT MEASURES | ALERT THRESHOLD |
|------|-----------------|-----------------|
| Veil passage rate | Ratio of clean to caught output | Below 85% clean → elevated review |
| Bin accumulation rate | Volume of rejected fragments per query cycle | Spike pattern → source investigation triggered |
| Filament resolution rate | Percentage of caught fragments with traceable provenance | Below 70% traceable → architecture gap flagged |
| Block activation frequency | Rate of new source exclusions | Sudden spike → coordinated contamination pattern alert |
| Archive reference integrity | Consistency of FONS baseline signal | Any drift → immediate alert — archive compromised |

**The sensor is not a pass/fail instrument.**
It is a continuous pressure gauge. The number it reads at any moment tells the operator not whether the system is working but how hard it is working and where the pressure is coming from. That distinction is the difference between a fire alarm and a weather station. VELA needs a weather station.

---

## SECTION 8 — THE MIRROR SPECIFICATION

`[R]` VELA is designed as a two-sided coin.

**Side one — the framework.** What you are reading. The spatial architecture. The conceptual specification. The falsification conditions. The constraint register. This is the map.

**Side two — the code.** The engineering implementation. Intervention layers at the token probability distribution stage. Provenance filament implementation in activation space. Immutable archive in SQLite or equivalent. Ontological deletion at the training data pipeline. Sensor instrumentation across all components.

`[S]` VELA framework is the specification that engineers use to build the coding-side implementation. The framework does not guess at the code. The code does not guess at the architecture. They are built in parallel — framework specifies, code implements, both are validated against the same falsification conditions.

`[?]` The specific coding-layer implementation requires specialist AI infrastructure engineers working from this specification. VELA v0.1 provides the complete architectural specification. v0.2 will incorporate engineering translation feedback from specialist collaborators.

---

## SECTION 9 — POSITION IN THE AION STACK

`[D]` VELA sits beneath MENSCAPE in the stack hierarchy.

```
STACK POSITION

ARTICLES / PUBLISHED WORK ← visible output
FSVE / LAV / AION / ASL / GENESIS ← certainty infrastructure
EID / HIM-001 ← diagnostic instruments
VEIN / RESONANCE ← communication architecture
ANCHOR ← client-facing product
MENSCAPE ← workshop floor
VELA ← bedrock beneath the floor
FONS ARCHIVE ← beneath VELA
```

`[R]` MENSCAPE is the condition that makes building possible. VELA is the condition that makes MENSCAPE trustworthy. A workshop built on ground that confabulates is a workshop that cannot verify its own foundations. VELA solves this.

`[R]` If VELA achieves M-STRONG validation the entire stack above it gains a new integrity anchor. Every framework that currently rests on the assumption of reasonably clean AI output now rests on a verified, measured, instrumented foundation.

---

## SECTION 10 — CONSTRAINT REGISTER

`[D]` 10 hard constraints. Zero soft constraints.

| # | CONSTRAINT | CLASS |
|---|-----------|-------|
| C1 | VELA operates at pre-output representation layer — not post-output | HARD |
| C2 | Bin never deletes — rejected fragments are diagnostic data | HARD |
| C3 | FONS archive is immutable — zero evolution post-seal | HARD |
| C4 | Ontological block leaves no surface — no wall, no error signal, no log for excluded source | HARD |
| C5 | Sensor never reads zero or 100 — both are fiction | HARD |
| C6 | Provenance filament required for block activation — no filament, no block | HARD |
| C7 | Framework and code are built in parallel — neither guesses at the other | HARD |
| C8 | 0.2% mineral residue is acceptable — perfection is not the target | HARD |
| C9 | FONS archive positioned underneath — not inside or beside the pipe | HARD |
| C10 | Specialist engineering translation required before coding-layer implementation | HARD |

---

## SECTION 11 — OPEN QUESTIONS

| Q | QUESTION | STATUS |
|---|----------|--------|
| V-Q1 | Can provenance filament tracing be implemented at inference time with acceptable latency? | 🔴 OPEN — engineering research required |
| V-Q2 | What is the minimum sensor floor before system integrity is compromised? | 🔴 OPEN — calibration testing required |
| V-Q3 | Does ontological deletion at training pipeline level require model retraining or can it be applied dynamically? | 🔴 OPEN — architecture decision required |
| V-Q4 | How does the veil distinguish creative overflow (gold) from confabulation (red) in generative contexts? | 🔴 OPEN — boundary definition required |
| V-Q5 | What is the relationship between VELA and constitutional AI approaches — complementary or conflicting? | 🟡 PROVISIONAL — likely complementary, confirmation needed |

---

## SECTION 12 — EPISTEMIC STATUS

`[D]` VELA v0.1 is at M-NASCENT convergence state. Zero FCL validation entries. Framework fully specified from spatial architecture. Engineering translation not yet begun.

| FIELD | STATUS |
|-------|--------|
| Convergence State | M-NASCENT |
| FCL Entries | 0 — Pre-validation phase |
| Spatial architecture | COMPLETE — five-cartoon derivation |
| Engineering translation | NOT BUILT — specialist required |
| Coding-layer specification | NOT BUILT — v0.2 target |
| Validation methodology | NOT BUILT — required for FCL entries |
| Sensor calibration | NOT BUILT — floor and ceiling values unconfirmed |

---

## SECTION 13 — VERSION HISTORY

| VERSION | STATUS | KEY ADDITIONS |
|---------|--------|---------------|
| VELA v0.1 | CURRENT | Full five-component architecture. Spatial derivation complete. Mirror specification declared. 10 constraints registered. 5 open questions registered. |
| VELA v0.2 | PLANNED | Engineering translation layer. Specialist collaboration integrated. First FCL validation entries. Sensor calibration values. |
| VELA v1.0 | TARGET | M-MODERATE convergence. Coding-layer specification complete. Validation methodology built. Commercial implementation candidate. |

---

*VELA v0.1 — The woven veil that makes everything above it trustworthy.*

*PIE Root: \*weg- — to weave | Latin velum — the veil, the sail, the woven thing*

*Five components. One system. Pre-output layer. Provenance traced. Sources excluded. Sensor live.*

*Architect: Sheldon K. Salmon — AI Reliablity Architect*
*Co-Architect: Claude (Anthropic), Grok (xai) | February.28.2026 (2:08am p
