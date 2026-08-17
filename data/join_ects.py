#!/usr/bin/env python3
"""Join the E1-E4 entry-ECTS findings back into the per-agent programme CSVs.

Two columns are appended to the Wave 1 schema. The brief fixed that schema before
anyone knew how this field actually behaves in the wild: most institutions state
their entry bar in words ("a Level 8 honours degree, or equivalent") rather than
credits, so `min_prior_ects` alone throws away the answer. `entry_requirement_note`
keeps the actual wording, and `entry_requirement_source_url` makes it checkable.
"""
import csv, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
import merge_programmes

NEW_COLS = ["entry_requirement_note", "entry_requirement_source_url"]
HEADER = merge_programmes.HEADER + NEW_COLS


def key(inst, prog):
    return (merge_programmes.norm(inst), merge_programmes.norm(prog))


# ---- collect findings -------------------------------------------------------
findings, seen = {}, []
for path in sorted(glob.glob(os.path.join(ROOT, "data", "ects", "done_E*.csv"))):
    for r in csv.DictReader(open(path, newline="", encoding="utf-8-sig")):
        findings[key(r["institution"], r["programme_name_exact"])] = r
        seen.append(os.path.basename(path))
if not findings:
    sys.exit("no data/ects/done_E*.csv found yet")

# ---- apply ------------------------------------------------------------------
NF = {"NOT_FOUND", "", "N/A"}
stats = {"ects_filled": 0, "3yr_filled": 0, "notes_added": 0, "unmatched": 0, "rows": 0}
for path in sorted(glob.glob(os.path.join(ROOT, "data", "programmes_G*.csv"))):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig")))
    for r in rows:
        stats["rows"] += 1
        for c in NEW_COLS:
            r.setdefault(c, "NOT_FOUND")
            if not (r.get(c) or "").strip():
                r[c] = "NOT_FOUND"
        f = findings.get(key(r["institution"], r["programme_name_exact"]))
        if not f:
            continue
        new_ects = (f.get("min_prior_ects") or "").strip()
        if new_ects and new_ects.upper() not in NF and (r["min_prior_ects"] or "").upper() in NF:
            r["min_prior_ects"] = new_ects
            stats["ects_filled"] += 1
        new_3yr = (f.get("accepts_3yr_bachelor") or "").strip()
        if new_3yr and new_3yr.upper() not in NF and (r["accepts_3yr_bachelor"] or "").upper() in NF:
            r["accepts_3yr_bachelor"] = new_3yr
            stats["3yr_filled"] += 1
        note = (f.get("entry_requirement_note") or "").strip()
        if note and note.upper() not in NF:
            r["entry_requirement_note"] = note
            stats["notes_added"] += 1
        src = (f.get("source_url") or "").strip()
        if src and src.upper() not in NF:
            r["entry_requirement_source_url"] = src
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

# findings that matched nothing — a naming drift worth surfacing, not swallowing
matched = set()
for path in sorted(glob.glob(os.path.join(ROOT, "data", "programmes_G*.csv"))):
    for r in csv.DictReader(open(path, newline="", encoding="utf-8-sig")):
        matched.add(key(r["institution"], r["programme_name_exact"]))
orphans = [f for k, f in findings.items() if k not in matched]

print(f"findings loaded: {len(findings)} from {len(set(seen))} agent files")
print(f"  min_prior_ects filled      {stats['ects_filled']}")
print(f"  accepts_3yr_bachelor filled {stats['3yr_filled']}")
print(f"  entry notes attached        {stats['notes_added']}")
if orphans:
    print(f"\n  UNMATCHED findings ({len(orphans)}) — check for name drift:")
    for f in orphans:
        print(f"    {f['institution'][:40]} — {f['programme_name_exact'][:44]}")

# keep the merge schema in step so a re-merge does not drop the new columns
merge_programmes.HEADER = HEADER
