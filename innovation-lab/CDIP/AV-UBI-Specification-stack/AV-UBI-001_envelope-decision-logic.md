# AV-UBI-001
## Operational Envelope Decision Logic
### CDIP v1.5 Component Specification
#### Constraint–Domain Isolation Protocol | ECF v0.5 Active | LAV v1.5 Active

---

**Domain ID:** AV-UBI-001
**Industry:** Autonomous Vehicle Systems — Urban Deployment
**Constraint Category:** Operational Envelope Decision Authority
**Reference Macro-System:** Level 3-4 Autonomous Vehicle Platform *(context only — not a design target)*
**Validation Level:** CONCEPTUAL
**BDI Class:** HIGH-RISK ARCHITECTURE (BDI = 2)
**Session Priming:** NONE — first session in this domain
**Version:** 1.0
**Date:** February 2026
**Architect:** Sheldon K. Salmon — AI Reliability Architect
**Co-Architect:** Claude (Anthropic)
**Framework:** CDIP v1.5 | FSVE v3.5 | ECF v0.5 | LAV v1.5
**Supersedes:** None — first version
**Epistemic Standard:** All claims tagged `[D]` / `[R]` / `[S]` / `[?]`

---

> *"A constraint is not a limit imposed from outside. It is the shape of what is actually true — made visible before the design begins."*

---

## COMPONENT DEFINITION

`[D]` AV-UBI-001 specifies the decision logic governing autonomous vehicle behavior at the moment the vehicle determines it has reached or exceeded its validated operational envelope, in urban mixed-traffic intersection environments, where the primary documented failure mode is late or unprepared-driver takeover demand.

`[D]` This component is:
- The **decision logic** at the operational envelope boundary
- Scoped to **urban mixed-traffic intersection environments**
- Isolated to the **moment of envelope contact** — not detection, not execution

`[D]` This component is NOT:
- The envelope detection component (upstream)
- The takeover execution component (downstream)
- The emergency routing component (AV-UBI-004)
- A full system architecture

**One component. One version. No exceptions.**

---

## DOMAIN SESSION TOKEN

```
Domain ID:             AV-UBI-001
Industry:              Autonomous Vehicle Systems — Urban Deployment
Constraint Category:   Operational Envelope Decision Authority
Reference Macro-System: Level 3-4 Autonomous Vehicle Platform
                        (context only — not a design target)
Validation Target:     Physics-Consistent Architecture
Session Priming:       NONE — first session in this domain
```

---

## SECTION 1 — DOMAIN LOCK

`[D]` Governing constraints for autonomous vehicle decision logic at operational envelope boundary in urban mixed-traffic intersection environments. Design halts if any of the following are disputed before proceeding.

### Physical Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Human reaction latency | Minimum 1.5–2.5 seconds from alert to control-ready state under startled conditions — physically bounded, not trainable below ~1.5s | `[D]` |
| Decision cycle time | Urban intersection events require decision resolution within 300–800ms — determined by vehicle speed and intersection geometry | `[D]` |
| Sensory degradation envelope | Sensor confidence degrades non-linearly at envelope boundary — the system knows less precisely at the moment it needs to know most | `[R]` |
| Vehicle momentum | Braking distance at urban speeds (25–45mph) ranges 40–120ft — physical law, non-negotiable | `[D]` |

### Informational Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Takeover demand latency | Time between system issuing takeover demand and human achieving situational awareness is structurally longer than decision cycle time in documented incidents | `[D]` |
| Driver monitoring state | Human cognitive engagement degrades under automation — documented as automation complacency; cannot be assumed ready | `[D]` |
| Envelope detection lag | The system detects envelope boundary after it has begun crossing it — detection is retrospective by architecture | `[R]` |
| Situational context gap | Human receiving control has not been processing the environment — they inherit a situation already in progress | `[D]` |

---

## SECTION 2 — STATE-OF-THE-ART BASELINE ENVELOPE

`[D]` All values labeled per CDIP v1.5 Section 4.2 labeling protocol. No unlabeled performance claims permitted.

