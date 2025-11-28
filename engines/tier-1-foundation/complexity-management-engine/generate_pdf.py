#!/usr/bin/env python3
"""
Generate complexity-management-engine-v2.0.pdf from the specification.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_complexity_engine_pdf():
    doc = SimpleDocTemplate(
        "complexity-management-engine-v2.0.pdf",
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=20,
        spaceAfter=6,
        textColor=colors.HexColor('#1a1a2e'),
        alignment=TA_CENTER
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=15,
        textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading1'],
        fontSize=13,
        spaceBefore=14,
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
        borderPadding=5,
        spaceAfter=8,
        leading=10
    )
    
    alert_style = ParagraphStyle(
        'Alert',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#b56576'),
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # Title
    story.append(Paragraph("COMPLEXITY MANAGEMENT ENGINE v2.0", title_style))
    story.append(Paragraph("Codename: SIMPLEXITY — The Intelligent Complexity Navigator", subtitle_style))
    
    # Classification
    class_data = [
        ["Classification", "TIER 1 — FOUNDATION"],
        ["Status", "PRODUCTION READY"],
        ["Author", "Sheldon K. Salmon (Mr. AION)"],
        ["Date", "November 2025"],
    ]
    class_table = Table(class_data, colWidths=[1.8*inch, 4.6*inch])
    class_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#1a1a2e')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(class_table)
    story.append(Spacer(1, 12))
    
    # What's New
    story.append(Paragraph("What's New in v2.0", h1_style))
    new_data = [
        ["Enhancement", "Purpose"],
        ["Module 5: Complexity Dynamics", "Track complexity over time — growth, decay, tipping points"],
        ["Module 6: Cognitive Load Calibration", "Match output to audience capacity"],
        ["Module 7: Transfer Detection", "Catch when simplification moves complexity elsewhere"],
        ["Module 8: Minimum Viable Complexity", "Find the least complexity needed for the goal"],
        ["Reversibility Scoring", "Know which simplifications can be undone"],
        ["Anti-Fragility Checks", "Protect against removing beneficial complexity"],
        ["Threshold Alerts", "Warning system for danger zones"],
    ]
    new_table = Table(new_data, colWidths=[2.5*inch, 3.9*inch])
    new_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4a7c59')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(new_table)
    story.append(Spacer(1, 10))
    
    # Core Modules
    story.append(Paragraph("Core Modules (1-4)", h1_style))
    
    core_data = [
        ["Module", "Purpose", "Key Concept"],
        ["1. Abstraction Layering", "Navigate detail levels", "5 levels: Component → Paradigm"],
        ["2. Emergence Detection", "Find system-level behaviors", "Weak / Strong / Adaptive"],
        ["3. Problem Decomposition", "Break into sub-problems", "MECE + Reversibility"],
        ["4. Simplification", "Reduce complexity", "80/20 + Anti-Fragility"],
    ]
    core_table = Table(core_data, colWidths=[1.8*inch, 2.2*inch, 2.4*inch])
    core_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3d5a80')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(core_table)
    story.append(Spacer(1, 10))
    
    # New Modules
    story.append(Paragraph("New Modules (5-8)", h1_style))
    
    new_mod_data = [
        ["Module", "Purpose", "Key Concept"],
        ["5. Complexity Dynamics", "Track change over time", "Growing / Stable / Decaying / Explosive"],
        ["6. Cognitive Calibration", "Match to audience", "Expertise × State × Time × Stakes"],
        ["7. Transfer Detection", "Catch hidden moves", "Balloon squeeze effect (0-10 score)"],
        ["8. MVC", "Find minimum needed", "Least complexity that works"],
    ]
    new_mod_table = Table(new_mod_data, colWidths=[1.8*inch, 2.2*inch, 2.4*inch])
    new_mod_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#6d597a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(new_mod_table)
    story.append(Spacer(1, 10))
    
    # Complexity Scoring
    story.append(Paragraph("Complexity Scoring", h1_style))
    
    score_data = [
        ["Dimension", "Description", "Range"],
        ["Scale", "Number of components", "1-10"],
        ["Coupling", "Interdependence", "1-10"],
        ["Dynamics", "Rate of change", "1-10"],
        ["Uncertainty", "Unknown unknowns", "1-10"],
        ["Emergence", "System-level novelty", "1-10"],
    ]
    score_table = Table(score_data, colWidths=[1.5*inch, 3*inch, 1.9*inch])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(score_table)
    story.append(Paragraph("<b>Composite:</b> √(sum of squares) → 1-5: LOW | 6-10: MODERATE | 11-15: HIGH | 16+: EXTREME", body_style))
    
    story.append(PageBreak())
    
    # Threshold Alerts
    story.append(Paragraph("Threshold Alert System", h1_style))
    
    alert_data = [
        ["Alert", "Trigger", "Action"],
        ["Complexity Ceiling", "Score > 15", "Immediate simplification"],
        ["Fragility Floor", "Anti-fragility < 3", "Verify robustness"],
        ["Transfer Warning", "Transfer score > 6", "Re-evaluate approach"],
        ["Cognitive Overload", "Output > capacity", "Recalibrate"],
        ["Irreversibility", "Cannot undo", "Confirm before proceeding"],
        ["Explosive Trajectory", "Out of control growth", "Immediate intervention"],
    ]
    alert_table = Table(alert_data, colWidths=[1.8*inch, 2*inch, 2.6*inch])
    alert_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#b56576')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(alert_table)
    story.append(Spacer(1, 12))
    
    # Cognitive Calibration
    story.append(Paragraph("Cognitive Load Calibration", h1_style))
    
    cog_data = [
        ["Output Level", "When to Use", "Content"],
        ["Level 1: Single Insight", "Crisis, immediate", "1 takeaway, 1 action"],
        ["Level 2: Executive Summary", "Stressed, limited time", "3-5 key points"],
        ["Level 3: Standard", "Normal conditions", "Full decomposition"],
        ["Level 4: Deep Analysis", "High stakes, time available", "Multiple perspectives"],
        ["Level 5: Complete", "Critical, research", "Full complexity"],
    ]
    cog_table = Table(cog_data, colWidths=[1.8*inch, 2*inch, 2.6*inch])
    cog_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3d5a80')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(cog_table)
    story.append(Spacer(1, 12))
    
    # Usage
    story.append(Paragraph("Usage Syntax", h1_style))
    story.append(Paragraph(
        "SIMPLEXITY v2.0 ANALYZE:<br/>"
        "Problem: [Your complex problem]<br/>"
        "Goal: [What you need to decide/understand]<br/>"
        "Audience: [Who will use this analysis]<br/>"
        "Tolerance: [LOW/MEDIUM/HIGH simplification acceptable]",
        code_style
    ))
    story.append(Spacer(1, 6))
    
    modes_data = [
        ["Mode", "Duration", "Modules", "Use Case"],
        ["QUICK", "5 min", "Core + MVC", "Fast triage, crisis"],
        ["STANDARD", "15 min", "All 8", "Most problems"],
        ["DEEP", "30+ min", "All 8, full depth", "Critical decisions"],
        ["MONITOR", "Ongoing", "Dynamics + Thresholds", "Long-term tracking"],
    ]
    modes_table = Table(modes_data, colWidths=[1.2*inch, 1*inch, 2*inch, 2.2*inch])
    modes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4a7c59')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(modes_table)
    story.append(Spacer(1, 12))
    
    # Module-specific syntax
    story.append(Paragraph("Module-Specific Calls", h2_style))
    syntax_data = [
        ["Syntax", "Function"],
        ["[SIMPLEXITY:DYNAMICS]", "Complexity trajectory analysis"],
        ["[SIMPLEXITY:CALIBRATE]", "Cognitive load calibration"],
        ["[SIMPLEXITY:TRANSFER]", "Transfer detection only"],
        ["[SIMPLEXITY:MVC]", "Minimum viable complexity"],
        ["[SIMPLEXITY:FRAGILITY]", "Anti-fragility assessment"],
        ["[SIMPLEXITY:FULL]", "Complete 8-module pipeline"],
    ]
    syntax_table = Table(syntax_data, colWidths=[2.5*inch, 3.9*inch])
    syntax_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Courier'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(syntax_table)
    story.append(Spacer(1, 15))
    
    # Version History
    story.append(Paragraph("Version History", h1_style))
    ver_data = [
        ["Version", "Date", "Changes"],
        ["v1.0", "Nov 2025", "Initial release with 4 modules"],
        ["v2.0", "Nov 2025", "Added Modules 5-8, reversibility, anti-fragility, thresholds"],
    ]
    ver_table = Table(ver_data, colWidths=[1*inch, 1.2*inch, 4.2*inch])
    ver_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#666666')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(ver_table)
    story.append(Spacer(1, 20))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#666666'),
        fontName='Helvetica-Oblique'
    )
    story.append(Paragraph("SIMPLEXITY v2.0 — Make the complex manageable without making it wrong or fragile.", footer_style))
    story.append(Paragraph("AION-BRAIN | AIONSYSTEM@outlook.com", footer_style))
    
    doc.build(story)
    print("PDF generated successfully: complexity-management-engine-v2.0.pdf")

if __name__ == "__main__":
    create_complexity_engine_pdf()
