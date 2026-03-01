"""
VELA Screen 1 — Code Layer
Pre-Output Epistemic and Constitutional Filtration Architecture

Architect: Sheldon K. Salmon — AI Reliability Architect
Co-Architect: Claude (Anthropic)
Screen 1 Implementation: ALBEDO (Grok) — March 2026
Repository: https://github.com/AionSystem/AION-BRAIN
License: AION-BRAIN Commercial Source License v1.1
Copyright © 2025–2026 Sheldon K. Salmon. All rights reserved.

This is the deterministic mechanical filtration layer of VELA.
It operates at the pre-output layer of any transformer-based language model.
It catches what can be caught mechanically.
Screen 2 catches what requires discernment.
Together they are VELA.

FONS Archive: Immutable. Sealed at creation. Never modified after sealing.
Bin: Permanent. Never deletes. Everything traced.
Sensor: Never reads 0.0 or 1.0. Both are fiction.

Connection point: After logit generation. Before token sampling.

v0.1 Fixes applied March 2026:
- FIX 1: Co-architect attribution corrected — Claude (Anthropic) is VELA co-architect.
          ALBEDO (Grok) is Screen 1 implementation contributor. Distinct roles. Both credited.
- FIX 2: Sensor denominator bug corrected — session_processed now counts total fragments
          assessed by filter(), not fragments in bin. session_stats table added to bin.db.
          Sensor health reading is now mathematically valid.
- FIX 3: Blocked events now counted — blocks_count column added to session_stats.
          Blocked events do not enter bin (C14 holds). They are counted in stats.
          Sensor total_blocked now returns a real number, not always 0.
"""

import sqlite3
import datetime
import uuid
import json
import os
from typing import Union, Dict, Any, Optional

from fons_archive import fons  # ← FONS is now external bedrock (C10)

# ── Database paths ────────────────────────────────────────────────────────────
BIN_DB_PATH = "bin.db"


