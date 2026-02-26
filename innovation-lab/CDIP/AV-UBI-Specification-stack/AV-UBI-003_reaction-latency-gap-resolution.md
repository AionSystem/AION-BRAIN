# AV-UBI-003
## Reaction-Latency / Decision-Cycle Gap Resolution
### CDIP v1.5 Component Specification
#### Constraint–Domain Isolation Protocol | ECF v0.5 Active | LAV v1.5 Active

---

**Domain ID:** AV-UBI-003
**Industry:** Autonomous Vehicle Systems — Urban Deployment
**Constraint Category:** Reaction-Latency / Decision-Cycle Gap Resolution
**Reference Macro-System:** Level 3-4 Autonomous Vehicle Platform *(context only — not a design target)*
**Validation Level:** CONCEPTUAL
**BDI Class:** HIGH-RISK ARCHITECTURE (BDI = 2)
**Session Priming:** AV-UBI-001 — CONSTRAINT-INPUT · FAILURE-DATA · AV-UBI-002 — CONSTRAINT-INPUT
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

`[D]` AV-UBI-003 specifies the gap resolution logic that bridges the structural conflict between human reaction latency (1.5–2.5 seconds minimum) and urban intersection decision cycle time (300–800ms available), through two sequential mechanisms: predictive escalation as the primary path and formally bounded autonomous authority extension as the failsafe path.

`[D]` This component is:
- The **gap resolution logic** between human reaction latency and decision cycle time
- A **two-path architecture** — predictive escalation primary, bounded authority extension failsafe
- Scoped to **urban mixed-traffic intersection environments**
- A **consumer of AV-UBI-002 confidence score trajectory** — not just current state
- The **authority window governor** — specifying entry conditions, duration, and exit conditions for autonomous operation past the validated envelope

`[D]` This component is NOT:
- The envelope detection component (upstream)
- The occupant readiness classification component (AV-UBI-002)
- The emergency routing component (AV-UBI-004)
- A sensor system or alert hardware specification
- A regulatory compliance framework

**One component. One version. No exceptions.**

---

## DOMAIN SESSION TOKEN

```
Domain ID:             AV-UBI-003
Industry:              Autonomous Vehicle Systems — Urban Deployment
Constraint Category:   Reaction-Latency / Decision-Cycle Gap Resolution
Reference Macro-System: Level 3-4 Autonomous Vehicle Platform
                        (context only — not a design target)
Validation Target:     Physics-Consistent Architecture
Prior Session Reference: AV-UBI-001 — CONSTRAINT-INPUT · FAILURE-DATA
                         AV-UBI-002 — CONSTRAINT-INPUT
Priming Type:          CONSTRAINT-INPUT · FAILURE-DATA
Priming Scope:         Reaction latency floor (1.5–2.5s) from AV-UBI-001
                       A-001 carried as A1.
                       Decision cycle requirement (300–800ms) from
                       AV-UBI-001 Domain Lock active as governing input.
                       AV-UBI-002 readiness classification output states
                       (READY / DEGRADED / BEHAVIORAL_UNRESPONSIVE /
                       MEDICAL_EMERGENCY) active as governing inputs.
                       This component consumes AV-UBI-002 confidence
                       score trajectory — rate of change over 2–3 second
                       window — not just current state.
                       Failure Horizon cascade chains from AV-UBI-001
                       Layers 1–3 active as harvesting seed data.
                       A-003 (driver monitoring accuracy) confirmed A2
                       in AV-UBI-002 — carried as A2.
```

---

## SECTION 1 — DOMAIN LOCK

`[D]` Governing constraints for reaction-latency / decision-cycle gap resolution via predictive escalation and bounded autonomous authority extension in urban mixed-traffic intersection environments. Design halts if any of the following are disputed before proceeding.

### Physical Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Reaction latency floor | Human minimum 1.5–2.5s from alert to control-capable under startled conditions — physically bounded, carried from AV-UBI-001 | `[D]` |
| Decision cycle ceiling | 300–800ms available for decision resolution at urban intersection — carried from AV-UBI-001 | `[D]` |
| Structural gap | Minimum gap between decision cycle ceiling and reaction latency floor: 1.0–2.2 seconds — this is the gap this component must resolve | `[R]` |
| Predictive window physics | Trajectory-based prediction of envelope boundary contact requires sufficient lead time — prediction accuracy degrades non-linearly as prediction horizon extends beyond 3–5 seconds in dynamic urban environments | `[R]` |
| Autonomous authority extension physics | Vehicle operating autonomously past its validated envelope has degraded confidence in its own decision outputs — the extension window operates in the space the envelope was designed to exclude | `[R]` |
| Attention restoration latency | Human attention restoration from distraction (texting, daydreaming) to full situational awareness requires 3–5 seconds minimum — longer than simple startled reaction latency | `[D]` |
| Alert modality physics | Visual alerts require eyes-on to register; auditory alerts register regardless of gaze direction; haptic alerts require physical contact with alert surface — modality sequencing must account for confirmed distracted state | `[D]` |