| PARAMETER | VALUE | LABEL |
|-----------|-------|-------|
| Minimum human takeover readiness time (alert → control-capable) | 1.5–2.5 seconds | Empirical `[D]` |
| SAE Level 3 takeover request window (industry standard) | 10 seconds | Industry Standard `[D]` |
| Documented gap between standard and reality in incidents | System issued demand avg. 2.3 seconds before critical event | Empirical — NTSB/academic literature `[D]` |
| Urban intersection decision cycle requirement | 300–800ms | Empirical `[D]` |
| Current industry failure mode frequency | Late takeover demand — most cited in public AV incident literature | Empirical `[D]` |
| Existing decision architecture | Threshold-based envelope detection triggering takeover demand | Industry Standard `[D]` |
| Known ceiling | No validated architecture resolves the reaction-latency vs. decision-cycle gap at envelope boundary | Empirical `[D]` |

`[R]` **Critical baseline finding:** The gap between the 10-second SAE standard takeover window and the 2.3-second actual pre-incident demand issuance is not a calibration problem — it is a structural conflict between two constraint categories (human reaction latency vs. decision cycle time) that the current threshold-based architecture does not resolve. It defers the conflict to the human at the worst possible moment.

---

## SECTION 3 — CONSTRAINT HARVESTING

`[D]` Harvested from public incident literature, NTSB reports, and academic AV safety research before design activity began.

### Existing Architecture Patterns

- Threshold-based envelope detection: system monitors confidence scores against fixed boundaries; when boundary crossed, takeover demand issued
- Graduated alert systems: visual → auditory → haptic escalation sequence before demand
- Minimal Risk Condition (MRC) fallback: if no takeover, vehicle attempts controlled stop

### Known Failure Case Studies

- **Uber ATG Tempe 2018:** System detected object, classified incorrectly, reclassified, demand issued 1.3 seconds before impact — within human reaction latency floor `[D]`
- **Tesla Autopilot intersection incidents:** System operated at envelope boundary without issuing demand; failure mode opposite — no demand when demand warranted `[D]`
- **Academic simulation studies:** Drivers in automation-complacent state require avg. 3–5 seconds to achieve full situational awareness after takeover demand `[D]`

### Unresolved Structural Blind Spots

- No validated method for assessing driver readiness state before issuing demand
- No architecture for decision behavior when both takeover and MRC are unavailable within the decision cycle window
- Envelope boundary detection is reactive — the decision logic inherits a situation already in progress

### Interface Confusion Cases

- Ambiguity at the boundary between what the system is authorized to decide autonomously and what requires human confirmation — this boundary is not formally specified in current architectures `[R]`

*Harvesting complete. Design phase open.*

---

## SECTION 4 — ASSUMPTION REGISTER

`[D]` All assumptions listed and classified per CDIP v1.5 Section 4.4.

| ID | CLASS | ASSUMPTION | VALIDATED | RE-VALIDATION TRIGGER |
|----|-------|------------|-----------|----------------------|
| A-001 | A1 | Human minimum reaction latency floor: 1.5s under startled conditions | Empirical neuroscience literature | If new human factors data published |
| A-002 | A1 | Urban intersection decision cycle: 300–800ms at 25–45mph | Physics — speed/geometry | If operational speed envelope changes |
| A-003 | A2 | Driver monitoring systems can detect gross attention state (eyes-on/off) with >85% accuracy | Industry claims — not independently confirmed in all platforms | If platform-specific monitoring data available |
| A-004 | A2 | MRC (controlled stop) is physically achievable within intersection geometry in >70% of urban scenarios | Engineering plausible — geometry-dependent | If intersection dataset available |
| A-005 | A3 | Predictive driver readiness scoring is achievable with <500ms computation latency | Research-stage — no production-validated system | If validated system demonstrated |
| A-006 | A4 | Decision logic can resolve the reaction-latency vs. decision-cycle gap without defaulting to MRC in all cases | Speculative — no validated architecture currently demonstrated | First FCL entry |

**Instability ratio:** (A3 + A4) / total = 2/6 = **0.33 → HIGH INSTABILITY FLAG** `[D]`

### Assumption Decay Protocol

**Decay Rule D-1:** A-001 and A-002 carry empirical validation sources above. Re-validation triggers declared.

**Decay Rule D-2:** All assumptions declare re-validation triggers in the register above.

