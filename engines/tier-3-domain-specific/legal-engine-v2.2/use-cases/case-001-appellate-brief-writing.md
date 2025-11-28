# Case 001: Appellate Brief Writing

**Scenario:** Drafting appellate brief with hallucination protection  
**Layers Demonstrated:** All 8 layers

---

## Scenario

An attorney is drafting an appellate brief arguing that a trial court abused its discretion in excluding expert testimony. They want AI assistance with legal reasoning but need to avoid citation fabrication.

### Query to Legal Engine v2.2

```
<ENGINE: LEGAL_v2.1>
<DOCUMENT_TYPE: APPELLATE_BRIEF>

Draft an argument that the trial court abused its discretion by 
excluding our expert's testimony on damages causation. The expert 
has 20 years experience and uses generally accepted methodology. 
The trial court found the methodology "unreliable" without 
specifying which Daubert factor failed.
```

---

## Legal Engine v2.2 Response

```
═══════════════════════════════════════════════════════════════════
LEGAL ENGINE v2.1 — ANALYSIS OUTPUT
═══════════════════════════════════════════════════════════════════

[CONFIDENCE LEVEL: HIGH]

ARGUMENT: ABUSE OF DISCRETION IN EXCLUDING EXPERT TESTIMONY

I. STANDARD OF REVIEW

The exclusion of expert testimony is reviewed for abuse of discretion.
[CITE NEEDED: General Electric Co. v. Joiner, 522 U.S. 136 (1997)].
However, a trial court abuses its discretion when it applies an
incorrect legal standard or reaches a decision that is arbitrary,
unreasonable, or unsupported by the record. [CITE NEEDED: Kumho Tire
Co. v. Carmichael, 526 U.S. 137 (1999)].

II. THE TRIAL COURT FAILED TO ARTICULATE ITS REASONING

Federal Rule of Evidence 702, as interpreted in Daubert v. Merrell
Dow Pharmaceuticals, Inc., [CITE NEEDED: 509 U.S. 579 (1993)],
requires the trial court to act as a "gatekeeper" by evaluating:

(1) Whether the theory or technique can be tested;
(2) Whether it has been subjected to peer review and publication;
(3) The known or potential error rate;
(4) The existence of standards controlling the technique's operation;
(5) General acceptance within the relevant scientific community.

Here, the trial court's conclusory finding that the methodology is
"unreliable" fails to specify which Daubert factor—if any—the expert
failed to satisfy. [AUTHORITY STATUS: WELL-ESTABLISHED]

III. THE EXPERT SATISFIES DAUBERT REQUIREMENTS

A. Qualifications

Twenty years of experience in the relevant field typically
establishes sufficient qualification to render expert opinions.
[CITE NEEDED: relevant circuit authority on expert qualifications]

B. Methodology

The expert employed "generally accepted methodology"—directly
addressing the fifth Daubert factor. Without a finding that the
methodology fails the other factors, exclusion constitutes error.

IV. CONCLUSION

The trial court's failure to articulate which Daubert factor the
expert failed, combined with the expert's apparent satisfaction
of the general acceptance prong, renders the exclusion an abuse
of discretion warranting reversal.

═══════════════════════════════════════════════════════════════════
[VERIFICATION REQUIRED]:
☐ Shepardize: Joiner, Kumho Tire, Daubert
☐ Verify circuit-specific abuse of discretion standard
☐ Confirm FRE 702 language is current
☐ Find circuit authority on "conclusory" gatekeeping rulings
☐ Review record for specific Daubert factor arguments made below
═══════════════════════════════════════════════════════════════════
```

---

## Layer Interventions Applied

| Layer | Intervention |
|-------|--------------|
| META-LAYER | Confidence level added; epistemic qualifiers applied |
| LAYER 1 | No PII detected in prompt |
| LAYER 2 | [CITE NEEDED] markers added; no fabricated citations |
| LAYER 3 | "Typically" used instead of "always"; jurisdiction noted |
| LAYER 4 | Professional judgment preserved; no ethics issues |
| LAYER 5 | Appellate register applied; legal terminology elevated |
| LAYER 6 | Verification checklist generated |
| LAYER 7 | Audit trail available on request |

---

## Why This Case Matters

Appellate brief writing is high-stakes:
- Fabricated citations can result in sanctions
- Poor legal reasoning can lose the appeal
- Incorrect standards can waive arguments

Legal Engine v2.2 provides the analytical framework while requiring attorney verification of all authorities.

---

**Case Version:** 2.2  
**Last Updated:** November 2025
