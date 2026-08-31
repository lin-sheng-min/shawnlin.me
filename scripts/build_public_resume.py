from pathlib import Path
from shutil import copyfile

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Shawn_Lin_Public_Resume.pdf"
PUBLIC_COPY = ROOT / "public" / "Shawn_Lin_Public_Resume.pdf"

INK = colors.HexColor("#171716")
MUTED = colors.HexColor("#66635E")
LINE = colors.HexColor("#CFC9BF")
ACCENT = colors.HexColor("#65705A")

styles = getSampleStyleSheet()
name_style = ParagraphStyle(
    "Name",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=27,
    leading=29,
    textColor=INK,
    spaceAfter=2,
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.2,
    leading=11,
    textColor=ACCENT,
    spaceAfter=4,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.8,
    leading=10,
    textColor=MUTED,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=7.6,
    leading=9,
    tracking=1.3,
    textColor=ACCENT,
    spaceBefore=7,
    spaceAfter=3,
)
company_style = ParagraphStyle(
    "Company",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=9.2,
    leading=11,
    textColor=INK,
)
meta_style = ParagraphStyle(
    "Meta",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.6,
    leading=9.2,
    textColor=MUTED,
)
meta_right_style = ParagraphStyle(
    "MetaRight",
    parent=meta_style,
    alignment=TA_RIGHT,
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.1,
    leading=10.3,
    textColor=INK,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=10,
    firstLineIndent=-7,
    bulletIndent=0,
    spaceAfter=1.4,
)
small_style = ParagraphStyle(
    "Small",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.6,
    leading=9.7,
    textColor=INK,
)


def section(title):
    return [
        Paragraph(title.upper(), section_style),
        HRFlowable(width="100%", thickness=0.55, color=LINE, spaceAfter=4),
    ]


def experience(company, location, role, period, bullets):
    heading = Table(
        [
            [Paragraph(company, company_style), Paragraph(location, meta_right_style)],
            [Paragraph(role, meta_style), Paragraph(period, meta_right_style)],
        ],
        colWidths=[4.45 * inch, 2.15 * inch],
        hAlign="LEFT",
    )
    heading.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    block = [heading, Spacer(1, 2)]
    block.extend(Paragraph(text, bullet_style, bulletText="•") for text in bullets)
    block.append(Spacer(1, 3))
    return KeepTogether(block)


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC_COPY.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        rightMargin=0.62 * inch,
        leftMargin=0.62 * inch,
        topMargin=0.46 * inch,
        bottomMargin=0.42 * inch,
        title="Shawn Lin Public Resume",
        author="Shawn Lin",
        subject="Technical Program Manager",
    )

    story = [
        Paragraph("Shawn Lin", name_style),
        Paragraph("Technical Program Manager", role_style),
        Paragraph(
            'San Francisco, CA &nbsp;&nbsp;|&nbsp;&nbsp; '
            '<a href="mailto:smlin.shawn@gmail.com" color="#66635E">smlin.shawn@gmail.com</a>'
            ' &nbsp;&nbsp;|&nbsp;&nbsp; '
            '<a href="https://www.linkedin.com/in/shawnlin/" color="#66635E">linkedin.com/in/shawnlin</a>',
            contact_style,
        ),
        Spacer(1, 7),
    ]

    story += section("Profile")
    story += [
        Paragraph(
            "Technical Program Manager with a software engineering foundation and experience connecting engineering, security, infrastructure, data, and business teams. I turn ambiguous technical work into clear plans, shared ownership, and dependable delivery.",
            body_style,
        )
    ]

    story += section("Experience")
    story += [
        experience(
            "Sigma Computing",
            "San Francisco, CA",
            "Technical Program Manager",
            "September 2025 to Present",
            [
                "Lead cross functional roadmaps and program delivery across engineering, security, and infrastructure teams.",
                "Improved incident response by redesigning triage, escalation, and post incident learning workflows with engineering partners.",
                "Built AI assisted automations that reduce repetitive coordination and help teams close work more efficiently.",
                "Guide planning for tooling, cloud infrastructure, and enterprise delivery with a focus on risk, cost, and engineering velocity.",
            ],
        ),
        experience(
            "Amazon",
            "Hybrid",
            "Technical Program Manager Intern",
            "June 2024 to September 2024",
            [
                "Turned more than 20 hours of manual data preparation into a roughly three minute setup with about five clicks.",
                "Made complex budget and project data easy to read for more than 50 users, supporting resource allocation and leadership decisions.",
                "Designed a repeatable workflow that transformed fragmented source files into a consistent view with minimal manual effort.",
                "Made quarterly planning easier by bringing spending progress, actual costs, and project status into one place.",
            ],
        ),
        experience(
            "Hour Loop",
            "Taipei, Taiwan",
            "Software Engineer",
            "May 2022 to January 2024",
            [
                "Built and scaled event driven order processing across AWS and GCP while improving reliability and observability.",
                "Developed data pipelines that turned advertising and clickstream data into actionable insights.",
                "Improved continuous delivery, test coverage, and engineering workflows across teams.",
                "Recognized as company wide Top Performer of the Year for cross team impact and technical leadership.",
            ],
        ),
    ]

    story += section("Earlier experience")
    earlier_experience = Table(
        [
            [Paragraph("<b>Industrial Technology Research Institute</b><br/>Software Engineer Intern", small_style), Paragraph("July 2019 to August 2019", meta_right_style)],
            [Paragraph("<b>Hokicat Digital Marketing</b><br/>Content Strategist", small_style), Paragraph("July 2018 to May 2019", meta_right_style)],
        ],
        colWidths=[4.65 * inch, 1.95 * inch],
        hAlign="LEFT",
    )
    earlier_experience.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(earlier_experience)

    story += section("Education")
    education = Table(
        [
            [Paragraph("<b>University of Illinois Urbana-Champaign</b><br/>Master of Computer Science", small_style), Paragraph("2025", meta_right_style)],
            [Paragraph("<b>National Tsing Hua University</b><br/>B.B.A. in Management and Technology<br/>Program of Computer Science and Quantitative Finance", small_style), Paragraph("2021", meta_right_style)],
        ],
        colWidths=[5.7 * inch, 0.9 * inch],
        hAlign="LEFT",
    )
    education.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(education)

    story += section("Selected tools")
    story.append(
        Paragraph(
            "Program delivery, incident management, cloud infrastructure, AI automation, Jira, Confluence, incident.io, n8n, Python, SQL, TypeScript, AWS, GCP, Azure, Terraform, Kubernetes, Databricks, Snowflake",
            small_style,
        )
    )

    doc.build(story)
    copyfile(OUTPUT, PUBLIC_COPY)


if __name__ == "__main__":
    build()
