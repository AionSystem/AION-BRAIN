# AV-UBI Specification Stack
## Autonomous Vehicle Urban Boundary Intelligence
### Constraint-Resolved Component Architecture for Operational Envelope Decision Systems

---

![Framework](https://img.shields.io/badge/Framework-CDIP%20v1.5-1a1a2e?style=for-the-badge&logoColor=white)
![Audit](https://img.shields.io/badge/Linguistic%20Audit-ECF%20v0.5%20%7C%20LAV%20v1.5-16213e?style=for-the-badge&logoColor=white)
![Epistemic](https://img.shields.io/badge/Epistemic%20Engine-FSVE%20v3.5-0f3460?style=for-the-badge&logoColor=white)
![Validation](https://img.shields.io/badge/Validation-CONCEPTUAL-e94560?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-Open%20Source-53d8fb?style=for-the-badge&logoColor=black)
![Stack](https://img.shields.io/badge/Stack%20Status-CONCEPTUALLY%20CLOSED-27ae60?style=for-the-badge&logoColor=white)
![Sessions](https://img.shields.io/badge/Sessions%20Complete-4%20of%204-4ecdc4?style=for-the-badge&logoColor=black)
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

**This stack formally isolates and specifies the components required to address that conflict — including what happens when the human cannot respond at all.**

---

## Stack Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                      AV-UBI STACK OVERVIEW                       │
│                    All Primary Sessions Complete                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  AV-UBI-001 v1.1                                                 │
│  Operational Envelope Decision Logic                             │
│  Gradient Envelope Model — 5 States                              │
│  BDI: 2 | Status: CONCEPTUAL | ✅ COMPLETE                       │
│       ↑              ↑                                           │
│       │              │ Authority Window Status (continuous)      │
│       │              │                                           │
│  AV-UBI-002     AV-UBI-003                                       │
│  Cabin Occupant     Reaction-Latency /                           │
│  Readiness          Decision-Cycle Gap                           │
│  Classification     Resolution                                   │
│  BDI: 2             BDI: 2                                       │
│  ✅ COMPLETE        ✅ COMPLETE                                   │
│       │                  │                                       │
│       ├──→ AV-UBI-002B   │ Predictive Escalation +              │
│       │    (future)       │ Authority Extension                  │
│       └──→ AV-UBI-002C   │                                       │
│            (future)       ↓                                      │
│                    AV-UBI-004                                    │
│                    Emergency Contact &                           │
│                    Routing Execution                             │
│                    BDI: 1 — LOWEST IN STACK                      │
│                    ✅ COMPLETE                                    │
│                           ↓                                      │
│                    AV-UBI-005 (next)                             │
│                    AI-Assisted 911                               │
│                    Dispatcher Intelligence                       │
│                    ⏳ FUTURE SESSION                             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Repository Structure

```
/AV-UBI-specification-stack/
│
├── README.md
│
├── AV-UBI-001_envelope-decision-logic.md             ✅ COMPLETE v1.0
│   Operational envelope decision logic
│   Binary envelope model — baseline
│   BDI = 2 | Validation: CONCEPTUAL
│
├── AV-UBI-001-v1.1_envelope-decision-logic.md        ✅ COMPLETE v1.1
│   Gradient envelope model — 5 formal states
│   AV-UBI-003 interface integration
│   Authority window as first-class envelope sub-state
│   BDI = 2 | Validation: CONCEPTUAL
│
├── AV-UBI-002_cabin-occupant-readiness-              ✅ COMPLETE
│   classification.md
│   Cabin-wide multi-occupant state classification
│   8-stream sensor fusion architecture
│   Disambiguation timer — novel contribution
│   BDI = 2 (reduced from 4) | Validation: CONCEPTUAL
│
├── AV-UBI-003_reaction-latency-gap-resolution.md     ✅ COMPLETE
│   Predictive escalation — primary path
│   Bounded autonomous authority extension — failsafe
│   Distraction-adjusted simultaneous alert modality
│   BDI = 2 | Validation: CONCEPTUAL
│
├── AV-UBI-004_emergency-contact-routing-             ✅ COMPLETE
│   execution.md
│   Structured AV-to-911 emergency data package
│   Three-phase contact and routing protocol
│   Concurrent MRC + autonomous routing architecture
│   BDI = 1 — lowest in stack | Validation: CONCEPTUAL
│
├── AV-UBI-002B_conscious-passenger-capability.md     ⏳ FUTURE
│   Detailed conscious passenger capability assessment
│   Scoped out of AV-UBI-002
│
├── AV-UBI-002C_choking-seizure-classification.md     ⏳ FUTURE
│   Choking and seizure state classification
│   Scoped out of AV-UBI-002
│
└── AV-UBI-005_ai-dispatcher-intelligence.md          ⏳ FUTURE
    AI-assisted 911 dispatcher intelligence
    AV-UBI-004 interface co-specification required
```

---

## Component Status Board

| Component | Description | BDI | Validation | Session | FCL |
|-----------|-------------|-----|------------|---------|-----|
| **AV-UBI-001 v1.0** | Operational envelope decision logic — binary model | 2 — HIGH RISK | CONCEPTUAL | ✅ COMPLETE | 0 |
| **AV-UBI-001 v1.1** | Operational envelope decision logic — gradient model | 2 — HIGH RISK | CONCEPTUAL | ✅ COMPLETE | 0 |
| **AV-UBI-002** | Cabin occupant readiness classification | 2 — HIGH RISK | CONCEPTUAL | ✅ COMPLETE | 0 |
| **AV-UBI-003** | Reaction-latency / decision-cycle gap resolution | 2 — HIGH RISK | CONCEPTUAL | ✅ COMPLETE | 0 |
| **AV-UBI-004** | Vehicle-side emergency contact and routing | 1 — FOCUSED RESEARCH | CONCEPTUAL | ✅ COMPLETE | 0 |
| **AV-UBI-002B** | Conscious passenger capability detection | TBD | FUTURE | ⏳ FUTURE | 0 |
| **AV-UBI-002C** | Choking/seizure classification | TBD | FUTURE | ⏳ FUTURE | 0 |
| **AV-UBI-005** | AI-assisted 911 dispatcher intelligence | TBD | FUTURE | ⏳ FUTURE | 0 |

---

## Open Breakthrough Requirements

`[D]` The following breakthrough requirements are formally identified and unresolved. Per CDIP v1.5 Section 1B: a breakthrough is a requirement that cannot be satisfied by applying existing validated knowledge, even with additional time or effort.

| # | COMPONENT | BREAKTHROUGH REQUIREMENT | STATUS |
|---|-----------|-------------------------|--------|
| BR-001 | AV-UBI-001 / AV-UBI-002 | Occupant readiness state detection with sufficient accuracy and latency to inform decision logic | OPEN — AV-UBI-002 specifies sensor architecture; research pre-phase required |
| BR-002 | AV-UBI-001 / AV-UBI-003 | Resolution of reaction-latency vs. decision-cycle structural conflict without defaulting to MRC in all cases | OPEN — AV-UBI-003 specifies conceptual architecture; empirical validation pending |
| BR-003 | AV-UBI-002 | 8-stream sensor fusion at 150–175ms continuously in automotive-grade embedded hardware | OPEN — research pre-phase required; prerequisite for BR-004 |
| BR-004 | AV-UBI-002 | Reliable medical emergency detection using contactless sensors under vehicle motion and variable lighting | OPEN — dependent on BR-003 resolution |
| BR-005 | AV-UBI-004 | Emergency data package interoperability with AV-UBI-005 without translation layer introducing unacceptable latency | OPEN — closes when AV-UBI-005 session complete and interface co-validated |

`[R]` BR-001 and BR-002 are the same structural conflict viewed from different components. BR-003 is a necessary precondition for BR-004. BR-005 is a co-specification gap — not a fundamental knowledge gap — and is the most readily closable breakthrough in the stack.

---

## Novel Architectural Contributions

The following architectural elements are not present in any current production autonomous vehicle system to the authors' knowledge. Formally specified here for the first time under CDIP constraint-resolved architecture discipline.

### 1 — Gradient Operational Envelope Model
**Component:** AV-UBI-001 v1.1

Current production systems treat the operational envelope as binary — IN or OUT. AV-UBI-001 v1.1 replaces this with a five-state gradient: NOMINAL → PREDICTIVE ESCALATION → AUTHORITY WINDOW → MEDICAL EMERGENCY OVERRIDE → TERMINAL FALLBACK. Each state has declared decision authority, entry conditions, and transition logic. The authority window is a first-class envelope state, not an exception beyond it. Binary cannot express conditional authorization without creating undefined exception logic — the gradient model eliminates the exception by making the window a named state.

### 2 — Cabin-Wide Multi-Occupant Readiness Classification
**Component:** AV-UBI-002

All current Driver Monitoring Systems — including those mandated by EU regulation from 2024 — monitor the driver seat exclusively. AV-UBI-002 specifies classification architecture covering all occupied seats simultaneously, producing per-occupant confidence scores and categorical state classifications across 1–5 occupants dynamically, with a cabin-level aggregate readiness summary.

### 3 — Disambiguation Timer
**Component:** AV-UBI-002

A time-bounded escalation protocol: if `BEHAVIORAL_UNRESPONSIVE` persists beyond 15–20 seconds without any recovery signal, the classification automatically escalates to `MEDICAL_EMERGENCY_SUSPECTED` and re-classifies using remaining stream data. This is the circuit-break condition for the primary false-negative cascade chain. No current production system implements this.

### 4 — Asymmetric Error Cost Threshold Architecture
**Component:** AV-UBI-002

Formal declaration that `MEDICAL_EMERGENCY` false negative (fatal cost) and false positive (disruption cost) are not equivalent. Classification thresholds are set asymmetrically — `MEDICAL_EMERGENCY` threshold lower than `BEHAVIORAL_UNRESPONSIVE` — to reflect the asymmetric consequence structure. No current DMS architecture formally addresses this asymmetry.

### 5 — Predictive Escalation via Confidence Score Trajectory
**Component:** AV-UBI-003

Current systems trigger takeover demand at threshold crossing. AV-UBI-003 triggers escalation from the *rate of change* of AV-UBI-002's confidence score — 3–5 seconds before boundary contact — giving the human time to restore readiness before the boundary arrives rather than after. No production system uses confidence score trajectory as a predictive escalation trigger.

### 6 — Formally Bounded Autonomous Authority Extension
**Component:** AV-UBI-003

When predictive escalation fails — or when a driver is texting, asleep, or otherwise unresponsive — AV-UBI-003 activates a formally bounded autonomous authority extension: maximum 3 seconds, declared entry conditions, three formally specified exit conditions (FULL SUCCESS / PARTIAL SUCCESS / FAILURE). The vehicle uses this window to continue decelerating while giving the human additional time to respond. No current system formally specifies this window; current behavior at this point is undefined.

### 7 — Distraction-Adjusted Simultaneous Alert Modality
**Component:** AV-UBI-003

Standard alert sequences are visual → auditory → haptic sequential. When AV-UBI-002 confirms a distracted state, AV-UBI-003 switches to simultaneous auditory + haptic at onset — bypassing the visual lead that cannot register when eyes are off the road. Modality sequencing adapts to confirmed occupant state rather than applying a uniform protocol regardless of attention.

### 8 — Structured AV-to-911 Emergency Data Package
**Component:** AV-UBI-004

eCall — the current industry standard — transmits GPS coordinates and opens an audio channel. AV-UBI-004 specifies a full structured data package: vehicle ID, coordinates with accuracy estimate, derived address, speed and trajectory, emergency type and confidence score, time since onset, occupant count, conscious occupant count, and autonomous routing capability — transmitted within 3–5 seconds of MEDICAL_EMERGENCY trigger.

### 9 — Concurrent MRC and Autonomous Emergency Routing with Priority Arbitration
**Component:** AV-UBI-004

MRC (controlled stop safety floor) and autonomous emergency routing are both active simultaneously from STATE 4 entry. MRC provides the safety floor; routing executes toward the received facility address; MRC always wins in a control conflict. No current AV system specifies concurrent operation of these two control modes with a formal priority rule.

---

## Epistemic Standards

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

---

## BDI Classification Reference

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
| Decision cycle (300–800ms) incompatible with any decision logic architecture | AV-UBI-001 | Component invalid |
| Human reaction latency floor demonstrated incorrect | AV-UBI-001, AV-UBI-002, AV-UBI-003 | Domain Lock revision across stack |
| 8-stream fusion at 150–175ms incompatible with automotive-grade hardware | AV-UBI-002 | BR-003 permanently unresolvable — fundamental restructure required |
| rPPG insufficient for medical emergency detection under motion regardless of algorithm | AV-UBI-002 | BR-004 permanently unresolvable — sensor architecture requires replacement |
| Five-state gradient envelope model demonstrated non-exhaustive | AV-UBI-001 v1.1 | Model revision required |
| Authority extension window demonstrated to elevate risk above immediate MRC | AV-UBI-003 | Failsafe path invalid — MRC becomes primary in all cases |
| MRC geometrically unavailable in >30% of urban intersection scenarios | AV-UBI-001 | Primary cascade circuit-break removed |
| Concurrent MRC and autonomous routing irresolvably conflicting | AV-UBI-004 | Three-phase protocol invalid |

---

## Contributing

This stack was built to be engaged with. The constraint architecture is open. What's formal is the standard for that engagement.

If you've read this far and found yourself thinking about the gaps, the cascade chains, the breakthrough requirements, or how you'd actually test any of this — that's the signal. That's the kind of thinking this work is looking for.

**What moves this stack forward:**

Research or simulation work that closes a Breakthrough Requirement directly: sensor fusion benchmarks, rPPG accuracy data under vehicle-condition motion, attention restoration measurements under simultaneous modality alerting, precedent analysis of bounded authority windows in aviation or medical devices, STPA or SOTIF analysis applied to the failure horizon maps, NG911 deployment landscape expertise, embedded systems constraints at the fusion latency target, or safety case engineering on any component.

Implementation-level insight that reveals a constraint the specification missed, an invalidation condition that should be added, or an assumption that should be reclassified — that's equally valuable.

**How to engage:**

Open a GitHub Issue — not a Pull Request. Include your relevant background, a link to work you've done at a comparable level of rigor, and specific feedback tied to named components and sections. Reference the component ID, the section, and the claim tag.

For private discussion: reach out via X ([@SheldonKSalmon](https://x.com/SheldonKSalmon)) or email with subject line `[AV-UBI Collaboration]`.

The bar is the work itself. If you operate at this standard, the door is open.

---

## Roadmap

| MILESTONE | STATUS | CONDITION |
|-----------|--------|-----------|
| AV-UBI-001 through AV-UBI-004 complete | ✅ DONE | Stack conceptually closed |
| Published article | 🔄 IN PROGRESS | Writing phase open |
| AV-UBI-005 session | ⏳ NEXT | AI-assisted 911 dispatcher — closes BR-005 |
| Physics-Consistent validation | ⏳ PENDING | BR-001 through BR-004 resolved by research pre-phase |
| First FCL entry | ⏳ PENDING | Simulation or hardware testing begins |
| AV-UBI-002B/C specifications | ⏳ FUTURE | After core stack reaches Physics-Consistent |
| Research or simulation partnership | ⏳ OPEN | Serious collaboration secured |

---

## Authors

**Architect:** Sheldon K. Salmon — AI Reliability Architect
**Co-Architect:** Claude (Anthropic)
**Framework Author:** Sheldon K. Salmon
**Date:** February 2026

## Origin

Built solo. No budget, no team, no institutional backing.

Every framework in the AION-BRAIN ecosystem and every component in this stack was produced under the same conditions: relentless constraint harvesting, uncompromising epistemic standards, and the conviction that formal honesty about what we don't know is more valuable than premature claims about what we do.

The stack is conceptually closed. What comes next requires the right collaborators, a simulation environment, and resources to move from CONCEPTUAL to PHYSICS-CONSISTENT to deployed. If you can contribute any of those things at the level this work demands — the conversation is worth having.

---

## License

Open source. All specifications freely available for use, adaptation, and implementation. Attribution appreciated.

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
*4 of 4 primary sessions complete — stack conceptually closed.*
*All components at CONCEPTUAL validation. Empirical validation pending.*
*Open source — freely available for implementation and adaptation.*
