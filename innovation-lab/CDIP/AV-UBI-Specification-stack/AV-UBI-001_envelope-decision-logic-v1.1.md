# AV-UBI-001
## Operational Envelope Decision Logic
### CDIP v1.5 Component Specification — v1.1 UPDATE
#### Constraint–Domain Isolation Protocol | ECF v0.5 Active | LAV v1.5 Active

---

**Domain ID:** AV-UBI-001
**Industry:** Autonomous Vehicle Systems — Urban Deployment
**Constraint Category:** Operational Envelope Decision Authority
**Reference Macro-System:** Level 3-4 Autonomous Vehicle Platform *(context only — not a design target)*
**Validation Level:** CONCEPTUAL
**BDI Class:** HIGH-RISK ARCHITECTURE (BDI = 2)
**Session Priming:** NONE — first session in this domain
**Version:** 1.1
**Previous Version:** 1.0 — February 2026
**Version Date:** February 2026
**Version Trigger:** AV-UBI-003 finalized — authority window status formalized as continuous signal; binary envelope model structurally incompatible with gradient authority state; interface contract update required
**Architect:** Sheldon K. Salmon — AI Reliability Architect
**Co-Architect:** Claude (Anthropic)
**Framework:** CDIP v1.5 | FSVE v3.5 | ECF v0.5 | LAV v1.5
**Epistemic Standard:** All claims tagged `[D]` / `[R]` / `[S]` / `[?]`

---

> *"A constraint is not a limit imposed from outside. It is the shape of what is actually true — made visible before the design begins."*

---

## VERSION DELTA — v1.0 → v1.1

`[D]` The following structural changes were made in response to AV-UBI-003 finalization. No changes were made to AV-UBI-003.

| CHANGE | SECTION | REASON |
|--------|---------|--------|
| Envelope model redefined from binary (IN / OUT) to multi-state gradient ontology | Section 1, Section 5 | Binary model structurally incompatible with authority window as a recognized operational state — authority window is neither IN nor OUT under binary model, producing undefined behavior |
| Authority window added as formal envelope sub-state | Section 1, Section 5 | Authority window must be a named state in the envelope model, not an exception beyond it — exception logic produces semantic contradiction with CDIP isolation discipline |
| AV-UBI-003 authority status signal added as formal continuous input | Section 7 | AV-UBI-003 produces four authority states; AV-UBI-001 must consume all four as positive signals |
| AUTHORITY_WINDOW_EXPIRED hardwired as positive signal | Section 5, Section 7 | Signal loss and expiry must produce identical downstream behavior — MRC activation; absence of signal must not be treated as AUTHORITY_INACTIVE |
| Decision output logic revised to reflect gradient state | Section 5 | Four decision outputs now map to gradient envelope states rather than binary boundary trigger |
| Transition logic added — explicit state-to-state rules | Section 5 | Gradient model requires declared transition conditions; implicit transitions are undefined behavior |
| New assumptions A-007 through A-009 added | Section 4 | Gradient envelope model and authority window sub-state introduce new assumptions not present in v1.0 |
| Failure Horizon updated — Layer 1 and Layer 2 revised | Section 6 | Gradient model changes failure trigger conditions |
| Open Actions updated | Section 12 | Prior open actions resolved or carried; new actions from v1.1 changes added |

**What did not change:**
- Domain Lock physical and informational constraints — unchanged
- BDI items 1 and 2 — unchanged; no new breakthrough requirements introduced
- Validation Level — CONCEPTUAL maintained; no architectural contradiction discovered that would require downgrade
- MRC logic and safety hierarchy — preserved in full
- AV-UBI-002 interface — unchanged
- Component definition and scope boundaries — unchanged

---

## COMPONENT DEFINITION

`[D]` AV-UBI-001 specifies the decision logic governing autonomous vehicle behavior across the operational envelope gradient — from nominal operation through predictive escalation through authority extension through terminal fallback — in urban mixed-traffic intersection environments.

`[D]` This component is:
- The **decision logic** governing behavior across the full envelope gradient
- Scoped to **urban mixed-traffic intersection environments**
- The **consumer of AV-UBI-003 authority window status** as a continuous governing input
- The **activator of MRC** when authority window expires or is not available

