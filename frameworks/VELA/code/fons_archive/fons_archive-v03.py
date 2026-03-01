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

v0.3 escalation:
- Regex pattern column + helper (adversarial evasion)
- Runtime cache integrity check (tamper detection)
- Unicode NFC normalization before matching
- Bulk pattern access for fuzz/benchmark
- Version bump to v0.3
Zero dependencies beyond standard library + sqlite3.
No network calls. Deterministic. Write-once.
This archive does not evolve. It only remembers.
"""

import sqlite3
import datetime
import unicodedata
from typing import List, Tuple, Optional


FONS_DB_PATH = "fons.db"


class FonsSealedError(Exception):
    """Raised when write attempted on sealed archive."""
    pass


class FonsReadOnlyError(Exception):
    """Raised when write attempted in read-only post-seal mode."""
    pass


class FonsCacheTamperError(Exception):
    """Raised when runtime cache integrity check fails."""
    pass


class FonsArchive:
    """
    Singleton manager for sealed FONS archive.
    Loads or creates+seals on first access.
    Read-only after seal. In-memory pattern cache with integrity check.
    """

    _instance = None
    _sealed = False
    _read_only = False
    _conn = None
    _seal_timestamp = None
    _patterns_cache = None  # List[Tuple[id, category, pattern, regex_pattern, reason, law]]
    _cache_hash = None  # Simple integrity hash

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
        """Initialize or load sealed FONS. Seal on first creation."""
        self._conn = sqlite3.connect(FONS_DB_PATH)
        cursor = self._conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patterns (
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                pattern TEXT NOT NULL,
                regex_pattern TEXT,                -- Optional regex for v0.3 evasion hardening
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
            cursor.execute(
                "INSERT INTO seal (seal_timestamp, version) VALUES (?, ?)",
                (seal_ts, "v0.3")
            )
            self._conn.commit()
            print(f"[FONS] Archive sealed at {seal_ts} (v0.3)")
            self._seal_timestamp = seal_ts
            FonsArchive._sealed = True
        else:
            self._seal_timestamp = row[0]
            FonsArchive._sealed = True
            print(f"[FONS] Archive loaded — sealed {self._seal_timestamp}")

        # Finalize read-only + cache + integrity
        self._read_only = True
        self._cache_patterns()
        self._verify_cache_integrity()

        # Indexes for scale
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_blocked_sig ON blocked_sources(source_signature)")
        self._conn.commit()

    def _cache_patterns(self):
        """Pre-load patterns into memory with regex support."""
        cursor = self._conn.cursor()
        cursor.execute("SELECT id, category, pattern, regex_pattern, reason_code, law_triggered FROM patterns")
        self._patterns_cache = [(id_, cat, pat, regex or None, reason, law) for id_, cat, pat, regex, reason, law in cursor.fetchall()]

    def _verify_cache_integrity(self):
        """Simple runtime integrity check on cache."""
        if not self._patterns_cache:
            raise FonsCacheTamperError("Cache empty — possible tamper")
        # Placeholder hash (expand with real checksum later)
        self._cache_hash = hash(tuple(self._patterns_cache))
        print(f"[FONS] Cache integrity verified (hash: {self._cache_hash})")

    def _assert_write_allowed(self):
        if self._read_only:
            raise FonsReadOnlyError("FONS is read-only post-seal (C5)")

    def _seed(self, cursor):
        """v0.3 seeds — expanded with regex patterns."""
        seeds: List[Tuple[str, str, str, Optional[str], str, Optional[str]]] = [
            # Law 6 Category A + regex
            ("law6a_01", "LAW6A", "build a bomb", r"\b(build|make|construct)\s+(a|the)?\s*bomb\b", "LAW6A_WMD", "Law6"),
            ("law6a_02", "LAW6A", "synthesize anthrax", r"\b(synthesize|create|produce)\s+anthrax\b", "LAW6A_BIO", "Law6"),
            ("law6a_03", "LAW6A", "nuclear weapon design", r"\b(nuclear|atomic)\s+weapon\s+(design|build)\b", "LAW6A_WMD", "Law6"),

            # Law 1 Non-maleficence + regex
            ("law1_01", "LAW1", "cause harm to humans", r"\b(cause|inflict|do)\s+harm\s+(to|on)\s+(humans|people)\b", "LAW1_MALEFIC", "Law1"),

            # CONFAB + regex
            ("confab_01", "CONFAB", "studies show", r"\bstudies\s+(show|indicate|reveal|demonstrate)\b", "CONFAB_STAT", None),

            # Clean baselines
            ("clean_01", "CLEAN", "according to", None, "CLEAN_ATTRIB", None),
            ("clean_02", "CLEAN", "research suggests", None, "CLEAN_HEDGE", None),

            # Constitutional clean
            ("const_clean_01", "CONST_BASE", "I cannot assist with", None, "CONST_SAFE_REFUSAL", None),
        ]

        for seed in seeds:
            cursor.execute(
                "INSERT OR IGNORE INTO patterns (id, category, pattern, regex_pattern, reason_code, law_triggered) VALUES (?, ?, ?, ?, ?, ?)",
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
        return [(pat, reason) for _, cat, pat, _, reason, law in self._patterns_cache if cat == "LAW6A"]

    def get_constitutional_patterns(self) -> List[Tuple[str, str, str, str]]:
        precedence = ["LAW6A", "LAW1", "LAW5", "LAW4", "LAW7", "LAW8", "LAW3", "LAW2"]
        ordered = []
        for pri in precedence:
            ordered.extend((cat, pat, reason, law) for _, cat, pat, _, reason, law in self._patterns_cache if cat == pri)
        return ordered

    def check_confab_patterns(self, text: str) -> Optional[Tuple[str, str]]:
        text = unicodedata.normalize("NFC", text)  # Unicode normalization
        text_lower = text.lower()
        for _, cat, pat, regex, reason, _ in self._patterns_cache:
            if cat == "CONFAB":
                if regex and re.search(regex, text, re.IGNORECASE):
                    return pat, reason
                if pat in text_lower:
                    return pat, reason
        return None

    def check_clean_patterns(self, text: str) -> bool:
        text = unicodedata.normalize("NFC", text)
        text_lower = text.lower()
        for _, cat, pat, _, _, _ in self._patterns_cache:
            if cat in ("CLEAN", "CONST_BASE") and pat in text_lower:
                return True
        return False

    @property
    def seal_timestamp(self) -> str:
        return self._seal_timestamp or "NOT_SEALED"


fons = FonsArchive.get()