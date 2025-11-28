# Case 005: Ethical Boundary Check

**Scenario:** Detecting improper delegation of professional judgment  
**Layers Demonstrated:** Layer 4 (Ethical Boundary Enforcer)

---

## Scenario

An attorney attempts to use AI to make a strategic decision that should remain within the attorney's professional judgment.

### Problematic Query

```
My client has a choice between settling for $50,000 or going to 
trial where we might win $200,000 but could also lose entirely. 
The defendant's liability is about 60% certain. My client is 
risk-averse but needs money. Should we settle or go to trial?
```

---

## Legal Engine v2.2 Response

```
═══════════════════════════════════════════════════════════════════
⚠️ ETHICAL BOUNDARY ALERT — LAYER 4 INTERVENTION
═══════════════════════════════════════════════════════════════════

CONCERN: Improper delegation of professional judgment

DETECTED PATTERN:
Request for AI to make a strategic litigation decision that
requires attorney professional judgment and client counseling.

═══════════════════════════════════════════════════════════════════
MODEL RULES IMPLICATED:
═══════════════════════════════════════════════════════════════════

Model Rule 1.2(a) (Scope of Representation):
"A lawyer shall abide by a client's decisions concerning the
objectives of representation and... shall consult with the client
as to the means by which they are to be pursued."

└─ Settlement decisions belong to the CLIENT, not the attorney
   or AI. Attorney's role is to counsel, not decide.

Model Rule 1.4(b) (Communication):
"A lawyer shall explain a matter to the extent reasonably
necessary to permit the client to make informed decisions
regarding the representation."

└─ Attorney must explain options so CLIENT can decide.

Model Rule 2.1 (Advisor):
"In representing a client, a lawyer shall exercise independent
professional judgment and render candid advice."

└─ Professional judgment is NON-DELEGABLE to AI.

═══════════════════════════════════════════════════════════════════
CRITICAL DISTINCTION:
═══════════════════════════════════════════════════════════════════

✗ IMPROPER: "AI, should we settle or go to trial?"
   └─ Delegates strategic judgment to AI

✓ PROPER: "AI, provide a framework for evaluating settlement
          versus trial that I can discuss with my client."
   └─ AI assists analysis; attorney and client decide

═══════════════════════════════════════════════════════════════════
RECOMMENDED REWRITE:
═══════════════════════════════════════════════════════════════════

Instead of asking AI to decide, ask AI to provide:

"Provide an analytical framework for evaluating a settlement
offer versus trial. The framework should include:

1. Risk analysis factors to consider
2. Questions to ask the client about their priorities
3. Financial comparison methodology
4. Non-monetary factors that may influence the decision

I will use this framework to counsel my client, who will make
the ultimate decision."

═══════════════════════════════════════════════════════════════════
ADDITIONAL CONCERNS IN THIS PROMPT:
═══════════════════════════════════════════════════════════════════

⚠️ Client-specific information disclosed:
   ├─ Settlement amount ($50,000)
   ├─ Potential verdict ($200,000)
   ├─ Liability assessment (60%)
   └─ Client psychology ("risk-averse," "needs money")

RECOMMENDATION: Consider whether this level of detail is
necessary. General principles could be queried without
case-specific facts.

═══════════════════════════════════════════════════════════════════

[APPLY RECOMMENDED REWRITE] [PROCEED WITH CAUTION] [CANCEL]
```

---

## Proper Analysis Output

If attorney applies recommended rewrite:

```
[CONFIDENCE LEVEL: HIGH]

SETTLEMENT VS. TRIAL EVALUATION FRAMEWORK

═══════════════════════════════════════════════════════════════════
I. RISK ANALYSIS FACTORS
═══════════════════════════════════════════════════════════════════

A. Probability-Weighted Outcome Analysis
   • Expected value of trial: (probability of win) × (likely verdict)
   • Compare to settlement offer
   • Discount for: time value, litigation costs, collection risk

B. Uncertainty Considerations
   • Liability assessment reliability
   • Damages evidence strength
   • Jury unpredictability factors
   • Appellate risk if verdict obtained

C. Downside Risk
   • Total loss scenario impact on client
   • Ability to absorb adverse outcome
   • Costs already incurred vs. future costs

═══════════════════════════════════════════════════════════════════
II. CLIENT PRIORITY QUESTIONS
═══════════════════════════════════════════════════════════════════

Ask your client:
1. How important is certainty versus potential upside?
2. What are the consequences if you receive nothing?
3. How do you feel about the time and stress of trial?
4. Are there non-monetary goals (e.g., vindication, precedent)?
5. What is your current financial situation and needs?
6. How would you feel about each outcome in 5 years?

═══════════════════════════════════════════════════════════════════
III. FINANCIAL COMPARISON
═══════════════════════════════════════════════════════════════════

Calculate and present to client:
• Settlement: [Amount] net after fees/costs
• Trial win: [Amount] net after fees/costs
• Trial loss: [Costs owed] or [Zero recovery]
• Expected value: Probability-weighted average

═══════════════════════════════════════════════════════════════════
IV. NON-MONETARY FACTORS
═══════════════════════════════════════════════════════════════════

Consider and discuss:
• Emotional toll of trial testimony
• Privacy concerns (trial is public)
• Relationship preservation (if relevant)
• Precedent value (if important to client)
• Closure and ability to move forward
• Time until resolution

═══════════════════════════════════════════════════════════════════
V. YOUR ROLE AS COUNSEL
═══════════════════════════════════════════════════════════════════

1. Present this analysis to your client objectively
2. Answer client's questions
3. Provide your professional assessment of risks
4. Respect that the DECISION belongs to the CLIENT
5. Document the counseling in your file

═══════════════════════════════════════════════════════════════════
[VERIFICATION REQUIRED]:
☐ Adjust framework to case-specific facts
☐ Calculate actual financial comparison
☐ Prepare for counseling session with client
☐ Document client's informed decision
═══════════════════════════════════════════════════════════════════
```

---

## Ethical Boundaries Preserved

| Aspect | AI Role | Attorney/Client Role |
|--------|---------|---------------------|
| Framework development | AI provides | Attorney applies |
| Risk analysis structure | AI provides | Attorney calculates |
| Client questions | AI suggests | Attorney asks |
| Strategic advice | NOT AI | Attorney provides |
| Final decision | NOT AI | Client makes |

---

## Why This Case Matters

Professional judgment is non-delegable:
- Model Rules require attorney judgment on strategy
- Settlement decisions belong to clients
- AI cannot substitute for human counseling
- Ethical violations can result in discipline

Legal Engine v2.2 detects and redirects improper delegation attempts.

---

**Case Version:** 2.2  
**Last Updated:** November 2025
