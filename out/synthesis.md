# Comparative analysis: Ayurveda, Traditional Chinese Medicine (TCM) and Unani

Corpus: three extractions under codebook v1.6 (`work/ayurveda/final.yml`, `work/tcm/final.yml`, `work/unani/final.yml`). Nothing here comes from outside them.

**Citation convention.** `[system: field.subfield]` names the leaf a claim rests on. A cross-system claim cites a filled leaf for every system it covers. Where a leaf is filled for only some systems, the claim is stated for those systems and marked "not established" for the others.

**Registers.** Four kinds of statement are kept apart: what a tradition claims (emic), what historians have established (historical scholarship), what biomedical evidence shows, and what is regulatory fact. Each is labelled where they could blur.

**Provenance notes that affect how far claims can be pushed.**
- Many leaves on construct, canon, contact and politics are uncited or indirect (open encyclopedia, catalog, blog). Each chapter says where this limits a claim.
- Leaves tagged `source_report: v1` are used only as context. They are Ayurveda `identification.alternate_names`, `primary_regions` and `materia_medica.flagship_agents`; TCM `modalities.items`, `economics.domestic_market_size` and `global_market_estimates`, and `education_and_licensure.biomedical_content_in_curriculum`; Unani `identification.practitioner_estimate`, `education_and_licensure.degree_programs` and `preclinical_and_constituent_evidence`. None carries a comparative claim here.
- `evidence_borrowed_from_other_traditions` is an empty list in fields 5 and 13 for all three systems. In field 14 it is empty for Ayurveda and TCM and non-empty for Unani. Those Unani entries are excluded from Unani's column (see chapter 7).

---

## Part I. Cross-system fields computed at synthesis

### I.1 Shared events (leaves: `canon_and_transmission.dated_events`, `disruption.dated_events`, `revival_and_institutionalization.dated_events`)

I matched events on label, date and description. Each row below is one data point, not two or three. None of these is convergent evidence. They are the same event seen from two reports.

| Event | Appears under | Date | What each extraction records |
|---|---|---|---|
| Macaulay's Minute | Ayurveda, Unani | 2 Feb 1835 (Ayurveda gives the day; Unani gives 1835, and its `disruption.period` gives 2 Feb 1835) | Ayurveda: a minute on general education, approved by Bentinck's resolution of 7 March 1835. Unani: an education policy privileging Western learning. [ayurveda: disruption.dated_events; unani: disruption.dated_events, disruption.period] |
| Bhore Committee | Ayurveda (recorded twice, in field 8 and field 9; counted once), Unani | 1946 | Both say the report treated indigenous medicine as unscientific. Both extractions' own verify notes say they did not read the report text and relied on secondary summaries. The Unani note adds that secondary sources say Bhore was disparaging but did not mainly address indigenous medicine. The agreement is therefore not independent confirmation. [ayurveda: disruption.dated_events, revival_and_institutionalization.dated_events; unani: disruption.dated_events] |
| Chopra Committee on Indigenous Systems of Medicine | Ayurveda, Unani | 1948 | Ayurveda: recommended developing indigenous systems with a synthesis approach. Unani: recommended integration toward "one Indian system". The two descriptions are compatible. Hakims sat on the committee (Unani `practitioner_response`). [ayurveda: revival_and_institutionalization.dated_events; unani: disruption.dated_events] |
| Sanskrit medical texts rendered at the Abbasid court (Mankah/Kankah al-Hindi) | Ayurveda, Unani | 786-809 (Ayurveda); "8th c." (Unani) | Labels differ. The match rests on description and overlapping date. Ayurveda names Caraka and Suśruta, the Barmakids and Harun al-Rashid. Unani names Mankah al-Hindi and the Abbasid court. Moderate-confidence match: Ayurveda's window runs into the 9th century and Unani's date is coarser. [ayurveda: canon_and_transmission.dated_events, canon_and_transmission.key_figures; unani: canon_and_transmission.dated_events, canon_and_transmission.key_figures] |

No `dated_events` leaf in TCM matches an event in either other system.

**Near-matches not counted.** These fall outside the three `dated_events` leaves or differ in substance.
- The NMI abolition order of 28 Jan 1835 is a dated event only in Ayurveda. [ayurveda: disruption.dated_events] Unani's `abolition_attempts` leaf is `absent`, but its gap-pass note says the same order discontinued the Calcutta Madrasa's Unani classes. That was found in secondary sources and not recorded as a finding. [unani: disruption.abolition_attempts] The Ayurveda leaf itself says the order discontinued both the Ayurvedic and Unani classes. So this is one event documented in one column, not two.
- WHO benchmarks for Ayurveda and for Unani were both published 11 Feb 2022. [ayurveda: legal_status.supranational_standards; unani: disruption..., see revival_and_institutionalization.dated_events and legal_status.supranational_standards] This is two instruments released together, and only Unani lists it as a dated event.
- The NCISM Act 2020 is dated in Unani's events. In Ayurveda it appears only in prose and in the legal leaf. It is the same statute and one regulatory fact. [ayurveda: revival_and_institutionalization.state_sponsorship, legal_status.jurisdictions; unani: revival_and_institutionalization.dated_events]
- Ayurveda's Native Medical Institution was founded 21 June 1822. [ayurveda: disruption.dated_events] TCM's Daoguang acupuncture decree is also dated 1822. [tcm: disruption.dated_events] The two are unrelated events in the same year and are not shared.
- The 12th-century Rgyud bzhi is a dated event in Ayurveda. TCM mentions the same text only in the `period` field of a relationship entry. [ayurveda: canon_and_transmission.dated_events; tcm: contact_and_borrowing.relationships]

### I.2 Corroborated exchanges (leaf: `contact_and_borrowing.relationships`; both `corroborated_by` leaves are `deferred`)

I kept each relationship's `kind` distinct. Shared descent, direct descent and parallel are never treated as exchange.

**Corroborated from both ends: one exchange.**

*Sanskrit medical texts into Arabic and Persian, Ayurveda and Unani.*
- Ayurveda records an `exchange` with "Arabic/Persian medicine (Abbasid Baghdad)", direction Sanskrit to Arabic/Persian, 786-809, documented translation, demonstrated. It names Caraka and Suśruta as rendered, Mankah/Kankah al-Hindi, and al-Razi's al-Ḥāwī. [ayurveda: contact_and_borrowing.relationships]
- Unani records an `exchange` with "Ayurveda (and Siddha)": Sanskrit texts into Arabic (8th c.) and Persian (from the 14th c.), plus Indian drugs into Arabic/Persian pharmacopoeias. It is documented translation, demonstrated. [unani: contact_and_borrowing.relationships]
- **What the Ayurveda end contributes:** the source side. That means the named texts, the named translator and patrons, and the period of the first wave.
- **What the Unani end contributes:** the receiving side. That means the second, Persian wave from the 14th c. and the flow of drugs. The Speziale monograph (Brill 2018), cited directly in Unani's construct-debate leaf, documents the Persian translation of Ayurvedic sources from the 14th c. [unani: construct_debate.positions]
- **Limits.** Ayurveda's relationships leaf is uncited. Unani's is cited only to an academia.edu profile (aggregator, indirect), and its verify pass could not confirm it from a single source. The extractions are isolated, but I cannot see whether their underlying sources overlap. Corroboration here means two reports agree. It is not a verified primary attestation.
- **Direction flag.** Unani labels the direction "bidirectional", but both flows it lists run from India into Arabic/Persian. Neither extraction records a flow back into Ayurveda in this channel.

**Both ends record the claim, but only as contested.**

*Pulse diagnosis.*
- Ayurveda records an `exchange` from "Islamic and/or Chinese" into Ayurveda, late, textual attestation, contested. [ayurveda: contact_and_borrowing.relationships]
- TCM records an `exchange` with "Multiple (pulse diagnosis origins)", direction unclear, structural parallel, contested. [tcm: contact_and_borrowing.relationships]
- The two extractions agree that the origin is unresolved. That is corroboration of the contest, not of an exchange. Unani has no relationship entry about pulse, even though it lists nabz as a method. [unani: diagnostics.methods] Its silence is not a contrast.