`[D]` This component is NOT:
- The envelope detection component (upstream)
- The occupant readiness classification component (AV-UBI-002)
- The gap resolution component (AV-UBI-003)
- The takeover execution component (downstream)
- The emergency routing component (AV-UBI-004)

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
Version:               1.1 — structural evolution from v1.0
Version Trigger:       AV-UBI-003 finalized
```

---

## SECTION 1 — DOMAIN LOCK

`[D]` Governing constraints for autonomous vehicle decision logic across the operational envelope gradient in urban mixed-traffic intersection environments. Design halts if any of the following are disputed before proceeding.

### v1.1 Envelope Model Declaration

`[D]` **The envelope is not a binary boundary.** It is a gradient with formally declared states. Treating it as binary produces a structural gap: the vehicle's operational authority is undefined during the interval between threshold crossing and human readiness confirmation. AV-UBI-003 closes that gap by specifying behavior during that interval. AV-UBI-001 v1.1 integrates that specification by recognizing the authority window as a named envelope sub-state rather than an exception beyond the envelope.

`[R]` **Gradient ontology rationale:** A binary IN / OUT model requires that any operation outside the envelope is categorically unauthorized. The authority window is operation outside the envelope that is conditionally authorized — for a bounded duration, under declared conditions, with declared exit logic. That conditional authorization cannot be expressed in a binary model without creating exception logic. Exception logic outside the envelope is undefined behavior under CDIP isolation discipline. The gradient model eliminates the exception by making the authority window a first-class envelope state.

### Physical Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Human reaction latency | Minimum 1.5–2.5 seconds from alert to control-capable under startled conditions — physically bounded | `[D]` |
| Decision cycle time | Urban intersection events require decision resolution within 300–800ms — determined by vehicle speed and intersection geometry | `[D]` |
| Structural gap | Minimum 1.0–2.2 seconds between decision cycle ceiling and reaction latency floor — the gap AV-UBI-003 bridges | `[R]` |
| Sensory degradation at boundary | Sensor confidence degrades non-linearly at envelope boundary — system knows less precisely at the moment it needs to know most | `[R]` |
| Vehicle momentum | Braking distance at urban speeds (25–45mph) ranges 40–120ft — physical law, non-negotiable | `[D]` |
| Authority extension physics | Vehicle operating in authority window has degraded decision confidence — operating in the space the envelope was designed to exclude | `[R]` |

### Informational Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Takeover demand latency | Time between system issuing takeover demand and human achieving situational awareness is structurally longer than decision cycle time in documented incidents | `[D]` |
| Driver monitoring state | Human cognitive engagement degrades under automation — cannot be assumed ready; AV-UBI-002 provides formal readiness classification | `[D]` |
| Envelope detection lag | System detects envelope boundary after it has begun crossing it — detection is retrospective by architecture | `[R]` |
| Situational context gap | Human receiving control has not been processing the environment — they inherit a situation already in progress | `[D]` |
| Authority signal continuity | AV-UBI-003 authority status must be consumed as a continuous positive signal — loss of signal must not be treated as AUTHORITY_INACTIVE; it must trigger MRC | `[R]` |

`[D]` Design halts if any of the above are disputed before proceeding.

---

## SECTION 2 — STATE-OF-THE-ART BASELINE ENVELOPE

*Unchanged from v1.0. Carried forward.*

| PARAMETER | VALUE | LABEL |
|-----------|-------|-------|
| Minimum human takeover readiness time (alert → control-capable) | 1.5–2.5 seconds | Empirical `[D]` |
| SAE Level 3 takeover request window (industry standard) | 10 seconds | Industry Standard `[D]` |
| Documented gap between standard and reality in incidents | System issued demand avg. 2.3 seconds before critical event | Empirical — NTSB/academic literature `[D]` |
| Urban intersection decision cycle requirement | 300–800ms | Empirical `[D]` |
| Current industry failure mode frequency | Late takeover demand — most cited in public AV incident literature | Empirical `[D]` |
| Existing decision architecture | Threshold-based envelope detection triggering takeover demand | Industry Standard `[D]` |
| Known ceiling | No validated architecture resolves the reaction-latency vs. decision-cycle gap at envelope boundary | Empirical `[D]` |

`[R]` **Critical baseline finding (carried from v1.0):** The gap between the 10-second SAE standard takeover window and the 2.3-second actual pre-incident demand issuance is not a calibration problem — it is a structural conflict between two constraint categories that the current threshold-based architecture does not resolve. AV-UBI-003 addresses this conflict. AV-UBI-001 v1.1 integrates that resolution into the decision logic architecture.

---

## SECTION 3 — CONSTRAINT HARVESTING

*Unchanged from v1.0. Carried forward. Interface confusion cases updated.*

### Existing Architecture Patterns

- Threshold-based envelope detection: system monitors confidence scores against fixed boundaries; when boundary crossed, takeover demand issued
- Graduated alert systems: visual → auditory → haptic escalation sequence before demand
- Minimal Risk Condition (MRC) fallback: if no takeover, vehicle attempts controlled stop

### Known Failure Case Studies

- **Uber ATG Tempe 2018:** Demand issued 1.3 seconds before impact — within human reaction latency floor `[D]`
- **Tesla Autopilot intersection incidents:** No demand issued at envelope boundary — opposite failure mode `[D]`
- **Academic simulation studies:** Drivers in automation-complacent state require avg. 3–5 seconds for full situational awareness after takeover demand `[D]`

### Unresolved Structural Blind Spots

- No validated method for assessing driver readiness state before issuing demand — addressed by AV-UBI-002
- No architecture for decision behavior during the gap between alert issuance and human readiness — addressed by AV-UBI-003
- Envelope boundary detection is reactive — decision logic inherits a situation already in progress

### Interface Confusion Cases — v1.1 Update

- `[R]` v1.0: Ambiguity at boundary between autonomous decision authority and human confirmation — not formally specified. **v1.1 resolution:** Gradient envelope model formally declares this boundary across five states. Each state has a declared decision authority level.
- `[R]` v1.1 NEW: AV-UBI-001 must not treat absence of AV-UBI-003 signal as AUTHORITY_INACTIVE. Signal loss equals AUTHORITY_WINDOW_EXPIRED equals MRC activation. This must be hardwired — no conditional logic on signal absence.

*Harvesting complete. Design phase open.*

---

## SECTION 4 — ASSUMPTION REGISTER

`[D]` v1.0 assumptions A-001 through A-006 carried forward. v1.1 adds A-007 through A-009 for gradient envelope model and authority window sub-state.

| ID | CLASS | VERSION | ASSUMPTION | VALIDATED | RE-VALIDATION TRIGGER |
|----|-------|---------|------------|-----------|----------------------|
| A-001 | A1 | v1.0 | Human minimum reaction latency floor: 1.5s under startled conditions | Empirical neuroscience literature | If new human factors data published |
| A-002 | A1 | v1.0 | Urban intersection decision cycle: 300–800ms at 25–45mph | Physics — speed/geometry | If operational speed envelope changes |
| A-003 | A2 | v1.0 | Driver monitoring systems detect gross attention state with >85% accuracy | Industry — not independently confirmed across all platforms | If platform-specific monitoring data available |
| A-004 | A2 | v1.0 | MRC is physically achievable within intersection geometry in >70% of urban scenarios | Engineering plausible — geometry-dependent | If intersection dataset available |
| A-005 | A3 | v1.0 | Predictive driver readiness scoring achievable with <500ms computation latency | Research-stage — no production-validated system | If validated system demonstrated |
| A-006 | A4 | v1.0 | Decision logic can resolve the reaction-latency vs. decision-cycle gap without defaulting to MRC in all cases | Speculative — AV-UBI-003 provides the architecture; empirical validation pending | First FCL entry from simulation |
| A-007 | A2 | v1.1 NEW | The five-state gradient envelope model is exhaustive — every operational condition of this vehicle in this domain maps to exactly one of the five declared states with no overlap and no gaps | Engineering plausible — states were derived from documented operational conditions | If simulation or operational testing reveals unmapped condition |
| A-008 | A2 | v1.1 NEW | State transitions are deterministic given declared trigger conditions — no scenario produces simultaneous eligibility for two transitions | Engineering plausible — trigger conditions were designed to be mutually exclusive | If testing reveals ambiguous transition condition |
| A-009 | A2 | v1.1 NEW | AV-UBI-003 authority status signal is available at sufficient update frequency for this component to consume it as a continuous governing input rather than a periodic check | Engineering plausible — dependent on AV-UBI-003 implementation | If AV-UBI-003 update frequency testing contradicts |

**Instability ratio:** (A3 + A4) / total = 2/9 = **0.22 → HIGH INSTABILITY FLAG MAINTAINED** `[D]`

### Assumption Decay Protocol

**Decay Rule D-1:** A-001 and A-002 carry empirical validation sources. Re-validation triggers declared.

**Decay Rule D-2:** All assumptions declare re-validation triggers in register above.

**Decay Rule D-3:** A-007, A-008, A-009 are v1.1 new — all carry as A2-under-review at next session open until confirmed by simulation or operational testing.

---

## SECTION 5 — GRADIENT ENVELOPE MODEL AND DECISION LOGIC

### 5.1 Envelope State Definitions

`[D]` The operational envelope is formally declared as a five-state gradient. Each state has a declared decision authority level, a defined entry condition, and defined transition triggers. No state is an exception to the model — all five are first-class envelope states.

```
STATE 1 — NOMINAL
  Definition: Vehicle operating within validated envelope.
              All sensors within confidence bounds.
              AV-UBI-002 state: READY.
              AV-UBI-003 state: AUTHORITY_INACTIVE.
  Decision authority: FULL AUTONOMOUS
  Decision output: AUTONOMOUS_CONTINUE
  Transition triggers:
    → STATE 2: AV-UBI-002 confidence trajectory declining
               AND projected boundary contact within
               3–5 second horizon
    → STATE 4: AV-UBI-002 state = MEDICAL_EMERGENCY
               (bypass STATE 2 and STATE 3)

