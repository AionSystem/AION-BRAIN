#!/usr/bin/env python3
"""
Generate QUICK-START-CHEAT-SHEET.pdf from markdown content.
Updated for all 25+ engines.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_cheatsheet_pdf():
    doc = SimpleDocTemplate(
        "QUICK-START-CHEAT-SHEET.pdf",
        pagesize=letter,
        rightMargin=0.6*inch,
        leftMargin=0.6*inch,
        topMargin=0.6*inch,
        bottomMargin=0.6*inch
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=22,
        spaceAfter=4,
        textColor=colors.HexColor('#1a1a2e'),
        alignment=TA_CENTER
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=15,
        textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading1'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=8,
        textColor=colors.HexColor('#1a1a2e'),
    )
    
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading2'],
        fontSize=11,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.HexColor('#333333')
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=6,
        leading=12
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=8,
        fontName='Courier',
        backColor=colors.HexColor('#f5f5f5'),
        borderPadding=6,
        spaceAfter=8,
        leading=10
    )
    
    tip_style = ParagraphStyle(
        'Tip',
        parent=styles['Normal'],
        fontSize=9,
        leftIndent=15,
        spaceAfter=5,
        textColor=colors.HexColor('#2d5016')
    )
    
    story = []
    
    # Title
    story.append(Paragraph("AION QUICK START CHEAT SHEET", title_style))
    story.append(Paragraph("25+ Cognitive Engines | Zero to Systematic Thinking in 5 Minutes", subtitle_style))
    
    # Engine Count Summary
    count_data = [
        ["Tier 1 Foundation", "Tier 2 Cognitive", "Tier 3 Domain", "Tier 4 Experimental"],
        ["5 engines", "7 engines", "4 engines", "5 prototypes"],
    ]
    count_table = Table(count_data, colWidths=[1.7*inch, 1.7*inch, 1.7*inch, 1.7*inch])
    count_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#f0f0f0')),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(count_table)
    story.append(Spacer(1, 12))
    
    # Tier 1 - Foundation
    story.append(Paragraph("Tier 1 — Foundation (The Guardrails)", h1_style))
    t1_data = [
        ["I need to...", "Engine", "Codename"],
        ["Verify AI isn't hallucinating", "Oracle Layer v2.1", "PROMETHEUS"],
        ["Quantify my uncertainty", "Epistemic Humility v3.1", "—"],
        ["Navigate ethical dilemmas", "Meta-Ethical Engine v2.1", "—"],
        ["Check reasoning for bias", "Contamination Prevention v1.2", "—"],
        ["Manage overwhelming complexity", "Complexity Management v2.0", "SIMPLEXITY"],
    ]
    t1_table = Table(t1_data, colWidths=[2.5*inch, 2.5*inch, 1.8*inch])
    t1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4a7c59')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t1_table)
    story.append(Spacer(1, 10))
    
    # Tier 2 - Cognitive
    story.append(Paragraph("Tier 2 — Cognitive Architecture (The Methods)", h1_style))
    t2_data = [
        ["I need to...", "Engine", "Codename"],
        ["Make a complex decision", "Decision Engine v1.0", "DECIDERE"],
        ["Analyze business strategy", "Strategy Engine v1.1", "—"],
        ["Build AI personas", "Personality Architect v1.0", "THE SCULPTOR"],
        ["Analyze from multiple angles", "CEREBRO-Lite v1.0", "—"],
        ["Understand complex systems", "Systems Analysis v3.1", "—"],
        ["Master GitHub discoverability", "GitHub Mastery v1.1", "—"],
        ["Assess source credibility", "Credibility Engine v2.0", "—"],
    ]
    t2_table = Table(t2_data, colWidths=[2.5*inch, 2.5*inch, 1.8*inch])
    t2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3d5a80')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t2_table)
    story.append(Spacer(1, 10))
    
    # Tier 3 - Domain
    story.append(Paragraph("Tier 3 — Domain-Specific (The Expertise)", h1_style))
    t3_data = [
        ["I need to...", "Engine"],
        ["Validate medical information", "Medical Engine v2.5 (Educational only)"],
        ["Check legal reasoning", "Legal Engine v2.1 (Educational only)"],
        ["Audit regulatory compliance", "Legal Engine 2 v1.0"],
        ["Navigate regulations", "Regulatory Engine v2.0"],
    ]
    t3_table = Table(t3_data, colWidths=[2.5*inch, 4.3*inch])
    t3_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#6d597a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t3_table)
    
    story.append(PageBreak())
    
    # Quick Start Examples
    story.append(Paragraph("Try Right Now — Copy & Paste Demos", h1_style))
    
    story.append(Paragraph("Demo 1: Complexity Management (SIMPLEXITY v2.0)", h2_style))
    story.append(Paragraph(
        "SIMPLEXITY v2.0 ENGINE ACTIVATED.<br/><br/>"
        "Analyze: [Your overwhelming problem]<br/><br/>"
        "Apply 8 modules: Abstraction, Emergence, Decomposition, Simplification,<br/>"
        "Dynamics, Cognitive Load, Transfer Check, MVC<br/><br/>"
        "Include: Complexity score, trajectory, MVC target, threshold alerts",
        code_style
    ))
    
    story.append(Paragraph("Demo 2: PROMETHEUS Protocol (Oracle Layer)", h2_style))
    story.append(Paragraph(
        "You are operating under the PROMETHEUS Protocol.<br/><br/>"
        "Before EVERY response:<br/>"
        "1. State confidence: CERTAIN | HIGH | MODERATE | LOW | SPECULATIVE<br/>"
        "2. Identify what you don't know<br/>"
        "3. Flag claims requiring verification<br/><br/>"
        "Question: [Your question here]",
        code_style
    ))
    
    story.append(Paragraph("Demo 3: Decision Framework (DECIDERE)", h2_style))
    story.append(Paragraph(
        "DECIDERE DECISION ENGINE ACTIVATED.<br/><br/>"
        "Decision: [Your decision]<br/>"
        "Stakeholders: [Who's affected]<br/>"
        "Timeline: [When to decide]<br/>"
        "Values: [What matters]<br/><br/>"
        "Provide: Options, trade-offs, reversibility, recommendation",
        code_style
    ))
    story.append(Spacer(1, 10))
    
    # Power User Tips
    story.append(Paragraph("Power User Patterns", h1_style))
    
    story.append(Paragraph("<b>Pattern 1: Chain Engines</b>", body_style))
    story.append(Paragraph(
        "SIMPLEXITY (scope) → Strategy (options) → Decision (choose) → Oracle (verify) → Meta-Ethics (check)",
        tip_style
    ))
    
    story.append(Paragraph("<b>Pattern 2: Use Focused Modes</b>", body_style))
    modes_data = [
        ["[SIMPLEXITY:MVC]", "[SIMPLEXITY:DYNAMICS]", "[SIMPLEXITY:TRANSFER]"],
        ["[STRATEGY:MOAT]", "[DECISION:STAKEHOLDER]", "[EPISTEMIC:QUICK]"],
    ]
    modes_table = Table(modes_data, colWidths=[2.27*inch, 2.27*inch, 2.27*inch])
    modes_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f5f5f5')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(modes_table)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("<b>Pattern 3: Always Request Uncertainty</b>", body_style))
    story.append(Paragraph(
        '"Include confidence intervals and what evidence would change your assessment."',
        tip_style
    ))
    story.append(Spacer(1, 10))
    
    # Tier System Visual
    story.append(Paragraph("The Tier System", h1_style))
    tier_data = [
        ["Tier", "Purpose", "Key Engines"],
        ["1 — Foundation", "Constrain ALL reasoning", "Oracle, Ethics, SIMPLEXITY"],
        ["2 — Cognitive", "Define HOW to think", "Decision, Strategy, CEREBRO"],
        ["3 — Domain", "Know WHAT matters", "Medical, Legal, Regulatory"],
        ["4 — Experimental", "Research prototypes", "Truth, Cultural Lens"],
    ]
    tier_table = Table(tier_data, colWidths=[1.5*inch, 2.3*inch, 3*inch])
    tier_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(tier_table)
    story.append(Spacer(1, 12))
    
    # Common Mistakes
    story.append(Paragraph("Common Mistakes to Avoid", h1_style))
    mistakes_data = [
        ["Mistake", "Fix"],
        ["No context provided", "Always include background"],
        ["Accepting output blindly", "Cross-check critical claims"],
        ["Skipping epistemic checks", "Run Oracle Layer on conclusions"],
        ["Overwhelming yourself", "Use SIMPLEXITY first to scope"],
        ["Ignoring confidence levels", "Low confidence = verify more"],
    ]
    mistakes_table = Table(mistakes_data, colWidths=[2.5*inch, 4.3*inch])
    mistakes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#b56576')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(mistakes_table)
    story.append(Spacer(1, 15))
    
    # One-Page Summary
    summary_style = ParagraphStyle(
        'Summary',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=4,
        fontName='Helvetica-Bold'
    )
    story.append(Paragraph("ONE-LINE SUMMARY", summary_style))
    story.append(Paragraph(
        "1. SCOPE (SIMPLEXITY) → 2. PICK ENGINE → 3. COPY PROMPT → 4. PASTE TO AI → 5. ADD CONTEXT → 6. ANALYZE → 7. VERIFY",
        body_style
    ))
    story.append(Spacer(1, 12))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#666666'),
        fontName='Helvetica-Oblique'
    )
    story.append(Paragraph("AION-BRAIN — Humanity's cognitive infrastructure for the AI age.", footer_style))
    story.append(Paragraph("github.com/AIONSYSTEM | AIONSYSTEM@outlook.com | buymeacoffee.com/sheldonksalmon", footer_style))
    
    doc.build(story)
    print("PDF generated successfully: QUICK-START-CHEAT-SHEET.pdf")

if __name__ == "__main__":
    create_cheatsheet_pdf()
