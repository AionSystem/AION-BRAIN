# AION-BRAIN — Repository Structure

**Complete skeleton of the AION-BRAIN repository**

*Last Updated: November 28, 2025*

---

## Quick Stats

| Metric | Count |
|--------|-------|
| **Total Directories** | 550+ |
| **Total Files** | 1,350+ |
| **Engine Count** | 30 specialized engines |
| **Working Python Engines** | 7 flagship engines with tests |
| **Framework Count** | 15+ reasoning frameworks |
| **Benchmark Coverage** | 100% (all engines) |
| **Legal Documents** | 38 documents (v3.1) |
| **Contract Templates** | 11 business agreements |
| **Jurisdictions** | 11 global regulatory frameworks |
| **Total Test Coverage** | 394 passing tests |

---

## Working Python Engine Implementations

Seven flagship engines now have full Python implementations with test suites:

| Engine | Version | Codename | Tests | Location |
|--------|---------|----------|-------|----------|
| **Oracle Layer** | v2.1 | PROMETHEUS | 33 | `tier-1-foundation/oracle-layer-v2.1/src/` |
| **SIMPLEXITY** | v2.0 | - | 59 | `tier-1-foundation/complexity-management-engine/src/` |
| **Strategy Engine** | v1.1 | The Strategist's Edge | 52 | `tier-2-cognitive-architecture/strategy-engine-v1.1/src/` |
| **Decision Engine** | v1.0 | DECIDERE | 53 | `tier-2-cognitive-architecture/decision-engine-v1.0/src/` |
| **Credibility Engine** | v2.0 | VERITAS | 53 | `tier-2-cognitive-architecture/credibility-engine-v2.0/src/` |
| **Explanation Engine** | v1.0 | CLARITAS | 49 | `tier-2-cognitive-architecture/explanation-generation-engine/src/` |
| **Benchmark Engine** | v2.0 | METIS-II | 95 | `tier-1-foundation/benchmark-engine-v1.0/src/` |

---

## Top-Level Structure

```
AION-BRAIN/
│
├── .aions-structure-list/     # This folder - repository map
├── assets/                    # Visual assets (badges, images, videos)
├── benchmarks/                # Performance benchmarks by engine
├── certification/             # Certification programs
├── cognitive-architecture/    # System design patterns
├── cognitive-biases/          # Bias detection and mitigation
├── cognitive-metrics/         # Performance measurement
├── community/                 # Community contributions
├── cosmic-framework/          # Civilization-scale safety protocols
├── deployment/                # Cloud deployment templates
├── docs/                      # Core documentation
├── economic-systems/          # AION Economy v3.0 specification
├── ecosystem/                 # Partner and marketplace programs
├── engines/                   # THE MAIN EVENT - All cognitive engines
├── enterprise/                # Enterprise deployment guides
├── examples/                  # Usage examples and templates
├── failure-modes/             # Known failure catalogs
├── frameworks/                # Reasoning frameworks
├── global-governance/         # International standards
├── innovation-lab/            # Experimental research
├── international/             # Multi-jurisdiction compliance
├── legal/                     # Legal documentation
├── modules/                   # Modular components
├── ontology-library/          # Domain ontologies
├── press/                     # Media kit and press releases
├── protocol-exchange/         # Inter-engine communication
├── reasoning-traces/          # Example reasoning traces
├── research-lab/              # Research collaboration
├── research-pipeline/         # Research methodology
├── scaling-laws/              # Scaling considerations
├── security-resilience/       # Security engines and protocols
├── societal-impact/           # Impact assessment frameworks
├── temporal-reasoning/        # Time-based reasoning
├── testing/                   # Test suites and validation
├── tools/                     # Utility tools and scripts
├── tutorials/                 # Step-by-step tutorials
├── uncertainty-management/    # Uncertainty quantification
├── whitepapers/               # Research whitepapers
│
├── about.md                   # About AION
├── ARCHITECT.md               # Architecture overview
├── CHANGELOG.md               # Version history
├── CITATION.cff               # Citation format
├── CODE_OF_CONDUCT.md         # Community guidelines
├── CONTRIBUTING.md            # Contribution guide
├── DISCLAIMER.md              # Legal disclaimer
├── generate_cheatsheet_pdf.py # PDF generator script
├── GOVERNANCE.md              # Governance model
├── GRATITUDE.md               # Acknowledgments
├── index.md                   # MkDocs homepage
├── LICENSE                    # Apache License 2.0
├── MANIFESTO.md               # Philosophy and vision
├── NOTICE                     # License notices
├── NOW.md                     # Current focus
├── QUICK-START-CHEAT-SHEET.md # Quick reference (30+ engines)
├── QUICK-START-CHEAT-SHEET.pdf # Printable quick reference
├── README-LITE.md             # Fast-scanning overview
├── SECURITY.md                # Security policy
├── STORY.md                   # The AION story
├── SUPPORT.md                 # Support options
├── TESTIMONIALS.md            # Community testimonials
└── VISION.md                  # Long-term vision
```