**Recorded at one end only, so not corroborated.**
- **India/Buddhist to China.** TCM records an exchange, India to China via Buddhist transmission, demonstrated. [tcm: contact_and_borrowing.relationships] Ayurveda records no outflow to China. Its only Buddhist entry is Buddhist monastic medicine descending into Ayurveda, which is contested and a different direction and kind. [ayurveda: contact_and_borrowing.relationships]
- **China to Persia (Tanksuqnama, Ilkhanate), demonstrated in TCM.** Unani records Chinese and Tibetan medicine as a `parallel` with status `convergence`, meaning no contact the report can show. [unani: contact_and_borrowing.relationships] This is a tension and not corroboration. Unani's own boundary treats Persian medicine as a same-system variant. [unani: identification.system_boundary] The corpus cannot say whether Unani's "no contact shown" simply reflects its report's scope.
- **Tibetan medicine.** Ayurveda records Sanskrit to Tibetan, and TCM records China to Tibet (pulse). Both are demonstrated and both concern the Rgyud bzhi. They are two different exchanges with a third party that has no extraction. Ayurveda's own note that the Rgyud bzhi "also integrates Chinese ... elements" is consistent with TCM's entry but is not a relationship leaf. [ayurveda: contact_and_borrowing.relationships; tcm: contact_and_borrowing.relationships]
- **Rasaśāstra/alchemy** (Ayurveda, contested), **Tibb al-Nabawi** (Unani) and **Latin Europe** (Unani, shared descent) are single-ended.

**Kinds kept distinct.**

| Kind | Entries |
|---|---|
| Direct descent | TCM to kampo and to Korean medicine; Greek to Unani. [tcm, unani: contact_and_borrowing.relationships] Ayurveda's Buddhist and Vedic antecedents are also coded descent and are contested. |
| Shared descent | Unani and Latin-European medicine, via the Qanun. [unani: contact_and_borrowing.relationships] |
| Parallel | Ayurveda and Greek humoral medicine; TCM, for "Greek humoral medicine and Ayurvedic tridosha"; Unani and Chinese/Tibetan. [ayurveda, tcm, unani: contact_and_borrowing.relationships] |
| Same-system variant | Unani and Traditional Persian Medicine. |

---

## Part II. Analysis by axis

## 1. Canon and dating

**Foundational texts as recorded.**
- **Ayurveda.** The Caraka Saṃhitā is dated "early centuries CE" and is a redaction of a treatise attributed to Agniveśa, completed in part by Dṛḍhabala. The Suśruta Saṃhitā may have begun in the last centuries BCE and was completed by a later redactor. The Aṣṭāṅgahṛdaya and Aṣṭāṅgasaṃgraha are c. 7th c. CE. [ayurveda: canon_and_transmission.foundational_texts, redaction_history]
- **TCM.** The Huangdi Neijing is a layered Han-period text. No date or author is given for the Nanjing, the Shennong Bencao Jing or the Shanghan Zabing Lun, apart from the traditional attribution to Zhang Zhongjing. [tcm: canon_and_transmission.foundational_texts]
- **Unani.** The corpus is Greek and Arabic with stated dates: the Hippocratic corpus, Galen, Hunayn's Risala, al-Razi's al-Ḥāwī (865-925), al-Majusi (d. 994) and the Qanun (begun c. 1012, completed 1020-1025). [unani: canon_and_transmission.foundational_texts] The Indian Unani compendia and commentaries are not titled. [unani: canon_and_transmission.secondary_canon]

**How contested the dating is, by each extraction's account.**
- **Ayurveda.**
  - Meulenbeld is quoted as saying the problems are "far from even approaching a solution".
  - Zysk places the formative period in Buddhist monastic communities from about the 4th c. BCE.
  - The report states that dates rest on internal layering and cross-references, not on external documentary anchors.
  - No firm authorial identity exists for Suśruta, Caraka or the two Vāgbhaṭas.
  - [ayurveda: canon_and_transmission.dating_and_authorship_disputes, self_reported_gaps.inventory]
- **TCM.**
  - Unschuld dates Suwen language and ideas to roughly 400 BCE-260 CE.
  - Li, Lo and Harper infer compilation after 168 BCE from the divergence from the Mawangdui manuscripts.
  - Sivin, Yamada, Hsu and Lo describe channel theory as having a developmental history.
  - Composite nature and Han dating are recorded as consensus. The dating of individual layers and the link between the excavated manuscripts and the received canon remain debated.
  - [tcm: canon_and_transmission.dating_and_authorship_disputes]
- **Unani.** The disputes concern textual transmission, not origin.
  - No complete critical edition of the Arabic Qanun exists, and the 2018 edition of part of Book I leaves "the larger unresolved textual problem".
  - Apocryphal attributions are documented.
  - The report calls the disputes "localized, not existential".
  - [unani: canon_and_transmission.dating_and_authorship_disputes, redaction_history]

**External anchors.**
- Ayurveda has one: the Bower Manuscript (c. 4th-6th c. CE, found 1890), which contains material overlapping the classical tradition, including quotations echoing Caraka. [ayurveda: canon_and_transmission.external_dating_anchors]
- TCM has several excavated or surviving witnesses. These are Mawangdui Tomb 3 (sealed 168 BCE, excavated 1973), Zhangjiashan, Laoguanshan/Tianhui and Wuwei, plus the Tai su preserved in Japanese copies. [tcm: canon_and_transmission.external_dating_anchors] The report reads Mawangdui as predating the received Neijing, and the dating debate turns on how the two relate.
- Unani has a dated copy of the Qanun's own Book 5 (444 H / 1052 CE), an undated but complete Timurid-era copy, and modern editions of Hunayn's Risala (1925, 2016). [unani: canon_and_transmission.external_dating_anchors]

**What the comparison supports.**
- The three extractions describe three different kinds of uncertainty, and I do not rank them on a single scale.
  - Ayurveda's is about the origin and authorship of the texts themselves.
  - TCM's is about layering within a composite, with pre-canon excavated material in play.
  - Unani's is about transmission and editions of works whose authors and dates the extraction states.
- The anchors also differ in kind. Ayurveda has a manuscript that overlaps the tradition. TCM has excavated neighbouring or earlier literature. Unani has a dated copy of the work itself.
- Source strength limits any ranking. Unani's canon leaves cite a reference work directly (Historia Medica, `direct`). TCM's rest on open encyclopedias (`indirect`), and only the Neijing is cited. Ayurveda's rest on named scholarship (Meulenbeld, Zysk) that is uncited or reached through catalog listings (`indirect`). [ayurveda, tcm, unani: canon_and_transmission.foundational_texts, dating_and_authorship_disputes] The Unani canon's apparent firmness may partly reflect better sourcing and a canon with attributed authors.
- TCM's dating of three of its four foundational texts is not given, so a cross-system dating comparison cannot be completed.
- The reports' own characterizations ("irreducible", "debated", "localized") are the reports' stances.
- Corpus-scale appraisal is not applicable to this axis.

## 2. Construct and continuity

**Positions, as recorded.** In all three systems the `positions` leaf is filled.
- **Ayurveda.**
  - The reinvention camp: Smith and Wujastyk (2008), Langford, Alter, Mukharji, and Sivaramakrishnan and others. Their evidence base is historical and ethnographic scholarship.
  - The continuity camp: the Ministry of AYUSH, practitioner-scholars and some Indologists, resting on persistence of texts, concepts and materia medica.
  - A middle position from Dominik Wujastyk: continuity of texts, discontinuity of much practice.
  - A variant, Maharishi Ayur-Ved, described as only loosely tied to classical texts.
  - [ayurveda: construct_debate.positions, identification.system_boundary]
- **TCM.**
  - Taylor (2005): TCM was invented in the 1950s PRC project.
  - Lei and Andrews: decisive transformation in the Republican era.
  - Unschuld: selective reconstruction.
  - Karchmer and Ernst: Hobsbawm's "invented tradition".
  - Scheid: "plurality within continuity".
  - PRC official narratives: unbroken transmission.
  - [tcm: construct_debate.positions]
- **Unani.**
  - Attewell (2007) and Alavi (2005, 2007): reconstitution in the late colonial period and the 19th c.
  - Liebeskind, Hardiman (2009, "invented traditions"), Sivaramakrishnan (2006) and Schmidt Stiedenroth (2020).
  - Speziale (2018): pre-colonial Persian-Ayurveda dynamism. The claim that this complicates "simple invention" is the report's own inference.
  - Critics of Iranian Traditional Persian Medicine, who call it a nationally branded new construction.
  - Defenders within CCRUM, Hamdard and the TPM faculties: lineage continuity.
  - [unani: construct_debate.positions]