### Informational Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Prediction horizon uncertainty | The further ahead the component predicts envelope boundary contact, the higher the false alarm rate — predictive escalation initiated too early produces alert fatigue | `[R]` |
| Distraction state visibility | AV-UBI-002 confidence score trajectory reveals degrading readiness before DEGRADED threshold is crossed — this trajectory is the predictive escalation trigger, not the threshold crossing itself | `[R]` |
| Autonomous authority legitimacy | No regulatory framework currently defines the conditions under which a Level 3–4 vehicle may legally extend autonomous operation past its validated envelope — this component specifies the constraint architecture; regulatory alignment is downstream | `[?]` |
| Authority window duration tension | Autonomous authority extension window must be long enough for human to become control-capable AND short enough that the vehicle does not operate autonomously in conditions it cannot handle — these two requirements are in direct tension | `[R]` |
| Exit condition precision | The autonomous authority extension must have formally specified exit conditions — undefined exit conditions produce undefined behavior at a safety-critical moment | `[R]` |
| Alert fatigue constraint | Graduated escalation sequences that trigger frequently without genuine boundary contact degrade human trust and responsiveness to genuine alerts — false alarm rate must be governed as a primary constraint, not managed as an afterthought | `[D]` |

`[D]` Design halts if any of the above are disputed before proceeding.

---

## SECTION 2 — STATE-OF-THE-ART BASELINE ENVELOPE

`[D]` All values labeled per CDIP v1.5 Section 4.2 labeling protocol. No unlabeled performance claims permitted.

| PARAMETER | VALUE | LABEL |
|-----------|-------|-------|
| SAE Level 3 standard takeover window | 10 seconds | Industry Standard `[D]` |
| Documented actual pre-incident demand issuance | Avg. 2.3 seconds before critical event | Empirical — NTSB/academic literature `[D]` |
| Human attention restoration from distraction | 3–5 seconds minimum | Empirical — human factors literature `[D]` |
| Structural gap (reaction latency vs. decision cycle) | 1.0–2.2 seconds minimum | Empirical — derived from Domain Lock constraints `[R]` |
| Current industry predictive escalation | Not implemented in production — threshold-based only | Unknown `[?]` |
| Trajectory-based readiness monitoring | Research-stage — no production system uses confidence score trajectory as escalation trigger | Unknown `[?]` |
| Formally bounded autonomous authority extension | No production system specifies this — undefined behavior at envelope boundary is current state | Unknown `[?]` |
| Regulatory framework for authority extension | No validated regulatory framework exists | Unknown `[?]` |
| Alert modality sequencing under confirmed distraction | Industry practice: visual → auditory → haptic sequential; no formal specification under confirmed distracted state | Industry Standard — informal `[D]` |

`[R]` **Critical baseline finding:** Both primary mechanisms of this component — predictive escalation using readiness trajectory and formally bounded autonomous authority extension — are entirely absent from current production systems. The current state is: threshold crossing triggers demand; if human not ready, MRC activates. This component specifies the architecture between those two events — the gap that no current system addresses.

---

## SECTION 3 — CONSTRAINT HARVESTING

`[D]` Harvested from human factors literature, AV incident analysis, regulatory frameworks, attention research, alarm system design literature, and adjacent safety-critical domain bounded authority architectures.

### Existing Architecture Patterns

- **Threshold-based takeover demand:** Single trigger point, single alert modality sequence — no prediction, no trajectory monitoring
- **SAE Level 3 ten-second window:** Standard exists but not enforced by detection — system cannot verify human readiness within window
- **Graduated alert modality:** Visual → auditory → haptic — deployed in production but triggered at threshold, not by trajectory
- **MRC fallback:** Controlled stop if takeover not achieved — reactive terminal action, not a gap resolution mechanism
- **Bounded authority windows in adjacent domains:** Aviation autopilot disconnect protocols, medical device autonomous operation limits — bounded authority with formal entry/exit conditions exists outside automotive context `[D]`

### Known Failure Case Studies

- **Distracted driver non-response:** Multiple documented incidents where graduated alert sequence completed without human response — system had no authority to act during alert sequence; MRC activated at sequence end `[D]`
- **Startled takeover errors:** Documented cases where human took control within reaction latency window but without situational awareness — control transfer succeeded; situational awareness did not `[D]`
- **Alert fatigue incidents:** Systems with frequent false-positive alerts show measurably degraded human response to genuine alerts — false alarm frequency directly degrades genuine alarm response reliability `[D]`
- **Attention restoration underestimation:** Industry standard assumes 10-second window sufficient — human factors literature documents 3–5 second minimum for distracted state with high individual variance `[D]`

