name: "🚀 Feature Request"
description: "Propose a new cognitive engine, framework, or systematic thinking enhancement"
title: "[Feature]: "
labels: ["enhancement", "needs-triage"]
body:
  - type: markdown
    attributes:
      value: |
        # Systematic Feature Proposal
        
        **Before submitting:** Have you taken the Paradox Strategic Assessment? High scorers receive prioritized review.
        
        This template helps us evaluate proposals systematically. Thoughtful completion demonstrates the systematic thinking we value.

  - type: checkboxes
    id: prereqs
    attributes:
      label: "Prerequisites"
      description: "Please confirm these before proceeding"
      options:
        - label: "I've read the ARCHITECT.md to understand project philosophy"
          required: true
        - label: "I've tried existing engines to understand the architecture"
          required: true
        - label: "This feature aligns with AION's non-negotiables (epistemic humility, contamination prevention, ethical design, accessibility)"
          required: true
        - label: "I understand AION-BRAIN is research software, not production code"
          required: true

  - type: textarea
    id: problem
    attributes:
      label: "Systematic Problem Statement"
      description: "What cognitive gap or systematic failure does this address?"
      placeholder: |
        Example: Current AI systems fail to [specific cognitive failure] when [context], leading to [negative outcome]. This matters because [systemic impact].
    validations:
      required: true

  - type: textarea
    id: hypothesis
    attributes:
      label: "Testable Hypothesis"
      description: "What falsifiable claim does this feature test?"
      placeholder: |
        Example: By implementing [mechanism], we hypothesize that [metric] will improve by [amount] in [context], falsifiable by [test].
    validations:
      required: true

  - type: textarea
    id: second_order
    attributes:
      label: "Second-Order Effects Analysis"
      description: "What are the potential unintended consequences or ripple effects?"
      placeholder: |
        - Primary effect: [direct outcome]
        - Second-order: [indirect consequence] 
        - Third-order: [systemic impact]
        - Potential failure modes: [how this could make things worse]
    validations:
      required: true

  - type: dropdown
    id: category
    attributes:
      label: "Feature Category"
      description: "Which tier of the cognitive architecture does this belong to?"
      options:
        - "Tier 1: Foundation (Constraint Systems)"
        - "Tier 2: Cognitive (Methodology Systems)"
        - "Tier 3: Domain-Specific (Expertise Systems)"
        - "Tier 4: Experimental (Research Systems)"
        - "Cross-Tier Integration"
        - "Tooling/Infrastructure"
    validations:
      required: true

  - type: textarea
    id: implementation
    attributes:
      label: "Implementation Sketch"
      description: "Brief outline of how this might work (no technical details required)"
      placeholder: |
        Core mechanism: [basic approach]
        Inputs: [what the engine/system would take]
        Processing: [key transformations or analyses]
        Outputs: [what users would receive]
        Ethical safeguards: [how misuse would be prevented]
    validations:
      required: true

  - type: textarea
    id: validation
    attributes:
      label: "Validation Protocol"
      description: "How would we test if this feature works as intended?"
      placeholder: |
        Test scenarios: [specific situations to test]
        Success criteria: [measurable outcomes]
        Failure conditions: [what would indicate the hypothesis is wrong]
        Baseline comparison: [how performance compares to current approaches]
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: "Alternative Approaches Considered"
      description: "What other ways could this problem be solved? Why is your approach optimal?"
      placeholder: |
        Alternative 1: [description] - Rejected because [reason]
        Alternative 2: [description] - Less optimal because [reason]
        Why this approach: [advantages over alternatives]
    validations:
      required: true

  - type: textarea
    id: resources
    attributes:
      label: "Resources & Constraints"
      description: "What would implementing this require?"
      placeholder: |
        Research needed: [knowledge gaps to fill]
        Data requirements: [what training/validation data]
        Computational costs: [API, processing needs]
        Expertise required: [domain knowledge, technical skills]
        Time estimate: [realistic implementation timeline]
    validations:
      required: true

  - type: textarea
    id: contribution
    attributes:
      label: "Contribution Pathway"
      description: "How could you contribute to developing this feature?"
      placeholder: |
        I can contribute: [specific skills or resources]
        I need help with: [areas where I lack expertise]
        Proposed timeline: [when/how development could happen]
        Collaboration preferences: [how you'd like to work together]
    validations:
      required: false

  - type: textarea
    id: context
    attributes:
      label: "Additional Context"
      description: "Anything else we should know?"
      placeholder: |
        Personal motivation: [why this matters to you]
        Related work: [similar systems or research]
        Potential collaborators: [people/organizations who might help]
        Questions for the community: [what you'd like feedback on]
    validations:
      required: false

  - type: markdown
    attributes:
      value: |
        ## Review Process
        
        **Stage 1:** Triage (1-2 weeks)
        - Check alignment with AION philosophy
        - Initial feasibility assessment
        
        **Stage 2:** Community Discussion (2-4 weeks)
        - GitHub Discussions thread
        - Refinement based on feedback
        
        **Stage 3:** Research Design (if approved)
        - Detailed specification
        - Validation protocol design
        - Resource planning
        
        **Note:** Most feature requests will NOT be implemented. We prioritize:
        1. Features advancing systematic thinking research
        2. Well-specified, testable hypotheses
        3. Proposals from PSA high scorers
        4. Community-supported ideas with validation plans
        
        Thank you for thinking systematically with us.
