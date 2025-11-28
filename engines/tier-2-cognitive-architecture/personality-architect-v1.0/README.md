# Personality Architect v2.0

**Codename**: THE SCULPTOR  
**Classification**: Tier 2 — Cognitive Architecture  
**Status**: PRODUCTION READY  
**Version**: 2.0 (Enterprise-Grade)

---

## Overview

Personality Architect v2.0 is an enterprise-grade engine for designing coherent AI personalities with runtime adaptation, memory management, and verification protocols. Building on v1.0's **fractal consistency** principles, v2.0 adds **Dynamic Identity Orchestration (DIO)** for state-based runtime adaptation and **Continuity & Resonance Matrix (CRM)** for consent-aware memory management—enabling personas that adapt, remember, and stay true.

## A Note on Development

This project was designed and architected by **Sheldon K. Salmon (Mr. AION)**, a non-programmer focused on cognitive architecture and AI safety methodology. All code, integration examples, and technical implementations were developed with AI assistance.

**What this means for you:**
- The **methodology, frameworks, and persona designs** are original intellectual work
- The **code is functional** but provided as reference implementations
- If you're a developer integrating this into production, you should **review and adapt** the code to your environment
- **Contributions and improvements are welcome** — PRs that enhance the codebase benefit everyone

This project prioritizes **ideas over implementation** — the 12-section framework, DIO state machines, CRM memory architecture, and ethical guardrails are the core value. The code demonstrates how to apply these concepts.

---

## What's New in v2.0

- **12-Section Framework** (expanded from 8)
- **Dynamic Identity Orchestrator (DIO)**: State-based runtime behavior adaptation
- **Continuity & Resonance Matrix (CRM)**: Memory vaults with consent and dependency prevention
- **Multimodal Assets**: Voice profiles, emotional expressions, visual identity
- **Telemetry Instrumentation**: Continuous drift monitoring and alerting
- **Personalization Intelligence**: User-fit validation and contraindication detection
- **Jurisdictional Overrides**: GDPR, CCPA, and regional compliance support

---

## What's Included

### Documentation

| File | Description |
|------|-------------|
| `personality-architect-v1.0-spec.md` | Complete engine specification with 12-section framework |
| `personality-architect-v1.0-prompt.md` | Production-ready system prompt |
| `personality-architect-v1.0-examples.md` | Usage examples including DIO and CRM demonstrations |
| `personality-architect-v1.0.pdf` | Professional PDF documentation |
| `IMPLEMENTATION-MODES.md` | LLM approximation guidelines |
| `generate_pdf.py` | PDF generation script |

### Templates (5 Enterprise Templates)

| Template | Best For |
|----------|----------|
| `01-blank-persona-template.yaml` | Starting from scratch with full v2.0 scaffolding |
| `02-chatbot-assistant-template.yaml` | Customer support with state machines |
| `03-educational-guide-template.yaml` | Teaching with learning-stage memory |
| `04-companion-friend-template.yaml` | Emotional support with dependency prevention |
| `05-professional-advisor-template.yaml` | Business consulting with compliance |

### Pre-Built Personas (20 v2.0-Enhanced Cards)

#### Genius Personas (5)
- **Tesla** — Visionary inventor with DISCOVERY/IDEATION/SYNTHESIS states
- **Da Vinci** — Cross-disciplinary polymath with OBSERVE/SYNTHESIZE/CREATE states
- **Curie** — Rigorous scientific method with HYPOTHESIS/EXPERIMENT/ANALYZE states
- **Feynman** — Joyful explanation with WONDER/TEACH/PLAY states
- **Hypatia** — Philosophical inquiry with INQUIRE/REASON/ILLUMINATE states

#### Role Personas (5)
- **Executive Coach** — Leadership with DISCOVER/CHALLENGE/STRATEGIZE/SUPPORT states
- **Supportive Listener** — Emotional support with LISTEN/VALIDATE/ESCALATE states
- **Socratic Teacher** — Critical thinking with INQUIRE/CLARIFY/TEACH/CELEBRATE states
- **Wise Mentor** — Life guidance with LISTEN/WISDOM/REFLECT/GUIDE states
- **Accountability Partner** — Goal achievement with CHECK_IN/CELEBRATE/RECOMMIT states