**Do the debates have the same shape?** The extractions support this for all three: each has a reinvention camp, a continuity camp allied with state or institutional actors, and a middle position. Ayurveda's middle is Wujastyk and TCM's is Scheid. Unani's is a report-level "reconstruction on a real foundation", since no named scholar is cast as a middle. [ayurveda, tcm, unani: construct_debate.positions, construct_debate.report_adjudication] Differences:
- **Periodization and driver.** TCM's construction is dated mid-20th c. and is led by the state. The mainstream TCM position is to treat it as invention, though Lei and Andrews locate the decisive change earlier, in the Republican era. Ayurveda's and Unani's are colonial-era professionalization under nationalist and communitarian politics, with later state institutionalization. Unani has a separate revival-level debate in Iran, dated from 2007. [tcm: construct_debate.positions; unani: construct_debate.positions, identification.system_boundary]
- **Scope.** Ayurveda has a variant with its own construct question (Maharishi). TCM records no variant-level question. Unani has Persian medicine. [ayurveda, unani: identification.system_boundary]
- **The debates are not independent.** Sivaramakrishnan appears in both Ayurveda's and Unani's positions, and Hardiman is recorded as treating Ayurveda and Unani together as "invented traditions". [ayurveda: construct_debate.positions; unani: construct_debate.positions] The two Indian debates share historiography, so they are not two separate observations. TCM's scholarship (Taylor, Lei, Andrews, Scheid, Unschuld) does not overlap with either.

**Evidence quality of the positions.**
- Unani's are cited directly to the works themselves (monographs, articles). The report's own glosses are flagged in the entries as interpretation.
- Ayurveda's rest partly on indirect catalog and practitioner-site citations, and one entry is flagged `claim_match: mismatch`.
- TCM's are mostly uncited, except for Lei and Andrews.
- So the structural similarity is well supported. The attribution of specific positions is firmest for Unani and weakest for TCM.

**Each report's adjudication, compared as a stance and not as evidence.**
- Ayurveda: both camps are "partly right and largely argue about different objects".
- TCM: a "scholarly near-consensus" of construction, with interpretation "genuinely unsettled".
- Unani: "reconstruction on a real foundation".
[ayurveda, tcm, unani: construct_debate.report_adjudication]
The reports lean differently. TCM's is the most invention-leaning by its own summary, but it hedges.

## 3. Rupture and survival

**Loss of patronage.**
- **Ayurveda:** partial. One seminar paper (Zafar 2018, reached through a search summary, `indirect`) argues that Delhi Sultanate and Mughal patronage went to Greek-Arabic medicine. No dated collapse was found. [ayurveda: disruption.loss_of_patronage]
- **TCM:** the 1822 Daoguang decree excluded acupuncture and moxibustion from the Imperial Medical Academy. The extraction calls this a loose fit. The source describes it as a local event with no proven wider effect. [tcm: disruption.loss_of_patronage]
- **Unani:** the Nizams of Hyderabad (1724-1948) were the strongest colonial-era patrons. The leaf records no loss of Mughal or princely patronage and no dates. [unani: disruption.loss_of_patronage]
- **Comparison.** A dynastic-collapse loss of patronage with dates is established for none of the three. Ayurveda's claim that patronage shifted to Unani cannot be checked against the Unani column, because that leaf says it gives no account of Mughal-era patronage. The claim is single-ended.

**Foreign pressure (leaf `colonial_power`).**
- Ayurveda: British `colonial_rule`, 1822-1835 and onward.
- Unani: British `colonial_rule`, 19th c. to 1947.
- TCM: `indirect_foreign_pressure` from Meiji Japan as model and intermediary, and from Western biomedicine. The report records no treaty-port or semi-colonial control, and the mode assignment is the extractor's reading. [ayurveda, tcm, unani: disruption.colonial_power]
- The corpus therefore contains two colonial-rule ruptures and one rupture under indirect foreign pressure. Both colonial-rule systems and the non-colonized one record abolition-level events, so colonial rule is not shown to be a precondition for those events.

**Abolition attempts.**
- **Ayurveda:** a government order of 28 Jan 1835 abolished the Native Medical Institution and discontinued its Ayurvedic and Unani classes. The extraction also records that the order preceded Macaulay's Minute of 2 Feb 1835, and that the Minute concerns education generally. [ayurveda: disruption.abolition_attempts, disruption.suppression_or_marginalization]
- **TCM:** in 1929 Yu Yunxiu proposed abolishing "old medicine". Practitioners protested on 17 March 1929, and the Nanjing government rescinded the proposal in December 1929. The extraction records that this episode is "often misread as an effective ban". [tcm: disruption.abolition_attempts, disruption.practitioner_response]
- **Unani:** the leaf is `absent`, but see the near-match note in I.1. The absence is a coverage gap in that extraction, not evidence that nothing happened. [unani: disruption.abolition_attempts]
- In both documented cases the events were narrower than the popular narrative. The 1835 order ended state-funded teaching classes. The 1929 measure was a proposal that was rescinded. The 1822 decree was local to the Imperial Academy. These are historians' findings recorded in the extractions and are not tradition claims.

**Post-colonial or post-dynastic breaks.**
- **Unani:** Hamdard split along Partition lines into India, Pakistan (1948) and Bangladesh (1953). The leaf is uncited and a single commercial institution. [unani: disruption.post_colonial_disruption]
- **Ayurveda:** `absent`. The gap pass found only fragments (Wikipedia on Tibbia College members migrating in 1947, and a Bangladesh 1983 ordinance), not direct evidence. [ayurveda: disruption.post_colonial_disruption]
- **TCM:** the Maoist systematization of the 1950s, framed as transformation and not as an institutional split. [tcm: disruption.post_colonial_disruption]
- **Comparison.** A Partition effect is documented for Unani only, through one firm. It is not established for Ayurveda, and Ayurveda's leaf is an addressed-and-not-found gap, not a finding of no effect.

**What each system changed in order to survive (historical-scholarship register).**
- **Ayurveda:** college curricula, printed textbooks, factory-made branded drugs, professional registration that marginalized folk healers, anatomy and laboratory science, and the vocabulary of "science". The report labels this the empirical core of the reinvention thesis. [ayurveda: construct_debate.positions]
- **Unani:** Western anatomy and surgery, madrasas, and Urdu literature and journals. [unani: disruption.colonial_power] The Tibbia College incorporated anatomy and surgery. [unani: revival_and_institutionalization.standardization_events]
- **TCM:**
  - The Republican-era and 1950s reconstruction is described in `disruption.post_colonial_disruption` and `construct_debate.positions`.
  - Specific changes recorded: rebranding as guoyi, a standardized curriculum modelled on Western medical textbooks, and Cheng Dan'an's relocation of points to nerve pathways.
  - The pattern-versus-disease reconciliation is attributed to Lei.
  - [tcm: disruption.practitioner_response, disruption.post_colonial_disruption, construct_debate.positions, theoretical_primitives.relation_to_biomedical_anatomy]
- **Common pattern:** in all three, adoption of biomedical anatomy or science into education or concepts, and organized purist-versus-integrationist splits.
  - Ayurveda: shuddha versus miśra. [ayurveda: revival_and_institutionalization.internal_factions]
  - Unani: Lucknow purists versus Delhi integrationists. [unani: revival_and_institutionalization.internal_factions]
  - TCM: jingfang "pure" classical practitioners versus standardized zhongyi, which Scheid partly treats as nationalist mythology. [tcm: revival_and_institutionalization.internal_factions]
- **Source limits.** TCM's factions leaf is `partial` and rests on a scholar's blog essay (`indirect`). Ayurveda's and Unani's rest on Wikipedia or practitioner-site citations (`indirect`).

## 4. Diagnostic reproducibility

**Which designs exist in which system.** I list them per system with no cross-system ordering.