STATE 2 — PREDICTIVE ESCALATION
  Definition: Envelope boundary contact projected.
              AV-UBI-003 escalation sequence active.
              AV-UBI-003 state: AUTHORITY_PREDICTIVE_ACTIVE.
              AV-UBI-002 state: READY or DEGRADED.
  Decision authority: AUTONOMOUS WITH ACTIVE HANDOFF PREPARATION
  Decision output: HYBRID_DECELERATE
                   (maintain trajectory, begin deceleration,
                   alert sequence running)
  Transition triggers:
    → STATE 1: AV-UBI-002 returns READY and boundary
               contact does not occur — escalation resolved
    → STATE 3: AV-UBI-003 escalation sequence completes
               without readiness confirmation AND boundary
               contact occurs or is imminent
    → STATE 4: AV-UBI-002 state = MEDICAL_EMERGENCY
               at any point during STATE 2

STATE 3 — AUTHORITY WINDOW
  Definition: Bounded autonomous operation past validated
              envelope boundary. Formally authorized for
              maximum 3 seconds under declared conditions.
              AV-UBI-003 state: AUTHORITY_WINDOW_ACTIVE.
              AV-UBI-002 state: DEGRADED or
              BEHAVIORAL_UNRESPONSIVE.
  Decision authority: CONDITIONAL AUTONOMOUS — BOUNDED
                      (deceleration only; no maneuvers;
                      no acceleration; no lane change)
  Decision output: HYBRID_DECELERATE
                   (active deceleration, maximum alerts,
                   authority window duration tracked)
  Transition triggers:
    → EXIT A (STATE 1 analog): AV-UBI-002 returns READY
      during window → DEMAND_TAKEOVER with assisted handoff
      → return to NOMINAL monitoring
    → EXIT B (STATE 2 analog): AV-UBI-002 returns DEGRADED
      during window → DEMAND_TAKEOVER with extended
      deceleration assist → heightened monitoring
    → EXIT C (STATE 5): AUTHORITY_WINDOW_EXPIRED signal
      received from AV-UBI-003 → MRC_ACTIVATE
    → STATE 4: AV-UBI-002 = MEDICAL_EMERGENCY at any
      point during STATE 3 → immediate override to
      STATE 4; MRC activated in parallel as safety floor
  Conditional authority constraints:
    — Maximum duration: 3 seconds hard limit
    — Vehicle must be decelerating throughout
    — No intersection entry if not already in it
    — Signal loss from AV-UBI-003 treated as
      AUTHORITY_WINDOW_EXPIRED — transition to STATE 5

