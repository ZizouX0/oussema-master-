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

## G5 (Ireland / Malta / Cyprus / Greece) follow-ups

**The Cypriot private sector is an accreditation minefield — G5's most valuable
finding.** Four programmes were rejected because their CYQAA accreditation has
lapsed with no renewal row in the register. These look entirely normal on their own
websites, and a degree from a programme whose accreditation expired will not pass
MESRS equivalence:

| Institution | Programme | CYQAA status |
|---|---|---|
| Neapolis University Pafos | MA Digital Video Production (~€3,500) | **expired Spring 2022** — was the single most on-target Track B match in Cyprus |
| European University Cyprus | MSc Digital Media | **expired Spring 2023** |
| The Cyprus Institute | MSc Simulation and Data Science | **expired Spring 2023** |
| University of Nicosia | MA Digital Art and Design | runs only to **Spring 2026** — already lapsed |

Each is worth a direct enquiry (accreditation may have been renewed without the
register being updated), but none can be recorded as verified today.

| # | Item | What to verify | Why it matters |
|---|---|---|---|
| 26 | **Greece — International Hellenic University**, Piraeus, NKUA, West Attica, Ionian University (audiovisual arts), American College of Greece / Alba | English-taught master's catalogues. IHU is a public university teaching **exclusively in English** and is likely the richest unexplored Greek source. Alba needs a UK-validation check. | Greece yields only 2 rows. The agent estimates a proper pass adds 4–8. The ministry database holds 1,368 programmes behind JS pagination and needs a crawl budget. |
| 27 | **IADT — KinoEyes / Viewfinder joint MAs** | Consortium partner lists. KinoEyes historically includes a UK partner. | Flagged not recorded, pending partner verification. Wave 2's F1 will meet these in the EMJMD catalogue and must apply the same rule. |
| 28 | **Post-study work rights: Malta, Cyprus, Greece** | Official third-country post-study residence rules. | Only Ireland's is verified (Stamp 1G: 12 months, renewable once to 24). The agent calls this the largest remaining gap in the territory and a real differentiator. |
| 29 | **Neapolis — MA Digital Video Production** | Whether CYQAA accreditation was renewed after Spring 2022. | Cheapest on-target Track B programme found in the whole sweep (~€3,500). Worth one email. |

**Excluded but worth reconsidering if the Track A definition is loosened:** National
College of Ireland MSc Data Analytics (€17,000, January 2027 start, IELTS 6.0),
Maynooth MSc Data Science and Analytics (€17,000) and MSc Digital Marketing
(€18,000). All are QQI-accredited NFQ Level 9 awards; all were excluded only because
they sit in a school of computing without an explicit business-analytics
specialisation.

**UK-linked exclusions applied correctly:** UCLan Cyprus (MSc Data Analytics, MSc/MA
Graphic Design) is the Cyprus campus of a UK institution.

**Irish equivalency note:** no Irish page states a rule for a Tunisian 180-ECTS
licence. Entry text uniformly reads "NFQ Level 8 honours degree or equivalent",
which is an individual assessment rather than a published yes/no — so `min_prior_ects`
is `NOT_FOUND` on every Irish row and `accepts_3yr_bachelor` is `conditional`. For
this applicant that means Ireland cannot be cleared in advance from public pages;
it requires per-programme enquiry.

## F4 (institution-level scholarships) follow-ups

**~89 of 123 institutions were never checked.** F4 worked strictly down the priority
order and stopped after the high-tuition tiers plus one art school. Unchecked and
worth a second pass, in rough value order: Barcelona School of Economics, Carlos III,
Politecnico di Milano, Ca' Foscari, Bologna, Trento, WU Vienna, USI, HSLU, ECAL/HEAD,
LUT, Oulu, BTH, Luleå, all Belgian, all French public, all German public, all
Czech/Polish/Romanian/Baltic/Slovenian institutions, plus the Track B schools
(FAMU, RUFA, Piet Zwart/Rotterdam UAS, AHK, AUAS, Macromedia, MOME, PJAIT,
ifs Köln, Filmuniversität Babelsberg, Louis-Lumière, ENSAV).

| # | Item | What to verify | Why it matters |
|---|---|---|---|
| 30 | **Católica-Lisbon** scholarships | Fees/scholarships page returned 503 to WebFetch and empty to Firecrawl. Only the bachelor's scheme was readable. | A Track A institution with no scholarship data at all. Worth a retry. |
| 31 | **IE Middle East & Africa Award** | The eligible-region country list renders client-side behind a "More info" control; neither WebFetch nor Firecrawl retrieved it. | Recorded `unclear`. IE tuition is among the highest in the dataset, so the answer is worth real money. |
| 32 | **Amsterdam Merit Scholarship (UvA)** | Amounts and deadlines are devolved to each Faculty/Graduate School and not published centrally. Check Economics and Business (Track A) and Humanities (Track B) separately. | `NOT_FOUND` on value and deadline. |
| 33 | **Frankfurt School master scholarship** | The published 15/25/50/75/100% ladder belongs to the **BSc** programme; the master's page says only "a partial amount of tuition". | Value unknown for a school charging non-EU master's fees. |
| 34 | **UCC College of Business and Law merit scholarships** | Confirmed to exist and to be automatic, but no value, eligibility detail or deadline is published anywhere. | Recorded at `low` confidence with three `NOT_FOUND` fields. |