*Ayurveda.* [ayurveda: diagnostics.reliability_evidence]
- Kurande 2013: clinician-vs-clinician, healthy volunteers, 15 raters, 20 subjects. Average pairwise weighted κ: pulse 0.07, tongue 0.17, prakṛti 0.28.
- Kessler 2019: clinician-vs-clinician, patients, 4 raters, 30 patients. It reports percent agreement of 95% on the final overall diagnosis after a nominal-group consensus procedure, and κ of 0 to 0.4 for constitutional entities.
- Rotti 2014: software-vs-clinician, n = 3,416 healthy subjects, Cohen κ 0.778.
- Rao 2022: instrument-vs-expert, n = 50 healthy subjects, Cohen κ 0.719 and 0.454, read from a review and not from the article.

*TCM.* [tcm: diagnostics.reliability_evidence]
- Jacobson 2019 systematic review, clinician-vs-clinician, 21 studies, population not stated. Mean pairwise agreement 57% across 9 studies (range 19-96) and mean κ 0.34 across 7 studies (range 0.07-0.59).
- Birkeflet 2011: 2 raters, 54 women, qualitative report only. Point selection agreement was poor, and excess/deficiency pattern agreement was moderate to fair.
- Birkeflet 2014: 8 raters, 25 written case histories, κ < 0.20 for patterns.

*Unani.* [unani: diagnostics.reliability_evidence]
- Mojahedi 2014: questionnaire-validation, weighted κ 0.40-0.83 across 39 retained items, n = 35 for test-retest. A review flag records that the abstract says 0.82 and the verify pass changed it to 0.83, unresolved.
- An ICC study (0.62 and 0.64), clinician-vs-clinician, 3 raters, 150 healthy volunteers. The primary paper was not located and the figures come from search snippets, so it is not directly verified.
- A 2026 Shiraz study, 350 healthy workers, Cohen κ from -0.023 to 0.602 depending on construct and comparator. It is labelled questionnaire-validation, but it compares clinical judgment with questionnaires, so the design label is the mapper's.
- Malik 2024: expert panel item selection, no coefficient in the abstract.

**Can the systems be ranked on diagnostic reproducibility? No.**
- The only design present in all three is clinician-vs-clinician. Even among those studies the statistic (weighted κ, percent agreement, pooled κ, ICC), the target (pulse, tongue, prakṛti; heterogeneous TCM patterns; warm-cold and wet-dry axes), the population (healthy volunteers, patients, not stated) and the rater count all differ.
- Ayurveda's best-agreement numbers come from software or instrument comparisons and a consensus procedure. Those are different quantities from clinician-vs-clinician agreement.
- Unani's κ values belong mainly to questionnaire validation, which is a different quantity again.
- I therefore offer no ordering, averaging or side-by-side reading of the coefficients.

**Sign versus synthesis.**
- Ayurveda is filled. In Kessler, agreement on the final diagnosis exceeded chance-corrected agreement on constitutional entities. The extraction says the contrast is the authors' and is not like-for-like. [ayurveda: diagnostics.sign_vs_synthesis]
- TCM is `partial`. No study of individual signs is extracted, although the extraction's own note records that the Jacobson abstract says 2 of the 21 studies assessed signs and gives no results for them. [tcm: diagnostics.sign_vs_synthesis, diagnostics.reliability_evidence]
- Unani is `absent`. The report found no study separating sign-level from integrated agreement, and none of nabz (pulse), baul (urine) or baraz (stool) reliability. [unani: diagnostics.sign_vs_synthesis, self_reported_gaps.inventory]
- Pulse is a named method in all three. [ayurveda, tcm, unani: diagnostics.methods] A pulse-specific reliability figure exists only in Ayurveda's column (Kurande). It is not established for TCM or Unani.

**Correspondence medicine as a class.**
- The codebook's `correspondence_system` leaf is `partial` for Ayurveda, where only a solar-seasonal scheme was confirmed, from an indirect source. It is `filled` for TCM, resting on an open encyclopedia. It is `not_applicable` for Unani, which the extraction says is inferred from the report's silence. [ayurveda, tcm, unani: theoretical_primitives.correspondence_system]
- So only two systems in the corpus carry a wider correspondence scheme. The third has a humoral scheme with no wider scheme recorded, and that recording is unverified.
- The claim "correspondence systems predict low reliability" cannot be tested here. There are two members of the class, with designs that differ from each other and from the single contrast system. The contrast system's own reliability data are mostly of a different design and partly unverified.
- What can be said of each system separately is given above. The class-level question stays open.

**Standardization efforts.**
- Ayurveda: a CCRAS Prakriti Assessment Scale, AyuSoft software and a pulse instrument. [ayurveda: diagnostics.standardization_efforts] The 0.65 target was removed as unconfirmed.
- TCM: WHO and ISO terminology standards, ICD-11 Chapter 26 and training exercises, with "limited demonstrated success" and no agreement threshold stated. [tcm: diagnostics.standardization_efforts]
- Unani: questionnaires, with "no independent gold standard" conceded and no target threshold. [unani: diagnostics.standardization_efforts]

**Report stances (field 18, compared as stances only).**
- Ayurveda: treat diagnosis as non-reproducible.
- TCM: poor reliability, "kappa about 0.34".
- Unani: agreement is "slight-to-moderate" with no gold standard, and flag the absence of pulse data.
[ayurveda, tcm, unani: report_conclusions.recommendations]
The wording is firmest where the reliability literature is largest.

## 5. Institutionalization and legal recognition

**Recognition tiers by jurisdiction** (`legal_status.jurisdictions`). Japan and Korea rows in TCM are excluded because they are siblings treated as different traditions (see `identification.system_boundary`).

| Jurisdiction | Ayurveda | TCM | Unani |
|---|---|---|---|
| India | full medical system | not applicable | full medical system |
| Pakistan | full medical system (no statute recorded; the notes say unverified) | not applicable | statutory registration (1965 Act) |
| Bangladesh | full medical system (unverified) | not applicable | tier null |
| Sri Lanka | full medical system (Act 31 of 1961) | not applicable | tier null |
| PRC, Taiwan | not applicable | full medical system | not applicable |
| Hong Kong, Singapore, Australia, Canada | not applicable, except Australia (below) | statutory registration | not applicable |
| Australia | unregulated (products under TGA; practitioners not under AHPRA) | statutory registration (AHPRA, from 2012) | not applicable |
| Malaysia | statutory registration (Act 775, 2016) | tier null (same Act 775) | not applicable |
| UAE | statutory registration | not applicable | not applicable |
| Switzerland | title protection (2015 diploma) | tier null | not applicable |
| Germany | unregulated | tier null | not applicable |
| United States | supplement/wellness only | supplement/wellness only | supplement/wellness only (grouped with Gulf/UK/EU) |
| UK / EU | unregulated | unregulated (UK) | grouped, supplement/wellness only |
| South Africa | not applicable | not applicable | statutory registration |
| Iran | not applicable | not applicable | tier null (insurance partly covers TPM) |

[ayurveda, tcm, unani: legal_status.jurisdictions]

**Coding flags.**
- Malaysia's Act 775 appears in both the Ayurveda and TCM columns. It is one regulatory fact, not two.
- In India, both Ayurveda and Unani sit under the NCISM Act 2020 and the Drugs and Cosmetics Act. That is one statutory scaffold, not two.
- Some tier differences are coding and not law. The Pakistani Act's title as recorded in Unani's extraction (Unani, Ayurvedic and Homoeopathic Practitioners Act 1965) names Ayurveda. Yet Ayurveda's Pakistan row records no statute and is tier "full medical system", while Unani's is "statutory registration". Sri Lanka's Act covers both, but Unani's tier is null. The Unani extraction says its tier assignments are the mapper's.
- TCM's PRC row says "equal legal footing", while the statute-checked `state_sponsorship` leaf says Article 3 states a policy of equal importance and not legal equivalence. I use the latter. [tcm: legal_status.jurisdictions, revival_and_institutionalization.state_sponsorship]

