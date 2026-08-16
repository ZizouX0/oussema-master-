#!/usr/bin/env python3
"""Build output/deadline_calendar.md — one chronological timeline of every dated
deadline in the dataset, from today forward, with the lead-time items that must be
started before them.

Dates already past are kept only when they mark the shape of a recurring cycle
(the brief's PRIOR_CYCLE convention): the 2026/27 round having closed on 15 January
tells the applicant when the 2027/28 round will close, which is the actionable fact.
"""
import csv, os, re
from datetime import date

TODAY = date(2026, 8, 16)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISO = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def parse(v):
    m = ISO.search(v or "")
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def load(name):
    p = os.path.join(ROOT, "output", name)
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


programmes = load("programmes_master.csv")
scholarships = load("scholarships_master.csv")

events = []
for r in programmes:
    d = parse(r["app_deadline_non_eu"])
    if d:
        prior = "PRIOR_CYCLE" in r["app_deadline_non_eu"]
        events.append({
            "date": d, "prior": prior, "kind": "programme",
            "what": f"{r['institution']} — {r['programme_name_exact']}",
            "where": f"{r['country']} · Track {r['track']}",
            "note": r["tuition_non_eu_per_year"],
        })
for r in scholarships:
    d = parse(r["deadline"])
    if d:
        prior = "PRIOR_CYCLE" in r["deadline"]
        events.append({
            "date": d, "prior": prior, "kind": "funding",
            "what": f"{r['scholarship_name']} — {r['funder']}",
            "where": r["level"],
            "note": f"{r['deadline_relative_to']} · {r['application_route']}",
        })

future = sorted([e for e in events if e["date"] >= TODAY], key=lambda e: e["date"])
past = sorted([e for e in events if e["date"] < TODAY], key=lambda e: (e["date"].month, e["date"].day))

out = [
    "# Deadline calendar",
    "",
    f"Generated {TODAY.isoformat()} from `programmes_master.csv` and `scholarships_master.csv`.",
    "",
    "Two sections. **Live dates** are deadlines that have not yet passed and can be acted",
    "on directly. **Cycle shape** covers deadlines that closed for the 2026/27 intake — they",
    "are kept because they tell you when the equivalent 2027/28 deadline will fall, which is",
    "the fact that matters for an autumn-2027 target. Nothing here is a prediction: each is",
    "the last published date for that programme or scheme.",
    "",
    "---",
    "",
    "## Before any of these: the lead-time items",
    "",
    "These are not deadlines, they are durations. Each must be *finished* before a deadline",
    "below, and each takes weeks to months. Starting them late is the most common way a",
    "well-researched application still fails.",
    "",
    "| Item | Realistic lead time | Why it gates everything after it |",
    "|---|---|---|",
    "| **MESRS equivalence enquiry** | Ask now; answer unknown | Decides whether one-year masters are usable at all. 51 of 179 rows depend on the answer. Direction de l'Enseignement Supérieur Privé et des Équivalences. |",
    "| **DGAE enquiry — can Esprit students be nominated?** | Ask now; before Oct 2026 | The MESRS bourse is nomination-based through the home institution, and the procedure is written around public universities. If private-institution students cannot be nominated, the main Tunisian funding route is closed. |",
    "| **Transcript audit against ECTS categories** | 1–2 weeks, self-directed | Corvinus requires 18–24 ECTS in named categories; Vilnius 20 ECTS in economics/management; EMAI 12 ECTS each of maths, programming, computing science. Fails are silent and late. |",
    "| **IELTS booking and sitting** | 4–8 weeks to a usable score | Test centres fill. AUEB Marketing Analytics requires **C2**; EBS requires IELTS 7.0. A retake adds another cycle. |",
    "| **Portfolio production (Track B)** | 2–4 months | SRH Berlin wants five to eight finished pieces plus a list of five favourite films. This is the one Track B route open on portfolio rather than a prior media degree — it is worth real time. |",
    "| **Recommendation letters** | 3–6 weeks | Academic referees are unavailable over the Tunisian summer break. |",
    "| **Transcript translation and legalisation** | 3–6 weeks | Sworn translation for anything not in Arabic, French or English; legalisation by both ministries. |",
    "| **Campus France «Études en France»** | Opens ~October for the following September | **Mandatory for Tunisians applying to France.** Caps you at 7 choices, requires an interview, then allow ~2 months for the visa. It closes before French university deadlines. |",
    "",
    "---",
    "",
    "## Live dates — from today forward",
    "",
]

if future:
    out += ["| Date | Days | Type | What | Where | Detail |", "|---|---|---|---|---|---|"]
    for e in future:
        out.append(f"| **{e['date'].isoformat()}** | {(e['date']-TODAY).days} | {e['kind']} | {e['what']} | {e['where']} | {e['note']} |")
else:
    out.append("_No future-dated deadlines in the dataset._")

out += [
    "",
    "---",
    "",
    "## Cycle shape — 2026/27 dates, read as next year's timing",
    "",
    "Sorted by month and day rather than year, because the point is the annual position.",
    "Expect the 2027/28 equivalent within a week or two of the same date.",
    "",
    "| Month-day | Type | What | Where | Detail |",
    "|---|---|---|---|---|",
]
for e in past:
    out.append(f"| {e['date'].strftime('%d %b')} | {e['kind']} | {e['what']} | {e['where']} | {e['note']} |")

out += [
    "",
    "---",
    "",
    "## The shape of the year, in one paragraph",
    "",
    "The binding sequence for an autumn-2027 start runs backwards from a January 2027",
    "cluster. **Erasmus Mundus consortium deadlines fall between roughly 20 December and",
    "20 January** — eight to nine months before the start, and three to four months ahead of",
    "the same consortium's self-funded round. **The Tunisian MESRS bourse call opens around",
    "October 2026 with results in late January 2027.** **Campus France «Études en France»",
    "opens around October 2026.** Several institutional scholarships close earlier still",
    "because they are folded into the admission application: Maastricht wants Studielink by",
    "8 December, CBS folds the scholarship into a 15 January admission, and UCD's",
    "Africa-region graduate deadline is 28 February — a month ahead of every other region.",
    "Working back from those, the IELTS sitting and the portfolio must be finished by",
    "**November 2026**, which means starting them in **September 2026**.",
    "",
]

dest = os.path.join(ROOT, "output", "deadline_calendar.md")
open(dest, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"wrote {dest} — {len(future)} live, {len(past)} cycle-shape entries")
