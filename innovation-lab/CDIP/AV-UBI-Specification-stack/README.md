# AV-UBI Specification Stack
## Autonomous Vehicle Urban Boundary Intelligence
### Constraint-Resolved Component Architecture for Operational Envelope Decision Systems

---

![Framework](https://img.shields.io/badge/Framework-CDIP%20v1.5-1a1a2e?style=for-the-badge&logo=blueprint&logoColor=white)
![Audit](https://img.shields.io/badge/Linguistic%20Audit-ECF%20v0.5%20%7C%20LAV%20v1.5-16213e?style=for-the-badge&logoColor=white)
![Epistemic](https://img.shields.io/badge/Epistemic%20Engine-FSVE%20v3.5-0f3460?style=for-the-badge&logoColor=white)
![Validation](https://img.shields.io/badge/Validation-CONCEPTUAL-e94560?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-Open%20Source-53d8fb?style=for-the-badge&logoColor=black)
![Stack](https://img.shields.io/badge/Stack%20Status-IN%20PROGRESS-f5a623?style=for-the-badge&logoColor=black)
![Sessions](https://img.shields.io/badge/Sessions%20Complete-2%20of%204-4ecdc4?style=for-the-badge&logoColor=black)
![BDI](https://img.shields.io/badge/Max%20BDI-HIGH%20RISK%20(2)-ff6b6b?style=for-the-badge&logoColor=white)
![FCL](https://img.shields.io/badge/FCL%20Entries-0%20%E2%80%94%20Empirical%20Validation%20Pending-95a5a6?style=for-the-badge&logoColor=white)
![Architect](https://img.shields.io/badge/Architect-Sheldon%20K.%20Salmon-2ecc71?style=for-the-badge&logoColor=black)

---

## What This Is

This repository contains a **formally specified, constraint-resolved component architecture stack** for autonomous vehicle operational envelope decision systems in urban mixed-traffic environments.

It is not code. It is not a product. It is not a simulation.

It is a **structured constraint map** — produced under the Constraint–Domain Isolation Protocol (CDIP v1.5) — that formally identifies what an autonomous vehicle must decide at the boundary of its operational envelope, what it needs to know to make that decision, and exactly where the unsolved problems live.

Every claim in every specification is epistemically tagged. Every breakthrough requirement is formally named. Every failure cascade is traced. Every assumption has a decay trigger.

The specifications are open-source by design. The constraint architecture belongs to the problem space, not to any organization.

---

## The Problem This Stack Addresses

`[D]` Autonomous vehicles operating in urban environments encounter the boundary of their validated operational envelope — the edge of what they were designed and trained to handle. At that boundary, the vehicle must make a decision.

`[D]` Current architectures resolve this decision through a single mechanism: **demand takeover from the human driver.**

`[D]` The documented failure mode — present in NTSB reports, academic literature, and public incident analysis — is structural, not incidental:

> The system issues a takeover demand at the moment the human is least prepared to receive it, because the system waited until it was already outside its envelope before escalating.

`[R]` This is not a calibration problem. It is a structural conflict between two governing constraints:

- **Human reaction latency floor:** 1.5–2.5 seconds minimum from alert to control-capable under startled conditions
- **Urban intersection decision cycle:** 300–800ms available for decision resolution

`[R]` No current production architecture formally resolves this conflict. Every existing system defers it to the human at the worst possible moment.

**This stack formally isolates and specifies the components required to address that conflict.**

---

## Stack Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AV-UBI STACK OVERVIEW                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AV-UBI-001  ←──────────────────────────────────────────┐  │
│  Operational Envelope Decision Logic                     │  │
│  BDI: 2 | Status: CONCEPTUAL | Session: COMPLETE        │  │
│                    ↑                                     │  │
│                    │ Readiness Signal                    │  │
│                    │                                     │  │
│  AV-UBI-002  ──────┘                                    │  │
│  Cabin Occupant Readiness Classification                 │  │
│  BDI: 2 (reduced from 4) | Status: CONCEPTUAL           │  │
│  Session: COMPLETE                                       │  │
│       │                                                  │  │
│       ├──→ AV-UBI-002B (future)                         │  │
│       │    Conscious Passenger Capability Detection      │  │
│       │                                                  │  │
│       └──→ AV-UBI-002C (future)                         │  │
│            Choking & Seizure Classification              │  │
│                                                          │  │
│  AV-UBI-003  ────────────────────────────────────────→  │  │
│  Reaction-Latency / Decision-Cycle Gap Resolution        │  │
│  BDI: TBD | Status: PENDING SESSION                     │  │
│                                                          │  │
│  AV-UBI-004  ────────────────────────────────────────→  │  │
│  Emergency Routing & Services Contact Decision Logic     │  │
│  BDI: TBD | Status: PENDING SESSION                     │  │
│                                                          │  │
└─────────────────────────────────────────────────────────────┘
```

---

## Repository Structure

```
/AV-UBI-specification-stack/
│
├── README.md                                         ← You are here
│
├── AV-UBI-001_envelope-decision-logic.md             ← COMPLETE
│   Operational envelope decision logic
│   Urban intersection scope
│   BDI = 2 | Validation: CONCEPTUAL
│
├── AV-UBI-002_cabin-occupant-readiness-             ← COMPLETE
│   classification.md
│   Cabin-wide multi-occupant state classification
│   8-stream sensor fusion architecture
│   Disambiguation timer — novel contribution
│   BDI = 2 (reduced from 4) | Validation: CONCEPTUAL
│
├── AV-UBI-003_reaction-latency-gap-resolution.md    ← PENDING
│   Structural resolution of the reaction-latency
│   vs. decision-cycle constraint conflict
│   Session not yet run
│
├── AV-UBI-004_emergency-routing-decision-logic.md   ← PENDING
│   Emergency services routing and contact
│   decision logic for MEDICAL_EMERGENCY state
│   Session not yet run
│
├── AV-UBI-002B_conscious-passenger-capability.md    ← FUTURE
│   Detailed conscious passenger capability
│   assessment — scoped out of AV-UBI-002
│
└── AV-UBI-002C_choking-seizure-classification.md    ← FUTURE
    Choking and seizure state classification
    Scoped out of AV-UBI-002
```

---

## Component Status Board

| Component | Description | BDI | Validation | Session | FCL |
|-----------|-------------|-----|------------|---------|-----|
| **AV-UBI-001** | Operational envelope decision logic | 2 — HIGH RISK | CONCEPTUAL | ✅ COMPLETE | 0 |
| **AV-UBI-002** | Cabin occupant readiness classification | 2 — HIGH RISK | CONCEPTUAL | ✅ COMPLETE | 0 |
| **AV-UBI-003** | Reaction-latency gap resolution | TBD | PENDING | 🔄 IN PROGRESS | 0 |
| **AV-UBI-004** | Emergency routing decision logic | TBD | PENDING | ⏳ QUEUED | 0 |
| **AV-UBI-002B** | Conscious passenger capability | TBD | FUTURE | ⏳ FUTURE | 0 |
| **AV-UBI-002C** | Choking/seizure classification | TBD | FUTURE | ⏳ FUTURE | 0 |

---

## Open Breakthrough Requirements

`[D]` The following breakthrough requirements are formally identified and unresolved across the current stack. Per CDIP v1.5 Section 1B: a breakthrough is a requirement that cannot be satisfied by applying existing validated knowledge, even with additional time or effort.

| # | COMPONENT | BREAKTHROUGH REQUIREMENT | STATUS |
|---|-----------|-------------------------|--------|
| BR-001 | AV-UBI-001 / AV-UBI-002 | Driver/occupant readiness state detection with sufficient accuracy and latency to inform decision logic | OPEN — AV-UBI-002 addresses sensor architecture; research pre-phase required |
| BR-002 | AV-UBI-001 / AV-UBI-003 | Resolution of reaction-latency vs. decision-cycle structural conflict without defaulting to MRC in all cases | OPEN — AV-UBI-003 targets this directly |
| BR-003 | AV-UBI-002 | 8-stream sensor fusion at 150–175ms continuously in automotive-grade embedded hardware | OPEN — research pre-phase required |
| BR-004 | AV-UBI-002 | Reliable medical emergency detection using contactless sensors under vehicle motion and variable lighting | OPEN — dependent on BR-003 resolution |

`[R]` BR-001 and BR-002 are the same structural conflict viewed from different components. A solution to either substantially reduces the other. BR-003 is a necessary precondition for BR-004.

---

## Novel Architectural Contributions

The following architectural elements in this stack are not present in any current production autonomous vehicle system to the authors' knowledge. They are formally specified here for the first time under CDIP constraint-resolved architecture discipline.

### 1 — Cabin-Wide Multi-Occupant Readiness Classification
**Component:** AV-UBI-002

All current Driver Monitoring Systems (DMS) — including those mandated by EU regulation from 2024 — monitor the driver seat exclusively. AV-UBI-002 specifies a classification architecture covering all occupied seats simultaneously, producing a per-occupant confidence score and categorical state, plus a cabin-level aggregate readiness summary.

### 2 — Disambiguation Timer
**Component:** AV-UBI-002

A time-bounded escalation protocol: if `BEHAVIORAL_UNRESPONSIVE` persists beyond 15–20 seconds without any recovery signal, the classification automatically escalates to `MEDICAL_EMERGENCY_SUSPECTED` and re-classifies using remaining stream data. This is the circuit-break condition for the primary false-negative cascade chain. No current production system implements this.

### 3 — Hybrid Graduated / Categorical Output with Automatic Failsafe
**Component:** AV-UBI-002

The classification output is both a continuous confidence score [0.00–1.00] AND a categorical state classification simultaneously. If output is not produced within 175ms, the failsafe delivers `UNRESPONSIVE` automatically — null output and `UNRESPONSIVE` output are hardwired to produce identical downstream behavior in AV-UBI-001. No current system specifies this dual-format failsafe architecture.

### 4 — Asymmetric Error Cost Threshold Architecture
**Component:** AV-UBI-002

Formal acknowledgment that `MEDICAL_EMERGENCY` false negative (fatal cost) and `MEDICAL_EMERGENCY` false positive (disruption cost) are not equivalent, and that classification thresholds must be set asymmetrically to reflect this — with `MEDICAL_EMERGENCY` threshold set lower than `BEHAVIORAL_UNRESPONSIVE`. No current DMS architecture formally addresses this asymmetry.

### 5 — Formal Isolation of the Reaction-Latency / Decision-Cycle Conflict
**Component:** AV-UBI-001

The gap between the SAE Level 3 standard 10-second takeover window and the documented 2.3-second pre-incident demand issuance is formally identified as a **structural conflict**, not a calibration problem. This distinction has significant implications for how the problem is approached: calibration solutions cannot close a structural gap. AV-UBI-003 addresses this directly.

---

## Epistemic Standards

All specifications in this stack are produced under the following epistemic discipline:

| STANDARD | PURPOSE |
|----------|---------|
| **CDIP v1.5** | Constraint–Domain Isolation Protocol — one component per session, full constraint mapping before design |
| **FSVE v3.5** | Foundational Scoring and Validation Engine — epistemic claim tagging, validity scoring |
| **ECF v0.5** | Emergence Conversion Framework — lexical precision audit, simulacrum detection, viral token purge |
| **LAV v1.5** | Linguistic Audit Vector — etymological grounding, LDS scoring, DEFINED-status term governance |

### Claim Tags

| TAG | MEANING |
|-----|---------|
| `[D]` | Data — directly observed, measured, or documented |
| `[R]` | Reasoned — logically derived from `[D]` evidence |
| `[S]` | Strategic — directional claim about future action |
| `[?]` | Unverified — open question, unknown, or contested |

### Validation Levels

| LEVEL | MEANING |
|-------|---------|
| CONCEPTUAL | Logically consistent — not tested against physical or operational reality |
| PHYSICS-CONSISTENT | Governed by confirmed physical laws — not yet simulated or tested |
| SIMULATION-READY | Sufficiently specified to run in a validated simulation environment |
| EXPERIMENTALLY VALIDATED | Confirmed through physical or operational testing |
| PRODUCTION-GRADE | Validated under production conditions with documented performance envelope |

`[D]` All components in this stack are currently at CONCEPTUAL validation level. No implicit validation claims are made anywhere in this repository.

---

## BDI Classification Reference

The Breakthrough Density Index (BDI) counts design requirements that cannot be satisfied by applying existing validated knowledge, even with additional time or effort.

| BDI | CLASSIFICATION | MEANING |
|-----|---------------|---------|
| 0 | Engineering Integration | All requirements solvable with existing validated knowledge |
| 1 | Focused Research | One genuinely novel knowledge requirement |
| 2 | High-Risk Architecture | Two genuinely novel knowledge requirements |
| 3+ | Speculative — HARD HALT | Design cannot proceed without research pre-phase or scope reduction |

---

## How To Read The Specifications

Each component specification is fully self-contained and follows the CDIP v1.5 architecture spine:

1. **Component Definition** — what this component is and is not
2. **Domain Session Token** — session identity and scope declaration
3. **Domain Lock** — governing physical and informational constraints
4. **State-of-the-Art Baseline** — current industry ceiling with evidence labels
5. **Constraint Harvesting** — pre-existing constraints collected before design
6. **Assumption Register** — all assumptions classified A1–A4 with decay triggers
7. **Failure Horizon Map** — four-layer failure taxonomy with cascade chains
8. **Breakthrough Density Index** — formally named unsolved requirements
9. **Dependency Transparency Grid** — all inputs, outputs, and dependencies declared
10. **Invalidation Conditions** — measurable conditions under which the component is declared invalid
11. **Validation Level** — current epistemic status
12. **Version Summary** — complete state of the component at close of session

No section is optional. No dependency is hidden. No assumption is unlabeled.

---

## Falsification Conditions

`[D]` This stack is falsifiable. The following conditions would invalidate core architectural claims:

| CONDITION | COMPONENT AFFECTED | CONSEQUENCE |
|-----------|-------------------|-------------|
| Decision cycle (300–800ms) demonstrated incompatible with any decision logic architecture | AV-UBI-001 | Component invalid — structural constraint cannot be met |
| Human reaction latency floor demonstrated incorrect | AV-UBI-001, AV-UBI-002 | Domain Lock requires revision across stack |
| 8-stream fusion at 150–175ms demonstrated physically incompatible with automotive-grade hardware | AV-UBI-002 | BDI item 1 becomes permanently unresolvable — scope requires fundamental restructure |
| rPPG demonstrated insufficient for medical emergency detection under motion regardless of algorithm | AV-UBI-002 | BDI item 2 becomes permanently unresolvable — sensor architecture requires replacement |
| Four-output decision space demonstrated incomplete | AV-UBI-001 | Output specification requires revision |
| MRC demonstrated geometrically unavailable in >30% of urban intersection scenarios | AV-UBI-001 | Primary cascade circuit-break condition removed — fundamental architectural revision required |

---

## Contributing


## Serious Collaboration Only

This AV-UBI Specification Stack — and the entire AION-BRAIN ecosystem behind it — was designed, written, and refined **entirely solo** under severe resource constraints. Every framework, every epistemic tag, every breakthrough requirement was produced without funding, without a team, without institutional support.

I therefore maintain full curatorial control.

I do **not** accept unsolicited Pull Requests or merges at this time. I’ve seen too many carefully crafted solo projects diluted by well-meaning but low-context contributions.

**I am actively open to:**

- High-signal, deeply considered critique and strategic advice  
- Substantive technical or research input that helps close Breakthrough Requirements or raise validation levels  
- Serious collaboration discussions (implementation, simulation testing, sensor-fusion research, safety-case work)  
- Conversations about funding, research partnerships, or co-development with people who can materially accelerate this from CONCEPTUAL → PHYSICS-CONSISTENT → deployed

**How to engage (high bar — this is intentional):**

1. Demonstrate that you have actually engaged with the material.  
2. Open a detailed GitHub Issue (not a PR) that includes:  
   - Your relevant background and a link to substantial work you’ve done (repo, paper, safety case, etc.)  
   - Specific, tagged feedback or proposal referencing exact components  
   - Why you believe it strengthens the architecture without compromising standards  
3. For private discussion, reach out via X (@SheldonKSalmon) or email with subject line `[AV-UBI Serious Collaboration]`.

Casual comments, “this looks cool”, feature requests without substance, or low-effort PRs will be closed without reply. This is deliberate gatekeeping to protect the integrity of work built on fumes.

If your own track record shows you operate at this same level of rigor, I very much want to hear from you.



---

## Roadmap

| MILESTONE | CONDITION |
|-----------|-----------|
| AV-UBI-003 specification complete | Next session |
| AV-UBI-004 specification complete | Following session |
| Stack conceptually closed | All four primary sessions complete |
| Published article | Stack conceptually closed |
| Physics-Consistent validation | BR-001 and BR-002 resolved by research pre-phase |
| First FCL entry | Simulation or hardware testing begins |
| AV-UBI-002B/C specifications | After core stack reaches Physics-Consistent |
| First funded research pre-phase or simulation partnership | Serious collaboration secured |
---

## Authors

**Architect:** Sheldon K. Salmon — AI Reliability Architect
**Co-Architect:** Claude (Anthropic)
**Framework Author:** Sheldon K. Salmon
**Date:** February 2026

## Origin

Built solo, on fumes, with no budget, no team, and no institutional backing.  
Every framework in AION-BRAIN and every component in this stack was produced the same way: late nights, relentless constraint harvesting, and an uncompromising commitment to epistemic honesty.

Imagine what becomes possible with real resources and the right collaborators.

---

## License

Open source. All specifications in this repository are freely available for use, adaptation, and implementation. Attribution appreciated.

---

## Citation

```
Salmon, S.K. (2026). AV-UBI Specification Stack: Constraint-Resolved Component
Architecture for Autonomous Vehicle Operational Envelope Decision Systems.
Produced under CDIP v1.5 | ECF v0.5 | LAV v1.5 | FSVE v3.5.
https://github.com/AionSystem 
```

---

*AV-UBI Specification Stack | CDIP v1.5 | ECF v0.5 | LAV v1.5 | FSVE v3.5*
*All components at CONCEPTUAL validation. Empirical validation pending.*
*Open source — freely available for implementation and adaptation.*