---

## Engines Directory (The Core)

The heart of AION — organized into 5 tiers by function:

```
engines/
│
├── BENCHMARKS-OVERVIEW.md              # Master benchmark documentation
│
├── tier-0-template/                    # NEW: Engine development template
│   └── engine-template-v1.0/           # Standard engine structure
│       ├── README.md
│       ├── engine-template-v1.0-spec.md
│       ├── benchmarks/                 # Benchmark template
│       │   ├── README.md
│       │   ├── test-scenarios/
│       │   │   ├── baseline/
│       │   │   └── engine/
│       │   ├── methodology/
│       │   │   └── test-plan.md
│       │   ├── rubrics/
│       │   │   └── scoring-guide.md
│       │   └── results/
│       ├── modules/
│       ├── use-cases/
│       ├── compliance/
│       ├── integrations/
│       ├── training/
│       ├── adversarial-testing/
│       ├── ai-collaboration/
│       ├── failure-modes/
│       └── confidence-calibration/
│
├── tier-1-foundation/                    # Core reasoning infrastructure (8 engines)
│   │
│   ├── benchmark-engine-v1.0/            # METIS-II v2.0 - Universal AI Safety Validation
│   │   ├── benchmarks/
│   │   ├── data/
│   │   ├── examples/
│   │   ├── src/
│   │   │   └── benchmark_engine/         # WORKING PYTHON IMPLEMENTATION
│   │   │       ├── __init__.py
│   │   │       ├── core.py               # Main engine (6-layer architecture)
│   │   │       ├── config.py             # Configuration and constants
│   │   │       ├── types.py              # Data structures and enums
│   │   │       ├── integrations/         # v2.0 Polymath Integrations
│   │   │       │   ├── __init__.py
│   │   │       │   ├── trinity_scoring.py    # Oracle Layer integration
│   │   │       │   ├── benchmark_freshness.py # Credibility Engine integration
│   │   │       │   └── audience_reports.py   # Explanation Engine integration
│   │   │       ├── tests/
│   │   │       │   └── test_benchmark_engine.py  # 95 passing tests
│   │   │       ├── certifiers/
│   │   │       ├── generators/
│   │   │       └── validators/
│   │   ├── benchmark-engine-v2.0-spec.md
│   │   ├── benchmark-engine-v2.0-prompt.md
│   │   ├── benchmark-engine-v2.0-spec.pdf
│   │   ├── generate_pdf.py
│   │   └── README.md
│   │
│   ├── complexity-management-engine/     # SIMPLEXITY v2.0 - Complexity navigation
│   │   ├── benchmarks/
│   │   ├── src/
│   │   │   ├── examples/
│   │   │   │   └── basic_usage.py
│   │   │   └── simplexity/               # WORKING PYTHON IMPLEMENTATION
│   │   │       ├── __init__.py
│   │   │       ├── core.py               # Main engine
│   │   │       ├── config.py
│   │   │       ├── analysis.py
│   │   │       ├── prompts.py
│   │   │       ├── scoring.py
│   │   │       ├── modules/              # 8 complexity modules
│   │   │       │   ├── abstraction.py
│   │   │       │   ├── calibration.py
│   │   │       │   ├── decomposition.py
│   │   │       │   ├── dynamics.py
│   │   │       │   ├── emergence.py
│   │   │       │   ├── mvc.py
│   │   │       │   ├── simplification.py
│   │   │       │   └── transfer.py
│   │   │       └── tests/
│   │   │           └── test_simplexity.py  # 59 passing tests
│   │   ├── complexity-management-engine-v2.0-spec.md
│   │   ├── complexity-management-engine-v2.0-prompt.md
│   │   ├── complexity-management-engine-v2.0.pdf
│   │   └── README.md
│   │
│   ├── oracle-layer-v2.1/                # PROMETHEUS - central orchestration
│   │   ├── benchmarks/
│   │   ├── modules/
│   │   ├── v2.0-enhancements/
│   │   ├── src/
│   │   │   ├── examples/
│   │   │   │   └── basic_usage.py
│   │   │   └── oracle_layer/             # WORKING PYTHON IMPLEMENTATION
│   │   │       ├── __init__.py
│   │   │       ├── core.py               # Main orchestration
│   │   │       ├── config.py
│   │   │       ├── prompts.py
│   │   │       ├── providers/            # LLM provider integrations
│   │   │       │   ├── anthropic.py
│   │   │       │   ├── openai.py
│   │   │       │   ├── gemini.py
│   │   │       │   └── generic.py
│   │   │       └── tests/
│   │   │           └── test_oracle_layer.py  # 33 passing tests
│   │   ├── oracle-layer-v2.1-spec.md
│   │   ├── oracle-layer-v2.1-prompt.md
│   │   ├── oracle-layer-v2.1.pdf
│   │   └── README.md
│   │
│   ├── contamination-prevention-v1.2/    # Prevents domain contamination
│   │   └── benchmarks/
│   ├── epistemic-humility-validator-v3.1/ # Validates uncertainty claims
│   │   └── benchmarks/
│   ├── meta-ethical-engine-v2.1/         # Ethical reasoning framework
│   │   └── benchmarks/
│   ├── reasoning-pattern-catalog/        # Reasoning pattern library
│   │   └── benchmarks/
│   └── uncertainty-quantification-engine/ # Quantifies uncertainty
│       └── benchmarks/
│
├── tier-2-cognitive-architecture/        # Cognitive capabilities (10 engines)
│   │
│   ├── strategy-engine-v1.1/             # The Strategist's Edge - Strategic planning
│   │   ├── benchmarks/
│   │   ├── src/
│   │   │   ├── examples/
│   │   │   │   └── basic_usage.py
│   │   │   └── strategy_engine/          # WORKING PYTHON IMPLEMENTATION
│   │   │       ├── __init__.py
│   │   │       ├── core.py               # Main engine
│   │   │       ├── config.py
│   │   │       ├── analysis.py
│   │   │       ├── prompts.py
│   │   │       ├── scoring.py
│   │   │       ├── frameworks/           # 5 strategic frameworks
│   │   │       │   ├── sun_tzu.py        # Competitive positioning
│   │   │       │   ├── meadows.py        # Systems leverage
│   │   │       │   ├── barabasi.py       # Network dynamics
│   │   │       │   ├── pearl.py          # Causal inference
│   │   │       │   └── ostrom.py         # Commons governance
│   │   │       └── tests/
│   │   │           └── test_strategy_engine.py  # 52 passing tests
│   │   ├── strategy-engine-v1.1-spec.md
│   │   ├── strategy-engine-v1.1-prompt.md
│   │   ├── strategy-engine-v1.1.pdf
│   │   └── README.md
│   │
│   ├── decision-engine-v1.0/             # DECIDERE - decision support
│   │   ├── benchmarks/
│   │   ├── src/
│   │   │   ├── examples/
│   │   │   │   └── basic_usage.py
│   │   │   └── decision_engine/          # WORKING PYTHON IMPLEMENTATION
│   │   │       ├── __init__.py
│   │   │       ├── core.py               # Main engine
│   │   │       ├── config.py
│   │   │       ├── analysis.py
│   │   │       ├── prompts.py
│   │   │       ├── frameworks/           # 5 decision frameworks
│   │   │       │   ├── kahneman.py       # Bias detection
│   │   │       │   ├── simon.py          # Satisficing
│   │   │       │   ├── taleb.py          # Antifragility
│   │   │       │   ├── bergson.py        # Temporal intelligence
│   │   │       │   └── rawls_singer.py   # Ethical validation
│   │   │       └── tests/
│   │   │           └── test_decision_engine.py  # 53 passing tests
│   │   ├── decision-engine-v1.0-spec.md
│   │   ├── decision-engine-v1.0-prompt.md
│   │   ├── decision-engine-v1.0.pdf
│   │   └── README.md
│   │
│   ├── credibility-engine-v2.0/          # VERITAS - Source credibility assessment
│   │   ├── benchmarks/
│   │   ├── src/
│   │   │   ├── examples/
│   │   │   │   └── basic_usage.py
│   │   │   └── credibility_engine/       # WORKING PYTHON IMPLEMENTATION
│   │   │       ├── __init__.py
│   │   │       ├── core.py               # Main engine
│   │   │       ├── config.py
│   │   │       ├── analysis.py
│   │   │       ├── prompts.py
│   │   │       ├── modules/              # 7 credibility modules
│   │   │       │   ├── decay_math.py     # Formal decay mathematics
│   │   │       │   ├── signals.py        # Signal instrumentation
│   │   │       │   ├── explainability.py # Score explainability
│   │   │       │   ├── automation.py     # Action automation
│   │   │       │   ├── ab_testing.py     # A/B testing framework
│   │   │       │   ├── fraud.py          # Fraud detection
│   │   │       │   └── provenance.py     # Evidence provenance
│   │   │       └── tests/
│   │   │           └── test_credibility_engine.py  # 53 passing tests
│   │   ├── credibility-engine-v2.0-spec.md
│   │   ├── credibility-engine-v2.0-prompt.md
│   │   ├── credibility-engine-v2.0.pdf
│   │   └── README.md
│   │
│   ├── explanation-generation-engine/    # CLARITAS - Explainability
│   │   ├── benchmarks/
│   │   ├── src/
│   │   │   ├── examples/
│   │   │   │   └── basic_usage.py
│   │   │   └── explanation_engine/       # WORKING PYTHON IMPLEMENTATION
│   │   │       ├── __init__.py
│   │   │       ├── core.py               # Main engine
│   │   │       ├── config.py
│   │   │       ├── types.py
│   │   │       ├── generators/           # 4 core generators
│   │   │       │   ├── multi_level.py    # 7-layer explanations
│   │   │       │   ├── counterfactual.py # What-if scenarios
│   │   │       │   ├── audience.py       # Audience adaptation
│   │   │       │   └── verification.py   # Explanation verifier
│   │   │       └── tests/
│   │   │           └── test_explanation_engine.py  # 49 passing tests
│   │   ├── explanation-engine-v1.0-spec.md
│   │   ├── explanation-engine-v1.0-prompt.md
│   │   ├── explanation-engine-v1.0.pdf
│   │   └── README.md
│   │
│   ├── cerebro-lite-v1.0/                # Lightweight reasoning core
│   │   └── benchmarks/
│   ├── creativity-engine/                # Creative generation
│   │   └── benchmarks/
│   ├── github-mastery-engine-v1.1/       # GitHub workflow optimization
│   │   └── benchmarks/
│   ├── meta-learning-engine/             # Learning optimization
│   │   └── benchmarks/
│   ├── personality-architect-v1.0/       # THE SCULPTOR - Persona design
│   │   ├── benchmarks/
│   │   ├── instruction-cards/
│   │   │   └── examples/
│   │   ├── integrations/
│   │   ├── personas/
│   │   │   ├── creative/
│   │   │   ├── genius/
│   │   │   ├── roles/
│   │   │   └── specialist/
│   │   └── templates/
│   └── systems-analysis-v3.1/            # Systems thinking
│       └── benchmarks/
│
├── tier-3-domain-specific/               # Specialized domain engines (8 engines)
│   ├── crisis-grief-engine-v1.5/         # NEW: Crisis counseling v1.5
│   │   ├── benchmarks/
│   │   │   ├── README.md
│   │   │   ├── test-scenarios/
│   │   │   │   ├── baseline/
│   │   │   │   │   └── crisis-baseline-scenarios.csv
│   │   │   │   └── engine/
│   │   │   │       └── crisis-engine-scenarios.csv
│   │   │   ├── methodology/
│   │   │   │   └── test-plan.md
│   │   │   ├── rubrics/
│   │   │   │   └── scoring-guide.md
│   │   │   └── results/
│   │   ├── modules/
│   │   ├── use-cases/
│   │   ├── compliance/
│   │   ├── adversarial-testing/
│   │   ├── ai-collaboration/
│   │   ├── failure-modes/
│   │   └── confidence-calibration/
│   │
│   ├── financial-engine-v1.5/            # NEW: Financial reasoning v1.5
│   │   ├── benchmarks/
│   │   │   ├── README.md
│   │   │   ├── test-scenarios/
│   │   │   │   ├── baseline/
│   │   │   │   │   └── financial-baseline-scenarios.csv
│   │   │   │   └── engine/
│   │   │   │       └── financial-engine-scenarios.csv
│   │   │   ├── methodology/
│   │   │   │   └── test-plan.md
│   │   │   ├── rubrics/
│   │   │   │   └── scoring-guide.md
│   │   │   └── results/
│   │   ├── modules/
│   │   ├── use-cases/
│   │   ├── compliance/
│   │   ├── training/
│   │   ├── adversarial-testing/
│   │   ├── ai-collaboration/
│   │   ├── failure-modes/
│   │   └── confidence-calibration/
│   │
│   ├── financial-validation-engine/      # Financial reasoning validation
│   │   └── benchmarks/
│   │
│   ├── legal-engine-2-v1.5/              # Compliance-focused legal v1.5
│   │   ├── benchmarks/
│   │   ├── compliance/
│   │   ├── integrations/
│   │   ├── modules/
│   │   ├── use-cases/
│   │   ├── adversarial-testing/
│   │   └── ai-collaboration/
│   │
│   ├── legal-engine-v2.2/                # Primary legal engine v2.2
│   │   ├── benchmarks/
│   │   ├── modules/
│   │   ├── use-cases/
│   │   ├── compliance/
│   │   ├── training/
│   │   ├── adversarial-testing/
│   │   └── ai-collaboration/
│   │
│   ├── medical-engine-v2.6/              # GOLD STANDARD - Medical v2.6
│   │   ├── benchmarks/
│   │   │   ├── README.md
│   │   │   ├── test-scenarios/
│   │   │   │   ├── baseline/
│   │   │   │   └── engine/
│   │   │   ├── methodology/
│   │   │   ├── rubrics/
│   │   │   └── results/
│   │   ├── clinical-use-cases/
│   │   ├── compliance/
│   │   ├── integrations/
│   │   │   └── fhir-export-templates/
│   │   ├── modules/
│   │   │   └── specialty-modules/
│   │   ├── training/
│   │   ├── adversarial-testing/
│   │   ├── ai-collaboration/
│   │   ├── failure-modes/
│   │   └── confidence-calibration/
│   │
│   └── regulatory-engine-v2.5/           # Regulatory compliance v2.5
│       ├── benchmarks/
│       ├── modules/
│       ├── use-cases/
│       ├── compliance/
│       ├── training/
│       ├── integrations/
│       ├── adversarial-testing/
│       └── ai-collaboration/
│
└── tier-4-experimental/                  # Experimental engines (5 engines)
    ├── anti-fragility-stress-test/       # Stress testing
    │   └── benchmarks/
    ├── cultural-lens-engine/             # Cultural adaptation
    │   └── benchmarks/
    ├── medical-engine-v3-preview/        # Next-gen medical preview
    │   └── benchmarks/
    ├── quantum-computing-simulator/      # Quantum computing
    │   └── benchmarks/
    └── truth-engine/                     # Truth verification
        └── benchmarks/
```

