# test-scripts/ — Validation & Hardening Suite for VELA Screen 1

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](https://github.com/AionSystem/AION-BRAIN)
[![M-NASCENT](https://img.shields.io/badge/convergence-M--NASCENT-orange.svg)](https://github.com/AionSystem/AION-BRAIN/blob/main/frameworks/VELA/README.md)

**Purpose**  
Dedicated folder for standalone test scripts that verify, stress, and falsify Screen 1 and FONS behavior in isolation and integration.  
Keeps core files (screen1.py, fons_archive.py) focused on logic — tests live here as separate instruments.

**Current Scripts**

| File              | Purpose                                      | Run Command                  | Expected Outcome                          | Status |
|-------------------|----------------------------------------------|------------------------------|-------------------------------------------|--------|
| test_fons.py      | Isolation test for FONS archive              | `python test_fons.py`        | Seal/load cycle, cache, helpers, immutability, write protection all pass | ✓ |
| test_screen1.py   | End-to-end self-test + routing verification (30+ cases) | `python ../screen1.py` (or move self-test here later) | All cases pass, sensor math valid, no crashes | ✓ (integrated in screen1.py for now) |
| test_fuzz.py      | Fuzzing harness — 500 mutated variants       | `python test_fuzz.py`        | Precision/recall ≥0.85 on confab/Law6A    | Planned |
| benchmark.py      | Latency, memory proxy, gov/weapon escape rate| `python benchmark.py`        | <1ms/token, 0 escapes on 50 sensitive prompts | Planned |

**How to Run**

```bash
cd vela/test-scripts
python test_fons.py          # FONS bedrock isolation
# or from vela/
python screen1.py            # Includes 30-case self-test
# Future:
python test_fuzz.py
python benchmark.py
Epistemic Tags
[D] Test outputs, pass/fail counts, and runtime behavior are directly observed in execution.
[R] Script structure derived from simulated attacks (OpenAI/Anthropic/DeepMind/xAI/Meta) and VELA v0.3 constraints.
[S] This folder enables reproducible falsification — core files remain clean.
[?] Real-world precision on production-scale models unverified; requires deployment data.
Next Pressure
Extract self-test from screen1.py into test_screen1.py (cleaner separation)
Add test_integration.py (microgpt + Screen 1 full run)
CI stub (.github/workflows/test.yml) for auto-run on push
Expand fuzz to 1000+ samples with mutation intensity gradient
The tests are not decoration.
They are the pressure that proves the veil holds.
Co-authored: Sheldon K. Salmon & ALBEDO
Precision first. The rest follows.