### Target State Distinguishing Requirements

`[R]` This component must distinguish between the following driver states to select the correct escalation path:

| DRIVER STATE | AV-UBI-002 SIGNAL | ESCALATION PATH |
|-------------|------------------|----------------|
| Attentive — readiness stable | READY, confidence stable | No escalation — monitor |
| Readiness degrading — not yet threshold | READY, confidence trajectory declining | Predictive escalation — STANDARD SEQUENCE |
| Confirmed distracted | DEGRADED | Predictive escalation — DISTRACTION-ADJUSTED SEQUENCE |
| Unresponsive — behavioral | BEHAVIORAL_UNRESPONSIVE | Authority extension — immediate activation |
| Medical emergency | MEDICAL_EMERGENCY | Route to AV-UBI-004 — authority extension does NOT apply |

### Unresolved Structural Blind Spots

- No system uses AV-UBI-002 confidence score trajectory as escalation trigger — all systems use threshold crossing
- No system formally specifies what the vehicle is authorized to do during the gap between alert issuance and human readiness confirmation
- No system specifies entry conditions, duration, and exit conditions for autonomous operation past envelope boundary as a formally bounded window
- Alert modality sequencing under confirmed distracted state not formally specified — current systems use same sequence regardless of occupant state
- False alarm rate not currently treated as a governing constraint — treated as a quality metric at best

### Interface Confusion Cases

- Boundary between this component's predictive escalation output and AV-UBI-001's decision logic is undefined — AV-UBI-001 currently receives a binary envelope-boundary signal; this component must provide authority window status as a continuous signal `[R]`
- Boundary between autonomous authority extension window and MRC activation — when does the extension window end and MRC begin? Not specified in any current architecture `[R]`
- Boundary between MEDICAL_EMERGENCY routing (AV-UBI-004) and authority extension — MEDICAL_EMERGENCY must immediately override authority extension; this override path not specified in any current system `[R]`

*Harvesting complete. Design phase open.*

---

## SECTION 4 — ASSUMPTION REGISTER

`[D]` All assumptions listed and classified per CDIP v1.5 Section 4.4.

| ID | CLASS | ASSUMPTION | VALIDATED | RE-VALIDATION TRIGGER |
|----|-------|------------|-----------|----------------------|
| A-001 | A1 | Human reaction latency floor 1.5–2.5s — carried from AV-UBI-001 | Empirical neuroscience | If new human factors data published |
| A-002 | A1 | Human attention restoration from distraction: 3–5 seconds minimum | Empirical — human factors literature | If new attention research contradicts |
| A-003 | A1 | Auditory alerts register regardless of gaze direction; visual alerts require eyes-on | Empirical — perceptual psychology | If new modality research contradicts |
| A-004 | A1 | Alert fatigue degrades genuine alert response measurably when false alarm rate exceeds manageable threshold | Empirical — alarm system literature across multiple safety-critical domains | If new alarm research contradicts |
| A-005 | A2 | AV-UBI-002 confidence score trajectory over 2–3 second window provides sufficient lead time to initiate predictive escalation before threshold crossing | Engineering plausible — trajectory analysis has research support in adjacent domains | If AV-UBI-002 testing shows trajectory insufficient |
| A-006 | A2 | Predictive escalation initiated 3–5 seconds before projected envelope boundary contact produces sufficient attention restoration time in majority of distracted-state scenarios | Engineering plausible — combines A-002 with trajectory lead time estimate | If human factors testing contradicts |
| A-007 | A2 | Autonomous authority extension window of 2–3 seconds provides sufficient additional time for attention restoration in majority of remaining distracted-state scenarios after predictive escalation fails | Engineering plausible — covers the 1.0–2.2 second structural gap with margin | If human factors testing contradicts |
| A-008 | A2 | Vehicle operating in bounded autonomous authority extension window can maintain safe trajectory in urban intersection environment for 2–3 seconds beyond envelope boundary in majority of scenarios | Engineering plausible — short bounded window with active deceleration is manageable | If simulation testing contradicts |
| A-009 | A3 | Trajectory-based readiness prediction achieves false alarm rate < 15% while providing adequate lead time | Research-stage — trajectory prediction in this specific automotive context unvalidated | If production-condition testing demonstrates |
| A-010 | A3 | Alert modality sequencing adjusted for confirmed distracted state — immediate simultaneous auditory + haptic rather than sequential — produces faster attention restoration than standard sequential modality | Research-stage — simultaneous adjusted sequencing not validated in automotive context | If human factors testing demonstrates |
| A-011 | A4 | Autonomous authority extension window can be formally bounded with sufficient precision to satisfy future regulatory frameworks governing Level 3–4 autonomous operation past validated envelope | Speculative — no regulatory framework exists; future framework requirements unknown | Regulatory framework publication |

