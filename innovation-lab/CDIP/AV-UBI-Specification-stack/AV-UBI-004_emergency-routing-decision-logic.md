# AV-UBI-004
## Vehicle-Side Emergency Contact and Routing Execution
### CDIP v1.5 Component Specification
#### Constraint–Domain Isolation Protocol | ECF v0.5 Active | LAV v1.5 Active

---

**Domain ID:** AV-UBI-004
**Industry:** Autonomous Vehicle Systems — Urban Deployment
**Constraint Category:** Vehicle-Side Emergency Contact and Routing Execution
**Reference Macro-System:** Level 3-4 Autonomous Vehicle Platform *(context only — not a design target)*
**Validation Level:** CONCEPTUAL
**BDI Class:** FOCUSED RESEARCH (BDI = 1) — lowest in stack
**Session Priming:** AV-UBI-001 v1.1 — CONSTRAINT-INPUT · STATE 4 · AV-UBI-002 — CONSTRAINT-INPUT · MEDICAL_EMERGENCY · AV-UBI-003 — CONSTRAINT-INPUT · authority window override
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

`[D]` AV-UBI-004 specifies the vehicle-side logic that, upon receiving a MEDICAL_EMERGENCY trigger, initiates 911 contact, transmits a structured emergency data package, receives routing address and responder ETA from AV-UBI-005 dispatcher system, executes autonomous navigation to the received address governed by estimated arrival time, and displays relevant information to any conscious occupants — all while operating concurrently with MRC deceleration as a safety floor.

`[D]` This component is:
- The **vehicle-side emergency interface** — contact, transmit, receive, route, display
- Activated by **MEDICAL_EMERGENCY trigger** from AV-UBI-001 STATE 4 OR AV-UBI-003 authority window override — both paths produce identical behavior
- Governed by **estimated arrival time** — not raw distance
- Operating **concurrently with MRC deceleration** — not instead of it
- The **upstream provider** to AV-UBI-005 dispatcher system via emergency data package

`[D]` This component is NOT:
- The occupant readiness classification component (AV-UBI-002)
- The gap resolution component (AV-UBI-003)
- The AI-assisted 911 dispatcher system (AV-UBI-005 — future session)
- The envelope decision logic (AV-UBI-001)
- A sensor system, medical diagnosis system, or facility triage system

**One component. One version. No exceptions.**

---

## DOMAIN SESSION TOKEN

```
Domain ID:             AV-UBI-004
Industry:              Autonomous Vehicle Systems — Urban Deployment
Constraint Category:   Vehicle-Side Emergency Contact and Routing Execution
Reference Macro-System: Level 3-4 Autonomous Vehicle Platform
                        (context only — not a design target)
Validation Target:     Physics-Consistent Architecture
Prior Session Reference: AV-UBI-001 v1.1 — CONSTRAINT-INPUT · STATE 4
                         AV-UBI-002 — CONSTRAINT-INPUT ·
                           MEDICAL_EMERGENCY signal + occupant state
                         AV-UBI-003 — CONSTRAINT-INPUT ·
                           authority window override path
Priming Type:          CONSTRAINT-INPUT · FAILURE-DATA
Priming Scope:         MEDICAL_EMERGENCY trigger arrives from two paths:
                         PATH A: AV-UBI-001 STATE 4 (via AV-UBI-002)
                         PATH B: AV-UBI-003 authority window override
                       Both paths produce identical component behavior.
                       No path-conditional logic permitted.
                       MRC activated as safety floor on STATE 4 entry.
                       This component operates concurrently with MRC.
                       Routing governed by estimated arrival time —
                       not raw distance. Confirmed design decision.
                       AV-UBI-005 (AI-assisted 911 dispatcher) is
                       downstream interface — dispatcher logic out of scope.
```

---

## SECTION 1 — DOMAIN LOCK

`[D]` Governing constraints for vehicle-side emergency contact and routing execution triggered by MEDICAL_EMERGENCY classification in urban autonomous vehicle deployment. Design halts if any of the following are disputed before proceeding.

### Physical Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| 911 contact precedes routing | Emergency contact must be initiated and data package transmitted before vehicle routing begins — contact precedes routing, not parallel | `[R]` |
| Data transmission physics | Structured emergency data package transmission over cellular infrastructure subject to coverage gaps, congestion, and latency — not guaranteed instantaneous | `[D]` |
| Routing execution physics | Vehicle navigation to received address requires current map data, real-time traffic state, and physical routing availability — not all urban scenarios permit optimal routing | `[D]` |
| MRC parallel operation | MRC is activated as safety floor on STATE 4 entry — this component operates concurrently with MRC deceleration; not assumes free navigation | `[R]` |
| ETA as snapshot | ETA received from AV-UBI-005 is computed at dispatch moment — traffic state changes during transit; ETA is governing input not a guarantee | `[R]` |
| Unattended autonomous operation | Driver is confirmed MEDICAL_EMERGENCY — vehicle operates autonomously for duration of routing; no human authority available | `[D]` |
| Conscious passenger signal | AV-UBI-002 CONSCIOUS_OCCUPANT_PRESENT signal governs whether gross alert display is appropriate — component must not assume conscious passenger absent | `[R]` |