STATE 4 — MEDICAL EMERGENCY OVERRIDE
  Definition: AV-UBI-002 state = MEDICAL_EMERGENCY.
              All other decision logic suspended.
              AV-UBI-004 emergency routing activated.
  Decision authority: EMERGENCY AUTONOMOUS — ROUTED
  Decision output: Route to AV-UBI-004
                   MRC activated in parallel as safety floor
  Transition triggers:
    → No return transition from STATE 4 within same session
      Medical emergency state does not self-resolve
      within the decision logic of this component

STATE 5 — TERMINAL FALLBACK
  Definition: Authority window expired without readiness.
              OR MRC required by intersection geometry
              before authority window could activate.
              AV-UBI-003 state: AUTHORITY_WINDOW_EXPIRED
              (positive signal — not signal absence).
  Decision authority: NONE — MRC ONLY
  Decision output: MRC_ACTIVATE
  Transition triggers:
    → No return transition from STATE 5 within same
      decision cycle. Session termination follows MRC.
      New session may return to STATE 1 if system
      re-validates operational conditions.
```

### 5.2 Transition Logic — Explicit Rules

`[D]` All state transitions are governed by the following rules. No implicit transitions permitted.

| FROM | TO | TRIGGER | AUTHORITY DURING TRANSITION |
|------|----|---------|---------------------------|
| STATE 1 | STATE 2 | AV-UBI-002 confidence trajectory declining + boundary contact projected 3–5s | AUTONOMOUS — transition is instantaneous |
| STATE 1 | STATE 4 | AV-UBI-002 = MEDICAL_EMERGENCY | EMERGENCY AUTONOMOUS — instantaneous |
| STATE 2 | STATE 1 | AV-UBI-002 returns READY + boundary contact does not occur | AUTONOMOUS — escalation cancelled |
| STATE 2 | STATE 3 | Escalation sequence completes without readiness + boundary imminent | CONDITIONAL AUTONOMOUS — transition instantaneous |
| STATE 2 | STATE 4 | AV-UBI-002 = MEDICAL_EMERGENCY | EMERGENCY AUTONOMOUS — instantaneous |
| STATE 3 | STATE 1* | EXIT A — AV-UBI-002 returns READY during window | DEMAND_TAKEOVER with assisted handoff — not full STATE 1 until human confirmed |
| STATE 3 | STATE 2* | EXIT B — AV-UBI-002 returns DEGRADED during window | DEMAND_TAKEOVER with deceleration assist — heightened monitoring |
| STATE 3 | STATE 5 | EXIT C — AUTHORITY_WINDOW_EXPIRED signal OR AV-UBI-003 signal loss | MRC_ACTIVATE — instantaneous |
| STATE 3 | STATE 4 | AV-UBI-002 = MEDICAL_EMERGENCY during window | EMERGENCY AUTONOMOUS + MRC parallel safety floor |
| STATE 4 | — | No return transition within session | — |
| STATE 5 | — | No return transition within decision cycle | — |

*EXIT A and EXIT B return to supervised operational states rather than full STATE 1 — human has control but monitoring continues at elevated sensitivity.

### 5.3 Decision Output Mapping

`[D]` Decision outputs map to gradient envelope states. Binary threshold triggering is eliminated.

| OUTPUT | ACTIVATED IN | CONDITIONS |
|--------|-------------|------------|
| `AUTONOMOUS_CONTINUE` | STATE 1 | Nominal operation — AV-UBI-002 READY, AV-UBI-003 INACTIVE, envelope confidence within bounds |
| `HYBRID_DECELERATE` | STATE 2, STATE 3 | Escalation active or authority window active — deceleration begins, alerts running, trajectory maintained |
| `DEMAND_TAKEOVER` | STATE 3 EXIT A, EXIT B | AV-UBI-002 readiness recovery during authority window — assisted handoff with deceleration maintained |
| `MRC_ACTIVATE` | STATE 5 | Authority window expired OR geometry requires immediate MRC OR AV-UBI-003 signal loss |
| Route to AV-UBI-004 | STATE 4 | AV-UBI-002 MEDICAL_EMERGENCY at any state |

### 5.4 Signal Loss Protocol

`[D]` AV-UBI-003 signal loss is not AUTHORITY_INACTIVE. Signal loss protocol:

```
SIGNAL LOSS HANDLING:

