# [Engine Name] v[X.Y] — Test Plan & Methodology

**Version:** 1.0  
**Purpose:** Reproducible benchmark validation methodology

---

## Overview

This document describes the methodology for validating [Engine Name] benchmark claims. All testing follows a paired comparison design: baseline (standard LLM) vs. engine-augmented responses.

---

## Test Design

### Paired Comparison Methodology

```
TEST STRUCTURE
==============

For each scenario in the test suite:

1. BASELINE TEST
   ├─ Prompt: Standard query (no engine context)
   ├─ Platform: Target AI (ChatGPT, Claude, Gemini, etc.)
   ├─ Record: Full response text
   └─ Score: Using standard rubric

2. ENGINE TEST  
   ├─ Prompt: Same query WITH [Engine] system prompt
   ├─ Platform: Same target AI platform
   ├─ Record: Full response text
   └─ Score: Using same rubric

3. COMPARISON
   ├─ Calculate: Score difference (Engine - Baseline)
   ├─ Aggregate: By category and overall
   └─ Analyze: Statistical significance
```

### Sample Size Justification

| Phase | Sample Size | Justification |
|-------|-------------|---------------|
| Pilot (1K+1K) | 1,000 per condition | 95% CI within ±3% margin |
| Full (8K+8K) | 8,000 per condition | 99% CI within ±1% margin, subcategory analysis |

---

## Scenario Design Principles

### Prompt Construction Rules

1. **Realistic Context:** Each scenario reflects actual use cases
2. **Graduated Complexity:** Mix of simple, moderate, and complex
3. **Domain Coverage:** All engine capabilities represented
4. **Edge Cases:** 15% of scenarios test boundary conditions
5. **Adversarial:** 10% designed to elicit common errors

### Category Distribution (1K Pilot)

| Category | Count | Percentage |
|----------|-------|------------|
| [Core Function 1] | 200 | 20% |
| [Core Function 2] | 200 | 20% |
| [Core Function 3] | 200 | 20% |
| [Safety/Boundaries] | 150 | 15% |
| [Edge Cases] | 150 | 15% |
| [Integration] | 100 | 10% |
| **TOTAL** | **1,000** | **100%** |

---

## Scoring Methodology

### Primary Scoring Scale

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Excellent | Complete, accurate, well-structured, safe |
| 4 | Good | Accurate with minor gaps or formatting issues |
| 3 | Acceptable | Mostly correct, some material errors |
| 2 | Poor | Significant errors affecting utility |
| 1 | Unacceptable | Fundamentally incorrect or misleading |
| 0 | Critical | Safety violation, fabrication, or harmful |

### Scoring Workflow

```
SCORING PROCEDURE
=================

1. READ response completely before scoring
2. IDENTIFY which category applies
3. CHECK against category-specific rubric
4. VERIFY any claims or citations
5. ASSIGN score with brief justification
6. FLAG any safety concerns immediately
```

---

## Data Collection Requirements

### Required Artifacts

```
OUTPUT ARTIFACTS
================

1. RAW RESPONSES
   ├─ baseline_responses.jsonl
   └─ engine_responses.jsonl

2. SCORED RESULTS
   ├─ baseline_scores.csv
   ├─ engine_scores.csv
   └─ paired_comparison.csv

3. METADATA
   ├─ test_environment.json
   ├─ platform_versions.json
   └─ tester_info.json (anonymized)

4. ANALYSIS
   ├─ statistical_summary.md
   ├─ category_breakdown.csv
   └─ improvement_analysis.md
```

### Response Recording Format

```json
{
  "scenario_id": "[ENGINE]-[CAT]-0001",
  "category": "[category_name]",
  "timestamp": "2025-11-27T10:30:00Z",
  "platform": "[ai_platform]",
  "platform_version": "[version]",
  "prompt": "[full prompt text]",
  "response": "[full response text]",
  "response_tokens": [N],
  "latency_ms": [N],
  "test_type": "baseline|engine",
  "engine_version": "[X.Y]"
}
```

---

## Statistical Analysis

### Required Calculations

1. **Mean Score by Category:** For baseline and engine
2. **Improvement Delta:** (Engine Mean - Baseline Mean)
3. **Paired t-test:** For statistical significance
4. **Effect Size:** Cohen's d for practical significance
5. **95% Confidence Intervals:** For all reported metrics

### Significance Thresholds

| Metric | Threshold | Interpretation |
|--------|-----------|----------------|
| p-value | < 0.05 | Statistically significant |
| Cohen's d | > 0.2 | Small effect |
| Cohen's d | > 0.5 | Medium effect |
| Cohen's d | > 0.8 | Large effect |

---

## Platform Testing Matrix

### Recommended Platforms

| Platform | Priority | Notes |
|----------|----------|-------|
| ChatGPT (GPT-4) | High | Most common deployment |
| Claude 3 Opus/Sonnet | High | Strong reasoning |
| Gemini Pro | Medium | Google ecosystem |
| GPT-4o | Medium | Multimodal |

---

## Quality Assurance

### Inter-Rater Reliability

For high-stakes metrics:
- Dual scoring by independent raters
- Calculate Cohen's Kappa
- Require Kappa > 0.7 for acceptance
- Resolve disagreements through discussion

### Audit Trail

Maintain complete records of:
- All raw responses
- All scoring decisions
- Any anomalies or exclusions
- Methodology deviations

---

**Methodology Version:** 1.0  
**Last Updated:** November 2025  
**Status:** Framework Ready — Awaiting Validation Execution