### Institutions confirmed to offer a non-EU master's applicant nothing

These are useful negatives — they close off options that look plausible from outside:

- **NHH (Norway)** — states plainly that as a publicly financed institution it offers
  no scholarships or financial support to students. Non-EU fee €18,660.
- **Trinity College Dublin** — its Global Excellence Postgraduate Scholarship
  **exempts** business, engineering, natural sciences and computer science/statistics.
  Trinity's Track A programme sits in the Business School, so it is excluded.
- **Utrecht** — Bright Minds Fellowships require an EU/EEA passport.
- **Kozminski** — the 100% "Best Students" award covers only Management and Finance
  and Accounting, not the Track A Big Data Science programme.
- **Corvinus** — the full-tuition Corvinus Scholarship is limited to Management and
  Leadership, Finance and the International MBA; none of the Corvinus rows in this
  dataset qualify. Only the 10% early-bird discount applies.
- **Breda UAS** — both BUas and NL Scholarship schemes are bachelor's-only.
- **IADT** and **TU Dublin** — no institutional award for an incoming non-EU master's
  applicant.
- **ESMT Developing Country Scholarship (LDC/LLDC)** — points at the UN LDC and LLDC
  lists; **Tunisia is on neither**, so it was correctly kept out of the dataset.

## F2 (national schemes) follow-ups

| # | Item | What to verify | Why it matters |
|---|---|---|---|
| 35 | **Government of Ireland International Education Scholarship** | The HEA domicile criterion (outside EU/EEA/CH/UK) is met, but Trinity's page refers to a separate "list of eligible countries" that is not published on the HEA site. **Chase goi-ies@hea.ie directly.** | Worth €10,000 plus a full fee waiver. Recorded `unclear` — the only unresolved national scheme of real value. |
| 36 | **Camões (Portugal)** | Whether "Bolsas da Cooperação" extends beyond PALOP/Timor-Leste. No country list was reachable. | Portugal's only national route; not recorded. |
| 37 | **IKY (Greece)** | Foreign-national awards run through bilateral cultural-agreement channels that could not be opened. | Greece already yields only 2 programmes; a funding route would change its weight. |
| 38 | **Estonia** | Whether any national state scholarship for a full master's exists. `studyinestonia.ee/scholarships` returns 404. | Estonia contributes 4 Track B rows. |

### National schemes confirmed CLOSED to Tunisians — do not spend effort here

The negatives are as valuable as the positives, because several of these appear on
every "scholarships for African students" listicle:

- **Swedish Institute (SISGP)** — 34-country list. **Morocco and Egypt are in;
  Tunisia is not.**
- **Czech Government Scholarships** — 12-country list, no North Africa.
- **VLIR-UOS ICP Connect (Belgium)** — 29 countries; only Morocco and Palestine from MENA.
- **Latvian State Scholarships** — 39 bilateral-agreement countries; only Egypt from Africa.
- **Lithuanian State Scholarships** — 17 countries, Tunisia absent.
- **DAAD Study Scholarships – Master Studies for All Academic Disciplines** — Tunisia is
  absent from the country selector **even though the funding cycle starting 1 Oct 2027
  matches this applicant exactly**. F2 flags this as the highest-risk false positive in
  the set: it is the scheme everyone assumes a Tunisian can use, and they cannot.

### Schemes that exist but fund nothing this applicant needs

- **Orange Knowledge Programme (NL)** — **ended 2024**. Nuffic now runs only short
  courses, Erasmus+ and the NL Scholarship.
- **Finland — no national scheme exists at all.** Study in Finland states scholarships
  are offered by individual universities and explicitly warns against "fully funded
  Finland government scholarship" advertising. Treat any such claim as fraudulent.
- **Swiss Government Excellence Scholarships** — for Tunisia these cover **research
  fellowships and PhD only** (deadline 2026-10-13 via the Swiss Embassy in Tunis). The
  art-scholarship stream, which is the only master's-funding type, excludes Tunisia.
- **OeAD Ernst Mach (Austria)** — funds 1–9 month research stays, not degrees.
- **Slovak SAIA** — states explicitly that it does not support full-degree students.
- **MAEC-AECID África-Med (Spain)** — Tunisia is listed, but applicants must be
  permanent public employees.
- **DAAD EPOS** — Tunisia eligible, blocked by a 2-year work-experience requirement.
- **DAAD Fine Art/Design/Film** — Tunisia eligible, requires a first degree in the arts,
  which is the Track B qualification wall again.
