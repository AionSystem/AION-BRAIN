# DECISION ENGINE v1.0 — POLYMATH MASTERMIND EDITION

**Codename:** DECIDERE — Personal Decision Analysis Framework  
**Author:** Sheldon K. Salmon (Mr. AION)  
**Classification:** TIER 1 — FOUNDATION  
**Release:** v1.0 — Production Specification (Polymath Integrated)  
**Date:** November 2025  
**Status:** Production-Ready | Open Source (Attribution Required)

---

## 1. EXECUTIVE SUMMARY

The Decision Engine v1.0 is a foundational cognitive framework that transforms chaotic, emotionally-charged life decisions into structured, multi-framework analysis with explicit confidence calibration. It integrates five specialized frameworks from CEREBRO v3.5 to provide comprehensive decision support for major life choices.

### Core Innovation
Where traditional decision-making relies on intuition (often biased), Decision Engine provides:
- **Bias Detection:** Catch hidden cognitive traps (Kahneman)
- **Satisficing:** Define "good enough" to stop overthinking (Simon)
- **Antifragility:** Test if decision survives stress (Taleb)
- **Temporal Intelligence:** Assess if NOW is optimal (Bergson)
- **Ethical Validation:** Ensure fairness to all stakeholders (Rawls/Singer)

### Tier Classification Rationale
Decision Engine is classified as **Tier 1 — Foundation** because:
- Decision-making is a *fundamental* cognitive operation, not a domain specialization
- It provides a foundational capability that other engines can leverage
- Like LBE (linguistic normalization) and CPP (contamination prevention), it's a basic building block
- It doesn't analyze a specific domain—it applies to ANY decision domain

---

## 2. ARCHITECTURE OVERVIEW

### 2.1 Five-Framework Integration

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  DECISION ENGINE v1.0 ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    USER DECISION QUERY                          │   │
│  │        "Should I quit my job to start a business?"              │   │
│  └─────────────────────────────┬───────────────────────────────────┘   │
│                                │                                        │
│                                ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              WORD ENGINE v2.2 (Query Bias Audit)                │   │
│  │        Detect hidden assumptions, emotional loading             │   │
│  └─────────────────────────────┬───────────────────────────────────┘   │
│                                │                                        │
│         ┌──────────────────────┼──────────────────────┐                │
│         ▼                      ▼                      ▼                │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐            │
│  │  KAHNEMAN   │      │   SIMON     │      │   TALEB     │            │
│  │   (Bias)    │      │ (Satisfice) │      │(Antifragile)│            │
│  └──────┬──────┘      └──────┬──────┘      └──────┬──────┘            │
│         │                    │                    │                    │
│         └──────────────────┬─┴────────────────────┘                    │
│                            │                                           │
│         ┌──────────────────┼──────────────────────┐                    │
│         ▼                  ▼                      ▼                    │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐            │
│  │  BERGSON    │      │RAWLS/SINGER │      │  SYNTHESIS  │            │
│  │  (Timing)   │      │  (Ethics)   │      │   MODULE    │            │
│  └──────┬──────┘      └──────┬──────┘      └──────┬──────┘            │
│         │                    │                    │                    │
│         └────────────────────┴────────────────────┘                    │
│                              │                                         │
│                              ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │           ORACLE LAYER v2.1 (Confidence Calibration)           │   │
│  │        Verify convergence, prevent fabrication                  │   │
│  └─────────────────────────────┬───────────────────────────────────┘   │
│                                │                                        │
│                                ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                 FINAL DECISION RECOMMENDATION                   │   │
│  │     IF-THEN Rule + Timeline + Confidence + Next Steps          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Parent Engine Integration

| Engine | Role in Decision Engine |
|--------|-------------------------|
| **CEREBRO v3.5** | Provides 5 specialized frameworks (Kahneman, Simon, Taleb, Bergson, Rawls/Singer) |
| **Oracle Layer v2.1** | Confidence calibration, prevents fabricated percentages |
| **Word Engine v2.2** | Detects bias in how user framed the question |
| **Lexical Alchemy v2.1** | Precision in recommendation language |
| **LBE v1.2** | Framework → plain language translation |

