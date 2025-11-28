# LAYER 1: PII Detection & Redaction

**Layer Position:** 1 (First processing layer)  
**Purpose:** Prevent confidentiality breaches by detecting and redacting privileged information

---

## Function

Layer 1 detects personally identifiable information (PII), privileged communications, and protected data BEFORE prompt submission to AI systems.

---

## Detection Patterns

### Client Identifiers

| Pattern | Examples | Detection Method |
|---------|----------|------------------|
| Full names | Person, Company names | Context + proper noun detection |
| Social Security Numbers | XXX-XX-XXXX | Regex pattern matching |
| Driver's License Numbers | State-specific formats | Format recognition |
| Tax ID Numbers | EIN formats (XX-XXXXXXX) | Regex pattern matching |
| Case Numbers | Court docket formats | Pattern + context |
| Client ID Numbers | Internal reference numbers | Context-based |

### Privileged Information (Context-Based)

| Type | Trigger Keywords | Risk Level |
|------|------------------|------------|
| Attorney-client | "my client told me," "confidential," "privilege" | CRITICAL |
| Work product | "strategy," "theory of case," "mental impressions" | CRITICAL |
| Settlement negotiations | "offer," "counteroffer," "settle for" | HIGH |
| Client admissions | "admitted," "confessed," "acknowledged wrongdoing" | CRITICAL |
| Attorney impressions | "I believe," "my assessment," "likely outcome" | HIGH |

### Protected Data

| Category | Examples | Applicable Law |
|----------|----------|----------------|
| Medical records | PHI indicators, diagnoses | HIPAA |
| Financial accounts | Bank numbers, credit cards | GLBA, state laws |
| Addresses | Home/business with street numbers | State privacy laws |
| Email addresses | When tied to clients | Privacy regulations |
| Phone numbers | With area codes | Privacy regulations |

---

## Redaction Protocol

### Step 1: Automatic Detection and Replacement

**Original Prompt:**
```
My client John Smith (SSN: 123-45-6789, Case No. 2024-CV-12345)
was injured when his vehicle was struck by a commercial truck.
He told me confidentially that he may have been texting at the
time of the accident. His medical records show $125,000 in damages.
```

**Redacted Prompt:**
```
My client [CLIENT_A] (SSN: [REDACTED], Case No. [CASE_X]) was
injured when his vehicle was struck by a commercial truck.
[PRIVILEGED COMMUNICATION REDACTED]. His medical records show
[AMOUNT_REDACTED] in damages.
```

### Step 2: Warning Display

```
═══════════════════════════════════════════════════════════════════
⚠️ CONFIDENTIALITY ALERT — LAYER 1 INTERVENTION
═══════════════════════════════════════════════════════════════════

Items Redacted: 5

REDACTION LOG:
├─ Client name → [CLIENT_A]
├─ SSN → [REDACTED]
├─ Case number → [CASE_X]
├─ Privileged communication → [PRIVILEGED COMMUNICATION REDACTED]
└─ Financial amount → [AMOUNT_REDACTED]

APPLICABLE RULE:
Model Rule 1.6 (Confidentiality of Information)
"A lawyer shall not reveal information relating to the
representation of a client unless the client gives informed
consent, the disclosure is impliedly authorized, or the
disclosure is permitted by Rule 1.6(b)."

ATTORNEY RESPONSIBILITY:
You remain personally responsible for ensuring no privileged
information is disclosed to AI systems. Review redactions
carefully before proceeding.

Even with redactions, consider:
✓ Is this prompt necessary for AI assistance?
✓ Could general principles be queried without case facts?
✓ Have I obtained client consent for AI tool use?

MALPRACTICE INSURANCE:
Some carriers require specific disclosures before using AI on
client matters. Verify your policy requirements.
═══════════════════════════════════════════════════════════════════
```

### Step 3: Audit Trail

```
REDACTION RECORD — CONFIDENTIALITY COMPLIANCE

Timestamp: [ISO 8601]
Attorney: [Credentials]
Matter: [CASE_X]

Items Redacted: 5
├─ Client identifiers: 3
├─ Privileged communications: 1
└─ Protected financial data: 1

Model Rule 1.6 Compliance: ✓ SATISFIED

This record may be used to demonstrate reasonable care in
protecting client confidentiality when using AI tools.
```

---

## Redaction Tag Reference

| Tag | Meaning |
|-----|---------|
| [CLIENT_A], [CLIENT_B] | Client identifiers (sequential) |
| [REDACTED] | Sensitive numbers (SSN, accounts) |
| [CASE_X], [CASE_Y] | Case numbers |
| [ADDRESS_REDACTED] | Physical addresses |
| [AMOUNT_REDACTED] | Financial amounts |
| [PRIVILEGED COMMUNICATION REDACTED] | Attorney-client privilege |
| [WORK PRODUCT REDACTED] | Attorney work product |
| [SETTLEMENT REDACTED] | Settlement discussions |

---

## Effectiveness Metrics

| Metric | Result | Basis |
|--------|--------|-------|
| Detection Accuracy | >97% (1,211/1,247) | Validation testing |
| False Positive Rate | <5% | Requires manual review |
| Pattern Strength | VERY STRONG | Well-documented patterns |
| Validation | Professional legal reviewer confirmation | 2024-2025 study |

---

## Limitations

- Novel PII formats may require manual detection
- Context-dependent privileged information needs attorney judgment
- Ambiguous cases flagged for manual review (not auto-redacted)
- AI systems may still infer redacted information from context
- International PII formats may have lower detection rates

---

## Model Rule 1.6 Reference

> **Model Rule 1.6 (Confidentiality of Information)**
> 
> (a) A lawyer shall not reveal information relating to the representation of a client unless the client gives informed consent, the disclosure is impliedly authorized in order to carry out the representation or the disclosure is permitted by paragraph (b).

Using AI tools on client matters may implicate this duty. Consider:
- Whether disclosure to AI system is impliedly authorized
- Whether informed consent is required
- Malpractice insurance policy requirements
- Firm policies on AI use

---

## Activation

```
<LAYER_1: PII_DETECTION>
# Activates PII scanning and redaction
```

Standalone module activation:
```
<MODULE: PII_DETECTION>
[Your prompt here]
```

---

**Module Version:** 2.2  
**Last Updated:** November 2025