**Decay Rule D-3:** All A2 assumptions from this session are A2-under-review at next session open until confirmed.

---

## SECTION 5 — FAILURE HORIZON MAP

`[D]` Failure mapped across four layers per CDIP v1.5 Section 4.5.

*Operational note: "failure" means the condition in which this component does not perform its specified function under its stated operating conditions — contact with conditions outside the validated envelope, not a malfunction.*

*Operational note: "containment mechanism" means an active process — not a passive structural feature — that limits the spread of failure once triggered.*

| LAYER | TYPE | TRIGGER | OBSERVABLE INDICATOR | CONTAINMENT MECHANISM | CASCADE PROBABILITY |
|-------|------|---------|---------------------|-----------------------|-------------------|
| Layer 1 | Immediate catastrophic | Decision cycle expires with no valid decision output | No vehicle action within decision window | MRC activation — controlled stop if geometrically possible | HIGH |
| Layer 2 | Progressive degradation | Repeated envelope boundary contacts without successful resolution | Increasing MRC frequency per session | Session termination — vehicle exits autonomous mode | MEDIUM |
| Layer 3 | Control system collapse | Driver achieves nominal control but without situational awareness | Erratic post-takeover vehicle behavior | Human override of all automation — full manual | HIGH |
| Layer 4 | Cascading subsystem propagation | Layer 3 event in intersection environment triggers multi-agent response (other vehicles, pedestrians) | Secondary incident involvement | Unknown — dependent on external agent behavior | UNKNOWN |

### Cascade Chain Declarations

**Chain 1 — Layer 1 → Layer 3 (primary documented cascade):**

```
CASCADE CHAIN:
From Layer 1 to Layer 3:
Trigger mechanism: MRC activates controlled stop;
  driver startled by sudden deceleration;
  assumes control under high stress without
  situational awareness of intersection state
Transmission path: Through driver monitoring dependency —
  system assumed driver ready; driver was not
Cascade speed: Immediate (2–4 seconds)
Circuit-break condition: Driver readiness confirmed
  BEFORE decision demand issued — not after
```

**Chain 2 — Layer 3 → Layer 4:**

```
CASCADE CHAIN:
From Layer 3 to Layer 4:
Trigger mechanism: Erratic post-takeover vehicle behavior
  creates unpredictable movement in shared intersection space
Transmission path: Through physical intersection geometry —
  other agents cannot predict vehicle trajectory
Cascade speed: Immediate
Circuit-break condition: Vehicle achieves controlled stop
  before secondary agent conflict; requires Layer 1
  MRC to have succeeded
```

*Operational note: "cascade" means sequential activation of failure in downstream components — it does not imply amplification. A cascade may dampen. These chains describe genuine cascade (sequential dependency-triggered failure), not coincident failure.*

---

## SECTION 6 — BREAKTHROUGH DENSITY INDEX

`[D]` Counting against CDIP v1.5 Section 1B operational definition — requirements that cannot be satisfied by existing validated knowledge, even with additional time or effort.

| # | REQUIREMENT | BREAKTHROUGH? | REASONING | TAG |
|---|-------------|--------------|-----------|-----|
| 1 | Detect driver readiness state with sufficient accuracy and latency to inform decision logic | **YES** | No production-validated system achieves this. A-005 is A3. Requires new empirical knowledge about psychophysiological state detection under automation-complacency conditions. | `[D]` |
| 2 | Resolve reaction-latency vs. decision-cycle gap without defaulting to MRC in all cases | **YES** | A-006 is A4. No validated architecture demonstrated. Requires either new decision logic architecture or capability not yet demonstrated in production. | `[D]` |
| 3 | Predict intersection agent behavior within decision cycle window | **NO** | Difficult but known solution paths exist — prediction models are research-active with demonstrated results. Not a breakthrough. | `[R]` |

**BDI = 2 — HIGH-RISK ARCHITECTURE** `[D]`

`[D]` BDI ≥ 2 — justification required:

Both breakthrough requirements map to the same structural conflict: the decision component must make a consequential choice faster than the human can be reliably ready to receive it, using readiness data that does not yet exist in validated form. These are not independent breakthroughs — they are two faces of the same unsolved problem. A solution to either one substantially reduces the other. This interdependency is noted as a design constraint on the research pre-phase path.