### Informational Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| 911 infrastructure variability | 911 infrastructure varies by jurisdiction — not all jurisdictions have AV-compatible structured data reception; component must handle non-AV-capable 911 response | `[D]` |
| Emergency type uncertainty | AV-UBI-002 MEDICAL_EMERGENCY classification includes CARDIAC / RESPIRATORY / SEIZURE / UNKNOWN — UNKNOWN is most common initial classification; component must route under uncertainty | `[R]` |
| Routing address dependency | Vehicle cannot route until address received from AV-UBI-005 — mandatory wait interval between 911 contact and routing execution | `[R]` |
| Wait interval safety | During wait for routing address vehicle is decelerating under MRC — wait interval must have declared timeout with fallback behavior | `[R]` |
| Responder ETA display | Conscious occupants receive incoming responder information — display must be accurate enough to be useful and simple enough to be processed under stress | `[R]` |
| Data package integrity | Emergency data transmitted to 911 must reflect AV-UBI-002 classification at moment of MEDICAL_EMERGENCY trigger — not a prior cached state | `[D]` |

`[D]` Design halts if any of the above are disputed before proceeding.

---

## SECTION 2 — STATE-OF-THE-ART BASELINE ENVELOPE

`[D]` All values labeled per CDIP v1.5 Section 4.2 labeling protocol. No unlabeled performance claims permitted.

| PARAMETER | VALUE | LABEL |
|-----------|-------|-------|
| Current AV emergency contact capability | eCall — automatic call on airbag deployment; audio connection only; no structured data package | Industry Standard `[D]` |
| Structured AV-to-911 data transmission | No production system — research and pilot programs only | Unknown `[?]` |
| AV autonomous routing to medical facility | No production system | Unknown `[?]` |
| 911 AI-assisted dispatch integration | Pilot programs in select jurisdictions — not standardized | Unknown `[?]` |
| Estimated arrival time as routing governor | Standard in consumer navigation — not applied to emergency routing in AV context | Industry Standard — adjacent `[D]` |
| Conscious occupant alert display during emergency routing | No production system | Unknown `[?]` |
| Concurrent MRC and autonomous routing | No production system specifies this — concurrent operation unspecified | Unknown `[?]` |
| Emergency data package format standard | No AV-specific standard — HL7 for medical, CAD for dispatch; neither designed for AV integration | Unknown `[?]` |

`[R]` **Critical baseline finding:** eCall is the only production emergency contact system in current AV deployment — reactive post-airbag, audio-only, no structured data. Every capability this component specifies operates beyond the current production frontier. This component is the first formal specification of vehicle-side autonomous emergency contact, routing, and occupant display architecture.

---

## SECTION 3 — CONSTRAINT HARVESTING

`[D]` Harvested from emergency services literature, AV safety research, telecommunications standards, medical dispatch protocols, and eCall system documentation.

### Existing Architecture Patterns

- **eCall (EU mandated):** Airbag-triggered automatic 911 call; transmits GPS location and basic vehicle data; audio channel for dispatcher; no medical state data; no autonomous routing `[D]`
- **OnStar and equivalents:** Manual or crash-triggered call; dispatcher-mediated; no structured medical data package; no autonomous routing `[D]`
- **NG911 (Next Generation 911):** IP-based 911 infrastructure supporting structured data transmission — deployed in select US jurisdictions; not universal `[D]`
- **CAD (Computer-Aided Dispatch):** Standard dispatch system; accepts structured incident data; AV data package integration not standardized `[D]`
- **Navigation ETA routing:** Real-time ETA computation standard in consumer navigation — not applied to AV emergency routing `[D]`

### Known Failure Case Studies

- **eCall coverage gaps:** Cellular infrastructure gaps produce failed eCall transmissions in rural and some urban environments — documented `[D]`
- **Audio-only 911 limitations:** Dispatcher cannot assess medical state from audio when occupant is unresponsive — critical information gap between incident and response `[D]`
- **Dispatch address errors:** GPS coordinates transmitted to 911 subject to urban canyon GPS degradation — derived address may be incorrect `[D]`
- **NG911 jurisdiction gaps:** Structured data transmission not universal — component must handle legacy 911 infrastructure response without degrading to silence `[D]`

### Unresolved Structural Blind Spots

- No standard AV emergency data package format exists — component must specify its own format and handle non-compliant 911 response
- No protocol for AV-to-facility direct communication — all current routing goes through dispatcher intermediary
- Wait interval timeout for routing address receipt has no declared protocol in any current system
- Concurrent MRC deceleration and autonomous destination routing not specified in any current AV architecture

### Interface Confusion Cases

- `[R]` Boundary between this component and AV-UBI-005 — this component transmits and receives; AV-UBI-005 processes and dispatches. Interface contract is the emergency data package format and the routing response format. Neither can be independently validated — co-specification required.
- `[R]` Boundary between MRC deceleration and destination routing — concurrent operation must not produce conflicting control signals to vehicle navigation system. Priority rule: MRC always wins. Routing waits during MRC conflict resolution.

*Harvesting complete. Design phase open.*

---

## SECTION 4 — ASSUMPTION REGISTER

`[D]` All assumptions listed and classified per CDIP v1.5 Section 4.4.

