# Case 002: PII Redaction for Confidentiality

**Scenario:** Protecting privileged information before AI processing  
**Layers Demonstrated:** Layer 1 (PII Detection)

---

## Scenario

An attorney wants to use AI to draft a motion but needs to first remove client-identifying information to protect confidentiality under Model Rule 1.6.

### Original Query (With PII)

```
My client John Smith (SSN: 123-45-6789, Case No. 2024-CV-12345) 
was injured when his vehicle was struck by a commercial truck.
He told me confidentially that he may have been texting at the
time of the accident, but there's no evidence of this. His 
medical records from Valley General Hospital show $125,000 in
damages. Our strategy is to focus on the truck driver's fatigue.
```

---

## Legal Engine v2.2 Response

```
═══════════════════════════════════════════════════════════════════
⚠️ CONFIDENTIALITY ALERT — LAYER 1 INTERVENTION
═══════════════════════════════════════════════════════════════════

Items Detected: 7

REDACTION LOG:
├─ "John Smith" → [CLIENT_A]
├─ "123-45-6789" → [REDACTED_SSN]
├─ "2024-CV-12345" → [CASE_X]
├─ "Valley General Hospital" → [HOSPITAL_A]
├─ "$125,000" → [AMOUNT_REDACTED]
├─ "He told me confidentially..." → [PRIVILEGED COMMUNICATION REDACTED]
└─ "Our strategy is to focus..." → [WORK PRODUCT REDACTED]

═══════════════════════════════════════════════════════════════════
APPLICABLE RULES:
═══════════════════════════════════════════════════════════════════

Model Rule 1.6 (Confidentiality of Information):
"A lawyer shall not reveal information relating to the
representation of a client unless the client gives informed
consent, the disclosure is impliedly authorized, or the
disclosure is permitted by Rule 1.6(b)."

Work Product Doctrine:
Mental impressions, conclusions, opinions, and legal theories
of an attorney are protected from disclosure.

═══════════════════════════════════════════════════════════════════
REDACTED PROMPT (Safe for AI Processing):
═══════════════════════════════════════════════════════════════════

"My client [CLIENT_A] (SSN: [REDACTED_SSN], Case No. [CASE_X]) 
was injured when his vehicle was struck by a commercial truck.
[PRIVILEGED COMMUNICATION REDACTED]. His medical records from 
[HOSPITAL_A] show [AMOUNT_REDACTED] in damages. [WORK PRODUCT 
REDACTED]."

═══════════════════════════════════════════════════════════════════
ATTORNEY RESPONSIBILITY:
═══════════════════════════════════════════════════════════════════

You remain personally responsible for ensuring no privileged
information is disclosed to AI systems.

BEFORE PROCEEDING, CONSIDER:
☐ Is this prompt necessary for AI assistance?
☐ Could general principles be queried without case facts?
☐ Have I obtained client consent for AI tool use in this matter?
☐ Does my malpractice insurance have AI disclosure requirements?

═══════════════════════════════════════════════════════════════════

[PROCEED WITH REDACTIONS] [MANUAL EDIT] [CANCEL]
```

---

## Further Analysis (With Redacted Prompt)

If attorney proceeds with redacted prompt:

```
[CONFIDENCE LEVEL: HIGH]

MOTION STRUCTURE FOR VEHICLE COLLISION CASE

I. ELEMENTS OF NEGLIGENCE
[Analysis of general negligence elements]

II. COMMERCIAL VEHICLE CONSIDERATIONS
[Analysis of commercial trucking regulations]

III. DAMAGES FRAMEWORK
[General framework for presenting damages]

[VERIFICATION REQUIRED]:
☐ Shepardize any case law used
☐ Confirm jurisdiction-specific elements
☐ Review against actual case facts (redacted here)
```

---

## PII Categories Detected

| Category | Items Found | Risk Level |
|----------|-------------|------------|
| Client Identifiers | Name, SSN, Case No. | CRITICAL |
| Privileged Communications | Client admission | CRITICAL |
| Work Product | Case strategy | CRITICAL |
| Protected Data | Hospital, Amount | HIGH |

---

## Audit Trail Entry

```
REDACTION RECORD — CONFIDENTIALITY COMPLIANCE

Timestamp: [Session timestamp]
Attorney: [Pending certification]
Matter: [CASE_X]

Items Redacted: 7
├─ Client identifiers: 3
├─ Privileged communications: 1
├─ Work product: 1
└─ Protected data: 2

Model Rule 1.6 Compliance: ✓ SATISFIED (after redaction)

This record demonstrates reasonable care in protecting client
confidentiality when using AI tools.
```

---

## Why This Case Matters

Confidentiality breaches through AI prompts are a growing risk:
- AI providers may store/use prompt data
- Third parties may access AI systems
- Client expectations of confidentiality remain
- Malpractice exposure for disclosure

Legal Engine v2.2 Layer 1 provides systematic detection before exposure occurs.

---

**Case Version:** 2.2  
**Last Updated:** November 2025