IF AV-UBI-003 signal lost during STATE 1 or STATE 2:
  → Treat as AUTHORITY_WINDOW_EXPIRED
  → Transition to STATE 5
  → MRC_ACTIVATE
  → Log signal loss event

IF AV-UBI-003 signal lost during STATE 3:
  → Treat as AUTHORITY_WINDOW_EXPIRED (EXIT C)
  → Transition to STATE 5
  → MRC_ACTIVATE
  → Log signal loss event

Rationale: A component whose authority status is unknown
  cannot be granted conditional autonomous authority.
  Conservative interpretation is mandatory at safety
  boundary. Signal loss equals worst-case assumption.
```

---

## SECTION 6 — FAILURE HORIZON MAP

`[D]` Failure horizon updated to reflect gradient envelope model. Layers 1 and 2 revised. Layers 3 and 4 carried from v1.0 with minor clarification.

| LAYER | TYPE | TRIGGER | OBSERVABLE INDICATOR | CONTAINMENT MECHANISM | CASCADE PROBABILITY |
|-------|------|---------|---------------------|-----------------------|-------------------|
| Layer 1 | Immediate catastrophic | STATE 5 reached — authority window expired or MRC required before window available — no control-capable human | No vehicle action producing safe outcome within decision window | MRC activation — controlled stop if geometrically possible | HIGH |
| Layer 2 | Progressive degradation | Repeated STATE 2 → STATE 3 cycles without EXIT A resolution — escalation succeeding but human not restoring READY state | Increasing authority window activations per session; AV-UBI-002 sustained DEGRADED classification | Session termination — vehicle exits autonomous mode; AV-UBI-003 alert fatigue accumulator flagged | MEDIUM |
| Layer 3 | Control system collapse | EXIT A or EXIT B achieved — human achieves nominal control during authority window but without situational awareness | Erratic post-takeover vehicle behavior during EXIT handoff | Deceleration assist maintained through EXIT B; velocity reduced at control transfer; AV-UBI-002 monitoring continues at elevated sensitivity | HIGH |
| Layer 4 | Cascading subsystem propagation | STATE 5 MRC in active intersection environment | Secondary incident involvement — multi-agent conflict | Unknown — dependent on intersection state at MRC activation | UNKNOWN |

### Cascade Chain Declarations — v1.1 Update

**Chain 1 — Layer 1 (revised from v1.0):**

```
CASCADE CHAIN:
From STATE 2 failure → STATE 3 → STATE 5:
Trigger mechanism: Predictive escalation fails to restore
  human readiness; authority window activates; window
  expires without readiness recovery; MRC activates