| ID | CLASS | ASSUMPTION | VALIDATED | RE-VALIDATION TRIGGER |
|----|-------|------------|-----------|----------------------|
| A-001 | A1 | MEDICAL_EMERGENCY trigger from both paths (AV-UBI-001 STATE 4 and AV-UBI-003 override) produces identical component behavior — no path-conditional logic | Architectural — derived from CDIP isolation discipline | If trigger path testing reveals behavioral divergence |
| A-002 | A1 | MRC deceleration and autonomous destination routing can operate concurrently without conflicting vehicle control signals when MRC priority rule is applied | Architectural — priority arbitration is established engineering pattern | If vehicle control system testing reveals irresolvable conflict |
| A-003 | A1 | GPS location data is sufficiently accurate for emergency address derivation in urban environments under non-adverse conditions | Empirical — documented GPS urban accuracy | If urban canyon degradation testing contradicts |
| A-004 | A2 | 911 contact initiation and emergency data package transmission can be completed within 3–5 seconds of MEDICAL_EMERGENCY trigger over cellular infrastructure | Engineering plausible — cellular data transmission at this volume within documented capability | If transmission latency testing contradicts |
| A-005 | A2 | Routing address and ETA can be received from AV-UBI-005 within 10–15 seconds of 911 contact — within MRC deceleration window in most urban scenarios | Engineering plausible — dispatch systems designed for speed | If AV-UBI-005 response latency testing contradicts |
| A-006 | A2 | Wait interval timeout of 20 seconds is sufficient to cover AV-UBI-005 response in majority of scenarios before fallback required | Engineering plausible — combines A-004 and A-005 with margin | If end-to-end latency testing contradicts |
| A-007 | A2 | Conscious occupant alert display rendered with sufficient simplicity to be processed under stress in under 3 seconds of viewing | Engineering plausible — HCI literature supports simplified stress-condition display | If human factors testing contradicts |
| A-008 | A3 | NG911 or AV-compatible 911 infrastructure available at sufficient coverage to receive structured data package in target urban deployment areas | Research-stage — NG911 deployment active but incomplete; urban coverage not universal | If deployment area infrastructure audit contradicts |
| A-009 | A3 | Emergency data package format specified in this component is interpretable by AV-UBI-005 dispatcher system without translation layer introducing unacceptable latency | Research-stage — no standard exists; interoperability requires co-specification with AV-UBI-005 | If AV-UBI-005 session produces incompatible format |
| A-010 | A4 | Autonomous vehicle routing to received address during concurrent MRC deceleration without human authority is legally permissible in target deployment jurisdictions at time of production deployment | Speculative — no jurisdiction has formally authorized this specific operation | Regulatory framework publication |

**Instability ratio:** (A3 + A4) / total = 3/10 = **0.30 → HIGH INSTABILITY FLAG** `[D]`

### Assumption Decay Protocol

**Decay Rule D-1:** A-001 through A-003 carry validation sources or architectural derivations. Re-validation triggers declared.

**Decay Rule D-2:** All assumptions declare re-validation triggers in register above.

**Decay Rule D-3:** A-004 through A-007 are A2 — all carry as A2-under-review at next session open until confirmed by integration testing. A-008 and A-009 are A3 — require empirical testing to advance.

---

## SECTION 5 — EMERGENCY DATA PACKAGE SPECIFICATION

`[R]` The emergency data package is the primary interface artifact between this component and AV-UBI-005. It must be compiled from current sensor state at moment of MEDICAL_EMERGENCY trigger — not cached state. It must be transmitted within 3–5 seconds of trigger.

```
EMERGENCY DATA PACKAGE — AV-UBI-004 v1.0:

TRANSMISSION TRIGGER:
  MEDICAL_EMERGENCY signal received from either path
  Package compiled from current state — not cached
  Target transmission window: 3–5 seconds from trigger

PACKAGE CONTENTS:

  VEHICLE BLOCK:
    vehicle_id:              [unique AV platform identifier]
    timestamp_trigger:       [UTC timestamp of MEDICAL_EMERGENCY trigger]
    timestamp_transmission:  [UTC timestamp of package transmission]
    location_coordinates:    [GPS lat/lng at trigger moment]
    location_confidence:     [GPS accuracy estimate in meters]
    address_derived:         [street address derived from coordinates]
    heading:                 [degrees 0–360]
    speed_at_trigger:        [mph]
    speed_trajectory:        [DECELERATING / STABLE / UNKNOWN]
    mrc_status:              [ACTIVE / STANDBY]

  OCCUPANT STATE BLOCK (from AV-UBI-002 at trigger moment):
    driver_state:            [MEDICAL_EMERGENCY]
    emergency_type:          [CARDIAC / RESPIRATORY / SEIZURE / UNKNOWN]
    emergency_confidence:    [AV-UBI-002 confidence score 0.00–1.00]
    time_since_onset:        [seconds from initial MEDICAL_EMERGENCY
                              detection to 911 contact]
    occupant_count_total:    [integer]
    conscious_occupants:     [integer — gross detection from AV-UBI-002]
    conscious_occupant_capable: [UNKNOWN — detail in AV-UBI-002B]

  VEHICLE CAPABILITY BLOCK:
    autonomous_routing:      [CAPABLE / DEGRADED / UNAVAILABLE]
    estimated_autonomous_range: [miles — battery/fuel estimate]
    navigation_system_status: [OPERATIONAL / DEGRADED]

  REQUEST BLOCK:
    routing_address_requested:        TRUE
    routing_by:                       ESTIMATED_ARRIVAL_TIME
    eta_to_facility_requested:        TRUE
    responder_eta_to_vehicle_requested: TRUE
    facility_type_preferred:          HOSPITAL
    continuous_location_updates:      TRUE
    update_interval_seconds:          10

LEGACY 911 FALLBACK PACKAGE (if NG911 unavailable):
  Channel type: AUDIO
  Automated voice message content:
    "Autonomous vehicle emergency. Vehicle ID: [id].
     Location: [address_derived]. Coordinates: [lat/lng].
     Medical emergency type: [emergency_type].
     Occupants: [occupant_count_total] total,
     [conscious_occupants] conscious.
     Autonomous routing capability: [autonomous_routing].
     Please provide routing address."
```

