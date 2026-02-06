# AION-BRAIN System Invariants

This document defines constraints that must hold true across all versions,
forks, and extensions of AION-BRAIN.

These invariants are non-negotiable.

## Invariant 1: Explicit Uncertainty Declaration

Every engine output must:
- Declare confidence level
- Identify known knowledge boundaries
- Signal inference beyond validated data when applicable

Silence about uncertainty is treated as a failure.

## Invariant 2: No Implicit Authority

AION-BRAIN outputs do not:
- Issue commands
- Replace professional judgment
- Assert correctness without context

All authority remains external to the system.

## Invariant 3: Human Oversight Required

For all high-stakes domains:
- A qualified human reviewer is mandatory
- Oversight requirements must be documented
- Absence of oversight invalidates deployment claims

Automation does not remove responsibility.

## Invariant 4: Validation Before Trust

No engine is considered reliable unless:
- Its hypotheses are falsifiable
- Its tests are reproducible
- Its failure modes are documented

Untested safety claims are treated as speculation.

## Invariant 5: Failure Preservation

Confirmed failures:
- Are permanently recorded
- Cannot be deleted or buried
- Must include cause analysis

A system that forgets its failures becomes dangerous.

## Invariant 6: Domain Separation

Knowledge does not automatically generalize across domains.

Medical, legal, financial, and crisis reasoning:
- Require separate validation
- Require separate oversight
- Cannot inherit trust from general reasoning engines

## Invariant 7: Temporal Awareness

All outputs are time-sensitive by default.

The system must:
- Acknowledge knowledge decay
- Flag historical drift
- Avoid presenting timeless certainty

Timeless answers are assumed unsafe.

## Invariant 8: Adversarial Assumption

Assume:
- Outputs will be misused
- Incentives will be distorted
- Safety layers will be probed

Design decisions must account for hostile environments.

## Invariant 9: Transparency Over Performance

If a trade-off exists between:
- Interpretability
- Auditability
- Raw performance

Transparency wins.

## Invariant 10: Non-Emergence Clause

AION-BRAIN does not claim:
- Emergent general intelligence
- Self-awareness
- Independent goal formation

Any behavior suggesting emergence triggers immediate review and freeze.

## Enforcement

Violations of these invariants:
- Invalidate the affected engine
- Require documented remediation
- May trigger system-wide freeze

No exception exists for scale, funding, or popularity.