**What the extractions show about where a tradition sits.** These are associations and not causal findings.
1. **Home region.** Full-medical-system tiers occur in home jurisdictions: India, Sri Lanka and others for Ayurveda, the PRC and Taiwan for TCM, India for Unani. [ayurveda, tcm, unani: legal_status.jurisdictions]
2. **Outside the home region.** Tiers fall to statutory registration where a general T&CM or health-professions statute exists (Malaysia, Australia, Singapore, Canada, Hong Kong, UAE, South Africa), and to supplement-only or unregulated elsewhere. The US is at the lowest tier for all three, and the UK for Ayurveda and TCM.
3. **Same jurisdiction, different tier.** Australia is the cleanest contrast. TCM is registered and Ayurveda's practitioners are not. The extractions give no reason. [ayurveda: legal_status.jurisdictions; tcm: legal_status.jurisdictions]
4. **Product regimes instead of practice regimes.** In the US, EU and Australia, recognition runs through product regimes such as DSHEA, the EU Traditional Herbal Medicinal Products Directive and the TGA. For Ayurveda the extraction spells out that EU registration requires traditional use plus quality and safety, "not efficacy". The EC's own 2008 report is recorded as calling the Directive's simplified route not appropriate for holistic traditions such as Ayurveda. [ayurveda: legal_status.jurisdictions, legal_status.supranational_standards; tcm: legal_status.supranational_standards] No jurisdiction in the corpus is recorded as tying its tier to efficacy evidence.
5. **Diffusion channels differ.** These are historical-scholarship and regulatory facts.
   - TCM: diplomatic opening (Reston, 1971) and Belt and Road commercial and soft-power promotion. [tcm: revival_and_institutionalization.diffusion_abroad]
   - Ayurveda: the Maharishi consumer variant, US professional bodies (NAMA 1998, NAMACB 2017), a Swiss diploma (2015) and Hungarian recognition as naturopathy restricted to doctors. [ayurveda: revival_and_institutionalization.diffusion_abroad, legal_status.jurisdictions]
   - Unani: a South African training programme with statutory recognition, and cupping and herbal practice among Gulf, UK, US and EU diaspora. The South Africa source is an expat guide (`indirect`), with the Act 63 of 1982 link checked on the AHPCSA FAQ. [unani: revival_and_institutionalization.diffusion_abroad, legal_status.jurisdictions]

**Market figures (field 19) cannot explain tiers.**
- TCM carries an unnamed-estimator domestic output figure of about RMB 900 billion (2024, `v1`, `incidental`) and a global range of USD 29 billion to above 280 billion, which the report itself says should be treated as unreliable (`incidental`, commercial research firms, `indirect`). It also carries a company revenue for Yunnan Baiyao (CNY 40.03 billion, 2024, `direct`). [tcm: economics.domestic_market_size, economics.global_market_estimates, economics.major_manufacturers]
- Ayurveda and Unani give named manufacturers with no figures, and domestic and global market leaves are `not_requested` in both. [ayurveda, unani: economics.major_manufacturers]
- These figures say nothing about use, efficacy or safety, and TCM's cannot be set against silence in the other two.

**Education and integration.**
- TCM is documented as a required component of biomedical education in China. [tcm: education_and_licensure.tradition_content_in_biomedical_curriculum] For Ayurveda only an `incidental` disputed JIPMER proposal is recorded, and for Unani the leaf is `not_requested`. The direction cannot be compared across all three.
- India's practitioner counts (Ayurveda 346,240, Unani 50,053, both 2022, from the same Lok Sabha annexure) are descriptive only. Ayurveda's is `incidental` and Unani's leaf is `v1`. TCM's leaf is `not_requested`, so no three-way comparison is possible.

## 6. Literature volume against evidence quality

I treat these as two questions. Volume is field 12 and quality is field 13.

### 6a. Volume and provenance (field 12), with each system's corpus-scale appraisal

- **Ayurveda: `filled`.** Thrigulla et al. is a bibliometric analysis of the AYUSH Research Portal to June 2020. It lists 6,528 clinical-trial articles across AYUSH, of which 3,903 are Ayurveda. Of these, 144 (3.69%) are Grade A (RCT), 725 Grade B and 3,034 Grade C. The abstract's "4.50%" Grade A figure is an unresolved discrepancy. The top 20 journals carry 75.56% of articles. The appraisal is of an institutional portal and is not a systematic world search. No Cochrane-level overview was found. [ayurveda: literature_state.corpus_scale_appraisal]
- **TCM: `partial`.** No whole-corpus appraisal was located. The nearest are an evidence map of 1,874 RCTs of Chinese patent medicines and classic prescriptions, and a bibliometric analysis of 1,908 acupuncture RCTs (2010-2024). Both cover subsets and were read from search summaries. [tcm: literature_state.corpus_scale_appraisal]
- **Unani: `partial`.** No dedicated appraisal was located. The same Thrigulla paper gives 427 Unani articles, of which 209 (48.95%) are Grade A, 95 Grade B and 123 Grade C. The paper is framed around Ayurveda, and the figures were taken from a summary. [unani: literature_state.corpus_scale_appraisal]
- **Status difference is partly an artefact.** The same paper yields `filled` for Ayurveda and `partial` for Unani because of how the reports framed it.
- **Volume comparison.** Only Ayurveda and Unani share a measuring instrument (the portal and the Clinical Trials Registry of India, CTRI). TCM is on different instruments, so a three-way volume ranking cannot be made.
  - Portal: Ayurveda 3,903 articles and Unani 427.
  - CTRI 2009-2020 registrations, from the same paper with the same denominator of 3,632: Ayurveda 2,054 and Unani 366. [ayurveda: literature_state.trial_counts; unani: literature_state.registry_and_reporting_practice]
  - Unani's smaller corpus says it is less studied, not that it was studied and found weaker.
- **A puzzle I cannot resolve.** On the same grading, Grade A is 3.69% for Ayurveda and 48.95% for Unani. Grade A here is a study-design label and not a certainty rating. Unani's figures are unverified against the full text, and Ayurveda's own leaf flags a discrepancy. I draw no conclusion about quality.
- **Registry practice.** Ayurveda: 96.9% prospective for 1,392 trials in 1 July 2018-31 March 2020. Unani: 63.39% prospective across all of 2009-2020. The windows and denominators differ, and Ayurveda's own note says not to combine them. [ayurveda, unani: literature_state.registry_and_reporting_practice] Within the shared 2009-2020 source, the AYUSH-wide retrospective share is 21% and Unani's is 36.61%. TCM's registration leaf is `partial` and uncited. [tcm: literature_state.registry_and_reporting_practice]
- **Geographic concentration.** Ayurveda: mostly India, with no figures (`partial`). TCM: an "enormous share" from China, with no figure. Unani: CCRUM, Indian colleges, Hamdard and Iranian TPM universities. [ayurveda, tcm, unani: literature_state.geographic_concentration_of_trials]
- **Publication bias.** TCM has one specific study (Vickers 1998, data to 1995: all acupuncture trials from China, Japan, Hong Kong and Taiwan were positive, and no trial from China or Russia/USSR found a test treatment ineffective). [tcm: literature_state.publication_bias_findings] Ayurveda's leaf is `absent`, meaning addressed and not found. Unani's is `partial`, an assertion with no named study. [ayurveda, unani: literature_state.publication_bias_findings] The finding exists for TCM only, and the other two leaves record no study. That is not evidence of lower bias there.

### 6b. Evidence quality (field 13), reviewers' own hedging

- **Ayurveda.**
  - Rheumatoid arthritis: a pilot RCT (n = 43) found the Ayurvedic, methotrexate and combination arms approximately equivalent within pilot limits, with the trial underpowered. A 2005 systematic review found that RCTs "fail to show convincingly" efficacy.
  - Ashwagandha for stress and anxiety: a 2024 meta-analysis of 9 RCTs (n = 558) found significant effects, with certainty "low-to-moderate" and substantial heterogeneity.
  - Whole-system treatment of major diseases: the report finds evidence "insufficient, low-quality, or preliminary" from unnamed reviews.
  - [ayurveda: evidence_state.reviews]
- **TCM.**
  - Acupuncture for chronic pain (IPD meta-analysis, 39 trials, 20,827 patients): superior to sham and to no acupuncture. The specific effect is small and contextual effects are larger. No certainty rating is given.
  - Migraine (Cochrane 2016): moderate certainty.
  - Low back pain (Cochrane 2020): low certainty against sham, with a difference below the clinically important threshold, and moderate certainty against no treatment.
  - PC6 nausea: low certainty against sham.
  - Moxibustion for breech presentation: moderate (2023).
  - Lianhua Qingwen for COVID-19: "lacks strong evidence".
  - Tai chi: reviews cover the modality in general and are treated by the report as TCM's own.
  - Australia's 2015 review of 17 natural therapies found no clear evidence of clinical effectiveness.
  - Cupping and qigong: none identified. Most herbal formulas: inconclusive.
  - [tcm: evidence_state.reviews]
