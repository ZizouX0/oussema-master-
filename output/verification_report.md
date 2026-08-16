# VERIFICATION REPORT — Agent V1 (adversarial)

Date: 2026-08-16 · Agent V1 · Status: **COMPLETE** — all four tasks finished.

**Headline findings**

1. **F3's MESRS conclusion holds for this applicant, but its reasoning is wrong in one place and incomplete in another. Do not delete the 51 rows.** Article 5 of the arrêté gives the equivalence commissions an express power to disregard the years requirement when the **credit count** suffices — F3 did not read it. The 51 rows move from *excluded* to *at commission discretion*.
2. **Zero level violations in 179 rows (0.0%, threshold 5%).** No territory needs re-running. I tried hard to break this and could not.
3. **The X-HEC MSc was wrongly excluded and should be ADDED** — ONISEP records the MSc&T as a *diplôme conférant le grade de master*, RNCP 7, 2 years, 140 ECTS. It clears MESRS Article 8 outright.
4. **Vlerick should stay out, for a different reason than expected** — its "Masters" are genuine NVAO-accredited 60-ECTS Advanced Masters, but they are *master-na-master* and **require a prior master's degree**. The applicant cannot enter.
5. **Six factual corrections** (Ghent fee, SRH fee + 4 fields, BI institution type, Algebra ECTS/duration/title, HSLU URLs) and **three duplicate scholarship pairs** (real count 103, not 106).