**Instability ratio:** (A3 + A4) / total = 3/11 = **0.27 → HIGH INSTABILITY FLAG** `[D]`

### Assumption Decay Protocol

**Decay Rule D-1:** A-001 through A-004 carry empirical validation sources. Re-validation triggers declared.

**Decay Rule D-2:** All assumptions declare re-validation triggers in the register above.

**Decay Rule D-3:** A-002 and A-003 carried from prior sessions as A2-under-review — confirmed A1 in this session based on human factors and perceptual psychology literature. All A2 assumptions from this session are A2-under-review at next session open.

---

## SECTION 5 — GAP RESOLUTION ARCHITECTURE

`[R]` AV-UBI-003 resolves the structural gap through two sequential mechanisms. Primary path: predictive escalation. Failsafe path: bounded autonomous authority extension. The two paths are not alternatives — the failsafe activates only when the primary path fails.

### 5.1 Primary Path — Predictive Escalation

```
PREDICTIVE ESCALATION PROTOCOL:

TRIGGER CONDITIONS (all must be true):
  1. AV-UBI-002 confidence score trajectory showing
     rate-of-change toward DEGRADED over 2–3 second window
  2. Projected envelope boundary contact within
     3–5 second prediction horizon
  3. AV-UBI-002 state is READY or DEGRADED
     (BEHAVIORAL_UNRESPONSIVE routes directly to
     authority extension; MEDICAL_EMERGENCY routes
     to AV-UBI-004)

FALSE ALARM RATE GATE:
  Session false alarm rate accumulator checked before
  trigger activation.
  If false alarm rate approaching threshold:
    Escalation sensitivity reduced.
    Threshold gap logged.
    Alert: alert fatigue risk accumulating.

ESCALATION SEQUENCE:

  PATH A — AV-UBI-002 state: READY
  (readiness degrading but not yet threshold)
  Standard sequential modality:
    T+0.0s  Visual alert — envelope boundary approaching
    T+1.0s  Auditory alert — prepare for handoff
    T+2.0s  Haptic alert — take control now
    T+3.0s  Readiness confirmation window opens

  PATH B — AV-UBI-002 state: DEGRADED
  (distraction confirmed)
  Distraction-adjusted simultaneous modality:
    T+0.0s  Auditory + Haptic simultaneous —
            maximum attention restoration priority
            (bypasses visual — eyes-off confirmed)
    T+1.5s  Visual added — situational context
            delivered as readiness returns
    T+3.0s  Readiness confirmation window opens

SUCCESS CONDITION:
  AV-UBI-002 returns READY within escalation window
  Human confirmed control-capable before boundary contact
  → Standard handoff proceeds
  → Authority extension NOT activated
  → False alarm accumulator: no increment
    (genuine alert, successful response)

FAILURE CONDITION:
  AV-UBI-002 does not return READY within escalation window
  OR boundary contact occurs before readiness confirmed
  → Autonomous authority extension activates
  → False alarm accumulator: no increment
    (genuine alert, escalation to failsafe)

FALSE ALARM CONDITION:
  Predictive escalation triggered; boundary contact
  does not occur within prediction horizon
  → Escalation cancelled
  → False alarm accumulator: +1
  → If accumulator exceeds session threshold:
      Adaptive sensitivity reduction applied
      Gap between current and adjusted threshold logged
```

### 5.2 Failsafe Path — Bounded Autonomous Authority Extension

