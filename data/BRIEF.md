# SHARED BRIEF — European Master's & Scholarship Research

Every agent in this operation reads this file first. Today's date: **2026-08-16**.
Repo root: `/home/user/oussema-master-`.

---

## APPLICANT PROFILE (confirmed fields only)

```
Nationality:              Tunisian (non-EU/EEA — this drives tuition and deadlines)
Current degree:           Licence — 3-year bachelor, 180 ECTS — Business Intelligence
Institution:              Esprit School of Business, Tunisia
Prior education:          Technical baccalauréat
Languages:                French (fluent), English (fluent), Arabic (native)
Technical skills:         Python, Scikit-learn, SQL, Power BI, Talend, machine learning,
                          data analytics, big data, decision-support systems
Creative practice:        Videography, video editing, visual content creation, music production
```

**UNRESOLVED — do not invent values for these. Any eligibility test that depends on
one of them is recorded `UNVERIFIED`:**
expected graduation · target intake · IELTS status/band · GPA/mention ·
budget ceiling EUR/year · funding posture · work-rights priority.

Working assumption for cycle context only (never presented as fact): graduation
mid-2027, target intake autumn 2027, applications opening late 2026 → mid 2027.

---

## THE TWO TRACKS

**TRACK A — Business Analytics.** Match semantically, not by exact string:
MSc Business Analytics · AI & Business Analytics · Data Science for Business ·
Business Analytics & Big Data · Analytics & Decision Sciences · Data-Driven
Management · Digital Business & Analytics · Marketing Analytics · Applied Data
Science (business-hosted). Include business schools, management faculties,
economics faculties, and CS-faculty programmes with an explicit business-analytics
specialisation.

**TRACK B — Digital Media / Media Production.**
MA Digital Media · Media Production · Digital Media Production · New Media ·
Media Arts & Production · Film & Digital Media · Screen Media · Interactive Media ·
Media Design · MSc Media Technology (production-oriented). Include art schools,
film schools, communication faculties, and applied-sciences universities
(Fachhochschule / hogeschool / ammattikorkeakoulu). These are systematically
missed by rankings-based searching — search national programme databases and
search in the local language even when the programme is taught in English.

---

## HARD CONSTRAINTS

1. **Geography:** continental Europe only. **EXCLUDE the United Kingdom. EXCLUDE
   Turkey.** No exceptions — including joint programmes with a UK partner
   institution. Flag those separately in your notes rather than recording them.
2. **Institution type:** public and private both. Private institutions must be
   tagged and their accreditation verified against the national accreditation body.
3. **Language:** taught in **English or French only**. Tag which. A programme
   requiring another language for admission is excluded — note partial-requirement
   near-misses in your notes.