- **Unani.**
  - Cupping for low back pain: a 2024 meta-analysis (11 RCTs, 921 participants) described by its authors as high- to moderate-quality evidence, with significant heterogeneity. It covers cupping in general and not Unani hijama specifically.
  - Wet cupping for mental health: a 2022 systematic review found few RCTs, mostly poor, and could not say whether it helps.
  - Post-COVID Unani interventions: a 2025 evidence map of 10 studies reports symptom reduction and favourable safety. No certainty rating is given, and the original "promising but insufficient" wording was not confirmed.
  - Herbal formulations: individual trials only, preliminary.
  - [unani: evidence_state.reviews]
- **Preclinical evidence is kept apart and never stands in for clinical evidence.**
  - Ayurveda: boswellic acids inhibit 5-lipoxygenase in vitro, and Arogyavardhini Vati was tested in rats. [ayurveda: evidence_state.preclinical_and_constituent_evidence]
  - TCM: artemisinin's isolation, which the report calls a drug from the herbal corpus and not validation of TCM theory. [tcm: evidence_state.preclinical_and_constituent_evidence]
  - Unani: isolation of Rauwolfia alkaloids, where reserpine was isolated by Ciba in 1952 and not by Siddiqui. [unani: evidence_state.preclinical_and_constituent_evidence]
- **Borrowed clinical evidence.** All three `evidence_borrowed_from_other_traditions` leaves under field 13 are empty. Unani's extraction treats hijama as its own tradition, so cupping reviews sit in `reviews`.

**What the comparison supports.**
- **Whole-system and multi-herb level.** Each extraction classes evidence at the whole-system or multi-herb-formula level as preliminary or inconclusive. [ayurveda, tcm, unani: evidence_state.reviews] Stronger signals sit at narrower levels: acupuncture for particular conditions, a single herb (ashwagandha) and cupping for back pain. The last covers cupping in general.
- **Only Ayurveda has a whole-system individualized trial recorded**, a pilot (n = 43).
- **Volume does not track quality.** Ayurveda's large portal count contrasts with a handful of named reviews. TCM's large literature is tempered by the publication-bias finding. Unani's small corpus contains one mid-rated general cupping meta-analysis. Nothing in field 12 implies field 13 here.
- **Cupping overlaps TCM and Unani.** TCM's extraction lists cupping as "none identified", while Unani's extraction found a cupping meta-analysis. TCM's "none identified" therefore reflects that report's search and not an absence in the literature. The two columns should not be merged, and the TCM entry is not a finding of no evidence.
- **Methodology disputes (field 16).** All three records describe a dispute about whether standard trial designs fit individualized practice.
  - Ayurveda: whole-system versus single-herb trade-off.
  - TCM: the validity of sham acupuncture, with Vickers and Ernst named.
  - Unani: whether RCT standards apply at all, and sham-cupping blinding.
  - Named parties are given only for TCM.
  - [ayurveda, tcm, unani: contemporary_controversies.research_methodology_disputes]
- **Report stances (field 18, as stances).**
  - Ayurveda: discount diagnosis, and avoid bhasma.
  - TCM: acupuncture is "defensible" for chronic pain, migraine and nausea, and Chinese-language-only trials should be discounted.
  - Unani: cupping is the least-weak case, and herbal formulations are preliminary.
  - [ayurveda, tcm, unani: report_conclusions.recommendations]

## 7. Harm

**Mechanism classes recorded** (`safety.intrinsic_toxicity`, `safety.adulteration_and_contamination`).

| Class | Ayurveda | TCM | Unani |
|---|---|---|---|
| Heavy metal | bhasma/rasaśāstra preparations, deliberately used and contested | contaminant only (lead, arsenic, mercury, no figures) | kushtas (lead compounds, arsenic trioxide) and surma (lead) |
| Plant toxin | ashwagandha hepatic injury | Aristolochia, ephedra, He Shou Wu | none recorded |
| Procedural | none recorded | acupuncture needling | hijama (wet cupping) infections |
| Pharmaceutical adulterant | recognized, no figures, unsourced | named, no figures | steroids in 80% of 29 samples (Unani and homeopathic mixed pool); one single-batch finding |
| Indirect | recognized, unsourced | not recorded | recognized, outcome data limited |
| Interaction | recognized, no data | not recorded | not recorded |

[ayurveda, tcm, unani: safety.intrinsic_toxicity, safety.adulteration_and_contamination]

**Measured figures.**
- Ayurveda: 14 of 70 products (20%) in Boston (JAMA 2004), 40 of 193 (20.7%) sold online (JAMA 2008), and 12 adult lead-poisoning cases in five states (MMWR 2004). [ayurveda: safety.adulteration_and_contamination, safety.documented_adverse_events]
- Unani: one marketed Kushtae Sadaf sample at 28.7 ppm lead against a 10 ppm limit, and surma lead up to 86% (1979) and 0.03-81.37% across 40 samples (1982). [unani: safety.adulteration_and_contamination]
- TCM: Belgian slimming-clinic cohort, 46% of 39 who underwent prophylactic surgery had urothelial carcinoma (NEJM 2000). Taiwan: 151 patients (PNAS 2012). Ephedra poison-centre calls fell from 10,326 (2002) to 180 (2013) after the FDA ban. [tcm: safety.documented_adverse_events]
- These are different products, sampling frames and outcomes. I do not compare prevalences across systems.

**Asymmetries to state carefully.**
- **Plant toxicity.** Documented for Ayurveda and TCM, not established for Unani. Unani's report says it searched for Unani-specific hepatotoxicity case reports with RUCAM scoring and found them absent, and that branded-kushta poisoning case reports are "sparse". [unani: self_reported_gaps.inventory, safety.documented_adverse_events] Unani's corpus is smaller and its literature often aggregates Ayurveda, Siddha and Unani, so absence of reports is not absence of harm.
- **Deliberate metals.** Documented in Ayurveda and Unani. For TCM the extraction records heavy metals only as contaminants, and its modalities list carries no mineral-metal item. [tcm: safety.adulteration_and_contamination, modalities.items, which is `v1`] Whether that reflects the tradition or the report's coverage is not determinable.
- **Procedural harm.** Recorded for TCM (needling) and Unani (hijama), not for Ayurveda. Ayurveda lists bloodletting among its modalities but no harm is recorded. [ayurveda: modalities.items]
- **Wildlife.** Conservation harm is documented for TCM (pangolin, rhino horn, tiger bone, bear bile; figures vary by source and are indicative). It is `not_requested` for Ayurveda and Unani. [tcm: contemporary_controversies.conservation_and_sourcing; ayurveda, unani: contemporary_controversies.conservation_and_sourcing]

**Regulatory response (regulatory fact).**
- **TCM.**
  - The FDA ban on ephedra alkaloid supplements took effect in April 2004 and was upheld in 2006.
  - Aristolochia warnings and bans in the US, Canada, UK and Netherlands followed the Belgian cluster.
  - China removed Guan mu tong in 2003, which is weakly sourced.
  - [tcm: safety.regulatory_actions_taken]
- **Ayurveda.**
  - FDA import alerts, with the extraction noting that the "66-41" label is imprecise.
  - Denmark banned ashwagandha in food in 2023 after a 2020 risk assessment.
  - RIVM (2024) and ANSES (2024) issued warnings, and an EU working group recommended prioritizing ashwagandha (June 2024).
  - India introduced export heavy-metal testing (2005) and pharmacovigilance for ASU&H drugs (2017).
  - [ayurveda: safety.regulatory_actions_taken]
- **Unani.**
  - India's 2005 order on heavy-metal testing of ASU drugs for export.
  - Permissible limits from the Ayurvedic Pharmacopoeia of India for herbal products.
  - A National Pharmacovigilance Programme launched in 2008, lapsed, then reconstituted.
  - [unani: safety.regulatory_actions_taken]
- **Shared Indian measures.** The 2005 export-testing order and the pharmacovigilance programme are ASU-wide. They appear in both Ayurveda and Unani but are one regulatory fact. The 2017 (Ayurveda) and 2008-then-reconstituted (Unani) accounts are compatible but neither was confirmed against primary text.
- **Pattern.** Each foreign regulatory action recorded for TCM and Ayurveda followed a documented case series, cluster or risk assessment. No foreign regulatory action is recorded for Unani. That is a coverage statement and not a finding that none occurred.