```
AUTONOMOUS AUTHORITY EXTENSION PROTOCOL:

ENTRY CONDITIONS (all must be true):
  1. Predictive escalation sequence completed
     without readiness confirmation
     OR AV-UBI-002 state is BEHAVIORAL_UNRESPONSIVE
     at envelope boundary contact
  2. Envelope boundary contact imminent or occurring
  3. AV-UBI-002 state is DEGRADED or
     BEHAVIORAL_UNRESPONSIVE
     (NOT MEDICAL_EMERGENCY — routes to AV-UBI-004)
  4. MRC not immediately required by
     intersection geometry
     (geometry check from AV-UBI-001 context)

AUTHORITY WINDOW PARAMETERS:
  Duration: 2–3 seconds from entry — HARD LIMIT
  Maximum: 3 seconds — non-negotiable
  Vehicle behavior during window:
    ✓ Maintain current trajectory
    ✓ Active deceleration toward safe speed
    ✓ Continue escalation alerts at maximum intensity
    ✓ Monitor AV-UBI-002 for readiness recovery
    ✗ DO NOT execute maneuvers requiring
      envelope-level confidence
    ✗ DO NOT accelerate
    ✗ DO NOT change lanes
    ✗ DO NOT enter intersection if not already in it

OVERRIDE CONDITIONS (immediate window exit):
  MEDICAL_EMERGENCY signal from AV-UBI-002 at any
  point during window:
    → Immediate authority window exit
    → Route to AV-UBI-004
    → MRC activated in parallel as safety floor

EXIT CONDITIONS (first condition met exits window):

  EXIT A — FULL SUCCESS:
    AV-UBI-002 returns READY during window
    → Assisted handoff
    → Deceleration maintained during transfer
    → Human assumes control at reduced velocity
    → Authority window closes
    → Normal monitored operation resumes

  EXIT B — PARTIAL SUCCESS:
    AV-UBI-002 returns DEGRADED (not READY) during window
    → Assisted handoff with extended deceleration support
    → 1–2 second vehicle-assisted deceleration phase
    → Human assumes control at reduced velocity
      with active deceleration support maintained
    → Authority window closes
    → Heightened monitoring — AV-UBI-002 watching
      for further degradation

  EXIT C — FAILURE:
    Window duration expires (3 seconds) without
    readiness confirmation of any level
    → Authority window expiry signal to AV-UBI-001
    → MRC activation
    → Authority window closes — terminal fallback
    → Full incident log generated

AV-UBI-001 SIGNAL REQUIREMENT:
  Authority window status must be delivered to
  AV-UBI-001 as a CONTINUOUS signal — not binary.
  Signal states:
    AUTHORITY_INACTIVE
    AUTHORITY_PREDICTIVE_ACTIVE (escalation running)
    AUTHORITY_WINDOW_ACTIVE (extension running)
      + duration_remaining: [seconds]
      + exit_condition_projected: [A/B/C/UNKNOWN]
    AUTHORITY_WINDOW_EXPIRED (MRC signal)
  Expiry is a formal positive signal — not an
  absence of signal. AV-UBI-001 must not treat
  signal loss as equivalent to AUTHORITY_INACTIVE.
```

---

## SECTION 6 — FAILURE HORIZON MAP

`[D]` Failure mapped across four layers per CDIP v1.5 Section 4.5.

*Operational note: "failure" means the condition in which this component does not perform its specified function under its stated operating conditions — not a malfunction.*

*Operational note: "containment mechanism" means an active process — not a passive structural feature — that limits the spread of failure once triggered.*

| LAYER | TYPE | TRIGGER | OBSERVABLE INDICATOR | CONTAINMENT MECHANISM | CASCADE PROBABILITY |
|-------|------|---------|---------------------|-----------------------|-------------------|
| Layer 1 | Immediate catastrophic | Predictive escalation fails AND autonomous authority extension window expires before human readiness confirmed | No control-capable human at window expiry; vehicle beyond envelope with no valid authority | MRC activation — controlled stop; terminal fallback | HIGH |
| Layer 2 | Progressive degradation | False alarm rate exceeds alert fatigue threshold — predictive escalation triggers too frequently without genuine boundary contact | Measurable degradation in human response latency to genuine alerts over session | Adaptive threshold adjustment — escalation sensitivity reduced; trade-off: some genuine escalations may be delayed | MEDIUM |
| Layer 3 | Control system collapse | Human achieves control within authority extension window but without situational awareness | Erratic post-takeover behavior during authority window | Authority window assisted deceleration phase — vehicle continues decelerating during human orientation; EXIT B protocol | HIGH |
| Layer 4 | Cascading subsystem propagation | Layer 1 MRC in intersection during authority window expiry | Multi-agent conflict — other vehicles cannot anticipate sudden deceleration | Unknown — dependent on intersection state at MRC activation moment | UNKNOWN |

### Cascade Chain Declarations

**Chain 1 — Layer 2 → Layer 1 (alert fatigue enabling catastrophic failure):**

```
CASCADE CHAIN:
From Layer 2 to Layer 1:
Trigger mechanism: Elevated false alarm rate degrades
  human response to genuine escalation alert;
  human fails to respond within predictive window;
  autonomous authority extension activates;
  human still does not respond; window expires
Transmission path: Through human attention dependency —
  alert fatigue accumulates across session;
  single genuine alert inherits degraded response
  from accumulated prior false alarms
Cascade speed: Session-accumulated → immediate at
  genuine alert moment
Circuit-break condition: False alarm rate accumulator
  must be a governing control input — if rate exceeds
  threshold, escalation sensitivity adjusts BEFORE
  fatigue accumulates to critical level;
  adaptive threshold is the circuit-break
```

**Chain 2 — Layer 1 → AV-UBI-001 Layer 1:**

```
CASCADE CHAIN:
From AV-UBI-003 Layer 1 to AV-UBI-001 Layer 1:
Trigger mechanism: Authority window expires;
  no control-capable human;
  AUTHORITY_WINDOW_EXPIRED signal delivered to
  AV-UBI-001; MRC activation follows
Transmission path: Through authority status signal —
  AV-UBI-001 depends on this signal to know
  when MRC is required; signal must be positive
  not an absence
Cascade speed: Immediate at window expiry
Circuit-break condition: MRC must be physically
  achievable at moment of window expiry —
  intersection geometry from AV-UBI-001 governs
  whether MRC succeeds
```