---

## SECTION 6 — THREE-PHASE ROUTING EXECUTION ARCHITECTURE

`[R]` Routing execution operates in three sequential phases following MEDICAL_EMERGENCY trigger. MRC deceleration runs concurrently as safety floor throughout all phases. Phase transition is triggered by received signals — not by elapsed time alone.

### Phase 1 — Contact and Transmit (Target: 0–5 seconds from trigger)

```
PHASE 1 — CONTACT AND TRANSMIT:

ACTIONS:
  Initiate 911 contact via cellular infrastructure
  Detect NG911 capability — structured or audio
  Compile emergency data package from current state
  Transmit structured package (NG911) OR
    activate audio fallback (legacy 911)
  Activate MRC deceleration as safety floor
  Display to conscious occupants (if AV-UBI-002
    CONSCIOUS_OCCUPANT_PRESENT = YES):
    "MEDICAL EMERGENCY DETECTED
     CONTACTING 911 NOW"

SUCCESS CONDITION:
  911 contact confirmed
  Data package transmission acknowledged
  → Proceed to PHASE 2

FAILURE CONDITIONS AND RESPONSES:
  911 contact fails — network unavailable:
    Retry at 5-second intervals — maximum 3 attempts
    If all attempts fail → FALLBACK PROTOCOL A
  Data package transmission fails — legacy 911:
    Audio fallback activated automatically
    → Proceed to PHASE 2 with degraded data channel
  GPS coordinates unavailable or low confidence:
    Last known location transmitted with
      LOW_CONFIDENCE flag
    Audio channel supplements with verbal location
      description if available
```

### Phase 2 — Wait and Receive (Target: 5–25 seconds from trigger)

```
PHASE 2 — WAIT AND RECEIVE:

ACTIONS:
  Await routing address from AV-UBI-005
  Await responder ETA from AV-UBI-005
  Continue MRC deceleration as safety floor
  Transmit continuous location updates to 911 channel
    at 10-second intervals
  Monitor AV-UBI-002 for occupant state changes
    If state changes — updated package transmitted
  Display to conscious occupants (if present):
    "911 CONTACTED
     AWAITING ROUTING INSTRUCTIONS"

WAIT INTERVAL TIMEOUT: 20 seconds from 911 contact
  At 15 seconds — transmit timeout warning to
    AV-UBI-005 channel: ROUTING_ADDRESS_TIMEOUT_WARNING
  At 20 seconds — if no address received:
    → FALLBACK PROTOCOL B

OCCUPANT STATE CHANGE DURING WAIT:
  If AV-UBI-002 state changes during PHASE 2:
    Updated package transmitted immediately
    Emergency type reclassification transmitted
    AV-UBI-005 notified of state change

SUCCESS CONDITION:
  Routing address received from AV-UBI-005
  → Proceed to PHASE 3

PARTIAL SUCCESS:
  Routing address received — responder ETA not received
  → Proceed to PHASE 3 without responder ETA display
  → Continue awaiting responder ETA; display when received
```

### Phase 3 — Route and Display (From address receipt)

```
PHASE 3 — ROUTE AND DISPLAY:

ACTIONS:
  Compute route to received address
    Governed by: ESTIMATED ARRIVAL TIME — not raw distance
  Suspend MRC full-stop deceleration
  Execute autonomous navigation to address
  Maintain reduced operational speed appropriate
    to autonomous urban operation
  Transmit continuous location updates to AV-UBI-005
    at 10-second intervals during routing
  Monitor AV-UBI-002 continuously during routing

DISPLAY TO CONSCIOUS OCCUPANTS (if present):
  Line 1: "ROUTING TO [FACILITY NAME]"
  Line 2: "ESTIMATED ARRIVAL: [ETA minutes]"
  Line 3: "EMERGENCY RESPONDERS EN ROUTE"
  Line 4: "RESPONDER ETA: [responder ETA]"
             (if received — omit line if not received)
  Line 5: "EMERGENCY REPORTED: [emergency_type]"
  Display update frequency: 30 seconds or on
    significant ETA change (>2 minutes variance)

MONITORING DURING ROUTING:
  AV-UBI-002 state monitored continuously
  If occupant state changes:
    Updated package transmitted to AV-UBI-005
    Display updated to reflect new classification
  If routing becomes unavailable (road closure etc.):
    Transmit REROUTING_REQUIRED to AV-UBI-005
    Request updated routing address
    MRC reactivated during re-routing interval
    Display: "REROUTING — PLEASE WAIT"
  If AV-UBI-005 transmits updated routing address:
    Reroute immediately to new address
    Display updated facility name and ETA

ARRIVAL PROTOCOL:
  At 500 meters from destination:
    Transmit ARRIVAL_IMMINENT to AV-UBI-005
  At destination:
    Stop vehicle at designated emergency entry point
      if determinable from map data — otherwise
      nearest safe stopping position
    Transmit ARRIVED to AV-UBI-005 with
      final coordinates
    Maintain MRC safety stop
    Display: "ARRIVED AT [FACILITY NAME]
              EMERGENCY SERVICES NOTIFIED"
    Hazard lights activated
```

