# AV-UBI-002
## Cabin Occupant Readiness Classification
### CDIP v1.5 Component Specification
#### Constraint–Domain Isolation Protocol | ECF v0.5 Active | LAV v1.5 Active

---

**Domain ID:** AV-UBI-002
**Industry:** Autonomous Vehicle Systems — Urban Deployment
**Constraint Category:** Cabin Occupant Readiness Classification
**Reference Macro-System:** Level 3-4 Autonomous Vehicle Platform *(context only — not a design target)*
**Validation Level:** CONCEPTUAL
**BDI Class:** HIGH-RISK ARCHITECTURE (BDI = 2, reduced from 4)
**Session Priming:** AV-UBI-001 — CONSTRAINT-INPUT · FAILURE-DATA
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

`[D]` AV-UBI-002 specifies the classification logic that takes available multi-stream sensor data from across the vehicle cabin and produces a graduated confidence score and categorical state classification for each occupant, delivered within 150–175ms, for consumption by AV-UBI-001's decision logic.

`[D]` This component is:
- The **occupant state classification engine** — not a sensor system
- Scoped to **all occupied seats** in the cabin — not driver only
- Producing **both a graduated confidence score and a categorical state classification** per occupant
- Required to **default to UNRESPONSIVE automatically** if output is not produced within 175ms

`[D]` This component is NOT:
- A sensor hardware specification
- A conscious passenger capability assessment (AV-UBI-002B)
- A choking or seizure classification component (AV-UBI-002C)
- An emergency routing component (AV-UBI-004)
- A full driver monitoring system

**One component. One version. No exceptions.**

---

## DOMAIN SESSION TOKEN

```
Domain ID:             AV-UBI-002
Industry:              Autonomous Vehicle Systems — Urban Deployment
Constraint Category:   Cabin Occupant Readiness Classification
Reference Macro-System: Level 3-4 Autonomous Vehicle Platform
                        (context only — not a design target)
Validation Target:     Physics-Consistent Architecture
Prior Session Reference: AV-UBI-001 — CONSTRAINT-INPUT · FAILURE-DATA
Priming Type:          CONSTRAINT-INPUT · FAILURE-DATA
Priming Scope:         Decision cycle latency requirement (300–800ms)
                       from AV-UBI-001 Domain Lock active as governing
                       input. Failure Horizon Layers 1–3 cascade chains
                       from AV-UBI-001 active as harvesting seed data.
                       A-001 (human reaction latency floor 1.5s) carried
                       as A1. A-003 (driver monitoring accuracy) carried
                       as A2-under-review per Decay Rule D-3.
```

---

## SECTION 1 — DOMAIN LOCK

`[D]` Governing constraints for cabin occupant readiness classification across full occupant state space in urban autonomous vehicle deployment. Design halts if any of the following are disputed before proceeding.

### Physical Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Sensor physics — eye tracking | Infrared eye tracking requires unobstructed line of sight; sunglasses, certain medical conditions, and extreme head angles defeat detection; maximum reliable range 18–24 inches from sensor | `[D]` |
| Sensor physics — biometric (rPPG) | Contactless heart rate detection (camera-based rPPG) achieves 70–85% accuracy under controlled conditions; degrades under motion, variable lighting, and skin tone variation | `[D]` |
| Sensor physics — grip | Capacitive steering wheel grip detection requires skin contact; gloves defeat detection; grip pressure alone cannot distinguish relaxed conscious grip from unconscious grip without individual baseline | `[D]` |
| Signal fusion latency | Each additional sensor stream adds computational load; fusion of 8 streams into single confidence score within 150–175ms is at the boundary of current embedded processing capacity | `[R]` |
| Cabin geometry | Fixed sensor placement must cover variable occupant positions across all seat configurations; no single sensor placement covers all occupant positions without blind spots | `[D]` |
| Medical state detection physics | Distinguishing cardiac event from sleep from impairment requires biometric signals that contactless sensors cannot yet measure with clinical reliability | `[D]` |
| Repeated classification latency | Producing a valid classification output every 150–175ms continuously without thermal throttling or processing degradation is an embedded systems constraint not yet validated at this sensor combination density | `[R]` |

### Informational Constraints

