#!/usr/bin/env python3
"""Apply agent V1's verified corrections to the merged datasets.

V1 re-derived each of these from an official source it opened itself; the
verification report records the source URL for every one. This script edits the
per-agent CSVs so the corrections survive a re-merge, rather than patching the
merged output where the next merge would overwrite them.
"""
import csv, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
from merge_programmes import HEADER as P_HEADER
from merge_scholarships import HEADER as S_HEADER

# ---------------------------------------------------------------- programmes
# (institution match, programme match) -> {field: new value}
EDITS = [
    (("ghent", "business engineering"), {
        "tuition_non_eu_per_year": "7079.40 (non-EEA, Tuition Fee B tier, academic year 2026-2027; EUR 305.40 fixed + 60 x (31 + 81.90))",
        "tuition_source_url": "https://www.ugent.be/student/en/administration/tuition/tuition-fee-master-programme-not-advanced-and-masters-programme-in-teaching.htm/tuitionmasterteacher20262027.htm",
    }),
    (("bi norwegian", ""), {
        "institution_type": "private-accredited-by-state",
    }),
    (("srh", "film"), {
        "institution": "SRH University (formerly SRH Berlin University of Applied Sciences)",
        "tuition_non_eu_per_year": "11543 (non-EU; SRH published rate EUR 5,950 per semester / EUR 11,543 per year / EUR 22,610 total, plus a one-off EUR 1,000 enrolment fee; price list valid from 1 April 2025)",
        "tuition_source_url": "https://www.srh-university.de/fileadmin/1HE/International/SRH-University-Tuition-Fees-EN-Non-EU.pdf",
        "programme_url": "https://www.srh-university.de/en/master/film-television-digital-narratives/v/",
        "ects": "120",
        "intake_months": "April; October",
    }),
    (("algebra", "data science"), {
        "ects": "120",
        "duration_months": "24",
        "degree_awarded": "Data Science specialisation of the Professional Graduate Study Programme in Applied Computer Engineering; academic title mag. ing. comp. (Professional Master in Computer Engineering, sub-specialization in Data Science)",
    }),
    (("lucerne", ""), {
        "tuition_source_url": "https://www.hslu.ch/en/lucerne-school-of-information-technology/studium/master/applied-data-science-and-ai/",
        "app_deadline_source_url": "https://www.hslu.ch/en/lucerne-school-of-information-technology/studium/master/applied-data-science-and-ai/admission/",
        "programme_url": "https://www.hslu.ch/en/lucerne-school-of-information-technology/studium/master/applied-data-science-and-ai/",
    }),
    # EDHEC rows rest on V1's inference about which umbrella diploma covers them.
    (("edhec", ""), {"confidence": "medium"}),
]

# ESSEC's grade de master expires 31/08/2027 — squarely at the assumed intake.
ESSEC_NOTE = (" NOTE: ESSEC's grade de master authorisation expires 31/08/2027 per the "
              "CEFDG register; confirm renewal before relying on this row for a 2027 intake.")

applied = []
for path in sorted(glob.glob(os.path.join(ROOT, "data", "programmes_G*.csv"))):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig")))
    changed = False
    for r in rows:
        inst = (r.get("institution") or "").lower()
        prog = (r.get("programme_name_exact") or "").lower()
        for (i_match, p_match), fields in EDITS:
            if i_match in inst and (not p_match or p_match in prog):
                for k, v in fields.items():
                    if r.get(k) != v:
                        applied.append(f"{os.path.basename(path)}: {r['institution'][:30]} · {k}")
                        r[k] = v
                        changed = True
        if "essec" in inst and "expires 31/08/2027" not in (r.get("fit_notes") or ""):
            r["fit_notes"] = (r.get("fit_notes") or "").rstrip(". ") + "." + ESSEC_NOTE
            applied.append(f"{os.path.basename(path)}: ESSEC · fit_notes (grade expiry)")
            changed = True
    if changed:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=P_HEADER, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            w.writerows(rows)

# ------------------------------------------------- scholarship de-duplication
# V1 found exactly three duplicate pairs. Deduplicating on URL alone is wrong here:
# several institutions publish every award on one scholarships landing page, so IE's
# four distinct awards and ESMT's three share a URL without being duplicates. Match
# each pair by name instead, and drop only the weaker record of the pair.
def drop_stipendium(r):
    """Two agents found Stipendium Hungaricum; keep the row citing the Call PDF and
    carrying an amount. The discarded row's unique fact — that Tunisian full-degree
    nominations are restricted to named subject areas — is preserved in gaps_and_risks."""
    return ("stipendium hungaricum" in (r.get("scholarship_name") or "").lower()
            and (r.get("amount_eur_year") or "").strip().upper() in ("NOT_FOUND", ""))


def drop_tunesia(r):
    """The same DAAD entry (detail=10000344) recorded once under the German spelling."""
    return "tunesia" in (r.get("scholarship_name") or "").lower()


def drop_ares_dup(seen):
    def f(r):
        if "ares-ac.be/fr/bourses-de-formations-internationales" not in (r.get("url") or "").lower():
            return False
        if seen:
            return True          # second and later copies go
        seen.append(1)
        return False
    return f


ares_seen = []
RULES = [drop_stipendium, drop_tunesia, drop_ares_dup(ares_seen)]

dropped = []
for path in sorted(glob.glob(os.path.join(ROOT, "data", "scholarships_F*.csv"))):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig")))
    keep = []
    for r in rows:
        hit = next((rule for rule in RULES if rule(r)), None)
        if hit:
            dropped.append(f"{os.path.basename(path)}: {r['scholarship_name']}")
            continue
        keep.append(r)
    if len(keep) != len(rows):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=S_HEADER, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            w.writerows(keep)

print(f"programme field corrections applied: {len(applied)}")
for a in applied:
    print("  ", a)
print(f"\nscholarship duplicates dropped: {len(dropped)}")
for d in dropped:
    print("  ", d)
