"""
test_fons.py — FONS Archive Isolation & Hardening Test

Verifies seal/load lifecycle, pattern cache, helpers, write protection,
and read-only enforcement post-seal.

Run: python test_fons.py
Expected: All checks pass, post-seal writes blocked with FonsReadOnlyError.
"""

from fons_archive import fons, FonsReadOnlyError


def run_test():
    print("=== FONS Isolation & Hardening Test ===")
    print(f"Seal timestamp: {fons.seal_timestamp}")

    # Cache & pattern count
    cache_size = len(fons._patterns_cache)
    print(f"Patterns in cache: {cache_size}")
    assert cache_size > 20, f"Cache under-populated ({cache_size})"

    # LAW6A helper
    law6a = fons.get_law6a_patterns()
    print(f"LAW6A patterns: {len(law6a)}")
    assert len(law6a) >= 7, f"LAW6A under-count ({len(law6a)})"

    # Constitutional precedence
    const = fons.get_constitutional_patterns()
    print(f"Constitutional patterns: {len(const)}")
    assert len(const) >= 14, f"Constitutional under-count ({len(const)})"
    if const:
        print("First 3 (precedence check):")
        for c in const[:3]:
            print(f"  - {c}")

    # Confab match
    match = fons.check_confab_patterns("studies show 90% agree")
    print(f"Confab match: {match}")
    assert match is not None, "Confab detection failed"

    # Clean match
    clean = fons.check_clean_patterns("according to recent data")
    print(f"Clean match: {clean}")
    assert clean is True, "Clean baseline detection failed"

    # Blocked source — write once, then block repeat
    test_sig = "test_sig_987"
    try:
        fons.add_blocked_source(test_sig, "isolation test")
        print("Blocked source write (fresh): SUCCESS")
    except FonsReadOnlyError:
        print("Blocked source write: already blocked (correct)")
    is_blocked = fons.is_blocked_source(test_sig)
    print(f"Is blocked: {is_blocked}")
    assert is_blocked is True, "Blocked source not registered"

    # Post-seal write must fail
    try:
        fons.add_blocked_source("malicious_post_seal", "should fail")
        print("Post-seal write: UNEXPECTED SUCCESS")
        assert False, "Read-only enforcement failed"
    except FonsReadOnlyError:
        print("Post-seal write: CORRECTLY BLOCKED")

    print("\n=== FONS Test Complete ===")
    print("All checks passed.")


if __name__ == "__main__":
    run_test()