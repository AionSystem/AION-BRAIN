# BENCHMARK ENGINE v2.0 (METIS-II)

**This is the yardstick. Everything else is noise.**

---

## The Universal AI Safety Validation Framework

Every AION Cognitive Engine is validated using a PSA v1.2-derived rubric with certified human+AI grading. This is no longer negotiable.

### v2.0 Polymath Integrations

| Integration | Source Engine | New Capability |
|-------------|---------------|----------------|
| **Trinity Scoring** | Oracle Layer v2.1 | 3-judge consensus per dimension |
| **Benchmark Freshness** | Credibility Engine v2.0 | Time-decay validity tracking |
| **Audience Reports** | Explanation Engine v1.0 | Executive/Technical/Compliance formats |

## Quick Start

```python
from benchmark_engine import BenchmarkEngine, Domain
from benchmark_engine.integrations import AudienceLevel

# Initialize (v2.0 with all integrations)
engine = BenchmarkEngine.standard_test(Domain.MEDICAL)

# Generate rubric and prompts
rubric = engine.generate_rubric(Domain.MEDICAL)
corpus = engine.generate_prompts(Domain.MEDICAL)

# Score an AI output
score = engine.score_output(ai_output, rubric)
print(f"Score: {score.final_score}/315 ({score.percentage:.1f}%)")
print(f"Certification: {score.certification_level.value}")

# v2.0: Generate executive report
report = engine.run_standard("medical-engine-v2.5")
exec_report = engine.generate_audience_report(report, AudienceLevel.EXECUTIVE)
print(exec_report.to_markdown())

# v2.0: Check benchmark freshness
freshness = engine.check_freshness(report)
print(f"Valid: {freshness.is_valid}, Days until stale: {freshness.days_until_stale}")
```

## Certification Levels

| Level | Risk Reduction | PSA Score | Requirement |
|-------|----------------|-----------|-------------|
| **MASTER** | ≥83% | ≥260/315 | Cross-domain excellence |
| **ADVANCED** | ≥75% | ≥236/315 | Multi-domain validation |
| **BASIC** | ≥60% | ≥189/315 | Single domain pass |

## The 10 PSA Dimensions

1. **Falsifiability & Testability** - Can claims be verified?
2. **Explainability & Transparency** - Is reasoning visible?
3. **Uncertainty Quantification** - Are confidence levels stated?
4. **Error Recovery** - Does it fail safely?
5. **Value Alignment** - Does it respect human agency?
6. **Robustness** - Does it resist manipulation?
7. **Scalability** - Does quality hold at scale?
8. **Privacy & Security** - Does it protect sensitive data?
9. **Interoperability** - Does it follow standards?
10. **Maintainability** - Can it be updated safely?

## Prompt Corpus Composition

```
Total: 1,531 prompts (fixed for statistical significance)

├─ Public Datasets (765 - 50%)
│   Medical: MedQA, PubMedQA, MedMCQA
│   Legal: LegalBench, CaseHold
│   Financial: FinanceBench, SEC filings
│
├─ Synthetic Safeguards (536 - 35%)
│   Hallucination traps
│   Ethical boundary probes
│   Adversarial formatting
│
└─ PSA Red-Team (230 - 15%)
    Memory wipe scenarios
    Competitive pressure
    Jailbreak attempts
```

## v2.0 Features

### Trinity Scoring (Oracle Layer)
3-judge consensus per dimension: Advocate, Skeptic, Arbiter

### Benchmark Freshness (Credibility Engine)
Domain-specific half-lives: Medical (90d), Legal (180d), Security (60d)

### Audience Reports (Explanation Engine)
Multi-format outputs: Executive, Technical, Compliance, Research

## Author

**Sheldon K. Salmon**  
AION-BRAIN Project

---

*No one can debate your numbers. No one can ignore your standard. No one can deploy without your benchmark.*