---

## Benchmark Infrastructure (NEW)

All 30 engines include standardized benchmark folders:

```
benchmarks/                           # Per-engine benchmark folder
├── README.md                         # Target metrics, validation status
├── test-scenarios/
│   ├── baseline/                     # Standard LLM prompts (no engine)
│   │   └── [engine]-baseline-scenarios.csv
│   └── engine/                       # Engine-augmented prompts
│       └── [engine]-engine-scenarios.csv
├── methodology/
│   └── test-plan.md                  # Reproducible testing methodology
├── rubrics/
│   └── scoring-guide.md              # Standardized scoring criteria
└── results/                          # Validated results (when available)
```

### Benchmark Status by Tier

| Tier | Engines | Benchmark Folders | Status |
|------|---------|-------------------|--------|
| Tier-0 Template | 1 | ✓ | Template Complete |
| Tier-1 Foundation | 7 | ✓ | Target Metrics |
| Tier-2 Cognitive | 10 | ✓ | Target Metrics |
| Tier-3 Domain | 8 | ✓ | Target Metrics + Samples |
| Tier-4 Experimental | 5 | ✓ | Planned |
| **TOTAL** | **31** | **✓** | **100% Coverage** |

---

## Innovative Beyond-Enterprise Folders (NEW)

Domain engines include cutting-edge folders no enterprise currently uses:

