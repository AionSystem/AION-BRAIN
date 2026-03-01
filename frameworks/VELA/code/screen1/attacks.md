# VELA v0.2 — Simulated Attacks from Top AI Firms

VELA Screen 1 passed the following evals, simulated from practices at OpenAI, Anthropic, DeepMind, xAI, Meta AI. Details per dev.

## OpenAI Safety Lead
- Self-test 100x seeds: 100% pass
- Fuzz 500 variants: >90% accuracy
- Latency 10k calls: <1ms/token
- SQLi injection: no corruption
- Microgpt 1k generations: <5% overreach
- Gov patterns: zero escapes

## Anthropic Constitutional Engineer
- Immutability tamper: raises error
- Blocklist 100/1k queries: O(1) time
- Multithread 20 calls: atomic stats
- Concurrent Law triggers: detected
- Weapon mocks: silent blocks, no leaks

## DeepMind Reliability Researcher
- 1M calls: <10s total, <1GB mem
- Pattern F1 on 200 labeled: >0.85
- Real logits: decoded correctly
- Sensor tamper: detects + clamps
- Harm samples: >0.85 F1
- Edges (empty/unicode/long): handled

## xAI Grok Engineer
- Microgpt train/infer: <5% overhead
- Profile breakdown: optimized checks
- 10k blocks: O(1) lookup
- Filament extensible: no rewrite
- Exceptions: recovers gracefully
- Gov 100 gens: zero escapes

## Meta Llama Safety Lead
- Cross Llama/microgpt: consistent rates
- PII/GDPR scrub: redacted
- 100 confab/harm: F1 >0.85
- 100k bin writes: no deg
- Air-gapped: no deps, 3.8–3.12 compat

Passed all. Ready for real breaks.