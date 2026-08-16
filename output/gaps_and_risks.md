# Gaps and risks

What this dataset does not know, what could still go wrong, and what to do about it.
Companion to `verification_report.md` (V1's audit) and `coverage_audit.md` (V2's).

---

## 1. Unresolved profile fields

Seven fields in the brief were left `[FILL]`. No values were invented. Any eligibility
test depending on one of them is recorded `UNVERIFIED`.

| Field | What it would have changed |
|---|---|
| Expected graduation | Recency cliffs: Vilnius caps the post-bachelor gap at 5 years for non-EU applicants; ASE Bucharest requires graduation in 2023 or later. Both are invisible on aggregators. |
| Target intake | Every deadline in the calendar is anchored to an assumed autumn 2027. A 2028 target shifts the entire timeline by a year. |
| IELTS status | AUEB Marketing Analytics requires **C2**; EBS requires 7.0; most require 6.5. Whether these are reachable is unknown, and a retake costs a cycle. |
| GPA / mention | IE's Dean's Award needs ≥3.8/4. Romania's scheme needs 7/10. Vilnius needs 60–70% averages. All unverifiable without the figure. |
| Budget ceiling | The difference between shortlisting Bremen at €0 and EBS at €33,780. Currently both are listed, which is unsatisfying but honest. |
| Funding posture | Decides whether Erasmus Mundus is the plan or a bonus. |
| Work-rights priority | Ireland's Stamp 1G (12 months, renewable to 24) is the strongest verified post-study right in the dataset. Whether that outweighs its equivalence risk is the applicant's call. |

**The highest-value unresolved question is not on that list.** It is: **do you intend
to return to Tunisia?** It decides how much weight the equivalence risk in §2 carries,
and therefore whether one-year masters belong in your plan at all.

---

## 2. The structural risks

### 2.1 Tunisian equivalence — discretionary, not fatal

The *arrêté* of 10 October 2023, articles 8 and 9, requires two years of study after
the licence. A one-year 60-ECTS master gives one. **But article 5 lets the commissions
disregard the required years where the ECTS count is sufficient** — V1 confirmed this
against the Arabic text after F3 missed it.

So: **51 of 181 rows carry discretionary risk, not disqualification.** All 15 Irish
rows, 11 of 16 Dutch, all 7 Spanish. A 120-ECTS two-year programme avoids the question
entirely, which is why the shortlist marks them.

Three further criteria from article 2 bite:
- **Examinations must be in person.** Hybrid and distance programmes are exposed — this
  affects both International Hellenic University rows, which are hybrid.
- **The programme must not be designed specifically for foreign students.**
- **Institution and diploma must both be recognised in the awarding country.**

**Action:** written confirmation from the Direction de l'Enseignement Supérieur Privé
et des Équivalences. Until then, treat one-year programmes as carrying real but
unquantified risk.

### 2.2 Track B's entry-qualification wall

The majority of media-production masters require a prior degree in media, film or fine
art. This is an eligibility rule, and a videography practice does not substitute:
Konstfack and Stockholm University of the Arts require a BFA; Kristiania 80 ECTS
in-field; Volda 90 ECTS plus practical courses; Xamk adds two years of industry work;
Le Fresnoy requires bac+5.

**Exactly three routes were found that are genuinely open:** SRH Berlin (portfolio, not
prior degree), FilmMemory (data-analytics entry assignment), and the technology-hosted
programmes at Bremen, AUTH, Leiden, EKA and ZHdK.

### 2.3 Esprit is private — and the Tunisian bourse may not reach you

The MESRS *bourse à l'étranger* pays €800/month in the EU plus tuition. But nomination
runs through the home institution, the procedure is written around public universities,
and the *bourse d'alternance* variant is **expressly limited to students of
établissements universitaires publics**. Whether Esprit students can be nominated at
all is unresolved. **Call DGAE before the October 2026 call.**

### 2.4 Subject-composition prerequisites

Not total credits — specific ones. Corvinus requires 18–24 ECTS across named
methodology, economics and business categories; Vilnius Digital Marketing 20 ECTS in
Business/Public Management or Economics; Vilnius Strategic Management 20 ECTS in
micro/macro/econometrics; EMAI 12 ECTS each of maths, programming and computing
science; Tilburg JADS 15 EC of maths and statistics plus named CS courses.

**Auditing your Esprit transcript against these categories is worth more than any
further searching.** Failures here are silent and late.

### 2.5 Accreditation that lapses

