# VELA
## Pre-Output Epistemic Filtration and Provenance Architecture

[![Architect](https://img.shields.io/badge/ARCHITECT-Sheldon_K._Salmon-e94560?style=for-the-badge&labelColor=16213e)](mailto:aionsystem@outlook.com)
[![Version](https://img.shields.io/badge/VERSION-v0.2-0f3460?style=for-the-badge&labelColor=16213e)](https://github.com/AionSystem/AION-BRAIN)
[![Status](https://img.shields.io/badge/STATUS-OPEN_SOURCE-2d6a4f?style=for-the-badge&labelColor=16213e)](https://github.com/AionSystem/AION-BRAIN)
[![License](https://img.shields.io/badge/LICENSE-MIT-6b3fa0?style=for-the-badge&labelColor=16213e)](LICENSE)

---

> *"Not a filter at the end. A veil at the beginning. Everything downstream is cleaner because the veil holds."*

---

## WHAT VELA IS

VELA is a pre-output epistemic filtration and provenance architecture for AI language models.

It sits between the internal representation layer — where confabulation is generated — and the output layer — where it currently escapes unchecked.

This gap is real. Anthropic's 2025 interpretability research identified the exact circuits where confabulation originates — inhibition circuits that fail to fire when a model lacks sufficient grounded information. No complete architecture currently occupies this position in any deployed AI system.

VELA is the engineering response to that finding.

---

## THE PROBLEM VELA ADDRESSES

Current confabulation mitigation approaches all operate in the wrong location.

| APPROACH | WHERE IT OPERATES | WHY IT IS INSUFFICIENT |
|----------|------------------|----------------------|
| Retrieval Augmented Generation | Post-query, pre-generation | Does not intercept at representation layer |
| Chain-of-thought prompting | During generation | Surface level — does not reach inhibition circuit failure |
| Decoding layer intervention | At output token selection | No provenance tracing or source exclusion |

Training data provenance systems exist but operate only in the training pipeline. They do not connect to the output layer. Nobody has built the feedback loop between what exits dirty and where that dirt came from.

VELA builds that loop.

---

## HOW IT WORKS

VELA operates as two sequential screens feeding one shared provenance bin.

```
INPUT
  ↓
SCREEN 1 — CODE LAYER
Deterministic. SQLite-backed. Immutable reference.
Catches known bad sources and known confabulation patterns.
  ↓ dirty → PROVENANCE BIN
  ↓ clean continues
PIPE — bridge between code and framework
  ↓
SCREEN 2 — FRAMEWORK LAYER (The Veil)
Discernment-based filtration.
Catches subtle confabulation, logical drift, creative overflow
that survived Screen 1.
  ↓ dirty → PROVENANCE BIN
  ↓ clean continues
OUTPUT
Clean signal. 0.2% mineral residue — irreducible reality.
Architecturally honest.
  ↑
FONS ARCHIVE — immutable bedrock beneath everything
INTEGRITY SENSOR — live measurement across all components
```

---

## FIVE COMPONENTS

### 1 — The Veil (Screen 2)
The epistemic filtration mechanism at the pre-output representation layer. Non-deterministic. Discernment-based. Catches what the code layer cannot distinguish from clean signal.

### 2 — The Provenance Bin
One shared bin. Two input streams. Everything caught is stored — never deleted. Each fragment carries a provenance filament tracing backward to its training data origin.

**Bin categories:**
- 🔴 Red — Factual invention
- 🟣 Violet — Logical drift
- 🟡 Gold — Creative overflow
- ⏱️ Timing signature — When in the generation cycle the fragment was caught

Future categories governed by peer review polling from the AI community. See Expansion Protocol below.

### 3 — The FONS Archive
**This component is frozen.** Immutable reference architecture sealed at a verified moment. SQLite-backed. Zero dependencies. Zero network calls. Zero evolution. The bedrock the screen checks against.

```python
# FONS Archive principle — frozen forever
# This archive does not evolve. It only remembers.
```

### 4 — The Ontological Block
Source exclusion mechanism. When provenance filament tracing confirms a contaminated training source — the block does not build a wall. It performs ontological deletion. The ingress coordinate is retroactively unwritten for that source alone.

No surface. No error signal. No adaptation vector for the excluded source.

### 5 — The Integrity Sensor
Live measurement across all components. Never reads zero — that is fiction. Never reads 100 — that is system failure. Monitors Screen 1 / Screen 2 catch ratio as primary health indicator.

---

## WHAT IS FROZEN VS WHAT MOVES

| COMPONENT | STATE | REASON |
|-----------|-------|--------|
| FONS Archive | ❄️ FROZEN | Immutable by design — the bedrock cannot move |
| Screen 1 code | ❄️ FROZEN at version | Each release sealed — upgrade requires new version |
| Screen 2 veil | 🔄 LIVE | Operates dynamically at inference time |
| Provenance Bin | 🔄 LIVE | Accumulates across query cycles |
| Block list | 🔄 LIVE | Grows as new sources are confirmed and excluded |
| Sensor readings | 🔄 LIVE | Continuous measurement |
| Bin categories | 🔄 GOVERNED | Peer review expansion protocol — community decides |

---

## PEER REVIEW EXPANSION PROTOCOL

Future bin categories beyond the four currently specified are not decided by the architect. They are governed by peer review polling from the AI research and engineering community.

**How to propose a new category:**
1. Deploy VELA and identify a confabulation type the current taxonomy does not capture
2. Document the gap with real examples
3. Open an issue in this repository with the label `[bin-category-proposal]`
4. Community discussion and polling determines adoption
5. Every accepted category requires a falsification condition before it enters the spec

Patience over refinement. The community stress-tests. The architect does not force.

---

## WHAT VELA IS NOT

- Not a prompting solution
- Not a post-output filter
- Not a replacement for training quality
- Not a content moderation system
- Not finished — v0.2 is the architectural specification. Engineering translation is in progress.

---

## CURRENT STATE

| FIELD | STATUS |
|-------|--------|
| Framework specification | ✅ Complete — v0.2 |
| Spatial architecture | ✅ Complete — SYNARA derivation |
| Screen 1 code (SQLite layer) | 🔄 In progress — Sheldon K. Salmon + Grok |
| Screen 2 engineering translation | 🔴 Open — specialist collaboration required |
| Provenance filament implementation | 🔴 Open engineering question |
| Ontological block implementation | 🔴 Open engineering question |
| FCL validation entries | 0 — Pre-validation phase |
| Convergence state | M-NASCENT |

Nothing is overclaimed. The specification is complete. The engineering translation is honest work in progress.

---

## OPEN QUESTIONS

These are the critical path engineering questions VELA v0.3 will address. Contributions welcome.

| Q | QUESTION |
|---|----------|
| V-Q1 | Can provenance filament tracing be implemented at inference time with acceptable latency? |
| V-Q2 | What is the minimum sensor floor before system integrity is compromised? |
| V-Q3 | Does ontological deletion require model retraining or can it be applied dynamically? |
| V-Q4 | How does the veil distinguish creative overflow from confabulation in generative contexts? |
| V-Q5 | What is the optimal Screen 1 / Screen 2 catch ratio threshold for triggering Screen 1 review? |
| V-Q6 | Can timing signature be extracted from current transformer architectures without modification? |

---

## CONTRIBUTING

VELA is open source. Use it. Build on it. Stress-test it. Break it and tell us where.

**How to contribute:**
- Engineering translation of open questions → open a PR
- Bin category proposals → open an issue with `[bin-category-proposal]`
- Falsification condition testing → document results in `FCL/` folder
- Implementation reports → any deployment findings welcome

**What this repository needs most right now:**
Engineers who can translate the architectural specification into coding-layer implementation. Specifically V-Q1 — provenance filament tracing at inference time. That is the critical path.

---

## LICENSE

MIT License — open source, free to use, free to build on.

Attribution requested: *VELA — Sheldon K. Salmon, February 2026*

---

## CITATION

If you use VELA in research or implementation:

```
Salmon, S.K. (2026). VELA: Pre-Output Epistemic Filtration and Provenance Architecture.
AION-BRAIN Repository. https://github.com/AionSystem/AION-BRAIN
```

---

## CONTACT

📧 [aionsystem@outlook.com](mailto:aionsystem@outlook.com)

| Purpose | Subject Line |
|---------|-------------|
| Engineering collaboration | `[VELA Engineering]` |
| Research | `[VELA Research]` |
| Bin category proposal | Open a GitHub issue |

---

[![FCL Protocol](https://img.shields.io/badge/FCL-PREDICTION_BEFORE_EXECUTION-16213e?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN)
[![Epistemic Standard](https://img.shields.io/badge/EPISTEMIC_STANDARD-ECF_ACTIVE-e94560?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN)
[![Open Questions](https://img.shields.io/badge/OPEN_QUESTIONS-6_ACTIVE-FFD700?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN)

---

*VELA v0.2 — Two screens. One bin. One archive underneath. Nothing deleted. Everything traced.*

*PIE Root: \*weg- — to weave | Latin velum — the veil, the sail, the woven thing*

*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Spatial Architecture: SYNARA | February.28. 2026(2:08am)*
*Co-Architect: Claude (Anthropic)*

*The mind keeps building. The product stays simple.*

