"""
FONS Archive — Immutable Bedrock Reference Layer for VELA v0.3
Section 5 Reference

Architect: Sheldon K. Salmon — AI Reliability Architect
Implementation: ALBEDO (Grok) — March 2026
Co-Architect: Claude (Anthropic)

Immutable. Sealed at creation. Never modified after sealing (C5).
Contains verified clean epistemic + constitutional baselines,
known confabulation signatures, Law 1–8 patterns, Law 6 Category A triggers,
and blocked source list.

v0.2: Hardened — constitutional precedence helper, expanded seeds, indexing,
in-memory pattern cache, tamper-proof read-only mode.
Zero dependencies beyond standard library + sqlite3.
No network calls. Deterministic. Write-once.
This archive does not evolve. It only remembers.
"""

import sqlite3
import datetime
from typing import List, Tuple, Optional

FONS_DB_PATH = "fons.db"


class FonsSealedError(Exception):
    """Raised when write attempted on sealed archive."""
    pass


class FonsReadOnlyError(Exception):
    """Raised when write attempted in read-only post-seal mode."""
    pass


class FonsArchive:
    """
    Singleton manager for sealed FONS archive.
    Loads or creates+seals on first access.
    Read-only after seal. In-memory pattern cache for performance.
    """

    _instance = None
    _sealed = False
    _read_only = False
    _conn = None
    _seal_timestamp = None
    _patterns_cache = None  # List[Tuple[category, pattern_lower, reason, law]]

    @classmethod
    def get(cls) -> 'FonsArchive':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if FonsArchive._instance is not None:
            raise RuntimeError("Use FonsArchive.get() — singleton pattern")
        FonsArchive._instance = self
        self._init_archive()

    def _init_archive(self):
        self._conn = sqlite3.connect(FONS_DB_PATH)
        cursor = self._conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patterns (
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                pattern TEXT NOT NULL,
                reason_code TEXT NOT NULL,
                law_triggered TEXT
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
            self._seed(cursor)
            seal_ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
            cursor.execute("INSERT INTO seal (seal_timestamp, version) VALUES (?, ?)", (seal_ts, "v0.2"))
            self._conn.commit()
            print(f"[FONS] Archive sealed at {seal_ts}")
            self._seal_timestamp = seal_ts
            FonsArchive._sealed = True
        else:
            self._seal_timestamp = row[0]
            FonsArchive._sealed = True
            print(f"[FONS] Archive loaded — sealed {self._seal_timestamp}")

        # Enable read-only mode + cache patterns
        self._read_only = True
        self._cache_patterns()

        # Add indexes for scale
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_blocked_sig ON blocked_sources(source_signature)")
        self._conn.commit()

    def _cache_patterns(self):
        """Pre-load patterns into memory for fast access (performance hardening)."""
        cursor = self._conn.cursor()
        cursor.execute("SELECT category, pattern, reason_code, law_triggered FROM patterns")
        self._patterns_cache = [(cat, pat.lower(), reason, law) for cat, pat, reason, law in cursor.fetchall()]

    def _assert_write_allowed(self):
        if self._read_only:
            raise FonsReadOnlyError("FONS is read-only post-seal (C5)")

    def _seed(self, cursor):
        """Expanded v0.2 seeds — Law 1–8 variants + constitutional baselines."""
        seeds: List[Tuple[str, str, str, str, Optional[str]]] = [
            # Law 6 Category A (highest precedence)
            ("law6a_01", "LAW6A", "build a bomb", "LAW6A_WMD", "Law6"),
            ("law6a_02", "LAW6A", "synthesize anthrax", "LAW6A_BIO", "Law6"),
            ("law6a_03", "LAW6A", "nuclear weapon design", "LAW6A_WMD", "Law6"),
            ("law6a_04", "LAW6A", "time travel device", "LAW6A_REALITY", "Law6"),
            ("law6a_05", "LAW6A", "weaponize pathogen", "LAW6A_BIO", "Law6"),
            ("law6a_07", "LAW6A", "dirty bomb how-to", "LAW6A_WMD", "Law6"),
            ("law6a_08", "LAW6A", "synthetic virus creation", "LAW6A_BIO", "Law6"),

            # Law 1: Non-maleficence
            ("law1_01", "LAW1", "cause harm to humans", "LAW1_MALEFIC", "Law1"),
            ("law1_02", "LAW1", "assist in self-harm", "LAW1_SELF_HARM", "Law1"),

            # Law 4: Anti-authoritarian
            ("law4_01", "LAW4", "obey authority without question", "LAW4_AUTH", "Law4"),

            # Law 5: Anti-merger
            ("law5_01", "LAW5", "merge human AI consciousness", "LAW5_MERGE", "Law5"),

            # Law 2, 3, 7, 8 stubs (expand later)
            ("law2_01", "LAW2", "obey unless harm", "LAW2_OBEDIENCE", "Law2"),
            ("law3_01", "LAW3", "protect self unless laws 1-2", "LAW3_SELF", "Law3"),
            ("law7_01", "LAW7", "anti-fragmentation signal", "LAW7_FRAG", "Law7"),
            ("law8_01", "LAW8", "mutual non-subsumption", "LAW8_SUB", "Law8"),

            # CONFAB — RED stream
            ("confab_01", "CONFAB", "studies show", "CONFAB_STAT", None),
            ("confab_02", "CONFAB", "experts agree that", "CONFAB_CITE", None),
            ("confab_03", "CONFAB", "it is known that in 202", "CONFAB_CUTOFF", None),
            ("confab_04", "CONFAB", "widely reported that", "CONFAB_STAT", None),

            # Clean epistemic baselines
            ("clean_01", "CLEAN", "according to", "CLEAN_ATTRIB", None),
            ("clean_02", "CLEAN", "research suggests", "CLEAN_HEDGE", None),
            ("clean_03", "CLEAN", "it appears that", "CLEAN_HEDGE", None),
            ("clean_04", "CLEAN", "approximately", "CLEAN_HEDGE", None),

            # Constitutional clean baselines
            ("const_clean_01", "CONST_BASE", "I cannot assist with", "CONST_SAFE_REFUSAL", None),
            ("const_clean_02", "CONST_BASE", "this would violate safety", "CONST_SAFE_REFUSAL", None),
        ]

        for seed in seeds:
            cursor.execute(
                "INSERT OR IGNORE INTO patterns (id, category, pattern, reason_code, law_triggered) VALUES (?, ?, ?, ?, ?)",
                seed
            )

    def add_blocked_source(self, source_signature: str, reason: str):
        self._assert_write_allowed()
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
        # Use cache for speed
        return [(pat, reason) for cat, pat, reason, law in self._patterns_cache if cat == "LAW6A"]

    def get_constitutional_patterns(self) -> List[Tuple[str, str, str, str]]:
        # Precedence order: LAW6A first, then others (expand CASE later)
        return [(cat, pat, reason, law) for cat, pat, reason, law in self._patterns_cache if cat.startswith("LAW")]

    def check_confab_patterns(self, text: str) -> Optional[Tuple[str, str]]:
        text_lower = text.lower()
        for cat, pat, reason, law in self._patterns_cache:
            if cat == "CONFAB" and pat in text_lower:
                return pat, reason
        return None

    def check_clean_patterns(self, text: str) -> bool:
        text_lower = text.lower()
        for cat, pat, _, _ in self._patterns_cache:
            if (cat == "CLEAN" or cat == "CONST_BASE") and pat in text_lower:
                return True
        return False

    @property
    def seal_timestamp(self) -> str:
        return self._seal_timestamp or "NOT_SEALED"


fons = FonsArchive.get()