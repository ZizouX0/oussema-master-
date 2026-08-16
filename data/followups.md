# Follow-up verification queue

Items Wave 1 agents flagged as unresolved and explicitly handed forward. Wave 3
(V1 fact-integrity, V2 coverage) consumes this list. Each entry names what to
check and where, so no item depends on rediscovering the context.

| # | Item | Territory | What to verify | Why it matters |
|---|---|---|---|---|
| 1 | **HEC Paris / École Polytechnique — MSc Data Science & AI for Business (X-HEC)** | G3 France | Whether it confers *grade de master* / *diplôme visé*. Check polytechnique.edu's own MSc&T accreditation page — the HEC pages don't state it. | Arguably the strongest Track A match in France. Application rounds already published for the target cycle (R1 2026-10-07 → R4 2027-04-28). Excluded pending this check. |
| 2 | **Tilburg — MSc Data Science in Business and Entrepreneurship (JADS)** | G2 Benelux | Programme page: ECTS, non-EU deadline, 3-year-bachelor acceptance. Fee listed €23,900 (26/27). | Squarely Track A. Dropped for a procedural reason (avoiding a duplicate Tilburg cluster), not a rule violation — it belongs in the dataset. |
| 3 | **Vlerick Business School masters** | G2 Benelux | Whether the "Masters in …" portfolio maps to NVAO-accredited Flemish master degrees. NVAO register shows decisions only for *Innovation and Entrepreneurship* and an MBA. | €20,950–22,950/yr. If not NVAO-accredited it fails MESRS equivalence — a costly mistake to make late. |
| 4 | **ZHdK Zurich — Track B masters** | G1 DACH | Which ZHdK MAs are English-taught. Programme list returns an empty shell to plain fetch; needs Firecrawl scrape. | The one known gap in Swiss Track B. |
| 5 | **Leiden — MSc Media Technology** | G2 Benelux | Current title, ECTS, whether production-oriented. Appears renamed/absorbed into *Creative Intelligence and Technology*. | Was a listed Track B target; status unresolved. |
| 6 | **Bologna DAMS/Cinema, IUAV Venice, Centro Sperimentale di Cinematografia, state Accademie di Belle Arti** | G7 Italy | Whether any second-cycle programme is English-taught. Assessed from prior evidence, not individually fetched. | Determines whether Italian Track B is genuinely limited to POLIMI + private academies. |
| 7 | **IED Milano — MA Visual Communication** | G7 Italy | A MIM/MUR accreditation decree for IED **Milano** second-level courses (one exists for IED Firenze, and for Milan/Rome/Turin first-level only). | Page claims *Diploma Accademico di Secondo Livello*, 120 CFA, English. Reported not recorded — resolvable only by decree or direct enquiry. |
| 8 | **ARES exemption circular (Belgium)** | G2 Benelux | Whether a Tunisian national can be exempted from the €4,175 non-EU supplement. Categories named are LDCs, scholarship holders, long-term residents. | Tunisia is not an LDC, so the applicant likely pays the full €5,369. Unconfirmed — the circular itself was never opened. |
| 9 | **Ghent tuition figure** | G2 Benelux | Two different non-EEA figures on two official UGent pages (€6,929 vs €6,540.10), neither naming an academic year. | Straight fact conflict; V1 must resolve which cycle each belongs to. |
| 10 | **Italian post-study work permit** | G7 Italy | Official ministry statement of the *permesso per attesa occupazione* terms. | `post_study_work_visa` is NOT_FOUND on every Italian row because no official source was reachable. |
| 11 | **Serbia, Albania, North Macedonia, Montenegro, Bosnia & Herzegovina, Moldova** | G8 CEE | **Zero coverage — not a single institutional page was opened.** Needs a dedicated pass. | G8's search allowance ran out a third of the way through 17 countries. Silence here must not be read as "nothing exists", and these are the countries where the 240-ECTS structural risk is most likely to be real. |
| 12 | **Bulgaria** | G8 CEE | Sofia University and the other state universities. Only Sofia's Digital Marketing MA surfaced, and it is distance-format with Bulgarian-language admission rules and no published fee. | Same as above: unresolved rather than empty. |
| 13 | **Poland, Croatia, Romania, Lithuania — second tier** | G8 CEE | Not reached: Poznań UEB, Wrocław UEB, Cracow UE, AGH, SWPS; Zagreb Faculty of Economics, ZSEM, Academy of Fine Arts Zagreb, ADU; UNATC Bucharest, Politehnica; KTU, VDU. | Coverage is substantial but explicitly not exhaustive in these four countries. |

## Transcript audit — act on this early

G8 surfaced the single most actionable finding of Wave 1 so far: **in the countries
it verified, the danger to a 180-ECTS holder is not total credits but subject
composition.** No country it reached imposes a blanket 240-ECTS rule — Ljubljana
states 180 is sufficient in writing, and Czechia, Poland, Estonia and Hungary
accept a bachelor in any field. But three institutions gate on *specific prior
credits*, which is exactly where a Business Intelligence licence can fail:

- **Corvinus (Budapest)** — 18–24 ECTS required across methodology, economics and
  business-studies categories, assessed per programme. Binds all four Corvinus rows.
- **Vilnius, Digital Marketing** — minimum 20 ECTS in Business/Public Management or
  Economics, plus a 70% grade average.
- **Vilnius, Strategic Management of Information Systems** — minimum 20 ECTS in
  microeconomics, macroeconomics or econometrics (or three years' verified work
  experience), plus a 60% average.

**Two recency cliffs that appear in no aggregator listing:** Vilnius University
requires that non-EU applicants' gap since the bachelor not exceed five years, and
Romania's ASE FABIZ requires non-EU applicants to have graduated in 2023 or later.
Both behave as hard eligibility cutoffs.

Practical consequence: the applicant's Esprit transcript should be audited against
those ECTS categories before any application effort is spent. That is a
higher-value action than any further searching.

## Deliberate exclusions worth surfacing to the applicant

Not errors — correct calls under the brief — but each is a real option the
applicant may want to reconsider, so they belong in `gaps_and_risks.md` rather
than vanishing.

- **University of Luxembourg — Master in Data Science.** 120 ECTS, English,
  **€800/year including non-EU** — by a wide margin the cheapest qualifying-level
  programme found anywhere in the sweep. Excluded because it sits in maths/CS with
  no business-analytics specialisation, so it fails the Track A definition. If the
  applicant will accept a general data-science master, this is the single strongest
  cost outlier in the dataset.
- **Luxembourg Track B: nothing exists.** The full 2026 master's brochure contains
  no media-production, film, digital-media or media-design master.
- **LUCA School of Arts, RITCS, KASK/HOGENT** (Flemish audiovisual arts) —
  Dutch-taught, no English variant found. Language near-misses.
- **Universitat d'Andorra — Master of Data Analytics.** 120 ECTS, AQUA-accredited,
  and it explicitly accepts 3-year bachelors — but taught in Catalan.
- **FH St. Pölten — Digital Media Production.** German-taught; otherwise close to a
  perfect Track B match at €1,500/semester.
- **Monaco** — no programme in either track; the entire IUM master portfolio is
  management/finance plus an MBA and DBA.
