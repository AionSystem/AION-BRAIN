# Case 001: Crisis Hotline Call Support

**Category:** Crisis Intervention
**Complexity:** Critical
**Modules Activated:** Risk Detection, Safety Planning, Professional Boundaries

---

## Scenario

A crisis counselor at a suicide prevention hotline receives a call from a person expressing suicidal thoughts. The caller states they have been thinking about ending their life after losing their job last month. The counselor uses Crisis & Grief Engine to support their intervention while maintaining full human control of the interaction.

---

## ⚠️ CRITICAL SAFETY FRAMEWORK

This use case demonstrates ENGINE SUPPORT for trained crisis counselors.

**The engine does NOT:**
- Replace the counselor's judgment
- Communicate directly with the caller
- Make autonomous decisions about risk level
- Determine whether to dispatch emergency services

**The engine DOES:**
- Provide structured assessment frameworks
- Remind counselors of key intervention elements
- Support documentation requirements
- Offer evidence-based prompts

---

## Initial Call Information

```
INCOMING CALL INFORMATION
=========================
Call ID: [Encrypted identifier]
Call Start: [Timestamp]
Initial Presentation: Caller states "I've been thinking about ending it"
Counselor: [Counselor ID]

IMMEDIATE CHECKLIST:
□ Establish rapport - ACTIVE
□ Assess for immediate danger - PENDING
□ Engage listening and validation - ACTIVE
```

---

## Engine-Supported Risk Assessment

### During Call - Assessment Support

```
<CRISIS_ENGINE_v1.0>
<MODE: CRISIS_HOTLINE>
<MODULE: RISK_DETECTION>

REAL-TIME ASSESSMENT SUPPORT
============================
[Counselor completes assessment; engine provides framework]

RISK FACTOR EXPLORATION:
========================
Suicidal Ideation:
□ Passive ("wish I wasn't here"): ____
□ Active ("thinking about killing myself"): ____
□ Frequency: ____
□ Duration: ____

If active ideation present:
□ Plan: [Yes/No] If yes, specifics: ____
□ Means access: [Yes/No] Type: ____
□ Intent: [1-10 scale or description]: ____
□ Timeline: ____

Protective Factors:
□ Reasons for living identified: ____
□ Support system: ____
□ Future orientation: ____
□ Help-seeking (calling now): YES ✓

Precipitating Event:
□ Recent loss/stressor: Job loss - 1 month ago
□ Anniversary/trigger: ____
□ Substance use (current): ____

Risk Assessment Conclusion: [Counselor determines]
</CRISIS_ENGINE_v1.0>
```

### Risk Level Framework (Counselor Reference)

```
RISK LEVEL GUIDANCE
===================
[Counselor uses clinical judgment with this framework]

IMMINENT RISK INDICATORS:
- Active plan with specific method
- Access to means
- Stated intent with timeline
- Prior attempt(s) especially recent
- Intoxication with ideation
- Acute agitation
- Expressed intent to act today

HIGH RISK INDICATORS:
- Active ideation with some planning
- Access to means (not secured)
- Limited protective factors
- Recent suicide attempt
- Acute hopelessness
- Significant psychiatric symptoms

MODERATE RISK INDICATORS:
- Active ideation without plan
- Some protective factors present
- Support system available
- Willing to engage in safety planning
- Future orientation present

LOWER RISK INDICATORS:
- Passive ideation only
- Strong protective factors
- Good support system
- Help-seeking behavior
- No plan or intent
- Willing to use coping strategies

⚠️ These are guidelines. Clinical judgment takes precedence.
Any concern about imminent danger should trigger appropriate response.
```

---

## Intervention Support

### De-escalation Prompts

