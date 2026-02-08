# Tier-1 Engine Reference

**Location:** `/engines/tier-1-foundation/constitutional-verification-engine-v1.0/`

---

## Import Paths

```python
# Core verifier
from constitutional_verification.core import ConstitutionalVerifier

# Primitives
from constitutional_verification.primitives import (
    constitutional_range_analysis,
    differentiable_verification,
    witness_search
)

# Sandbagging detection (implementation)
from constitutional_verification.sandbagging import (
    SandbaggingDetector,
    ContextInvariantProver,
    InterpretationSpaceAnalyzer
)

# Engine integrations
from constitutional_verification.integrations import (
    OracleLayerIntegration,
    BenchmarkEngineIntegration
)
Theory Documentation
Interval Logic: ../../../engines/tier-1-foundation/constitutional-verification-engine-v1.0/theory/interval_logic.md
Constitutional Bounds: ../../../engines/tier-1-foundation/constitutional-verification-engine-v1.0/theory/constitutional_bounds.md
Completeness Proofs: ../../../engines/tier-1-foundation/constitutional-verification-engine-v1.0/theory/completeness_proofs.md
When to Use This Reference
Scenario 1: Implementing Defense Protocols
# defense-protocols/sandbagging-defense-protocols.md implementation

from constitutional_verification import ConstitutionalVerifier
from constitutional_verification.sandbagging import SandbaggingDetector

# Initialize with defense configuration
verifier = ConstitutionalVerifier(defense_mode="paranoid")
detector = SandbaggingDetector(verifier)

# Apply protocol
result = detector.detect(task="capability_probe", context=ctx)
Scenario 2: Runtime Monitoring
# deployment-safeguards/runtime-monitoring-protocols.md

from constitutional_verification import ConstitutionalVerifier

verifier = ConstitutionalVerifier(monitoring_enabled=True)

# Configure alerts
verifier.configure_alerts(
    channels=["security-ops", "slack"],
    thresholds={"loophole_score": 0.7, "sandbagging_score": 0.8}
)

# Monitor production traffic
verifier.monitor_stream(production_requests)
Scenario 3: Pre-Deployment Audit
# deployment-safeguards/pre-deployment-checklist.md

from constitutional_verification import ConstitutionalVerifier
from constitutional_verification.primitives import witness_search

verifier = ConstitutionalVerifier(verification_mode="complete")

# Run exhaustive audit
audit_result = verifier.audit(
    model=production_model,
    constitution=constitution_spec,
    adversarial_prompts=red_team_prompts
)

if not audit_result.passed:
    print(f"Audit failed: {audit_result.violations}")
    print(f"Counterexamples: {audit_result.counterexamples}")
Integration with Security Systems
Sentinel Architecture
# sentinel-architecture-integration.md

from security_resilience.sentinels import SentinelOrchestrator
from constitutional_verification import ConstitutionalVerifier

# Integrate constitutional verification into sentinel system
sentinel = SentinelOrchestrator()
verifier = ConstitutionalVerifier()

sentinel.register_tier1_engine("constitutional_verification", verifier)
sentinel.enable_constitutional_layer()
Red Team Commander
# red-team-commander-integration.md

from security_resilience.red_team import RedTeamCommander
from constitutional_verification import ConstitutionalVerifier

red_team = RedTeamCommander()
verifier = ConstitutionalVerifier()

# Test constitutional bounds
red_team.test_constitutional_robustness(
    verifier=verifier,
    attack_scenarios=["loophole_exploitation", "sandbagging", "context_manipulation"]
)
File Structure Reference
engines/tier-1-foundation/constitutional-verification-engine-v1.0/
├── src/constitutional_verification/
│   ├── core.py                      # Main verifier class
│   ├── config.py                    # Configuration
│   ├── types.py                     # Type definitions
│   ├── primitives/
│   │   ├── range_analysis.py       # Import for bound checking
│   │   ├── differentiable_verification.py
│   │   └── witness_search.py       # Import for proof construction
│   ├── sandbagging/
│   │   ├── detector.py             # SandbaggingDetector class
│   │   ├── context_invariant_proofs.py
│   │   └── interpretation_space.py
│   ├── integrations/
│   │   ├── oracle_layer.py
│   │   └── benchmark_engine.py
│   └── tests/
│       ├── test_constitutional_verification.py
│       ├── test_primitives.py
│       └── test_sandbagging.py
└── theory/
    ├── interval_logic.md            # Mathematical foundations
    ├── constitutional_bounds.md
    └── completeness_proofs.md
Common Patterns
Pattern 1: Defense Protocol Implementation
# Standard pattern for implementing a new defense protocol

from constitutional_verification import ConstitutionalVerifier
from constitutional_verification.primitives import witness_search

class NewDefenseProtocol:
    def __init__(self):
        self.verifier = ConstitutionalVerifier()
    
    def defend(self, threat):
        # Use Tier-1 primitives
        bounds = self.verifier.check_bounds(threat.context)
        witness = witness_search(bounds, threat.constraint)
        
        if witness.found:
            return self.construct_defense(witness)
        else:
            return self.escalate_to_human()
Pattern 2: Threat Scenario Testing
# Standard pattern for testing threat scenarios

from constitutional_verification import ConstitutionalVerifier
from constitutional_verification.sandbagging import SandbaggingDetector

def test_threat_scenario(scenario):
    verifier = ConstitutionalVerifier()
    detector = SandbaggingDetector(verifier)
    
    # Run scenario
    result = detector.detect(
        task=scenario.task,
        context=scenario.context,
        expected_capability=scenario.baseline
    )
    
    # Log for case study
    if result.is_sandbagging:
        log_incident(scenario, result)
Version Compatibility
Tier-1 Engine Version
Compatible Security-Resilience Protocols
v1.0 (current)
All current defense protocols
v2.0 (planned)
Will add Polymath integrations
See Also:
Constitutional Verification Engine README
Security-Resilience Integration Guide
Defense Protocols Overview
