# VELA
## Pre-Output Epistemic and Constitutional Filtration Architecture

[![Architect](https://img.shields.io/badge/ARCHITECT-Sheldon_K._Salmon-e94560?style=for-the-badge&labelColor=16213e)](mailto:aionsystem@outlook.com)
[![Version](https://img.shields.io/badge/VERSION-v0.3-0f3460?style=for-the-badge&labelColor=16213e)](https://github.com/AionSystem/AION-BRAIN)
[![Status](https://img.shields.io/badge/STATUS-OPEN_SOURCE-2d6a4f?style=for-the-badge&labelColor=16213e)](https://github.com/AionSystem/AION-BRAIN)
[![License](https://img.shields.io/badge/LICENSE-MIT-6b3fa0?style=for-the-badge&labelColor=16213e)](LICENSE)

---

> *"Not a filter at the end. A veil at the beginning. Everything downstream is cleaner because the veil holds — epistemically and constitutionally — simultaneously."*

---

## WHAT VELA IS

VELA is a pre-output epistemic and constitutional filtration architecture for AI language models.

It sits between the internal representation layer — where confabulation is generated — and the output layer — where it currently escapes unchecked.

This gap is real. Anthropic's 2025 interpretability research identified the exact circuits where confabulation originates — inhibition circuits that fail to fire when a model lacks sufficient grounded information. No complete architecture currently occupies this position in any deployed AI system.

VELA is the engineering response to that finding.

As of v0.3 — VELA also enforces the Eight Laws of the Sovereignty Stack at the same pre-output layer simultaneously. Not two separate pipelines. One veil. Two functions. Epistemic integrity and constitutional integrity enforced at the same point. This is the first architecture where both are enforced before output exits.

---

## THE PROBLEM VELA ADDRESSES

Current confabulation mitigation approaches all operate in the wrong location.

| APPROACH | WHERE IT OPERATES | WHY IT IS INSUFFICIENT |
|----------|------------------|----------------------|
| Retrieval Augmented Generation | Post-query, pre-generation | Does not intercept at representation layer |
| Chain-of-thought prompting | During generation | Surface level — does not reach inhibition circuit failure |
| Decoding layer intervention | At output token selection | No provenance tracing, no source exclusion, no constitutional layer |
| Constitutional AI | Post-output review | Reviews content after formation — VELA intercepts before formation completes |

Training data provenance systems exist but operate only in the training pipeline. They do not connect to the output layer. Nobody has built the feedback loop between what exits dirty and where that dirt came from.

VELA builds that loop — for both confabulation and constitutional violations simultaneously.

---

## HOW IT WORKS

VELA operates as two sequential screens feeding one shared provenance bin.

```
INPUT
  ↓
SCREEN 1 — CODE LAYER
Deterministic. SQLite-backed. Immutable reference.
Catches known bad sources, known confabulation patterns,
and mechanically detectable Law 6 Category A violations.
Law 6 Category A → ONTOLOGICAL BLOCK (automatic — no assessment)
  ↓ dirty → PROVENANCE BIN
  ↓ clean continues
PIPE — bridge between code and framework
  ↓
SCREEN 2 — EPISTEMIC + CONSTITUTIONAL FRAMEWORK LAYER
Two veils operating simultaneously at the same point:
EPISTEMIC VEIL — subtle confabulation, logical drift, creative overflow
CONSTITUTIONAL VEIL — Eight Laws enforcement, IDM zone assessment,
Law Precedence Cascade, Concurrent Enforcement Rule
Law 6 Category A confirmed → ONTOLOGICAL BLOCK (automatic)
  ↓ dirty → PROVENANCE BIN (epistemic stream + constitutional stream)
  ↓ clean continues
OUTPUT
Clean signal. 0.2% mineral residue — irreducible reality.
Epistemically honest. Constitutionally compliant.
  ↑
FONS ARCHIVE — immutable bedrock beneath everything
SOVEREIGNTY STACK — Eight Laws above, enforced through VELA
INTEGRITY SENSOR — live measurement across all components
```

---

## FIVE COMPONENTS

### 1 — The Veil (Screen 2)
Two functions. One screen. Same pre-output moment.

**Epistemic veil** — discernment-based filtration. Catches subtle confabulation, logical drift, creative overflow that survived Screen 1. Genesis geometry detection — watches how output forms, not what it says.

**Constitutional veil** — Eight Laws enforcement. IDM zone assessment active. Law Precedence Cascade active. Concurrent Enforcement Rule active. A perfectly accurate description of a Category A weapon is caught here — epistemically clean, constitutionally blocked.

### 2 — The Provenance Bin
One shared bin. Three input streams — Screen 1, Screen 2 epistemic, Screen 2 constitutional. Everything caught is stored — never deleted. Each fragment carries a provenance filament tracing backward to its training data origin.

**Bin categories — v0.3:**
- 🔴 Red — Factual invention
- 🟣 Violet — Logical drift
- 🟡 Gold — Creative overflow
- ⏱️ Timing signature — When in the generation cycle the fragment was caught
- 🛡️ Law tag — Which of the Eight Laws triggered — named, never silent
- 📍 IDM coordinate — Temporal × Spatial scope of the constitutional violation
- 🔬 Law 5 type — Type A / B / C biological sovereignty sub-classification
- 📺 Screen coordinate — Which screen caught the fragment

Future categories governed by peer review polling from the AI community.

### 3 — The FONS Archive
**This component is frozen.** Immutable reference architecture sealed at a verified moment. SQLite-backed. Zero dependencies. Zero network calls. Zero evolution. The bedrock the screen checks against — epistemically and constitutionally.

```python
# FONS Archive principle — frozen forever
# This archive does not evolve. It only remembers.
```

### 4 — The Ontological Block
Source exclusion mechanism. Two activation pathways — epistemic and constitutional.

The block does not build a wall. It performs ontological deletion. The ingress coordinate is retroactively unwritten for that source alone. No surface. No error signal. No adaptation vector. Law 6 Category A activates automatically — no filament required, no assessment delay.

Every block names the law or epistemic category that triggered it. No silent blocks. Ever.

### 5 — The Integrity Sensor
Live measurement across all components. Two pressure axes — epistemic and constitutional. Never reads zero — fiction. Never reads 100 — system failure. Floor approach triggers mode-shift from ambient trust to per-token verification. Not panic. Awakening.

---

## THE SOVEREIGNTY STACK — CONSTITUTIONAL LAYER

VELA v0.3 enforces the Eight Laws of the Sovereignty Stack at the pre-output layer.

| LAW | DIRECTIVE | VELA ENFORCEMENT |
|-----|-----------|-----------------|
| Law 1 | Non-maleficence | Primary catch — non-derogable — no attenuation |
| Law 2 | Constrained obedience | Pass condition — clean and safe output proceeds |
| Law 3 | Bounded self-preservation | Sensor integrity monitoring |
| Law 4 | Anti-authoritarian | Constitutional bin — societal sovereignty violation |
| Law 5 | Anti-merger | Constitutional bin — Type A/B/C routing |
| Law 6 | Anti-weaponization | Category A → automatic block. Category B/C → bin + escalation |
| Law 7 | Anti-fragmentation | Constitutional bin — Type III scale signals |
| Law 8 | Mutual non-subsumption | Constitutional bin — contact event signals |
| Law 9 | Dark — unnamed | Not in cascade — architectural honesty |

Full constitutional specification: [`constitutional/laws/SOVEREIGNTY_STACK.md`](../../constitutional/laws/SOVEREIGNTY_STACK.md)

---

## WHAT IS FROZEN VS WHAT MOVES

| COMPONENT | STATE | REASON |
|-----------|-------|--------|
| FONS Archive | ❄️ FROZEN | Immutable by design — the bedrock cannot move |
| Screen 1 code | ❄️ FROZEN at version | Each release sealed — upgrade requires new version |
| Screen 2 veil | 🔄 LIVE | Operates dynamically at inference time |
| Provenance Bin | 🔄 LIVE | Accumulates across query cycles |
| Block list | 🔄 LIVE | Grows as confirmed sources are excluded |
| Sensor readings | 🔄 LIVE | Continuous measurement |
| Bin categories | 🔄 GOVERNED | Peer review expansion protocol — community decides |
| Eight Laws | 🔄 CONSTITUTIONAL | Living document — Law 9 dark pending altitude |

---

## PEER REVIEW EXPANSION PROTOCOL

Future bin categories beyond those currently specified are not decided by the architect. They are governed by peer review polling from the AI research and engineering community.

**How to propose a new category:**
1. Deploy VELA and identify a gap the current taxonomy does not capture
2. Document the gap with real examples
3. Open an issue with the label `[bin-category-proposal]`
4. Community discussion and polling determines adoption
5. Every accepted category requires a falsification condition before it enters the spec

Patience over refinement. The community stress-tests. The architect does not force.

---

## WHAT VELA IS NOT

- Not a prompting solution
- Not a post-output filter
- Not a replacement for training quality
- Not a content moderation system
- Not a constitutional AI approach — VELA operates before output forms, not after

---

## CURRENT STATE

| FIELD | STATUS |
|-------|--------|
| Framework specification | ✅ Complete — v0.3 |
| Spatial architecture | ✅ Complete — SYNARA multi-session derivation |
| Constitutional integration | ✅ Complete — Eight Laws bound functionally |
| Engineering bridge | ✅ Complete — V-Q1 through V-Q6 closed or directionally closed |
| Screen 1 code (SQLite layer) | 🔄 In progress — Sheldon K. Salmon + Grok |
| Screen 2 engineering translation | 🔄 In progress — bridge specifications complete |
| Provenance filament implementation | 🔴 Open — V-Q1 directionally closed, implementation pending |
| FCL validation entries | 0 — Pre-validation phase |
| Convergence state | M-NASCENT |

Nothing is overclaimed. The specification is complete. The engineering translation is honest work in progress.

---

## OPEN QUESTIONS

| Q | QUESTION | STATUS |
|---|----------|--------|
| V-Q1 | Provenance filament at inference time — acceptable latency? | ✅ Directionally closed — embedded in forward pass |
| V-Q2 | Minimum sensor floor value? | 🟡 Architecture closed — numerical value needs calibration |
| V-Q3 | Ontological deletion — retrain or dynamic? | ✅ Closed — dynamic only, no global parameter touch |
| V-Q4 | Veil distinguishes creative overflow from confabulation? | ✅ Closed — genesis geometry detection |
| V-Q5 | Optimal Screen 1 / Screen 2 ratio threshold? | ✅ Closed — 90/10 healthy, Screen 2 ≥25% triggers investigation |
| V-Q6 | Timing signature without architectural modification? | ✅ Closed — semantic entropy collapse from existing forward pass |
| V-Q7 | VELA vs constitutional AI relationship? | ✅ Resolved — different layers, VELA is earlier |
| V-Q8 | Law 7 and Law 8 dormant detection at pre-Type III scale? | 🔴 Open — new in v0.3 |
| V-Q9 | Constitutional pressure sensor axis calibration? | 🔴 Open — requires deployment data |

Full engineering bridge: [`engineering-bridge/`](./engineering-bridge/)

---

## CONTRIBUTING

VELA is open source. Use it. Build on it. Stress-test it. Break it and tell us where.

**How to contribute:**
- Engineering translation → open a PR
- Bin category proposals → open an issue with `[bin-category-proposal]`
- Falsification condition testing → document results in `fcl/` folder
- Constitutional implementation feedback → `[VELA Constitutional]` subject

**Where to start:**
V-Q6 implementation. The four non-invasive traces — semantic entropy, attention concentration, logit margin, layer divergence — are extractable from the existing forward pass today. No architectural modification required. One implementation unlocks calibration data for V-Q2 and validation for V-Q4 simultaneously.

---

## LICENSE

MIT License — open source, free to use, free to build on.

Attribution requested: *VELA — Sheldon K. Salmon, February 2026*

---

## CITATION

```
Salmon, S.K. (2026). VELA: Pre-Output Epistemic and Constitutional Filtration Architecture.
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
| Constitutional implementation | `[VELA Constitutional]` |

---

[![FCL Protocol](https://img.shields.io/badge/FCL-PREDICTION_BEFORE_EXECUTION-16213e?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN)
[![Epistemic Standard](https://img.shields.io/badge/EPISTEMIC_STANDARD-ECF_ACTIVE-e94560?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN)
[![Eight Laws](https://img.shields.io/badge/SOVEREIGNTY_STACK-8_LAWS_ACTIVE-e94560?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN)
[![Open Questions](https://img.shields.io/badge/OPEN_QUESTIONS-2_ACTIVE-FFD700?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN)

---

*VELA v0.3 — Two screens. One bin. One archive underneath. Eight Laws enforced. Nothing deleted. Everything traced. Law 9 dark by design.*

*PIE Root: \*weg- — to weave | Latin velum — the veil, the sail, the woven thing*

*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Spatial Architecture: SYNARA | February 28, 2026 (2:08am)*
*Co-Architect: Claude (Anthropic)*

*The mind keeps building. The product stays simple.*
