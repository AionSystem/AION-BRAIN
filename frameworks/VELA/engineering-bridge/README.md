# VELA — Engineering Bridge

This folder contains narrative engineering specifications derived from SYNARA's spatial architecture sessions.

VELA's framework specification tells engineers **what** to build. The engineering bridge tells engineers **what right feels like when it is working** — the target state in spatial language that no technical brief alone can provide.

Read both together. They are one complete brief.

---

## WHAT IS IN THIS FOLDER

| FILE | COVERS | STATUS |
|------|--------|--------|
| [VQ-1-3.md](./VQ-1-3.md) | V-Q1 (latency), V-Q2 (sensor floor), V-Q3 (retraining vs dynamic block) | V-Q1 closed. V-Q2 architecture closed, value open. V-Q3 closed. |
| [VQ-4-6.md](./VQ-4-6.md) | V-Q4 (creative vs confabulation), V-Q5 (screen ratio threshold), V-Q6 (timing signature) | V-Q4 closed. V-Q5 closed. V-Q6 closed. |

---

## OPEN QUESTIONS AVAILABLE TO ENGINEERS

The full open question register lives here:

[![Open Questions](https://img.shields.io/badge/OPEN_QUESTIONS-REGISTER-e94560?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN/tree/main/frameworks%2FVELA%2Fopen-questions)

**Current open question status:**

| Q | QUESTION | BRIDGE DOCUMENT | STATUS |
|---|----------|----------------|--------|
| V-Q1 | Can provenance filament tracing be implemented at inference time with acceptable latency? | [VQ-1-3.md](./VQ-1-3.md) | ✅ Closed — embedded in forward pass geometry |
| V-Q2 | What is the minimum sensor floor before system integrity is compromised? | [VQ-1-3.md](./VQ-1-3.md) | 🟡 Architecture closed — numerical value requires deployment calibration |
| V-Q3 | Does ontological deletion require model retraining or dynamic application? | [VQ-1-3.md](./VQ-1-3.md) | ✅ Closed — dynamic only, no global parameter touch, building never goes dark |
| V-Q4 | How does the veil distinguish creative overflow from confabulation? | [VQ-4-6.md](./VQ-4-6.md) | ✅ Closed — genesis geometry detection, four falsifiable tests specified |
| V-Q5 | What is the optimal Screen 1 / Screen 2 catch ratio threshold? | [VQ-4-6.md](./VQ-4-6.md) | ✅ Closed — 90/10 healthy baseline, Screen 2 ≥25% triggers investigation |
| V-Q6 | Can timing signature be extracted without architectural modification? | [VQ-4-6.md](./VQ-4-6.md) | ✅ Closed — semantic entropy collapse detectable from existing forward pass |
| V-Q7 | What is the relationship between VELA and constitutional AI approaches? | Not yet built | 🟡 Provisional — likely complementary, confirmation needed |

---

## WHERE TO START — CRITICAL PATH FOR ENGINEERS

Five of six primary questions are now closed. The architecture is specified. What remains is implementation.

**Start with V-Q6.**

The four non-invasive traces — semantic entropy, attention concentration, logit margin, layer-wise representation divergence — are all extractable from the existing forward pass today. No new architecture required. No modification to weights or attention mechanisms.

Implement the V-Q6 monitoring layer first. The data it produces will:
- Calibrate V-Q2's numerical floor value
- Validate V-Q4's genesis geometry detection in real deployment
- Produce the first FCL validation entries for VELA

**One implementation unlocks three specifications simultaneously.**

---

## HOW TO USE THIS FOLDER

If you are an engineer looking to contribute to VELA implementation:

1. Read [VELA v0.2 spec](../specs/VELA-v0.2.md) first — the full architectural specification
2. Read the relevant bridge document for the question you are working on
3. Check the [open questions register](https://github.com/AionSystem/AION-BRAIN/tree/main/frameworks%2FVELA%2Fopen-questions) for current status
4. Open a PR or issue with your findings — all contributions welcome

---

## A NOTE ON READING SYNARA'S SPATIAL LANGUAGE

The bridge documents are written in spatial narrative — not conventional technical prose.

This is intentional. Spatial language specifies the target state in a register that technical briefs cannot reach. When the bridge says *"the veil is already the medium the representation swims through"* — that is an architectural instruction, not a metaphor. When it says *"no global parameter touch — surgical micro-updates only"* — that is a hard constraint.

Read the spatial language as precisely as you would read a technical specification. It is one.

---

*VELA Engineering Bridge*
*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Spatial Architecture: SYNARA | February 2026*
*Co-Architect: Claude (Anthropic)*
