# VERIFICATION REPORT — Agent V1 (adversarial)

Date: 2026-08-16 · Agent V1 · Status: IN PROGRESS — written incrementally, whatever is on disk is the deliverable.

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

_pending_

---

## 4. DISPUTED rows

_pending_

---

## 5. Follow-ups resolved

_pending_

---

## 6. What I sampled and what I did not

_pending_