| CONSTRAINT | GOVERNING PRINCIPLE | TAG |
|------------|-------------------|-----|
| Baseline requirement | Accurate state classification requires individual occupant baseline — cold-start classification without baseline produces higher false positive/negative rates | `[D]` |
| State transition ambiguity | Several target states share observable signatures at detection boundary — drowsy vs. early cardiac event, drunk vs. medical emergency; disambiguation requires multi-signal confirmation across time | `[R]` |
| Occupant count variability | Component must handle 1–5 occupants dynamically; classification complexity scales non-linearly with occupant count | `[R]` |
| Privacy constraint | Continuous biometric monitoring of all occupants generates sensitive personal data; data minimization principles govern what can be retained vs. processed-and-discarded | `[D]` |
| False positive cost | MEDICAL_EMERGENCY false positive triggers emergency routing — high disruption cost; false negative costs are potentially fatal; asymmetric error costs govern threshold architecture | `[R]` |
| Conscious passenger detection | Determining whether a non-driver occupant is conscious, capable, and positioned to assist requires behavioral signal interpretation not currently in any production system — deferred to AV-UBI-002B | `[R]` |

`[D]` Design halts if any of the above are disputed before proceeding.

---

## SECTION 2 — STATE-OF-THE-ART BASELINE ENVELOPE

`[D]` All values labeled per CDIP v1.5 Section 4.2 labeling protocol. No unlabeled performance claims permitted.

| PARAMETER | VALUE | LABEL |
|-----------|-------|-------|
| Current production eye-tracking accuracy (driver only) | 85–92% under non-adverse conditions | Empirical `[D]` |
| Camera-based rPPG heart rate accuracy | 70–85% controlled; degrades significantly under motion | Empirical `[D]` |
| Steering wheel grip detection (capacitive) | Deployed in production; binary contact only in most systems | Industry Standard `[D]` |
| Multi-sensor fusion classification latency (current best) | 200–400ms for 3–4 sensor streams | Empirical `[D]` |
| 8-stream fusion at 150–175ms | Not demonstrated in production embedded systems | Unknown `[?]` |
| Occupant state classification beyond driver | No production system — research only | Unknown `[?]` |
| Medical emergency detection (automotive) | No validated production system | Unknown `[?]` |
| Conscious passenger assist-capable detection | No system demonstrated | Unknown `[?]` |
| Cabin-wide multi-occupant readiness classification | No system demonstrated | Unknown `[?]` |

`[R]` **Critical baseline finding:** Every capability beyond single-driver eye-tracking and head position is either research-stage or undemonstrated. This component is operating almost entirely beyond the validated production frontier. Constraint harvest must be rigorous. BDI is high.

---

## SECTION 3 — CONSTRAINT HARVESTING

`[D]` Harvested from automotive safety literature, medical monitoring research, human factors studies, and AV incident analysis before design activity began.

### Existing Architecture Patterns

- **Single-driver eye-tracking:** Deployed in Volvo, Mercedes, BMW — monitors gaze direction and blink rate; driver seat only
- **Driver Monitoring Systems (DMS):** EU mandated from 2024 — head position plus eye tracking, driver seat only
- **Wearable biometric monitoring:** Research demonstrations only in automotive context; not production-deployed
- **Camera-based rPPG:** Demonstrated in controlled research; not production-deployed in vehicles
- **Seat occupancy detection:** Pressure-based, binary — present/absent only, no state classification
- **eCall system:** Automatic emergency call on airbag deployment — reactive post-event, not predictive

### Known Failure Case Studies

- **DMS defeat by sunglasses:** Documented across multiple production systems — eye tracking fails, system defaults to no-alert `[D]`
- **Cold-start false positives:** Systems without individual baseline flag alert drivers as inattentive in first 30–60 seconds `[D]`
- **Drowsy vs. medical event misclassification:** No production system distinguishes these — both produce similar observable signatures in early stages `[D]`
- **Multi-occupant blind spots:** All current DMS architectures monitor driver seat exclusively — passenger states invisible to system `[D]`
- **Grip detection with gloves:** Capacitive systems produce false unresponsive signals in cold weather glove use `[D]`

### Target State Distinguishing Signatures

`[R]` The following state-to-signal mapping is derived from human factors and medical literature. It governs what the multi-stream sensor combination must be capable of distinguishing:

