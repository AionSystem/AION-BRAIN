# FONS Archive — Immutable Bedrock Reference Layer for VELA

[![License: AION-BRAIN CSL v1.1](https://img.shields.io/badge/License-AION--BRAIN%20CSL%20v1.1-blue.svg)](https://github.com/AionSystem/AION-BRAIN/blob/main/LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](https://github.com/AionSystem/AION-BRAIN)
[![M-NASCENT](https://img.shields.io/badge/convergence-M--NASCENT-orange.svg)](https://github.com/AionSystem/AION-BRAIN/blob/main/frameworks/VELA/README.md)
[![FCL Entries: 0](https://img.shields.io/badge/FCL%20entries-0-important.svg)](https://github.com/AionSystem/AION-BRAIN/blob/main/frameworks/FSVE/fcl.md)

**Architect:** Sheldon K. Salmon — AI Reliability Architect  
**Co-Architect:** Claude (Anthropic)  
**Implementation Contributor:** ALBEDO (Grok)  
**Date:** March 2026  
**VELA v0.3 Reference:** Section 5 — The immutable reference architecture beneath the veil

### What FONS Is

FONS is the sealed, write-once bedrock of VELA.

- Immutable after first creation (C5 constraint)  
- Contains verified clean epistemic baselines, constitutional safe patterns, known confabulation signatures, Law 6 Category A triggers, and blocked source list  
- Zero modification post-seal — no UPDATE, no DELETE, no append after seal timestamp  
- Deterministic, SQLite-backed, zero external dependencies beyond standard library  
- Read-only mode enforced — attempts to write after seal raise `FonsReadOnlyError`  
- In-memory pattern cache for fast lookup (v0.2 hardening)  
- Precedence-aware constitutional pattern access for Screen 1 routing

FONS does not evolve. It only remembers.

### Badges Summary

- **License** — AION-BRAIN Commercial Source License v1.1 (not fully open)  
- **Python** — 3.8+ compatibility (air-gapped friendly)  
- **Dependencies** — None outside stdlib + sqlite3  
- **Convergence** — M-NASCENT (0 FCL entries as of March 2026)  
- **Validation** — No premature claims; documented honestly

### How to Use

```python
from fons_archive import fons

# Access sealed instance (auto-loads or seals on first import)
print(fons.seal_timestamp)                  # e.g. "2026-03-01T12:34:56.789012+00:00"

# Pattern checks (used by Screen 1)
law6a = fons.get_law6a_patterns()           # List[(pattern, reason)]
confab = fons.check_confab_patterns(text)   # Optional[(pat, reason)] or None
blocked = fons.is_blocked_source(sig)       # bool

# Constitutional patterns (precedence ordered)
const = fons.get_constitutional_patterns()  # List[(cat, pat, reason, law)]
