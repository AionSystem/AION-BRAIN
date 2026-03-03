# What the CIA Knew About Bad Analysis That AI Developers Haven't Learned Yet

## The most dangerous thing your AI produces is the answer it didn't give you.

**Friday Salmon Certainty Report**
*Sheldon K. Salmon & ALBEDO \u2014 March 2026*

---

In 2009, the United States Government declassified a document that should be required reading for every organization deploying AI today.

It was not about AI. It was not about technology. It was about the oldest reliability problem in human decision-making: how smart, trained, well-resourced analysts consistently arrive at the wrong answer \u2014 not because they are careless, but because they are confident.

The document is called the CIA Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis. It is publicly available. Almost nobody in AI has read it.

That is a mistake worth correcting.

---

## The Door

Here is the problem the CIA identified, stated plainly.

`[D]` When analysts face a question, they generate a leading hypothesis early \u2014 often based on the first coherent explanation that fits the available data. From that point forward, every subsequent piece of evidence is evaluated against that leading hypothesis. Evidence that supports it is accepted. Evidence that doesn't is dismissed, re-interpreted, or forgotten.

The problem is not that analysts are biased. The problem is structural. The leading hypothesis becomes the frame. The frame decides what counts as signal and what counts as noise. The analyst is not ignoring contrary evidence deliberately \u2014 the frame is doing it for them, automatically, below the level of conscious scrutiny.

The CIA called this the mind-set problem. They built an entire suite of structured techniques to interrupt it.

Now consider what an AI system does when it generates an output.

It does exactly the same thing \u2014 faster, more fluently, and with no awareness that it is doing it.

---

## The Descent

`[R]` When an AI produces a confident answer, it has run a selection process. From the full space of possible responses, one surfaced. The others did not. The output you receive is the winner of a competition you were not invited to observe.

This is not a flaw. It is how generation works. The question is not whether suppression happened. Suppression always happens. The question is what got suppressed \u2014 and whether any of it mattered.

The CIA found, across decades of documented intelligence failures, that the most dangerous suppressions share a pattern. The suppressed hypothesis was not impossible. It was uncomfortable. It required a different model of the adversary than the one the analyst had built. It predicted an outcome the analyst found unlikely \u2014 not because the evidence ruled it out, but because the analyst's prior experience said it wouldn't happen.

Pearl Harbor. The Yom Kippur War. Iraq's WMD assessment, in reverse.

In every case, the suppressed hypothesis was available. The evidence was there. The frame chose not to see it.

`[R]` Your AI does not have decades of prior experience. What it has is training \u2014 which is prior experience at scale. Its frame is not one analyst's career. It is a compression of everything it was trained on. The suppression mechanism is identical. The speed is orders of magnitude higher.

---

## The Turn

Here is what the CIA built to fix it.

The technique is called Analysis of Competing Hypotheses \u2014 ACH. The core move is an inversion. Instead of asking *which hypothesis does the evidence support,* you ask *which hypothesis does the evidence fail to disprove.*

The difference is not semantic. It is architectural.

When you evaluate evidence in favor of a hypothesis, you are looking for confirmation. Confirmation is easy to find. Any pattern that fits the frame will do. The CIA found that analysts could construct convincing cases for the wrong answer with the same evidence they used to construct cases for the right one \u2014 because they were selecting evidence to fit, not testing evidence to break.

When you evaluate evidence against hypotheses \u2014 when you ask *what would this evidence look like if each hypothesis were true, and does what we see actually fit* \u2014 the frame loses its grip. Evidence that is consistent with all hypotheses tells you nothing. Only evidence that is inconsistent with some hypotheses and consistent with others has diagnostic value. The matrix forces you to find the discriminating evidence instead of the confirming evidence.

`[D]` The CIA documented this in a declassified case study. In March 1995, Aum Shinrikyo attacked the Tokyo subway with sarin. Early analysis faced four competing hypotheses about the group's nature. When the evidence was arrayed against all four simultaneously rather than fed into the leading hypothesis, the discrimination became clear. The matrix showed which evidence was genuinely diagnostic and which was consistent with everything \u2014 and therefore useless for determining the right answer.

This is not a historical curiosity. It is an operational method