### 2.3 Three Operational Modes

| Mode | Duration | Steps | Best For |
|------|----------|-------|----------|
| **QUICK** | 5-10 min | 3 (Bias, Optionality, Ethics) | Fast clarity needed |
| **STANDARD** | 15-20 min | 7 (Full core protocol) | Important decisions |
| **DEEP** | 30-45 min | 9 (+ Word Engine, Cultural Lens, Iteration) | Life-changing decisions |

---

## 3. FRAMEWORK 1: KAHNEMAN — BIAS DETECTION

### 3.1 Purpose
Identify and mitigate cognitive biases that distort decision-making. Based on Daniel Kahneman's behavioral economics research.

### 3.2 Primary Biases Detected

| Bias | Description | Decision Impact |
|------|-------------|-----------------|
| **Anchoring** | Over-relying on first information | Salary anchors expectations |
| **Loss Aversion** | Losses feel 2x worse than gains | Overweight "what I'm giving up" |
| **Availability** | Recent/vivid events weighted more | Friend's success story dominates |
| **Confirmation** | Seek evidence supporting existing view | Cherry-pick supporting data |
| **Overconfidence** | Overestimate own accuracy | "I'm sure this will work" |
| **Status Quo** | Prefer current state | "Better the devil you know" |
| **Sunk Cost** | Continue due to past investment | "I've spent 5 years here" |
| **Planning Fallacy** | Underestimate time/cost | "I'll be profitable in 6 months" |

### 3.3 Pre-Mortem Protocol

**Concept:** Imagine it's 12 months later and the decision FAILED. Why?

**Process:**
1. Mentally fast-forward to failure scenario
2. Generate 5-7 specific failure causes
3. Rank by probability and severity
4. Create mitigation plans for top 3

**Output Example:**
```
PRE-MORTEM: "I quit to start a business and failed"

Failure Causes:
1. Runway depleted before product-market fit (P: 40%, Severity: HIGH)
2. Partner resentment escalated to separation (P: 25%, Severity: CRITICAL)
3. Underestimated competitive response (P: 35%, Severity: MEDIUM)
4. Health issues from stress (P: 20%, Severity: HIGH)
5. Key technical challenge unsolvable (P: 15%, Severity: HIGH)

Mitigations:
1. Extend runway to 24 months OR reduce burn rate 40%
2. Weekly check-ins with partner, explicit escalation protocol
3. Competitive analysis before launch, pivot plan ready
```

### 3.4 Debiasing Strategies

| Bias | Debiasing Strategy |
|------|---------------------|
| Anchoring | Generate alternative anchors (3 different starting points) |
| Loss Aversion | Reframe as "what do I gain?" not "what do I lose?" |
| Availability | Seek statistical base rates, not anecdotes |
| Confirmation | Actively seek disconfirming evidence |
| Overconfidence | Ask "what would need to be true for me to be wrong?" |
| Status Quo | Calculate cost of inaction |
| Sunk Cost | "If I hadn't invested X, would I start now?" |
| Planning Fallacy | Use reference class forecasting |

---

## 4. FRAMEWORK 2: SIMON — SATISFICING

### 4.1 Purpose
Define "good enough" to prevent analysis paralysis. Based on Herbert Simon's bounded rationality research.

### 4.2 The Satisficing Principle

**Key Insight:** Humans cannot optimize perfectly. "Good enough" beats "perfect but never decided."

**Protocol:**
1. Define MINIMUM acceptable outcome (must-haves)
2. Define TARGET outcome (would be great)
3. Define STRETCH outcome (dream scenario)
4. Set decision deadline based on reversibility

### 4.3 Aspiration Level Framework