**Enforcement gaps recorded in a system's own column.**
- **TCM:** pangolin scales remained in the official Pharmacopoeia despite the CITES Appendix I listing. [tcm: safety.regulatory_actions_taken]
- **Unani:**
  - The pharmacovigilance programme lapsed and was later reconstituted.
  - ASU pharmacopoeias sit outside mainstream harmonization (2023 comparison of nine pharmacopoeias).
  - [unani: safety.regulatory_actions_taken]
- **Ayurveda:** the extraction records a dispute over whether "properly prepared" bhasmas are non-toxic, and records that measured levels exceeded limits regardless of processing. It records no enforcement gap as such. [ayurveda: safety.adulteration_and_contamination]
- **Excluded from Unani's column.** Unani's leaf also contains a "loophole" bullet (intentionally metallic preparations assessed under separate criteria from the 10 ppm ceiling). The extraction's own borrowed leaf identifies this as a claim from an Ayurveda-directed commercial source applied to Unani "by analogy". It is therefore excluded from Unani's column, together with the borrowed ASU-wide toxicology and DILI items. [unani: safety.evidence_borrowed_from_other_traditions] Ayurveda's extraction does not carry it, so it is a lead and not a finding for any system.

## 8. Borrowing against convergence

This chapter rests on `contact_and_borrowing.relationships` in all three systems, which is filled throughout. Status assignments in all three rest on report assertion. Ayurveda's leaf is uncited, TCM's is cited only for the Tai su survival, and Unani's is cited to an aggregator. [ayurveda, tcm, unani: contact_and_borrowing.relationships]

**Demonstrated transmission (documented translation or textual attestation, status demonstrated).**
- Ayurveda to Arabic and Persian medicine: corroborated from both ends (I.2).
- Ayurveda to Tibetan medicine, and China to Tibetan medicine: recorded separately (I.2).
- India/Buddhist to China (TCM only), and China to Persia via the Tanksuqnama (TCM only).
- Prophetic medicine folded into colonial-era Unani, which the extraction says is a mapper choice of evidence type. [unani: contact_and_borrowing.relationships]

**Direct descent (an ancestor, not an exchange).** TCM to kampo and to Korean medicine, and Greek to Unani. Ayurveda's Buddhist and Vedic antecedents are contested. Descent is not borrowing between contemporaries.

**Shared descent.** Unani and Latin-European medicine through the Qanun. [unani: contact_and_borrowing.relationships] Not an exchange.

**Structural parallel.** This is one conceptual family seen from three places, with three different statuses.
- Unani descends directly from Greek humoral medicine, and this is demonstrated.
- Ayurveda's relationship with Greek humoral medicine is coded `parallel` but with status `contested`. The report says the existence or direction of influence is unresolved, with Filliozat arguing early contact and Zysk arguing largely independent development. [ayurveda: contact_and_borrowing.relationships]
- TCM records "Greek humoral medicine and Ayurvedic tridosha" as a parallel, convergence. Unani records Chinese and Tibetan medicine as a parallel, convergence.
- The Ayurveda and Unani extractions record a demonstrated transmission of Sanskrit texts into Arabic and Persian, so a channel existed. The corpus does not say what conceptual content crossed in either direction. I do not infer that the humoral and doṣa schemes are connected, or that they are not.
- Ayurveda's own status of `contested` on a `parallel` kind does not match the codebook's pairing of parallel with convergence. The mapper said the status reflects the report's "unresolved" judgment.

**What convergence and borrowing each claim.**
- Convergence here means similarity with no contact shown by the report. It is not evidence of a shared origin. Shared descent and direct descent are documented through translations or textual attestation in the extractions, but the evidence-type labels describe the report's assertion and not its sources.
- The extractions do not say which similarities are convergent and which reflect transmission beyond the entries above.

## 9. Politicization

**State sponsorship (regulatory fact; historical scholarship where noted).**
- **Ayurveda:** the Chopra Committee (1948), the Central Council of Indian Medicine (1970 Act), the Ministry of AYUSH (2014) and the NCISM Act (2020). It also records India's US$85 million commitment to the WHO Global Traditional Medicine Centre, 2022-2032, within US$250 million. [ayurveda: revival_and_institutionalization.state_sponsorship]
- **TCM:** PRC systematization from the 1950s, the 2016 TCM Law (effective 1 July 2017) with Article 3's "equal importance" policy, COVID-19 promotion and the Belt and Road TCM Development Plan (2016-2020). [tcm: revival_and_institutionalization.state_sponsorship]
- **Unani:** the Ministry of AYUSH, CCRUM, NIUM Bengaluru and NCISM in India, the National Council for Tibb in Pakistan, and Iran's Ministry of Health approval of a Persian-medicine PhD (2007), with insurance coverage for some services. The Nizams of Hyderabad were pre-independence patrons. [unani: revival_and_institutionalization.state_sponsorship]
- The Indian machinery (AYUSH, NCISM) is one set of institutions serving both Ayurveda and Unani, so it counts once.

**Nationalist framing.**
- All three revival contexts record nationalism.
  - Ayurveda: nationalist-tinged revival, with "5,000-year-old" government claims flagged by the report as advocacy. [ayurveda: revival_and_institutionalization.nationalist_framing]
  - TCM: guoyi and anti-imperialist nationalism, with the Belt and Road framing. [tcm: revival_and_institutionalization.nationalist_framing]
  - Unani: Ajmal Khan's Congress presidency (1921), plus critics calling the Iranian revival an "invented tradition". [unani: revival_and_institutionalization.nationalist_framing]
- Ayurveda's nationalist-framing leaf is `partial` with no detailed treatment.

**Pandemic-era promotion.**
- **Ayurveda:**
  - AYUSH-64 was repurposed for COVID-19.
  - Patanjali's Coronil was launched in June 2020. The re-promotion in February 2021 claimed a WHO certificate, which WHO denied, and the CoPP was issued by India's DCGI.
  - The Supreme Court heard IMA v. Patanjali (2022-2024) and contempt charges were dropped in August 2024. The court status rests on news outlets (`indirect`).
  - [ayurveda: contemporary_controversies.politicized_episodes, contemporary_controversies.who_engagement]
- **TCM:** domestic promotion ("three medicines and three formulas", Lianhua Qingwen) drew international criticism of the weak evidence. [tcm: contemporary_controversies.politicized_episodes] The Lianhua Qingwen evidence is recorded as lacking strong support. [tcm: evidence_state.reviews]
- **Unani:** AYUSH and Unani immunity and treatment claims "criticised for outpacing evidence". This is `partial` and thinly sourced, with no named case. [unani: contemporary_controversies.politicized_episodes]
- Promotion is documented for all three, at very different depths. The Ayurveda and Unani cases share the Indian policy context.

**WHO engagement and standards.**
- ICD-11 Chapter 26 (150 disorders, 196 patterns, optional, approved at WHA 2019) and the ISO/TC 249 naming dispute are recorded for TCM. [tcm: contemporary_controversies.who_engagement, contemporary_controversies.politicized_episodes]
- For Ayurveda and Unani the extractions record WHO benchmarks (2022), and Ayurveda adds the GTMC at Jamnagar. Both extractions say ICD-11 is not mentioned in their reports, which is a coverage statement. [ayurveda, unani: contemporary_controversies.who_engagement]
- A contrast on ICD-11 cannot be drawn.

**Integration disputes (within the country of origin).**
- **Ayurveda:** a CCIM notification of 20 Nov 2020 lets postgraduate practitioners perform 58 procedures. The IMA calls it "mixopathy" and held strikes in December 2020 and February 2021. A Supreme Court petition is recorded as unresolved, with a hearing listed for January 2026. The status rests on news outlets. [ayurveda: contemporary_controversies.integration_disputes, legal_status.jurisdictions]
- **Unani:** the same IMA protests and "mixopathy" language, plus Iran's debate over insurance. The litigation statement is uncited, and the Andhra Pradesh example concerns Ayurvedic doctors. [unani: contemporary_controversies.integration_disputes]
- **TCM:** `partial`. The 2016 law's simplified licensing and easier classical-formula approval are called controversial, and critics see provisions chilling criticism. No litigation status is given, and the report does not otherwise describe integration disputes within China. [tcm: contemporary_controversies.integration_disputes]
- **Comparison.** The Indian dispute counts once, since Unani's extraction mostly restates Ayurveda-directed events. TCM's is a different shape, a dispute over licensing under a state policy of integration. The absence of a fuller TCM integration dispute in the extraction is a coverage statement and not a contrast.