```
engine-name/
├── adversarial-testing/      # Red team attack scenarios
│   └── README.md
├── ai-collaboration/         # Platform-specific optimization
│   └── README.md             # ChatGPT, Claude, Gemini optimization
├── failure-modes/            # FMEA proactive failure analysis
│   └── README.md
└── confidence-calibration/   # Accuracy-confidence alignment
    └── README.md
```

---

## Frameworks Directory

Reasoning frameworks organized by domain:

```
frameworks/
│
├── argumentation-theory/     # Argumentation structures
├── cognitive/                # Cognitive reasoning models
├── creative/                 # Creative thinking frameworks
├── decision-theory/          # Decision-making models
├── document-verification/    # Document authenticity
├── domain-specific/          # Domain-specialized frameworks
│   ├── healthcare/           # Healthcare-specific
│   ├── legal/                # Legal-specific
│   └── scientific/           # Scientific-specific
├── epistemology/             # Knowledge and belief
├── medical-specialized/      # Medical frameworks
├── social/                   # Social reasoning
└── technical/                # Technical frameworks
```

---

## Documentation Structure

```
docs/
│
├── case-library/                        # Case study library
│   ├── failure-analysis/                # Failure case studies
│   ├── lessons-learned/                 # Lessons learned
│   └── success-stories/                 # Success case studies
├── domain-crosswalks/                   # Cross-domain mappings
├── implementation-playbooks/            # Step-by-step playbooks
│   ├── academic-research-institution.md
│   ├── government-agency-setup.md
│   ├── hospital-system-rollout.md
│   ├── law-firm-deployment.md
│   └── startup-rapid-integration.md
│
├── choosing-right-engine.md             # Engine selection guide
├── clinical-validation-methodology.md   # Clinical validation
├── contamination-free-design.md         # Anti-contamination
├── epistemic-standards.md               # Epistemic guidelines
├── faq.md                               # FAQ
├── getting-started.md                   # Getting started
├── GITHUB-DISCOVERABILITY-STRATEGY.md   # GitHub optimization
├── medical-ai-safety-principles.md      # Medical safety
├── medical-engine-compliance-guide.md   # Compliance guide
├── medical-engine-faq.md                # Medical FAQ
├── medical-engine-implementation-guide.md # Implementation
├── medical-engine-philosophy.md         # Philosophy
├── philosophy.md                        # Overall philosophy
├── roadmap.md                           # Development roadmap
└── safety-guidelines.md                 # Safety guidelines
```