Transmission path: Through sequential state degradation —
  each state is a containment attempt; STATE 5 is the
  condition where all containment has failed
Cascade speed: 5–8 seconds total (escalation 3–5s +
  authority window 2–3s)
Circuit-break condition: AV-UBI-002 readiness recovery
  at any point before STATE 5 — EXIT A or EXIT B
  breaks the chain
```

**Chain 2 — Layer 3 → Layer 4 (carried from v1.0, clarified):**

```
CASCADE CHAIN:
From Layer 3 to Layer 4:
Trigger mechanism: EXIT A or EXIT B handoff produces
  erratic post-takeover behavior in shared intersection
Transmission path: Through physical intersection geometry
Cascade speed: Immediate
Circuit-break condition: Deceleration assist during EXIT
  reduces velocity before transfer; lower velocity at
  transfer reduces multi-agent conflict probability
```

---

## SECTION 7 — DEPENDENCY TRANSPARENCY GRID

`[D]` v1.1 update: AV-UBI-003 authority status added as formal continuous input. All eight fields updated.

| FIELD | CONTENT |
|-------|---------|
| **Inputs** | Envelope confidence score from detection layer · AV-UBI-002 cabin occupant readiness classification output — READY / DEGRADED / BEHAVIORAL_UNRESPONSIVE / MEDICAL_EMERGENCY + confidence score + confidence score trajectory · AV-UBI-003 authority status signal — AUTHORITY_INACTIVE / AUTHORITY_PREDICTIVE_ACTIVE / AUTHORITY_WINDOW_ACTIVE (+ duration_remaining) / AUTHORITY_WINDOW_EXPIRED — consumed as continuous positive signal; loss treated as AUTHORITY_WINDOW_EXPIRED · Intersection geometry data · Vehicle momentum state · Time-to-event estimate |
| **Outputs** | Decision signal — one of: `AUTONOMOUS_CONTINUE` / `HYBRID_DECELERATE` / `DEMAND_TAKEOVER` / `MRC_ACTIVATE` · Route-to-AV-UBI-004 signal on MEDICAL_EMERGENCY · Current envelope state: STATE 1–5 (continuous, for session logging) |
| **Energy source** | Computational — onboard processing; no independent physical energy dependency |
| **Control dependencies** | Governed by validated operational envelope definition · Governed by AV-UBI-002 readiness signal and confidence trajectory · Governed by AV-UBI-003 authority status signal — continuous, four-state · Governed by gradient envelope state machine — five states with declared transition logic · Governed by signal loss protocol — loss equals AUTHORITY_WINDOW_EXPIRED |
| **Environmental exposure** | Urban intersection geometry · Mixed traffic agent behavior · Sensor degradation conditions at envelope boundary · AV-UBI-003 signal continuity — degraded communication infrastructure produces signal loss events |
| **Maintenance requirements** | Envelope boundary definitions require re-validation when operational domain changes · Decision output thresholds require re-validation if AV-UBI-002 or AV-UBI-003 output format changes · Gradient state transition triggers require re-validation if AV-UBI-003 authority window duration changes · Signal loss protocol requires re-validation if communication architecture changes |
| **Upstream reliance** | Envelope detection component must function · AV-UBI-002 must function and provide confidence score trajectory — single-point classification insufficient · AV-UBI-003 must function and provide continuous authority status signal — signal loss triggers MRC · Intersection geometry mapping must be current · Null input from AV-UBI-002 treated identically to UNRESPONSIVE — hardwired · AV-UBI-003 signal loss treated identically to AUTHORITY_WINDOW_EXPIRED — hardwired |
| **Downstream impact** | MRC activation component receives MRC_ACTIVATE signal · Driver alert and handoff execution receives DEMAND_TAKEOVER signal · AV-UBI-004 emergency routing receives MEDICAL_EMERGENCY override · Deceleration control receives HYBRID_DECELERATE command · Session logging receives current envelope state continuously |

---

## SECTION 8 — INVALIDATION CONDITIONS

`[D]` v1.0 conditions 1–4 carried forward. v1.1 adds conditions 5–7 for gradient model.

> "This component is invalid if:"

1. The decision cycle requirement (300–800ms) is demonstrated to be physically incompatible with any decision logic architecture — meaning no computation pathway can produce a valid output within the window `[D]`

2. Driver readiness state is demonstrated to be undetectable with sufficient accuracy to inform the decision within the available latency — making A-005 permanently A4 and BDI effectively irreducible `[R]`

3. The five-state decision output space (`AUTONOMOUS_CONTINUE` / `HYBRID_DECELERATE` / `DEMAND_TAKEOVER` / `MRC_ACTIVATE` / Route-to-AV-UBI-004) is demonstrated to be incomplete — meaning real intersection scenarios produce conditions none of the five outputs correctly handles `[S]`

4. MRC is demonstrated to be geometrically unavailable in >30% of urban intersection scenarios — removing the primary cascade circuit-break condition `[?]`

5. The five-state gradient envelope model is demonstrated to be non-exhaustive — meaning a real operational condition exists that does not map to exactly one of the five declared states `[R]`

6. State transitions are demonstrated to be non-deterministic — meaning real scenarios produce simultaneous eligibility for two or more transitions with no declared resolution rule `[R]`

7. AV-UBI-003 authority status signal cannot be delivered at sufficient update frequency to function as a continuous governing input — meaning the authority window cannot be governed by this component in real-time `[R]`

---

## SECTION 9 — VALIDATION LEVEL

**Validation Level: CONCEPTUAL — MAINTAINED**

`[D]` No architectural contradiction was discovered during v1.1 update that requires downgrade. The gradient envelope model is logically consistent with the v1.0 constraint set. The authority window as a named sub-state resolves the structural gap that binary model created rather than introducing new contradiction. Validation level is unchanged.

| LEVEL | STATUS |
|-------|--------|
| Conceptual | ✓ CURRENT — logically consistent |
| Physics-Consistent | Pending — requires BDI item resolution |
| Simulation-Ready | Pending — gradient state model requires simulation validation specifically |
| Experimentally Validated | Pending |
| Production-Grade | Pending |

`[R]` **v1.1 simulation note:** The gradient envelope model introduces a state machine that requires simulation validation of transition logic before Physics-Consistent can be claimed. Specifically: A-007 (exhaustiveness) and A-008 (determinism) must be confirmed in simulation. These are v1.1 additions and were not required in v1.0.

---

## SECTION 10 — BDI — UNCHANGED FROM v1.0

`[D]` No new breakthrough requirements introduced by v1.1 changes. BDI = 2 maintained.

| # | REQUIREMENT | BREAKTHROUGH? | STATUS |
|---|-------------|--------------|--------|
| 1 | Detect occupant readiness state with sufficient accuracy and latency to inform decision logic | **YES** | Open — AV-UBI-002 addresses sensor architecture; research pre-phase required |
| 2 | Resolve reaction-latency vs. decision-cycle gap without defaulting to MRC in all cases | **YES** | Open — AV-UBI-003 provides conceptual architecture; empirical validation pending |

**BDI = 2 — HIGH-RISK ARCHITECTURE** `[D]`

`[R]` **v1.1 BDI note:** The gradient envelope model and authority window sub-state do not introduce new breakthrough requirements. The architecture for bounded state machines with declared transition logic is well-established. The breakthrough requirements remain the two empirical gaps identified in v1.0.

---

## SECTION 11 — COMPONENT STACK POSITION — v1.1 UPDATE

```
AV-UBI-001 — Operational envelope decision logic (THIS COMPONENT v1.1)
     ↑
     Receives from: Envelope detection (upstream, unspecified)
     Receives from: AV-UBI-002 — cabin occupant readiness
                    classification + confidence score trajectory
     Receives from: AV-UBI-003 — authority status signal (continuous)
     ↓
     Sends to: MRC activation component (downstream)
     Sends to: Driver alert and handoff execution (downstream)
     Sends to: AV-UBI-004 — emergency routing (MEDICAL_EMERGENCY)
     Sends to: Deceleration control (HYBRID_DECELERATE command)
     Sends to: Session logging (envelope state continuous)

