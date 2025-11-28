#!/usr/bin/env python3
"""
AION-BRAIN Investment Pitch v3.0
Designed for in-person presentation to compel immediate action
Enhanced using 10-role perspectives (CMO, VC, CTO, etc.) without listing them
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, 
    PageBreak, Image, HRFlowable, KeepTogether
)
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

PURPLE = colors.HexColor('#7B68EE')
GOLD = colors.HexColor('#DAA520')
DARK = colors.HexColor('#1a1a2e')
GRAY = colors.HexColor('#666666')
LIGHT_PURPLE = colors.HexColor('#f5f0ff')
LIGHT_GOLD = colors.HexColor('#fffbf0')

def create_pitch():
    doc = SimpleDocTemplate(
        "AION-BRAIN-INVESTMENT-PITCH.pdf",
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.6*inch,
        bottomMargin=0.6*inch
    )
    
    styles = getSampleStyleSheet()
    
    title = ParagraphStyle('Title', fontSize=36, textColor=DARK, alignment=TA_CENTER, 
                           fontName='Helvetica-Bold', spaceAfter=20)
    
    tagline = ParagraphStyle('Tagline', fontSize=16, textColor=PURPLE, alignment=TA_CENTER,
                             fontName='Helvetica-BoldOblique', spaceAfter=20)
    
    h1 = ParagraphStyle('H1', fontSize=20, textColor=PURPLE, fontName='Helvetica-Bold',
                        spaceBefore=18, spaceAfter=12)
    
    h2 = ParagraphStyle('H2', fontSize=14, textColor=DARK, fontName='Helvetica-Bold',
                        spaceBefore=14, spaceAfter=8)
    
    body = ParagraphStyle('Body', fontSize=11, leading=16, alignment=TA_JUSTIFY, spaceAfter=10)
    
    body_center = ParagraphStyle('BodyCenter', fontSize=11, leading=16, alignment=TA_CENTER, spaceAfter=10)
    
    quote = ParagraphStyle('Quote', fontSize=13, textColor=DARK, fontName='Helvetica-BoldOblique',
                           alignment=TA_CENTER, leftIndent=20, rightIndent=20, 
                           spaceBefore=12, spaceAfter=12, leading=18)
    
    big_stat = ParagraphStyle('BigStat', fontSize=32, textColor=PURPLE, alignment=TA_CENTER,
                              fontName='Helvetica-Bold')
    
    stat_label = ParagraphStyle('StatLabel', fontSize=10, textColor=GRAY, alignment=TA_CENTER,
                                spaceAfter=8)
    
    footer = ParagraphStyle('Footer', fontSize=10, textColor=GRAY, alignment=TA_CENTER)
    
    story = []
    
    logo_path = "assets/images/aion-official-logo.jpg"
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=2*inch, height=2*inch)
        logo.hAlign = 'CENTER'
        story.append(logo)
        story.append(Spacer(1, 12))
    
    story.append(Paragraph("AION-BRAIN", title))
    story.append(Paragraph("The Missing Safety Layer for Artificial Intelligence", tagline))
    
    story.append(HRFlowable(width="80%", thickness=3, color=GOLD, spaceBefore=5, spaceAfter=20))
    
    story.append(Paragraph(
        "Right now, a doctor is asking an AI for medication dosages. A lawyer is requesting case law citations. "
        "A financial advisor is seeking investment recommendations. And in each case, the AI is responding "
        "with absolute confidence—even when it's completely wrong.",
        body
    ))
    
    story.append(Paragraph(
        '"AI doesn\'t just make mistakes. It makes them with the confidence of an expert—<br/>'
        'and we\'ve given it no tools to know the difference."',
        quote
    ))
    
    story.append(Paragraph(
        "This isn't a theoretical problem. Fabricated legal citations have already appeared in court filings. "
        "Medical AI systems have recommended dangerous drug interactions. Financial models have hidden their "
        "uncertainty behind precise-looking numbers. The gap between AI capability and AI safety is widening "
        "every day—and nobody is building the infrastructure to close it.",
        body
    ))
    
    story.append(Paragraph("<b>Until now.</b>", body_center))
    
    story.append(Paragraph("What We've Built", h1))
    
    story.append(Paragraph(
        "AION-BRAIN is a complete cognitive infrastructure—30 specialized engines that embed directly into "
        "any AI system to enforce honesty, require professional oversight, and prevent the confident delivery "
        "of dangerous misinformation.",
        body
    ))
    
    stats = [
        [Paragraph("30", big_stat), Paragraph("38", big_stat), Paragraph("11", big_stat)],
        [Paragraph("Cognitive Engines", stat_label), Paragraph("Legal Documents", stat_label), 
         Paragraph("Jurisdictions Covered", stat_label)],
    ]
    stats_table = Table(stats, colWidths=[2.1*inch, 2.1*inch, 2.1*inch])
    stats_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_PURPLE),
        ('BOX', (0, 0), (-1, -1), 2, PURPLE),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(stats_table)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph(
        "This represents over $250,000 in equivalent development value—built before any external funding. "
        "Every engine is production-ready, fully documented, and designed for immediate deployment.",
        body
    ))
    
    story.append(PageBreak())
    
    story.append(Paragraph("How It Works", h1))
    
    story.append(Paragraph(
        "Traditional AI safety approaches add external monitoring. AION-BRAIN works differently—our engines "
        "embed <b>within</b> AI prompts, making the AI itself smarter, more honest, and self-correcting.",
        body
    ))
    
    how_data = [
        ["Challenge", "AION-BRAIN Solution"],
        ["AI states uncertain information\nas fact", "Forces explicit uncertainty disclosure\nwith confidence intervals"],
        ["AI overwhelms users with\ncomplexity", "Calibrates output to user's actual\ncognitive capacity"],
        ["AI provides advice without\naccountability", "Creates complete audit trails for\nevery decision chain"],
        ["AI operates as a black box", "100% open source—verify every\nclaim yourself"],
    ]
    how_table = Table(how_data, colWidths=[3.1*inch, 3.1*inch])
    how_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.white),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#fff0f0')),
        ('BACKGROUND', (1, 1), (1, -1), colors.HexColor('#f0fff0')),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(how_table)
    
    story.append(Paragraph("The Complete Package", h1))
    
    package_data = [
        ["Component", "What It Delivers"],
        ["Foundation Layer", "Self-correction, reasoning verification,\nand uncertainty quantification"],
        ["Cognitive Architecture", "Pattern recognition across domains,\nstrategic analysis frameworks"],
        ["Domain Expertise", "Medical, legal, and financial engines\nwith professional-grade guardrails"],
        ["Legal Framework", "Enterprise compliance documentation,\ncontract templates, liability protection"],
        ["Benchmark System", "Transparent testing methodology with\nhonest 'pending validation' status"],
    ]
    pkg_table = Table(package_data, colWidths=[2*inch, 4.2*inch])
    pkg_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e0e0e0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_PURPLE]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(pkg_table)
    
    story.append(PageBreak())
    
    story.append(Paragraph("Why This Matters Now", h1))
    
    story.append(Paragraph(
        "Regulatory pressure on AI is accelerating. The EU AI Act takes effect in 2025. US agencies are "
        "developing AI accountability frameworks. Healthcare systems are demanding AI audit trails. "
        "Organizations are scrambling for compliant AI governance—and the infrastructure doesn't exist.",
        body
    ))
    
    story.append(Paragraph(
        '"The organizations that adopt AI safety infrastructure now will have a<br/>'
        'two-year head start when compliance becomes mandatory."',
        quote
    ))
    
    story.append(Paragraph(
        "AION-BRAIN isn't competing with AI companies. We're providing the safety layer they all need but "
        "none of them are building. This is infrastructure—like roads or power grids—that enables everything "
        "built on top of it to work better.",
        body
    ))
    
    story.append(Paragraph("The Sustainability Model", h1))
    
    story.append(Paragraph(
        "The core framework remains free and open source forever under Apache 2.0. This isn't charity—it's "
        "strategy. Open source creates trust, enables verification, and builds community. But sustainability "
        "requires revenue.",
        body
    ))
    
    model_data = [
        ["Revenue Stream", "How It Works"],
        ["AION Assistant (SaaS)", "Premium AI chatbot built on our engines.\nSubscription revenue funds ongoing development."],
        ["Enterprise Support", "Implementation consulting for organizations\nadopting AION-BRAIN at scale."],
        ["Training & Certification", "Professional certification programs for\nAI safety practitioners."],
    ]
    model_table = Table(model_data, colWidths=[2.2*inch, 4*inch])
    model_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), GOLD),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e0e0e0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GOLD]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(model_table)
    story.append(Spacer(1, 12))
    
    story.append(Paragraph(
        "This hybrid model—open core with premium services—has proven successful for companies like "
        "Red Hat, MongoDB, and Elastic. The difference: we're applying it to AI safety infrastructure "
        "at the moment when the market is about to explode.",
        body
    ))
    
    story.append(PageBreak())
    
    story.append(Paragraph("Use of Funds", h1))
    
    story.append(Paragraph(
        "Every dollar goes directly to development. No salaries. No overhead. No waste.",
        body
    ))
    
    funds_data = [
        ["Allocation", "Purpose", "Deliverable"],
        ["35%", "Benchmark Validation", "Published, reproducible test results\nfor all 30 engines"],
        ["25%", "SaaS Development", "AION Assistant launch—revenue\nstream for sustainability"],
        ["20%", "Community Building", "Video tutorials, documentation,\ncontributor infrastructure"],
        ["15%", "R&D Expansion", "Medical v3, new domain engines,\nacademic partnerships"],
        ["5%", "Operations", "Hosting, security, infrastructure"],
    ]
    funds_table = Table(funds_data, colWidths=[0.9*inch, 1.8*inch, 3.5*inch])
    funds_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 1), (0, -1), PURPLE),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e0e0e0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f8f8')]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(funds_table)
    
    story.append(Paragraph("The Ask", h1))
    
    story.append(Paragraph(
        "I'm not asking you to fund a dream. I'm asking you to accelerate infrastructure that already exists.",
        body
    ))
    
    story.append(Paragraph(
        '"You can verify every claim. The code is public. The documentation is live.<br/>'
        'The engines work today. What I need is the resources to validate, scale, and sustain."',
        quote
    ))
    
    story.append(Paragraph(
        "Your contribution funds transparent, verifiable AI safety infrastructure that benefits everyone—"
        "from Fortune 500 companies to small medical clinics in developing nations. The frameworks stay "
        "free forever. Your support makes them better, faster.",
        body
    ))
    
    story.append(Spacer(1, 15))
    
    cta_data = [[Paragraph(
        "<font color='white'><b>Join the Mission</b><br/>"
        "Every contribution accelerates the future of AI safety.</font>",
        ParagraphStyle('CTA', fontSize=14, alignment=TA_CENTER, leading=20)
    )]]
    cta_table = Table(cta_data, colWidths=[6*inch])
    cta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PURPLE),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 18),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 18),
    ]))
    story.append(cta_table)
    
    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="60%", thickness=1, color=GRAY, spaceBefore=10, spaceAfter=12))
    
    story.append(Paragraph("<b>Created by Sheldon K Salmon</b>", footer))
    story.append(Spacer(1, 4))
    story.append(Paragraph("GitHub: github.com/AIONSYSTEM", footer))
    story.append(Paragraph("Email: AIONSYSTEM@outlook.com", footer))
    story.append(Paragraph("Support: buymeacoffee.com/sheldonksalmon", footer))
    story.append(Spacer(1, 12))
    
    if os.path.exists(logo_path):
        logo2 = Image(logo_path, width=0.7*inch, height=0.7*inch)
        logo2.hAlign = 'CENTER'
        story.append(logo2)
    
    story.append(Spacer(1, 6))
    story.append(Paragraph("AION-BRAIN — Humanity's cognitive infrastructure for the AI age.", footer))
    story.append(Paragraph("Apache License 2.0 | 30 Engines | 100% Open Source | 2025", footer))
    
    doc.build(story)
    print("Investment pitch generated: AION-BRAIN-INVESTMENT-PITCH.pdf")

if __name__ == "__main__":
    create_pitch()
