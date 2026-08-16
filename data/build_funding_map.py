#!/usr/bin/env python3
"""Build output/funding_map.md — every scheme the applicant is plausibly eligible for,
ordered by value, with the application route and how it sequences against university
deadlines.

Rows where `tunisia_eligible` starts with "no" are excluded from the map proper but
listed at the end: knowing a scheme is closed is what stops it being re-researched
every time it appears on a listicle.
"""
import csv, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NF = {"NOT_FOUND", "N/A", "", "UNVERIFIED"}


def verdict(v):
    return re.split(r"[\s—-]", (v or "").strip().lower(), 1)[0]


def amount(v):
    """Annual EUR value for ranking. Returns (has_value, value)."""
    if not v or v.strip().upper() in NF:
        return (0, 0)
    m = re.search(r"\d[\d ,.]*", v)
    if not m:
        return (0, 0)
    n = re.sub(r"[^\d]", "", m.group())
    return (1, int(n)) if n else (0, 0)


def clause(v, limit=180):
    """Agents cite the full eligibility clause; trim for display, keep the substance."""
    v = re.sub(r"\s+", " ", v or "").strip()
    return v if len(v) <= limit else v[:limit].rsplit(" ", 1)[0] + "…"


rows = list(csv.DictReader(open(os.path.join(ROOT, "output", "scholarships_master.csv"),
                                newline="", encoding="utf-8")))
open_rows = [r for r in rows if verdict(r["tunisia_eligible"]) == "yes"]
unclear = [r for r in rows if verdict(r["tunisia_eligible"]) == "unclear"]
closed = [r for r in rows if verdict(r["tunisia_eligible"]) == "no"]

open_rows.sort(key=lambda r: (-amount(r["amount_eur_year"])[0], -amount(r["amount_eur_year"])[1]))

by_level = {}
for r in open_rows:
    by_level.setdefault(r["level"] or "other", []).append(r)

out = [
    "# Funding map",
    "",
    f"{len(rows)} schemes examined: **{len(open_rows)} open to a Tunisian applicant**, "
    f"{len(unclear)} unresolved, {len(closed)} confirmed closed.",
    "",
    "Every eligibility verdict here was reached by opening the scheme's own country list or",
    "eligibility clause. None is inferred from a scheme describing itself as open to",
    "\"developing countries\" — that phrasing is exactly what makes these schemes look",
    "available when they are not.",
    "",
    "---",
    "",
    "## The order to actually work in",
    "",
    "Ranked by expected value, not by headline amount — a scheme's worth is its award",
    "multiplied by the chance of getting it, minus the effort of applying.",
    "",
    "**1. Erasmus Mundus Joint Masters — do these first, and do several.** Full tuition",
    "waiver plus €1,400/month for the whole degree. Tunisia is not merely eligible: the",
    "Erasmus+ Programme Guide 2026 allocates 18% of the budget to Neighbourhood South and",
    "requires **at least 20% of that to go to Tunisia**. No other scheme in this dataset",
    "combines that award size with that structural advantage. The deadlines are the",
    "earliest of anything here (late December to late January), and each consortium is a",
    "separate application, so they parallelise well.",
    "",
    "**2. Stipendium Hungaricum, Banach NAWA, Invest Your Talent in Italy.** Full national",
    "schemes that name Tunisia in their own lists and cover tuition plus living. All three",
    "run through a home-country nomination or a central portal rather than the university,",
    "so they sit *outside* the university timeline and can be pursued in parallel.",
    "",
    "**3. Institutional waivers at the expensive schools.** A 100% Bocconi merit award or a",
    "Maastricht NL-High Potential is worth more than a mid-size national scholarship — but",
    "these are lotteries with published odds as low as 2%, and most are decided inside the",
    "admission application. Apply early in the round; several are weighted to first rounds.",
    "",
    "**4. The Tunisian MESRS bourse.** €800/month in the EU plus tuition, but nomination is",
    "through the home institution and the whole procedure is written around public",
    "universities. **Establish whether Esprit students can be nominated at all before",
    "planning around it.**",
    "",
    "---",
    "",
]

LEVEL_ORDER = ["EU", "national", "institutional", "bilateral", "private", "other"]
LEVEL_TITLE = {
    "EU": "EU-level and multilateral",
    "national": "National government schemes",
    "institutional": "Institution-level awards and waivers",
    "bilateral": "Bilateral and third-party",
    "private": "Private foundations",
    "other": "Other",
}

for lv in LEVEL_ORDER:
    if lv not in by_level:
        continue
    out += [f"## {LEVEL_TITLE[lv]} ({len(by_level[lv])})", "",
            "| Scheme | Covers | Amount /yr | Deadline | Sequencing | Route |",
            "|---|---|---|---|---|---|"]
    for r in by_level[lv]:
        out.append(
            f"| **{r['scholarship_name']}** — {r['funder']} | {r['covers']} | "
            f"{r['amount_eur_year']} | {r['deadline']} | {r['deadline_relative_to']} | "
            f"{r['application_route']} |")
    out += [""]

if unclear:
    out += [
        "---",
        "",
        f"## Unresolved ({len(unclear)}) — worth one email each",
        "",
        "Each of these is plausibly open but could not be confirmed from a published list.",
        "They are not in the ranking above because presenting an unconfirmed scheme as",
        "available is the failure mode this project is built to avoid.",
        "",
        "| Scheme | Why unresolved | Where to ask |",
        "|---|---|---|",
    ]
    for r in unclear:
        out.append(f"| **{r['scholarship_name']}** — {r['funder']} | {clause(r['tunisia_eligible'])} | {r['url']} |")
    out += [""]

out += [
    "---",
    "",
    f"## Confirmed closed to Tunisian nationals ({len(closed)})",
    "",
    "Recorded so they are not researched again. Several appear on every \"scholarships for",
    "African students\" listicle; the clause that excludes Tunisia is quoted in each case.",
    "",
    "| Scheme | The excluding clause |",
    "|---|---|",
]
for r in closed:
    out.append(f"| **{r['scholarship_name']}** — {r['funder']} | {clause(r['tunisia_eligible'], 300)} |")

out += [
    "",
    "---",
    "",
    "## Sequencing, stated plainly",
    "",
    "The single most expensive mistake available here is applying to a university before",
    "checking whether its funding closed first. Three patterns recur:",
    "",
    "- **Scholarship deadline *is* the admission deadline.** CBS Copenhagen: tick the box and",
    "  write the statement inside the 15 January application, or the money is gone.",
    "- **Scholarship requires an application already submitted.** Maastricht NL-High Potential",
    "  needs Studielink done by 8 December, with the scholarship form following by 1 February.",
    "- **Region-specific earlier deadlines.** UCD closes for **Africa-region** graduate",
    "  applicants on 28 February, a month before every other region. Luiss closes its non-EU",
    "  window on 20 March, a month before its EU window.",
    "",
    "And two that require the offer in hand: Galway's Cairnes and both Maynooth awards need",
    "the offer **accepted and the deposit paid** by the deadline, which makes \"automatic\"",
    "awards conditional on moving money early.",
    "",
]

dest = os.path.join(ROOT, "output", "funding_map.md")
open(dest, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"wrote {dest} — {len(open_rows)} open, {len(unclear)} unresolved, {len(closed)} closed")