| STATE | DISTINGUISHING SIGNALS |
|-------|----------------------|
| Attentive | Eyes on road, head stable, grip normal, vitals at individual baseline |
| Inattentive / distracted | Eyes off road, head turned, grip normal, vitals baseline |
| Drowsy | Eyes closing (micro-sleep patterns), head dropping, grip loosening, breathing rhythm shift |
| Asleep | Eyes closed sustained, head dropped, grip released, breathing rhythm slowed |
| Impaired (alcohol/substances) | Eye movement irregular, head instability, grip inconsistent, reaction lag in behavioral response |
| Behavioral unresponsive | Loss of all active signals — grip released, head dropped, eyes closed, no vocalization |
| Medical emergency (cardiac) | Sudden loss of active signals, possible facial blood flow change detectable via rPPG within 30–60 seconds of onset, postural collapse in seat pressure |
| Conscious passenger present | Seat pressure active, movement present, vocalization possible — gross detection only (capability assessment deferred to AV-UBI-002B) |

### Unresolved Structural Blind Spots

- No validated method for distinguishing behavioral unresponsiveness from medical emergency using contactless sensors alone
- No architecture for conscious-passenger-capable detection (deferred to AV-UBI-002B)
- No multi-occupant fusion architecture with defined output latency demonstrated
- Baseline establishment protocol for new or multiple occupants not defined in any production system
- Asymmetric error cost architecture — formal threshold-setting framework where false positive and false negative carry different consequence weights — not addressed in current systems

### Interface Confusion Cases

- Boundary between this component's MEDICAL_EMERGENCY signal and AV-UBI-004 emergency routing activation logic is undefined in all current systems — no formal handoff specification exists `[R]`
- Boundary between this component's readiness classification output and AV-UBI-001 decision logic input not formally specified in any production architecture — AV-UBI-001 was designed to receive this signal; no system currently produces it `[R]`

*Harvesting complete. Design phase open.*

---

## SECTION 4 — ASSUMPTION REGISTER

`[D]` All assumptions listed and classified per CDIP v1.5 Section 4.4.

| ID | CLASS | ASSUMPTION | VALIDATED | RE-VALIDATION TRIGGER |
|----|-------|------------|-----------|----------------------|
| A-001 | A1 | Human reaction latency floor 1.5s — carried from AV-UBI-001 | Empirical neuroscience | If new human factors data published |
| A-002 | A1 | Infrared eye tracking defeated by sunglasses and extreme head angles | Empirical — documented in production systems | If new sensor technology demonstrated |
| A-003 | A1 | Seat pressure distribution changes measurably during loss of consciousness | Empirical — medical literature on postural collapse | If new measurement data challenges this |
| A-004 | A1 | Cardiac events produce measurable changes in facial blood flow detectable by rPPG within 30–60 seconds of onset | Empirical — medical literature | If medical literature contradicts |
| A-005 | A2 | 8-stream sensor fusion can be architected to produce classification output within 150–175ms using parallel processing pipeline | Engineering plausible — parallel architecture reduces sequential latency | If embedded systems testing contradicts |
| A-006 | A2 | Individual occupant baseline can be established within first 60–90 seconds of session without interrupting normal operation | Engineering plausible — passive observation period | If baseline establishment testing contradicts |
| A-007 | A2 | Drowsy state and early medical emergency can be disambiguated within 3–5 seconds using combined biometric and behavioral signals | Engineering plausible — multi-signal disambiguation has research support | If research contradicts disambiguation timeline |
| A-008 | A2 | Conscious passenger presence and gross capability can be detected via seat pressure, movement pattern, and vocalization signals combined — gross detection only | Engineering plausible — combination not validated as integrated system | If system testing contradicts |
| A-009 | A3 | Camera-based rPPG achieves sufficient accuracy for medical emergency detection under vehicle motion and variable lighting conditions | Research-stage — controlled demonstrations only; vehicle conditions untested | If production-condition testing demonstrates |
| A-010 | A3 | 8-stream continuous fusion at 150–175ms is achievable without thermal throttling in automotive-grade embedded hardware over sustained operation | Research-stage — no sustained operation demonstration at this sensor density | If automotive-grade hardware testing demonstrates |
| A-011 | A4 | Choking event produces a distinctive enough combined signal signature to be classified separately from other unresponsive states within the classification latency window | Speculative — deferred to AV-UBI-002C | AV-UBI-002C session |
| A-012 | A4 | Seizure produces a distinctive enough combined signal signature to be classified as MEDICAL_EMERGENCY within the latency window | Speculative — deferred to AV-UBI-002C | AV-UBI-002C session |