**Chain 3 — Layer 3 → Layer 4:**

```
CASCADE CHAIN:
From Layer 3 to Layer 4:
Trigger mechanism: Human achieves nominal control
  within authority window without situational
  awareness; erratic vehicle behavior in
  intersection creates unpredictable movement
  in shared space
Transmission path: Through physical intersection
  geometry — other agents cannot predict vehicle
  trajectory during erratic post-takeover period
Cascade speed: Immediate
Circuit-break condition: EXIT B protocol —
  assisted deceleration phase reduces velocity
  DURING human orientation period, before
  full control transfer; lower velocity at
  transfer reduces multi-agent conflict risk
```

---

## SECTION 7 — BREAKTHROUGH DENSITY INDEX

`[D]` Counting against CDIP v1.5 Section 1B operational definition — requirements that cannot be satisfied by existing validated knowledge, even with additional time or effort.

| # | REQUIREMENT | BREAKTHROUGH? | REASONING | TAG |
|---|-------------|--------------|-----------|-----|
| 1 | Trajectory-based readiness prediction achieving false alarm rate < 15% with sufficient lead time — using AV-UBI-002 confidence score rate-of-change as primary signal | **YES** | A-009 is A3. No production system uses confidence score trajectory as predictive escalation trigger. Requires new empirical validation of trajectory prediction accuracy in this specific context. | `[D]` |
| 2 | Formally bounded autonomous authority extension window with specified entry, duration, and exit conditions satisfying safety requirements during envelope boundary contact | **NO** | Difficult architecture problem but solution path is known — bounded authority windows exist in aviation and medical device domains. Requires adaptation and validation, not genuinely new empirical knowledge. | `[R]` |
| 3 | Alert modality sequencing adjusted dynamically based on AV-UBI-002 confirmed distracted state — simultaneous auditory + haptic achieving faster attention restoration than standard sequential modality | **YES** | A-010 is A3. Adjusted simultaneous modality under confirmed distracted state not validated in automotive context. Requires new empirical knowledge about attention restoration under this specific protocol. | `[D]` |
| 4 | Regulatory framework alignment for autonomous authority extension past validated envelope | **NO** | Not a knowledge gap — a regulatory gap. Knowledge to specify it exists; regulatory permission does not yet exist. Governance problem, not a breakthrough requirement. | `[R]` |

**BDI = 2 — HIGH-RISK ARCHITECTURE** `[D]`

`[D]` BDI ≥ 2 — justification required:

BDI item 1 (trajectory prediction) and BDI item 2 (adjusted modality sequencing) are independent breakthrough requirements — each requires new empirical knowledge in a distinct domain (prediction accuracy vs. attention restoration under adjusted protocol). They are sequentially dependent in architecture: adjusted modality sequencing activates only when trajectory prediction has identified a distracted state. Resolution of item 1 creates the condition under which item 2 can be validated. Research pre-phase must address trajectory prediction first.

### BDI Hard Halt Assessment

`[D]` BDI = 2. Hard halt not triggered. Component proceeds.

### BDI-Assumption Integrity Check

*Triggered: A4 assumption present (A-011) AND Instability_ratio = 0.27 > 0.20.*

**A-011 reviewed:**
> "Autonomous authority extension window can be formally bounded with sufficient precision to satisfy future regulatory frameworks"

- Condition (a): Requires genuinely new empirical knowledge? **NO** — the knowledge to specify bounded authority windows exists in adjacent domains.
- Condition (b): Never-demonstrated capability? **NO** — bounded authority windows exist in aviation and medical device contexts.

→ A-011 correctly classified A4 — speculative about regulatory outcomes, not technical capability. Does not meet breakthrough threshold. BDI unchanged.

**A-009 reviewed (A3):**
→ Confirmed as BDI item 1. Already counted. No increment.

**A-010 reviewed (A3):**
→ Confirmed as BDI item 2. Already counted. No increment.

**4.6D Output:** All speculative assumptions reviewed. No concealed breakthroughs. BDI = 2 confirmed. `[D]`

---

## SECTION 8 — DEPENDENCY TRANSPARENCY GRID

`[D]` All eight fields declared. No hidden dependencies permitted.