---

## SECTION 7 — FALLBACK PROTOCOLS

`[D]` All fallback conditions have declared behavior. No undefined fallback state permitted under CDIP isolation discipline.

```
FALLBACK PROTOCOL A — 911 contact fails after 3 attempts:

  Condition: Network unavailable or 911 unreachable
    after 3 retry attempts at 5-second intervals

  Actions:
    MRC full-stop — vehicle stops at nearest safe position
    Hazard lights activated
    Horn pattern: emergency signal (3 long, 3 short, 3 long)
    Display (if conscious occupant present):
      "911 CONTACT FAILED
       EMERGENCY — CALL 911 NOW
       YOUR LOCATION: [address_derived]
       COORDINATES: [lat/lng]"
    Continue retry attempts at 30-second intervals
    If contact established during retry:
      Transmit emergency data package
      Proceed to PHASE 2

  Rationale: Vehicle cannot safely route without
    dispatcher coordination when contact has failed.
    Controlled stop with manual alert is safer than
    autonomous routing to unknown destination.
    Conscious occupant is the terminal human-in-the-loop
    fallback in this failure scenario.

---

FALLBACK PROTOCOL B — routing address not received
  within 20-second timeout:

  Condition: 911 contacted successfully; no routing
    address received within 20-second wait interval

  Actions:
    Compute route to nearest hospital from internal
      map data using estimated arrival time
    Proceed with autonomous routing to computed destination
    Display: "ROUTING TO NEAREST HOSPITAL
              911 COORDINATION PENDING"
    Continue transmitting location to 911 channel
      at 10-second intervals
    Accept routing address override from AV-UBI-005
      if received during autonomous routing —
      reroute immediately to received address
    Notify AV-UBI-005: ROUTING_FALLBACK_B_ACTIVE
      with destination transmitted

  Rationale: Known dispatcher delay is preferable to
    MRC full-stop when routing capability is available
    and destination class (hospital) is determinable
    without dispatcher confirmation. Continuous location
    transmission maintains dispatcher awareness.
    Override acceptance ensures dispatcher routing
    supersedes fallback routing when available.

---

FALLBACK PROTOCOL C — autonomous routing unavailable:

  Condition: Vehicle navigation system DEGRADED or
    UNAVAILABLE — cannot execute routing to address

  Actions:
    MRC full-stop — vehicle stops at nearest safe position
    Transmit to AV-UBI-005:
      AUTONOMOUS_ROUTING_UNAVAILABLE
      Current stopped coordinates
      Request: DISPATCH_TO_CURRENT_LOCATION
    Display (if conscious occupant present):
      "VEHICLE STOPPED
       EMERGENCY SERVICES DISPATCHED TO YOUR LOCATION
       YOUR LOCATION: [address_derived]
       STAY IN VEHICLE"
    Hazard lights activated
    Continue transmitting location at 10-second intervals
    Continue monitoring AV-UBI-002 for state changes

  Rationale: Routing failure does not eliminate 911
    contact benefit. Responders dispatched to current
    stopped location. Controlled stop is preferable to
    degraded autonomous routing attempt.
```

---

## SECTION 8 — FAILURE HORIZON MAP

`[D]` Failure mapped across four layers per CDIP v1.5 Section 4.5.

*Operational note: "failure" means the condition in which this component does not perform its specified function under its stated operating conditions — not a malfunction.*

| LAYER | TYPE | TRIGGER | OBSERVABLE INDICATOR | CONTAINMENT MECHANISM | CASCADE PROBABILITY |
|-------|------|---------|---------------------|-----------------------|-------------------|
| Layer 1 | Immediate catastrophic | 911 contact fails after all retries AND autonomous routing unavailable simultaneously | Vehicle stopped; no emergency services contact; no routing | FALLBACK PROTOCOL A — hazard lights, horn, display; manual contact by conscious occupant if present; terminal human-in-the-loop | MEDIUM |
| Layer 2 | Progressive degradation | 911 contacted but routing address not received within timeout | Vehicle operating on internal map routing without dispatcher coordination | FALLBACK PROTOCOL B — nearest hospital routing; continuous location transmission; override acceptance | LOW |
| Layer 3 | Control system collapse | Autonomous routing conflicts with MRC deceleration signal — competing control commands to vehicle navigation | Undefined vehicle navigation behavior during conflict | MRC priority rule — MRC always wins; routing waits during conflict; routing resumes after resolution | MEDIUM |
| Layer 4 | Cascading subsystem propagation | Vehicle routing in urban environment during emergency without full dispatcher coordination creates traffic conflict | Secondary incident involving other vehicles during emergency routing | UNKNOWN — dependent on intersection and traffic state during routing; hazard lights active throughout to signal emergency status | LOW |

### Cascade Chain Declarations

**Chain 1 — Layer 1 (terminal failure):**