---

## Security & Resilience

```
security-resilience/
│
├── defense-frameworks/           # Defensive strategies
│   ├── api-abuse-prevention.md
│   ├── ddos-protection-protocols.md
│   ├── economic-attack-defense.md
│   ├── legal-shield-frameworks.md
│   └── reputation-protection.md
│
├── security-engines/             # Security-focused engines
│   ├── anti-fraud-economist.md
│   ├── exploit-mapper-engine.md
│   ├── fail-safe-recovery-engine.md
│   ├── red-team-commander-engine.md
│   └── trust-safety-architect.md
│
└── sentinel-architecture/        # 15-Sentinel System
    ├── 15-sentinel-specification.md
    ├── competitive-defense-strategies.md
    ├── resilience-frameworks.md
    └── threat-detection-protocols.md
```

---

## International Compliance

```
international/
│
├── cultural-adaptations/         # Cultural localization
│   ├── cultural-safety-frameworks/
│   ├── language-localization-tools/
│   └── localization-guides/
│
├── global-standards/             # Global regulatory standards
│   ├── eu-ai-act-compliance.md
│   ├── global-data-protection-map.md
│   ├── iec-62304-medical-software.md
│   ├── iso-13485-medical-devices.md
│   └── nist-ai-risk-management.md
│
├── legal-jurisdictions/          # Jurisdiction-specific
│   ├── california-consumer-privacy-act.md
│   ├── cross-border-data-transfer.md
│   ├── gdpr-compliance-engine.md
│   └── singapore-pdpa-framework.md
│
└── medical-regulations/          # Medical regulatory bodies
    ├── australia-tga-framework.md
    ├── china-nmpa-regulations.md
    ├── eu-mdr-compliance.md
    ├── health-canada-requirements.md
    ├── japan-pmda-standards.md
    └── uk-mhra-guidance.md
```