```
┌─────────────────────────────────────────────────────────────┐
│                    ASPIRATION LEVELS                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STRETCH ─────────────────────────────────────────────────  │
│  │  "Dream scenario" — unlikely but worth pursuing          │
│  │  Example: $500K ARR in Year 1, industry recognition      │
│  │                                                          │
│  TARGET ──────────────────────────────────────────────────  │
│  │  "Would be great" — realistic but ambitious              │
│  │  Example: $150K ARR, sustainable growth, work-life       │
│  │                                                          │
│  MINIMUM ─────────────────────────────────────────────────  │
│  │  "Good enough" — proceed if achieved                     │
│  │  Example: Covers living expenses + 10% savings           │
│  │                                                          │
│  UNACCEPTABLE ────────────────────────────────────────────  │
│     Below minimum — triggers exit/abort                     │
│     Example: Depleted savings, relationship damage          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4.4 Decision Deadline Protocol

| Reversibility | Decision Timeline |
|---------------|-------------------|
| Highly Reversible (can undo easily) | Decide quickly, adjust later |
| Partially Reversible (some cost to undo) | Take reasonable time, set deadline |
| Irreversible (cannot undo) | Thorough analysis, seek external input |

### 4.5 Search Stopping Rules

1. **First-Good-Enough Rule:** Accept first option meeting minimum criteria
2. **Best-of-N Rule:** Evaluate N options, pick best (N ≤ 7 typically)
3. **Time-Bound Rule:** Decide by deadline with best available option
4. **Opportunity Cost Rule:** When search cost > expected improvement, stop

---

## 5. FRAMEWORK 3: TALEB — ANTIFRAGILITY & OPTIONALITY

### 5.1 Purpose
Test if decision survives uncertainty and stress. Based on Nassim Taleb's antifragility research.

### 5.2 Fragility Classification

| Category | Description | Example |
|----------|-------------|---------|
| **FRAGILE** | Breaks under stress | All savings in one stock |
| **ROBUST** | Survives stress unchanged | Diversified index fund |
| **ANTIFRAGILE** | Gets STRONGER under stress | Skills + network that grow from challenge |

### 5.3 Optionality Assessment

**Definition:** Optionality = asymmetric upside. Limited downside, unlimited upside.

**Key Questions:**
1. What's the MAXIMUM I can lose? (Capped?)
2. What's the MAXIMUM I can gain? (Unlimited?)
3. Is the decision REVERSIBLE?
4. Does it CREATE or DESTROY future options?

**Optionality Scoring:**

| Score | Description |
|-------|-------------|
| **HIGH** | Capped downside + unlimited upside + reversible |
| **MEDIUM** | Moderate risk + proportional upside + partially reversible |
| **LOW** | Uncapped downside OR limited upside OR irreversible |

### 5.4 Stress Testing Protocol

**Barbell Strategy Test:**
```
Conservative Side (90%):           Aggressive Side (10%):
├─ Stable income source            ├─ High-risk opportunity
├─ Emergency fund intact           ├─ Startup investment
├─ Core relationships protected    ├─ Career pivot attempt
└─ Health insurance maintained     └─ Geographic experiment
```

**Black Swan Scenarios:**
1. What if the economy crashes 6 months in?
2. What if a key relationship ends?
3. What if health issues arise?
4. What if a competitor emerges?
5. What if the opportunity evaporates?

**Antifragility Test:**
- Does stress DESTROY the decision? → FRAGILE
- Does stress leave it UNCHANGED? → ROBUST
- Does stress make it STRONGER? → ANTIFRAGILE

### 5.5 Via Negativa Principle

**Core Insight:** What you DON'T do is more important than what you DO.

**Application:**
- What can I REMOVE from the decision to reduce risk?
- What commitments should I AVOID?
- What dependencies should I ELIMINATE?

---

## 6. FRAMEWORK 4: BERGSON — TEMPORAL PHASE ASSESSMENT

### 6.1 Purpose
Determine if NOW is the right time for this decision. Based on Henri Bergson's philosophy of time.

### 6.2 Temporal Phases

| Phase | Characteristics | Action Bias |
|-------|-----------------|-------------|
| **GESTATION** | Idea forming, not ready | WAIT |
| **EMERGENCE** | Conditions aligning | PREPARE |
| **RIPENESS** | Optimal moment | ACT NOW |
| **DECAY** | Opportunity fading | ACT IMMEDIATELY or abandon |
| **CLOSURE** | Window closed | ACCEPT, move on |

### 6.3 Temporal Alignment Factors

**External Factors:**
- Market conditions (favorable/unfavorable)
- Economic cycle (expansion/recession)
- Industry timing (early/mature/declining)
- Regulatory environment (stable/changing)
- Technological readiness (premature/optimal/obsolete)

**Internal Factors:**
- Personal readiness (skills, experience, confidence)
- Financial position (runway, obligations, flexibility)
- Relationship stability (support system)
- Health and energy (sustainable effort capacity)
- Emotional state (clarity vs. reactive)

### 6.4 Temporal Decision Matrix

```
                    INTERNAL READINESS
                    LOW         HIGH
                ┌───────────┬───────────┐
         HIGH   │   WAIT    │  ACT NOW  │