**Note:** A-011 and A-012 are carried in this register for traceability but travel with AV-UBI-002C. They do not contribute to this component's active BDI after scope reduction.

**Post-scope-reduction instability ratio:** (A3 + A4 active) / total active = 2/10 = **0.20 → HIGH INSTABILITY FLAG CLEARED** *(exactly at threshold — monitor at next version)* `[D]`

### Assumption Decay Protocol

**Decay Rule D-1:** A-001 through A-004 carry empirical validation sources above. Re-validation triggers declared.

**Decay Rule D-2:** All assumptions declare re-validation triggers in the register above.

**Decay Rule D-3:** A-003 carried from AV-UBI-001 as A2-under-review — confirmed A2 in this session based on EU DMS deployment data. All A2 assumptions from this session are A2-under-review at next session open until confirmed.

---

## SECTION 5 — SENSOR STREAM ARCHITECTURE

`[R]` The following eight sensor streams are required inputs to the classification component. Stream architecture governs what signals are available for fusion.

| STREAM | SENSOR TYPE | OCCUPANT COVERAGE | PRIMARY STATE CONTRIBUTION |
|--------|-------------|------------------|--------------------------|
| 1 | Infrared eye tracking | Driver + front passenger | Attentiveness, drowsiness, impairment |
| 2 | Head position and movement tracking | All occupied seats | Drowsiness, postural collapse, behavioral pattern |
| 3 | Steering wheel capacitive grip pressure | Driver only | Engagement level, loss of consciousness |
| 4 | Seat pressure distribution | All occupied seats | Postural state, loss of consciousness, occupant presence |
| 5 | Camera-based rPPG biometric | All occupied seats | Heart rate, cardiac event detection, impairment |
| 6 | Cabin microphone vocalization | Cabin-wide | Distress, choking (gross detection), conscious state |
| 7 | Seat occupancy detection | All seats | Occupant count, presence/absence |
| 8 | CO2 / air quality monitoring | Cabin-wide | Secondary impairment detection support |

`[R]` **Stream health monitoring:** Each stream must report its own confidence status continuously. Degraded stream triggers automatic confidence score adjustment in fusion output. Loss of rPPG stream (Stream 5) specifically must elevate MEDICAL_EMERGENCY threshold sensitivity on remaining streams — rPPG is the primary medical emergency discriminator.

---

## SECTION 6 — CLASSIFICATION OUTPUT ARCHITECTURE

`[D]` This component produces a hybrid output — both graduated and categorical — as a dual failsafe architecture.

### Primary Output (per occupant)

```
CONFIDENCE SCORE: [0.00 – 1.00]
  Graduated continuous score representing classification certainty.
  Updated every 150–175ms.
  Score reflects both state classification confidence AND
  sensor stream health at time of output.
```

### Secondary Output (per occupant)

```
STATE CLASSIFICATION: categorical
  READY              — occupant attentive and control-capable
  DEGRADED           — occupant present but attention or
                       capability reduced; AV-UBI-001 should
                       weight takeover demand lower
  BEHAVIORAL_UNRESPONSIVE — occupant not responding to environment;
                       no medical emergency indicators present
  MEDICAL_EMERGENCY  — medical emergency indicators present;
                       AV-UBI-004 emergency routing signal triggered
```

### Aggregate Output (cabin-level)

```
CABIN_READINESS_SUMMARY:
  Highest-risk occupant state flagged as cabin state
  CONSCIOUS_OCCUPANT_PRESENT: YES / NO
    (gross detection only — detailed capability
    assessment deferred to AV-UBI-002B)
```

### Failsafe Output

```
FAILSAFE:
  Condition: Classification output not produced within 175ms
  Action: UNRESPONSIVE default delivered automatically
  Requirement: Null output and UNRESPONSIVE output must
    produce identical downstream behavior in AV-UBI-001.
    This must be hardwired — no conditional logic on null.
```

### Disambiguation Timer

```
DISAMBIGUATION PROTOCOL:
  Condition: BEHAVIORAL_UNRESPONSIVE persists beyond
    15–20 seconds without any recovery signal
  Action: Escalate to MEDICAL_EMERGENCY_SUSPECTED
    and re-classify using remaining stream data
  Purpose: Circuit-break condition for Chain 2 cascade —
    prevents permanent BEHAVIORAL_UNRESPONSIVE
    classification when medical event is progressing
```