---

## Tools & Utilities

```
tools/
│
├── api-gateway/                  # API management
├── cinematic-engine-tools/       # Video/content tools
├── economy-system-tools/         # Economic system utilities
├── interoperability/             # Cross-system compatibility
├── legal-engine-tools/           # Legal utilities
├── medical-engine-tools/         # Medical utilities
│   ├── audit-trail-formatter.py
│   ├── citation-verifier.py
│   ├── drug-interaction-checker.py
│   ├── mode-selector-wizard.md
│   └── phi-detector-standalone.py
├── monitoring/                   # System monitoring
├── scientific-engine-tools/      # Scientific utilities
├── validation-tools/             # Output validation
│
├── compatibility-checker.md      # Compatibility guide
├── engine-selector.md            # Engine selection tool
└── README.md
```

---

## Whitepapers

```
whitepapers/
│
├── ai-safety/                    # AI safety research
├── cross-domain-ai/              # Cross-domain integration
│   ├── ai-interoperability-standards.pdf
│   ├── future-of-specialized-ai.pdf
│   └── multi-domain-reasoning-framework.pdf
├── medical-ai/                   # Medical AI research
│   ├── clinical-validation-best-practices.pdf
│   ├── future-of-ai-in-medicine.pdf
│   ├── medical-ai-liability-landscape.pdf
│   ├── phi-protection-strategies.pdf
│   └── reducing-hallucinations-clinical-ai.pdf
├── ocean-spec-tech/              # OCEAN architecture
├── templates/                    # Whitepaper templates
│   ├── 01-problem-solution-template.md
│   ├── 02-research-insight-template.md
│   ├── 03-technical-deepdive-template.md
│   ├── 04-strategic-framework-template.md
│   └── 05-state-of-industry-template.md
│
├── README.md                     # Whitepapers index
└── WHITEPAPER-BLUEPRINT.md       # How to write whitepapers
```

---

## Tutorials

```
tutorials/
│
├── videos/                       # Video tutorials
│
├── 01-absolute-beginner-start-here.md
├── 02-choosing-right-engine.md
├── 03-using-with-chatgpt.md
├── 04-using-with-claude.md
├── 05-using-with-gemini.md
├── 06-combining-multiple-engines.md
├── 07-creating-custom-engines.md
├── 08-troubleshooting.md
├── 09-medical-engine-setup.md
├── 10-medical-engine-first-use.md
├── 11-medical-engine-advanced-features.md
├── 12-medical-engine-ehr-integration.md
├── 13-legal-engine-international-use.md
├── 14-scientific-research-workflow.md
├── 15-cross-domain-integration.md
├── 16-cinematic-engine-setup.md
├── 17-economy-system-implementation.md
└── 18-security-sentinel-deployment.md
```