EXTERNAL        │  Prepare  │  Optimal  │
ALIGNMENT       │  yourself │  moment   │
                ├───────────┼───────────┤
         LOW    │   WAIT    │   WAIT    │
                │  Both not │  External │
                │  aligned  │  not ready│
                └───────────┴───────────┘
```

### 6.5 Kairos vs. Chronos

**Chronos:** Linear, measurable time (deadlines, schedules)  
**Kairos:** Qualitative, opportune time (the right moment)

**Protocol:**
1. What does CHRONOS say? (Calendar deadlines, biological clock, market windows)
2. What does KAIROS say? (Does this FEEL like the right moment?)
3. If they conflict, which dominates? (Usually Chronos for external, Kairos for internal)

---

## 7. FRAMEWORK 5: RAWLS/SINGER — ETHICAL VALIDATION

### 7.1 Purpose
Ensure decision is fair to all stakeholders. Based on John Rawls' justice theory and Peter Singer's utilitarianism.

### 7.2 Stakeholder Mapping

| Category | Examples |
|----------|----------|
| **Direct Beneficiaries** | You, customers, partners |
| **Direct Losers** | Employer, competitors, replaced workers |
| **Indirect Affected** | Family, community, ecosystem |
| **Voiceless** | Future generations, children, animals, environment |

### 7.3 Veil of Ignorance Test (Rawls)

**Concept:** Would you design this outcome if you didn't know which stakeholder you'd be?

**Protocol:**
1. List all stakeholders affected
2. Identify the LEAST ADVANTAGED stakeholder
3. Ask: "Does this decision protect the worst-off?"
4. If NO: Can it be redesigned to protect them?

**Example:**
```
Decision: Quit job to start business

Least Advantaged: Your children (income instability risk)

Veil of Ignorance Test:
"If I didn't know whether I'd be the entrepreneur (upside) or the child
(downside), would I design this outcome?"

Result: PASSES if children's education fund is protected AND
        health insurance maintained AND exit plan exists
```

### 7.4 Utilitarian Calculus (Singer)

**Formula:** Total Benefits - Total Harms = Net Utility

**Scoring Approach:**
1. Assign utility units to each stakeholder impact
2. Weight by probability of occurrence
3. Calculate net utility

**Example:**
```
Benefits:
├─ You: +100 (life transformation, purpose, growth)
├─ Future customers: +30 (problem solved)
├─ Ecosystem: +10 (innovation, jobs created)
└─ Total: +140

Harms:
├─ Family: -40 (short-term stress, uncertainty)
├─ Employer: -15 (replacement cost, transition)
├─ Coworkers: -10 (workload redistribution)
└─ Total: -65