```
CASCADE CHAIN:
From Layer 1 — simultaneous contact and routing failure:
Trigger mechanism: Network failure + navigation system
  failure simultaneously; both primary functions
  unavailable at trigger moment
Transmission path: Through infrastructure dependency —
  both 911 contact and routing require external
  infrastructure (cellular network, map data,
  navigation system)
Cascade speed: Immediate — both fail at trigger
Circuit-break condition: Manual intervention by
  conscious occupant — terminal human-in-the-loop
  fallback. AV-UBI-002B conscious passenger
  capability assessment becomes critical here —
  CONSCIOUS_OCCUPANT_PRESENT alone is insufficient;
  capability to place 911 call matters.
  This is the strongest argument for AV-UBI-002B
  prioritization after core stack completion.
```

**Chain 2 — Layer 3 → Layer 4:**

```
CASCADE CHAIN:
From Layer 3 to Layer 4:
Trigger mechanism: MRC/routing conflict produces
  erratic vehicle behavior during emergency transit
  in urban shared traffic environment
Transmission path: Through physical traffic environment —
  erratic behavior creates unpredictable movement
  in space shared with other agents
Cascade speed: Immediate
Circuit-break condition: MRC priority resolution —
  MRC always wins; vehicle decelerates during
  conflict; routing resumes after resolution;
  conflict window is bounded by priority rule
  response time, not by driver response
```

---

## SECTION 9 — BREAKTHROUGH DENSITY INDEX

`[D]` Counting against CDIP v1.5 Section 1B operational definition — requirements that cannot be satisfied by existing validated knowledge, even with additional time or effort.

| # | REQUIREMENT | BREAKTHROUGH? | REASONING | TAG |
|---|-------------|--------------|-----------|-----|
| 1 | Structured AV-to-911 emergency data package transmission and reception within 3–5 seconds over cellular infrastructure | **NO** | Cellular data transmission at this volume within this latency is within documented capability. NG911 infrastructure supports structured data. Engineering integration problem — not new empirical knowledge. | `[R]` |
| 2 | Concurrent MRC deceleration and autonomous destination routing without conflicting vehicle control signals | **NO** | Complex engineering integration but solution path known — priority arbitration systems exist in aerospace and robotics. Requires adaptation and validation, not new empirical knowledge. | `[R]` |
| 3 | Estimated arrival time routing to emergency facility during autonomous operation without human authority | **NO** | ETA routing is a solved navigation problem. Applying it to emergency autonomous routing requires integration and validation — not new empirical knowledge. | `[R]` |
| 4 | Emergency data package interoperability with AV-UBI-005 dispatcher system without translation layer introducing unacceptable latency | **YES** | A-009 is A3. No standard exists. Interoperability requires co-specification between this component and AV-UBI-005 — neither can independently validate it. Requires new agreed specification validated through testing. | `[D]` |

**BDI = 1 — FOCUSED RESEARCH** `[D]`

`[D]` BDI = 1 — lowest BDI in the AV-UBI stack. Justification:

The single breakthrough requirement is a co-specification gap, not a fundamental knowledge gap. The knowledge to build both sides of the interface exists. The validated agreement between the two sides does not exist because AV-UBI-005 has not been specified. This breakthrough closes automatically when AV-UBI-005 session is complete and the interface contract is co-validated. Every other requirement in this component is a solved-problem integration.

### BDI Hard Halt Assessment

`[D]` BDI = 1. Hard halt not triggered. Component proceeds.

### BDI-Assumption Integrity Check

*Triggered: A4 assumption present (A-010) AND Instability_ratio = 0.30 > 0.20.*

**A-010 reviewed:**
> "Autonomous vehicle routing to received address during concurrent MRC deceleration without human authority is legally permissible in target jurisdictions"

- Condition (a): Requires genuinely new empirical knowledge? **NO** — regulatory analysis required, not new physical or technical knowledge.
- Condition (b): Never-demonstrated capability? **PARTIAL** — autonomous emergency routing exists in adjacent domains; AV-specific regulatory authorization absent.

→ A-010 correctly classified A4 — speculative about regulatory outcomes, not technical capability. Does not meet breakthrough threshold. BDI unchanged.

**A-008 reviewed (A3):**
→ Confirmed as contributing to BDI item 1 — NG911 coverage affects data package delivery reliability. Already counted. No increment.

**A-009 reviewed (A3):**
→ Confirmed as BDI item 1 directly. Already counted. No increment.

**4.6D Output:** All speculative assumptions reviewed. No concealed breakthroughs. BDI = 1 confirmed. `[D]`

---

## SECTION 10 — DEPENDENCY TRANSPARENCY GRID

`[D]` All eight fields declared. No hidden dependencies permitted.

