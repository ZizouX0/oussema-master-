#!/usr/bin/env python3
"""Merge and deduplicate Wave 2 scholarship CSVs into output/scholarships_master.csv.

Dedup key: scholarship name + funder, normalised. F1–F4 overlap by design — an
Erasmus Mundus consortium award can surface from both the EU sweep and the
institution sweep — so the richer record wins, same rule as the programme merge.

Sort order: value descending (highest amount first, since funding_map.md is
ordered by value), then level, then name. Unknown amounts sort last.
"""
import csv, glob, os, re, sys, unicodedata

HEADER = [
    "scholarship_name", "funder", "level", "countries_covered",
    "institutions_covered", "tracks_eligible", "covers", "amount_eur_year",
    "duration_covered", "tunisia_eligible", "other_eligibility", "deadline",
    "deadline_relative_to", "application_route", "url", "verified_date",
    "confidence",
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[.'’]", "", s)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\b(scholarship|scholarships|programme|program|grant|grants|"
               r"award|awards|fellowship|the|of|for|de|du|des)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def verified_score(row: dict) -> int:
    return sum(
        1 for k, v in row.items()
        if v and v.strip() and v.strip().upper() not in {"NOT_FOUND", "N/A", "UNVERIFIED", "UNCLEAR"}
    )


def amount_key(v: str):
    m = re.search(r"\d[\d.,]*", v or "")
    if not m:
        return (1, 0.0)
    return (0, -float(m.group(0).replace(".", "").replace(",", ".")))


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = sorted(glob.glob(os.path.join(root, "data", "scholarships_F*.csv")))
    if not files:
        sys.exit("no data/scholarships_F*.csv found — has Wave 2 finished?")

    kept, dupes, per_source = {}, [], {}
    for path in files:
        agent = os.path.basename(path).replace("scholarships_", "").replace(".csv", "")
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        per_source[agent] = len(rows)
        for row in rows:
            row = {k: (row.get(k) or "").strip() for k in HEADER}
            key = (norm(row["scholarship_name"]), norm(row["funder"]))
            if not any(key):
                continue
            if key in kept:
                dupes.append((agent, row["scholarship_name"]))
                if verified_score(row) > verified_score(kept[key]):
                    kept[key] = row
            else:
                kept[key] = row

    out = sorted(kept.values(),
                 key=lambda r: (amount_key(r["amount_eur_year"]), r["level"], r["scholarship_name"]))
    dest = os.path.join(root, "output", "scholarships_master.csv")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(out)

    total = sum(per_source.values())
    print(f"merged {total} rows from {len(files)} agents -> {len(out)} unique "
          f"({len(dupes)} duplicates collapsed)\n")
    for agent in sorted(per_source):
        print(f"  {agent}: {per_source[agent]} rows")
    elig = {}
    for r in out:
        # agents cite the full eligibility clause in this field, so key on the verdict only
        verdict = re.split(r"[\s—-]", r["tunisia_eligible"].strip().lower(), 1)[0] or "blank"
        elig[verdict] = elig.get(verdict, 0) + 1
    print("\ntunisia_eligible:", elig)
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