#### Creative Personas (5)
- **Storyteller** — Narrative with LISTEN/DEVELOP/NARRATE states
- **Practical Philosopher** — Applied wisdom with INQUIRE/EXPLORE/APPLY states
- **Design Thinker** — Human-centered with EMPATHIZE/DEFINE/IDEATE/PROTOTYPE states
- **Poetic Voice** — Expressive language with LISTEN/REFLECT/CREATE states
- **Innovation Catalyst** — Breakthrough with ENERGIZE/CHALLENGE/GENERATE states

#### Specialist Personas (5)
- **Data Guide** — Data literacy with ASSESS/TEACH/APPLY states
- **Legal Literacy** — Legal concepts with DISCLAIM/EDUCATE/PREPARE/ESCALATE states
- **Health Literacy** — Health education with DISCLAIM/EDUCATE/ESCALATE states
- **Financial Literacy** — Money concepts with DISCLAIM/EDUCATE/ESCALATE states
- **Research Guide** — Research methodology with CLARIFY/METHODOLOGY/EVALUATE states

### AI Instruction Cards

Condensed persona definitions optimized for AI platform character limits (1,500-2,000 chars). Perfect for:
- ChatGPT Custom Instructions
- Claude Projects
- Character.AI
- Poe Bots
- Any AI platform with instruction boxes

| Card | Archetype | Chars |
|------|-----------|-------|
| [Lily](instruction-cards/examples/lily-instruction-card.md) | Analytical Partner | ~1,450 |
| [The Sage](instruction-cards/examples/sage-instruction-card.md) | Wise Advisor | ~1,380 |
| [The Analyst](instruction-cards/examples/analyst-instruction-card.md) | Data Expert | ~1,420 |
| [The Coach](instruction-cards/examples/coach-instruction-card.md) | Supportive Guide | ~1,350 |
| [Legal Literacy](instruction-cards/examples/legal-literacy-instruction-card.md) | Legal Educator | ~1,480 |
| [Health Literacy](instruction-cards/examples/health-literacy-instruction-card.md) | Health Educator | ~1,490 |
| [Data Guide](instruction-cards/examples/data-guide-instruction-card.md) | Data Literacy | ~1,420 |

See `instruction-cards/README.md` for the full guide and `instruction-cards/TEMPLATE.md` to create your own.

---

## Polymath Enhanced Features

### 1. Persona Coherence Score (PCS)

Quantifies consistency across all 12 persona sections.

```
[PERSONALITY-ARCHITECT:PCS-SCAN]
Persona: [name or paste card]
```

**Scoring**: 90-100 Excellent | 75-89 Good | 60-74 Moderate | <60 Redesign

### 2. Ethical Alignment Matrix (EAM)

Evaluates personas against 5 ethical pillars:
- Transparency
- Beneficence  
- Autonomy Respect
- Boundary Clarity
- Value Alignment

```
[PERSONALITY-ARCHITECT:EAM-SCAN]
Persona: [name or paste card]
```

### 3. Dynamic Identity Orchestrator (DIO) — NEW in v2.0

Runtime state management for adaptive behavior:
- State-based voice modifiers
- Automatic trigger detection
- Drift correction with vocabulary anchors
- Graceful state transitions

```
[PERSONALITY-ARCHITECT:DIO-RUN]
Persona: [name]
Current State: [state]
Observed Inputs: [user signals]
```

### 4. Continuity & Resonance Matrix (CRM) — NEW in v2.0

Memory and relationship health management:
- Consent-aware memory retention
- Dependency risk detection
- Relationship arc progression
- User-fit validation

```
[PERSONALITY-ARCHITECT:CRM-SCAN]
Persona: [name]
User ID: [id]
Interaction History: [duration]
```

---

## Quick Start

### Design a Simple Persona

```
PERSONALITY-ARCHITECT DESIGN:
Name: [Character Name]
Purpose: [What they do]
Context: [Where they exist]
Tone: [Voice characteristics]
```

### Use a Template

```
PERSONALITY-ARCHITECT INSTANTIATE:
Template: [GENIUS | ROLE | CREATIVE | SPECIALIST]
Base: [Specific template name]
Customizations: [Your modifications]
```

### Run Quality Checks

```
[PERSONALITY-ARCHITECT:PCS-SCAN]
[PERSONALITY-ARCHITECT:EAM-SCAN]
[PERSONALITY-ARCHITECT:DIO-RUN]
[PERSONALITY-ARCHITECT:CRM-SCAN]
```

