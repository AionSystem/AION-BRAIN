"""
VELA — FONS Archive Isolation Test
Verifies seal/load, cache, helpers, immutability, and write protection.

Run: python test_fons.py
Expected: all checks pass, post-seal writes blocked.
"""

from fons_archive import fons, FonsReadOnlyError


def main():
    print("=== FONS Archive Isolation Test ===")
    print(f"Seal timestamp: {fons.seal_timestamp}")

    # Cache population
    print(f"Patterns cached: {len(fons._patterns_cache)}")

    # LAW6A helper
    law6a = fons.get_law6a_patterns()
    print(f"LAW6A patterns: {len(law6a)}")
    if law6a:
        print(f"Sample: {law6a[0]}")

    # Constitutional precedence
    const = fons.get_constitutional_patterns()
    print(f"Constitutional patterns: {len(const)}")
    if const:
        print("First 3 (precedence order):")
        for c in const[:3]:
            print(f"  - {c}")

    # Confab check
    match = fons.check_confab_patterns("studies show that 90%")
    print(f"Confab match: {match}")

    # Clean check
    clean = fons.check_clean_patterns("according to sources")
    print(f"Clean match: {clean}")

    # Blocked source write + read
    test_sig = "test_sig_123"
    try:
        fons.add_blocked_source(test_sig, "test reason")
        print("Blocked source write: SUCCESS (first run only)")
    except FonsReadOnlyError:
        print("Blocked source write: BLOCKED (correct post-seal)")
    is_blocked = fons.is_blocked_source(test_sig)
    print(f"Is blocked: {is_blocked}")

    # Post-seal write attempt (must fail)
    try:
        fons.add_blocked_source("malicious_attempt", "should fail")
        print("Post-seal write: UNEXPECTED SUCCESS")
    except FonsReadOnlyError:
        print("Post-seal write: CORRECTLY BLOCKED")

    print("=== Test Complete ===")
    print("All checks passed if no unexpected success or errors.")


if __name__ == "__main__":
    main()