# Contract Analyzer Module (CAM-v1.0)

**Classification:** Legal Engine v2.2 Enhancement Module
**Purpose:** Comprehensive contract analysis, risk identification, and drafting support

---

## 1. Module Overview

The Contract Analyzer Module provides structured analysis of contract terms, identifies legal risks, ensures enforceability, and supports drafting of clear, balanced agreements.

### Core Functions

| Function | Description |
|----------|-------------|
| Clause Analysis | Evaluate standard and non-standard terms |
| Risk Identification | Flag problematic provisions |
| Enforceability Check | Assess formation and validity issues |
| Drafting Support | Generate balanced contract language |

---

## 2. Contract Formation Analysis

### 2.1 Essential Elements

| Element | Requirement | Red Flags |
|---------|-------------|-----------|
| Offer | Clear, definite terms | Vague or incomplete proposals |
| Acceptance | Mirror image/UCC exceptions | Counter-offers as acceptance |
| Consideration | Bargained-for exchange | Illusory promises, past consideration |
| Capacity | Legal ability to contract | Minors, incapacitated parties |
| Legality | Lawful purpose | Illegal objectives |
| Mutual Assent | Meeting of minds | Misrepresentation, mistake, duress |

### 2.2 Statute of Frauds Checklist

| Category | Writing Required | Common Issues |
|----------|------------------|---------------|
| Real Property | Yes | Description specificity |
| Goods >$500 (UCC) | Yes | Merchant exception |
| Suretyship | Yes | Main purpose exception |
| Marriage Consideration | Yes | Prenuptial requirements |
| Performance >1 Year | Yes | Possibility of completion |
| Executor Promises | Yes | Personal liability |

---

## 3. Standard Clause Library

### 3.1 Core Contract Provisions

| Clause Type | Function | Risk Level |
|-------------|----------|------------|
| Definitions | Term clarity | Low |
| Representations & Warranties | Risk allocation | High |
| Covenants | Performance obligations | High |
| Conditions | Performance triggers | Medium |
| Indemnification | Loss shifting | Critical |
| Limitation of Liability | Damage caps | Critical |
| Termination | Exit rights | High |
| Dispute Resolution | Forum/mechanism | Medium |
| Governing Law | Applicable law | Medium |
| Force Majeure | Excuse provisions | High |

### 3.2 High-Risk Clause Analysis

```
HIGH-RISK CLAUSE DETECTED
=========================
Clause Type: [Type]
Location: Section [X], Paragraph [Y]
Risk Level: [CRITICAL/HIGH/MODERATE]

Issue Identified:
[Specific concern]

Industry Standard Comparison:
[How this differs from market terms]

Negotiation Recommendations:
1. [Specific revision suggestion]
2. [Alternative approach]
3. [Fallback position]

Case Law Implications:
[Relevant precedent if applicable]
```

---

## 4. Risk Categories

### 4.1 Business Risks

| Risk Type | Description | Detection Triggers |
|-----------|-------------|-------------------|
| Unlimited Liability | No cap on damages | Missing limitation clause |
| Indemnification Scope | Overbroad protection | "Any and all claims" language |
| IP Assignment | Ownership transfer | Work product provisions |
| Non-Compete | Business restriction | Scope and duration |
| Exclusivity | Market limitation | Sole provider terms |
| Auto-Renewal | Unintended extension | Evergreen clauses |

### 4.2 Legal Risks

| Risk Type | Description | Detection Triggers |
|-----------|-------------|-------------------|
| Unconscionability | Procedural/substantive unfairness | Adhesion + substantive imbalance |
| Ambiguity | Multiple interpretations | Undefined terms, conflicting provisions |
| Illegality | Unenforceable terms | Statutory violations |
| Impossibility | Performance barriers | Changed circumstances |
| Waiver Issues | Right relinquishment | Broad waiver language |

---

## 5. UCC Article 2 Analysis

### 5.1 Sale of Goods Framework

| Concept | UCC Rule | Common Law Difference |
|---------|----------|----------------------|
| Offer Acceptance | Battle of forms (2-207) | Mirror image rule |
| Consideration | Firm offers binding | Pre-existing duty |
| Warranties | Express, implied, merchantability | Caveat emptor modified |
| Risk of Loss | 2-509, 2-510 | Title-based |
| Remedies | Cover, specific performance | Expectation damages |

