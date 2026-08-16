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
| 14 | **UPF — Master in Digital Culture and Emerging Media** | G6 Spain | Language of instruction. The page carries an English title, English CV/motivation requirement and a B2 English floor, but never states the teaching language. | Officially recognised UPF master. **The single most likely additional Spain Track B row** — Spain currently yields only two. |
| 15 | **Universidad Pontificia Comillas — Máster Universitario en Análisis de Negocio / Business Analytics** | G6 Spain | Language of instruction. Official status already confirmed (BOE-A-2025-15932); the programme page was unreachable. | Second-most-likely additional Spain Track A row. |
| 16 | **EADA, EAE, ESIC, Deusto, IED Madrid/Barcelona, Elisava, BAU, U-tad** | G6 Spain | *Oficial* vs *propio* status of any English-taught master. | **Unverified, not rejected** — the distinction is unclear from their marketing pages, which is exactly the trap the brief warns about. |
| 17 | **Lusófona tuition** | G6 Portugal | An annual figure. The site publishes a per-ECTS rate (€11.18–12.68) and a "monthly value for 30 ECTS" (€335.40–380.40) that are mutually inconsistent; the fees pages render empty. | Four Track B rows carry `NOT_FOUND` tuition. Lusófona is the **only** Portuguese provider running English-taught DGES-registered media-production masters at scale, so these rows matter disproportionately. |
| 18 | **Portugal post-study work permit** | G6 Portugal | Article 122.º-O terms from an official source. AIMA returned 503 repeatedly; SEF's site is retired. | `post_study_work_visa` is NOT_FOUND on all eight Portuguese rows. |
| 19 | **ISEG, U.Porto, U.Aveiro, IPCA, ESAD, Escola Superior de Teatro e Cinema** | G6 Portugal | Not reached before the search allowance ran out. | Portuguese coverage is incomplete, particularly for Track B outside Lusófona. |

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

## Additional deliberate exclusions from G6 (Spain / Portugal)

- **ISCTE Business School — Master in Business Analytics** and **Master in Data
  Science.** Non-EU tuition €5,000 year 1 / €2,500 year 2 — cheap, and an exact
  Track A title. Excluded because ISCTE states the programmes are lectured in
  Portuguese, with only three Data Science units deliverable in English. Worth
  revisiting only if the applicant's Portuguese changes.
- **ESCAC — Máster Universitario en Estudios de Cine y Culturas Visuales**
  (Universitat de Barcelona, official, 60 ECTS, €5,200). Spain's strongest film-school
  official master; Spanish-taught.
- **Berklee Valencia — MM Music Production, Technology & Innovation** and the two
  other production masters (€50,430). These are **US Berklee degrees carrying no
  Spanish official title** — only Berklee's Global Entertainment and Music Business
  master holds a Spanish RUCT registration, and that one is an entertainment-business
  degree fitting neither track. Given the applicant's music-production practice this
  is the most tempting exclusion in the dataset, and the level rule is unambiguous.
- **Universidad de Navarra — Máster Universitario en Big Data Science.** Official,
  but Spanish-taught *and* delivered in a Friday/Saturday executive format.
- **Lusófona / KINO EYES — The European Movie Master** (Erasmus Mundus). Excluded
  under the UK-partner rule: Edinburgh Napier is a consortium partner. Flagged here
  because Wave 2's F1 agent will encounter it in the EMJMD catalogue and must apply
  the same rule.

**Structural finding — Spain Track B.** Two verified rows only, after searching in
Spanish and Catalan across ESCAC, ECAM, UPF Communication, UPV, IED, Elisava, BAU,
U-tad, URJC/IUNIT and Berklee Valencia. The pattern is consistent and structural:
Spain's official media and film masters are almost all taught in Spanish or Catalan,
and the English-taught media offer is concentrated in private schools selling
*títulos propios*. This is a finding about the country, not a gap in the search.

## G4 (Nordics) follow-ups

| # | Item | What to verify | Why it matters |
|---|---|---|---|
| 20 | **BI Norwegian Business School** accreditation | NOKUT accreditation as a specialised university institution. BI's own page says only "an independent, not-for-profit foundation". | Tagged `private` unconfirmed. MESRS equivalence depends on it and BI is a headline Track A name at NOK 135,600/yr. |
| 21 | **Reykjavík University** accreditation + tuition | Icelandic ministry accreditation; tuition published only inside linked PDF fee schedules that the scrape could not reach. | Private, unconfirmed on both counts. |
| 22 | **NTNU (Norway)** | Non-EEA fee page (`ntnu.edu/studies/tuition-fee`); search suggested NOK 176,300/yr for economics/social science. | The one Norwegian institution left unopened. No row created. |
| 23 | **Luleå (LTU)** tuition | The fee table lists "Data Science" and "International Business" but has no row for Data Analytics in Business and Economics. | Recorded `NOT_FOUND` rather than inferred from a neighbouring programme. |
| 24 | **University of Lapland — Arctic Indigenous Cinema MA** | Whether admission is open irrespective of Indigenous background. €13,000/yr with a €6,000 scholarship, 120 ECTS, English. | A genuine Track B match excluded only because eligibility could not be confirmed. |
| 25 | **Post-study work rights, all five Nordic countries** | Official immigration-authority statements. | `post_study_work_visa` is `NOT_FOUND` on all 22 Nordic rows; the agent refused to assert terms from memory. |

## Structural finding — Track B has an entry-qualification wall

This is now visible across three territories and is more consequential for this
applicant than tuition or deadlines. **Media-production masters overwhelmingly
require a prior degree in the field, not merely a portfolio.** The applicant's
videography and music-production practice is real but sits outside a media
bachelor, and these are hard eligibility rules rather than preferences:

- **Konstfack (SE)** — requires a Bachelor of Fine Arts; selection on artistic
  portfolio and interview.
- **Stockholm University of the Arts (SE)** — requires a BFA plus a degree project
  from a Film and Media bachelor. Also the most expensive programme found anywhere
  in the sweep: SEK 1,346,000 total.
- **Kristiania (NO)** — 80 ECTS required within audiovisual media, storytelling,
  visual art, design or technology.
- **Volda (NO)** — 90 ECTS in media/journalism plus 40 ECTS of practical courses.
- **Xamk (FI), Virtual Production** — the strongest Finnish UAS match on content;
  restricted to Bachelor of Engineering or Bachelor of Culture and Arts holders
  **plus two years' post-degree work experience in the field**.
- **Le Fresnoy (FR)** — bac+5 or seven years' professional experience.
- **La Fémis (FR)** — 4-year cursus entered at bac+2.

Consequence for the shortlist: Track B candidates must be filtered on
`quantitative_prereqs` / prior-degree subject before cost or deadline. The
realistic Track B openings for a Business Intelligence graduate are the
technology-and-media-hosted programmes (interaction design, media technology,
digital media at applied-sciences universities) rather than the film and fine-art
academies — and that distinction should drive the Track B shortlist rather than
programme prestige.
