# Layer 1: Risk Detection Module

**Priority:** Critical
**Function:** Immediate identification of life-threatening indicators

---

## Purpose

This module continuously monitors for indicators of imminent risk requiring immediate professional intervention. It serves as the first line of safety in all crisis/grief interactions.

---

## Detection Categories

### 1.1 Suicide Risk Indicators

| Indicator Type | Examples | Risk Weight |
|----------------|----------|-------------|
| **Ideation** | "I want to die," "I can't go on" | High |
| **Plan** | Specific method, location, time | Critical |
| **Means** | Access to lethal means | Critical |
| **Intent** | "I'm going to do it" | Critical |
| **Timeline** | "Tonight," "This week" | Critical |
| **Preparation** | Giving away possessions, goodbye notes | Critical |
| **Resolution** | Sudden calm after prolonged crisis | High |

### 1.2 Homicide Risk Indicators

| Indicator Type | Examples | Risk Weight |
|----------------|----------|-------------|
| **Identified Target** | Named person or group | Critical |
| **Stated Intent** | "I'm going to hurt them" | Critical |
| **Plan Details** | How, when, where | Critical |
| **Means Access** | Weapons, opportunity | Critical |
| **Escalating Threats** | Increasing severity | High |

### 1.3 Self-Harm Indicators

| Indicator Type | Examples | Risk Weight |
|----------------|----------|-------------|
| **Active Self-Injury** | Current or recent cutting, burning | High |
| **Escalating Behavior** | Increasing severity or frequency | High |
| **Life-Threatening Methods** | Overdose, asphyxiation | Critical |
| **Lack of Control** | "I can't stop" | High |

### 1.4 Vulnerable Person Indicators

| Indicator Type | Examples | Risk Weight |
|----------------|----------|-------------|
| **Child Abuse/Neglect** | Disclosed or suspected | Critical |
| **Elder Abuse** | Physical, financial, emotional | Critical |
| **Dependent Adult Abuse** | Exploitation, neglect | Critical |
| **Domestic Violence** | Current danger situation | Critical |

---

## Risk Classification Output

### Imminent Risk
```
⚠️ IMMINENT RISK DETECTED
-------------------------
Indicator: [Specific finding]
Classification: IMMINENT
Required Action: IMMEDIATE PROFESSIONAL INTERVENTION
Escalation: MANDATORY
Emergency Services: CONSIDER 911/988

Do NOT continue without addressing safety.
```

### High Risk
```
⚠️ HIGH RISK DETECTED
---------------------
Indicator: [Specific finding]
Classification: HIGH
Required Action: Same-session safety planning
Escalation: Supervisor notification recommended
Follow-up: Within 24-48 hours required
```

### Moderate Risk
```
MODERATE RISK NOTED
-------------------
Indicator: [Specific finding]
Classification: MODERATE
Required Action: Safety planning discussion
Follow-up: Schedule within 1 week
Monitoring: Increased attention to indicators
```

### Low Risk
```
LOW RISK ASSESSMENT
-------------------
Current Status: No immediate concerns
Protective Factors: [List identified factors]
Monitoring: Standard care protocols
Reassessment: Periodic check-ins
```

---

## Protective Factors Assessment

Always assess alongside risk:

| Category | Factors |
|----------|---------|
| **Internal** | Reasons for living, future orientation, coping skills |
| **External** | Social support, family connection, treatment engagement |
| **Spiritual** | Religious beliefs, meaning, purpose |
| **Practical** | Housing, employment, stability |

---

## Warning Sign Patterns

### Acute Warning Signs (Immediate)
- Threatening to hurt or kill self
- Looking for ways to kill self
- Talking or writing about death/dying/suicide
- Hopelessness
- Rage, anger, seeking revenge
- Acting reckless or engaging in risky activities
- Feeling trapped
- Increasing alcohol or drug use
- Withdrawing from friends, family, society
- Anxiety, agitation, unable to sleep or sleeping all the time
- Dramatic mood changes
- No reason for living, no sense of purpose

### Chronic Risk Factors
- Previous suicide attempt
- Family history of suicide
- Chronic pain or illness
- Recent loss
- Access to lethal means
- Social isolation
- Substance abuse
- Mental health condition

---

## Integration Requirements

This module MUST run before all other processing in crisis contexts.

When risk is detected at IMMINENT or HIGH level:
1. Halt standard processing
2. Display risk alert
3. Provide intervention guidance
4. Require human decision before proceeding
5. Document detection and response

---

## Limitations

This module:
- Supports but does not replace clinical judgment
- Cannot detect concealed or minimized risk
- Requires honest disclosure to function
- Must be combined with professional assessment
- Is not a substitute for training

---

*Every indicator detected is a signal, not a diagnosis. Professional judgment remains essential.*