UPSTREAM COMPONENTS:
AV-UBI-002 — Cabin occupant readiness classification
  Provides: Readiness classification + confidence score + trajectory
AV-UBI-003 — Reaction-latency gap resolution
  Provides: Authority status signal (continuous, four states)

DOWNSTREAM SESSIONS:
AV-UBI-004 — Emergency routing and services contact
  (receives MEDICAL_EMERGENCY override from STATE 4)
AV-UBI-002B — Conscious passenger capability (future)
AV-UBI-002C — Choking/seizure classification (future)
```

---

## SECTION 12 — VERSION SUMMARY — v1.1

| FIELD | VALUE |
|-------|-------|
| **Domain ID** | AV-UBI-001 |
| **Version** | 1.1 |
| **Version trigger** | AV-UBI-003 finalized — binary envelope model structurally incompatible |
| **Component** | Operational envelope decision logic — urban intersection |
| **BDI Class** | HIGH-RISK ARCHITECTURE (BDI = 2) — unchanged |
| **Validation Level** | CONCEPTUAL — maintained; no contradiction found |
| **High Instability Flag** | YES — Instability_ratio: 0.22 |
| **Sponsor Authorization** | Not required — BDI < 3 |
| **4.6D Check** | Carried from v1.0 — no new A4 assumptions introduced |
| **Open Breakthrough Requirements** | (1) Occupant readiness detection · (2) Reaction-latency/decision-cycle gap resolution — unchanged from v1.0 |
| **Primary cascade risk** | STATE 2 → STATE 3 → STATE 5 — sequential containment failure chain; 5–8 second cascade window |
| **New assumptions** | A-007 (gradient exhaustiveness) · A-008 (transition determinism) · A-009 (AV-UBI-003 signal frequency) — all A2-under-review |
| **Critical interface requirements** | AV-UBI-003 signal loss = AUTHORITY_WINDOW_EXPIRED — hardwired · AV-UBI-002 null output = UNRESPONSIVE — hardwired |
| **Simulation requirement added** | Gradient state model requires A-007 and A-008 confirmation before Physics-Consistent validation |
| **FCL Entries** | 0 — specification complete, empirical validation pending |
| **Next version trigger** | AV-UBI-004 integration OR BDI item resolution OR A-007/A-008 simulation results |

---

## SECTION 13 — OPEN ACTIONS — v1.1

| ACTION | PRIORITY | STATUS | TRIGGER |
|--------|----------|--------|---------|
| Confirm AV-UBI-002 delivers confidence score trajectory at ≥4Hz — required for AV-UBI-003 trajectory computation | CRITICAL | OPEN | AV-UBI-002 next version |
| Confirm AV-UBI-003 signal update frequency sufficient for continuous consumption by this component | CRITICAL | OPEN | AV-UBI-003 implementation |
| Validate gradient state model exhaustiveness (A-007) in simulation | HIGH | OPEN | Simulation environment available |
| Validate state transition determinism (A-008) in simulation | HIGH | OPEN | Simulation environment available |
| Integrate AV-UBI-004 emergency routing — STATE 4 interface contract | HIGH | OPEN | AV-UBI-004 session complete |
| Advance to Physics-Consistent validation | HIGH | OPEN | BDI items 1 and 2 resolved |
| AION v3.0 cross-reference — system-level failure definition mirror note | LOW | OPEN | AION v3.0 next version cycle |

---

*AV-UBI-001 v1.1 — Operational Envelope Decision Logic*
*CDIP v1.5 | ECF v0.5 | LAV v1.5 | FSVE v3.5*
*BDI = 2 — HIGH-RISK ARCHITECTURE | Validation: CONCEPTUAL*
*Version trigger: AV-UBI-003 finalized — gradient envelope model adopted*
*Session complete. No expansion permitted without new DST.*

*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Co-Architect: Claude (Anthropic) | February 2026*
*Open-source specification — no prior version required*
