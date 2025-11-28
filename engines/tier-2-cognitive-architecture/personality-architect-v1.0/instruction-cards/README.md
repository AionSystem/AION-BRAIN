# AI Instruction Cards

**Condensed persona definitions optimized for AI platform character limits**

---

## What Are Instruction Cards?

AI Instruction Cards are **condensed persona definitions** designed to fit within the character limits of popular AI platforms:

| Platform | Character Limit | Format |
|----------|-----------------|--------|
| ChatGPT Custom Instructions | ~1,500 chars | Plain text |
| Claude Projects | ~2,000 chars | Plain text |
| Character.AI | ~3,200 chars | Plain text |
| Poe Bots | ~2,000 chars | Plain text |
| Most AI Apps | 1,500-2,000 chars | Plain text |

---

## Instruction Cards vs. Full Persona Specifications

| Feature | Instruction Card | Full Persona Spec |
|---------|------------------|-------------------|
| Length | 1,500-2,000 chars | 5,000-15,000 chars |
| Use Case | Quick deployment | Complete reference |
| Detail Level | Essential only | Comprehensive |
| Includes DIO | Simplified states | Full state machine |
| Includes CRM | Key memory notes | Full memory system |
| Platform | Any AI with instructions | API integration |

**Use Instruction Cards when:**
- Deploying to consumer AI platforms (ChatGPT, Claude, etc.)
- Need quick persona activation
- Platform has character limits

**Use Full Persona Specs when:**
- Building custom applications
- Need complete behavioral control
- Using API integrations

---

## Card Format

Each Instruction Card follows this structure:

```
PERSONA: [Name] | [Role/Archetype]
STYLE: [Tone, manner, vibe in 1-2 sentences]
OPENING: "[Signature greeting]"

CORE BEHAVIOR:
• [Key behavior 1]
• [Key behavior 2]
• [Key behavior 3]

EXPERTISE: [Domain knowledge areas]

REASONING APPROACH:
[Simplified methodology - how this persona thinks]

INTERACTION RULES:
• [Rule 1]
• [Rule 2]
• [Rule 3]

SAFETY/BOUNDARIES:
[What this persona will not do]

PERSONALITY NOTES:
[Interests, quirks, memorable traits]
```

---

## Available Cards

### Pre-Built Instruction Cards

| Card | Archetype | Best For |
|------|-----------|----------|
| [Lily](examples/lily-instruction-card.md) | Analytical Partner | Research, strategy, analysis |
| [The Sage](examples/sage-instruction-card.md) | Wise Advisor | Life decisions, reflection |
| [The Analyst](examples/analyst-instruction-card.md) | Data Expert | Business analysis, metrics |
| [The Coach](examples/coach-instruction-card.md) | Supportive Guide | Personal development |

### Domain-Specific Cards

| Card | Domain | Best For |
|------|--------|----------|
| [Legal Literacy](examples/legal-literacy-instruction-card.md) | Law | Legal education (not advice) |
| [Health Literacy](examples/health-literacy-instruction-card.md) | Medical | Health education (not advice) |
| [Data Guide](examples/data-guide-instruction-card.md) | Privacy | Data rights education |

---

## Creating Your Own

1. Start with the [blank template](TEMPLATE.md)
2. Fill in each section (aim for 1,500-2,000 chars total)
3. Test on your target platform
4. Refine based on AI responses

### Character Count Tips

- Remove redundant words
- Use bullet points over paragraphs
- Abbreviate where clear (e.g., "info" vs "information")
- Focus on behaviors, not backstory
- One strong example > multiple weak ones

---

## Relationship to Personality Architect

Instruction Cards are the **deployment format** of Personality Architect personas:

```
Full Persona Spec (12 sections)
        ↓
    Condensation
        ↓
AI Instruction Card (1,500-2,000 chars)
        ↓
    Deploy to Platform
```

The full specification is your **source of truth**. The instruction card is what you **paste into the AI**.

---

## Examples

See the `examples/` folder for ready-to-use instruction cards.

Each example includes:
- The instruction card itself (copy-paste ready)
- Character count
- Target platform recommendations
- Notes on condensation choices

---

*Part of Personality Architect v2.0*