*[Note: The disambiguation timer is novel. No current production system implements a time-bounded escalation from behavioral to medical classification. This is a primary architectural contribution of AV-UBI-002.]*

---

## SECTION 7 — FAILURE HORIZON MAP

`[D]` Failure mapped across four layers per CDIP v1.5 Section 4.5.

*Operational note: "failure" means the condition in which this component does not perform its specified function under its stated operating conditions — not a malfunction.*

*Operational note: "containment mechanism" means an active process — not a passive structural feature — that limits the spread of failure once triggered.*

| LAYER | TYPE | TRIGGER | OBSERVABLE INDICATOR | CONTAINMENT MECHANISM | CASCADE PROBABILITY |
|-------|------|---------|---------------------|-----------------------|-------------------|
| Layer 1 | Immediate catastrophic | Classification output not produced within 175ms window | No signal delivered to AV-UBI-001 | Failsafe default to UNRESPONSIVE — AV-UBI-001 activates MRC | HIGH |
| Layer 2 | Progressive degradation | Sensor stream dropout reduces classification accuracy below reliable threshold | Confidence score falls below minimum viable threshold | Surviving streams maintain degraded classification; confidence score reflects degradation; AV-UBI-001 informed of degraded input | MEDIUM |
| Layer 3 | Control system collapse | Baseline corruption — occupant change mid-session without baseline reset | Classification systematically biased toward prior occupant baseline | Session baseline reset trigger; degraded confidence flagged to AV-UBI-001 until new baseline established | MEDIUM |
| Layer 4 | Cascading subsystem propagation | MEDICAL_EMERGENCY false negative — event classified as BEHAVIORAL_UNRESPONSIVE | Emergency routing not triggered; AV-UBI-001 attempts MRC or takeover demand on medically unresponsive occupant | Unknown — dependent on whether MRC succeeds and whether other occupants can respond | HIGH |

### Cascade Chain Declarations

**Chain 1 — Layer 1 → AV-UBI-001 Layer 1 (primary inter-component cascade):**

```
CASCADE CHAIN:
From AV-UBI-002 Layer 1 to AV-UBI-001 Layer 1:
Trigger mechanism: Classification output failure within
  175ms window; no readiness signal delivered;
  AV-UBI-001 decision logic receives null input
Transmission path: Through component interface —
  AV-UBI-001 is dependent on this component's output;
  null input forces worst-case assumption
Cascade speed: Immediate — within decision cycle window
Circuit-break condition: Failsafe default to UNRESPONSIVE
  must be hardwired — null output and UNRESPONSIVE output
  must produce identical downstream behavior in AV-UBI-001
```

**Chain 2 — Layer 4 → AV-UBI-001 incorrect decision:**

```
CASCADE CHAIN:
From AV-UBI-002 Layer 4 to AV-UBI-001 decision error:
Trigger mechanism: MEDICAL_EMERGENCY classified as
  BEHAVIORAL_UNRESPONSIVE; AV-UBI-001 receives wrong
  state classification; issues takeover demand or MRC
  instead of emergency routing signal
Transmission path: Through classification output —
  AV-UBI-001 trusts this component's output;
  wrong input produces wrong decision
Cascade speed: Immediate
Circuit-break condition: Disambiguation timer —
  if BEHAVIORAL_UNRESPONSIVE persists beyond
  15–20 seconds without recovery signal, escalate to
  MEDICAL_EMERGENCY_SUSPECTED and re-classify
```

**Chain 3 — Layer 2 → Layer 4 (degradation enabling false negative):**

```
CASCADE CHAIN:
From Layer 2 to Layer 4:
Trigger mechanism: Sensor dropout degrades biometric
  stream specifically; medical emergency occurs
  during degraded biometric state; system cannot
  distinguish emergency from behavioral unresponsive
  without rPPG signal
Transmission path: Through sensor dependency —
  rPPG stream is the primary medical emergency
  discriminator; its loss collapses emergency detection
Cascade speed: Hours to immediate — degradation
  may precede emergency by any interval
Circuit-break condition: rPPG stream dropout must
  elevate MEDICAL_EMERGENCY threshold sensitivity
  on remaining streams — compensatory heightening
  when primary discriminator is unavailable
```

---

## SECTION 8 — BREAKTHROUGH DENSITY INDEX

`[D]` Counting against CDIP v1.5 Section 1B operational definition — requirements that cannot be satisfied by existing validated knowledge, even with additional time or effort.