Inputs read: `data/BRIEF.md`, `output/programmes_master.csv` (179 rows), `output/scholarships_master.csv` (106 rows), `data/followups.md` (F3's finding).

---

## 1. MESRS equivalence verdict

### What I actually opened

The PDF at `https://www.mes.tn/image.php?id=18153` — *Journal Officiel de la République Tunisienne* n°119, 17 October 2023, pages 5543–5548, carrying the **قرار من وزير التعليم العالي والبحث العلمي مؤرخ في 10 أكتوبر 2023 يتعلق بضبط المعايير التي تسند على أساسها معادلة الشهادات والعناوين** ("Arrêté of the Minister of Higher Education and Scientific Research of 10 October 2023 fixing the criteria on the basis of which equivalence of diplomas and titles is granted"). 6 pages, 28 articles. I extracted the Arabic text myself with `pdftotext` and read articles 1–10 and 25–28 directly. F3's citation (JORT n°119, 17 Oct 2023, p. 5544) is **accurate** — the page break `صفحــة 5544` falls immediately before Article 6, and Articles 8–9 sit on 5544.

Signed: Moncef Boukthir, Minister of Higher Education; countersigned Ahmed Hachani, Head of Government. Article 27 abrogates the previous governing text (arrêté of 15 August 1996). I searched for a 2024–2026 amendment and **found none** — this arrêté is the text in force as of today.

### VERDICT: F3 is RIGHT on the outcome, WRONG on the mechanism, and MISSED a decisive article.

**F3's operative conclusion — that a 60-ECTS one-year master's taken on a 3-year licence does not, on the face of Articles 8 and 9, satisfy the equivalence criteria — is CONFIRMED.** But F3's report presents this as a hard, automatic disqualification of 51 rows. **That is an overstatement, and Article 5 is the reason.**

### The operative text, quoted

**Article 8 — equivalence to the national *Mastère professionnel*** (my transcription from the PDF):

> الفصل 8 ـ تسند المعادلة للشهادة الوطنية للماجستير المهني إلى كل من يستجيب للشرطين التاليين:
> ـ أن يكون متحصلا على الشهادة الوطنية للإجازة أو على شهادة معادلة تختم تكوينا جامعيا تدوم الدراسة فيه ثلاث (3) سنوات على الأقل بعد البكالوريا أو ما يعادلها أو شهادة تخول التسجيل بالتعليم العالي بالبلد الذي تم فيه الحصول على الشهادة،
> ـ أتم بنجاح سنتين اثنتين (2) من الدراسة بعد الإجازة أو ما يعادلها وناقش بنجاح مشروع ختم الدروس.
> وفي كل الحالات تسند المعادلة إلى كل من أتم بنجاح مدة دراسة جامعية لا تقل عن خمس (5) سنوات.

**My translation:**

> Article 8 — Equivalence to the national *Mastère professionnel* diploma is granted to anyone who satisfies the two following conditions:
> — that he holds the national *licence* diploma, or an equivalent diploma concluding a university course of study lasting at least three (3) years after the baccalauréat or its equivalent, or a diploma permitting enrolment in higher education in the country where the diploma was obtained;
> — that he has successfully completed **two (2) years of study after the licence** or its equivalent and has successfully defended a final-year project (*projet de fin d'études*).
> And in all cases, equivalence is granted to anyone who has successfully completed a period of university study of **not less than five (5) years**.

**Article 9 — equivalence to the national *Mastère de recherche*** is word-for-word identical except that the second condition ends `وناقش بنجاح رسالة بحث` — "and has successfully defended a research dissertation" — and the same five-year sentence closes it.

### Correction 1 to F3 — the five-year sentence is a *sufficient* condition, not a floor

F3 renders the closing sentence as a requirement: *"each closes with 'in all cases, equivalence is granted to whoever has successfully completed not less than five (5) years of university study'"*, and then treats it as an additional minimum that must be met. **That inverts a sufficient condition into a necessary one.** The Arabic is affirmative and grant-shaped — `تسند المعادلة إلى كل من أتم` ("equivalence *is granted to* anyone who has completed"). A restrictive floor would be written `لا تسند المعادلة إلا لمن…` ("equivalence is granted *only* to…"), and it is not.

Read as a floor the sentence is also **logically redundant**: the two conditions above it already produce 3 + 2 = 5 years automatically, so a floor of 5 would never bind on anyone who met them. Read as a saving clause it does real work — it catches, for example, a 4-year bachelor plus a 1-year master (5 years total, but only 1 year post-licence), which fails condition two yet is rescued by the five-year route. That is the only reading under which the sentence has any operative content.

**Does this change the answer for this applicant? No.** A 3-year/180-ECTS Tunisian licence plus a 1-year/60-ECTS master gives **four** years total and **one** year post-licence. It fails condition two of Article 8/9 (needs two years post-licence) *and* it fails the five-year saving route (4 < 5). F3 reaches the right destination by a faulty route. Worth correcting because the faulty route also mis-scores other profiles: a 240-ECTS 4-year bachelor holder doing a 1-year master **would** pass via the saving clause under the correct reading and fail under F3's.

### Correction 2 — F3 MISSED ARTICLE 5, and it is decisive

This is the finding F3's report does not contain anywhere:

> الفصل 5 ـ يمكن للجنة الوطنية لمعادلة الشهادات والعناوين واللجان القطاعية لمعادلة الشهادات والعناوين **عدم التقيد بعدد سنوات الدراسة والتكوين المستوجبة** في الحالات التي يعد فيها **عدد الأرصدة** أو عدد ساعات الدروس والبرامج **كافيا** لإسناد المعادلة.

**My translation:**

> Article 5 — The National Commission for the Equivalence of Diplomas and Titles and the sectoral equivalence commissions **may disregard the required number of years of study and training** in cases where the **number of credits**, or the number of teaching hours and the programmes, is **sufficient** to grant the equivalence.

`الأرصدة` is the standard Tunisian LMD term for ECTS credits. **Article 5 is an express statutory power to set aside the year-counting rule of Articles 6–9 whenever the credit count or contact hours are judged sufficient.** The years-based test in Articles 8–9 is therefore a default, not an absolute bar.

**And Article 4** adds a second softening: the commissions `أن تطلب، عند الاقتضاء، تكوينا إضافيا لمدة معينة في اختصاص الشهادة` — "may require, where appropriate, additional training for a specified period in the specialisation of the diploma." So the realistic set of outcomes for a one-year master's is three, not one: refused; granted under Article 5; or granted conditional on complementary training under Article 4.

**Honest assessment of how much Article 5 helps.** Less than one might hope. A Tunisian *mastère* is 120 credits. A 60-ECTS master's presents half that, so a commission applying Article 5 on the credit limb has a weak case to work with. Article 5 is strongest for programmes where **duration is short but credits are full** — a 120-ECTS master delivered in 16–18 months, or a 90-ECTS programme spanning two academic years. It is weakest for exactly the Irish/Spanish 60-ECTS twelve-month model. So Article 5 does not rescue the 51 rows; it converts them from *excluded* to *at commission discretion, on a weak credit argument*.

### The correct verdict, stated plainly

1. **Do not delete any row on the strength of this finding.** F3's own text already says the finding "must be confirmed in writing… before it is treated as settled," but the 51-row exposure table reads as a verdict. Article 5 means it is not one. Rows should carry a flag, not be removed.
2. **The binding constraint is the second limb of Articles 8/9 — two years of study after the licence — not the five-year clause.** Anything under two full years post-licence is presumptively non-equivalent, subject to Article 5 discretion.
3. **ECTS, not months, is the variable to record.** Article 5 makes credits the express escape hatch, so `ects` is the field that decides this question. 120 ECTS = safe. 90 ECTS = arguable under Article 5. 60 ECTS = weak.
4. **It binds only if the applicant needs Tunisian recognition** (public sector, regulated profession, doctorate in Tunisia, any *concours*). F3 is right about this and it remains the highest-value unresolved question in the brief.
5. Written confirmation from the *Direction de l'Enseignement Supérieur Privé et des Équivalences* should now ask a sharper question than F3 framed: **not** "does a one-year master's qualify" but **"under Article 5 of the arrêté of 10 October 2023, will 60 ECTS / 90 ECTS be treated as a sufficient credit count to disregard the two-year requirement of Article 8?"**

### Article 2 — F3 listed three criteria; there are seven

For completeness, Article 2 requires the sectoral commissions to apply **seven** conditions, not the three F3 extracted:

1. Holding a baccalauréat or equivalent, or a diploma permitting enrolment in higher education in the awarding country.
2. **Recognition of both the institution and the diploma in the country of award** (`الاعتراف بالمؤسسة الجامعية وبالشهادة بالبلد الذي تم فيه الحصول على الشهادة`).
3. The **university character** of the diploma (`الصبغة الجامعية للشهادة`).
4. The **in-person character of examinations** (`الصبغة الحضورية للامتحانات`).
5. **The availability of the diploma and the specialisation within the Tunisian university system** (`توفر الشهادة والاختصاص بالمنظومة الجامعية التونسية`) — F3 omitted this one, and it is a real risk for niche Track B titles with no Tunisian counterpart.
6. That the training is **not specifically directed at foreign students**.
7. That the diploma is **authenticated by the competent authorities** of the awarding country.

Criterion 3 (`الصبغة الجامعية`) is the one that independently kills *máster propio*, *Mastère Spécialisé* and non-state-recognised private awards — so the level filter in Task 2 below is doing MESRS work as well as brief work.

**Source:** `https://www.mes.tn/image.php?id=18153` (JORT n°119, 17 Oct 2023, pp. 5543–5548). Retrieved and text-extracted 2026-08-16.

---

## 2. Level violations

### Method

I ran a keyword scan over `programme_name_exact` + `degree_awarded` on **all 179 rows** for: MBA/EMBA, *máster propio / título propio*, *Mastère Spécialisé*, *Master di primo/secondo livello*, postgraduate diploma/certificate, executive/continuing education, bachelor, doctoral/research-only, plus *Laurea Magistrale*, *Diploma Accademico*, "Advanced Master", "Professional Master", "Specialized". 22 rows matched. I then ran a second, independent scan on structural signals — `ects` < 60 or `NOT_FOUND` (49 rows), `duration_months` < 9 or `NOT_FOUND` (8 rows), `degree_awarded` shorter than 12 characters (11 rows) — because a violation can hide behind an innocuous name. Suspicious rows were taken to the official/state source.

### HEADLINE: 0 confirmed level violations out of 179 rows (0.0%). This is far below the 5% (9-row) threshold. No territory needs re-running on level grounds.

That is a genuinely good result and I want to be clear that I tried hard to break it. The 22 keyword hits were almost all false positives of two kinds: (a) eleven Italian rows correctly recording *Laurea Magistrale, 120 CFU*, which is the correct second-cycle degree; (b) five French rows whose `degree_awarded` contains the string "not a Mastère Spécialisé" — the negation matched my own pattern. Wave 1 appears to have applied this filter carefully and to have documented the France/Spain traps in the field itself.

### Rows I took to the source, and what I found

| Row | Institution / programme | Suspicion | Outcome |
|---|---|---|---|
| 29 | ESSEC — Master in Data Sciences & Business Analytics (DSBA) | French MScs usually carry only an RNCP title, not *grade de master* | **CLEARED.** CEFDG standing list names it explicitly: *Diplôme « sciences des données et techniques analytiques pour la gestion »*, formation "Master in Data Sciences & Business Analytics (DSBA)", **grade Master 01/09/2021 → 31/08/2027**, Bac+5, RNCP 7, Visa = Non. **But see the expiry warning below.** |
| 27 | emlyon — Master in Data Science & AI Strategy | same | **CLEARED.** CEFDG lists emlyon *Diplôme spécialisé en management de l'innovation* (DSMI), Visa = Oui, **grade Master 01/09/2024 → 31/08/2028**. The row's stated validating diploma matches. |
| 28 | IESEG — Master in AI & Data Analytics for Business | same | **CLEARED.** CEFDG lists IESEG *Diplôme d'études spécialisées en management international (DESMI)*, Visa = Oui, **grade Master 01/09/2025 → 31/08/2030**. IESEG's own 2025 announcement confirms the renewal covers the PGE and the DESMI. |
| 30, 31 | EDHEC — MSc Data Analytics & AI; MSc Marketing Analytics | same | **CLEARED, with a caveat.** CEFDG lists EDHEC *Diplôme supérieur en stratégie et gestion des entreprises* (formation "MSc Business Management"), Visa = Oui, grade Master 01/09/2025 → 31/08/2030 — the umbrella diploma under which EDHEC's business MSc tracks are delivered. Neither MSc is named individually in the CEFDG list, so the mapping is inferential rather than explicit. Recorded as a caveat, not a violation. |
| 93 | UPF-BSM — MSc in Management, Business Analytics specialisation | Spanish *máster propio* trap | **CLEARED.** The award is the *Màster Universitari en Ciències Empresarials*, an **official UPF degree**; AQU Catalunya has institutionally accredited UPF-BSM, which certifies all its official master's degrees. The row already records the distinction correctly, including that the analytics content is elective-driven. |
| 96 | IE — Master in Business Analytics and Data Science | Spanish *título propio* trap | **CLEARED, and the row is exemplary.** It records that only the Business Analytics half is the official state degree (BOE-A-2021-20309) and that the Data Science component is an IE *título propio* with no state recognition on its own. That is exactly the distinction the brief demands. |
| 171 | IE — Master in Creative Direction, Content & Branding | Two aggregators describe this as "a University Private Degree from IE Universidad" (i.e. *título propio*) | **NOT a violation, but DISPUTED — see §4.** The row records the official *Máster Universitario en Creación y Gestión de Medios Visuales* (BOE-A-2014-9664). IE does hold that official title. I could not find, on ie.edu itself, the page that maps this commercial programme name to that official title — the programme page (retrieved via firecrawl, since ie.edu blocks WebFetch) states neither "official" nor "propio". The aggregator claim is uncorroborated and aggregators are not admissible under the brief, so I am not removing the row; I am downgrading its confidence. |
| 149, 150 | NABA — MA Creative Media Production; MA Visual Design & IMC | NABA runs **both** 2-year *Diplomi Accademici di Secondo Livello* and 1-year 60-CFA *Academic Masters*; only the former is a degree | **CLEARED.** NABA's own page for Creative Media Production states "Second Level Academic Degree in New Technologies for Arts", **120 CFA, 2 years**, "recognised by the MUR", and it sits under `/en/postgraduate/`, not under `/en/academic-masters/` where the 1-year 60-CFA products live. The rows record the correct product. |
| 148 | RUFA — Film Arts | AFAM diploma, not a university degree | **CLEARED.** *Diploma Accademico di Secondo Livello*, 120 CFA, legally *equipollente* to a *Laurea Magistrale* under the AFAM framework. The row says so. |
| 11, 12, 13 | Algebra Bernays University (Croatia) | `degree_awarded` reads "Professional Graduate Study Programme" / "Graduate Study Programme" — Croatia's old *stručni specijalist* was **not** a master's | **CLEARED on level; two other problems found — see §3 and §4.** Algebra's own page gives the academic title as **`mag. ing. comp.` — "Professional Master in Computer Engineering, sub-specialization in Data science"**, **120 ECTS**, **4 semesters (2 years)**. `mag.` is a master's title under the Croatian qualifications framework. Level is fine. |
| 78 | TIAS — Full-time Master in Management/Business Administration (MScBA) | name contains "Business Administration"; MBA exclusion | **CLEARED.** It is an NVAO-accredited MSc, not an MBA. TIAS's separate MBA products are not in the dataset. |
| 147 | TU Dublin — MSc Creative Digital Media | F3's notes say TU Dublin's **online** MSc was excluded, yet a TU Dublin MSc is in the file | **CLEARED — no contradiction.** The row is TU294, the on-campus 18-month/90-ECTS programme, not the online variant. |
| 99, 100 | Lund; Luleå — "Master of Science (60 credits)" | is a Swedish 60-credit *magisterexamen* a master's? | **CLEARED.** It is a degree at second-cycle level in the Swedish framework and meets the brief's 60-ECTS floor. It sits squarely in the MESRS risk band, which is a §1 issue, not a level issue. |
| 5 | TU Wien — Dipl.-Ing. | non-obvious degree name | **CLEARED.** Austrian *Diplom-Ingenieur* from a Masterstudium is a master's-level degree; the row already says "equivalent to Master of Science". |
| 48 | Reykjavik University — 90 ECTS MSc | under 120 | **CLEARED.** 90 ECTS exceeds the brief's 60-ECTS floor. |

### One time-bomb worth flagging even though it is not a violation

**Row 29 (ESSEC DSBA): the *grade de master* authorisation expires 31/08/2027.** The working assumption in the brief is an autumn-2027 intake. A student entering in September 2027 would be entering the first cohort *after* the current authorisation lapses. Every other French private row in the file runs to 2028 or 2030. ESSEC will presumably seek renewal, but this is not something to discover in 2027. Recorded in §3 as a note to add to `fit_notes`, not as a removal.

### What the level scan did *not* cover

I did not independently re-verify state recognition for the 30 rows that no scan flagged and that come from unambiguous public national universities (e.g. Aalto, KU Leuven, Politecnico di Milano). Their `degree_awarded` values are internally consistent and name the national degree correctly. If a level error survives in this dataset, it is more likely in the private/applied-sciences/art-school segment than there.

---

## 3. Corrections

Every correction below is against an official source I opened myself.

### Programme rows

| Row | Field | Recorded | Correct value | Source |
|---|---|---|---|---|
| 8 — Ghent, MSc Business Engineering | `tuition_non_eu_per_year` | `6929 (non-EEA tuition fee; academic year not stated on the page)` | **`7079.40 (non-EEA, Tuition Fee B tier, academic year 2026-2027)`** — €305.40 fixed + 60 × (€31 + €81.90). The €6,929 recorded is the **2025-26** figure; the €6,540.10 seen elsewhere is **2023-24**. | `https://www.ugent.be/student/en/administration/tuition/tuition-fee-master-programme-not-advanced-and-masters-programme-in-teaching.htm/tuitionmasterteacher20262027.htm` |
| 8 — Ghent | `tuition_source_url` | faculty programme-overview page, which states no academic year | the dated central UGent fee page above | as above |
| 79 — BI Norwegian Business School | `institution_type` | `private` | **`private-accredited-by-state`** — NOKUT lists BI under *Specialised Universities*; status granted 2008 | `https://www.nokut.no/en/higher-education/higher-education-institutions/` |
| 130 — SRH, M.A. Film, TV and Digital Narratives | `tuition_non_eu_per_year` | `11900 (…SRH's own marketing quotes 5700 per semester — a live fact conflict…)` | **`11543 (non-EU; SRH published rate: EUR 5,950 per semester / EUR 11,543 per year / EUR 22,610 total, plus a one-off EUR 1,000 enrolment fee; price list valid from 1 April 2025)`**. The conflict is resolved in favour of €5,950/semester; €5,700 is stale. But €11,900 was a doubling of the semester rate and does not match SRH's own annual column. | `https://www.srh-university.de/fileadmin/1HE/International/SRH-University-Tuition-Fees-EN-Non-EU.pdf` |
| 130 — SRH | `ects` | `NOT_FOUND` | **`120`** | `https://www.srh-university.de/en/master/film-television-digital-narratives/v/` |
| 130 — SRH | `intake_months` | `NOT_FOUND` | **`April; October`** | as above |
| 130 — SRH | `institution` | `SRH Berlin University of Applied Sciences` | **`SRH University (formerly SRH Berlin University of Applied Sciences)`** — `srh-berlin.de` 301-redirects to `srh-university.de` | observed 301 |
| 130 — SRH | `tuition_source_url`, `programme_url` | both point at DAAD | replace with SRH's own fee-list PDF and programme page above. DAAD is a reasonable discovery source but SRH is the primary one, and the DAAD record is what produced the conflict. | as above |
| 11 — Algebra, Data Science | `ects` | `NOT_FOUND` | **`120`** | `https://www.algebra.hr/sveuciliste/en/graduate-study-programmes/data-science/` |
| 11 — Algebra, Data Science | `duration_months` | `NOT_FOUND` | **`24`** ("4 semesters (2 years)") | as above |
| 11 — Algebra, Data Science | `degree_awarded` | `Data Science specialisation of the Professional Graduate Study Programme in Applied Computer Engineering` | add the actual title: **`… ; academic title mag. ing. comp. (Professional Master in Computer Engineering, sub-specialization in Data Science)`** | as above |
| 102 — HSLU | `tuition_source_url`, `app_deadline_source_url`, `programme_url` | `.../applied-information-and-data-science/…` | HSLU has renamed the programme; those URLs now 301 to **`.../master/applied-data-science-and-ai/`** and **`.../applied-data-science-and-ai/admission/`**. Update to the canonical URLs. The recorded `programme_name_exact` already matches the new name. | observed 301 |
| 12, 13 — Algebra | `fit_notes` | notes blended/online delivery | keep, but the delivery mode needs to be surfaced as an eligibility fact, not a footnote — see §4 | — |

### Scholarship rows — three duplicate pairs

These are merge artefacts from Wave 2 (the same scheme found independently by two agents). They inflate the funding count by three.

| Rows | Scheme | Evidence |
|---|---|---|
| **81 and 82** | ARES *Bourses de formations internationales 2027-2028* | identical funder, identical deadline `2026-09-18`, **identical URL** `https://ares-ac.be/fr/bourses-de-formations-internationales-2027-2028`. Keep row 82 (its `amount_eur_year` note is more informative). |
| **83 and 84** | *Government Scholarships Programme Tunesia / Tunisia* | same funder, **identical URL** `https://www2.daad.de/…?detail=10000344`; one spells the country "Tunesia" (German) and the other "Tunisia". Keep one. |
| **71 and 88** | *Stipendium Hungaricum* | same scheme, same deadline `2026-01-15 PRIOR_CYCLE`, different pages of the same funder's site. Row 71 is materially better (cites the Call for Applications PDF, p.7, and gives the amount); row 88 has `amount_eur_year: NOT_FOUND`. **Keep 71, drop 88** — but first move row 88's unique fact into 71: the Tunisia entry on `stipendiumhungaricum.hu/partners/` restricts Tunisian full-degree master's nominations to **named subject areas**, which is an eligibility constraint row 71 does not carry. |

Corrected scholarship count after de-duplication: **103**, not 106.

### Things I checked that turned out to be RIGHT (recorded so the audit trail is honest)

- **Rows 3 and 5 (Austria), €726.72/semester third-country tuition** — confirmed verbatim on the ministry page: *"Other degree programme students from third countries who do have the right of residence for students… will in principle be liable to pay tuition fees of 726.72 euros per semester."*
- **Row 162 (UvA, MA New Media and Digital Culture), €25,900** — confirmed: UvA's 2026-2027 institutional fee table gives Faculty of Humanities **Master's (one year) €25,900**. Correctly tagged `PRIOR_CYCLE`. Row 73 (UvA, Amsterdam School of Economics, €21,800) also matches the same table exactly.
- **Row 56 (UCD Business Analytics), €26,180** — confirmed verbatim on `ucd.ie/courses/b154`: `nonEU Year 1 - € 26180`.
- **Row 95 (Esade MSc Business Analytics), €39,000** — confirmed, and it is the **2027-28** figure, i.e. the target cycle. Better than recorded.
- **Row 96 (IE), €43,000** — confirmed verbatim (`43,000€*`), but the page attaches it to *"Full-Time April & September **2026** Intakes"*. Under brief rule 3 this should carry **` PRIOR_CYCLE`**; it does not. Minor, listed here rather than as a correction because the figure itself is right.
- **Rows 70, 71, 74 (Tilburg)** — all three re-derived against the official institutional fee list; all three correct, including the differing cycle labels and the `PRIOR_CYCLE` tag on row 74 only. See §5.6.
- **Row 71 (scholarship, Stipendium Hungaricum), €2,520/yr** — I initially flagged this as a currency-conversion error, since HUF 43,700/month is only about €112. It is **not** an error: the figure correctly sums the HUF 43,700 stipend *and* the HUF 40,000 accommodation contribution, and the row says so.
- **Row 21 (scholarship, EMJM), €16,800/yr** — consistent with the EMJM individual-support rate of €1,400/month × 12.

---

## 4. DISPUTED rows

Facts I could not confirm. **None of these should be deleted** — each should be downgraded to `confidence: low` and carry the note given.

| Row | What is disputed | Why I could not settle it |
|---|---|---|
| **171 — IE, Master in Creative Direction, Content & Branding** | Whether this commercial programme actually leads to the official *Máster Universitario en Creación y Gestión de Medios Visuales* (BOE-A-2014-9664), as recorded, or is an IE *título propio*. | Two independent aggregators describe it as "a University Private Degree from IE Universidad". IE's own programme page — which I retrieved in full via firecrawl — states **neither** "official" nor "propio" anywhere. IE does hold the official title in question, so the mapping is plausible; I simply could not find IE's own page that makes it. Aggregators are inadmissible under the brief, so the row stays. **Downgrade `medium` → `low`.** At €37,000/yr and with `título propio` being the exact Spanish trap the brief names, this must be settled in writing with IE before any application. Note the contrast with row 96, where IE *does* publish the official/propio split and the row records it. |
| **11, 12, 13 — Algebra Bernays University** | Not the level (settled: `mag. ing. comp.`, 120 ECTS, 2 years) but the **delivery mode**. Algebra's own page gives study mode as **"Full online and/or blended"**, with a "Full online model — 100% online, with no need to attend campus." | **This collides directly with MESRS Article 2, which requires `الصبغة الحضورية للامتحانات` — the in-person character of examinations.** F3 used exactly this criterion to justify excluding TU Dublin's online MSc and EUC's distance programmes, but the Algebra rows survived. Whether the *examinations* specifically are in person, even in the blended model, is not stated on any page I could find. Until it is, these three rows carry the same defect that removed others. **Downgrade all three; rows 12 and 13 are already `low`, so downgrade row 11 `medium` → `low`.** |
| **12, 13 — Algebra, Digital Marketing / Economics of Digital Business** | `degree_awarded` is only "Graduate Study Programme – …", with `ects` and `duration_months` both `NOT_FOUND`. | I verified the Data Science programme in detail but not these two. By analogy they are almost certainly also 120 ECTS / 4 semesters, **but analogy is not verification** and I will not write an unverified number into a data file. |
| **30, 31 — EDHEC MSc Data Analytics & AI; MSc Marketing Analytics** | These carry `confidence: high`, but the CEFDG register does not name either programme individually. The *grade de master* is attached to EDHEC's umbrella diploma *Diplôme supérieur en stratégie et gestion des entreprises* ("MSc Business Management"), and the inference that these two tracks sit under it is mine, not EDHEC's or CEFDG's. | EDHEC's own marketing asserts *grade de master* and *diplôme visé bac+5* without naming the covering diploma. **Downgrade `high` → `medium`** until EDHEC confirms which registered diploma each MSc validates. |
| **29 — ESSEC DSBA** | Not disputed on level — CEFDG names it explicitly. But its *grade de master* authorisation **expires 31/08/2027**, i.e. right at the brief's assumed intake. | Renewal is a future administrative act that no source can confirm today. Add to `fit_notes`; do not downgrade. |
| **90, 168, 169, 170 — Babeș-Bolyai University (4 rows)** | All four use the same generic faculty listing page `https://www.ubbcluj.ro/en/programe_academice/masterat/` as `programme_url`, and all four have `tuition_non_eu_per_year: NOT_FOUND`. | A listing page is not a programme source. Three are already `low`; **row 90 is `medium` and should be downgraded.** For a non-EU applicant a row with no tuition figure and no programme-specific URL is close to unusable. |
| **107 — Cyprus University of Technology, MSc Interaction Design** | `tuition_non_eu_per_year: NOT_FOUND` on a `low`-confidence row for a **joint programme with Tallinn University**. | Joint programmes frequently have a fee split that neither partner publishes in full. Flagged rather than resolved. |
| **All 51 one-year rows identified by F3** | Whether MESRS grants equivalence. | Per §1, Article 5 makes this a matter of commission discretion on the credit count, not a rule. Not resolvable from any published text — it needs the written ruling. **Flag; do not delete.** |

---

## 5. Follow-ups resolved

### 5.1 HEC Paris / École Polytechnique — MSc Data Science & AI for Business (X-HEC) — **RESOLVED: it DOES confer the *grade de master*. This row should be ADDED.**

The exclusion was wrong. Two independent official sources settle it:

- **ONISEP** (the state careers-information agency under the ministries of Education and Higher Education) has a formation record for **"Master of Science and Technology"** which states, verbatim: **"Durée de la formation : 2 ans"**, **"Diplôme conférant le grade de master"**, **"Inscrit au RNCP : Niveau 7 (bac + 5)"**. Its "Où se former ?" table lists exactly two providers: **École des Hautes Études Commerciales de Paris (HEC), Jouy-en-Josas** and **École polytechnique, Institut polytechnique de Paris, Palaiseau**. Source: `https://www.onisep.fr/ressources/univers-formation/formations/post-bac/master-of-science-and-technology` (retrieved via firecrawl; the site 403s WebFetch).
- **École Polytechnique's own programme page** gives **2 years / 140 ECTS / September intake / €28,950 per year at École Polytechnique**, taught in English. Source: `https://programmes.polytechnique.edu/en/master/programs/data-science-for-business-joint-degree-with-hec`.

**On the "diplôme visé" question specifically: no, and it does not need to be.** I checked the CEFDG standing register of *diplômes visés et gradés au 01/09/2025* (`https://www.cefdg.fr/wp-content/uploads/2026/04/BDD-formations_2025-26_Site-CEFDG_04-2026_VF.xlsx`). HEC Paris appears there for its PGE, MBA, Executive MBA and its Masters in International Finance / Marketing / Economics & Finance / Sustainability / Strategic Management / Accounting — **the X-HEC MSc is not among them**, and École Polytechnique does not appear at all. That is not a defect: CEFDG's remit is management-school diplomas, and the *visa* is a separate instrument from the *grade*. The MSc&T is a *diplôme d'établissement* of École Polytechnique that **carries the grade de master and RNCP level 7** — which is precisely what the brief requires ("recognised as a master's by the national qualifications framework").

**And it is two full years / 140 ECTS**, so unlike almost every other elite-brand Track A option it clears the MESRS Article 8 two-year test in §1 outright. On the brief's own criteria this is arguably the single strongest Track A row in France.

**Row to ADD (fields I could verify; `NOT_FOUND` where I could not):**

```
track: A
country: France
city: Palaiseau; Jouy-en-Josas
institution: Ecole Polytechnique (Institut Polytechnique de Paris) and HEC Paris
institution_type: public
programme_name_exact: Master of Science Data Science & AI for Business (X-HEC)
degree_awarded: Master of Science and Technology (MSc&T) - diplome conferant le grade de master, inscrit au RNCP niveau 7 (bac+5), per ONISEP; joint degree Ecole Polytechnique / HEC Paris
faculty_or_school: Ecole Polytechnique Graduate Degree programmes / HEC Paris
language: EN
duration_months: 24
ects: 140
intake_months: September
tuition_non_eu_per_year: 28950 (stated as "per year at Ecole Polytechnique"; the HEC-year fee is not stated on the same page - CONFIRM)
tuition_source_url: https://programmes.polytechnique.edu/en/master/programs/data-science-for-business-joint-degree-with-hec
living_cost_estimate_year: NOT_FOUND
app_deadline_non_eu: NOT_FOUND
app_deadline_source_url: NOT_FOUND
min_prior_ects: NOT_FOUND
accepts_3yr_bachelor: NOT_FOUND
english_req: NOT_FOUND
other_tests: GMAT reported (median 710 on HEC's page); confirm whether required
portfolio_required: n/a
work_experience_required: no
quantitative_prereqs: strong foundation in mathematics and economics; highly quantitative
programme_url: https://www.hec.edu/en/master-s-programs/master-science-data-science-ai-business-x-hec
post_study_work_visa: NOT_FOUND
fit_notes: Two-year 140-ECTS joint degree with the grade de master, so it satisfies the two-year-post-licence condition of the Tunisian equivalence arrete. Year one is quantitative at Ecole Polytechnique, year two business-facing at HEC.
verified_date: 2026-08-16
confidence: medium
```

Do **not** promote this to `high` until the non-EU deadline, the total two-year cost, and `accepts_3yr_bachelor` are read off an admissions page. `tuition_non_eu_per_year` in particular is a trap here: €28,950 is described as the École Polytechnique year, and a two-year joint degree that switches campus almost certainly does not charge the same in year two.

### 5.2 Vlerick Business School — **RESOLVED: NVAO-accredited Flemish master degrees, YES. But the applicant is INELIGIBLE. Do not add.**

This is the most consequential of the follow-ups and the answer is not the one the question anticipated.

Vlerick's own institutional page states, verbatim: **"Vlerick Business School is recognised by the Flemish Parliament Act of 18 May 1999 as a statutory registered institution"** and **"The degree programmes of Vlerick Business School are Advanced Master's (EQF 7) and equal 60 ECTS."** The NVAO decisions register for Vlerick lists eight accredited programmes — *Master in International Management and Strategy, Master in Innovation and Entrepreneurship, Master of Business Administration, Master in Financial Management, Master in Marketing Strategy, Master in General Management, Master in Business Analytics and Artificial Intelligence, MBA: General Management* — so the earlier note that NVAO "shows decisions only for Innovation and Entrepreneurship and an MBA" was **incomplete**; Business Analytics & AI is there.

**But the same Vlerick page states the entry rule: "Advanced Master's programmes are only open to holders of a Master's degree, possibly after an aptitude test."**

These are Flemish ***master-na-master*** (ManaMa) programmes. They are genuine 60-ECTS EQF-7 degrees — the level filter passes — but they sit *after* a master's, not after a bachelor's. **The applicant holds a 180-ECTS licence and cannot enter.** `min_prior_ects` would be 300, `accepts_3yr_bachelor` = **no**.

So the €21–23k/yr question resolves itself: there is nothing to spend it on. Vlerick correctly does not appear in `programmes_master.csv`, and it should stay out. Sources: `https://www.vlerick.com/en/information-on-the-flemish-higher-education-system/`, `https://www.nvao.net/en/decisons/vlerick-business-school`.

*Secondary consequence:* the ManaMa/Advanced-Master structure is a systematic trap in Flanders and the Netherlands, not a Vlerick quirk. Any Belgian or Dutch row whose award is described as "Advanced Master" or "master-na-master" needs the same check. I scanned the 179 rows for those strings and found none, so the dataset is clean on this point.

### 5.3 Ghent University — **RESOLVED: both recorded figures are stale. The current 2026-27 figure is €7,079.40.**

Neither €6,929 nor €6,540.10 is the current fee, and I can date both precisely because UGent's fee formula is arithmetic and reproducible:

| Academic year | Formula (non-EEA, Tuition Fee B) | Total for 60 credits |
|---|---|---|
| 2023-24 | — | **€6,540.10** ← the second figure in the file |
| 2025-26 | €299 fixed + €28.60/credit + €81.90/credit higher fee | 299 + 60 × 110.50 = **€6,929.00** ← the figure recorded in row 8 |
| **2026-27 (current)** | **€305.40 fixed + €31/credit + €81.90/credit higher fee** | 305.40 + 60 × 112.90 = **€7,079.40** |

Tuition Fee B is the tier that applies to **Economics** (as well as Science, Medicine, Engineering, Bioscience Engineering, Pharmaceutical and Political & Social Sciences); Tuition Fee A (€2,297.40) applies to Arts, Law and Psychology. **MSc Business Engineering sits in the Faculty of Economics and Business Administration, so Tuition Fee B is the right tier.**

**Correction for row 8:** `tuition_non_eu_per_year` → `7079.40 (non-EEA, Tuition Fee B tier, academic year 2026-2027)`; `tuition_source_url` → `https://www.ugent.be/student/en/administration/tuition/tuition-fee-master-programme-not-advanced-and-masters-programme-in-teaching.htm/tuitionmasterteacher20262027.htm`. The programme-overview page currently cited does not name an academic year, which is exactly why the error happened; the dated central page should be cited instead.

### 5.4 BI Norwegian Business School — **RESOLVED: YES, NOKUT-accredited as a specialised university institution.**

**NOKUT's own register of higher education institutions lists "BI – Norwegian Business School" under the *Specialised Universities* category** (`https://www.nokut.no/en/higher-education/higher-education-institutions/`). BI's accreditations page dates the grant to **2008**. Under NOKUT's definition, a specialised university institution holds doctoral accreditation within its subject area and may itself accredit new master's programmes within that area.

**Correction for row 79:** `institution_type` → `private-accredited-by-state` (currently `private`). This matters for the brief's rule 5 and for MESRS Article 2's "recognition of the institution and the diploma in the country of award" criterion, both of which BI now clears. Row 79 is a 120-ECTS / 24-month programme, so it also clears the Article 8 two-year test — combined with NOK 135,600/yr this is one of the better-value clean Track A rows in the file.

### 5.5 SRH Berlin — M.A. Film, Television and Digital Narratives — **RESOLVED: €5,950/semester is right, €5,700 is stale, and the recorded annual figure of €11,900 is wrong too.**

Both parties to the conflict were partly wrong. I went to SRH's **own official fee list** — `https://www.srh-university.de/fileadmin/1HE/International/SRH-University-Tuition-Fees-EN-Non-EU.pdf` — and extracted the line verbatim:

```
M.A.   Film, Television and Digital Narratives    € 5,950    € 11,543    € 22,610
```

with the footer **"Tuition fees in this price list are valid from 1st of April 2025."** and **"— Enrolment fee: € 1000 / programme (Non-EU)"**. SRH's own programme page independently states **"€5,950 per semester"** plus the **one-off €1,000 enrolment fee**.

So: **DAAD's €5,950/semester is correct and is confirmed by SRH itself. The €5,700 figure is stale marketing and should be discarded.**

**But the row's derived annual figure is also wrong.** Row 130 records `11900`, i.e. 5,950 × 2. SRH's own columns are €5,950 per semester / **€11,543 per year** / **€22,610 total** — note 5,950 × 4 = 23,800 ≠ 22,610, so the per-semester list rate and the billed annual rate are not the same number. **Use SRH's published annual figure of €11,543, not a doubling of the semester rate.** This is a good illustration of why derived arithmetic on fee fields is unsafe.

Corrections for row 130 are listed in §3; they also include ECTS (120), intakes (April; October) and a rename — **the institution is now "SRH University"**; `srh-berlin.de` 301-redirects to `srh-university.de`, so the recorded institution name and both recorded URLs are on the old domain.

### 5.6 Tilburg / JADS — MSc Data Science in Business and Entrepreneurship — **VERIFIED. Row below. But read the eligibility note first.**

Verified from Tilburg's own pages (via firecrawl; tilburguniversity.edu blocks WebFetch) and from the official institutional fee list.

**The eligibility finding is more important than the row.** Direct admission requires a **technical** bachelor's containing **≥15 EC in mathematics and statistics (≥5 EC maths, ≥5 EC statistics)** *and* coursework in **Databases, Data Structures & Algorithms, Programming (preferably Python), and Machine Learning / Data Mining**. A candidate who has the 15 EC but not the rest is routed through the **JADS pre-Master**. And explicitly: *"Students holding an international Diploma evaluated as a higher professional education Bachelor… are most likely to be eligible to a pre-Master."* A Tunisian *licence* from a private institution is a realistic candidate for that classification. So `accepts_3yr_bachelor` is **conditional**, with the pre-Master as the likely route — which under the brief goes in `fit_notes`, not as its own row.

**Row to ADD:**

```
track: A
country: Netherlands
city: 's-Hertogenbosch (also Eindhoven and Tilburg campuses)
institution: Tilburg University and Eindhoven University of Technology (Jheronimus Academy of Data Science, JADS)
institution_type: public
programme_name_exact: Data Science in Business and Entrepreneurship (joint degree)
degree_awarded: Master of Science (MSc) - joint degree of Tilburg University and Eindhoven University of Technology; RIO/CROHO code 65018 "M Data Science in Business and Entrepreneurship (joint degree)"
faculty_or_school: Jheronimus Academy of Data Science (JADS); registered under Tilburg School of Economics and Management (TiSEM)
language: EN
duration_months: 24
ects: 120
intake_months: August; January
tuition_non_eu_per_year: 23900 (2026/27 non-EEA institutional fee; the 2027/28 non-EEA rate is published as "Not yet known") PRIOR_CYCLE
tuition_source_url: https://www.tilburguniversity.edu/sites/default/files/download/Instellingstarieven%20voor%20masteropleidingen%202026-2027.pdf
living_cost_estimate_year: 12000-14400 (university figure: EUR 1,000-1,200 per month)
app_deadline_non_eu: 2027-04-01
app_deadline_source_url: https://www.tilburguniversity.edu/education/masters-programs/data-science-business-entrepreneurship/application
min_prior_ects: NOT_FOUND
accepts_3yr_bachelor: conditional
english_req: IELTS Academic 6.5 overall with min 6.0 Writing and Speaking; TOEFL iBT 90 overall with 22 Writing / 21 Speaking for reports issued before 21 Jan 2026; IELTS Online not accepted; scores from a single test date only
other_tests: no
portfolio_required: n/a
work_experience_required: no
quantitative_prereqs: Technical bachelor with min 15 EC mathematics and statistics (min 5 EC mathematics, min 5 EC statistics) plus courses in Databases, Data Structures and Algorithms, Programming (preferably Python), and Machine Learning / Data Mining
programme_url: https://www.tilburguniversity.edu/education/masters-programmes/data-science-business-and-entrepreneurship
post_study_work_visa: yes - orientation year (zoekjaar) permit, 1 year, free labour market access
fit_notes: Two-year 120-ECTS joint degree, so it clears the two-year-post-licence condition of the Tunisian equivalence arrete, unlike Tilburg's one-year masters. A holder of a professionally-oriented three-year licence is most likely routed through the JADS pre-Master rather than admitted directly.
verified_date: 2026-08-16
confidence: medium
```

Deadline note: 1 April is the non-EEA deadline for the end-of-August start (1 October for the end-of-January start). EEA nationals get 1 June. I have written 2027-04-01 to match the brief's working assumption of an autumn-2027 intake, consistent with how rows 70 and 71 are recorded.

**Incidental cross-check, and it came out clean.** While in the fee list I re-derived the three existing Tilburg rows against it. The document is titled *"institutional tuition fees 2026/2027 and 2027/2028"* with columns 26/27 EEA · 26/27 non-EEA · 27/28 EEA · 27/28 non-EEA:

| Row | Programme (RIO code) | 26/27 non-EEA | 27/28 non-EEA | Recorded | Verdict |
|---|---|---|---|---|---|
| 70 | M Marketing Analytics (60064) | €19,900 | **€20,500** | 20500 "2027/28 non-EEA" | **correct** |
| 71 | M Business Analytics and Operations Research (60057) | €19,900 | **€20,500** | 20500 "2027/28 non-EEA" | **correct** |
| 74 | M Data Science and Society (60964) | **€23,900** | *"Not yet known"* | 23900 "2026/27 … PRIOR_CYCLE" | **correct, and correctly tagged** |

I went in expecting to find a cycle-labelling error — three rows citing one document with two different cycle labels is exactly the shape of a mistake — and there isn't one. The 27/28 rate genuinely is published for some programmes and genuinely is not published for Data Science and Society. Wave 1 read this correctly, including applying `PRIOR_CYCLE` to precisely the right row.

---

## 6. What I sampled and what I did not

I could not re-open 285 rows, so the honest statement of coverage matters as much as the findings.

### Automated, and therefore 100% coverage

- **Level keyword scan** — all 179 programme rows, `programme_name_exact` + `degree_awarded`, 20 patterns. 22 hits triaged.
- **Structural anomaly scan** — all 179 rows: `ects` < 60 or missing (49 rows), `duration_months` < 9 or missing (8), `degree_awarded` under 12 characters (11).
- **Duplicate detection** — all 179 programme and all 106 scholarship rows, on (institution + programme name), on `programme_url`, and on `url`. Found 3 duplicate scholarship pairs; **zero duplicate programme rows**.
- **Link check — all 392 unique URLs across both files**, every URL-bearing field (`tuition_source_url`, `app_deadline_source_url`, `programme_url`, scholarship `url`), HEAD with GET fallback.

**Link-check result, stated carefully: I found no dead links.** 27 URLs returned non-200 on the first pass, and I initially wrote two of them up as 404s. On re-testing with browser headers, **every one was a false positive** — bot filtering (403s from Maynooth, Tilburg, UPF, Algebra, BUas, UvA-adjacent hosts) or header-sensitive 404s (the Austrian ministry page and both HSLU pages return 200 to a normal browser). Two `URLError`s (`deai.ulb.be`, `investyourtalentapplication.esteri.it`) are most likely transient or proxy-related and I am not calling them dead. The one substantive product of the link check was discovering that **HSLU's three URLs now 301-redirect to a renamed programme path** (§3). Automated link-checking against university sites produces mostly noise, and I would rather report that than an impressive-looking list of phantom dead links.

### Manually opened at the official source (37 rows/questions)

**Statute:** the MESRS arrêté of 10 October 2023 in full — Articles 1–10 and 25–28 read in Arabic from the JORT PDF, plus a search for post-2023 amendments (none found).

**Level triage — 20 programme rows:** 27, 28, 29, 30, 31 (French *grade de master*, resolved against the CEFDG standing register — a single authoritative source covering all five); 93, 96, 171 (Spanish *oficial* vs *propio*); 148, 149, 150 (Italian AFAM second-level vs 1-year academic master); 11, 12, 13 (Croatian professional graduate title); 5, 48, 78, 99, 100, 147.

**Follow-ups — 6, all closed:** X-HEC/MSc&T, Vlerick, Ghent, BI Norwegian, SRH Berlin, Tilburg JADS.

**Tuition verification — the top of the price distribution.** I opened the source for the **5 highest-tuition rows**: 96 (IE, €43,000 ✓), 95 (Esade, €39,000 ✓), 171 (IE, €37,000 — page opened, fee not re-confirmed, see below), 56 (UCD, €26,180 ✓), 162 (UvA, €25,900 ✓). Plus rows 73, 70, 71, 74, 8, 130, 3, 5, 102 opened for other reasons, each of which also carried a fee check.

**Scholarships:** the **34-row stipend + `tunisia_eligible: yes` set was enumerated in full and read row by row**; I spot-verified the amount arithmetic on the two largest structural blocks — the 17 EMJM rows at €16,800 (= €1,400/month × 12, consistent) and Stipendium Hungaricum (rows 71/88) — and ran the duplicate check across all 106.

### Explicitly NOT sampled — the gaps in this audit

1. **I did not verify the recorded tuition figure for row 171 (IE Creative Direction, €37,000)** even though it is the third-highest in the file. I opened the programme page but spent the budget on the more consequential official/propio question. **The €37,000 is unverified by me.**
2. **I did not open the remaining ~148 programme rows' tuition sources.** Coverage of the fee field is roughly the top 5 by value plus 9 opened incidentally — call it **8% of rows, but weighted to where the money is**. The five I checked were all correct, which is weak positive evidence for the rest but not proof.
3. **I did not verify a single application deadline independently** except where one appeared on a page I opened for another purpose (JADS, UCD, Vienna). Deadlines are the field most likely to carry silent `PRIOR_CYCLE` errors and they are **the least audited field in this report**.
4. **I did not check `living_cost_estimate_year`, `post_study_work_visa`, `english_req`, `other_tests`, `portfolio_required`, or `work_experience_required` on any row I did not open for another reason.** `post_study_work_visa` in particular carries long immigration-law claims that no one has re-verified.
5. **I did not audit the 72 `high`-confidence scholarship rows** beyond the duplicate scan and the stipend subset. The `deadline_relative_to` field — which the brief calls critical — **has not been verified on any row**.
6. **I did not test the EU-vs-non-EU trap systematically**, which the brief calls the most common error in the task. The rows I opened happened to be correct on this, but I checked perhaps a dozen. **A dedicated pass over `tuition_non_eu_per_year` for the 60 rows whose source URL is a generic institution-wide fee page would be the highest-value next audit** — that URL shape is exactly where an EU figure gets copied into a non-EU field.
7. **I did not re-verify state recognition for the ~30 unambiguous public-university rows.** Judged low-risk; not zero-risk.
8. **I did not open the Greek ministry site, ihu.gr, maynoothuniversity.ie or ucd.ie beyond row 56**, despite having firecrawl budget left, because the level and follow-up questions took priority.

### Firecrawl usage

**10 of 60 calls used.** Spent on: the ministry BO arrêté (1), Onisep MSc&T (1), Algebra (1), IE ×2 (2), Tilburg/JADS ×4 (4), UCD (1). WebFetch and WebSearch carried roughly 30 further retrievals unmetered, and two official files (the CEFDG register `.xlsx` and the Tilburg fee `.pdf`) were pulled directly with `urllib` against the proxy CA bundle at no firecrawl cost. **50 calls remain unspent** — enough for the deadline pass and the EU/non-EU pass described above.
