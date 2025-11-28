# CEREBRO-Lite v1.0 — Practical Examples

## Example 1: Startup Pivot Decision

### Input
```
CEREBRO-LITE ANALYZE:
Subject: Should I pivot my SaaS startup from B2C to B2B?
Context: Current MRR $15K, 200 users, high churn (8%/month), B2B inquiries increasing
Goal: Determine if pivot is strategically sound and identify risks
```

### Output

---

#### [FRAMEWORK 1: MEADOWS — Systems Analysis]

**System Mapping:**
```
STOCKS:
├─ Customer base: 200 users (B2C)
├─ MRR: $15K
├─ Brand equity: Moderate (B2C-focused)
├─ Team capability: Engineering-heavy
└─ Runway: [Depends on burn rate]

FLOWS:
├─ Inflow: New B2C signups (slowing)
├─ Outflow: Churn at 8%/month (critical)
├─ B2B inquiries: Increasing (signal)
└─ Revenue per user: Low (B2C pricing)

FEEDBACK LOOPS:
├─ VICIOUS: High churn → Less revenue → Less development → More churn
├─ POTENTIAL VIRTUOUS: B2B customer → Higher LTV → More resources → Better product → More B2B
└─ CONSTRAINT: B2C brand may limit B2B credibility
```

**Leverage Point Analysis:**
| Level | Intervention | Feasibility |
|-------|--------------|-------------|
| 12 | Adjust pricing | Easy but low impact |
| 7 | Add B2B feedback loop | Medium effort, high impact |
| 5 | Change system rules (target customer) | This is the pivot |
| 3 | Change system goal (growth vs survival) | Strategic choice |

**System Archetype Detected:** Limits to Growth (B2C market saturating) + Opportunity for Shift (B2B signal)

**Meadows Recommendation:** The system is showing clear leverage at Level 5 (change the rules). B2C feedback loop is vicious; B2B loop is potentially virtuous. **Pivot recommended**, but manage transition carefully.

---

#### [FRAMEWORK 2: KAHNEMAN — Bias Detection]

**Biases Detected:**

| Bias | Evidence | Risk Level |
|------|----------|------------|
| **Sunk Cost Fallacy** | Reluctance to abandon 200 B2C users | MEDIUM |
| **Confirmation Bias** | May be overweighting B2B inquiries | MEDIUM |
| **Survivorship Bias** | Looking at successful B2B pivots, ignoring failures | LOW |
| **Optimism Bias** | Underestimating B2B complexity | MEDIUM |
| **Availability Heuristic** | Recent B2B inquiries feel more significant | LOW |

**System 1 vs System 2:**
- Current thinking: System 1 (intuitive excitement about B2B)
- Required: System 2 (deliberate analysis of transition costs)