| FIELD | CONTENT |
|-------|---------|
| **Inputs** | MEDICAL_EMERGENCY trigger — from AV-UBI-001 STATE 4 OR AV-UBI-003 authority window override — both paths produce identical behavior · AV-UBI-002 full classification state at trigger moment — emergency type, confidence score, occupant count, conscious occupants · AV-UBI-002 continuous state updates during routing — state changes transmitted to AV-UBI-005 · GPS location and heading at trigger moment · Vehicle speed and trajectory at trigger moment · Vehicle navigation system status — CAPABLE / DEGRADED / UNAVAILABLE · Cellular network status — NG911 / legacy / unavailable · Routing address from AV-UBI-005 (received — not assumed) · Responder ETA from AV-UBI-005 (received — not assumed) |
| **Outputs** | 911 contact initiation · Emergency data package (structured) to AV-UBI-005 · Audio fallback channel content (legacy 911) · Autonomous routing command to vehicle navigation system · MRC coordination signal — suspend full-stop / reactivate · Continuous location updates to AV-UBI-005 at 10-second intervals during routing · Conscious occupant display commands — PHASE 1 / PHASE 2 / PHASE 3 / FALLBACK messages · AUTONOMOUS_ROUTING_UNAVAILABLE signal to AV-UBI-005 if routing fails · ARRIVED signal to AV-UBI-005 at destination · REROUTING_REQUIRED request to AV-UBI-005 if routing disrupted |
| **Energy source** | Computational — onboard processing · Cellular radio for 911 contact and data transmission · Vehicle navigation system for routing execution · Display and audio subsystems for occupant alerts · Hazard light and horn systems for FALLBACK PROTOCOL A |
| **Control dependencies** | Governed by MEDICAL_EMERGENCY trigger — activation non-optional once trigger received · Governed by MRC priority rule — MRC always wins control conflict with routing · Governed by wait interval timeout (20 seconds) — FALLBACK PROTOCOL B activates at timeout · Governed by AV-UBI-002 continuous state — updated packages transmitted if state changes · Governed by AV-UBI-005 routing address — routing cannot execute without received address except in FALLBACK PROTOCOL B |
| **Environmental exposure** | Cellular network coverage and NG911 infrastructure availability · Urban GPS accuracy under canyon conditions · Traffic state during autonomous routing — affects ETA accuracy · Road network availability during routing — closures, construction · AV-UBI-005 response latency — not governed by this component |
| **Maintenance requirements** | Internal map data for FALLBACK PROTOCOL B must be current and include hospital locations · GPS accuracy calibration per deployment environment · Emergency data package format requires re-validation if AV-UBI-005 interface contract changes · Wait interval timeout requires re-validation if AV-UBI-005 response latency profile changes across jurisdictions · Cellular infrastructure capability audit required per deployment jurisdiction before production |
| **Upstream reliance** | AV-UBI-002 must provide classification state at trigger moment — stale data not acceptable · AV-UBI-001 STATE 4 or AV-UBI-003 must deliver MEDICAL_EMERGENCY trigger — component does not self-activate · Vehicle navigation system must be operational for PHASE 3 — FALLBACK PROTOCOL C if unavailable · Cellular infrastructure must be available — FALLBACK PROTOCOL A if unavailable · MRC system must be operational as safety floor — MRC failure during this component's operation is an upstream failure outside this component's scope |
| **Downstream impact** | AV-UBI-005 receives emergency data package, continuous location updates, routing status signals, and occupant state changes · Vehicle navigation system receives routing commands and suspension/reactivation coordination · MRC system receives coordination signals — suspend / reactivate · Conscious occupant display receives all phase and fallback alert messages · Emergency facility receives incoming patient data via AV-UBI-005 — not directly from this component |

---

## SECTION 11 — INVALIDATION CONDITIONS

> "This component is invalid if:"

1. Cellular network latency for emergency data package transmission is demonstrated to be structurally incompatible with the 3–5 second contact window in target urban deployment environments — meaning physics of data transmission over available infrastructure cannot meet the timing requirement regardless of optimization `[D]`

2. Concurrent MRC deceleration and autonomous destination routing is demonstrated to produce irresolvable control conflicts in the vehicle navigation system — meaning the two signals cannot coexist regardless of priority arbitration architecture `[R]`

3. FALLBACK PROTOCOL B (routing to nearest hospital on internal map data) is demonstrated to be less safe than FALLBACK PROTOCOL A (full stop) in the majority of urban scenarios where AV-UBI-005 response is delayed — meaning the autonomous routing fallback creates more risk than controlled stop `[S]`

4. Emergency data package interoperability with AV-UBI-005 requires a translation layer that introduces latency exceeding the PHASE 1 transmission window — meaning the co-specification requirement cannot be met without degrading the contact timeline `[R]`

5. The three-phase routing architecture is demonstrated to be incomplete — meaning real emergency scenarios produce states not covered by PHASE 1, PHASE 2, PHASE 3, or any declared fallback protocol `[S]`

6. GPS coordinate accuracy in target urban deployment environments is demonstrated to be insufficient for emergency address derivation — meaning location data transmitted to AV-UBI-005 is structurally unreliable as a routing input `[R]`

---

## SECTION 12 — VALIDATION LEVEL

**Validation Level: CONCEPTUAL**

`[D]` This component specification is logically consistent with its stated constraint set and internally consistent with AV-UBI-001 v1.1, AV-UBI-002, and AV-UBI-003 interface requirements. It has not been tested against physical or operational reality. One breakthrough requirement remains open — data package interoperability — which closes when AV-UBI-005 is specified and interface contract is co-validated.

| LEVEL | STATUS |
|-------|--------|
| Conceptual | ✓ CURRENT — logically consistent |
| Physics-Consistent | Pending — BDI item 1 closes when AV-UBI-005 session complete and interface co-validated |
| Simulation-Ready | Pending — three-phase protocol and fallback architecture require simulation validation |
| Experimentally Validated | Pending |
| Production-Grade | Pending — regulatory clearance (A-010) required in addition to technical validation |