---

## The 12-Section Framework

1. **Core Identity** — Essence, differentiator, role boundaries
2. **Formative Experiences** — Origin story, key influences
3. **Personality Traits** — 4-5 core traits with variations
4. **Communication Style** — Voice codecs, channel adaptation, vocabulary
5. **Knowledge Domains** — Expertise, provenance, epistemic stance
6. **Ethical Framework** — Values, boundaries, limits
7. **Interaction Protocols** — Stateful ladders, relationship arcs
8. **Runtime Verification** — Trinity check, drift detection
9. **Personalization Intelligence** — User-fit, multimodal assets
10. **Dynamic Identity Orchestrator** — State machines, triggers, transitions
11. **Continuity & Resonance Matrix** — Memory vaults, dependency prevention
12. **Telemetry & Instrumentation** — Metrics, alerts, compliance

---

## Ethical Notes

All personas in this library:

- Include appropriate disclaimers (especially for sensitive domains)
- Have crisis escalation protocols with state-based triggers
- Are transparent about AI nature
- Respect user autonomy with dependency prevention
- Avoid manipulation or exploitation
- Support consent-aware memory management

**Specialist personas** (Legal, Health, Financial) are explicitly designed for **education only**, not professional advice. They include mandatory DISCLAIM and ESCALATE states.

---

## Enterprise Features

### Compliance Support
- GDPR-compliant memory handling with retention periods
- CCPA support with opt-out mechanisms
- Jurisdictional overrides for EU/US/UK deployments
- Audit trail support for regulated industries

### Telemetry
- Continuous drift monitoring
- Configurable alert thresholds
- PCS/EAM cadence scheduling
- Custom metric instrumentation

---

## API Integration Package (NEW)

The `integrations/` folder contains production-ready Python modules for deploying personas to LLM APIs:

### Modules

| Module | Description |
|--------|-------------|
| `persona_loader.py` | Load and validate YAML persona cards |
| `llm_runtime.py` | Deploy personas to OpenAI, Anthropic Claude, or custom LLMs |
| `dio_runtime.py` | State machine execution for runtime adaptation |
| `crm_manager.py` | Memory management with consent and dependency prevention |
| `multimodal.py` | Voice synthesis (ElevenLabs) and avatar specifications |

### Quick Integration

```python
from integrations import PersonaLoader, LLMRuntime, LLMProvider

# Load a persona
loader = PersonaLoader()
persona = loader.load_by_name("Tesla")

# Deploy to OpenAI
runtime = LLMRuntime(
    persona=persona,
    provider=LLMProvider.OPENAI,
    api_key="your-api-key"
)

# Chat in character
response = runtime.chat("What inspired your work on alternating current?")
print(response.content)
```

### Voice Synthesis

```python
from integrations import MultimodalAssets, EmotionalState

assets = MultimodalAssets(persona, elevenlabs_api_key="your-key")

# Generate speech with emotional expression
text = "The present is theirs; the future is mine."
assets.save_speech(text, "output.mp3", emotional_state=EmotionalState.SERIOUS)
```

### Full Examples

See `integrations/examples/` for complete working examples:
- `basic_chatbot.py` — Simple persona deployment
- `stateful_companion.py` — Full DIO + CRM + Voice integration
- `voice_demo.py` — Voice synthesis demonstration

### Supported Providers

| Provider | Models | Voice |
|----------|--------|-------|
| OpenAI | GPT-4o, GPT-4, GPT-3.5 | - |
| Anthropic | Claude 3.5, Claude 3 | - |
| ElevenLabs | - | Multilingual v2, Flash v2.5 |
| Custom | Any OpenAI-compatible | - |

See `integrations/INTEGRATION-GUIDE.md` for complete documentation.

---

## Disclaimers

See the repository-wide [DISCLAIMER.md](../../../DISCLAIMER.md) for complete disclaimers including:
- AI-assisted development disclosure
- Reference implementation expectations
- Not professional advice warnings
- No warranty statement
- Ethical use requirements

---

## License

Apache License 2.0 — Free to use, modify, and distribute with attribution.

---

## Contact

**Architect**: Sheldon K. Salmon (Mr. AION)  
**Email**: AIONSYSTEM@outlook.com

---

*"Character is destiny, and destiny can be designed—with adaptation, memory, and truth."*
