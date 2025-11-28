# Module 1: Jurisdiction Identification

**Engine:** Legal Engine 2 v1.5  
**Purpose:** Identify all applicable legal jurisdictions and resolve conflicts of law

---

## Overview

The Jurisdiction Identification module maps the complete landscape of legal authorities that apply to a given situation. This is the critical first step because every subsequent analysis depends on knowing which laws apply.

---

## CEREBRO Frameworks Activated

| Framework | Application |
|-----------|-------------|
| **Meadows** (Systems) | Nested jurisdictional hierarchies |
| **Barabási** (Networks) | Jurisdictional connection patterns |
| **Pearl** (Causality) | Which jurisdiction's law controls? |
| **Hofstadter** (Self-reference) | Regulatory loops and conflicts |

---

## Step 1: Geographic Jurisdiction Mapping

### Federal Jurisdiction (United States)

**Triggers for Federal Jurisdiction:**
- Transaction crosses state lines (interstate commerce)
- Federal statute directly governs (e.g., FLSA, ADA, securities law)
- Constitutional rights at issue
- Federal agency has jurisdiction (FDA, FTC, SEC, etc.)
- Diversity jurisdiction ($75,000+ and parties from different states)

**Controlling Authority:**
- U.S. Constitution
- United States Code (U.S.C.)
- Code of Federal Regulations (CFR)
- Federal case law (binding in applicable circuit)

### State Jurisdiction

**Primary State Determination:**

| Factor | Weight |
|--------|--------|
| Where contract was formed | High |
| Where performance occurs | High |
| Where parties are domiciled | Medium |
| Where harm occurred (torts) | High |
| Choice of law clause | High (if valid) |

**Secondary States:**
- Additional states with jurisdictional hooks
- Multi-state operations trigger compliance in each state
- "Long-arm" jurisdiction analysis required

**Controlling Authority:**
- State constitution
- State statutes and codes
- State administrative regulations
- State case law

### Local Jurisdiction (County/Municipal)

**Common Local Requirements:**
- County ordinances
- City/municipal codes
- Zoning regulations
- Local licensing requirements
- Local business registration
- Occupancy permits

**Controlling Authority:**
- Local ordinances
- Municipal codes
- County regulations

### International Jurisdiction

**Triggers:**
- Foreign party to transaction
- Processing data of foreign residents (GDPR)
- International shipping or services
- Foreign subsidiary operations

**Controlling Authority:**
- Foreign country statutes
- Treaties and conventions
- International law principles

---

## Step 2: Regulatory Jurisdiction Mapping

### Industry-Specific Regulators

#### Healthcare
| Regulator | Authority |
|-----------|-----------|
| HIPAA/OCR | Health information privacy |
| FDA | Drugs, devices, biologics |
| CMS | Medicare/Medicaid |
| State Boards | Professional licensing |
| DEA | Controlled substances |

#### Financial Services
| Regulator | Authority |
|-----------|-----------|
| SEC | Securities regulation |
| FINRA | Broker-dealer oversight |
| FDIC | Bank insurance |
| CFPB | Consumer financial protection |
| State Banking | State-chartered institutions |
| FinCEN | Anti-money laundering |

#### Data Privacy
| Regulator | Authority |
|-----------|-----------|
| FTC | Unfair/deceptive practices |
| State AGs | State privacy law enforcement |
| CPPA (California) | CCPA/CPRA enforcement |
| DPAs (EU) | GDPR enforcement |
| HHS/OCR | HIPAA enforcement |

#### Employment
| Regulator | Authority |
|-----------|-----------|
| DOL | Wage and hour |
| EEOC | Discrimination |
| NLRB | Labor relations |
| OSHA | Workplace safety |
| State Labor | State wage/hour and safety |

#### Consumer Protection
| Regulator | Authority |
|-----------|-----------|
| FTC | Federal consumer protection |
| State AGs | State UDAP enforcement |
| CFPB | Financial consumer protection |

---

## Step 3: Conflicts of Law Analysis

### Resolution Framework

When multiple jurisdictions apply, resolve conflicts using this priority:

#### 1. Choice of Law Clause Check
```
IF contract contains choice of law clause:
├─ Is it enforceable?
│   ├─ Not unconscionable
│   ├─ Not contrary to public policy
│   └─ Chosen state has reasonable relationship
├─ IF valid → Apply chosen jurisdiction's law
└─ EXCEPTION: Mandatory consumer/employment laws may still apply
```

