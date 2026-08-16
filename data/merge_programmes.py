#!/usr/bin/env python3
"""Merge and deduplicate Wave 1 programme CSVs into output/programmes_master.csv.

Dedup key: institution + programme name, both normalised (lowercase, punctuation
and legal-form noise stripped). The same programme can legitimately surface from
two agents when an institution sits near a territory boundary or runs a joint
degree, so the merge keeps the record with the most verified fields rather than
the first one seen.

Sort order, per the brief: track, then country, then tuition ascending
(NOT_FOUND sorts last so unverified cost never leads a country block).
"""
import csv, glob, os, re, sys, unicodedata

HEADER = [
    "track", "country", "city", "institution", "institution_type",
    "programme_name_exact", "degree_awarded", "faculty_or_school", "language",
    "duration_months", "ects", "intake_months", "tuition_non_eu_per_year",
    "tuition_source_url", "living_cost_estimate_year", "app_deadline_non_eu",
    "app_deadline_source_url", "min_prior_ects", "accepts_3yr_bachelor",
    "english_req", "other_tests", "portfolio_required", "work_experience_required",
    "quantitative_prereqs", "programme_url", "post_study_work_visa", "fit_notes",
    "verified_date", "confidence",
]

NOISE = re.compile(
    r"\b(university|universit[aeày]t?|universidade|universidad|universit[eé]|"
    r"school|schule|hochschule|escuela|escola|business|of|the|de|di|des|du|van|"
    r"der|and|&|msc|ma|mssc|master|masters|master's|in|programme|program)\b"
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    # Drop dots and apostrophes before splitting, so "M.Sc." collapses to "msc"
    # rather than tokenising into "m sc" and never matching "MSc".
    s = re.sub(r"[.'’]", "", s)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = NOISE.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


def verified_score(row: dict) -> int:
    """How many fields carry a real value rather than NOT_FOUND/blank."""
    return sum(
        1 for k, v in row.items()
        if v and v.strip() and v.strip().upper() not in {"NOT_FOUND", "N/A", "UNVERIFIED"}
    )


def tuition_key(v: str):
    m = re.search(r"\d[\d.,]*", v or "")
    if not m:
        return (1, 0.0)  # NOT_FOUND and friends sort last
    return (0, float(m.group(0).replace(".", "").replace(",", ".")))


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = sorted(glob.glob(os.path.join(root, "data", "programmes_G*.csv")))
    if not files:
        sys.exit("no data/programmes_G*.csv found — has Wave 1 finished?")

    kept, dupes, per_source = {}, [], {}
    for path in files:
        agent = os.path.basename(path).replace("programmes_", "").replace(".csv", "")
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        per_source[agent] = {"rows": len(rows), "A": 0, "B": 0}
        for row in rows:
            row = {k: (row.get(k) or "").strip() for k in HEADER}
            per_source[agent][row["track"]] = per_source[agent].get(row["track"], 0) + 1
            key = (norm(row["institution"]), norm(row["programme_name_exact"]))
            if not any(key):
                continue
            if key in kept:
                dupes.append((agent, row["institution"], row["programme_name_exact"]))
                if verified_score(row) > verified_score(kept[key]):
                    kept[key] = row
            else:
                kept[key] = row

    out = sorted(
        kept.values(),
        key=lambda r: (r["track"], r["country"], tuition_key(r["tuition_non_eu_per_year"])),
    )
    dest = os.path.join(root, "output", "programmes_master.csv")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(out)

    print(f"merged {sum(v['rows'] for v in per_source.values())} rows from "
          f"{len(files)} agents -> {len(out)} unique ({len(dupes)} duplicates collapsed)\n")
    print(f"{'agent':6} {'rows':>5} {'A':>4} {'B':>4}")
    for agent in sorted(per_source):
        v = per_source[agent]
        print(f"{agent:6} {v['rows']:>5} {v.get('A', 0):>4} {v.get('B', 0):>4}")
    if dupes:
        print("\nduplicates collapsed:")
        for agent, inst, prog in dupes:
            print(f"  [{agent}] {inst} — {prog}")
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