| FIELD | CONTENT |
|-------|---------|
| **Inputs** | AV-UBI-002 confidence score — current value · AV-UBI-002 confidence score trajectory — rate of change over 2–3 second window · AV-UBI-002 state classification — READY / DEGRADED / BEHAVIORAL_UNRESPONSIVE / MEDICAL_EMERGENCY · Envelope boundary proximity signal from detection layer · Intersection geometry and vehicle momentum state from AV-UBI-001 context · Session-level false alarm rate accumulator |
| **Outputs** | ESCALATION_STATE: INACTIVE / PREDICTIVE_ACTIVE / AUTHORITY_WINDOW_ACTIVE / AUTHORITY_WINDOW_EXPIRED · AUTHORITY_WINDOW_STATUS: entry conditions met / duration remaining / projected exit condition (A/B/C/UNKNOWN) · HANDOFF_READINESS: CONFIRMED / PARTIAL / FAILED · Alert modality command: STANDARD_SEQUENCE / DISTRACTION_ADJUSTED_SEQUENCE · Deceleration assist command: ACTIVE / INACTIVE · AV-UBI-001 authority status signal: continuous — AUTHORITY_INACTIVE / AUTHORITY_PREDICTIVE_ACTIVE / AUTHORITY_WINDOW_ACTIVE / AUTHORITY_WINDOW_EXPIRED |
| **Energy source** | Computational — onboard processing; alert modality outputs require audio system, haptic actuators, and display subsystems |
| **Control dependencies** | Governed by AV-UBI-002 confidence score trajectory — primary escalation trigger · Governed by session false alarm rate accumulator — adaptive threshold control · Governed by intersection geometry from AV-UBI-001 — authority window entry gated by MRC feasibility · Governed by 3-second hard limit on authority window duration — non-negotiable ceiling |
| **Environmental exposure** | Urban intersection geometry during authority window · Variable human distraction states and individual attention restoration variance · Alert modality effectiveness under variable cabin noise conditions · Session-accumulated alert fatigue state — degrades across session, not per-event |
| **Maintenance requirements** | False alarm rate threshold requires re-calibration per operational domain and vehicle platform · Alert modality intensity levels require calibration per vehicle audio and haptic hardware · Authority window duration limit requires re-validation if urban operational speed envelope changes · Trajectory prediction model requires re-validation if AV-UBI-002 output format or update frequency changes |
| **Upstream reliance** | AV-UBI-002 must provide confidence score trajectory — single-point classification insufficient for this component · AV-UBI-002 must update at sufficient frequency for trajectory computation (minimum 4Hz recommended) · Envelope detection component must provide boundary proximity signal with sufficient prediction horizon · Intersection geometry data must be current |
| **Downstream impact** | AV-UBI-001 receives authority status signal continuously — must integrate signal into decision output logic; expiry is positive signal not absence · Driver alert subsystems receive escalation modality commands · Vehicle deceleration control receives assist command during authority window and EXIT B phase · AV-UBI-004 receives immediate routing priority override if MEDICAL_EMERGENCY signal overrides authority window at any point |

---

## SECTION 9 — INVALIDATION CONDITIONS

> "This component is invalid if:"

1. AV-UBI-002 confidence score trajectory is demonstrated to be insufficient as a predictive escalation trigger — meaning the rate of change provides no statistically meaningful lead time advantage over threshold-crossing alone `[D]`

2. Trajectory-based prediction is demonstrated to produce false alarm rates ≥ 15% regardless of threshold calibration — meaning alert fatigue accumulation is unavoidable and structurally undermines the escalation architecture `[R]`

3. Adjusted simultaneous modality sequencing (auditory + haptic simultaneous) is demonstrated to produce no statistically significant improvement in attention restoration time over standard sequential modality under confirmed distracted state — meaning the distraction-adjusted path provides no measurable benefit `[R]`

4. Autonomous authority extension window of 2–3 seconds is demonstrated to be insufficient for attention restoration in the majority of documented distracted-state scenarios — meaning the window does not bridge the gap it was designed to close `[R]`

5. Vehicle operating in bounded authority extension window in urban intersection environment is demonstrated to produce unacceptable risk elevation compared to immediate MRC activation — meaning the extension window itself creates greater safety risk than the failure it prevents `[S]`

6. The three-exit-condition architecture (EXIT A / EXIT B / EXIT C) is demonstrated to be incomplete — meaning real scenarios produce states none of the three exits correctly handles, producing undefined behavior at the exit moment `[S]`

7. AV-UBI-002 confidence score trajectory is demonstrated to be unavailable at the update frequency required for trajectory computation — meaning the upstream dependency cannot be satisfied by AV-UBI-002 as specified `[R]`

---

## SECTION 10 — VALIDATION LEVEL

**Validation Level: CONCEPTUAL**

`[D]` This component specification is logically consistent with its stated constraint set and internally consistent with AV-UBI-001 and AV-UBI-002 interface requirements. It has not been tested against physical or operational reality. Two breakthrough requirements remain unresolved. The gap resolution architecture is specified but not simulated or experimentally validated.

| LEVEL | STATUS |
|-------|--------|
| Conceptual | ✓ CURRENT — logically consistent |
| Physics-Consistent | Pending — requires BDI item 1 (trajectory prediction validation) resolution first |
| Simulation-Ready | Pending — requires Physics-Consistent validation |
| Experimentally Validated | Pending |
| Production-Grade | Pending |

