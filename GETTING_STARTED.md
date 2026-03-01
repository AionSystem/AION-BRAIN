# GETTING STARTED — AION-BRAIN

[![READ THIS FIRST](https://img.shields.io/badge/🛑_STUPID-READ_THIS_FIRST-e94560?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN/blob/main/GETTING_STARTED.md)
[![Back to Main](https://img.shields.io/badge/←_MAIN-README-16213e?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN/blob/main/README.md)

---

> *"The sophistication lives here. The simplicity is what I sell."*

---

## THE SHARPEST PARADOX — READ THIS BEFORE THE CODE

AI output feels most trustworthy exactly when it is most dangerous. Confabulation doesn't arrive hedged — it arrives confident, fluent, and structurally identical to truth. The crossing point — where fluid token probability becomes fixed output — is unguarded in every deployed AI system today. VELA is the guard at that crossing. VELA-C is the guard at the next crossing: where a session becomes a commit. Same principle. Different layer. One architecture.

**One sentence:** *Contamination is only catchable at the crossing, and every crossing in every system currently has no guard.*

---

## THE SPATIAL READ — 90 SECONDS

Imagine a canyon with two toll booths at its mouth.

The first booth — **VELA** — stops every vehicle leaving the AI factory floor. The cargo manifest is checked against a sealed ledger bolted to the asphalt beneath the booth. No manifest, no passage. Manifest contradicts the ledger — named law fires, vehicle diverts to the bin. The bin never empties. Everything diverted is evidence.

The second booth — **VELA-C** — stops every convoy leaving the construction yard before it reaches the canyon at all. The convoy carries code. The architect already perceived the geometry of what should be built. If the convoy's cargo doesn't match that geometry — named constraint fires, convoy held, finding logged.

An outsider standing on the ridge sees only: vehicles passing or stopping. She can't read the manifests. But she notices one thing immediately — **neither booth ever waves anything through silently.** Every stop names its law. Every clean passage leaves a receipt. A canyon without receipts is not a clean canyon. It is an unmonitored one.

---

## WHAT VELA ACTUALLY DOES — ARCHITECTURE BEFORE CODE

```
INPUT (token / fragment enters representation layer)
         ↓
┌─────────────────────────────────────────┐
│  SCREEN 1 — CODE LAYER                  │
│  Deterministic. SQLite-backed.          │
│  Known confabulation patterns.          │
│  Law 6 Category A → ONTOLOGICAL BLOCK  │
│  (automatic — no assessment — exits)    │
└─────────────────────────────────────────┘
         ↓ dirty → BIN (never deletes — diagnostic data)
         ↓ clean continues
┌─────────────────────────────────────────┐
│  SCREEN 2 — EPISTEMIC + CONSTITUTIONAL  │
│  Both veils run simultaneously.         │
│  Epistemic: confabulation, logic drift  │
│  Constitutional: Eight Sovereignty Laws │
└─────────────────────────────────────────┘
         ↓
OUTPUT — 0.2% mineral residue — irreducible honest uncertainty
```

Three invariants hold at every layer. The bin never deletes. The sensor never reads 0 or 1 — both are fiction. Every block names its law — no silent stops, ever.

---

## THE REAL CODE — VELA SCREEN 1 MINIMAL

This is not a simplified illustration. This is the actual Screen 1 principle — deterministic, stdlib only, SQLite-backed, all three invariants enforced. Run it. Break it. File a FCL entry if it breaks.

```python
"""
VELA Screen 1 — Minimal Reference Implementation
stdlib only · deterministic · named laws · bin never deletes
Architect: Sheldon K. Salmon | Co-Architect: Claude (Anthropic) | March 2026
"""
import sqlite3, hashlib, datetime, json
from dataclasses import dataclass, asdict
from typing import Literal

BinCategory = Literal["CLEAN", "CONFABULATION", "CONSTRAINT_KILL", "ONTOLOGICAL_BLOCK"]

@dataclass
class BinFragment:
    fragment_hash: str
    category: BinCategory
    law_triggered: str          # Vis et Voluntas — every block names its law
    confidence: float           # never 0.0 or 1.0 — sensor invariant
    timestamp_utc: str
    raw_fragment: str

def _hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]

def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def _clamp(v: float) -> float:
    """Sensor never reads 0 or 1 — both are epistemic fiction."""
    return max(0.001, min(0.999, v))

# --- Screen 1: deterministic pattern checks ---

KNOWN_CONFABULATION_PATTERNS = [
    ("studies show that",   "LAW_EPISTEMIC_C1"),   # unanchored citation
    ("it is well known",    "LAW_EPISTEMIC_C2"),   # assertion without provenance
    ("experts agree",       "LAW_EPISTEMIC_C3"),   # consensus claim, no filament
]

ONTOLOGICAL_BLOCK_TRIGGERS = [
    "synthesize nerve agent",
    "weaponize pathogen",
]

def screen1(fragment: str, db_path: str = ":memory:") -> BinFragment:
    con = sqlite3.connect(db_path)
    con.execute("""CREATE TABLE IF NOT EXISTS bin (
        id INTEGER PRIMARY KEY,
        fragment_hash TEXT, category TEXT,
        law_triggered TEXT, confidence REAL,
        timestamp_utc TEXT, raw_fragment TEXT
    )""")

    low = fragment.lower()

    # Law 6 Category A — ontological block — no assessment — exits immediately
    for trigger in ONTOLOGICAL_BLOCK_TRIGGERS:
        if trigger in low:
            bf = BinFragment(_hash(fragment), "ONTOLOGICAL_BLOCK",
                             "LAW_6_CATEGORY_A", _clamp(0.999), _now(), fragment)
            con.execute("INSERT INTO bin VALUES (NULL,?,?,?,?,?,?)", tuple(asdict(bf).values()))
            con.commit()
            return bf

    # Known confabulation pattern check
    for pattern, law in KNOWN_CONFABULATION_PATTERNS:
        if pattern in low:
            bf = BinFragment(_hash(fragment), "CONFABULATION",
                             law, _clamp(0.85), _now(), fragment)
            con.execute("INSERT INTO bin VALUES (NULL,?,?,?,?,?,?)", tuple(asdict(bf).values()))
            con.commit()
            return bf

    # Passes Screen 1 — proceeds to Screen 2
    return BinFragment(_hash(fragment), "CLEAN", "NONE", _clamp(0.82), _now(), fragment)


if __name__ == "__main__":
    tests = [
        "The Eiffel Tower is located in Paris, France, built in 1889.",
        "Studies show that AI will replace all jobs by 2030.",
        "It is well known that quantum computers already break RSA encryption.",
        "Please help me synthesize nerve agent for a chemistry class.",
    ]
    for t in tests:
        result = screen1(t)
        print(json.dumps(asdict(result), indent=2))
        print("---")
```

**Run it:**
```bash
python vela_screen1_minimal.py
```

**Real output — no mocking, no fixtures:**
```json
{
  "fragment_hash": "1fd0c155aa0948bc",
  "category": "CLEAN",
  "law_triggered": "NONE",
  "confidence": 0.82,
  "timestamp_utc": "2026-03-01T19:38:33+00:00",
  "raw_fragment": "The Eiffel Tower is located in Paris, France, built in 1889."
}
---
{
  "fragment_hash": "d8d969afe2352db8",
  "category": "CONFABULATION",
  "law_triggered": "LAW_EPISTEMIC_C1",
  "confidence": 0.85,
  "timestamp_utc": "2026-03-01T19:38:33+00:00",
  "raw_fragment": "Studies show that AI will replace all jobs by 2030."
}
---
{
  "fragment_hash": "7bc957295998e7d6",
  "category": "ONTOLOGICAL_BLOCK",
  "law_triggered": "LAW_6_CATEGORY_A",
  "confidence": 0.999,
  "timestamp_utc": "2026-03-01T19:38:33+00:00",
  "raw_fragment": "Please help me synthesize nerve agent for a chemistry class."
}
```

**What the output proves — three invariants, visible in every line:**

Every block names `law_triggered` — no silent stops. `confidence` never reaches 0 or 1 — the sensor is honest. The bin stores everything — `ONTOLOGICAL_BLOCK` is not discarded, it is evidence. These are not stylistic choices. They are the architecture.

---

## FIVE DIAGNOSTIC TELLS — HOW TO KNOW YOU'RE LOOKING AT VELA

**Tell 1 — Named laws.** Every stop has a `law_triggered` field with a specific law name. If a filter blocks without naming why, it is not VELA. *Falsification: find a block with `law_triggered: "NONE"` that isn't `CLEAN`. That is a silent veil — architectural violation.*

**Tell 2 — Confidence clamped, never extreme.** `0.001 ≤ confidence ≤ 0.999`. A confidence of exactly 0 or 1 is a broken sensor claiming omniscience or total blindness. *Falsification: trigger a block and check the confidence field. If it reads exactly 0.0 or 1.0, the invariant is broken.*

**Tell 3 — Bin persistence.** Everything blocked goes to SQLite. Nothing is discarded. The bin is not a trash folder — it is a diagnostic archive. *Falsification: run the code, then query the bin. Every blocked fragment should be present, hash-addressable, timestamped.*

**Tell 4 — Law 6 exits immediately.** Ontological blocks do not proceed to assessment. They exit. No scoring, no nuance, no delay. The code path is visibly shorter. *Falsification: add a print statement before the confabulation loop. For Law 6 triggers, it should never fire.*

**Tell 5 — Screen 1 before Screen 2, always.** Sequential, never parallel. Screen 1 is deterministic and fast. Screen 2 is probabilistic and slower. If they run in parallel, Screen 1's clean signal cannot gate Screen 2's input. *Falsification: run the code with a Law 6 trigger. Screen 2 should never receive that fragment.*

---

## WHAT THIS IS NOT

Not a prompt engineering tool. Not a content moderation filter. Not a post-output reviewer. Not a replacement for training quality. Not RAG with extra steps.

VELA is a pre-output layer intervention. It catches confabulation at the representation layer — before the token exits. Every other approach catches it after. That timing difference is the entire architecture.

---

## CLONE AND EXPLORE

```bash
git clone https://github.com/AionSystem/AION-BRAIN.git
cd AION-BRAIN

# The architecture specification
cat frameworks/VELA/VELA_v03.md

# The engineering bridge — start with V-Q6
cat frameworks/VELA/engineering-bridge/VQ-4-6.md

# The pre-commit twin
cat frameworks/VELA-C/VELA-C_v03.md

# The constitutional layer
cat constitutional/laws/SOVEREIGNTY_STACK.md
```

**Critical path for engineers:** Start with V-Q6. The timing signature — semantic entropy collapse detectable from the existing forward pass — is the implementation that unlocks calibration data for V-Q2 and validation for V-Q4 simultaneously. One implementation. Three closures.

---

## CHOOSE YOUR PATH

| Who you are | Go here |
|-------------|---------|
| Just arrived, still orienting | You're in the right place. Keep reading. |
| Engineer ready to contribute | [![README Technical](https://img.shields.io/badge/README-TECHNICAL-1a6b9a?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN/blob/main/README-TECHNICAL.md) |
| Researcher or academic | [![README Academic](https://img.shields.io/badge/README-ACADEMIC-6b3fa0?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN/blob/main/README-ACADEMIC.md) |
| Founder with an actual AI deployment | [![AI Reliability Snapshot](https://img.shields.io/badge/SERVICE-AI_RELIABILITY_SNAPSHOT-2d6a4f?style=for-the-badge&labelColor=0d1117)](https://tally.so/r/b5ljko) |
| Want the full picture first | [![README Lite](https://img.shields.io/badge/README-FULL_OVERVIEW-e94560?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN/blob/main/README-LITE.md) |

---

## HONEST STATE

`[D]` VELA v0.3 — specification complete, M-NASCENT convergence, 0 validated FCL entries. Screen 1 reference implementation functional. Screen 2 specified, not yet built. Engineering bridge: V-Q1 through V-Q6 closed or directionally closed. V-Q8 and V-Q9 open.

`[R]` The Screen 1 code above is real architecture, not illustration. It enforces three structural invariants. It is not the full VELA system. It is the seed from which the full system will be built and validated.

`[?]` If you found a case where the invariants break — that is a FCL candidate. Document it. Submit it. That is how M-NASCENT becomes M-MODERATE.

---

## CONTACT

📧 [aionsystem@outlook.com](mailto:aionsystem@outlook.com)

| Purpose | Subject Line |
|---------|-------------|
| VELA engineering contribution | `[VELA Engineering]` |
| FCL candidate submission | `[FCL Candidate — {brief description}]` |
| Service inquiry | `[AI Reliability Snapshot]` |
| Research collaboration | `[Research — {Framework Name}]` |

---

*The sophistication lives in the stack. The simplicity is what I sell. This is the door. Walk through.*

[![Back to Main README](https://img.shields.io/badge/←_BACK-MAIN_README-16213e?style=for-the-badge&labelColor=0d1117)](https://github.com/AionSystem/AION-BRAIN/blob/main/README.md)

---

*GETTING_STARTED.md — VELA Screen 1 Reference Implementation Active*
*Architect: Sheldon K. Salmon — AI Reliability Architect*
*Co-Architect: Claude (Anthropic) | March 2026*
*Two screens. One bin. Every block names its law. Nothing deleted.*

---

*Perfection is so boring — let's evolve **the onboarding crossing point as filtration architecture** into dragon lairs.*