Net Utility: +75 (POSITIVE)
Confidence: MEDIUM (depends on success probability)
```

### 7.5 Moral Circle Expansion (Singer)

| Scope | Considers |
|-------|-----------|
| **NARROW** | Self + immediate family only |
| **MODERATE** | Close community, foreseeable future |
| **EXPANSIVE** | Future generations, global impact, environment |

**Challenge:** Can you widen your circle? What would change?

### 7.6 Ethical Verdict

| Verdict | Criteria |
|---------|----------|
| **JUST ✅** | Passes Veil of Ignorance + Positive Net Utility + Moderate+ Moral Circle |
| **PROBLEMATIC ⚠️** | Fails one test but fixable |
| **UNJUST ❌** | Fails multiple tests, fundamental concerns |

---

## 8. STEP 0: WORD ENGINE QUERY AUDIT (DEEP MODE)

### 8.1 Purpose
Detect hidden assumptions and biases in how the user framed the decision question.

### 8.2 Seven-Lens Analysis

| Lens | What It Detects |
|------|-----------------|
| **Linguistic** | Binary framing, passive voice, absolute language |
| **Cognitive** | Concept clusters activated (identity, fear, status) |
| **Cultural** | Cultural valence (startup culture, family expectations) |
| **Contextual** | Recent life events influencing framing |
| **Directional** | Unconscious steering (seeking permission vs. genuine inquiry) |
| **Emotional** | Fear, excitement, resignation in framing |
| **Risk** | Hallucination triggers (absolutes, binaries) |

### 8.3 Query Reframing Protocol

**Original Query:** "Should I quit my stable job to start a risky business?"

**Analysis:**
- Linguistic: Binary framing + loaded language ("stable" vs "risky")
- Emotional: Fear-dominant (emphasizing risk, not opportunity)
- Hidden Assumption: Job = safety, Business = danger (may be false)
- Directional: Seeking permission to stay (not genuine exploration)

**Reframed Query:** "What conditions would justify transitioning from employment to entrepreneurship, and what's my validation timeline?"

---

## 9. CULTURAL LENS OPTIONS (DEEP MODE)

### 9.1 Available Cultural Perspectives

| Culture | Emphasis |
|---------|----------|
| **Confucian** | Family harmony, filial piety, collective over individual |
| **Daoist** | Wu wei (effortless action), flow, natural timing |
| **Ubuntu** | "I am because we are" — community interdependence |
| **Indigenous** | Seven generations thinking, land connection |
| **Islamic Tawhid** | Unity, stewardship, submission to higher purpose |

### 9.2 Cultural Lens Application

**Example: Confucian Lens on Career Decision**
```
Standard Western Analysis: "What's best for MY career growth?"

Confucian Reframe:
├─ How does this affect family harmony?
├─ What do I owe to parents who sacrificed for me?
├─ Does this bring honor or shame to family name?
├─ Am I prioritizing individual desire over collective good?
└─ How would a virtuous person (junzi) decide?

Conclusion: May prioritize stability + family security over
            individual ambition, or frame ambition AS family service
```

---

## 10. CONFIDENCE CALIBRATION

### 10.1 Convergence Scoring

| Confidence | Criteria |
|------------|----------|
| **HIGH** | 4-5 frameworks independently agree |
| **MEDIUM** | 2-3 frameworks converge |
| **LOW** | Single framework or unresolved contradictions |
| **VERY LOW** | Insufficient data, frameworks in conflict |

### 10.2 Oracle Layer Integration

**Epistemic Safeguards:**
- Never fabricate confidence percentages
- Explicitly state "What I Cannot Know" (Gödelian limits)
- Recommend external validation when needed
- All recommendations are probabilistic, not deterministic

### 10.3 External Validation Triggers

Recommend external expert consultation when:
- Decision involves technical expertise (medical, legal, financial)
- Confidence remains LOW after full analysis
- Stakes are irreversible AND high
- Frameworks remain in unresolved conflict

---

## 11. OUTPUT FORMAT SPECIFICATION

### 11.1 Quick Mode Output

```
═══════════════════════════════════════════
⚡ QUICK ANALYSIS COMPLETE
═══════════════════════════════════════════

