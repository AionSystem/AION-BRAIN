#!/usr/bin/env python3
"""
Personality Architect v2.0 - PDF Generator
Generates a professional PDF from the specification markdown
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import re
import os

AION_BLUE = HexColor('#1a365d')
AION_ACCENT = HexColor('#3182ce')
AION_LIGHT = HexColor('#e2e8f0')

def create_styles():
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=AION_BLUE,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=20,
        textColor=AION_ACCENT,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    ))
    
    styles.add(ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=12,
        textColor=AION_BLUE,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=AION_LIGHT,
        borderPadding=5
    ))
    
    styles.add(ParagraphStyle(
        'SubsectionHeader',
        parent=styles['Heading3'],
        fontSize=13,
        spaceBefore=15,
        spaceAfter=8,
        textColor=AION_ACCENT,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=14
    ))
    
    styles.add(ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        leftIndent=20,
        fontName='Helvetica',
        leading=12
    ))
    
    styles.add(ParagraphStyle(
        'CodeBlock',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Courier',
        leftIndent=20,
        spaceAfter=8,
        backColor=AION_LIGHT,
        leading=11
    ))
    
    styles.add(ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor('#718096'),
        alignment=TA_CENTER
    ))
    
    return styles

def parse_markdown_to_elements(md_content, styles):
    elements = []
    lines = md_content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            elements.append(Spacer(1, 6))
            i += 1
            continue
        
        if line.startswith('# '):
            title = line[2:].strip()
            if 'PERSONALITY ARCHITECT' in title.upper() or 'PERSONA' in title.upper():
                elements.append(Paragraph(title, styles['CustomTitle']))
            else:
                elements.append(Paragraph(title, styles['SectionHeader']))
        
        elif line.startswith('## '):
            section = line[3:].strip()
            elements.append(Paragraph(section, styles['SectionHeader']))
        
        elif line.startswith('### '):
            subsection = line[4:].strip()
            elements.append(Paragraph(subsection, styles['SubsectionHeader']))
        
        elif line.startswith('#### '):
            subsubsection = line[5:].strip()
            elements.append(Paragraph(f"<b>{subsubsection}</b>", styles['CustomBody']))
        
        elif line.startswith('- ') or line.startswith('* '):
            bullet_text = line[2:].strip()
            bullet_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', bullet_text)
            bullet_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', bullet_text)
            bullet_text = re.sub(r'`(.*?)`', r'<font face="Courier" size="9">\1</font>', bullet_text)
            elements.append(Paragraph(f"• {bullet_text}", styles['CustomBullet']))
        
        elif line.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if code_lines:
                code_text = '<br/>'.join([l.replace(' ', '&nbsp;') for l in code_lines[:15]])
                if len(code_lines) > 15:
                    code_text += '<br/>... [truncated]'
                elements.append(Paragraph(code_text, styles['CodeBlock']))
        
        elif line.startswith('>'):
            quote_text = line[1:].strip()
            quote_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', quote_text)
            elements.append(Paragraph(f"<i>{quote_text}</i>", styles['CustomBody']))
        
        elif line.startswith('---') or line.startswith('═'):
            elements.append(Spacer(1, 10))
        
        elif line.startswith('|'):
            pass
        
        else:
            text = line
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
            text = re.sub(r'`(.*?)`', r'<font face="Courier" size="9">\1</font>', text)
            elements.append(Paragraph(text, styles['CustomBody']))
        
        i += 1
    
    return elements

def generate_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    spec_path = os.path.join(script_dir, 'personality-architect-v1.0-spec.md')
    output_path = os.path.join(script_dir, 'personality-architect-v1.0.pdf')
    
    with open(spec_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    styles = create_styles()
    elements = []
    
    elements.append(Spacer(1, 1*inch))
    elements.append(Paragraph("AION COGNITIVE ENGINES", styles['CustomSubtitle']))
    elements.append(Paragraph("PERSONALITY ARCHITECT v2.0", styles['CustomTitle']))
    elements.append(Paragraph("Enterprise-Grade Persona Design Framework", styles['CustomSubtitle']))
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("Designing characters that adapt, remember, and stay true.", styles['CustomBody']))
    elements.append(Spacer(1, 0.3*inch))
    
    features = [
        "12-Section Comprehensive Framework",
        "Dynamic Identity Orchestrator (DIO) for Runtime Adaptation",
        "Continuity & Resonance Matrix (CRM) for Memory Management",
        "Multimodal Voice Assets & Telemetry Instrumentation",
        "20 Production-Ready Persona Cards",
        "5 Enterprise Templates"
    ]
    
    for feature in features:
        elements.append(Paragraph(f"• {feature}", styles['CustomBullet']))
    
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("Tier 2: Cognitive Architecture | Ethical Clearance: APPROVED", styles['Footer']))
    
    elements.append(PageBreak())
    
    spec_elements = parse_markdown_to_elements(md_content, styles)
    elements.extend(spec_elements)
    
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("═" * 60, styles['CustomBody']))
    elements.append(Paragraph("AION-BRAIN - Personality Architect v2.0", styles['Footer']))
    elements.append(Paragraph("Confidential - For authorized use only", styles['Footer']))
    
    doc.build(elements)
    print(f"PDF generated successfully: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_pdf()