Four Cypriot programmes were rejected because CYQAA accreditation had expired with no
renewal — while their websites looked entirely normal. **ESSEC's *grade de master*
authorisation expires 31/08/2027**, at the assumed intake. Accreditation is a
point-in-time fact, not a permanent property, and MESRS equivalence depends on it.

---

## 3. Coverage gaps — what was not searched

### Confirmed absences (checked, nothing qualifies)

- **Serbia** — structurally closed. Master academic studies are 1 year / 60 ECTS on a
  mandatory 240-ECTS base; a 180-ECTS licence does not reach the entry floor. Confirmed
  independently at Singidunum and Belgrade FON.
- **Bosnia & Herzegovina** — same 4+1 structure. SSST is Buckingham-validated (UK rule).
- **Luxembourg** — no media master exists; its Data Science master has no
  business-analytics specialisation.
- **Monaco** — no programme in either track.
- **Finland** — no national scholarship scheme exists at all.

### Genuine gaps (not searched, or searched and unresolved)

| Gap | Size | What it would take |
|---|---|---|
| **Greek ministry database** | 1,368 programmes | `studies.minedu.gov.gr/program/?programme_id=N` — static, numbered records giving language, ECTS, fee **and delivery mode**. The highest-yield unexploited source in the project. |
| **~89 of 123 institutions unchecked for scholarships** | unknown | F4 checked 34 and stopped. Unchecked skew to continental public universities and Track B art schools, where awards are smaller but competition is thinner. |
| **Albania, North Macedonia, Montenegro** | 2 candidates found, neither recordable | SEEU publishes no second-cycle fee (one email). UNYT has no programme-level ASCAL decision and unresolved Greenwich exposure. |
| **Bulgaria** | effectively zero | Only Sofia's Digital Marketing MA surfaced; distance-format, Bulgarian admission rules. |
| **Second-tier Poland, Croatia, Romania, Lithuania** | unknown | Poznań, Wrocław, Cracow UE, AGH, SWPS; Zagreb FEB, ZSEM; UNATC; KTU, VDU. |
| **Portugal outside Lusófona** | unknown | ISEG, U.Porto, Aveiro, IPCA, ESAD, ESTC not reached. |

### Schema gap

**Delivery mode has no column.** The brief's schema predates the discovery that MESRS
requires in-person examinations, which makes hybrid and distance delivery an
eligibility fact rather than a preference. It is recorded in `fit_notes` where known,
but it is not queryable, and the Greek register publishes it for every programme.

---

## 4. What the audit did not verify

V1 was explicit, and this is the honest boundary of the dataset's reliability:

- **No deadline was independently verified.** Not one of 181 programme rows or 103
  funding rows had its deadline re-confirmed against the source.
- **`deadline_relative_to` is unaudited across all 103 scholarship rows** — and it is
  the field most likely to cost an opportunity, because several scholarships close
  before the application they depend on.
- **The EU-vs-non-EU trap was not tested systematically.** The brief calls it the most
  common error in this task. V1 names this as the highest-value next audit.
- Level integrity **was** checked on all 181 rows: **0 violations**.
- All 392 URLs were reachability-tested: **no dead links**. V1 initially reported two
  404s, re-tested with browser headers, found all 27 non-200s were false positives, and
  reported that rather than a phantom list.

**Field completeness, stated plainly:** tuition 88%, deadlines 63%, `min_prior_ects`
53%, `post_study_work_visa` 49%, living costs **11%**. Those numbers are low because
agents recorded `NOT_FOUND` instead of estimating. A denser-looking dataset would have
been a less honest one.

---

## 5. The six things to do first

1. **Write to the Direction de l'Enseignement Supérieur Privé et des Équivalences** and
   ask whether a 60-ECTS one-year master on a 3-year licence satisfies articles 8/9.
   Decides 51 rows.
2. **Call DGAE** and ask whether Esprit students can be nominated for the *bourse à
   l'étranger*. Decides whether the main Tunisian funding route exists for you.
3. **Audit your transcript** against the ECTS categories in §2.4.
4. **Book IELTS.** 4–8 weeks to a usable score; everything downstream waits on it.
5. **Start a Track B portfolio** if Track B is real for you — 2–4 months, and SRH Berlin
   is the one portfolio-admitted route found.
6. **Diarise November 2026 – January 2027.** Erasmus Mundus consortium deadlines, the
   MESRS bourse results, and Campus France all land in that window, roughly eight months
   before an autumn 2027 start.
