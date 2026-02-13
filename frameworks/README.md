graph TB
    subgraph Core[Core Meta-Frameworks - Universal]
        FSVE[FSVE<br/>Epistemic Validation]
        GENESIS[GENESIS<br/>Pattern Extraction]
        AION[AION<br/>Structural Integrity]
    end
    
    subgraph AI[AI Systems Applications]
        ABYSSAL[ABYSSAL<br/>Depth Measurement]
        TransAudit[Transformer Audit<br/>Future]
        HalDetect[Hallucination Detection<br/>Future]
    end
    
    subgraph Medical[Medical AI Applications]
        ClinVal[Clinical Validation<br/>Future]
        DiagConf[Diagnosis Confidence<br/>Future]
    end
    
    FSVE --> ABYSSAL
    GENESIS --> ABYSSAL
    AION --> ABYSSAL
    
    FSVE --> TransAudit
    FSVE --> HalDetect
    
    FSVE --> ClinVal
    GENESIS --> DiagConf
    
    style FSVE fill:#667eea
    style GENESIS fill:#f093fb
    style AION fill:#4facfe
    style ABYSSAL fill:#ff6b6b