**Debiasing Recommendations:**
1. Run pre-mortem: "Assume the pivot failed—why?"
2. Seek disconfirming evidence: Talk to B2B rejections, not just inquiries
3. Calculate switching costs explicitly (don't just feel them)
4. Set decision criteria BEFORE gathering more data

**Kahneman Recommendation:** The enthusiasm for pivot may be partially bias-driven. **Validate B2B demand quantitatively** before committing. Interview 10 potential B2B customers about willingness to pay.

---

#### [FRAMEWORK 3: SUN TZU — Strategic Analysis]

**Position Assessment:**

| Factor | B2C Position | B2B Position |
|--------|--------------|--------------|
| Terrain | Crowded, commoditized | Less crowded, higher barriers |
| Resources | Adequate | Stretched (sales team needed) |
| Timing | Late (market mature) | Early-mid (opportunity window) |
| Reputation | Established (weak) | Unestablished |

**Competitive Analysis:**
- B2C: Fighting against funded competitors on their terrain (disadvantage)
- B2B: Potential to establish position before larger players notice

**Strategic Vulnerabilities:**
- Pivot creates temporary weakness (neither B2C nor B2B strength)
- Competitors may attack during transition
- B2B requires sales capability you don't have

**Strategic Opportunities:**
- "Win without fighting": Exit B2C battlefield entirely
- Information advantage: B2B inquiries = market intelligence others lack
- Speed: Small team can pivot faster than large competitors

**Sun Tzu Recommendation:** The current position is weak (fighting uphill in B2C). **Pivot is strategically sound** if executed quickly to minimize vulnerability window. Secure 2-3 B2B customers before announcing pivot publicly.

---

#### [FRAMEWORK 4: PEARL — Causal Inference]

**Causal Hypotheses:**

**Hypothesis 1:** B2C market saturation → Declining growth
```
Evidence: Industry data shows B2C SaaS maturity
Mechanism: Commodity pricing pressure
Confidence: STRONG
```

**Hypothesis 2:** High churn → Revenue pressure
```
Evidence: 8% monthly churn = 96% annual churn (catastrophic)
Mechanism: Product-market fit issues OR wrong market segment
Confidence: STRONG
```

**Hypothesis 3:** B2B inquiries → B2B demand exists
```
Evidence: Increasing inquiries (need quantity data)
Mechanism: Word of mouth OR feature fit for B2B
Confidence: MODERATE (need more data)
```

**Causal Graph:**
```
B2C Market Saturation
         ↓
   Declining Growth ← High Churn
         ↓
   Revenue Pressure
         ↓
 Pivot Consideration ← B2B Inquiries ← ?Product Fit for B2B?
```

**Confounders Identified:**
- Confusing "inquiries" with "demand" (inquiries ≠ willingness to pay)
- Churn might follow to B2B if root cause is product, not market

**Counterfactual Analysis:**
- If you stay B2C: 96% annual churn → likely death in 12-18 months
- If you pivot to B2B: Unknown, but current trajectory is unsustainable

**Pearl Recommendation:** The causal chain from B2C saturation to revenue pressure is STRONG. However, the causal link from B2B inquiries to B2B success is MODERATE. **Validate B2B willingness-to-pay before pivot.**

---

#### [FRAMEWORK 5: TALEB — Anti-Fragility Stress Test]

**Fragility Classification:**

| Component | Classification | Evidence |
|-----------|---------------|----------|
| Current B2C model | FRAGILE | Dies under churn stress |
| Revenue concentration | FRAGILE | 200 users = small base |
| B2B model (proposed) | ROBUST to ANTI-FRAGILE | Fewer, stickier customers |
| Team | ROBUST | Engineering skills transfer |

**Stress Test Results:**

| Scenario | B2C Response | B2B Response |
|----------|--------------|--------------|
| 50% churn spike | Death | Survivable (fewer, stickier) |
| Recession | Cuts hurt (discretionary) | Cuts hurt less (business-critical) |
| New competitor | Crushed (price war) | Defensible (relationships) |
| Key person leaves | Moderate impact | Higher impact (sales) |

**Optionality Audit:**
- Current: LOW optionality (path to death clear)
- Post-pivot: HIGHER optionality (each B2B customer = learning)

**Skin in the Game Check:**
- Founders have skin in the game (their money, time)
- Advisors pushing B2B pivot may not (ask: do they have downside?)

**Via Negativa Recommendations:**
1. REMOVE: Lowest-value B2C customers (free up resources)
2. REMOVE: Features that only B2C needs
3. REMOVE: B2C marketing spend
4. DON'T REMOVE: Core product (reusable for B2B)

**Taleb Recommendation:** Current model is FRAGILE. Pivot to B2B increases anti-fragility. **Recommend pivot**, but use barbell strategy: 90% effort on B2B, 10% maintaining minimal B2C revenue during transition.

---

### [SYNTHESIS]

**Convergent Patterns (STRONG — 5/5 frameworks agree):**
- Current B2C model is unsustainable (churn is fatal)
- Pivot to B2B is directionally correct
- Execution risk is the main concern, not strategic direction

**Divergent Insights (areas of nuance):**
- Kahneman warns of confirmation bias in reading B2B signals
- Pearl notes that "inquiries ≠ validated demand"
- Sun Tzu emphasizes speed to minimize vulnerability window

**Contradictions (none significant):**
- All frameworks point in same direction

**Meta-Pattern:**
The pattern across patterns is: **The question is not WHETHER to pivot, but HOW to de-risk the pivot.** All frameworks agree the current state is terminal; they differ only on how to validate B2B before committing.

---

### [PATTERN DECAY ASSESSMENT]

| Pattern | Domain | Half-Life | Current Confidence |
|---------|--------|-----------|-------------------|
| B2C market saturation | Market dynamics | 12 months | 85% |
| Churn unsustainability | Financial | 6 months | 95% |
| B2B demand signal | Market dynamics | 6 months | 65% |

**Revalidation Schedule:**
- Re-run analysis if B2B validation interviews change picture
- Re-assess in 3 months regardless

---

### [CROSS-DOMAIN BRIDGE]

**Bridge Identified:** Biological immune system → Startup pivot

| Source | Target |
|--------|--------|
| Immune cell apoptosis (programmed death) | Killing B2C business unit |
| Adaptive immunity (learning from threats) | Learning from B2B customers |
| Memory cells (retained knowledge) | Core product/engineering team |

**Bridge Strength:** MODERATE (metaphor useful for framing, not precise execution)

**Insight:** Like an immune system, kill what's not working (B2C) to free resources for adaptation (B2B). Retain "memory" (core capabilities) that work in both contexts.

---

### [RECOMMENDATIONS]

**Priority Actions:**

| Priority | Action | Framework Source |
|----------|--------|-----------------|
| 1 | Interview 10 B2B prospects on willingness-to-pay | Pearl, Kahneman |
| 2 | If validated, secure 2-3 B2B customers quietly | Sun Tzu |
| 3 | Begin B2C wind-down (lowest-value first) | Taleb |
| 4 | Announce pivot only after B2B traction | Sun Tzu |
| 5 | Reallocate engineering to B2B features | Meadows |

**Confidence Level:** STRONG (5/5 frameworks converge on pivot direction)

**Risk Factors to Monitor:**
- B2B validation interviews disconfirm demand
- Key team member resists pivot
- Runway insufficient for transition period

---

### Summary

| Dimension | Assessment |
|-----------|------------|
| Strategic Direction | Pivot to B2B (STRONG confidence) |
| Execution Approach | Validate → Secure customers → Announce |
| Key Risk | Confirmation bias in reading B2B signals |
| Timeline | 3-6 months for validation + early B2B traction |
| Fallback | If B2B doesn't validate, explore acquisition/shutdown |

---

## Example 2: Investment Decision

### Input
```
CEREBRO-LITE ANALYZE:
Subject: Should I invest $50K in a friend's restaurant startup?
Context: Friend has 10 years restaurant experience, prime location secured, 
         seeking $500K total, I'd be 10% investor, no prior restaurant investments
Goal: Determine if investment is sound and identify risks
```

### Abbreviated Output

**[SYNTHESIS]**

**Convergent Patterns (STRONG):**
- Restaurant industry has high failure rates (70% fail in 5 years)
- Personal relationship creates bias risk
- Operator experience is strongest positive signal

**Divergent Insights:**
- Meadows: Look for leverage in location (feedback loop with foot traffic)
- Taleb: Position is FRAGILE (single location, thin margins)
- Pearl: Experience correlates with success but doesn't guarantee it

**Recommendations:**

| Action | Rationale |
|--------|-----------|
| Reduce investment to $25K max | Barbell: limit downside |
| Require business plan with 3-year projections | Pearl: test causal assumptions |
| Include buyback clause | Taleb: create optionality |
| Meet entire team, not just friend | Kahneman: reduce relationship bias |
| Visit comparable restaurants they've managed | Pearl: validate experience claim |

**Confidence:** MODERATE (2-3 frameworks align on caution)

**Key Insight:** The question isn't "Is my friend good?" It's "Does THIS restaurant, in THIS location, with THIS capital structure work?" Separate the person from the business case.

---

## Example 3: Career Decision

### Input
```
CEREBRO-LITE ANALYZE:
Subject: Should I leave my corporate job to join an early-stage startup?
Context: 15 years at Fortune 500, VP level, $300K total comp
         Startup offer: Co-founder/COO role, $150K + 5% equity, Series A
Goal: Evaluate risk/reward and identify decision criteria
```

### Abbreviated Output

**[SYNTHESIS]**

**Convergent Patterns (STRONG):**
- Financial risk is real (50% comp cut + startup failure risk)
- Career optionality increases (startup experience rare at VP level)
- Timing matters (age, family situation, runway)

**Key Frameworks Applied:**

**Meadows:** Corporate career has balancing feedback (stability but ceiling). Startup has reinforcing feedback (success compounds, failure compounds).

**Taleb:** Corporate is ROBUST but not ANTI-FRAGILE. Startup is FRAGILE but offers optionality. Consider barbell: Can you negotiate part-time consulting to maintain income floor?

**Sun Tzu:** Your 15-year corporate experience is competitive advantage in startup world (most startups lack operational rigor). Use it.

**Recommendations:**

| Factor | Weight in Decision |
|--------|-------------------|
| Runway (how long can you survive on $150K?) | Critical |
| Equity structure (5% with what dilution protection?) | High |
| Founder quality (would you follow them into battle?) | Critical |
| Market timing (is this a good vintage for startups?) | Medium |
| Personal satisfaction (are you dying in corporate?) | High |

**Confidence:** MODERATE (decision is personal; frameworks provide structure, not answer)

---

## Example 4: Cross-Domain Bridge in Action

### Input
```
[CEREBRO-LITE:BRIDGE]
Source Pattern: How ant colonies manage distributed decision-making
Source Domain: Biology/entomology
Target Context: Managing a 500-person remote company
```

### Output

**[CROSS-DOMAIN BRIDGE ANALYSIS]**

**Source Pattern Extraction:**
```
Ant Colony Decision-Making:
├─ No central command (queen doesn't direct daily activity)
├─ Local rules create global behavior (stigmergy)
├─ Pheromone trails = information sharing mechanism
├─ Threshold-based responses (ants act when signal > threshold)
├─ Redundancy (many ants, failure of one doesn't matter)
└─ Specialization emerges from context, not assignment
```

**Target Domain Mapping:**

| Ant Colony | Remote Company |
|------------|----------------|
| Pheromone trails | Shared dashboards, Slack channels |
| Local rules | Clear decision rights per role |
| Threshold responses | Escalation criteria (when to act) |
| Redundancy | Cross-training, documentation |
| Emergent specialization | Self-organizing teams |
| Queen (reproduction, not command) | CEO (vision, not micromanagement) |

**Bridge Strength:** STRONG (structural isomorphism + mechanism transfer)

**Adaptation Required:**
- Ants are interchangeable; humans have unique skills
- Human pheromones = explicit communication needed
- Speed: ant decisions in seconds; human decisions in hours/days

**Novel Insights for Remote Company:**
1. **Create "pheromone trails"**: Make work visible (dashboard, weekly updates) so others can follow successful patterns
2. **Threshold-based escalation**: Define when employees should escalate vs. act autonomously
3. **Emergent specialization**: Let roles evolve based on context rather than rigid job descriptions
4. **Redundancy**: Ensure no single person is a critical path

**Recommended Implementation:**
- Implement "work visibility" tools (Linear, Notion with public projects)
- Document decision rights: "You decide X, escalate Y"
- Rotate people through different contexts to develop emergent specialization

---

## Summary Table

| Example | Subject | Confidence | Key Recommendation |
|---------|---------|------------|-------------------|
| 1 | Startup B2C→B2B Pivot | STRONG (5/5) | Validate B2B, then pivot |
| 2 | Restaurant Investment | MODERATE (3/5) | Reduce amount, add protections |
| 3 | Corporate→Startup Jump | MODERATE (2-3/5) | Depends on runway and founder |
| 4 | Ant Colony→Remote Mgmt | STRONG bridge | Implement "pheromone trails" |

---

*CEREBRO-Lite v1.0 — Pattern recognition in action.*
