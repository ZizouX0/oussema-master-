#!/usr/bin/env python3
"""Convert every markdown deliverable to PDF.

Markdown -> styled HTML -> Chromium print-to-PDF. Chromium rather than a LaTeX
pipeline because these documents are mostly wide tables, and Chromium is the only
renderer here that reflows them sensibly and keeps hyperlinks clickable.
"""
import os, re, sys
import markdown
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "output")
PDF_DIR = os.path.join(OUT, "pdf")
os.makedirs(PDF_DIR, exist_ok=True)

DOCS = [
    (os.path.join(OUT, "shortlist.md"), "Shortlist — 15 Track A, 15 Track B"),
    (os.path.join(OUT, "gaps_and_risks.md"), "Gaps and risks"),
    (os.path.join(OUT, "funding_map.md"), "Funding map"),
    (os.path.join(OUT, "deadline_calendar.md"), "Deadline calendar"),
    (os.path.join(OUT, "verification_report.md"), "Verification report (V1, adversarial)"),
    (os.path.join(OUT, "coverage_audit.md"), "Coverage audit (V2, adversarial)"),
    (os.path.join(ROOT, "data", "transcript_audit.md"),
     "Transcript audit — entry requirements, subject credits and blockers"),
    (os.path.join(ROOT, "data", "followups.md"), "Follow-up queue"),
    (os.path.join(ROOT, "data", "BRIEF.md"), "Research brief (what every agent was told)"),
    (os.path.join(ROOT, "data", "institutions.md"), "Institutions surfaced"),
]

CSS = """
@page { size: A4 landscape; margin: 14mm 12mm 16mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 8.6pt; line-height: 1.5;
       color: #1f2933; margin: 0; }
h1 { font-size: 19pt; margin: 0 0 2mm; color: #10151c; letter-spacing: -0.2pt; }
h2 { font-size: 13pt; margin: 7mm 0 2mm; padding-bottom: 1.4mm;
     border-bottom: 1.6pt solid #1f2933; color: #10151c; page-break-after: avoid; }
h3 { font-size: 10.5pt; margin: 5mm 0 1.5mm; color: #24313d; page-break-after: avoid; }
h4 { font-size: 9.4pt; margin: 4mm 0 1mm; color: #3a4855; page-break-after: avoid; }
p { margin: 0 0 2.2mm; }
table { border-collapse: collapse; width: 100%; margin: 2.5mm 0 4mm;
        font-size: 7.6pt; page-break-inside: auto; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th { background: #1f2933; color: #fff; text-align: left; padding: 1.7mm 2mm;
     font-weight: 600; border: 0.4pt solid #1f2933; }
td { padding: 1.5mm 2mm; border: 0.4pt solid #d3d9df; vertical-align: top; }
tbody tr:nth-child(even) { background: #f5f7f9; }
code { background: #eef1f4; padding: 0.3mm 1mm; border-radius: 1.5pt;
       font-family: "DejaVu Sans Mono", monospace; font-size: 7.4pt; }
a { color: #1b6ac9; text-decoration: none; word-break: break-all; }
strong { color: #10151c; }
ul, ol { margin: 0 0 2.5mm; padding-left: 5mm; }
li { margin-bottom: 1mm; }
blockquote { border-left: 2.5pt solid #c8d0d8; margin: 2mm 0; padding: 0 0 0 3mm; color: #4a5866; }
hr { border: 0; border-top: 0.6pt solid #d3d9df; margin: 5mm 0; }
.doc-head { border-bottom: 2.4pt solid #1f2933; padding-bottom: 2.5mm; margin-bottom: 5mm; }
.doc-sub { color: #5a6874; font-size: 8pt; margin-top: 1mm; }
"""

SUB = ("European Master's &amp; Scholarship Research · Tunisian applicant, 180-ECTS Licence "
       "in Business Intelligence · compiled 2026-08-16 · 181 programmes, 103 funding schemes")

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for src, title in DOCS:
        if not os.path.exists(src):
            print(f"  skip (missing): {src}")
            continue
        text = open(src, encoding="utf-8").read()
        # The first heading becomes the styled document header instead of body text.
        text = re.sub(r"\A#\s+.*\n", "", text, count=1)
        md.reset()
        body = md.convert(text)
        html = (f"<!doctype html><html><head><meta charset='utf-8'>"
                f"<title>{title}</title><style>{CSS}</style></head><body>"
                f"<div class='doc-head'><h1>{title}</h1>"
                f"<div class='doc-sub'>{SUB}</div></div>{body}</body></html>")
        tmp = os.path.join(PDF_DIR, ".render.html")
        open(tmp, "w", encoding="utf-8").write(html)
        page.goto("file://" + tmp)
        page.wait_for_load_state("networkidle")
        name = os.path.splitext(os.path.basename(src))[0] + ".pdf"
        dest = os.path.join(PDF_DIR, name)
        page.pdf(path=dest, format="A4", landscape=True, print_background=True,
                 margin={"top": "14mm", "bottom": "16mm", "left": "12mm", "right": "12mm"},
                 display_header_footer=True,
                 header_template="<div></div>",
                 footer_template=(
                     "<div style='font-size:7pt;color:#8a96a3;width:100%;padding:0 12mm;"
                     "font-family:Arial,sans-serif;display:flex;justify-content:space-between'>"
                     f"<span>{title}</span>"
                     # both page numbers must sit in ONE flex child, or space-between
                     # scatters "1", "/" and "4" across the whole footer width
                     "<span><span class='pageNumber'></span> / "
                     "<span class='totalPages'></span></span></div>"))
        print(f"  {name:28} {os.path.getsize(dest)//1024:>5} KB")
        os.remove(tmp)
    browser.close()
print(f"\nPDFs in {PDF_DIR}")
