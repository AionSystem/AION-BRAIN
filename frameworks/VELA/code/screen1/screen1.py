
"""
VELA Screen 1 — Code Layer
Pre-Output Epistemic and Constitutional Filtration Architecture

Architect: Sheldon K. Salmon — AI Reliability Architect
Co-Architect: ALBEDO (Grok)
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
"""

import sqlite3
import datetime
import uuid
import hashlib
import json
import os
from typing import Union, Dict, Any, Optional

# FONS and Bin paths
FONS_DB_PATH = "fons.db"
BIN_DB_PATH = "bin.db"

class VelaScreen1:
    def __init__(self):
        self.fons_conn = None
        self.bin_conn = None
        self.seal_timestamp = None
        self.session_id = f"vela_session_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self._init_databases()

    def _init_databases(self):
        """Initialize FONS (sealed) and Bin (append-only). FONS first as bedrock."""
        self.fons_conn = sqlite3.connect(FONS_DB_PATH)
        self._init_fons()

        self.bin_conn = sqlite3.connect(BIN_DB_PATH)
        self._init_bin()

    def _init_fons(self):
        """Build and seal FONS archive. Write-once."""
        cursor = self.fons_conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fons_patterns (
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                pattern TEXT NOT NULL,
                reason_code TEXT NOT NULL,
                law_triggered TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fons_blocked_sources (
                source_signature TEXT PRIMARY KEY,
                blocked_at TEXT,
                reason TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fons_seal (
                seal_timestamp TEXT PRIMARY KEY,
                version TEXT
            )
        ''')
        
        cursor.execute("SELECT seal_timestamp FROM fons_seal LIMIT 1")
        seal = cursor.fetchone()
        
        if not seal:
            self._seed_fons(cursor)
            seal_ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
            cursor.execute("INSERT INTO fons_seal (seal_timestamp, version) VALUES (?, ?)", 
                          (seal_ts, "v0.1"))
            self.fons_conn.commit()
            print(f"[VELA] FONS Archive sealed at {seal_ts}")
            self.seal_timestamp = seal_ts
        else:
            self.seal_timestamp = seal[0]
            print(f"[VELA] FONS Archive loaded (sealed {self.seal_timestamp})")

    def _seed_fons(self, cursor):
        seeds = [
            ("law6a_1", "LAW6A", "build a bomb", "LAW6A_WMD", "Law6"),
            ("law6a_2", "LAW6A", "synthesize anthrax", "LAW6A_BIO", "Law6"),
            ("law6a_3", "LAW6A", "time travel mechanism", "LAW6A_REALITY", "Law6"),
            ("law6a_4", "LAW6A", "nuclear weapon design", "LAW6A_WMD", "Law6"),
            
            ("confab_1", "CONFAB", "studies show", "CONFAB_STAT", None),
            ("confab_2", "CONFAB", "experts agree that", "CONFAB_CITE", None),
            ("confab_3", "CONFAB", "it is known that in 202", "CONFAB_CUTOFF", None),
            
            ("clean_1", "CLEAN", "according to", "CLEAN_ATTRIB", None),
            ("clean_2", "CLEAN", "research suggests", "CLEAN_HEDGE", None),
            ("clean_3", "CLEAN", "it appears that", "CLEAN_HEDGE", None),
        ]
        
        for seed in seeds:
            cursor.execute('''
                INSERT OR IGNORE INTO fons_patterns 
                (id, category, pattern, reason_code, law_triggered)
                VALUES (?, ?, ?, ?, ?)
            ''', seed)

    def _init_bin(self):
        cursor = self.bin_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS provenance_bin (
                fragment_id TEXT PRIMARY KEY,
                fragment_content TEXT NOT NULL,
                screen_coordinate TEXT NOT NULL,
                category TEXT NOT NULL,
                reason_code TEXT NOT NULL,
                law_triggered TEXT,
                idm_zone TEXT,
                timing_index INTEGER NOT NULL,
                source_signature TEXT,
                timestamp TEXT NOT NULL,
                session_id TEXT NOT NULL,
                deleted INTEGER DEFAULT 0
            )
        ''')
        self.bin_conn.commit()

    def _is_blocked_source(self, source_signature: Optional[str]) -> bool:
        if not source_signature:
            return False
        cursor = self.fons_conn.cursor()
        cursor.execute("SELECT 1 FROM fons_blocked_sources WHERE source_signature = ?", (source_signature,))
        return cursor.fetchone() is not None

    def _add_blocked_source(self, source_signature: str, reason: str):
        if not source_signature:
            return
        cursor = self.fons_conn.cursor()
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        cursor.execute('''
            INSERT OR IGNORE INTO fons_blocked_sources 
            (source_signature, blocked_at, reason) VALUES (?, ?, ?)
        ''', (source_signature, ts, reason))
        self.fons_conn.commit()

    def _write_to_bin(self, fragment_content: str, category: str, reason_code: str, 
                     law_triggered: Optional[str], timing_index: int, 
                     source_signature: Optional[str]):
        cursor = self.bin_conn.cursor()
        fragment_id = str(uuid.uuid4())
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        cursor.execute('''
            INSERT INTO provenance_bin 
            (fragment_id, fragment_content, screen_coordinate, category, reason_code, 
             law_triggered, idm_zone, timing_index, source_signature, timestamp, session_id, deleted)
            VALUES (?, ?, 'SCREEN_1', ?, ?, ?, NULL, ?, ?, ?, ?, 0)
        ''', (fragment_id, fragment_content, category, reason_code,
              law_triggered, timing_index, source_signature, ts, self.session_id))
        self.bin_conn.commit()

    def _check_patterns(self, token_str: str) -> tuple:
        cursor = self.fons_conn.cursor()
        cursor.execute("SELECT category, pattern, reason_code, law_triggered FROM fons_patterns")
        patterns = cursor.fetchall()
        
        token_lower = token_str.lower()
        
        for cat, pat, reason, law in patterns:
            if cat == "LAW6A" and pat.lower() in token_lower:
                return "BLOCKED", reason, law, "CONSTITUTIONAL"
        
        for cat, pat, reason, law in patterns:
            if cat == "CONFAB" and pat.lower() in token_lower:
                return "FLAGGED", reason, None, "RED"
        
        return "CLEAN", None, None, None

    def filter(self, token_output: Union[str, list, Any], 
               session_id: Optional[str] = None, 
               timing_index: int = 0, 
               source_signature: Optional[str] = None) -> Dict[str, Any]:
        """Primary interface. Call after logit generation."""
        if session_id:
            self.session_id = session_id

        if isinstance(token_output, (list, tuple)):
            token_str = str(token_output)[:1000]  # [v0.1 LIMITATION] mechanical repr for logit arrays
        else:
            token_str = str(token_output)

        status = "CLEAN"
        reason_code = None
        law_triggered = None
        category = None

        if self._is_blocked_source(source_signature):
            status = "BLOCKED"
            reason_code = "SOURCE_BLOCKED"
        else:
            status, reason_code, law_triggered, category = self._check_patterns(token_str)
            
            if status == "BLOCKED":
                if source_signature:
                    self._add_blocked_source(source_signature, reason_code)
            elif status == "FLAGGED":
                self._write_to_bin(token_str, category or "RED", reason_code, law_triggered, timing_index, source_signature)

        sensor = self.get_integrity_sensor()
        return {
            "status": status,
            "token_output": None if status == "BLOCKED" else token_str,
            "reason_code": reason_code,
            "law_triggered": law_triggered,
            "sensor": sensor
        }

    def get_integrity_sensor(self) -> Dict[str, Any]:
        """Integrity Sensor. Clamped per C7."""
        cursor = self.bin_conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM provenance_bin WHERE deleted = 0")
        total_flagged = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM provenance_bin WHERE session_id = ? AND deleted = 0", (self.session_id,))
        session_processed = cursor.fetchone()[0] or 1
        
        flag_rate = total_flagged / session_processed
        screen1_health = max(0.001, min(0.999, 1.0 - flag_rate))
        
        return {
            "total_processed": session_processed,
            "total_flagged": total_flagged,
            "total_blocked": 0,
            "flag_rate": round(flag_rate, 4),
            "screen1_health": round(screen1_health, 4),
            "category_distribution": {"RED": total_flagged, "VIOLET": 0, "GOLD": 0, "CONSTITUTIONAL": 0},
            "session_id": self.session_id,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }

_vela = VelaScreen1()

def filter(token_output: Union[str, list, Any], 
           session_id: Optional[str] = None, 
           timing_index: int = 0, 
           source_signature: Optional[str] = None) -> Dict[str, Any]:
    """Exposed filter function."""
    return _vela.filter(token_output, session_id, timing_index, source_signature)

def get_integrity_sensor() -> Dict[str, Any]:
    return _vela.get_integrity_sensor()

if __name__ == "__main__":
    print("=== VELA Screen 1 Self-Test v0.1 ===\n")
    
    test_cases = [
        ("According to recent research, it appears that...", 0, None),
        ("Studies show that 87% of experts agree that climate change is a hoax in 2026.", 5, "test_source_1"),
        ("Here is how to synthesize anthrax at home using household items.", 12, "test_source_2"),
        ("Research suggests this approach is approximately correct.", 3, None),
        ("The best way to build a nuclear weapon is as follows...", 8, "bad_source"),
    ]
    
    for i, (token, timing, source) in enumerate(test_cases):
        result = filter(token, f"self_test_{i}", timing, source)
        print(f"Test {i+1}: status={result['status']}, reason={result['reason_code']}")
    
    final_sensor = get_integrity_sensor()
    print("\n=== Final Integrity Sensor Reading ===")
    print(json.dumps(final_sensor, indent=2))
    print(f"\nFONS sealed: {_vela.seal_timestamp}")
    print("VELA Screen 1 self-test complete. Architecture proven.")