#### 2. Federal Preemption Analysis
```
IF both federal and state law apply:
├─ EXPRESS PREEMPTION: Statute explicitly preempts
├─ IMPLIED PREEMPTION: Conflicts with federal scheme
├─ FIELD PREEMPTION: Federal government occupies entire field
└─ IF preempted → Federal law controls
```

#### 3. Most Significant Relationship Test
```
IF no preemption and no valid choice of law:
├─ Where did injury occur?
├─ Where did conduct causing injury occur?
├─ Where are parties domiciled/incorporated?
├─ Where is relationship centered?
└─ Apply law of jurisdiction with most significant relationship
```

#### 4. Statutory Choice of Law
```
SOME STATUTES SPECIFY THEIR OWN REACH:
├─ GDPR: Applies to EU data subjects regardless of company location
├─ CCPA: Applies if business meets CA thresholds
├─ Securities laws: Apply to transactions in US markets
└─ IF statute asserts jurisdiction → Comply with that statute
```

---

## Output Template

```
═══════════════════════════════════════════════════════════════
JURISDICTION ANALYSIS REPORT
═══════════════════════════════════════════════════════════════

SITUATION: [Brief description]

GEOGRAPHIC JURISDICTIONS IDENTIFIED:

✓ FEDERAL (United States):
  ├─ Trigger: [Why federal jurisdiction applies]
  ├─ Applicable Laws: [List]
  └─ Risk Level: [CRITICAL/HIGH/MODERATE/LOW]

✓ [PRIMARY STATE]:
  ├─ Trigger: [Why this state applies]
  ├─ Applicable Laws: [List]
  └─ Risk Level: [CRITICAL/HIGH/MODERATE/LOW]

✓ [ADDITIONAL STATES] (if multi-state):
  ├─ Trigger: [Why each state applies]
  ├─ Applicable Laws: [List]
  └─ Risk Level: [CRITICAL/HIGH/MODERATE/LOW]

✓ LOCAL (if applicable):
  ├─ Jurisdiction: [County/City]
  └─ Requirements: [List]

✓ INTERNATIONAL (if applicable):
  ├─ Jurisdiction: [Country/Region]
  ├─ Applicable Laws: [List]
  └─ Risk Level: [CRITICAL/HIGH/MODERATE/LOW]

REGULATORY JURISDICTIONS IDENTIFIED:

✓ [REGULATOR NAME]:
  ├─ Authority: [What they regulate]
  ├─ Jurisdiction: [Scope]
  ├─ Enforcement: [Penalties/actions available]
  └─ Risk Level: [CRITICAL/HIGH/MODERATE/LOW]

[Repeat for each regulator]

CONFLICTS OF LAW RESOLUTION:

ISSUE: [Describe conflict]
ANALYSIS:
├─ [Step-by-step resolution]
└─ RESOLUTION: [Which law applies]

ATTORNEY CONSULTATION RECOMMENDED:
⚠️ [List items requiring attorney analysis]

═══════════════════════════════════════════════════════════════

PATTERN STRENGTH: [STRONG/MODERATE/WEAK]
BASIS: [Explanation]

CONFIDENCE: [HIGH/MODERATE/LOW]
├─ High confidence: [Areas with clear law]
├─ Moderate confidence: [Fact-specific areas]
└─ Limitations: [Areas requiring expert analysis]
```

---

## Common Jurisdiction Patterns

### SaaS Company (Multi-State)
- Federal: FTC, interstate commerce
- Delaware: Incorporation
- California: Headquarters, CCPA
- Multi-state: Customers in 50 states
- EU: If any EU users (GDPR)

### Healthcare Provider
- Federal: HIPAA, Medicare/Medicaid
- State: Licensing, state privacy laws
- Local: Health department, zoning

### E-commerce Retailer
- Federal: FTC, consumer protection
- State(s): Sales tax nexus, consumer laws
- International: If shipping abroad

### Employer (Multi-Location)
- Federal: FLSA, Title VII, ADA, FMLA
- State(s): Each state with employees
- Local: Minimum wage, sick leave ordinances

---

**Module Version:** 1.0  
**Last Updated:** November 2025