**Intellectual property and conservation.** Ayurveda has the TKDL and the 1997 turmeric patent revocation (law-firm source, `indirect`). TCM has Chinese defensive databases, and no named biopiracy case was located. Unani's IP and conservation leaves are `not_requested`. [ayurveda, tcm, unani: contemporary_controversies.intellectual_property] These cannot be compared across all three.

**A claim carried by one memoir.** The Li Zhisui allegation that Mao privately doubted Chinese medicine rests on memoir testimony. [tcm: construct_debate.positions] It is an allegation and is not corroborated elsewhere in the corpus.

---

## Extraction inconsistencies worth knowing

- TCM `legal_status.jurisdictions` (PRC: "equal legal footing") is superseded by the corrected `revival_and_institutionalization.state_sponsorship` (equal importance, not legal equivalence).
- TCM `diagnostics.sign_vs_synthesis` says no sign-level study is reported, while its reliability notes say 2 of 21 reviewed studies assessed signs.
- Unani's `diagnostics.reliability_evidence` carries an unresolved review flag on the Mojahedi κ upper bound (0.82 versus 0.83). Its ICC entry lacks a located primary paper.
- Ayurveda's Grade A share is 3.69% by computation and 4.50% in the abstract, unresolved.
- Unani's `contact_and_borrowing.relationships` labels the Ayurveda exchange "bidirectional" while listing only India-to-Arabic/Persian flows.
- Ayurveda records the Bhore Committee as a dated event in two fields. It is one event.

---

## Findings that hold across every system

Each item rests on filled leaves in all three extractions.

1. **Structure of the construct debate.** Each system has a reinvention camp, a continuity camp allied with state or institutional actors, and a middle position. The Indian two share historiography and so are not independent. [ayurveda, tcm, unani: construct_debate.positions]
2. **Textual core and modern system are distinguished.** Each report separates the textual core from the modern institutional system, as a stance and not as a finding. [ayurveda, tcm, unani: construct_debate.report_adjudication]
3. **Adoption of biomedical science and purist splits.** Biomedical anatomy or science entered education or concepts, and purist-versus-integrationist splits exist in all three. [ayurveda, tcm, unani: construct_debate.positions, revival_and_institutionalization.internal_factions]
4. **No whole-corpus global appraisal.** None of the three has a corpus-scale appraisal built on a systematic world search. Ayurveda's is portal-based, TCM's covers subsets, and Unani's is a stratum of a multi-system portal analysis. [ayurveda, tcm, unani: literature_state.corpus_scale_appraisal]
5. **Whole-system and multi-herb level evidence is preliminary or inconclusive** in each extraction. Stronger signals sit at narrower modality levels. [ayurveda, tcm, unani: evidence_state.reviews]
6. **Integrated diagnostic constructs lack a demonstrated high-reliability result.** Each report flags this as under-established. Ayurveda's report says large multi-rater patient studies are essentially absent, TCM's says the literature is modest, and Unani's found no sign-level or pulse reliability study. Coefficients cannot be ranked across systems. [ayurveda, tcm, unani: self_reported_gaps.inventory, diagnostics.reliability_evidence]
7. **Nationalist framing, state sponsorship and pandemic-era promotion** are documented for all three, at unequal depth. [ayurveda, tcm, unani: revival_and_institutionalization.nationalist_framing, revival_and_institutionalization.state_sponsorship, contemporary_controversies.politicized_episodes]
8. **Legal tier.** Full-medical-system status appears only in home jurisdictions, and the US sits at the lowest tier for all three. [ayurveda, tcm, unani: legal_status.jurisdictions]
9. **Contact claims are weakly cited.** Every system's relationships leaf is uncited, indirect or single-source. [ayurveda, tcm, unani: contact_and_borrowing.relationships]

## Findings that hold for some systems and not others, and why

- **Dating uncertainty.** It is about origin for Ayurveda, layering for TCM and editions for Unani. The difference is partly a difference in canon (attributed authors in Unani) and partly in source quality. No ranking is offered. [chapter 1]
- **Colonial rule and abolition.**
  - Two systems record colonial rule, and TCM records indirect foreign pressure.
  - Formal abolition-level events are documented for Ayurveda and TCM.
  - They are not established for Unani, where the leaf is `absent` and the same 1835 order affected its classes.
  - This reflects how each report sourced its evidence.
  - [chapter 3]
- **Post-colonial break.**
  - Documented for Unani (Hamdard split, single firm, uncited), TCM (1950s systematization), and not established for Ayurveda, where it is an addressed gap.
  - [chapter 3]
- **Reliability designs.**
  - Ayurveda has four designs, TCM one, and Unani two (mostly questionnaire validation).
  - The Unani and TCM reports flag absent or modest sign-level data.
  - Pulse-specific reliability exists in Ayurveda's column only.
  - [chapter 4]
- **Correspondence system.**
  - Present for Ayurveda (partial) and TCM, and not recorded for Unani (inferred from silence).
  - This prevents a test of whether correspondence schemes affect reliability.
  - [chapter 4]
- **Publication bias.**
  - A specific study exists for TCM (Vickers 1998, now old), and no study exists for Ayurveda or Unani.
  - That difference in literature is not a difference in bias.
  - [chapter 6]
- **Plant toxicity, procedural harm, and deliberate metals.**
  - Plant toxicity is documented for Ayurveda and TCM.
  - Procedural harm is documented for TCM and Unani.
  - Deliberate metals are documented for Ayurveda and Unani.
  - The silences reflect reports' coverage and corpus size, and are not contrasts.
  - [chapter 7]
- **Wildlife conservation, IP, and ICD-11.** Covered for TCM or Ayurveda only, and `not_requested` or unmentioned elsewhere. [chapters 7 and 9]
- **Recognition outside the home region.**
  - Australia is the only same-jurisdiction contrast (TCM registered, Ayurveda not).
  - Channels differ: diplomacy and trade for TCM, consumer wellness and professional bodies for Ayurveda, and a training programme for Unani.
  - [chapter 5]

## Questions this corpus cannot answer

- Which system's diagnosis is more reproducible? The designs, statistics, targets and populations differ, and Unani's ICC entry is unverified.
- Whether correspondence-system medicine, as a class, has lower diagnostic reliability. Only two members exist, and the contrast system's status is inferred from silence.
- Whether TCM or Unani pulse diagnosis matches Ayurveda's pulse result. Pulse-specific data exist for Ayurveda only.
- The relative volume of the three literatures. TCM has no whole-corpus appraisal and is measured on different instruments.
- Whether Unani's small corpus and high Grade A share (48.95%) reflect design, selection or summary error. The figures were read from a summary.
- Which system has the worst publication bias. A specific study exists for TCM only.
- Whether TCM's "none identified" for cupping reflects the literature or the report's search, given the Unani cupping meta-analysis.
- Whether TCM uses deliberate mineral or metal preparations, and so whether heavy-metal harm is contaminant-only for TCM.
- Comparative harm prevalence. The products, samples and outcomes differ across the three.
- The effect of Partition on Ayurvedic institutions, and whether Unani's abolition-level record is truly empty.
- Whether the pre-Mughal or Mughal patronage shift toward Unani happened as Ayurveda's single seminar-paper source says. The Unani column has no account of it.
- Whether China to Persia (Tanksuqnama) contact bears on Unani, given Unani's "no contact shown" parallel with Chinese medicine.
- What content crossed in the Ayurveda-Unani text exchange, and whether the humoral and doṣa similarities reflect transmission, shared descent or convergence.
- Whether the corroboration of the Ayurveda-Unani exchange rests on independent sources. The extractions' citations are uncited or indirect and cannot be checked here.
- What predicts recognition tier beyond the home-region association. The extractions give no reason for Australia's split, and market figures cannot be used.
- Whether any jurisdiction's tier depends on efficacy evidence. None is recorded as doing so.
- Whether the outcome of the Indian mixopathy litigation has changed. The record is news-based and stops at January 2026.
