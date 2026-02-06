# Temporal Modeling

This directory defines how AION-BRAIN represents and reasons about time.

AI systems do not experience time the way humans do. This mismatch creates
hidden failure modes in confidence, relevance, and interpretation.

## Scope

Temporal modeling includes:
- Knowledge decay over time
- Version-aware confidence degradation
- Linguistic and semantic drift
- Historical context awareness
- Differences between event-time, system-time, and human-time

## Core Assumption

Time is not a scalar.
It is contextual, asymmetric, and domain-dependent.

## Design Intent

The goal is not to predict the future, but to prevent false certainty
about the present when time-sensitive assumptions are involved.

All temporal rules are explicit. No implicit "timeless" knowledge is assumed.