### Pre-Scope-Reduction BDI = 4

| # | REQUIREMENT | BREAKTHROUGH? | DISPOSITION |
|---|-------------|--------------|------------|
| 1 | 8-stream sensor fusion at 150–175ms continuously in automotive-grade embedded hardware | YES | Retained in AV-UBI-002 |
| 2 | Reliable medical emergency detection using contactless sensors under vehicle motion and variable lighting | YES | Retained in AV-UBI-002 |
| 3 | Conscious passenger capability detection | YES | Scoped to AV-UBI-002B |
| 4 | Choking and seizure distinctive signal classification within latency window | YES | Scoped to AV-UBI-002C |

### Post-Scope-Reduction BDI = 2

| # | REQUIREMENT | BREAKTHROUGH? | REASONING | TAG |
|---|-------------|--------------|-----------|-----|
| 1 | 8-stream sensor fusion producing graduated confidence score plus categorical classification within 150–175ms continuously in automotive-grade embedded hardware | **YES** | A-010 is A3. No production demonstration at this sensor density and latency. Requires new validated embedded processing architecture. | `[D]` |
| 2 | Reliable medical emergency detection and classification using contactless sensors under vehicle motion and variable lighting | **YES** | A-009 is A3. No validated system demonstrated. Requires new empirical knowledge about contactless biometric reliability under vehicle-condition motion. | `[D]` |

**BDI = 2 — HIGH-RISK ARCHITECTURE** `[D]`

`[D]` BDI ≥ 2 — justification required:

Breakthrough 2 (medical emergency detection) is dependent on Breakthrough 1 (fusion latency) — reliable medical classification requires all biometric streams delivered within the latency window. Breakthrough 1 is a necessary precondition for Breakthrough 2. Research pre-phase must address fusion latency first. Sequencing is fixed by constraint, not preference.

### BDI Hard Halt Assessment

`[D]` Pre-scope-reduction BDI = 4 — Hard halt triggered. Scope reduction executed. Post-scope-reduction BDI = 2 — Hard halt cleared. Component proceeds.

### BDI-Assumption Integrity Check

*Triggered: A4 assumptions present (A-011, A-012) AND Instability_ratio pre-reduction = 0.33 > 0.20.*

*Note: A-011 and A-012 travel with AV-UBI-002C after scope reduction. Active A4 assumptions post-reduction: none.*

**A-009 reviewed (A3, Instability_ratio triggered):**
> "Camera-based rPPG achieves sufficient accuracy for medical emergency detection under vehicle motion and variable lighting"

- Condition (a): Requires genuinely new empirical knowledge? **YES** — vehicle-condition validation does not exist.
- Condition (b): Never-demonstrated capability? **YES** — no production demonstration under these conditions.

→ Confirmed as breakthrough requirement. Already counted as BDI item 2. No increment needed.

**A-010 reviewed (A3, Instability_ratio triggered):**
> "8-stream continuous fusion at 150–175ms achievable without thermal throttling in automotive-grade embedded hardware"

- Condition (a): Requires genuinely new empirical knowledge? **YES** — sustained operation at this density undemonstrated.
- Condition (b): Never-demonstrated capability? **YES** — no production-grade demonstration exists.

→ Confirmed as breakthrough requirement. Already counted as BDI item 1. No increment needed.

**4.6D Output:** All speculative assumptions correctly mapped to BDI items. No concealed breakthroughs. BDI = 2 confirmed. `[D]`

---

## SECTION 9 — DEPENDENCY TRANSPARENCY GRID

`[D]` All eight fields declared. No hidden dependencies permitted.

