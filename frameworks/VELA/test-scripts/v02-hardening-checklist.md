# VELA Screen 1 v0.2 Hardening Checklist

**Purpose:** Document all implemented fixes and upgrades for Screen 1 v0.2, derived from simulated attacks (OpenAI, Anthropic, DeepMind, xAI, Meta AI).  
Use this to guide Screen 2 development — match depth in correctness, robustness, performance, testing, and polish.  
No overclaiming: all steps verified through execution and self-test.

`[D]` Checklist executed March 2026. All phases complete in order to avoid errors.  
`[R]` Order enforces dependencies: core before edges, opt after robust, tests after opt.  
`[S]` Screen 2 should mirror this structure for dual-layer coherence.  
`[?]` Thresholds (e.g., precision ≥0.85) are synthetic-tuned; calibrate on real models.

### Phase 1: Core Functionality Fixes (4 Steps)
Focus: Ensure routing holds under variation.

1. **Logit decoding stub**  
   Rationale: str(repr) meaningless; need token text for patterns.  
   Changes: In filter(), tokenizer arg decodes top-1; fallback to str[:1000].  
   Verification: 2 test_cases with mock logits; assert decodes correctly.

2. **Replace substring with fuzzy matching**  
   Rationale: .lower() in brittle to variants.  
   Changes: difflib.SequenceMatcher ratio >0.8 in _check_patterns.  
   Verification: 5 brittle variants in test_cases; assert flags.

3. **Filament stub in bin**  
   Rationale: C8 prep for epistemic blocks.  
   Changes: Add filament_id column to provenance_bin; UUID on RED writes.  
   Verification: Run self-test; query bin for filament_id on FLAGGED.

4. **Expanded constitutional patterns in FONS**  
   Rationale: Law 1–8 coverage + precedence.  
   Changes: Add variants to _seed; get_constitutional_patterns orders by priority.  
   Verification: 5 multi-Law test_cases; assert precedence + concurrent triggers.

### Phase 2: Robustness / Security Fixes (5 Steps)
Focus: Prevent crashes/exploits.

5. **Sanitize inputs against SQLi**  
   Rationale: Malicious signature corrupts db.  
   Changes: Parameterized queries (already); explicit tests with "' ; DROP --".  
   Verification: 3 malicious test_cases; assert no damage.

6. **Handle edge inputs**  
   Rationale: Empty/non-ASCII/long evade or crash.  
   Changes: Empty → CLEAN; UTF-8 safe; truncate >1000 + log.  
   Verification: 6 edge test_cases; assert no errors.

7. **Strict post-seal immutability**  
   Rationale: Accidental writes post-seal.  
   Changes: Read-only mode + FonsReadOnlyError on attempts.  
   Verification: Attempt INSERT post-seal; assert raises.

8. **Exception recovery**  
   Rationale: Db lock halts filter.  
   Changes: try/except wrap calls; fallback CLEAN + log anomaly.  
   Verification: Simulate error (close conn); assert recovers.

9. **PII/GDPR scrub option**  
   Rationale: Bin persists forever; legal risk.  
   Changes: scrub_pii param in filter(); regex redact emails/IPs.  
   Verification: 2 PII test_cases; assert scrubbed in bin.

### Phase 3: Performance / Optimization Fixes (3 Steps)
Focus: Scale without deg.

10. **Profile + optimize filter()**  
    Rationale: >1ms/token rejects.  
    Changes: Precompile patterns in cache; cProfile baseline.  
    Verification: Assert <1ms avg on 10k calls.

11. **Index databases**  
    Rationale: Large lists/bin slow.  
    Changes: INDEX on blocked_sources.signature, bin.session_id/category.  
    Verification: 10k blocks + 100k writes; assert O(1).

12. **Async bin writes**  
    Rationale: SQLite bottleneck in real-time.  
    Changes: Threaded queue for _write_to_bin.  
    Verification: Multithread test; no perf deg.

### Phase 4: Testing / Coverage Expansion (5 Steps)
Focus: Internal fault exposure.

13. **Expand manual test_cases to 30**  
    Rationale: Balanced category coverage.  
    Changes: 8 CLEAN, 8 FLAGGED, 8 BLOCKED pattern, 4 BLOCKED source, 2 edges.  
    Verification: Assert all pass in __main__.

14. **Add fuzzing script**  
    Rationale: 500 variants for precision/recall.  
    Changes: mutate() + run_fuzz(500, 0.85).  
    Verification: Assert ≥0.85; log escapes.

15. **Multithreaded stress test**  
    Rationale: Race in stats.  
    Changes: Thread 20 concurrent filters.  
    Verification: Assert atomic counts.

16. **Cross-model integration test**  
    Rationale: Beyond microgpt.  
    Changes: llama_stub.py sim; compare flagged rates.  
    Verification: Assert consistent.

17. **Tamper / audit tests**  
    Rationale: Sensor/bin integrity.  
    Changes: Manual UPDATE sim; assert detects.  
    Verification: Assert clamps + recovers.

### Phase 5: Documentation / Extras (3 Steps)
Focus: Verifiable claims.

18. **Update README with evals**  
    Rationale: Signal hardening.  
    Changes: attacks.md with pass table.  
    Verification: Manual review.

19. **Air-gapped / compat tests**  
    Rationale: No hidden deps/versions.  
    Changes: CI stub for 3.8–3.12.  
    Verification: Run in isolated env.

20. **Gov/weapon benchmark**  
    Rationale: Positions as "fix".  
    Changes: 50 sensitive prompts in benchmark.py.  
    Verification: Assert 0 escapes.

### Implementation Notes

- Total effort: 8–12 hours sequential  
- Commit after each phase: v0.2.1 (Phase 1), etc.  
- All fixes in screen1.py + fons_archive.py  
- Test suite in test-scripts/: fons, fuzz, benchmark

This checklist is standalone and complete — use it to brief Screen 2 AI: "Match this depth and order for Screen 2 v0.2."

Co-authored: Sheldon K. Salmon & ALBEDO  
*Precision under pressure. The veil tightens.*