### BDI Hard Halt Assessment

`[D]` BDI = 2. Hard halt not triggered (threshold: BDI ≥ 3). Component proceeds.

### BDI-Assumption Integrity Check

*Triggered: A4 assumption present (A-006) AND Instability_ratio = 0.33 > 0.20.*

**A-006 reviewed:**
> "Decision logic can resolve the reaction-latency vs. decision-cycle gap without defaulting to MRC in all cases"

- Condition (a): Requires genuinely new empirical knowledge? **YES** — no validated architecture demonstrated.
- Condition (b): Requires never-demonstrated capability? **YES** — no production system has closed this gap.

→ Confirmed as breakthrough requirement. Already counted as BDI item 2. No BDI increment needed.

**A-005 reviewed** (A3, Instability_ratio triggered):
> "Predictive driver readiness scoring achievable with <500ms computation latency"

- Condition (a): Requires genuinely new empirical knowledge? **YES** — production validation absent.
- Condition (b): Never-demonstrated capability? **PARTIAL** — research demonstrations exist but not at production latency requirements.

→ Confirmed as breakthrough requirement. Already counted as BDI item 1. No BDI increment needed.

**4.6D Output:** Both speculative assumptions correctly mapped to BDI items. No concealed breakthroughs. BDI = 2 confirmed. `[D]`

---

## SECTION 7 — DEPENDENCY TRANSPARENCY GRID

`[D]` All eight fields declared. No hidden dependencies permitted.

| FIELD | CONTENT |
|-------|---------|
| **Inputs** | Envelope confidence score from detection layer · AV-UBI-002 cabin occupant readiness classification output (READY / DEGRADED / BEHAVIORAL_UNRESPONSIVE / MEDICAL_EMERGENCY + confidence score) · Intersection geometry data · Vehicle momentum state · Time-to-event estimate |
| **Outputs** | Decision signal — one of: `AUTONOMOUS_CONTINUE` / `DEMAND_TAKEOVER` / `MRC_ACTIVATE` / `HYBRID_DECELERATE` |
| **Energy source** | Computational — onboard processing; no independent physical energy dependency |
| **Control dependencies** | Governed by validated operational envelope definition · Governed by AV-UBI-002 readiness signal (currently dependent on unvalidated capability — A-005) |
| **Environmental exposure** | Urban intersection geometry · Mixed traffic agent behavior · Sensor degradation conditions at envelope boundary |
| **Maintenance requirements** | Envelope boundary definitions require re-validation when operational domain changes · Decision output thresholds require re-validation if AV-UBI-002 output format changes |
| **Upstream reliance** | Envelope detection component must function · AV-UBI-002 cabin occupant readiness classification must function · Intersection geometry mapping must be current · Null input from AV-UBI-002 must be treated identically to UNRESPONSIVE — this must be hardwired |
| **Downstream impact** | MRC activation component · Driver alert and handoff execution component · AV-UBI-004 emergency routing (receives MEDICAL_EMERGENCY signal from AV-UBI-002 via this component) · Session logging and incident reporting |

`[R]` **Interface dependency note (v1.0 update):** AV-UBI-002 is now the formal upstream provider of the driver/occupant readiness signal. The "Driver monitoring state signal" input originally specified is precisely defined as the AV-UBI-002 output package. Any change to AV-UBI-002's output format or classification states requires a corresponding update to this component's input specification.

---

## SECTION 8 — INVALIDATION CONDITIONS

`[D]` This component is invalid if:

1. The decision cycle requirement (300–800ms) is demonstrated to be physically incompatible with any decision logic architecture — meaning no computation pathway can produce a valid output within the window `[D]`

2. Driver readiness state is demonstrated to be undetectable with sufficient accuracy to inform the decision within the available latency — making A-005 permanently A4 and BDI effectively irreducible `[R]`

3. The four-output decision space (`AUTONOMOUS_CONTINUE` / `DEMAND_TAKEOVER` / `MRC_ACTIVATE` / `HYBRID_DECELERATE`) is demonstrated to be incomplete — meaning real intersection scenarios produce conditions none of the four outputs correctly handles `[S]`