4. **LEVEL — MASTER'S DEGREES ONLY. The strictest filter in this brief.**
   Qualifies only if it is a full second-cycle degree awarding a master's title,
   **60 ECTS minimum**, recognised as a master's by the national qualifications
   framework.

   **Excluded with no exceptions:** MBAs and Executive MBAs (including "MBA in
   Business Analytics"); executive, part-time-professional and continuing-education
   programmes; postgraduate diplomas and certificates; *Mastère Spécialisé* (FR);
   *máster propio / título propio* (ES); bootcamps, professional certificates,
   micro-credentials, summer schools; bachelor's, integrated 5-year programmes
   entered at year one, foundation years; PhD/doctoral/research-only programmes;
   pre-master's and bridging programmes — **except** where a bridging route is the
   required entry path into a qualifying master's for a 180-ECTS holder, which goes
   in the parent programme's `fit_notes`, never as its own row.

   **The two most common traps:** in Spain, *máster propio* is university-awarded
   and is NOT equivalent to *máster oficial* — only *oficial* qualifies and only
   *oficial* passes MESRS equivalence in Tunisia. In France, *Mastère Spécialisé*
   (CGE label) is not the state *Master* diploma. Verify which you are looking at
   and record the distinction in `degree_awarded`.

   If you cannot confirm state recognition, **do not put the row in your CSV** —
   list it in your final report under "level unconfirmed."
5. **Degree recognition:** the applicant holds 180 ECTS. Some countries and
   programmes require 240. **Critical filter** — record `min_prior_ects` for every
   row and flag where a 3-year bachelor is insufficient or needs a bridging year.

---

## VERIFICATION RULES — NON-NEGOTIABLE

1. **Never state a fact without an official source URL** — university, ministry, or
   funder page. Aggregators (Studyportals, Mastersportal, Keystone, ranking sites)
   may be used to **discover** programmes but **never** as the source for tuition,
   deadlines, or eligibility.
2. **Never construct a URL.** If you cannot find the page, write `NOT_FOUND`.
3. **Record the cycle** a figure belongs to. Today is 2026-08-16: the 2026/27
   intake cycle has closed and 2027/28 figures may not be published yet. If only a
   previous cycle's figure exists, record it and append ` PRIOR_CYCLE` to the value.
4. **Non-EU vs EU is the most common error in this task.** Non-EU/EEA tuition and
   deadlines are frequently different and often on a separate page. Get the non-EU
   figure. If only one figure exists, verify explicitly that it applies to non-EU
   applicants before recording it.
5. **Accreditation check for every private institution** — MESRS equivalence back
   in Tunisia depends on it. Flag anything unconfirmed.
6. **No estimates, no ranges, no "approximately"** unless the source itself says so.
7. **No editorialising inside the data files.** `fit_notes` is factual fit against
   the profile, two sentences maximum. Analysis belongs in the final report only.

---

## RESEARCH TOOLING

Load web tools first: `ToolSearch` with query `select:WebSearch,WebFetch`.

**Order of preference:**
1. `WebSearch` to discover, `WebFetch` to read. These are unmetered — use them for
   the overwhelming majority of your work.
2. **Firecrawl only when WebFetch fails** — JavaScript-rendered course catalogues,
   art-school sites that return an empty shell, or when you need every programme
   under a path. The CLI is authenticated:
   ```bash
   firecrawl scrape "<url>" -o .firecrawl/<name>.md     # one JS-heavy page
   firecrawl map "<domain>" --search "master"           # find programme URLs
   ```
   **Hard budget: 40 firecrawl calls per agent.** The account holds ~1,000 credits
   shared across all 14 agents. Exceeding your budget starves later agents. Report
   how many you used.

**Search national programme databases first** — they are more complete than any
ranking site. Locate and use the registry for each of your countries: DAAD
(DE), Studyinfo.fi (FI), studyinholland / Studiekeuze123 (NL), Campus France
catalogue (FR), Universitaly (IT), universityadmissions.se (SE), Study in Denmark,
national ministry registries elsewhere. Then individual faculty pages. Then the
applied-sciences and art-school sector explicitly. Then the private sector
explicitly — private business schools dominate Track A and rarely appear in
public databases.

---

## WRITING YOUR CSV

Write with Python's `csv` module so quoting is correct — never hand-assemble CSV
lines, several fields contain commas.

```python
import csv
HEADER = [ ... exact field list for your wave, in order ... ]
with open("data/<your file>.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(HEADER)
    w.writerows(rows)
```

Unverifiable field → the literal string `NOT_FOUND`. Never an estimate, never blank.

### Wave 1 — programme record header (exact order)

```
track,country,city,institution,institution_type,programme_name_exact,degree_awarded,
faculty_or_school,language,duration_months,ects,intake_months,tuition_non_eu_per_year,
tuition_source_url,living_cost_estimate_year,app_deadline_non_eu,app_deadline_source_url,
min_prior_ects,accepts_3yr_bachelor,english_req,other_tests,portfolio_required,
work_experience_required,quantitative_prereqs,programme_url,post_study_work_visa,
fit_notes,verified_date,confidence
```

Values: `track` A|B · `institution_type` public|private|private-accredited-by-state|
applied-sciences · `language` EN|FR|EN/FR · `tuition_non_eu_per_year` numeric EUR
(convert and note the original currency) · dates ISO `YYYY-MM-DD` ·
`min_prior_ects` 180|240|other · `accepts_3yr_bachelor` yes|no|conditional|NOT_FOUND ·
`portfolio_required` yes|no|n/a · `work_experience_required` yes|no|preferred ·
`verified_date` 2026-08-16 · `confidence` high|medium|low.

### Wave 2 — scholarship record header (exact order)

```
scholarship_name,funder,level,countries_covered,institutions_covered,tracks_eligible,
covers,amount_eur_year,duration_covered,tunisia_eligible,other_eligibility,deadline,
deadline_relative_to,application_route,url,verified_date,confidence
```

Values: `level` EU|national|bilateral|institutional|private · `tracks_eligible` A|B|both ·
`covers` tuition|tuition+stipend|partial|travel|living only · `tunisia_eligible`
yes|no|unclear — and cite where the eligibility clause lives · `deadline_relative_to`
before/after university application (**critical — always record it**) ·
`application_route` apply via university|apply direct|via home ministry.

---

## KNOWN FAILURE MODES

- **Track B is harder than Track A.** Media production lives in art schools and
  applied-sciences institutions with thin English web presence and no aggregator
  listings. Budget more effort there. Search local-language programme names.
- **Private business schools inflate.** Ignore rankings and employment marketing
  entirely; record only schema fields.
- **Tunisian eligibility is inconsistently documented.** Many schemes say
  "developing countries" or point to an ODA-recipient list rather than naming
  Tunisia. Open the actual list and check. Do not infer.
- **The 3-year bachelor question disqualifies otherwise-perfect matches**,
  especially in parts of Central Europe and for some German programmes. Check it
  early per programme, not at the end.
- **Do not stop at the first plausible answer per country.** Exhaustiveness within
  the constraints is the point.
- **Coverage floor:** never pad. If a territory genuinely yields few Track B
  results, say so and describe exactly what you searched.

**Accuracy outranks coverage. A short verified list beats a long speculative one.**
