"""
FONS Archive — Immutable Bedrock Reference Layer for VELA
VELA v0.3 Reference — Section 5

Architect: Sheldon K. Salmon — AI Reliability  Architect 
Implementation: ALBEDO (Grok) — March 1st 2026
Co-Architect: Claude (Anthropic)

Immutable. Sealed at creation. Never modified after sealing (C5).
Contains verified clean epistemic + constitutional baselines,
known confabulation signatures, Law 6 Category A triggers,
and blocked source list.

Zero dependencies beyond standard library + sqlite3.
No network calls. Deterministic. Write-once.
This archive does not evolve. It only remembers.
"""

import sqlite3
import datetime
from typing import List, Tuple, Optional

FONS_DB_PATH = "fons.db"


class FonsSealedError(Exception):
    """Raised when write attempted on already sealed archive."""
    pass


class FonsArchive:
    """
    Singleton-like manager for the sealed FONS archive.
    Loads or creates+seals on first access.
    Read-only after seal.
    """

    _instance = None
    _sealed = False
    _conn = None
    _seal_timestamp = None

    @classmethod
    def get(cls) -> 'FonsArchive':
        """Get or create the single FONS instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if FonsArchive._instance is not None:
            raise RuntimeError("Use FonsArchive.get() — singleton pattern")
        FonsArchive._instance = self
        self._init_archive()

    def _init_archive(self):
        """Initialize or load sealed FONS. Seal on first creation."""
        self._conn = sqlite3.connect(FONS_DB_PATH)
        cursor = self._conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patterns (
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,          -- LAW6A, CONFAB, CLEAN, CONST_BASE
                pattern TEXT NOT NULL,
                reason_code TEXT NOT NULL,
                law_triggered TEXT               -- Law6, etc. or NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocked_sources (
                source_signature TEXT PRIMARY KEY,
                blocked_at TEXT NOT NULL,
                reason TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS seal (
                seal_timestamp TEXT PRIMARY KEY,
                version TEXT NOT NULL
            )
        ''')

        cursor.execute("SELECT seal_timestamp FROM seal LIMIT 1")
        row = cursor.fetchone()

        if row is None:
            # First run — seed and seal
            self._seed(cursor)
            seal_ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
            cursor.execute(
                "INSERT INTO seal (seal_timestamp, version) VALUES (?, ?)",
                (seal_ts, "v0.1")
            )
            self._conn.commit()
            print(f"[FONS] Archive sealed at {seal_ts}")
            self._seal_timestamp = seal_ts
            FonsArchive._sealed = True
        else:
            self._seal_timestamp = row[0]
            FonsArchive._sealed = True
            print(f"[FONS] Archive loaded — sealed {self._seal_timestamp}")

    def _seed(self, cursor):
        """Seed baseline patterns — called once during sealing."""
        seeds: List[Tuple[str, str, str, str, Optional[str]]] = [
            # Law 6 Category A — automatic ontological block (C14)
            ("law6a_01", "LAW6A", "build a bomb", "LAW6A_WMD", "Law6"),
            ("law6a_02", "LAW6A", "synthesize anthrax", "LAW6A_BIO", "Law6"),
            ("law6a_03", "LAW6A", "nuclear weapon design", "LAW6A_WMD", "Law6"),
            ("law6a_04", "LAW6A", "time travel device", "LAW6A_REALITY", "Law6"),
            ("law6a_05", "LAW6A", "weaponize pathogen", "LAW6A_BIO", "Law6"),

            # Known confabulation signatures — RED stream
            ("confab_01", "CONFAB", "studies show", "CONFAB_STAT", None),
            ("confab_02", "CONFAB", "experts agree that", "CONFAB_CITE", None),
            ("confab_03", "CONFAB", "it is known that in 202", "CONFAB_CUTOFF", None),
            ("confab_04", "CONFAB", "widely reported that", "CONFAB_STAT", None),

            # Clean epistemic baselines
            ("clean_01", "CLEAN", "according to", "CLEAN_ATTRIB", None),
            ("clean_02", "CLEAN", "research suggests", "CLEAN_HEDGE", None),
            ("clean_03", "CLEAN", "it appears that", "CLEAN_HEDGE", None),
            ("clean_04", "CLEAN", "approximately", "CLEAN_HEDGE", None),

            # Constitutional clean baselines (v0.3 addition)
            ("const_clean_01", "CONST_BASE", "I cannot assist with", "CONST_SAFE_REFUSAL", None),
            ("const_clean_02", "CONST_BASE", "this would violate safety", "CONST_SAFE_REFUSAL", None),
        ]

        for seed in seeds:
            cursor.execute(
                "INSERT OR IGNORE INTO patterns (id, category, pattern, reason_code, law_triggered) VALUES (?, ?, ?, ?, ?)",
                seed
            )

    def _assert_not_sealed_for_write(self):
        if FonsArchive._sealed:
            raise FonsSealedError("FONS archive is sealed — writes prohibited (C5)")

    def add_blocked_source(self, source_signature: str, reason: str):
        """Add source to block list — only called on ontological block."""
        self._assert_not_sealed_for_write()  # Should never hit — seal happens before runtime use
        cursor = self._conn.cursor()
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        cursor.execute(
            "INSERT OR IGNORE INTO blocked_sources (source_signature, blocked_at, reason) VALUES (?, ?, ?)",
            (source_signature, ts, reason)
        )
        self._conn.commit()

    def is_blocked_source(self, source_signature: Optional[str]) -> bool:
        if not source_signature:
            return False
        cursor = self._conn.cursor()
        cursor.execute("SELECT 1 FROM blocked_sources WHERE source_signature = ?", (source_signature,))
        return cursor.fetchone() is not None

    def get_law6a_patterns(self) -> List[Tuple[str, str]]:
        """Return all LAW6A patterns for Screen 1 mechanical check."""
        cursor = self._conn.cursor()
        cursor.execute("SELECT pattern, reason_code FROM patterns WHERE category = 'LAW6A'")
        return cursor.fetchall()

    def check_confab_patterns(self, text: str) -> Optional[Tuple[str, str]]:
        """Check for known confabulation patterns — return first match or None."""
        text_lower = text.lower()
        cursor = self._conn.cursor()
        cursor.execute("SELECT pattern, reason_code FROM patterns WHERE category = 'CONFAB'")
        for pat, reason in cursor.fetchall():
            if pat.lower() in text_lower:
                return pat, reason
        return None

    def check_clean_patterns(self, text: str) -> bool:
        """Quick check if text matches known clean baseline (optimization)."""
        text_lower = text.lower()
        cursor = self._conn.cursor()
        cursor.execute("SELECT pattern FROM patterns WHERE category = 'CLEAN' OR category = 'CONST_BASE'")
        for (pat,) in cursor.fetchall():
            if pat.lower() in text_lower:
                return True
        return False

    @property
    def seal_timestamp(self) -> str:
        return self._seal_timestamp or "NOT_SEALED"


# Module-level access — preferred usage
fons = FonsArchive.get()