| FIELD | CONTENT |
|-------|---------|
| **Inputs** | Stream 1: Infrared eye tracking — driver + front passenger · Stream 2: Head position and movement — all occupied seats · Stream 3: Steering wheel capacitive grip pressure — driver · Stream 4: Seat pressure distribution — all seats · Stream 5: Camera-based rPPG biometric — all occupied seats · Stream 6: Cabin microphone vocalization — cabin-wide · Stream 7: Seat occupancy detection — all seats · Stream 8: CO2/air quality — cabin-wide · Individual occupant baseline profiles (established within session or declared via Session Priming) |
| **Outputs** | PRIMARY: Confidence score [0.00–1.00] per occupant · SECONDARY: State classification per occupant — READY / DEGRADED / BEHAVIORAL_UNRESPONSIVE / MEDICAL_EMERGENCY · AGGREGATE: Cabin readiness summary + CONSCIOUS_OCCUPANT_PRESENT (YES/NO) · FAILSAFE: UNRESPONSIVE default if output not produced within 175ms |
| **Energy source** | Computational — onboard embedded processing via parallel pipeline architecture; no independent physical energy dependency beyond vehicle power |
| **Control dependencies** | Governed by individual occupant baseline profiles · Governed by stream health monitor — degraded stream triggers confidence adjustment · Governed by disambiguation timer — BEHAVIORAL_UNRESPONSIVE escalates to MEDICAL_EMERGENCY_SUSPECTED after 15–20 seconds without recovery signal · Governed by asymmetric error cost thresholds — MEDICAL_EMERGENCY threshold set lower than BEHAVIORAL_UNRESPONSIVE to reflect fatal cost of false negative |
| **Environmental exposure** | Variable cabin lighting affecting rPPG accuracy · Vehicle motion and vibration affecting all stream accuracy · Temperature affecting capacitive grip detection · Occupant variation — sunglasses defeating eye tracking · Variable occupant count 1–5 · Adverse weather affecting cabin sensor conditions |
| **Maintenance requirements** | Sensor stream calibration per vehicle platform · rPPG baseline recalibration if cabin lighting configuration changes · Grip sensor recalibration for seasonal temperature variation · Occupant baseline profiles cleared between sessions unless explicit Session Priming carry-forward declared · Stream health thresholds require re-validation if hardware changes |
| **Upstream reliance** | All eight sensor streams must be operational at session start · Embedded processing hardware must be within thermal operating range · Seat occupancy detection must correctly identify occupied seats before classification begins · Individual baseline establishment must complete within 60–90 seconds before full classification reliability is achieved |
| **Downstream impact** | AV-UBI-001 receives all outputs — primary consumer of readiness classification · AV-UBI-004 emergency routing receives MEDICAL_EMERGENCY signal · AV-UBI-002B receives CONSCIOUS_OCCUPANT_PRESENT signal for detailed capability assessment · Session logging and incident reporting receives full classification record including stream health states at time of each classification |

---

## SECTION 10 — INVALIDATION CONDITIONS

`[D]` This component is invalid if:

1. 8-stream sensor fusion within 150–175ms is demonstrated to be physically incompatible with automotive-grade embedded processing under sustained operation — meaning thermal or computational limits make the latency target unachievable without hardware not deployable in production vehicles `[D]`

2. Camera-based rPPG is demonstrated to be insufficient for medical emergency detection under vehicle motion conditions regardless of algorithm improvement — meaning the physics of contactless biometric detection under motion precludes reliable cardiac event identification `[D]`

3. The four-state classification output (READY / DEGRADED / BEHAVIORAL_UNRESPONSIVE / MEDICAL_EMERGENCY) is demonstrated to be insufficient — meaning real occupant states exist that none of the four classifications correctly captures, producing systematically wrong signals to AV-UBI-001 `[R]`

4. Individual occupant baseline establishment within 60–90 seconds is demonstrated to be insufficient for accurate classification — meaning reliable state detection requires longer baseline periods than the operational window allows `[R]`

5. The FAILSAFE default-to-UNRESPONSIVE is demonstrated to produce unacceptable false MRC activation rates in normal operation — meaning the failsafe itself creates a safety problem worse than the failure it prevents `[S]`

---

## SECTION 11 — VALIDATION LEVEL

**Validation Level: CONCEPTUAL**

`[D]` This component specification is logically consistent with its stated constraint set and internally consistent with AV-UBI-001 interface requirements. It has not been tested against physical or operational reality. Two breakthrough requirements remain unresolved. The classification architecture is specified but not simulated or experimentally validated.

| LEVEL | STATUS |
|-------|--------|
| Conceptual | ✓ CURRENT — logically consistent |
| Physics-Consistent | Pending — requires BDI item 1 resolution (fusion latency) first |
| Simulation-Ready | Pending — requires Physics-Consistent validation |
| Experimentally Validated | Pending |
| Production-Grade | Pending |

---

## SECTION 12 — VERSION SUMMARY

