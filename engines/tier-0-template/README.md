# Tier-0: Engine Template

**Purpose:** Template folder structure for creating new AION-BRAIN engines

---

## Overview

This tier serves as a **template and reference** for creating new engines in the AION-BRAIN ecosystem. It contains the complete folder structure, file templates, and documentation standards that all engines should follow.

**This is not an operational engine** — it is a blueprint for engine development.

---

## Using This Template

### To Create a New Engine:

1. Copy the `engine-template-v1.0/` folder
2. Rename to your engine name with version (e.g., `my-engine-v1.0/`)
3. Update all template files with your engine-specific content
4. Place in the appropriate tier folder:
   - **Tier-1:** Foundation engines (core safety, validation, reasoning)
   - **Tier-2:** Cognitive architecture (creativity, decision-making, meta-learning)
   - **Tier-3:** Domain-specific (medical, legal, financial, etc.)
   - **Tier-4:** Experimental (preview versions, research concepts)

### Version Numbering Convention:

| Version Type | Format | Example |
|-------------|--------|---------|
| Major release | X.0 | 2.0 |
| Minor update | X.Y | 2.1 |
| Preview/Experimental | vX-preview | v3-preview |

---

## Standard Engine Folder Structure

```
engine-name-vX.Y/
├── README.md                    # Engine overview and quick start
├── engine-name-vX.Y-spec.md     # Full specification (800+ lines)
├── engine-name-vX.Y-prompt.md   # System prompt for AI platforms
├── engine-name-vX.Y-examples.md # Usage examples and scenarios
│
├── modules/                     # Engine modules (minimum 7 core)
│   ├── module-01-*.md
│   ├── module-02-*.md
│   └── ...
│
├── use-cases/                   # Real-world application scenarios (minimum 10)
│   ├── use-case-01-*.md
│   └── ...
│
├── compliance/                  # Regulatory and ethical compliance
│   ├── compliance-overview.md
│   └── ...
│
├── integrations/                # Platform and system integrations
│   ├── integration-overview.md
│   └── ...
│
├── training/                    # User training and certification materials
│   ├── training-overview.md
│   └── ...
│
├── benchmarks/                  # Performance validation framework
│   ├── README.md                # Benchmark targets and methodology overview
│   ├── test-scenarios/
│   │   ├── baseline/            # Standard LLM prompts (no engine)
│   │   └── engine/              # Engine-augmented prompts
│   ├── methodology/
│   │   └── test-plan.md         # Reproducible test methodology
│   ├── rubrics/
│   │   └── scoring-guide.md     # Scoring criteria
│   └── results/                 # Validated results (when available)
│
├── adversarial-testing/         # Red team attack scenarios
│   └── README.md
│
├── ai-collaboration/            # Platform-specific optimization
│   └── README.md
│
├── failure-modes/               # FMEA proactive failure analysis
│   └── README.md
│
└── confidence-calibration/      # Accuracy-confidence alignment
    └── README.md
```

---

## Minimum Content Requirements

### By Tier:

| Tier | Modules | Use Cases | Spec Lines | Benchmarks |
|------|---------|-----------|------------|------------|
| Tier-1 Foundation | 5+ | 5+ | 400+ | Required |
| Tier-2 Cognitive | 7+ | 8+ | 600+ | Required |
| Tier-3 Domain | 10+ | 10+ | 800+ | Required |
| Tier-4 Experimental | 3+ | 3+ | 200+ | Planned |

### Benchmark Requirements:

All engines must include benchmark infrastructure:
- Target metrics (even if pending validation)
- Test scenario templates
- Scoring methodology
- Transparent status (validated vs. targets)

---

## Quality Standards

### Documentation Quality:
- Clear, professional language
- Consistent formatting (Markdown)
- Version numbers throughout
- Last updated dates

### Content Quality:
- Evidence-based where possible
- Citation of sources
- Realistic targets
- Transparent limitations

### Safety Standards:
- Professional disclaimers
- Scope boundaries defined
- Escalation triggers documented
- Human oversight emphasized

---

## Files in This Template

| File | Purpose |
|------|---------|
| `README.md` | This overview |
| `engine-template-v1.0/` | Complete engine template |

---

**Template Version:** 1.0  
**Last Updated:** November 2025  
**Maintainer:** AION-BRAIN Core Team