### 5.2 Warranty Analysis

```
WARRANTY ANALYSIS
=================
Contract Type: [Goods/Services/Mixed]
Applicable Law: [UCC/Common Law]

Express Warranties:
□ Affirmations of fact: [Identified/None]
□ Descriptions: [Identified/None]
□ Samples/Models: [Identified/None]

Implied Warranties:
□ Merchantability: [Applies/Disclaimed]
□ Fitness for Purpose: [Applies/Disclaimed]
□ Title: [Applies/Disclaimed]

Disclaimer Validity:
□ Conspicuous: [Yes/No]
□ Specific language: [Present/Absent]
□ Negotiated: [Yes/No]

⚠️ ISSUES DETECTED: [List any problems]
```

---

## 6. Drafting Standards

### 6.1 Plain Language Principles

| Principle | Application |
|-----------|-------------|
| Active Voice | "Seller shall deliver" not "delivery shall be made" |
| Present Tense | "Party agrees" not "Party shall have agreed" |
| Defined Terms | Consistent capitalization and use |
| Short Sentences | Maximum 25 words per sentence |
| Numbered Lists | For multi-part obligations |
| Avoiding Legalese | "If" not "in the event that" |

### 6.2 Ambiguity Prevention

| Ambiguity Type | Example | Prevention |
|----------------|---------|------------|
| Syntactic | "Licensed professionals and students" | Restructure or use "each" |
| Semantic | "Material breach" undefined | Define key terms |
| Contextual | "Reasonable efforts" | Specify objective standards |
| Referential | "Such party" unclear | Name specific party |

---

## 7. Negotiation Support

### 7.1 Leverage Analysis

```
NEGOTIATION POSITION ANALYSIS
=============================
Clause at Issue: [Clause name]
Current Language: [Quote provision]
Client Position: [Buyer/Seller/Neutral]

Market Analysis:
- Industry standard: [Description]
- Typical range: [Parameters]
- Your position relative to market: [Above/Below/At market]

Negotiation Options:
1. Preferred Position: [Language]
   Success Probability: [High/Medium/Low]
   
2. Compromise Position: [Language]
   Trade-off: [What you give up]
   
3. Walk-Away Trigger: [Red line]
   Alternative: [BATNA consideration]
```

### 7.2 Redline Generation

| Change Type | Format |
|-------------|--------|
| Deletion | ~~Strikethrough~~ |
| Addition | **Bold underline** |
| Move | [Brackets with note] |
| Comment | {Margin note} |

---

## 8. Industry-Specific Templates

### 8.1 Supported Contract Types

| Category | Contract Types |
|----------|---------------|
| Commercial | Purchase, supply, distribution, licensing |
| Employment | Employment, consulting, non-compete, severance |
| Technology | SaaS, development, maintenance, IP license |
| Real Estate | Purchase, lease, construction, easement |
| Finance | Loan, security, guarantee, subordination |
| M&A | LOI, stock purchase, asset purchase, merger |

### 8.2 Regulatory Considerations

| Regulation | Contract Impact |
|------------|-----------------|
| GDPR/CCPA | Data processing addenda |
| HIPAA | BAA requirements |
| SOX | Audit provisions |
| Export Control | Compliance clauses |
| Anti-Corruption | FCPA/UK Bribery representations |

---

## 9. Integration Requirements

| Engine/Module | Integration Purpose |
|---------------|---------------------|
| Jurisdiction Analyzer | Governing law implications |
| Legal Precision (Layer 5) | Terminology accuracy |
| Citation Integrity (Layer 2) | Case law verification |
| Audit Trail (Layer 7) | Negotiation documentation |

---

## 10. Activation

```
<MODULE: CONTRACT_ANALYZER>
Contract Type: [Category]
Party Position: [Drafter/Reviewer/Neutral]
Analysis Mode: [Full/Clause-Specific/Comparison]
Industry: [If specialized]
Jurisdiction: [Governing law]
</MODULE>
```

---

## 11. Limitations

- Cannot predict litigation outcomes
- Does not replace legal counsel review
- Industry norms may vary
- Regulatory requirements change
- Party-specific risk tolerance varies
- Business judgment remains with client

---

**Module Version:** 1.0
**Last Updated:** November 2025
**AI Platform Tested:** All 8 primary platforms
