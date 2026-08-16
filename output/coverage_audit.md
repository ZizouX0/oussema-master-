# Coverage audit — V2 (adversarial pass over Waves 1 & 2)

**Date:** 2026-08-16 · **Baseline audited:** `output/programmes_master.csv`, 168 rows
**Scope:** the six zero-coverage countries, Greece, Bulgaria, Track B in the four
strongest Track B territories, and the private business-school sector.
**Firecrawl usage: 14 calls of the 90 allowed.** Everything else was WebSearch/WebFetch.

Nothing below is in `programmes_master.csv` — each candidate was checked against the
institution+programme list before being written up.

---

## 1. GENUINE MISSES

### GREECE — the largest single gap in the dataset

Greece held 2 rows. Five programmes below are qualifying and absent. G5's estimate of
"4–8 additional rows" was accurate.

#### A1. International Hellenic University — MSc in e-Business and Digital Marketing
| Field | Value |
|---|---|
| track | A |
| country / city | Greece / Thermi, Thessaloniki |
| institution | International Hellenic University (School of Science & Technology, UCIPS) |
| institution_type | public |
| programme_name_exact | MSc in e-Business and Digital Marketing |
| degree_awarded | MSc — Greek state postgraduate degree, **certified by the Hellenic Authority for Higher Education (HAHE/ETHAAE)**, published in the Government Gazette |
| language | EN ("taught exclusively in English") |
| duration_months | 18 full-time (30 part-time) |
| ects | 90 |
| tuition_non_eu_per_year | €3,700 **total** (no EU/non-EU differential published) |
| app_deadline_non_eu | 2026-08-26 (2026/27 cycle — PRIOR_CYCLE relative to a 2027 intake) |
| min_prior_ects | NOT_FOUND — stated as "an undergraduate University degree in Engineering, Science, Informatics, Economics & Business Administration" |
| english_req | State Certificate B2 or equivalent (waived for English-medium degree holders) |
| programme_url | https://st.ihu.gr/studies/postgraduate/ebusiness |
| confidence | high |

