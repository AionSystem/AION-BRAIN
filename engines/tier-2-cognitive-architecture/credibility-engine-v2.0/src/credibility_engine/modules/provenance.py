"""
CREDIBILITY ENGINE v2.0 - Module 7: Evidence Provenance
=========================================================

Immutable evidence storage and verification.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import hashlib
import uuid


@dataclass
class ProvenanceRecord:
    """Immutable record of evidence provenance."""
    record_id: str
    asset_id: str
    timestamp: datetime
    source_url: str
    content_hash: str
    verifier: str
    verification_method: str
    chain_hash: str = ""
    metadata: Dict = field(default_factory=dict)


@dataclass
class VerificationResult:
    """Result of provenance verification."""
    is_valid: bool
    hash_matches: bool
    chain_intact: bool
    issues: List[str]


class ProvenanceSystem:
    """
    Module 7: Evidence Provenance System
    
    Provides:
    - Immutable evidence logging
    - Cryptographic hash verification
    - Chain of custody tracking
    """
    
    def __init__(self):
        """Initialize provenance system."""
        self._records: Dict[str, ProvenanceRecord] = {}
        self._chain: List[str] = []
    
    @staticmethod
    def compute_hash(content: str) -> str:
        """Compute SHA-256 hash of content."""
        return hashlib.sha256(content.encode()).hexdigest()
    
    @staticmethod
    def compute_chain_hash(previous_hash: str, current_hash: str) -> str:
        """Compute chain hash linking to previous record."""
        combined = f"{previous_hash}:{current_hash}"
        return hashlib.sha256(combined.encode()).hexdigest()
    
    def add_record(
        self,
        asset_id: str,
        source_url: str,
        content: str,
        verifier: str,
        verification_method: str,
        metadata: Optional[Dict] = None
    ) -> ProvenanceRecord:
        """Add new provenance record."""
        record_id = str(uuid.uuid4())
        content_hash = self.compute_hash(content)
        
        previous_hash = self._chain[-1] if self._chain else "GENESIS"
        chain_hash = self.compute_chain_hash(previous_hash, content_hash)
        
        record = ProvenanceRecord(
            record_id=record_id,
            asset_id=asset_id,
            timestamp=datetime.now(),
            source_url=source_url,
            content_hash=content_hash,
            verifier=verifier,
            verification_method=verification_method,
            chain_hash=chain_hash,
            metadata=metadata or {}
        )
        
        self._records[record_id] = record
        self._chain.append(chain_hash)
        
        return record
    
    def verify_record(self, record: ProvenanceRecord, content: str) -> VerificationResult:
        """Verify a provenance record."""
        issues = []
        
        computed_hash = self.compute_hash(content)
        hash_matches = computed_hash == record.content_hash
        
        if not hash_matches:
            issues.append("Content hash does not match stored hash")
        
        chain_intact = record.chain_hash in self._chain
        if not chain_intact:
            issues.append("Record not found in provenance chain")
        
        is_valid = hash_matches and chain_intact
        
        return VerificationResult(
            is_valid=is_valid,
            hash_matches=hash_matches,
            chain_intact=chain_intact,
            issues=issues
        )
    
    def get_record(self, record_id: str) -> Optional[ProvenanceRecord]:
        """Get a provenance record by ID."""
        return self._records.get(record_id)
    
    def get_records_for_asset(self, asset_id: str) -> List[ProvenanceRecord]:
        """Get all provenance records for an asset."""
        return [r for r in self._records.values() if r.asset_id == asset_id]
    
    def get_chain_length(self) -> int:
        """Get length of provenance chain."""
        return len(self._chain)
    
    def verify_chain_integrity(self) -> bool:
        """Verify entire chain integrity."""
        if not self._chain:
            return True
        
        records = sorted(self._records.values(), key=lambda r: r.timestamp)
        
        previous_hash = "GENESIS"
        for record in records:
            expected_chain = self.compute_chain_hash(previous_hash, record.content_hash)
            if expected_chain != record.chain_hash:
                return False
            previous_hash = record.chain_hash
        
        return True
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for provenance system."""
        return """
MODULE 7: EVIDENCE PROVENANCE SYSTEM
├─ Immutable Evidence Store
│   ├─ Cryptographic hash + timestamp + source URL
│   └─ Chain of custody linking
├─ Verification Fields:
│   ├─ Asset type (demo | testimonial | case_study | endorsement)
│   ├─ Verifier identity
│   ├─ Verification method
│   └─ Expiration conditions
└─ Chain Integrity:
    └─ Each record links to previous via hash chain
"""