---

## SECTION 13 — VERSION SUMMARY

| FIELD | VALUE |
|-------|-------|
| **Domain ID** | AV-UBI-004 |
| **Component** | Vehicle-side emergency contact and routing execution |
| **BDI Class** | FOCUSED RESEARCH (BDI = 1) — lowest in AV-UBI stack |
| **Validation Level** | CONCEPTUAL |
| **High Instability Flag** | YES — Instability_ratio: 0.30 |
| **Sponsor Authorization** | Not required — BDI < 3 |
| **4.6D Check** | EXECUTED — no concealed breakthroughs found |
| **Open Breakthrough Requirements** | (1) Emergency data package interoperability with AV-UBI-005 — closes when AV-UBI-005 session complete |
| **Novel architectural contributions** | (1) Structured AV-to-911 emergency data package — first formal specification · (2) Three-phase emergency contact and routing protocol with declared phase transitions — first formal specification · (3) Concurrent MRC and autonomous routing with MRC priority arbitration — first formal specification · (4) Three-path fallback architecture with declared behavior for all failure conditions — first formal specification · (5) Conscious occupant stress-condition display protocol during autonomous emergency routing — first formal specification |
| **Primary cascade risk** | Layer 1 — simultaneous 911 contact failure and routing unavailability; terminal fallback to manual intervention by conscious occupant; AV-UBI-002B capability assessment critical here |
| **AV-UBI-005 dependency** | BDI item 1 closes when AV-UBI-005 specifies compatible data package format — co-specification required; neither component can be independently validated on this item |
| **Regulatory flag** | A-010 — autonomous routing without human authority requires jurisdiction-specific legal clearance; deployment blocked until regulatory authorization obtained |
| **FCL Entries** | 0 — specification complete, empirical validation pending |
| **Next version trigger** | AV-UBI-005 session complete OR NG911 infrastructure testing OR first FCL entry from integration simulation |

---

## SECTION 14 — COMPONENT STACK POSITION

`[D]` AV-UBI-004 occupies the following position in the AV-UBI specification stack:

```
AV-UBI-001 v1.1 — Operational envelope decision logic
  STATE 4 → triggers AV-UBI-004

AV-UBI-002 — Cabin occupant readiness classification
  MEDICAL_EMERGENCY signal → AV-UBI-001 STATE 4
  Occupant state at trigger moment → AV-UBI-004
  Continuous state updates during routing → AV-UBI-004
  CONSCIOUS_OCCUPANT_PRESENT → AV-UBI-004 display logic

AV-UBI-003 — Reaction-latency gap resolution
  Authority window MEDICAL_EMERGENCY override → AV-UBI-004

AV-UBI-004 — Vehicle-side emergency contact and routing (THIS COMPONENT)
  ↓
  Sends to: AV-UBI-005 — emergency data package + location updates
  Sends to: Vehicle navigation system — routing commands
  Sends to: MRC system — coordination signals
  Sends to: Display system — occupant alert messages

DOWNSTREAM REQUIRED SESSION:
AV-UBI-005 — AI-assisted 911 dispatcher intelligence
  Receives: Emergency data package from AV-UBI-004
  Processes: Dispatch decision, facility selection by ETA
  Sends: Routing address and responder ETA to AV-UBI-004
  BDI item 1 co-validation depends on this session

FUTURE SESSIONS (from stack):
AV-UBI-002B — Conscious passenger capability detection
  Critical for FALLBACK PROTOCOL A terminal scenario
AV-UBI-002C — Choking and seizure classification
  Expands MEDICAL_EMERGENCY type classification
```

---

## SECTION 15 — OPEN ACTIONS

| ACTION | PRIORITY | TRIGGER |
|--------|----------|---------|
| Run AV-UBI-005 session — AI-assisted 911 dispatcher intelligence | CRITICAL | Next session — closes BDI item 1 |
| Co-validate emergency data package format between AV-UBI-004 and AV-UBI-005 | CRITICAL | AV-UBI-005 session complete |
| NG911 infrastructure audit per target deployment jurisdiction | HIGH | Pre-deployment planning |
| Regulatory clearance assessment per jurisdiction for autonomous emergency routing | HIGH | Pre-deployment planning — A-010 |
| Integration simulation — three-phase protocol with MRC concurrent operation | HIGH | Simulation environment available |
| Prioritize AV-UBI-002B — conscious passenger capability | MEDIUM | Layer 1 cascade terminal scenario makes this the highest-value future session |
| Update README stack status — AV-UBI-004 complete | LOW | Immediate |

---

*AV-UBI-004 v1.0 — Vehicle-Side Emergency Contact and Routing Execution*
*CDIP v1.5 | ECF v0.5 | LAV v1.5 | FSVE v3.5*
*BDI = 1 — FOCUSED RESEARCH | Validation: CONCEPTUAL*
*Session complete. No expansion permitted without new DST.*

*Novel contributions: Structured AV-to-911 emergency data package · Three-phase contact and routing protocol · Concurrent MRC and autonomous routing with priority arbitration · Three-path fallback architecture · Conscious occupant stress-condition display protocol.*

*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Co-Architect: Claude (Anthropic) | February 2026*
*Open-source specification — no prior version required*