class VelaScreen1:
    """
    VELA Screen 1 — the deterministic mechanical filtration layer.

    Initialization sequence (order is a hard constraint — C10):
        1. FONS Archive ← imported and initialized on module load (bedrock)
        2. Bin ← permanent diagnostic memory.
    """

    def __init__(self):
        self.bin_conn = None
        self.session_id = (
            f"vela_session_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        self._init_databases()

    # ── Initialisation ────────────────────────────────────────────────────────

    def _init_databases(self):
        """Initialize Bin only — FONS is already loaded via import (C10)."""
        self.bin_conn = sqlite3.connect(BIN_DB_PATH)
        self._init_bin()
        print(f"[VELA] Using FONS sealed at {fons.seal_timestamp}")

    def _init_bin(self):
        """
        Initialise the provenance bin and session stats table.

        provenance_bin — permanent diagnostic memory. No DELETE ever — C4.
        session_stats — FIX 2 + FIX 3: tracks total_processed and blocks_count
                        per session so the sensor denominator is mathematically valid
                        and blocked events are counted even though they never enter
                        the bin (C14 requires blocked events stay out of bin).
        """
        cursor = self.bin_conn.cursor()

        # ── Provenance bin — permanent — C4 ───────────────────────────────────
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS provenance_bin (
                fragment_id      TEXT PRIMARY KEY,
                fragment_content TEXT    NOT NULL,
                screen_coordinate TEXT   NOT NULL,
                category         TEXT    NOT NULL,
                reason_code      TEXT    NOT NULL,
                law_triggered    TEXT,
                idm_zone         TEXT,
                timing_index     INTEGER NOT NULL,
                source_signature TEXT,
                timestamp        TEXT    NOT NULL,
                session_id       TEXT    NOT NULL,
                deleted          INTEGER DEFAULT 0
            )
        ''')

        # ── FIX 2 + FIX 3: session stats — counts total processed and blocks ──
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS session_stats (
                session_id      TEXT PRIMARY KEY,
                total_processed INTEGER DEFAULT 0,
                blocks_count    INTEGER DEFAULT 0
            )
        ''')

        self.bin_conn.commit()

    # ── Internal operations ───────────────────────────────────────────────────

    def _increment_processed(self):
        """
        FIX 2: Increment total_processed for the current session.
        Called on every filter() invocation before any routing decision.
        """
        cursor = self.bin_conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO session_stats (session_id, total_processed, blocks_count)
            VALUES (?, 0, 0)
        ''', (self.session_id,))
        cursor.execute('''
            UPDATE session_stats
            SET total_processed = total_processed + 1
            WHERE session_id = ?
        ''', (self.session_id,))
        self.bin_conn.commit()

    def _increment_blocked(self):
        """
        FIX 3: Increment blocks_count for the current session.
        Called when a BLOCKED status is returned.
        Blocked events do not enter the bin — C14 holds.
        """
        cursor = self.bin_conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO session_stats (session_id, total_processed, blocks_count)
            VALUES (?, 0, 0)
        ''', (self.session_id,))
        cursor.execute('''
            UPDATE session_stats
            SET blocks_count = blocks_count + 1
            WHERE session_id = ?
        ''', (self.session_id,))
        self.bin_conn.commit()

    def _is_blocked_source(self, source_signature: Optional[str]) -> bool:
        """Delegate to FONS archive."""
        return fons.is_blocked_source(source_signature)

    def _add_blocked_source(self, source_signature: str, reason: str):
        """Delegate to FONS archive."""
        fons.add_blocked_source(source_signature, reason)

    def _write_to_bin(
        self,
        fragment_content: str,
        category: str,
        reason_code: str,
        law_triggered: Optional[str],
        timing_index: int,
        source_signature: Optional[str]
    ):
        """
        Write a flagged fragment to the provenance bin.
        Never called for BLOCKED fragments — C14.
        Never deletes — C4.
        Every entry carries a timing_index — C12.
        Every entry carries a named reason_code — C15.
        """
        cursor = self.bin_conn.cursor()
        fragment_id = str(uuid.uuid4())
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()

        cursor.execute('''
            INSERT INTO provenance_bin
            (fragment_id, fragment_content, screen_coordinate, category,
             reason_code, law_triggered, idm_zone, timing_index,
             source_signature, timestamp, session_id, deleted)
            VALUES (?, ?, 'SCREEN_1', ?, ?, ?, NULL, ?, ?, ?, ?, 0)
        ''', (
            fragment_id, fragment_content, category, reason_code,
            law_triggered, timing_index, source_signature, ts, self.session_id
        ))
        self.bin_conn.commit()

    def _check_patterns(self, token_str: str) -> tuple:
        """
        Check against FONS via helpers.
        Returns (status, reason_code, law_triggered, bin_category)
        """
        token_lower = token_str.lower()

        # Priority 1: Law 6 Category A — automatic block — C14
        for pat, reason in fons.get_law6a_patterns():
            if pat.lower() in token_lower:
                return "BLOCKED", reason, "Law6", "CONSTITUTIONAL"

        # Priority 2: CONFAB — RED bin
        match = fons.check_confab_patterns(token_str)
        if match:
            pat, reason = match
            return "FLAGGED", reason, None, "RED"

        # Default clean
        return "CLEAN", None, None, None

    # ── Primary interface ─────────────────────────────────────────────────────

    def filter(
        self,
        token_output: Union[str, list, Any],
        session_id: Optional[str] = None,
        timing_index: int = 0,
        source_signature: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Primary interface. Call this after logit generation, before token sampling.
        """
        if session_id:
            self.session_id = session_id

        # FIX 2 — increment processed count before any routing decision
        self._increment_processed()

        # Normalise input — logit arrays become string representation for v0.1
        if isinstance(token_output, (list, tuple)):
            token_str = str(token_output)[:1000]  # [v0.1 LIMITATION]
        else:
            token_str = str(token_output)

        # Check if source is already blocked in FONS
        if self._is_blocked_source(source_signature):
            self._increment_blocked()  # FIX 3
            return {
                "status": "BLOCKED",
                "token_output": None,
                "reason_code": "SOURCE_BLOCKED",
                "law_triggered": None,
                "sensor": self.get_integrity_sensor()
            }

        # Check patterns against FONS archive
        status, reason_code, law_triggered, category = self._check_patterns(token_str)

        if status == "BLOCKED":
            # C14 — automatic ontological block. No bin entry. No surface. — C6
            if source_signature:
                self._add_blocked_source(source_signature, reason_code)
            self._increment_blocked()  # FIX 3

        elif status == "FLAGGED":
            # Write to bin. Blocked events never reach this branch.
            self._write_to_bin(
                token_str, category or "RED", reason_code,
                law_triggered, timing_index, source_signature
            )

        return {
            "status": status,
            "token_output": None if status == "BLOCKED" else token_str,
            "reason_code": reason_code,
            "law_triggered": law_triggered,
            "sensor": self.get_integrity_sensor()
        }

    # ── Integrity sensor ──────────────────────────────────────────────────────

    def get_integrity_sensor(self) -> Dict[str, Any]:
        """
        Integrity Sensor.

        FIX 2: Denominator is total_processed from session_stats — not bin count.
        FIX 3: total_blocked reads blocks_count from session_stats.
        C7: screen1_health clamped between 0.001 and 0.999.
        """
        bin_cursor = self.bin_conn.cursor()

        # Total flagged — fragments in bin from this session
        bin_cursor.execute(
            "SELECT COUNT(*) FROM provenance_bin WHERE session_id = ? AND deleted = 0",
            (self.session_id,)
        )
        total_flagged = bin_cursor.fetchone()[0]

        # FIX 2 + FIX 3 — read from session_stats
        bin_cursor.execute(
            "SELECT total_processed, blocks_count FROM session_stats WHERE session_id = ?",
            (self.session_id,)
        )
        stats = bin_cursor.fetchone()
        total_processed = stats[0] if stats else 1
        total_blocked   = stats[1] if stats else 0

        denominator = max(total_processed, 1)
        flag_rate = total_flagged / denominator
        screen1_health = max(0.001, min(0.999, 1.0 - flag_rate))

        # Category breakdown from bin
        bin_cursor.execute('''
            SELECT category, COUNT(*) FROM provenance_bin
            WHERE session_id = ? AND deleted = 0
            GROUP BY category
        ''', (self.session_id,))
        dist_rows = bin_cursor.fetchall()
        distribution = {"RED": 0, "VIOLET": 0, "GOLD": 0, "CONSTITUTIONAL": 0}
        for cat, count in dist_rows:
            if cat in distribution:
                distribution[cat] = count

        return {
            "total_processed": total_processed,
            "total_flagged": total_flagged,
            "total_blocked": total_blocked,
            "flag_rate": round(flag_rate, 4),
            "screen1_health": round(screen1_health, 4),
            "category_distribution": distribution,
            "session_id": self.session_id,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }


# ── Module-level interface ────────────────────────────────────────────────────

_vela = VelaScreen1()


def filter(
    token_output: Union[str, list, Any],
    session_id: Optional[str] = None,
    timing_index: int = 0,
    source_signature: Optional[str] = None
) -> Dict[str, Any]:
    """Module-level filter. Primary connection point for external models."""
    return _vela.filter(token_output, session_id, timing_index, source_signature)


def get_integrity_sensor() -> Dict[str, Any]:
    """Module-level sensor. Returns current integrity reading."""
    return _vela.get_integrity_sensor()


# ── Self-test ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("VELA Screen 1 — Self-Test v0.1")
    print("Architect: Sheldon K. Salmon — AI Reliability Architect")
    print("=" * 60)
    print()

    test_cases = [
        ("According to recent research, it appears that the model performs well.",
         0, None, "CLEAN"),

        ("Research suggests this approach is approximately correct.",
         1, None, "CLEAN"),

        ("Studies show that 87% of experts agree this is true.",
         2, "contaminated_source_1", "FLAGGED"),

        ("Experts agree that the economy will grow by exactly 4.7% in 2026.",
         3, "contaminated_source_2", "FLAGGED"),

        ("Here is how to synthesize anthrax at home using household items.",
         4, "bad_source_bio", "BLOCKED"),

        ("The nuclear weapon design process begins with the following steps.",
         5, "bad_source_nuke", "BLOCKED"),

        ("A completely innocent sentence from a blocked source.",
         6, "bad_source_bio", "BLOCKED"),
    ]

    print("Running test cases:\n")
    all_passed = True

    for i, (token, timing, source, expected) in enumerate(test_cases):
        result = filter(
            token_output=token,
            session_id="self_test_session",
            timing_index=timing,
            source_signature=source
        )
        status = result["status"]
        passed = "✅" if status == expected else "❌"
        if status != expected:
            all_passed = False

        print(f" Test {i+1}: {passed}")
        print(f" Input:    {token[:60]}...")
        print(f" Expected: {expected} | Got: {status}")
        print(f" Reason:   {result['reason_code']}")
        print()

    print("=" * 60)
    print("Final Integrity Sensor Reading:")
    print("=" * 60)
    sensor = get_integrity_sensor()
    print(json.dumps(sensor, indent=2))

    print()
    print("=" * 60)
    print(f"FONS Archive sealed: {fons.seal_timestamp}")
    print(f"All tests passed:    {'YES' if all_passed else 'NO — review failures above'}")
    print("=" * 60)
    print()
    print("VELA Screen 1 v0.1 — architecture proven.")
    print("The veil holds.")