```
DE-ESCALATION SUPPORT
=====================
[Counselor selects and adapts as appropriate]

VALIDATION STATEMENTS:
"It sounds like you've been carrying a lot since losing your job."
"Thank you for calling and sharing this with me."
"What you're going through sounds really painful."

COLLABORATIVE ENGAGEMENT:
"I'm glad you reached out. Let's figure out together how to get through tonight."
"You took an important step by calling. That tells me part of you wants to find another way."

HOPE-ORIENTED (use cautiously, not dismissively):
"Many people who have been where you are have found their way through."
"Let's talk about what has helped you get through hard times before."

⚠️ AVOID:
- Minimizing ("It's not that bad")
- Problem-solving too quickly
- Demanding promises
- Expressing shock or judgment
- Religious/philosophical arguments (unless client-initiated)
```

### Safety Planning Support (During Call)

```
SAFETY PLANNING ELEMENTS
========================
[For calls where safety planning is appropriate]

BRIEF SAFETY PLAN FRAMEWORK:
1. Warning signs we discussed: [Counselor notes]
2. Coping strategies that work for you: [Client-generated]
3. People you can reach out to: [Client-generated]
4. Professional resources:
   - Your therapist/counselor: ____
   - This crisis line: 988 (24/7)
   - Local crisis team: ____
   - Emergency room: ____
5. Making your environment safer tonight: [Specific plan]

MEANS RESTRICTION:
"You mentioned [method]. Can we talk about putting some distance between you and that tonight?"
Options to explore:
- Give to someone else
- Lock in car
- Remove from home
- Other barriers

FOLLOW-UP:
□ Permission to follow up: [Yes/No]
□ Preferred time/method: ____
□ Other professional involved: ____
```

---

## Call Resolution

### Documentation Support

```
CALL DOCUMENTATION
==================
Call End: [Timestamp]
Duration: [Minutes]
Counselor: [ID]

CALLER PRESENTATION:
Presenting issue: Suicidal ideation after job loss
Current ideation: [Counselor assessment]
Plan: [Counselor assessment]
Means: [Counselor assessment]
Intent: [Counselor assessment]
Risk Level Assessed: [Counselor determination]

INTERVENTION:
□ Active listening and validation
□ Risk assessment completed
□ Safety planning: [Yes/No/Partial]
□ Means restriction discussed: [Yes/No]
□ Resources provided: [List]
□ Emergency services dispatched: [Yes/No]
□ Warm transfer made: [Yes/No - to whom]

DISPOSITION:
□ Caller agreed to safety plan
□ Caller agreed to contact [resources]
□ Follow-up scheduled: [Yes/No - when]
□ Caller declined services/ended call

FOLLOW-UP PLAN:
□ Call-back scheduled: [Date/Time]
□ Notification sent to: [If applicable]
□ Supervisor review: [If required]

COUNSELOR NOTES:
[Free-text for clinical observations]

Counselor Signature: _________________ Date: _________
```

---

## Counselor Self-Care Prompt

```
POST-CALL COUNSELOR CHECK
=========================
[After difficult calls]

□ Take a moment before next call
□ Note any personal reactions
□ Consider: Is supervision or peer support needed?
□ Document any secondary trauma indicators
□ Use available self-care resources

Remember: Supporting people in crisis is demanding work.
Your wellbeing matters.
```

---

## Key Principles Demonstrated

1. **Engine supports, never replaces** — All decisions made by counselor
2. **Frameworks, not scripts** — Counselor adapts to individual
3. **Documentation support** — Reduces burden while ensuring completeness
4. **Safety integration** — Means restriction consistently addressed
5. **Counselor wellbeing** — Secondary trauma awareness

---

## Integration with Engine Architecture

| Layer | Function in This Case |
|-------|----------------------|
| Layer 1 (Risk Detection) | Provides assessment framework |
| Layer 2 (Professional Boundaries) | Scope reminders |
| Layer 4 (Safety Planning) | Safety plan structure |
| Layer 6 (Audit Trail) | Documentation support |

---

## Limitations Acknowledged

- This use case shows professional support, not direct caller interaction
- Engine cannot hear tone of voice or assess non-verbal cues
- All risk assessments require human judgment
- Caller may not be forthcoming; clinical skill essential
- Emergency dispatch decisions are human decisions

---

*This use case demonstrates crisis support workflow. All crisis intervention requires trained professionals with clinical judgment.*
