# Marketplace Submission Guidelines

How to submit extensions, integrations, and derivative engines to the AION-BRAIN Marketplace.

---

## About the Marketplace

The AION-BRAIN Marketplace is a curated collection of community-created:
- **Extensions** — Add-ons that enhance core engines
- **Integrations** — Connectors to other platforms
- **Derivative Engines** — New engines built on AION-BRAIN principles
- **Templates** — Ready-to-use configurations
- **Tools** — Utilities that support AION-BRAIN usage

---

## Marketplace Status

**Current Status:** Planning Phase

The marketplace is currently in development. We're accepting early submissions for review and inclusion when the marketplace launches.

---

## What We Accept

### Extensions

| Type | Description | Example |
|------|-------------|---------|
| **Engine enhancers** | Add capabilities to existing engines | Additional output formats |
| **Workflow add-ons** | Multi-engine workflow components | Chained engine templates |
| **Output processors** | Process engine outputs | Visualization tools |
| **Input enhancers** | Improve input processing | Context preprocessors |

### Integrations

| Type | Description | Example |
|------|-------------|---------|
| **Platform connectors** | Connect to other platforms | Slack integration |
| **Data source adapters** | Pull from data sources | Research database connector |
| **Output destinations** | Send outputs elsewhere | Documentation generator |
| **Workflow automation** | Automate engine usage | Scheduled analysis |

### Derivative Engines

| Type | Description | Example |
|------|-------------|---------|
| **Domain-specific** | Engines for specific industries | Veterinary Engine |
| **Specialized** | Focused capability engines | Interview Analyzer |
| **Experimental** | Novel engine concepts | Emerging domain coverage |

### Templates

| Type | Description | Example |
|------|-------------|---------|
| **Prompt templates** | Ready-to-use prompts | Industry-specific prompts |
| **Configuration templates** | Pre-configured setups | Enterprise deployment config |
| **Workflow templates** | Multi-step workflows | Due diligence workflow |

---

## Submission Requirements

### All Submissions

| Requirement | Description |
|-------------|-------------|
| **Documentation** | Clear README with purpose, usage, requirements |
| **License** | Apache 2.0 or compatible open-source license |
| **Quality** | Meets quality standards (see [quality-standards.md](quality-standards.md)) |
| **Testing** | Demonstrated working implementation |
| **Attribution** | Proper attribution to AION-BRAIN |

### Extensions and Integrations

| Requirement | Description |
|-------------|-------------|
| **Compatibility** | Works with current AION-BRAIN version |
| **Security** | No security vulnerabilities |
| **Performance** | Acceptable performance characteristics |
| **Error handling** | Graceful error handling |

### Derivative Engines

| Requirement | Description |
|-------------|-------------|
| **AION Principles** | Follows core AION-BRAIN principles |
| **Specification** | Complete specification document |
| **Prompt** | Ready-to-use prompt template |
| **Examples** | Documented examples |
| **Disclaimers** | Appropriate domain disclaimers |

---

## Submission Process

### Step 1: Prepare Your Submission

**Create your package with:**

```
your-submission/
├── README.md              # Overview, purpose, usage
├── CHANGELOG.md           # Version history
├── LICENSE                # Apache 2.0 or compatible
├── docs/
│   ├── installation.md    # How to install/use
│   ├── configuration.md   # Configuration options
│   └── examples.md        # Usage examples
├── src/                   # Source code (if applicable)
└── tests/                 # Test cases (if applicable)
```

**README must include:**

```markdown
# [Submission Name]

## Overview
[Brief description]

## Purpose
[What problem does this solve?]

## Requirements
[Prerequisites and dependencies]

## Installation
[How to install/use]

## Usage
[How to use, with examples]

## Compatibility
[AION-BRAIN version compatibility]

## License
[License information]

## Author
[Your information]

## Changelog
[Link to CHANGELOG.md]
```

### Step 2: Self-Review

**Before submitting, verify:**

- [ ] Documentation is complete
- [ ] Code is tested and working
- [ ] Quality standards are met
- [ ] License is included
- [ ] Attribution is correct
- [ ] No security issues
- [ ] Examples are provided

### Step 3: Submit

**Via GitHub:**
1. Fork the AION-BRAIN repository
2. Add your submission to `community/marketplace-submissions/`
3. Submit a Pull Request
4. Use title: "Marketplace Submission: [Name]"

**Via Email:**
1. Email: AIONSYSTEM@outlook.com
2. Subject: "Marketplace Submission: [Name]"
3. Include: ZIP file or repository link
4. Include: Description and category

### Step 4: Review

| Stage | Duration | Activities |
|-------|----------|------------|
| Initial Review | 1-2 weeks | Documentation, structure check |
| Technical Review | 1-2 weeks | Code review, testing |
| Quality Review | 1 week | Quality standards assessment |
| Decision | — | Accept, revise, or decline |

### Step 5: Publication

**If accepted:**
1. Submission is added to marketplace
2. You're notified of publication
3. Submission is promoted to community
4. You're credited as the creator

---

## Submission Categories

### Free Submissions

| Category | Description |
|----------|-------------|
| Community contributions | Open-source, free to use |
| Personal projects | Individual creations |
| Educational resources | Learning materials |

### Premium Submissions (Future)

| Category | Description |
|----------|-------------|
| Commercial extensions | Paid add-ons |
| Enterprise integrations | Premium connectors |
| Professional services | Bundled with services |

See [revenue-sharing-model.md](revenue-sharing-model.md) for premium submission terms.

---

## Review Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Quality** | 30% | Meets quality standards |
| **Usefulness** | 25% | Solves real problems |
| **Documentation** | 20% | Complete, clear docs |
| **Alignment** | 15% | Follows AION principles |
| **Originality** | 10% | Novel contribution |

---

## After Submission

### If Accepted

- Submission is published to marketplace
- You're credited as creator
- You're responsible for maintenance
- Community can provide feedback
- Updates can be submitted

### If Revision Requested

- Feedback provided on needed changes
- Revise and resubmit
- Re-review upon resubmission

### If Declined

- Reason provided
- Can revise and resubmit
- Can appeal decision
- Feedback for improvement

---

## Maintenance

### Creator Responsibilities

| Responsibility | Description |
|----------------|-------------|
| Bug fixes | Address reported issues |
| Compatibility | Update for new versions |
| Documentation | Keep docs current |
| Support | Respond to user questions |

### Marketplace Support

| Support Type | Description |
|--------------|-------------|
| Listing management | We manage the listing |
| Visibility | We promote quality submissions |
| Feedback channel | We facilitate user feedback |
| Issue escalation | We escalate critical issues |

---

## Questions?

**General Questions:** GitHub Discussions
**Submission Questions:** AIONSYSTEM@outlook.com

---

*Last updated: November 2025*