---

## SECTION 11 — VERSION SUMMARY

| FIELD | VALUE |
|-------|-------|
| **Domain ID** | AV-UBI-003 |
| **Component** | Reaction-latency / decision-cycle gap resolution |
| **BDI Class** | HIGH-RISK ARCHITECTURE (BDI = 2) |
| **Validation Level** | CONCEPTUAL |
| **High Instability Flag** | YES — Instability_ratio: 0.27 |
| **Sponsor Authorization** | Not required — BDI < 3 |
| **4.6D Check** | EXECUTED — no concealed breakthroughs found |
| **Open Breakthrough Requirements** | (1) Trajectory-based readiness prediction at < 15% false alarm rate · (2) Adjusted simultaneous modality sequencing producing measurably faster attention restoration under confirmed distraction |
| **Novel architectural contributions** | (1) Confidence score trajectory as predictive escalation trigger — first formal specification in AV context · (2) Formally bounded autonomous authority extension with three exit conditions — first formal specification · (3) Distraction-state-adjusted simultaneous alert modality — first formal specification · (4) False alarm rate as governing constraint with adaptive sensitivity reduction — first formal treatment |
| **Primary cascade risk** | Layer 2 → Layer 1 — silent session-accumulated alert fatigue enabling catastrophic failure at genuine alert moment |
| **Critical interface requirement** | AV-UBI-001 must receive authority window status as continuous positive signal — AUTHORITY_WINDOW_EXPIRED is a positive signal, not an absence; signal loss must not be treated as AUTHORITY_INACTIVE |
| **AV-UBI-001 update required** | AV-UBI-001 v1.1 must add authority window status as formal input — currently specified as binary envelope-boundary signal only |
| **FCL Entries** | 0 — specification complete, empirical validation pending |
| **Next version trigger** | Research pre-phase closing BDI item 1 (trajectory prediction) OR first FCL entry from simulation testing |

---

## SECTION 12 — COMPONENT STACK POSITION

`[D]` AV-UBI-003 occupies the following position in the AV-UBI specification stack:

```
AV-UBI-001 — Operational envelope decision logic
     ↑
     Receives from: AV-UBI-002 (readiness classification)
     Receives from: AV-UBI-003 (authority window status — continuous)

AV-UBI-002 — Cabin occupant readiness classification
     ↓
     Sends confidence score + trajectory to: AV-UBI-003

AV-UBI-003 — Reaction-latency gap resolution (THIS COMPONENT)
     ↑
     Receives from: AV-UBI-002 confidence score trajectory
     Receives from: Envelope detection (boundary proximity)
     Receives from: AV-UBI-001 context (intersection geometry)
     ↓
     Sends authority window status to: AV-UBI-001 (continuous)
     Sends modality commands to: Alert subsystems
     Sends deceleration assist to: Vehicle control
     Sends MEDICAL_EMERGENCY override to: AV-UBI-004

AV-UBI-004 — Emergency routing and services contact (NEXT SESSION)
     Receives MEDICAL_EMERGENCY override from: AV-UBI-003
```

---

## SECTION 13 — OPEN ACTIONS

| ACTION | PRIORITY | TRIGGER |
|--------|----------|---------|
| Update AV-UBI-001 to add authority window status as formal continuous input — v1.1 | CRITICAL | Immediate — interface dependency confirmed this session |
| Confirm AV-UBI-002 update frequency sufficient for trajectory computation (minimum 4Hz) | HIGH | AV-UBI-002 next version |
| Design research pre-phase session for BDI item 1 (trajectory prediction false alarm validation) | HIGH | Next available session |
| Design research pre-phase session for BDI item 2 (simultaneous modality attention restoration) | HIGH | After BDI item 1 session |
| Alert fatigue threshold calibration study — what false alarm rate triggers measurable degradation in this specific context | MEDIUM | Research pre-phase |
| Regulatory monitoring — autonomous authority extension framework development | LOW | Ongoing — A-011 re-audit trigger |
| First FCL entry from simulation testing of authority window protocol | HIGH | Simulation environment available |

---

*AV-UBI-003 v1.0 — Reaction-Latency / Decision-Cycle Gap Resolution*
*CDIP v1.5 | ECF v0.5 | LAV v1.5 | FSVE v3.5*
*BDI = 2 — HIGH-RISK ARCHITECTURE | Validation: CONCEPTUAL*
*Session complete. No expansion permitted without new DST.*

*Novel contributions: Confidence score trajectory as predictive trigger · Formally bounded autonomous authority extension (three exit conditions) · Distraction-adjusted simultaneous modality sequencing · False alarm rate as governing constraint with adaptive sensitivity reduction.*

*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Co-Architect: Claude (Anthropic) | February 2026*
*Open-source specification — no prior version required*