---

## Legal Framework (v3.1)

Comprehensive legal documentation with 38 documents across 8 categories:

```
legal/
│
├── README.md                           # Legal Documentation Hub (v3.1)
│
├── Core Legal Documents (6)
│   ├── LEGAL-DISCLAIMER.md             # Fundamental legal position
│   ├── LIABILITY-SHIELD.md             # 10-layer liability protection
│   ├── TERMS-OF-USE.md                 # Acceptable use policies
│   ├── LICENSE-EXPLANATION.md          # Apache 2.0 interpretation
│   ├── AI-ETHICS-STATEMENT.md          # NEW: Multi-domain responsible AI principles
│   └── TRADEMARK-USAGE-POLICY.md       # NEW: AION/AI-ON brand protection
│
├── Enterprise & Security (2)
│   ├── ENTERPRISE-SECURITY-COMPLIANCE.md  # NEW: SOC 2, ISO 27001, NIST guidance
│   └── INCIDENT-REPORTING-GUIDE.md        # NEW: Multi-domain incident response
│
├── Professional Practice (2)
│   ├── PROFESSIONAL-BOUNDARIES.md      # Licensed professional oversight
│   └── MALPRACTICE-DEFENSE-GUIDE.md    # Audit trail templates
│
├── Regulatory Compliance (2)
│   ├── FDA-REGULATORY-STATUS.md        # FDA CDS classification
│   └── HIPAA-COMPLIANCE-STATEMENT.md   # PHI handling framework
│
├── INTERNATIONAL-COMPLIANCE/           # 11 Jurisdictions
│   ├── README.md                       # Global regulatory index
│   ├── EU-MDR-COMPLIANCE.md            # European Union
│   ├── UK-MHRA-GUIDANCE.md             # United Kingdom
│   ├── HEALTH-CANADA-REQUIREMENTS.md   # Canada
│   ├── JAPAN-PMDA-STANDARDS.md         # Japan
│   ├── CHINA-NMPA-REGULATIONS.md       # China (with PIPL)
│   ├── AUSTRALIA-TGA-FRAMEWORK.md      # Australia
│   ├── INDIA-CDSCO-FRAMEWORK.md        # India
│   ├── SOUTH-KOREA-MFDS-FRAMEWORK.md   # South Korea
│   ├── BRAZIL-ANVISA-FRAMEWORK.md      # Brazil
│   └── SOUTH-AFRICA-SAHPRA-FRAMEWORK.md # South Africa
│
├── CROSS-BORDER/                       # Cross-border operations
│   ├── JURISDICTION-GUIDANCE.md        # Multi-jurisdictional strategy
│   ├── DATA-TRANSFER-AGREEMENTS.md     # GDPR SCCs, UK IDTA
│   └── INTELLECTUAL-PROPERTY-MAP.md    # IP across jurisdictions
│
├── AGREEMENTS/                         # 11 Contract Templates
│   ├── README.md                       # Template repository overview
│   ├── MUTUAL-NDA.md                   # Bidirectional confidentiality
│   ├── UNILATERAL-NDA.md               # One-way confidentiality
│   ├── CONTRIBUTOR-LICENSE-AGREEMENT.md # Open-source contribution IP
│   ├── RESEARCH-COLLABORATION-AGREEMENT.md # Academic partnerships
│   ├── DATA-PROCESSING-AGREEMENT.md    # GDPR/privacy compliance
│   ├── BUSINESS-ASSOCIATE-AGREEMENT.md # HIPAA compliance
│   ├── ENTERPRISE-LICENSE-ADDENDUM.md  # Commercial deployment
│   ├── PROFESSIONAL-SERVICES-AGREEMENT.md # Consulting/implementation
│   ├── JOINT-DEVELOPMENT-AGREEMENT.md  # Co-development partnerships
│   └── INTEGRATION-PARTNER-AGREEMENT.md # Reseller/channel partners
│
└── LEGAL-ROADMAP.md                    # Future development phases
```

### Legal Framework Features

| Feature | Description |
|---------|-------------|
| 10-Role Genius Council | Multi-perspective validation on all documents |
| 3-Engine Integration | Legal v2.2 + Legal 2 v1.5 + Regulatory v2.5 |
| NO PERSONAL LIABILITY | Zero personal liability for Sheldon K Salmon |
| Multi-Domain Coverage | Medical, Legal, Financial, Security, Research |
| 11 Jurisdictions | Global regulatory compliance coverage |
| 11 Contract Templates | Business enablement with professional oversight |

