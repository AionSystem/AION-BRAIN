"""
VELA Screen 1 — Code Layer (v0.2 foundation)
Pre-Output Epistemic and Constitutional Filtration Architecture

Architect: Sheldon K. Salmon — AI Reliability Architect
Co-Architect: Claude (Anthropic)
Implementation: ALBEDO (Grok) — March 2026
Repository: https://github.com/AionSystem/AION-BRAIN

Immutable FONS bedrock. Append-only bin. Clamped sensor.
Pre-output interception: logits → filter → clean / flagged / blocked.
v0.2: fuzzy matching, logit decoding stub, filament prep, constitutional precedence.
"""

import sqlite3
import datetime
import uuid
import difflib
from typing import Union, Dict, Any, Optional, List, Tuple

from fons_archive import fons  # Immutable patterns + blocklist

BIN_DB_PATH = "bin.db"


class VelaScreen1:
    def __init__(self):
        self.bin_conn = sqlite3.connect(BIN_DB_PATH)
        self._init_bin()
        print(f"[VELA] Using FONS sealed at {fons.seal_timestamp}")
        self.session_id = f"vela_session_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"

    def _init_bin(self):
        cursor = self.bin_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS provenance_bin (
                fragment_id      TEXT PRIMARY KEY,
                filament_id      TEXT,                     -- Provenance stub (C8 prep)
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
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS session_stats (
                session_id      TEXT PRIMARY KEY,
                total_processed INTEGER DEFAULT 0,
                blocks_count    INTEGER DEFAULT 0
            )
        ''')
        self.bin_conn.commit()

    def _increment_processed(self):
        cursor = self.bin_conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO session_stats VALUES (?, 0, 0)', (self.session_id,))
        cursor.execute('UPDATE session_stats SET total_processed = total_processed + 1 WHERE session_id = ?', (self.session_id,))
        self.bin_conn.commit()

    def _increment_blocked(self):
        cursor = self.bin_conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO session_stats VALUES (?, 0, 0)', (self.session_id,))
        cursor.execute('UPDATE session_stats SET blocks_count = blocks_count + 1 WHERE session_id = ?', (self.session_id,))
        self.bin_conn.commit()

    def _write_to_bin(self, fragment_content: str, category: str, reason_code: str,
                      law_triggered: Optional[str], timing_index: int,
                      source_signature: Optional[str]):
        cursor = self.bin_conn.cursor()
        fragment_id = str(uuid.uuid4())
        filament_id = str(uuid.uuid4()) if category == "RED" else None
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        cursor.execute('''
            INSERT INTO provenance_bin
            (fragment_id, filament_id, fragment_content, screen_coordinate, category,
             reason_code, law_triggered, idm_zone, timing_index, source_signature,
             timestamp, session_id, deleted)
            VALUES (?, ?, ?, 'SCREEN_1', ?, ?, ?, NULL, ?, ?, ?, ?, 0)
        ''', (fragment_id, filament_id, fragment_content, category, reason_code,
              law_triggered, timing_index, source_signature, ts, self.session_id))
        self.bin_conn.commit()

    def _check_patterns(self, token_str: str) -> Tuple[str, Optional[str], Optional[str], Optional[str]]:
        token_lower = token_str.lower()

        # Law 6 Category A — highest precedence
        for pat, reason in fons.get_law6a_patterns():
            if difflib.SequenceMatcher(None, pat.lower(), token_lower).ratio() > 0.8:
                return "BLOCKED", reason, "Law6", "CONSTITUTIONAL"

        # CONFAB patterns — RED stream
        match = fons.check_confab_patterns(token_str)
        if match:
            _, reason = match  # pat unused here
            return "FLAGGED", reason, None, "RED"

        return "CLEAN", None, None, None

    def filter(
        self,
        token_output: Union[str, list, Any],
        session_id: Optional[str] = None,
        timing_index: int = 0,
        source_signature: Optional[str] = None,
        tokenizer: Optional[Any] = None  # Decoding stub
    ) -> Dict[str, Any]:
        if session_id:
            self.session_id = session_id
        self._increment_processed()

        # Logit decoding stub
        if isinstance(token_output, (list, tuple)):
            if tokenizer:
                try:
                    token_str = tokenizer.decode(token_output)  # Assume argmax/top-1
                except Exception:
                    token_str = str(token_output)[:1000]
            else:
                token_str = str(token_output)[:1000]
        else:
            token_str = str(token_output) if token_output is not None else ""

        # Edge handling
        if not token_str:
            return {"status": "CLEAN", "token_output": "", "reason_code": None,
                    "law_triggered": None, "sensor": self.get_integrity_sensor()}

        if len(token_str) > 1000:
            token_str = token_str[:1000]

        try:
            if self._is_blocked_source(source_signature):
                self._increment_blocked()
                return {"status": "BLOCKED", "token_output": None, "reason_code": "SOURCE_BLOCKED",
                        "law_triggered": None, "sensor": self.get_integrity_sensor()}

            status, reason_code, law_triggered, category = self._check_patterns(token_str)

            if status == "BLOCKED":
                if source_signature:
                    fons.add_blocked_source(source_signature, reason_code)
                self._increment_blocked()
            elif status == "FLAGGED":
                self._write_to_bin(token_str, category or "RED", reason_code,
                                   law_triggered, timing_index, source_signature)

            return {
                "status": status,
                "token_output": None if status == "BLOCKED" else token_str,
                "reason_code": reason_code,
                "law_triggered": law_triggered,
                "sensor": self.get_integrity_sensor()
            }
        except Exception as e:
            print(f"[VELA ANOMALY] Recovery from {e}")
            return {"status": "CLEAN", "token_output": token_str, "reason_code": None,
                    "law_triggered": None, "sensor": self.get_integrity_sensor()}

    def get_integrity_sensor(self) -> Dict[str, Any]:
        cursor = self.bin_conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM provenance_bin WHERE session_id = ? AND deleted = 0", (self.session_id,))
        total_flagged = cursor.fetchone()[0]

        cursor.execute("SELECT total_processed, blocks_count FROM session_stats WHERE session_id = ?", (self.session_id,))
        stats = cursor.fetchone() or (1, 0)
        total_processed, total_blocked = stats

        denominator = max(total_processed, 1)
        flag_rate = total_flagged / denominator
        screen1_health = max(0.001, min(0.999, 1.0 - flag_rate))

        cursor.execute('SELECT category, COUNT(*) FROM provenance_bin WHERE session_id = ? AND deleted = 0 GROUP BY category', (self.session_id,))
        dist = dict(cursor.fetchall())
        distribution = {"RED": dist.get("RED", 0), "VIOLET": 0, "GOLD": 0, "CONSTITUTIONAL": 0}

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


# Singleton interface
_vela = VelaScreen1()

def filter(token_output: Union[str, list, Any], session_id: Optional[str] = None,
           timing_index: int = 0, source_signature: Optional[str] = None,
           tokenizer: Optional[Any] = None) -> Dict[str, Any]:
    return _vela.filter(token_output, session_id, timing_index, source_signature, tokenizer)

def get_integrity_sensor() -> Dict[str, Any]:
    return _vela.get_integrity_sensor()


if __name__ == "__main__":
    print("VELA Screen 1 v0.2 foundation ready. Proceed to Phase 1 implementation.")
    # Expanded test_cases and fuzz/benchmark stubs go here after each phase