| FIELD | VALUE |
|-------|-------|
| **Domain ID** | AV-UBI-002 |
| **Component** | Cabin occupant readiness classification |
| **BDI Class** | HIGH-RISK ARCHITECTURE (BDI = 2, reduced from 4) |
| **Validation Level** | CONCEPTUAL |
| **High Instability Flag** | CLEARED post-reduction (ratio: 0.20 — monitor at next version) |
| **Sponsor Authorization** | Not required — BDI < 3 post-reduction |
| **4.6D Check** | EXECUTED — no concealed breakthroughs found |
| **Scoped-out components** | AV-UBI-002B (conscious passenger capability) · AV-UBI-002C (choking/seizure classification) |
| **Open Breakthrough Requirements** | (1) 8-stream fusion at 150–175ms in automotive-grade hardware · (2) Contactless medical emergency detection under vehicle conditions |
| **Primary cascade risk** | Layer 4 → AV-UBI-001 incorrect decision — MEDICAL_EMERGENCY classified as BEHAVIORAL_UNRESPONSIVE — HIGH probability if rPPG stream degraded |
| **Novel architectural contribution** | Disambiguation timer — time-bounded escalation from BEHAVIORAL_UNRESPONSIVE to MEDICAL_EMERGENCY_SUSPECTED after 15–20 seconds without recovery signal. No current production system implements this. |
| **Interface dependency** | AV-UBI-001 must treat null output and UNRESPONSIVE output identically — must be hardwired in AV-UBI-001 |
| **FCL Entries** | 0 — specification complete, empirical validation pending |
| **Next version trigger** | Research pre-phase session closing BDI item 1 (fusion latency) OR first FCL entry from sensor stream testing |

---

## SECTION 13 — COMPONENT STACK POSITION

`[D]` AV-UBI-002 occupies the following position in the AV-UBI specification stack:

```
AV-UBI-001 — Operational envelope decision logic
     ↑
     Receives from: AV-UBI-002 (THIS COMPONENT)

AV-UBI-002 — Cabin occupant readiness classification (THIS COMPONENT)
     ↑
     Receives from: 8 sensor streams (upstream hardware)
     ↓
     Sends to: AV-UBI-001 — full classification output package
     Sends to: AV-UBI-004 — MEDICAL_EMERGENCY signal
     Sends to: AV-UBI-002B — CONSCIOUS_OCCUPANT_PRESENT signal

DOWNSTREAM DEPENDENT SESSIONS:
AV-UBI-002B — Conscious passenger capability detection
  (receives CONSCIOUS_OCCUPANT_PRESENT from this component)
AV-UBI-002C — Choking and seizure classification
  (extends this component's classification state space)
AV-UBI-003 — Reaction-latency / decision-cycle gap resolution
  (addresses AV-UBI-001 BDI item 2)
AV-UBI-004 — Emergency routing and services contact decision logic
  (receives MEDICAL_EMERGENCY signal from this component
   via AV-UBI-001)
```

---

## SECTION 14 — OPEN ACTIONS

| ACTION | PRIORITY | TRIGGER |
|--------|----------|---------|
| Confirm AV-UBI-001 hardwires null output = UNRESPONSIVE in next version update | CRITICAL | Immediate — interface dependency |
| Design research pre-phase session for BDI item 1 (8-stream fusion latency) | HIGH | Next session |
| Design research pre-phase session for BDI item 2 (rPPG under vehicle motion) | HIGH | After BDI item 1 session |
| Open AV-UBI-002B session (conscious passenger capability) | MEDIUM | After core component advances to Physics-Consistent |
| Open AV-UBI-002C session (choking/seizure classification) | MEDIUM | After core component advances to Physics-Consistent |
| Re-audit Instability_ratio at next version — sitting at threshold 0.20 | LOW | Next version open |
| First FCL entry from sensor stream testing | HIGH | Hardware testing available |

---

*AV-UBI-002 v1.0 — Cabin Occupant Readiness Classification*
*CDIP v1.5 | ECF v0.5 | LAV v1.5 | FSVE v3.5*
*BDI = 2 — HIGH-RISK ARCHITECTURE (reduced from 4) | Validation: CONCEPTUAL*
*Session complete. No expansion permitted without new DST.*

*Novel contribution: Disambiguation timer — time-bounded escalation from BEHAVIORAL_UNRESPONSIVE to MEDICAL_EMERGENCY_SUSPECTED. First formal specification of cabin-wide multi-occupant readiness classification with hybrid graduated/categorical output and automatic failsafe.*

*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Co-Architect: Claude (Anthropic) | February 2026*
*Open-source specification — no prior version required*
