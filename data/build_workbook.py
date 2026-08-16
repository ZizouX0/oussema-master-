#!/usr/bin/env python3
"""Build output/masters_research.xlsx — the whole dataset in one filterable workbook.

Design goals, in order:
  1. Every sheet filters and sorts without setup — autofilter on, header frozen.
  2. Add the derived columns the raw CSVs lack but every real question needs:
     a numeric tuition column (the text one cannot be sorted), and an
     equivalence-safe flag (2 years / 120 ECTS).
  3. Colour carries meaning, never decoration: green = verified/safe,
     amber = conditional, red = blocked or unverified.
"""
import csv, os, re, sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "output")

INK = "1F2933"
HEAD_FILL = PatternFill("solid", fgColor="1F2933")
HEAD_FONT = Font(color="FFFFFF", bold=True, size=10)
GREEN = PatternFill("solid", fgColor="D8F0DC")
AMBER = PatternFill("solid", fgColor="FDF0D5")
RED = PatternFill("solid", fgColor="FADBD8")
GREY = PatternFill("solid", fgColor="EEF1F4")
THIN = Side(style="thin", color="D3D9DF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def load(name):
    with open(os.path.join(OUT, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def eur(v):
    """Pull a sortable number out of a free-text tuition field."""
    if not v or v.strip().upper() in ("NOT_FOUND", "N/A", ""):
        return None
    m = re.search(r"\d[\d\s.,]*", v)
    if not m:
        return None
    s = m.group().strip()
    # 7079.40 / 23,900 / 1 346 000 -> keep decimals, drop thousands separators
    s = re.sub(r"[\s]", "", s)
    if re.search(r"[.,]\d{2}$", s):
        s = re.sub(r"[.,](?=\d{3})", "", s)
        s = s.replace(",", ".")
    else:
        s = re.sub(r"[.,]", "", s)
    try:
        return round(float(s), 2)
    except ValueError:
        return None


def two_year(r):
    e = re.search(r"\d+", r.get("ects") or "")
    d = re.search(r"\d+", r.get("duration_months") or "")
    if (e and int(e.group()) >= 120) or (d and int(d.group()) >= 20):
        return "yes"
    if (e and int(e.group()) < 120) or (d and int(d.group()) < 20):
        return "NO - discretionary risk"
    return "unknown"


def style_sheet(ws, ncols, nrows, widths, wrap_cols=(), freeze="A2"):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for c in range(1, ncols + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill, cell.font = HEAD_FILL, HEAD_FONT
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border = BORDER
    ws.row_dimensions[1].height = 30
    ws.freeze_panes = freeze
    if nrows >= 1:
        ws.auto_filter.ref = f"A1:{get_column_letter(ncols)}{nrows + 1}"
    for row in ws.iter_rows(min_row=2, max_row=nrows + 1, max_col=ncols):
        for cell in row:
            cell.border = BORDER
            cell.alignment = Alignment(
                vertical="top",
                wrap_text=cell.column in wrap_cols,
            )
            cell.font = Font(size=10)


wb = Workbook()

# ------------------------------------------------------------------ READ ME
ws = wb.active
ws.title = "READ ME"
readme = [
    ("European Master's & Scholarship Research", 16, True),
    ("181 verified programmes · 103 funding schemes · 27 countries · compiled 2026-08-16", 11, False),
    ("", 11, False),
    ("HOW TO USE THIS WORKBOOK", 12, True),
    ("Every sheet has filter arrows on the header row and the header frozen — click any arrow to filter.", 10, False),
    ("Sort by any column. The 'Tuition EUR (sortable)' column exists because the raw tuition text cannot be sorted.", 10, False),
    ("", 11, False),
    ("THE SHEETS", 12, True),
    ("Shortlist — start here. 15 Track A + 15 Track B chosen for fit to your actual profile.", 10, False),
    ("Programmes — all 181. Filter by track, country, language, 2-year flag, 3-year-bachelor acceptance.", 10, False),
    ("Funding — all 103 schemes. Filter 'Tunisia eligible' to yes.", 10, False),
    ("Deadlines — every dated deadline, chronological. Filter by status to see only live ones.", 10, False),
    ("Actions — the 6 things to do first, then the full follow-up queue with named contacts.", 10, False),
    ("Excluded — programmes deliberately kept out, with the reason. Check here before re-researching anything.", 10, False),
    ("", 11, False),
    ("COLOUR MEANS SOMETHING", 12, True),
    ("Green — verified, or safe on that criterion.", 10, False),
    ("Amber — conditional, or depends on something unresolved.", 10, False),
    ("Red — blocked, ineligible, or unverified where it matters.", 10, False),
    ("", 11, False),
    ("THREE THINGS TO KNOW BEFORE READING ANYTHING ELSE", 12, True),
    ("1. NOT_FOUND means nobody could verify it from an official source. It is never an estimate. "
     "Living costs are NOT_FOUND on 89% of rows for this reason.", 10, False),
    ("2. Tuition is per year for a non-EU applicant, and excludes living costs. In Switzerland, Ireland "
     "and the Nordics living costs exceed tuition several times over; in Greece, Poland and Romania they do not.", 10, False),
    ("3. No deadline in this dataset was independently re-verified. Confirm any deadline you act on.", 10, False),
]
for i, (text, size, bold) in enumerate(readme, start=1):
    c = ws.cell(row=i, column=1, value=text)
    c.font = Font(size=size, bold=bold, color=INK)
    c.alignment = Alignment(wrap_text=True, vertical="top")
ws.column_dimensions["A"].width = 118
for i in (1, 4, 8, 16, 21):
    ws.row_dimensions[i].height = 24
for i in (22, 23, 24):
    ws.row_dimensions[i].height = 30

# --------------------------------------------------------------- Programmes
progs = load("programmes_master.csv")
P_COLS = [
    ("track", "Track", 7), ("country", "Country", 14), ("city", "City", 16),
    ("institution", "Institution", 34), ("institution_type", "Type", 16),
    ("programme_name_exact", "Programme", 38), ("degree_awarded", "Degree awarded", 26),
    ("language", "Lang", 8), ("duration_months", "Months", 8), ("ects", "ECTS", 7),
    ("_2yr", "2-year (equivalence safe)", 15),
    ("_tuition_num", "Tuition EUR (sortable)", 13),
    ("tuition_non_eu_per_year", "Tuition, non-EU, as published", 30),
    ("app_deadline_non_eu", "Deadline (non-EU)", 15),
    ("min_prior_ects", "Min prior ECTS", 10),
    ("accepts_3yr_bachelor", "Accepts 3-yr bachelor", 12),
    ("english_req", "English requirement", 24), ("other_tests", "Other tests", 14),
    ("portfolio_required", "Portfolio", 10),
    ("quantitative_prereqs", "Quantitative prerequisites", 34),
    ("post_study_work_visa", "Post-study work", 22),
    ("fit_notes", "Fit notes", 40), ("confidence", "Confidence", 11),
    ("programme_url", "Programme URL", 30), ("tuition_source_url", "Tuition source", 30),
]
ws = wb.create_sheet("Programmes")
ws.append([c[1] for c in P_COLS])
for r in progs:
    r["_2yr"] = two_year(r)
    r["_tuition_num"] = eur(r.get("tuition_non_eu_per_year"))
    ws.append([r.get(c[0]) for c in P_COLS])
style_sheet(ws, len(P_COLS), len(progs), [c[2] for c in P_COLS],
            wrap_cols={6, 7, 13, 17, 20, 22})
idx = {c[0]: i + 1 for i, c in enumerate(P_COLS)}
for row in range(2, len(progs) + 2):
    for key, fill_map in (
        ("_2yr", {"yes": GREEN, "NO - discretionary risk": RED, "unknown": AMBER}),
        ("accepts_3yr_bachelor", {"yes": GREEN, "no": RED, "conditional": AMBER, "NOT_FOUND": GREY}),
        ("confidence", {"high": GREEN, "medium": AMBER, "low": RED}),
    ):
        cell = ws.cell(row=row, column=idx[key])
        fill = fill_map.get(str(cell.value))
        if fill:
            cell.fill = fill
    for key in ("programme_url", "tuition_source_url"):
        cell = ws.cell(row=row, column=idx[key])
        if isinstance(cell.value, str) and cell.value.startswith("http"):
            cell.hyperlink = cell.value
            cell.font = Font(size=9, color="1B6AC9", underline="single")
    t = ws.cell(row=row, column=idx["_tuition_num"])
    t.number_format = '#,##0'

# ------------------------------------------------------------------ Funding
funds = load("scholarships_master.csv")
F_COLS = [
    ("scholarship_name", "Scholarship", 38), ("funder", "Funder", 26),
    ("level", "Level", 14), ("_elig", "Tunisia eligible", 13),
    ("countries_covered", "Countries", 24), ("institutions_covered", "Institutions", 24),
    ("tracks_eligible", "Tracks", 9), ("covers", "Covers", 18),
    ("_amount_num", "Amount EUR/yr (sortable)", 14),
    ("amount_eur_year", "Amount as published", 26),
    ("duration_covered", "Duration covered", 18),
    ("deadline", "Deadline", 15),
    ("deadline_relative_to", "Sequencing vs university application", 30),
    ("application_route", "How to apply", 22),
    ("other_eligibility", "Other eligibility", 38),
    ("tunisia_eligible", "Eligibility clause (verbatim)", 60),
    ("confidence", "Confidence", 11), ("url", "URL", 32),
]
ws = wb.create_sheet("Funding")
ws.append([c[1] for c in F_COLS])
for r in funds:
    r["_elig"] = re.split(r"[\s—-]", (r.get("tunisia_eligible") or "").strip().lower(), 1)[0] or "?"
    r["_amount_num"] = eur(r.get("amount_eur_year"))
    ws.append([r.get(c[0]) for c in F_COLS])
style_sheet(ws, len(F_COLS), len(funds), [c[2] for c in F_COLS],
            wrap_cols={1, 13, 15, 16})
fidx = {c[0]: i + 1 for i, c in enumerate(F_COLS)}
for row in range(2, len(funds) + 2):
    cell = ws.cell(row=row, column=fidx["_elig"])
    cell.fill = {"yes": GREEN, "no": RED, "unclear": AMBER}.get(str(cell.value), GREY)
    c2 = ws.cell(row=row, column=fidx["confidence"])
    c2.fill = {"high": GREEN, "medium": AMBER, "low": RED}.get(str(c2.value), GREY)
    u = ws.cell(row=row, column=fidx["url"])
    if isinstance(u.value, str) and u.value.startswith("http"):
        u.hyperlink = u.value
        u.font = Font(size=9, color="1B6AC9", underline="single")
    a = ws.cell(row=row, column=fidx["_amount_num"])
    a.number_format = '#,##0'


# ---------------------------------------------------------------- Shortlist
def md_tables(path):
    """Yield (heading, [rows]) for every pipe table in a markdown file."""
    heading, header, rows = "", None, []
    for line in open(path, encoding="utf-8"):
        s = line.strip()
        if s.startswith("#"):
            if header and rows:
                yield heading, header, rows
            heading, header, rows = s.lstrip("# ").strip(), None, []
            continue
        if s.startswith("|") and s.endswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            if header is None:
                header = cells
            else:
                rows.append(cells)
        elif header and rows:
            yield heading, header, rows
            header, rows = None, []
    if header and rows:
        yield heading, header, rows


def strip_md(v):
    v = re.sub(r"\*\*(.+?)\*\*", r"\1", v)
    v = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", v)
    return v.replace("✅", "yes").replace("⚠️", "caution").replace("`", "").strip()


short = []
for heading, header, rows in md_tables(os.path.join(OUT, "shortlist.md")):
    track = "A" if "TRACK A" in heading.upper() else ("B" if "TRACK B" in heading.upper() else None)
    if not track or len(header) < 6:
        continue
    for r in rows:
        short.append([track] + [strip_md(c) for c in r])

if short:
    ws = wb.create_sheet("Shortlist", 1)
    ws.append(["Track", "Rank", "Programme", "Country", "2-year",
               "Tuition/yr", "After funding", "The specific risk"])
    for r in short:
        ws.append(r[:8])
    style_sheet(ws, 8, len(short), [7, 6, 46, 12, 9, 16, 24, 58], wrap_cols={3, 6, 7, 8})
    for row in range(2, len(short) + 2):
        t = ws.cell(row=row, column=1)
        t.fill = GREEN if t.value == "A" else AMBER
        y = ws.cell(row=row, column=5)
        y.fill = GREEN if str(y.value).startswith("yes") else AMBER

# ---------------------------------------------------------------- Deadlines
from datetime import date
TODAY = date(2026, 8, 16)
ISO = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def parse_date(v):
    m = ISO.search(v or "")
    if not m:
        return None
    try:
        return date(*(int(g) for g in m.groups()))
    except ValueError:
        return None


dl = []
for r in progs:
    d = parse_date(r.get("app_deadline_non_eu"))
    if d:
        dl.append([d, "live" if d >= TODAY else "closed - shows next year's timing",
                   "programme", f"{r['institution']} — {r['programme_name_exact']}",
                   r["country"], f"Track {r['track']}",
                   r.get("tuition_non_eu_per_year"), "", r.get("programme_url")])
for r in funds:
    d = parse_date(r.get("deadline"))
    if d:
        dl.append([d, "live" if d >= TODAY else "closed - shows next year's timing",
                   "funding", f"{r['scholarship_name']} — {r['funder']}",
                   r.get("countries_covered"), r.get("level"),
                   r.get("amount_eur_year"), r.get("deadline_relative_to"), r.get("url")])
dl.sort(key=lambda x: x[0])

ws = wb.create_sheet("Deadlines", 3)
ws.append(["Date", "Status", "Type", "What", "Where", "Level / Track",
           "Amount or tuition", "Sequencing", "URL"])
for r in dl:
    ws.append(r)
style_sheet(ws, 9, len(dl), [12, 30, 11, 54, 22, 14, 26, 30, 30], wrap_cols={4, 7, 8})
for row in range(2, len(dl) + 2):
    c = ws.cell(row=row, column=1)
    c.number_format = "yyyy-mm-dd"
    s = ws.cell(row=row, column=2)
    s.fill = GREEN if s.value == "live" else GREY
    u = ws.cell(row=row, column=9)
    if isinstance(u.value, str) and u.value.startswith("http"):
        u.hyperlink = u.value
        u.font = Font(size=9, color="1B6AC9", underline="single")

# ------------------------------------------------------------------ Actions
ACTIONS = [
    ["1", "Write to Direction de l'Enseignement Superieur Prive et des Equivalences (MESRS)",
     "Ask whether a 60-ECTS one-year master on a 3-year licence satisfies articles 8/9 of the arrete of 10 Oct 2023.",
     "Decides whether 51 of 181 programmes are usable, including all 15 Irish rows.", "NOW"],
    ["2", "Call DGAE (Direction Generale des Affaires Estudiantines)",
     "Ask whether students of a PRIVATE institution (Esprit) can be nominated for the bourse universitaire a l'etranger.",
     "The procedure is written around public universities. If not, the main Tunisian funding route is closed to you.",
     "Before Oct 2026"],
    ["3", "Audit your Esprit transcript against named ECTS categories",
     "Corvinus 18-24 ECTS in methodology/economics/business; Vilnius 20 ECTS economics or management; EMAI 12 ECTS each maths, programming, computing; JADS 15 EC maths and statistics.",
     "Failures here are silent and late. Worth more than any further searching.", "1-2 weeks, self-directed"],
    ["4", "Book IELTS", "Target 7.0 overall. AUEB Marketing Analytics needs C2; EBS needs 7.0; most need 6.5.",
     "4-8 weeks to a usable score, and everything downstream waits on it. A retake costs a cycle.", "September 2026"],
    ["5", "Start a Track B portfolio (only if Track B is real for you)",
     "SRH Berlin wants 5-8 finished pieces plus a list of five favourite films.",
     "It is the ONLY portfolio-admitted Track B route found in the whole search. Takes 2-4 months.", "September 2026"],
    ["6", "Diarise November 2026 - January 2027",
     "Erasmus Mundus consortium deadlines, MESRS bourse results, Campus France Etudes en France opening.",
     "The entire funding year lands in this window, ~8 months before an autumn 2027 start.", "Now"],
]
ws = wb.create_sheet("Actions", 4)
ws.append(["#", "Action", "What exactly", "Why it matters", "When"])
for a in ACTIONS:
    ws.append(a)
start = len(ACTIONS) + 3
ws.cell(row=start, column=1, value="FULL FOLLOW-UP QUEUE — items agents could not resolve").font = Font(bold=True, size=11, color=INK)
qrows = []
for heading, header, rows in md_tables(os.path.join(ROOT, "data", "followups.md")):
    for r in rows:
        if len(r) >= 4 and r[0].strip().isdigit():
            qrows.append([r[0], strip_md(r[1]), strip_md(r[2]) if len(r) > 4 else "",
                          strip_md(r[-2]), strip_md(r[-1])])
ws.append([])
ws.append(["#", "Item", "Territory", "What to verify", "Why it matters"])
hdr2 = ws.max_row
for q in qrows:
    ws.append(q)
style_sheet(ws, 5, len(ACTIONS), [5, 46, 60, 60, 20], wrap_cols={2, 3, 4})
for c in range(1, 6):
    cell = ws.cell(row=hdr2, column=c)
    cell.fill, cell.font = HEAD_FILL, HEAD_FONT
    cell.alignment = Alignment(vertical="center", wrap_text=True)
for row in range(2, ws.max_row + 1):
    for c in range(1, 6):
        cell = ws.cell(row=row, column=c)
        if cell.row > hdr2 or cell.row <= len(ACTIONS) + 1:
            cell.alignment = Alignment(vertical="top", wrap_text=c in (2, 3, 4, 5))
            cell.font = cell.font if cell.row == hdr2 else Font(size=10)
for row in range(2, len(ACTIONS) + 2):
    ws.cell(row=row, column=1).fill = RED if row <= 3 else AMBER

# ----------------------------------------------------------------- Excluded
EXCLUDED = [
    ["Vlerick Business School (all masters)", "Belgium", "A",
     "Genuine NVAO-accredited degrees, but Flemish master-na-master: open ONLY to holders of a prior master's. You cannot enter.", "Ineligible"],
    ["Berklee Valencia — MM Music Production, Technology & Innovation (+2 others)", "Spain", "B",
     "US Berklee degrees carrying no Spanish official title. Only their Global Entertainment and Music Business master has RUCT registration.", "Level"],
    ["GOBELINS Paris — Mastere animation", "France", "B",
     "Official page claims only 'diplome vise niveau 7', never grade de master.", "Level"],
    ["Neapolis Pafos — MA Digital Video Production (~EUR 3,500)", "Cyprus", "B",
     "CYQAA accreditation expired Spring 2022, no renewal in the register. Was the most on-target Cypriot Track B match.", "Accreditation lapsed"],
    ["European University Cyprus — MSc Digital Media", "Cyprus", "B", "CYQAA accreditation expired Spring 2023.", "Accreditation lapsed"],
    ["The Cyprus Institute — MSc Simulation and Data Science", "Cyprus", "A", "CYQAA accreditation expired Spring 2023.", "Accreditation lapsed"],
    ["University of Nicosia — MA Digital Art and Design", "Cyprus", "B", "CYQAA accreditation ran only to Spring 2026, already lapsed.", "Accreditation lapsed"],
    ["University of Luxembourg — Master in Data Science", "Luxembourg", "A",
     "EUR 800/yr including non-EU — the cheapest qualifying-level programme found anywhere. Excluded only because it sits in maths/CS with no business-analytics specialisation. RECONSIDER if a general data-science master is acceptable.", "Track definition"],
    ["Le Fresnoy", "France", "B", "No level statement on any official page, and entry requires bac+5 or 7 years' professional experience.", "Level + ineligible"],
    ["La Femis", "France", "B", "A 4-year cursus entered at bac+2, structurally not a second-cycle master.", "Level"],
    ["Lodz Film School — Film and TV Production", "Poland", "B", "Curriculum entirely in Polish, C1 Polish required. The strongest Track B name in Poland.", "Language"],
    ["FH St. Polten — Digital Media Production", "Austria", "B", "German-taught. Otherwise close to a perfect match at EUR 1,500/semester.", "Language"],
    ["Universitat d'Andorra — Master of Data Analytics", "Andorra", "A", "Catalan-taught. Explicitly accepts 3-year bachelors.", "Language"],
    ["ISCTE — Business Analytics / Data Science", "Portugal", "A", "Portuguese-taught. EUR 5,000 y1 / 2,500 y2 — cheap and exact-title.", "Language"],
    ["Konstfack, Stockholm University of the Arts, Kristiania, Volda, Xamk", "SE/NO/FI", "B",
     "All require a prior degree in media/film/fine art (BFA, or 80-90 in-field ECTS, or 2 years' industry work). A videography practice does not substitute.", "Entry qualification"],
    ["Mundus Journalism, CLMCE, MAGMA, GLOCAL, EDUMAH, Kino Eyes", "multi", "B",
     "Erasmus Mundus consortia with UK partners (City St George's, Glasgow, Edinburgh Napier).", "UK partner"],
    ["UCLan Cyprus, Prague City University, SSST Sarajevo", "CY/CZ/BA", "A/B", "Degrees validated by UK institutions.", "UK partner"],
    ["Serbia — all", "Serbia", "A/B", "Master academic studies are 1 year / 60 ECTS on a mandatory 240-ECTS base. A 180-ECTS licence does not reach the entry floor.", "Structurally closed"],
    ["Bosnia — IUS and others", "Bosnia", "A/B", "Same 4+1 structure as Serbia.", "Structurally closed"],
    ["All MBAs and Executive MBAs", "all", "A", "Excluded by the brief with no exceptions, including 'MBA in Business Analytics' variants.", "Level"],
]
ws = wb.create_sheet("Excluded", 5)
ws.append(["Programme / group", "Country", "Track", "Why it was excluded", "Category"])
for e in EXCLUDED:
    ws.append(e)
style_sheet(ws, 5, len(EXCLUDED), [50, 14, 8, 78, 22], wrap_cols={1, 4})
for row in range(2, len(EXCLUDED) + 2):
    ws.cell(row=row, column=5).fill = AMBER

# -------------------------------------------------------------- Institutions
inst = []
for heading, header, rows in md_tables(os.path.join(ROOT, "data", "institutions.md")):
    for r in rows:
        if len(r) >= 4:
            inst.append([strip_md(c) for c in r[:4]])
if inst:
    ws = wb.create_sheet("Institutions")
    ws.append(["Country", "Institution", "Type", "Tracks"])
    for r in inst:
        ws.append(r)
    style_sheet(ws, 4, len(inst), [16, 52, 22, 10])

wb.save(os.path.join(OUT, "masters_research.xlsx"))
print(f"wrote masters_research.xlsx")
print(f"  Programmes {len(progs)} · Funding {len(funds)} · Shortlist {len(short)} · "
      f"Deadlines {len(dl)} · Actions {len(ACTIONS)}+{len(qrows)} · Excluded {len(EXCLUDED)} · "
      f"Institutions {len(inst)}")