Squarely Track A (digital business + marketing analytics + "skills related to data
analysis and evaluation"). **Caveat to record in `fit_notes`:** study mode is
"Hybrid: In-person/Remote", weekday evenings — this collides with the MESRS
in-person-examination criterion (arrêté art. 2) that F3 identified.

#### A2. International Hellenic University — MSc in Data Science
Same institution, school, fee (**€3,700 total**), ECTS (**90**), duration (18 months),
language (EN), HAHE certification and deadline (2026-08-26).
URL: https://st.ihu.gr/studies/postgraduate/datascience
Entry: "undergraduate degree… preferably STEM; other degrees considered with solid
background in statistics/mathematics and good knowledge of databases and programming"
— a Business Intelligence licence plausibly clears this.

**Boundary flag, not a recommendation:** this sits in a Science & Technology school
with no explicit business-analytics stream, so under a strict reading of the Track A
definition it is excludable. But the dataset already contains Utrecht *MSc Applied
Data Science*, Tilburg *MSc Data Science and Society* and HSLU *MSc Applied Data
Science and AI* on the same footing. **Either A2 goes in or those three come out** —
the current dataset is internally inconsistent on this boundary. Same hybrid-delivery
caveat as A1.

#### A3. Athens University of Economics and Business — MSc in Marketing Analytics
| Field | Value |
|---|---|
| track | A |
| country / city | Greece / Athens |
| institution | Athens University of Economics and Business (Dept. of Marketing and Communication) |
| institution_type | public |
| programme_name_exact | MSc in Marketing Analytics |
| language | EN (AUEB's own programme list: "Greek and/or english"; the tuition page and admission rules are published in English and require an English certificate) |
| duration_months | 15 full-time, incl. a 3-month Analytics Capstone Project |
| ects | 75 |
| tuition_non_eu_per_year | €4,800 **total**, full-time (part-time €5,800); no non-EU differential published; figures shown for September 2026 entry |
| tuition_source_url | https://www.dept.aueb.gr/en/marketinganalytics/content/tuition-fees |
| english_req | **C2 for the full-time programme** (C1 for part-time) — an unusually high bar, record it |
| work_experience_required | no for full-time; **yes, 2 years, for part-time** |
| programme_url | https://www.dept.aueb.gr/en/marketinganalytics |
| confidence | medium (language field is stated as "Greek and/or english" on AUEB's central list — worth one confirming email before the row is treated as settled) |

This is an exact-title Track A match at a public university already represented in the
dataset by a *different* AUEB programme. Its absence is a straightforward miss.

#### A4. Athens University of Economics and Business — MSc in AI and Data Science
English, full-time and part-time, **€6,000 total**, offered jointly by the Departments
of Informatics and Statistics. €3,000 of assistantships available to full-time
students, reducing the effective fee to €3,000.
URL: https://datascience.aueb.gr/ · https://www.dept.aueb.gr/en/cs/content/graduate-study-program-master-science-data-science
Same boundary flag as A2 — Informatics/Statistics faculty, no business stream.

#### B1. Aristotle University of Thessaloniki — MSc in Digital Media – Computational Intelligence
| Field | Value |
|---|---|
| track | B |
| country / city | Greece / Thessaloniki |
| institution | Aristotle University of Thessaloniki, School of Informatics |
| institution_type | public |
| programme_name_exact | Digital Media – Computational Intelligence |
| language | EN ("Courses are taught in English, and foreign students are welcome") |
| duration_months | 18 (3 semesters) |
| ects | 90 |
| tuition_non_eu_per_year | €1,800 **for the whole programme** — the cheapest qualifying Track B programme found anywhere in this audit |
| mode | **In-person** (ministry register records mode as in-person — materially better than the IHU hybrid programmes for MESRS purposes) |
| quantitative_prereqs | "a degree in computer science or electrical and computer engineering or a numerate physical science discipline" — **this is a real risk for a Business Intelligence licence and must be checked before applying** |
| programme_url | https://dmci-en.csd.auth.gr/ · ministry record: https://studies.minedu.gov.gr/program/?programme_id=1191 |
| confidence | high |

Directly comparable to Bauhaus-Weimar *Computer Science for Digital Media*, which the
dataset already carries as Track B. AUTH is already in the dataset for a different
programme, so this is a programme-level miss, not an institution-level one.

---

### NETHERLANDS

#### B2. Leiden University — MSc Creative Intelligence & Technology *(resolves followup #5)*
The old **MSc Media Technology has been renamed, not abolished**. It is the same
programme, same faculty, same programme code.

| Field | Value |
|---|---|
| track | B |
| institution | Leiden University, Faculty of Science |
| programme_name_exact | Creative Intelligence & Technology (previously Media Technology) |
| degree_awarded | Master of Science · programme code **60206** |
| language | EN · duration 24 months · 120 ECTS · full-time · starts September and February |
| tuition_non_eu_per_year | **€22,500** institutional fee, 2026-2027 (€17,200 for a second master's; €2,694 statutory for EU/EEA) |
| tuition_source_url | https://www.universiteitleiden.nl/en/education/study-programmes/master/creative-intelligence--technology/admission-and-application/tuition-fees |
| app_deadline_non_eu | 1 April (non-EEA, for the following September) |
| accepts_3yr_bachelor | conditional — the programme markets itself as "open to any field of previous Bachelor education"; the ECTS floor is not published |
| programme_url | https://www.universiteitleiden.nl/en/education/study-programmes/master/creative-intelligence--technology |
| confidence | high on structure and fee; medium on the 180-ECTS question |

#### A5. TIAS School for Business and Society — Full-time MScBA, Business Analytics track
| Field | Value |
|---|---|
| track | A · institution_type **private** (Tilburg/TU-Eindhoven-affiliated) |
| programme_name_exact | Full-time Master in Management/Business Administration (MScBA) — **Business Analytics Track** |
| degree_awarded | MSc — **NVAO-accredited** (stated on the programme page) |
| language | EN · duration 12 months · ects **NOT_FOUND** |
| tuition_non_eu_per_year | €28,500 for the whole programme (VAT-exempt; includes the Brussels learning experience) |
| programme_url | https://www.tias.edu/en/courses/full-time-master-in-managementbusiness-administration-mscba-13453 |
| confidence | medium — ECTS and the non-EU deadline are not published |

A one-year 12-month master is squarely in F3's 51-row MESRS risk band. Flag on the row.

---

### GERMANY

#### A6. EBS Universität für Wirtschaft und Recht — Master in Business Analytics & AI
| Field | Value |
|---|---|
| track | A · institution_type **private, state-recognised** (institutional accreditation by the German *Wissenschaftsrat* / Council of Science and Humanities; AACSB) |
| city | Oestrich-Winkel / Wiesbaden |
| programme_name_exact | Master in Business Analytics & AI |
| degree_awarded | Master of Science |
| language | EN |
| ects / duration | **120 ECTS / 4 semesters** (Semester Abroad or Practice track). An Accelerated track of 60 ECTS / 2 semesters exists but **requires 240 ECTS or equivalent professional experience — closed to this applicant** |
| tuition_non_eu_per_year | €33,780 **total** for the 4-semester track (€27,830 for the accelerated track); no EU/non-EU differential published. −€3,000 early-enrolment bonus if enrolled by 28 February |
| min_prior_ects | **180** — "Bachelor's degree with minimum 180 ECTS in any field". This is one of the few German programmes that says so explicitly |
| other_tests | **GMAT / GRE / BAT / EBSgrad / CAT required** |
| english_req | TOEFL iBT 95 or IELTS 7.0 |
| app_deadline_non_eu | no formal deadline; visa applicants advised to apply by 30 May for an autumn start |
| programme_url | https://www.ebs.edu/en/ebs-business-school/study-programmes/master-in-business-analytics |
| confidence | high |

Note for the report: WHU's Master in Business Analytics is **being phased out and is
closed to new applicants from 2026** — correctly absent, and worth stating so nobody
re-adds it.

#### B3. SRH University (SRH Berlin University of Applied Sciences) — M.A. Film, Television and Digital Narratives
| Field | Value |
|---|---|
| track | B · institution_type **private, state-recognised** (accredited by the German Council of Science and Humanities) |
| city | Berlin |
| degree_awarded | Master of Arts · language EN · duration 4 semesters |
| tuition_non_eu_per_year | **€5,950 per semester for non-EU applicants** (€4,980/semester EU/EEA/CH) per DAAD's official International Programmes record = **€11,900/yr non-EU**. SRH's own marketing quotes €22,800 total / €5,700 per semester — **a live fact conflict; the non-EU figure must be confirmed with the school** |
| portfolio_required | **yes** — five to eight pieces of film work (films, screenplays, exposés or film analyses) plus a list of five favourite films/series |
| english_req | B2 |
| app_deadline_non_eu | none published; rolling |
| programme_url | https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/7011/ |
| confidence | medium (fee conflict) |

Materially relevant to this applicant: unlike almost every Track B programme in the
"entry-qualification wall" list in `followups.md`, SRH asks for a **portfolio**, not a
prior degree in the field. That makes it one of the very few Track B routes actually
open to a Business Intelligence graduate with a videography practice.

---

### SWITZERLAND — *resolves followup #4 (ZHdK)*

#### B4. Zürcher Hochschule der Künste — MA Design, Major Interaction Design
| Field | Value |
|---|---|
| track | B · institution_type public (HES/Fachhochschule) · city Zurich |
| programme_name_exact | MA Design, Interaction Design (Major within the Master's programme in Design) |
| degree_awarded | Master of Arts in Design |
| **language** | **English — "Main teaching language: English"** ← this is the answer followup #4 asked for |
| ects | 120 (Major coursework 90) · duration 4 semesters · autumn start |
| tuition_non_eu_per_year | **CHF 1,220 per semester for non-Swiss = CHF 2,440/yr** (CHF 720/semester Swiss) |
| app_deadline_non_eu | 27 February 2026 (2026 entry — expect late February 2027 for the target cycle) |
| programme_url | https://www.zhdk.ch/en/degree-programmes/design/ma-design-interaction-design |
| confidence | high |

**Partial resolution only.** ZHdK's MA Design has six majors; only Interaction Design
was confirmed English (Knowledge Visualization's language field renders empty even to
Firecrawl). The six **MA Film** majors — Cinematography, Creative Producing,
Documentary Filmmaking, Directing Fiction, Film Editing, Screenwriting — publish their
programme copy in German and should be treated as German-taught until an admissions
reply says otherwise. Do not add them.

---

### MOLDOVA — the only qualifying programme found in the six zero-coverage countries

#### A7. Technical University of Moldova — Master's degree, Data Science
| Field | Value |
|---|---|
| track | A (boundary — technical university, see note) · institution_type public · city Chișinău |
| language | EN (listed under "STUDY-PROGRAMMES IN ENGLISH") |
| ects / duration | **120 ECTS / 2 years** |
| tuition_non_eu_per_year | **€3,000 per academic year**, stated for **2026-2027** — i.e. the correct cycle, not a prior-cycle figure. Admission fee €100. Excludes legalisation, residence permit, medical insurance |
| tuition_source_url | https://international.utm.md/tuition-fees/ |
| confidence | high on fee/ECTS/language; medium on Track A fit and on ANACEC programme accreditation, which was not opened |

**Why it matters disproportionately:** at €3,000/yr with 120 ECTS over two years it
satisfies F3's MESRS five-year/two-year-post-licence reading *and* is among the
cheapest qualifying programmes in the whole dataset. UTM's own **Business Analytics**
master (120 ECTS) is **Romanian-taught** and correctly fails the language filter.
The other UTM English master, Software Engineering, is 90 ECTS / 1.5 years and out of
track. The "International MBA Agrobusiness Management" is excluded by the MBA rule.

---

### NORTH MACEDONIA — candidates, with a structural catch

South East European University (Tetovo/Skopje) — private-public, state-established —
publishes an explicit English-programme list. Second-cycle programmes offered in
English that touch the tracks:

| Programme | Faculty | ECTS as listed |
|---|---|---|
| **Business Analytics** | Business and Economics | **60 only** |
| Marketing and Innovation Management | Business and Economics | 60 only |
| **Business Informatics** | Contemporary Sciences and Technologies | **60–120** |
| Computer Sciences (Data Science module) | Contemporary Sciences and Technologies | 60–120 |

Source: https://www.seeu.edu.mk/en/future-students/academics/english-programmes

SEEU states its second cycle follows "the model 3+2 (four semesters, 120 ECTS)… open
to candidates who have obtained an undergraduate diploma equivalent to three years
(180 ECTS) or four years (240 ECTS)." **Read together, the 120-ECTS variants of
Business Informatics and Computer Sciences/Data Science are open to a 180-ECTS holder;
Business Analytics, listed at 60 ECTS only, most likely is not.** That is precisely
the inverse of what a title-based search would conclude — the on-title programme is
the one that is probably closed.

**Not recorded, because tuition could not be obtained.** SEEU's Financial Aid page
covers first-cycle programmes only and publishes no second-cycle fee. This is a
one-email gap, not a research gap: `financialaid@seeu.edu.mk`.

---

### ALBANIA — one candidate, blocked on accreditation

**University of New York Tirana — MSc in Data Science and Business Analytics.**
120 ECTS, 2 years, English (B1 floor), Faculty of Engineering and Architecture,
Department of Information and Intelligent Systems. Programme fee **€9,000 for the
programme** (UNYT's published master fee table).
URLs: https://www.unyt.edu.al/page/pm-data-science-and-business-analytics ·
https://int.unyt.edu.al/tuition-fees/

**Do not record it yet.** Two checks failed:

1. **Programme-level accreditation is not evidenced.** UNYT holds 6-year ASCAL
   institutional accreditation (from December 2020) and the ASCAL register lists
   programme decisions for *MSc Computer Sciences* (BA Nr. 198, 13.12.2024, valid to
   12.12.2029) and *MSc Business Administration* (BA Nr. 200, to 12.12.2028) — but
   **no decision for Data Science and Business Analytics appears in the register
   entry.** Under brief rule 5 that is unconfirmed, not confirmed.
   Register: https://www.ascal.al/en/hei-list/hei/universiteti-i-new-york-ut-ne-tirane-2
2. **UK-partner exposure.** UNYT runs master's degrees "in collaboration with the
   University of Greenwich, UK". The evidence indicates the Greenwich arrangement
   attaches to the **MSc Computer Science**, not to DSBA — but this was not confirmed
   from a Greenwich or UNYT partnership document. If DSBA turns out to be
   Greenwich-validated it is excluded outright by the brief's UK rule.

Given the Cypriot accreditation minefield G5 documented, treating this as "found" would
repeat exactly the error the brief warns about.

---

## 2. CONFIRMED ABSENCES

### 2.1 SERBIA — structurally closed to a 180-ECTS holder. This is the audit's most consequential negative.

Serbian *master academic studies* are **one year / 60 ECTS**, sitting on top of a
**four-year / 240-ECTS** undergraduate degree. Two independent statements:

- **Singidunum University**, on its own master admissions page: *"The length of Master
  program is one year and it carries 60 ECTS."* Its complete English-taught master
  list is **Business Economics · Business Systems in Tourism and Hospitality · Data
  Science** — all one-year/60-ECTS.
  https://singidunum.ac.rs/admission-master/
- **University of Belgrade, Faculty of Organizational Sciences**: master academic
  studies are open to candidates who "have previously completed undergraduate academic
  studies with at least 240 ECTS points… or at least eight semesters." Its
  *Information Systems and Technologies* master is a one-year, 60-ECTS programme.

**Consequence:** the applicant's 180-ECTS licence does not reach the entry floor for
the Serbian one-year model, and no 120-ECTS English-taught alternative surfaced. G8's
hypothesis — that the Western Balkans are where the 240-ECTS structure genuinely bites —
is **confirmed for Serbia**. This is a country-level finding, not a search gap.
Searched: Singidunum (English portal + master admissions), University of Belgrade FON,
Serbian higher-education law summaries, StudyInSerbia/obrazovanje.rs registries.

### 2.2 BOSNIA & HERZEGOVINA — same structure, plus an accreditation problem

- **International University of Sarajevo**: bachelor 4 years/240 ECTS, master
  **1 year/60 ECTS**. Same structural exclusion as Serbia. ~€3,500/yr.
- **Sarajevo School of Science and Technology**: English-medium, but "in association
  with the University of Buckingham" — **UK-validation exposure across the portfolio**,
  which is a brief exclusion, not merely a caveat.
- **International Burch University**: English-medium; master's are "60 to 120 ECTS
  depending on the bachelor's entry point", so a 120-ECTS route plausibly exists. But
  its recognition is **cantonal** (Ministry of Education, Science and Youth of Sarajevo
  Canton) plus **BAC — the British Accreditation Council, a private UK body, not a
  state accreditor**. Neither the state-recognition test nor the track fit was
  established. **Not recorded. Genuinely unresolved rather than absent** — see §3.

### 2.3 MONTENEGRO — no qualifying programme evidenced

University of Montenegro (public, Podgorica) and University of Donja Gorica (private)
both advertise English-taught master's, but no track-relevant, English-taught,
state-accredited master's programme page was located. The one concrete UDG master
identified is an **MSc in Statistics** (120 ECTS, Faculty for International Economics,
Finance and Business) — out of both tracks. **Reported as not-found rather than
non-existent**: UDG's programme catalogue was not reachable at programme level and this
country deserves one more pass with a Montenegrin-language search.

### 2.4 BULGARIA — effectively empty for both tracks, and the reason is documented

- **Sofia University St. Kliment Ohridski** — its own official page for "Master's
  Degree programs in English or other foreign languages" names only **Medicine** and
  **Pharmacy**, and both are 5–6 year integrated first-degree programmes, i.e.
  excluded by the level rule. Everything else is devolved to faculty websites with no
  central English list.
  https://www.uni-sofia.bg/index.php/eng/admission/international_students/master_s_degree_programs_in_english_or_other_foreign_languages
- **UNWE (University of National and World Economy)** — the international tuition page
  lists a master's fee only for **Law, taught in Bulgarian** (€3,300/yr). UNWE's two
  English-taught master's most relevant to Track A — *MSc Digital Marketing and
  Transformation* and *MBA in Global Operations and Analytics* — are **double degrees
  with Abertay University, Scotland**, and are therefore **excluded by the brief's
  UK-partner rule**, not merely unverified. The MBA is doubly excluded.
- **New Bulgarian University** — publishes only a fee band for non-EU master's students
  (10,800–13,200 BGN = €5,522–6,749/yr) with no English-taught programme list; no
  track-relevant English master's page was reachable.

**Verdict:** Bulgaria's near-absence from the dataset is close to correct. What exists
in Track A is either Bulgarian-taught or UK-validated. Nothing in Track B surfaced at
all. G8 was right to record it as unresolved; it now resolves mostly to *nothing
qualifies*.

### 2.5 Track B — programmes checked and correctly absent

| Institution | Programme | Why it is correctly absent |
|---|---|---|
| University of the Aegean | Cultural Informatics and Communication (incl. *Culture and Documentary Film Production*) | **Greek-taught** (ministry register, programme 1467). 90 ECTS, €2,800/yr. A genuine language near-miss. |
| Ionian University, Corfu | MA Audiovisual Arts in the Digital Age | Language of instruction not stated anywhere on the official page; and entry requires that "the diploma a candidate holds should relate primarily to traditional art forms" — the Track B qualification wall. €2,400 total. **Excluded, but see §3.** |
| Ionian University | MARes in Hybrid Arts | Classes delivered **remotely**; a Master *of Research*. Fails the delivery and level tests. |
| TAMK (Finland) | Master's Degree Programme in Media Production | **Finnish-taught**, 60 ECTS, multi-modal (TAMK study guide). Finland's most obvious-looking UAS Track B target, and it fails on language. |
| Hochschule Darmstadt | Motion Pictures | It is a **Bachelor** (7 semesters), taught almost entirely in English. Not a master. Correctly absent. |
| Tallinn University BFM | JMD Film Arts (Kino Eyes) | UK consortium partner (Edinburgh Napier) — excluded by the same rule already applied to Lusófona/KINO EYES. Confirms followup #27's suspicion. |
| ZHdK | six MA Film majors | German-taught. |
| Alba Graduate Business School | — | **No MSc in Business Analytics or Data Science exists.** Alba's MSc portfolio is Finance, Strategic HRM, Tourism Management etc., plus four MBAs. There is nothing to record, so the UK-validation question raised in followup #26 is moot for both tracks. Its US NECHE accreditation would in any case have been a problem. |

### 2.6 Track A — checked and correctly absent

- **WHU – Otto Beisheim** Master in Business Analytics: **being phased out, closed to
  new applicants from 2026.**
- **Nyenrode Business University**: portfolio is MBA/MSc Accountancy-led; no
  business-analytics master's found.
- **RSM MScBA Business Analytics & Management**: already in the dataset under Erasmus
  University Rotterdam. Not a duplicate to add.
- **Kozminski Master in Big Data Science**: already in the dataset.
- **Sofia University Digital Marketing MA**: as G8 found, unusable — confirmed.

---

## 3. STILL UNRESOLVED

Ordered by how much they would change the dataset.

| # | Item | What is missing | What would settle it |
|---|---|---|---|
| V2-1 | **SEEU (North Macedonia) second-cycle tuition** | No published master's fee. The 120-ECTS Business Informatics / Data Science variants otherwise look open to a 180-ECTS holder | One email to `financialaid@seeu.edu.mk`. Would convert 1–2 rows |
| V2-2 | **UNYT Tirana — DSBA programme accreditation + Greenwich status** | ASCAL register shows no programme decision for this master; Greenwich partnership scope unconfirmed | ASCAL decision PDF, or a written statement from UNYT. Decides whether Albania yields 1 row or 0 |
| V2-3 | **AUEB MSc Marketing Analytics — language** | AUEB's central list says "Greek and/or english"; the departmental site is fully English and demands C2 English | One email to `marketinganalytics@aueb.gr`. This is the strongest Greek Track A addition and it hangs on one word |
| V2-4 | **Ionian University — MA Audiovisual Arts in the Digital Age, language** | Never stated on the official page | Email `avarts.ada@ionio.gr`. Even if English, the "traditional art forms" entry rule probably closes it |
| V2-5 | **SRH Berlin non-EU fee** | DAAD says €5,950/semester non-EU; SRH marketing says €5,700/semester flat | The school's own fee schedule |
| V2-6 | **ZHdK MA Design — the other five majors' teaching language** | Only Interaction Design confirmed English; the language field renders empty on the other major pages | Firecrawl with JS wait, or the ZHdK admissions office |
| V2-7 | **Montenegro (UDG + UCG) programme catalogues** | Not reachable at programme level | A Montenegrin-language pass over `udg.edu.me` and `ucg.ac.me` |
| V2-8 | **International Burch University (BiH)** | 120-ECTS master route exists in principle; state recognition is cantonal + a private UK accreditor | BiH state/entity accreditation agency register |
| V2-9 | **Greek ministry database completeness** | `masters.minedu.gov.gr` has migrated to `studies.minedu.gov.gr` and its filter UI is JS-paginated. I reached individual records via site-scoped search, not a systematic sweep of all 1,368 | A crawl of `studies.minedu.gov.gr/program/?programme_id=N` — the records are cleanly numbered and each states language, ECTS, fee and delivery mode. **This is the single highest-yield unexploited resource in the whole project** and it is cheap: the pages are static and WebFetch-readable once you have the numeric ID |
| V2-10 | **TIAS MScBA ECTS and non-EU deadline** | Not published | TIAS admissions |
| V2-11 | **EKA/TalTech Design and Technology Futures (Estonia)** | 120 ECTS, English, joint EKA+TalTech; entry requires a prior degree "in technology, design or innovation" plus a portfolio. Track B fit is arguable (design, not media production) and the non-EU fee was not confirmed from an official page | `artun.ee` admissions pages; then a track-fit decision |

---

## 4. ASSESSMENT PER TERRITORY (Wave 1 groups)

| Group | Territory | Verdict | Reasoning |
|---|---|---|---|
| **G1** | DACH (DE/AT/CH/LI) | **Adequate, with two named holes now filled** | 21 rows. Germany's public Track B coverage is genuinely good. The private sector was under-searched: **EBS** (Track A) and **SRH Berlin** (Track B) were both missed, and both are state-recognised. ZHdK is now resolved for Interaction Design. Austria and Liechtenstein look correctly thin. |
| **G2** | Benelux | **Adequate → good, one clear miss** | 24 rows and strong Track B. **Leiden's renamed programme was dropped rather than updated** — a maintenance failure, not a search failure. TIAS was never checked. Followups #2 (Tilburg/JADS), #3 (Vlerick), #8 and #9 remain open and are V1's to resolve. |
| **G3** | France | **Adequate** | 14 rows. Not re-audited here beyond confirming no Track B leakage; followup #1 (X-HEC) is a V1 fact question. |
| **G4** | Nordics | **Adequate** | 22 rows across five countries with a well-documented Track B entry-qualification wall. Not re-audited; the open items are fee/accreditation facts, not coverage. |
| **G5** | Ireland / Malta / Cyprus / **Greece** | **Ireland, Malta, Cyprus adequate. GREECE WAS UNACCEPTABLE — now materially repaired** | Greece held 2 rows against a public university system that runs a fully English-medium international centre plus HAHE-certified English MSc programmes at AUEB and AUTH at €1,800–6,000 *total*. Five qualifying programmes were absent, one of them (AUTH Digital Media – Computational Intelligence, €1,800 all-in, in-person) is among the best value-for-money rows in the entire dataset. The failure was tooling, not judgement: `ihu.gr` and the ministry database both return 503 to WebFetch and needed Firecrawl, and the agent's budget was spent. |
| **G6** | Iberia | **Not re-audited** | G6's own structural finding on Spanish-language Track B is well-evidenced and I found no reason to doubt it. Followups #14–#19 are unaddressed by this pass. |
| **G7** | Italy | **Not re-audited** | Followups #6, #7, #10 remain open. |
| **G8** | CEE / SEE (17 countries) | **Thin, but less culpable than it looks — and the biggest single gap is now closed as a negative, not a positive** | The six zero-coverage countries yield, on the evidence: **one qualifying programme (Moldova/UTM), two blocked candidates (SEEU North Macedonia on fees, UNYT Albania on accreditation), and three structural exclusions (Serbia, Bosnia, and — pending one more pass — Montenegro).** Serbia and Bosnia run 4+1 with a 240-ECTS entry floor and are effectively closed to this applicant regardless of language. Bulgaria resolves to near-empty for documented reasons. **G8's silence was largely correct; the dataset was not missing much, but nobody could have known that until it was checked.** Poland/Croatia/Romania/Lithuania second-tier institutions (followup #13) remain genuinely unchecked. |

### Cross-cutting observations

1. **The dataset has an unstated Track A boundary rule and it is applied inconsistently.**
   Utrecht, Tilburg (Data Science and Society) and HSLU are in; IHU Data Science, AUEB
   AI and Data Science and NKUA DSIT would be out on the same criterion. Someone should
   write the rule down and re-apply it in one pass, in either direction. Until then,
   "is X missing?" has no determinate answer for general applied-data-science degrees.
2. **Delivery mode is not captured in the schema and it now matters.** F3's finding
   that MESRS requires in-person examination makes hybrid/distance delivery a
   disqualifier, not a footnote. Both IHU programmes are hybrid; AUTH's is in-person;
   the Greek ministry register publishes this field for every programme. **The schema
   has no column for it.** That is a structural omission affecting far more than Greece.
3. **The 240-ECTS risk is real but geographically narrow.** It binds hard in Serbia and
   Bosnia and probably Montenegro; it does *not* bind in Moldova (120-ECTS masters),
   North Macedonia (explicit 3+2 route at 120 ECTS) or anywhere G8 previously checked.
   G8's original reading — that subject composition, not total credits, is the usual
   danger — survives, with the Western Balkans as the documented exception.
4. **Track B remains the weak track, but for a reason that is now clear.** Of every
   Track B programme examined in this audit, exactly one — SRH Berlin — admits on
   portfolio rather than on a prior degree in the field. The realistic Track B universe
   for this applicant is much smaller than the row count suggests, and the shortlist
   should be filtered on `quantitative_prereqs` before anything else.

---

## Firecrawl usage

**14 calls of the 90 allocated** (≈46 credits, leaving ~250 of the shared 297).
Breakdown: IHU UCIPS index + 3 IHU programme pages (4); ZHdK — 2 site maps and 4 page
scrapes (6); Leiden CIT (1); UTM Moldova fee schedule (1); Singidunum master
admissions (1); one wasted call on a ZHdK redirect shell (1).

Firecrawl was used only where WebFetch failed outright: `ihu.gr` / `st.ihu.gr` and
`masters.minedu.gov.gr` return **HTTP 503** to WebFetch on every path, and
`zhdk.ch`, `universiteitleiden.nl`, `international.utm.md` and `singidunum.ac.rs`
render their programme facts client-side. Everything else in this audit was done with
unmetered WebSearch and WebFetch.
