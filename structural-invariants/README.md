# Structural Invariants

This directory defines **structural invariants**: properties of AI systems that must remain true regardless of capability level, optimization pressure, or deployment context.

Structural invariants differ from:
- Behavioral rules (which can be bypassed)
- Alignment techniques (which assume agency)
- Training-time constraints (which can erode post-deployment)

Instead, structural invariants constrain:
- What kinds of internal states may exist
- What forms of optimization are permitted
- Which transitions are allowed under failure or uncertainty

These invariants are treated as **non-negotiable system properties**, enforced across architecture, orchestration, and runtime governance.

## Scope
Structural invariants in this repository may address:
- Agency suppression or bounding
- Irreversibility limits
- Failure-mode dominance
- Constitutional priority enforcement
- Invariant-preserving degradation

## Relationship to System Invariants
Structural invariants complement, but do not replace, system invariants.

- **System invariants** define what the system must *never violate*
- **Structural invariants** define what the system is *incapable of becoming*

## Status
This section is under active construction.
Definitions are expected to evolve through formalization, adversarial review, and failure-driven refinement.