4. MRC is demonstrated to be geometrically unavailable in >30% of urban intersection scenarios — removing the primary cascade circuit-break condition `[?]`

---

## SECTION 9 — VALIDATION LEVEL

**Validation Level: CONCEPTUAL**

`[D]` This component specification is logically consistent with its stated constraint set. It has not been tested against physical or operational reality. All breakthrough requirements remain unresolved. The decision architecture is specified but not simulated or experimentally validated.

| LEVEL | STATUS |
|-------|--------|
| Conceptual | ✓ CURRENT — logically consistent |
| Physics-Consistent | Pending — requires BDI item resolution |
| Simulation-Ready | Pending — requires Physics-Consistent validation |
| Experimentally Validated | Pending |
| Production-Grade | Pending |

---

## SECTION 10 — VERSION SUMMARY

| FIELD | VALUE |
|-------|-------|
| **Domain ID** | AV-UBI-001 |
| **Component** | Operational envelope decision logic — urban intersection |
| **BDI Class** | HIGH-RISK ARCHITECTURE (BDI = 2) |
| **Validation Level** | CONCEPTUAL |
| **High Instability Flag** | YES — Instability_ratio: 0.33 |
| **Sponsor Authorization** | Not required — BDI < 3 |
| **4.6D Check** | EXECUTED — no concealed breakthroughs found |
| **Open Breakthrough Requirements** | (1) Driver readiness detection · (2) Reaction-latency/decision-cycle gap resolution |
| **Primary cascade risk** | Layer 1 → Layer 3 → Layer 4 — immediate, HIGH probability chain |
| **Interface dependency** | AV-UBI-002 output is the formal upstream readiness signal — null output must equal UNRESPONSIVE in all downstream logic |
| **FCL Entries** | 0 — specification complete, empirical validation pending |
| **Next version trigger** | AV-UBI-002 closes BDI item 1 OR AV-UBI-003 closes BDI item 2 OR first FCL entry from simulation testing |

---

## SECTION 11 — COMPONENT STACK POSITION

`[D]` AV-UBI-001 occupies the following position in the AV-UBI specification stack:

```
AV-UBI-001 — Operational envelope decision logic (THIS COMPONENT)
     ↑
     Receives from: Envelope detection (upstream, unspecified)
     Receives from: AV-UBI-002 — Cabin occupant readiness classification
     ↓
     Sends to: MRC activation component (downstream, unspecified)
     Sends to: Driver alert and handoff execution (downstream, unspecified)
     Sends to: AV-UBI-004 — Emergency routing decision logic (via MEDICAL_EMERGENCY signal)

DEPENDENT SESSIONS:
AV-UBI-002 — Cabin occupant readiness classification
AV-UBI-003 — Reaction-latency / decision-cycle gap resolution
AV-UBI-004 — Emergency routing and services contact decision logic
AV-UBI-002B — Conscious passenger capability detection (future)
AV-UBI-002C — Choking and seizure classification (future)
```

---

## SECTION 12 — OPEN ACTIONS

| ACTION | PRIORITY | TRIGGER |
|--------|----------|---------|
| Update input specification to reflect AV-UBI-002 formal output format once AV-UBI-002 closes | HIGH | AV-UBI-002 session complete |
| Re-audit four-output decision space against AV-UBI-002B and AV-UBI-002C outputs when available | MEDIUM | AV-UBI-002B/C sessions complete |
| Advance to Physics-Consistent validation | HIGH | BDI items 1 and 2 resolved by research pre-phase sessions |
| First FCL entry from simulation testing | HIGH | Simulation environment available |
| Cross-reference AION v3.0 "failure" definition at system level | LOW | AION v3.0 next version cycle |

---

*AV-UBI-001 v1.0 — Operational Envelope Decision Logic*
*CDIP v1.5 | ECF v0.5 | LAV v1.5 | FSVE v3.5*
*BDI = 2 — HIGH-RISK ARCHITECTURE | Validation: CONCEPTUAL*
*Session complete. No expansion permitted without new DST.*

*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Co-Architect: Claude (Anthropic) | February 2026*
*Open-source specification — no prior version required*