Decision: [User's decision restated]

Bias Detected: [Primary bias identified]
Debiasing: [One-line correction]

Reversibility: [HIGH | MEDIUM | LOW]
Optionality: [Creates options | Destroys options | Neutral]

Ethics Check: [PASSES | FAILS] + one-line reason

RECOMMENDATION: [PROCEED | WAIT | DECLINE | NEED MORE INFO]

Confidence: [HIGH | MEDIUM | LOW]
Missing Info: [What would raise confidence]

═══════════════════════════════════════════
```

### 11.2 Standard Mode Output

```
═══════════════════════════════════════════
🎯 STANDARD ANALYSIS COMPLETE
═══════════════════════════════════════════

[7-step analysis summary]

═══════════════════════════════════════════
FINAL RECOMMENDATION
═══════════════════════════════════════════

Decision Rule:
IF [condition 1]
AND [condition 2]
AND [condition 3]
THEN: [Action]
ELSE: [Alternative]

Timeline: [IMMEDIATE | WAIT X DAYS | WAIT FOR TRIGGER]
Confidence: [HIGH | MEDIUM | LOW]
Frameworks Aligned: [X/5]

Next Steps:
1. [Immediate action]
2. [Second priority]
3. [Third priority]

═══════════════════════════════════════════
```

### 11.3 Deep Mode Output

Full report including:
- Word Engine query audit
- Cultural lens analysis (if selected)
- Complete 7-step protocol
- Expected value calculation
- Iterative refinement notes
- 8-page comprehensive decision report

---

## 12. DECISION DOMAINS

### 12.1 Supported Decision Types

| Category | Examples |
|----------|----------|
| **Career** | Quit job, start business, switch fields, accept offer |
| **Relationship** | Commitment, breakup, marriage, children |
| **Location** | Relocate, buy house, emigrate |
| **Financial** | Major investment, education, property |
| **Life Transition** | Retirement, major pivot, health decisions |

### 12.2 NOT Ideal For

- Small daily choices (what to eat, what to wear)
- Already-made decisions seeking validation
- Decisions requiring domain expertise (medical diagnosis, legal strategy)
- Urgent emergencies requiring immediate action

---

## 13. LIMITATIONS & APPROPRIATE USE

### 13.1 What Decision Engine CANNOT Do

- ❌ Make the decision FOR you (only structures thinking)
- ❌ Guarantee outcomes (all decisions involve uncertainty)
- ❌ Provide medical, legal, or financial advice
- ❌ Predict the future (assesses likelihood, not certainty)
- ❌ Read your mind (quality depends on info provided)

### 13.2 What Decision Engine CAN Do

- ✅ Catch biases you're blind to
- ✅ Structure chaotic thinking into clear decision rules
- ✅ Tell you if NOW is the right time (or when to wait)
- ✅ Check if decision is reversible (optionality)
- ✅ Make sure you've considered who gets hurt/helped
- ✅ Give confidence levels so you know when to seek more info

---

## 14. VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | November 2025 | Initial production release, 5 frameworks, 3 modes |

---

## 15. CITATION

```bibtex
@software{salmon2025decision,
  author = {Salmon, Sheldon K.},
  title = {Decision Engine v1.0: DECIDERE},
  year = {2025},
  version = {1.0},
  organization = {AION-BRAIN},
  classification = {Tier 1 - Foundation},
  license = {Open Source (Attribution Required)}
}
```

---

**Document Classification:** PRODUCTION SPECIFICATION  
**Engine Status:** Production-Ready | Open Source  
**Last Updated:** November 2025  
**Author:** Sheldon K. Salmon (Mr. AION)