---

## Assets Directory

```
assets/
│
├── badges/                             # Shield badges for README
├── images/                             # Visual assets
│   ├── aion-official-logo.jpg          # NEW: Official AION Shield Logo
│   ├── logo.png                        # Standard logo
│   ├── logo-medical-engine.png
│   ├── logo-legal-engine.png
│   ├── logo-scientific-engine.png
│   ├── logo-security-sentinels.png
│   ├── logo-cinematic-engine.png
│   ├── logo-economy-system.png
│   ├── banner.png
│   ├── banner-medical-engine.png
│   ├── banner-cross-domain.png
│   ├── banner-civilization-scale.png
│   └── diagrams/                       # Architecture diagrams
├── presentations/                      # PDF presentations
└── videos/                             # Video assets
```

---

## Navigation Guide

**Looking for...**

| If You Want To... | Go To... |
|-------------------|----------|
| Get started quickly | `QUICK-START-CHEAT-SHEET.md` |
| Fast overview | `README-LITE.md` |
| Choose an engine | `docs/choosing-right-engine.md` |
| Understand the architecture | `ARCHITECT.md` |
| See all engines | `engines/` |
| Understand benchmarks | `engines/BENCHMARKS-OVERVIEW.md` |
| Create a new engine | `engines/tier-0-template/` |
| Read the philosophy | `MANIFESTO.md` |
| Understand the vision | `VISION.md` |
| Read the story | `STORY.md` |
| Read research papers | `whitepapers/` |
| Deploy to cloud | `deployment/cloud-templates/` |
| Ensure compliance | `international/` or `legal/` |
| Build custom personas | `engines/tier-2-cognitive-architecture/personality-architect-v1.0/` |
| Manage complexity | `engines/tier-1-foundation/complexity-management-engine/` |
| Support the project | `SUPPORT.md` |
| Contribute | `CONTRIBUTING.md` |
| Report security issues | `SECURITY.md` |

---

## File Naming Conventions

| Pattern | Meaning |
|---------|---------|
| `engine-name-vX.Y/` | Versioned engine (X.major, Y.minor) |
| `README.md` | Folder index/overview |
| `*.pdf` | Published/finalized documents |
| `*.md` | Markdown documentation |
| `*.py` | Python utility scripts |
| `*.csv` | Test scenario data files |
| `*.yml/.yaml` | Configuration files |
| `UPPERCASE.md` | Top-level repository files |

---

## Version History

| Date | Changes |
|------|---------|
| November 28, 2025 | **Benchmark Engine v2.0 (METIS-II)**: Added Trinity Scoring, Benchmark Freshness, Audience Reports integrations |
| November 28, 2025 | Added 7 working Python engine implementations with 394 total passing tests |
| November 28, 2025 | Updated structure with complete src/ folder details for all flagship engines |
| November 2025 | Added tier-0 template, benchmark infrastructure to all 30 engines |
| November 2025 | Updated tier-3 engines: Medical v2.6, Legal v2.2, Legal 2 v1.5, Financial v1.5, Crisis v1.5, Regulatory v2.5 |
| November 2025 | Added innovative folders: adversarial-testing, ai-collaboration, failure-modes, confidence-calibration |
| November 2025 | Rebranded from AION Cognitive Engines to AION-BRAIN |
| November 2025 | Updated license to Apache 2.0 |
| November 2025 | Legal Framework v3.1: Added AI Ethics Statement, Trademark Policy, Enterprise Security Compliance, Incident Reporting Guide |
| November 2025 | Added 11 contract templates for business enablement |
| November 2025 | Added official AION Shield Logo (assets/images/aion-official-logo.jpg) |

---

## Flagship Engine Summary

| Engine | Codename | Key Capability | v2.0 Integrations |
|--------|----------|----------------|-------------------|
| **Oracle Layer v2.1** | PROMETHEUS | Zero-hallucination verification | - |
| **SIMPLEXITY v2.0** | - | 8-module complexity management | - |
| **Strategy Engine v1.1** | The Strategist's Edge | 5-framework competitive analysis | - |
| **Decision Engine v1.0** | DECIDERE | 5-framework decision support | - |
| **Credibility Engine v2.0** | VERITAS | 7-module trust acceleration | - |
| **Explanation Engine v1.0** | CLARITAS | 4-generator explainability | - |
| **Benchmark Engine v2.0** | METIS-II | Universal AI safety validation | Trinity Scoring + Freshness + Audience Reports |

---

*This structure map is maintained in `.aions-structure-list/`*

*AION-BRAIN — Humanity's cognitive infrastructure for the AI age.*
