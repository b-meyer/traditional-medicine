# Audit of out/synthesis.md against the three extractions

Method. Every cross-system claim in the analysis was traced to the leaves it cites in work/ayurveda/final.yml, work/tcm/final.yml and work/unani/final.yml. Closely related claims were clustered into one unit, so the counts below are of claim units and not of sentences. Supported units are listed at the end in compressed form.

## Summary

| Class | Count |
|---|---|
| Supported | 60 |
| Overreaching | 15 |
| Unsupported | 5 |
| Miscompared | 7 |
| Total claim units | 87 |
| Traces to no extraction (writer's knowledge), counted separately and overlapping the above | 5 |

The shared-events section is mostly sound. Its one weak match is the pulse-diagnosis "corroboration" (O2). The shared-event counting itself (Macaulay, Bhore, Chopra, Mankah, the NMI order, NCISM, Act 775) is honest, and Bhore is correctly counted once.

The analysis repeatedly states the caveat and then drops it in the headline or in the closing "Findings that hold across every system" list. Examples are the Unani middle position, purist-versus-integrationist splits, the US tier, and "documented for all three".

---

## Overreaching

**O1. "Corroborated from both ends: one exchange" (I.2, Sanskrit texts into Arabic and Persian)**
- Evidence. Ayurveda's entry is the Abbasid Baghdad wave only (786-809). Unani's entry covers three flows: Sanskrit into Arabic in the 8th c., Persian translation from the 14th c., and Indian drugs into pharmacopoeias. [ayurveda and unani: contact_and_borrowing.relationships]
- Only the 8th-c. wave is recorded at both ends. The synthesis admits the asymmetry in the bullets but keeps the two-ended headline. Ayurveda's leaf is uncited, and Unani's is an academia.edu profile that verify could not confirm.
- Fix. Restate as: "The 8th-c. Abbasid translation wave is recorded in both columns. The 14th-c. Persian wave and the drug flow are recorded in the Unani column only."

**O2. Pulse diagnosis: "Both ends record the claim, but only as contested" (I.2)**
- Evidence. Ayurveda's entry is "Islamic and/or Chinese" into Ayurveda, late. TCM's entry has `other_tradition: Multiple (pulse diagnosis origins)`, direction null, `structural parallel`. [ayurveda and tcm: contact_and_borrowing.relationships]
- Nothing in the TCM leaf names Ayurveda as a party. This pairs two entries because both carry the label "pulse".
- There is also a tension. Ayurveda posits a possible China-to-India flow, and TCM records no outflow to India.
- Fix. Treat them as two independent contested entries. Ayurveda records a contested pulse borrowing. TCM records an unspecified "multiple origins" parallel. Do not call this corroboration of the contest.

**O3. "Each has a reinvention camp, a continuity camp ... and a middle position" (Ch2, Finding 1)**
- Evidence. Ayurveda names Dominik Wujastyk as a middle and TCM names Scheid. Unani names no scholar as a middle. Its "middle" is `report_adjudication`, which is marked "Report's stance, not consensus". Speziale's "complicates simple invention" is marked the report's own inference. [unani: construct_debate.positions, report_adjudication]
- This counts a report's own conclusion as a scholarly position.
- Fix. "Reinvention and continuity camps are recorded in all three. A named scholarly middle is recorded for Ayurveda and TCM. Unani's middle is the report's own stance."

**O4. "The debates are not independent" (Ch2)**
- Evidence. Hardiman appears only in Unani's positions, not in Ayurveda's. [unani: construct_debate.positions] The only shared name is Sivaramakrishnan. In Ayurveda this is a report-listed group with no individual work. In Unani it is a specific Punjab monograph. [ayurveda and unani: construct_debate.positions]
- Name overlap alone does not show shared historiography.
- Fix. "Sivaramakrishnan is named in both. Whether the two rest on the same works is not recorded. Hardiman groups the two systems but is recorded in the Unani column only."

**O5. "Both colonial-rule systems and the non-colonized one record abolition-level events" (Ch3)**
- Evidence. Unani's `disruption.abolition_attempts` is `absent`. The 1835 Unani classes appear only in Ayurveda's leaf and in Unani's gap note, which was not recorded as a finding. The synthesis contradicts itself in its closing section ("not established for Unani").
- TCM's 1929 event is a proposal that was rescinded.
- "Non-colonized" is not in the TCM extraction, which says only that the report records no treaty-port or semi-colonial control (see T1).
- Fix. "Abolition-level events are recorded for Ayurveda (one institution, 1835) and TCM (a proposal, 1929). Unani's leaf is absent. The data cannot support any inference about colonial rule as a precondition."

**O6. "In both documented cases the events were narrower than the popular narrative" (Ch3)**
- Evidence. Only TCM's leaf says the 1929 episode is "often misread as an effective ban". [tcm: disruption.abolition_attempts]
- Ayurveda's leaf corrects the report's own earlier error about the Minute. It describes no popular narrative.
- The statement also generalises from two systems and three events.
- Fix. Restrict to TCM. For Ayurveda say "the extraction corrects the report's dating of the abolition relative to the Minute".

**O7. Partition effect "documented for Unani only" (Ch3, Findings "some not others")**
- Evidence. [unani: disruption.post_colonial_disruption] is uncited, `unverifiable`, and its only sources are company sites and Wikipedia. The Partition year is "not stated in report".
- Unani's own `disruption.period` note says it removed "post-1947 Partition breaks" because no source was found.
- The leaf records company foundings (Hamdard Pakistan 1948, Bangladesh 1953). The Partition framing is the report's.
- The synthesis also puts this beside TCM's 1950s systematization, which its own leaf frames as "rather than institutional split".
- Fix. "Unani asserts a Hamdard division after Partition, uncited and unverified. The Unani column itself removed a Partition claim elsewhere as unsourced. TCM's entry is a different kind of break."

**O8. "Purist-versus-integrationist splits exist in all three" and "organized" (Ch3 common pattern, Finding 3)**
- Evidence. The TCM leaf is `partial`. It has one split, jingfang "pure" versus standardized zhongyi, and no integrationist faction. Its note says "Scientized/integrative TCM as a named faction, and dated splits, not found" and that it "gives no dated organizational split or named institutional factions". [tcm: revival_and_institutionalization.internal_factions]
- Ayurveda and Unani cite Wikipedia or practitioner sites.
- "IMA/AYUSH" is not an Ayurveda faction.
- Fix. "A purist-versus-integrationist split is recorded for Ayurveda (Sen versus Sharma) and Unani (Lucknow versus Delhi), both on indirect sources. TCM records a purist classical-formula contrast with state TCM and no integrationist faction."

**O9. "Only two systems carry a wider correspondence scheme" (Ch4)**
- Evidence. Ayurveda's leaf is `partial`. Only the solar-seasonal scheme was confirmed, and "any wider cosmological correspondence" was "not verified". TCM's is wuxing and wuyun liuqi correlative cosmology. [ayurveda and tcm: theoretical_primitives.correspondence_system]
- These are not the same kind of scheme, so the two-member class is not established.
- Fix. "TCM records a correlative-cosmology scheme. Ayurveda confirms a seasonal scheme only. Unani's entry is inferred from silence."

**O10. "The US is at the lowest tier for all three" and "full-medical-system only in home jurisdictions" (Ch5 items 1-2, Finding 8)**
- Evidence. TCM's US row has tier `supplement/wellness only`, yet its scope says "acupuncture licensed state by state" with state boards and NCCAOM. The row contradicts its own tier. Unani's US entry is a grouped "Gulf / UK / US / EU" row.
- Many tiers are mapper or extractor assignments. The TCM note says "extractor inferences". Unani says "mapper assignments". Ayurveda's Nepal, Bangladesh and Pakistan rows are unverified.
- Fix. "US tier is supplement-only for Ayurveda. TCM's US tier label conflicts with state acupuncture licensure. Unani's is a grouped row." Mark the home-region pattern as resting on mapper-assigned tiers.

**O11. "Tiers fall to statutory registration where a general T&CM or health-professions statute exists (Malaysia, Australia, Singapore, Canada, Hong Kong, UAE, South Africa)" (Ch5 item 2)**
- Evidence. Singapore (TCM Practitioners Act), Canada (TCM Act 2006) and Hong Kong (Chinese Medicine Ordinance) are TCM-specific statutes. UAE `statute: null`. [tcm and ayurveda: legal_status.jurisdictions]
- Only Malaysia, South Africa and Australia (for TCM) fit "general". Australia also has Ayurveda unregulated under the same scheme.
- Fix. Drop "general" and split into system-specific statutes, general statutes, and UAE (no statute recorded).

**O12. "In the US, EU and Australia, recognition runs through product regimes" (Ch5 item 4)**
- Evidence. This is true for Ayurveda in Australia (TGA, practitioners unregistered). TCM's Australian row is practitioner registration under AHPRA. [ayurveda and tcm: legal_status.jurisdictions]
- Fix. Name the system for each jurisdiction.

**O13. "Each foreign regulatory action recorded for TCM and Ayurveda followed a documented case series, cluster or risk assessment" (Ch7)**
- Evidence. Only two links are recorded. One is the Aristolochia warnings after the Belgian cluster. The other is the Denmark ban after the 2020 DTU assessment.
- The ephedra ban has outcome data only (poison-centre calls fell after it). The FDA import alerts, Health Canada and TGA advisories, the UK FSA consultation and the RIVM and ANSES warnings have no recorded antecedent. [tcm and ayurveda: safety.regulatory_actions_taken]
- Fix. State the two recorded links only. Note also that the TCM leaf says the April 2004 ephedra effective date was "not confirmed".

**O14. "Pandemic-era promotion documented for all three" (Ch9, Finding 7)**
- Evidence. Unani's leaf is `partial`, uncited and "thinly sourced", with "no named court case or state endorsement dates". [unani: contemporary_controversies.politicized_episodes]
- Ayurveda has named episodes (Coronil, AYUSH-64) and TCM has three medicines and three formulas plus Lianhua Qingwen.
- Fix. "Documented for Ayurveda and TCM. Asserted in one uncited sentence for Unani."

**O15. "Unani's canon leaves cite a reference work directly" (Ch1, source strength)**
- Evidence. The S1 Historia Medica citation attaches to the Qanun claims only. Other dates and figures are "uncited in report" or attributed in text to other works. [unani: foundational_texts notes, dated_events, key_figures]
- The synthesis uses this to argue the Unani canon's "apparent firmness may partly reflect better sourcing".
- Fix. "Direct sourcing covers the Qanun. The Razi and al-Majusi dates and other figures are uncited."

---

## Unsupported

**U1. "2026 Shiraz study ... Cohen kappa from -0.023 to 0.602" (Ch4)**
- Evidence. These are CI bounds. The leaf's κ values are 0.081 to 0.512 for clinical versus questionnaire, and 0.132 to 0.366 for questionnaire versus questionnaire. The CIs are 0.422-0.602, 0.368-0.656 and -0.023 to 0.185. [unani: diagnostics.reliability_evidence]
- Fix. Report the κ values, not the CI endpoints.

**U2. "The wording is firmest where the reliability literature is largest" (Ch4)**
- Evidence. No field records literature size as a measure of the report's firmness. Ayurveda's report is the firmest ("non-reproducible") on four studies and says large studies are "essentially absent". [ayurveda and tcm: report_conclusions, self_reported_gaps.inventory]
- Fix. Delete it.

**U3. "Ayurveda has four designs, TCM one, and Unani two" (Findings "some not others")**
- Evidence. Ayurveda has four studies but three designs: clinician-vs-clinician (Kurande, Kessler), software-vs-clinician (Rotti) and instrument-vs-expert (Rao). [ayurveda: diagnostics.reliability_evidence]
- The same bullet says the TCM report flags "absent or modest sign-level data". TCM's leaf says the report "does not explicitly contrast" signs, and the modest-literature caveat is separate.
- Fix. "Three designs across four studies."

**U4. "One conceptual family seen from three places" (Ch8)**
- Evidence. The three parallels concern different pairs. Ayurveda is paired with Greek humoral, TCM with Greek humoral plus tridosha, and Unani with Chinese and Tibetan. Only Unani's Greek entry is descent. [ayurveda, tcm and unani: contact_and_borrowing.relationships]
- No field says these form one family. This merges entries because of label similarity.
- Fix. List the pairs separately.

**U5. Provenance note: "None [of the v1 leaves] carries a comparative claim here"; Unani `preclinical_and_constituent_evidence` listed as v1**
- Evidence. Ch7 uses [tcm: modalities.items, v1] for the "no mineral-metal item" comparison. Ch5 uses Unani `practitioner_estimate` (v1) in a side-by-side count.
- Unani's preclinical leaf is `source_report: verify` with `replaced_from: v1`, not v1.
- Fix. Correct the note, and either drop or caveat the v1-dependent comparisons.

---

## Miscompared

**M1. "Volume does not track quality" (Ch6b)**
- The synthesis earlier says TCM volume cannot be placed on a shared instrument. Here it asserts "TCM's large literature".
- Evidence. The TCM extraction has only subset counts (1,874 RCTs, 1,908 acupuncture RCTs) and the "enormous share" statement.
- Unani's cupping meta-analysis is called "mid-rated". The leaf says "high- to moderate-quality" by the authors, and it is a general-cupping review. [tcm and unani: literature_state, evidence_state.reviews]
- Fix. Volume and quality can be compared only for Ayurveda and Unani, on the shared portal. Drop the three-way pattern.

**M2. "Each extraction classes whole-system or multi-herb evidence as preliminary or inconclusive" (Ch6b, Finding 5)**
- Evidence. Ayurveda's basis is "Cochrane and other rigorous reviews (unnamed)". TCM's is `none identified`, "report classes them as inconclusive". Unani's is "individual trials only" plus "report says most remain preliminary".
- This is the reports' own conclusions, with no named review at that level.
- TCM and Unani have no whole-system or pattern-individualised entry. Only Ayurveda has one (Furst).
- Fix. "The three reports each characterise herbal or whole-system evidence as preliminary. This is report stance, not an evidence finding."

**M3. "Stronger signals sit at narrower levels ... cupping for back pain" (Ch6b)**
- Evidence. The Unani signal is a general-cupping meta-analysis, not Unani hijama. [unani: evidence_state.reviews] Unani's own geographic note says cupping research clusters in "India, Iran and China". [unani: literature_state.geographic_concentration_of_trials]
- TCM's column says cupping has "none identified". The extraction's empty `evidence_borrowed_from_other_traditions` depends on treating hijama as a separate tradition, which the synthesis accepts.
- The certainty frames also differ: authors' self-rating, GRADE, and "low-to-moderate".
- Fix. Mark the cupping signal as general-modality evidence not attributable to Unani. Do not rank certainty across systems.

**M4. Finding 6: "Integrated diagnostic constructs lack a demonstrated high-reliability result"**
- Evidence. This rests on report self-statements (`self_reported_gaps`). The extractions contain high values in other designs: Kessler 95% agreement on the final diagnosis, Rotti κ 0.778, and Mojahedi weighted κ up to 0.83. [ayurveda and unani: diagnostics.reliability_evidence]
- Ch4 itself says these are not comparable. "Large patient studies absent" (Ayurveda) is not the same statement as "no high reliability".
- Fix. Say: "No extraction reports a high chance-corrected agreement from a clinician-vs-clinician study of the integrated diagnosis in a patient population. The reports flag this as a gap."

**M5. Unani "own column" enforcement gaps and regulation (Ch7)**
- The synthesis says borrowed ASU items are excluded from Unani's column.
- Evidence. It still lists Unani's pharmacovigilance lapse. That item is sourced to S27, an Ayurvedic heavy-metal paper the extraction itself flags `claim_match: mismatch` and lists among borrowed sources. It also lists the nine-pharmacopoeia ASU comparison, and "permissible limits from the Ayurvedic Pharmacopoeia of India". [unani: safety.regulatory_actions_taken, safety.evidence_borrowed_from_other_traditions]
- Fix. Move these to the shared Indian measures, where they are already noted as one fact. Remove them from "enforcement gaps in a system's own column".

**M6. "The mainstream TCM position is to treat it as invention" (Ch2)**
- Evidence. This rests on the report's own phrasing ("scholarly majority", "near-consensus"). The same extraction records that Lei and Andrews place the change earlier and that Scheid is "the most cited middle position". [tcm: construct_debate.positions, report_adjudication]
- Fix. "The TCM report characterises invention as the majority view."

**M7. India practitioner counts side by side: Ayurveda 346,240, Unani 50,053 (Ch5)**
- Evidence. Ayurveda's leaf is `incidental` and Unani's is `source_report: v1`. [ayurveda and unani: identification.practitioner_estimate] TCM's leaf is `not_requested`.
- Both figures cite the same Lok Sabha annexure directly, so the risk is low, but the synthesis's own rule bars comparisons that rest only on v1 or incidental leaves.
- Fix. Present as two descriptive counts with the provenance caveat, or drop.

---

## Claims tracing to no extraction (writer's knowledge)

- **T1. "The non-colonized one" (TCM, Ch3).** The extraction says only that the report records no treaty-port or semi-colonial control. Absence of a record is not "non-colonized". Remove.
- **T2. The "popular narrative" of the 1835 Ayurveda abolition (Ch3).** No field describes one. Remove or source.
- **T3. "One conceptual family" (Ch8).** See U4.
- **T4. The firmness-follows-literature-size claim (Ch4).** See U2.
- **T5. "Diaspora" as the channel for Unani cupping and herbal practice in the Gulf, UK, US and EU (Ch5 item 5).** The leaf says "practice as cupping/herbal CAM". Only surma use "among South Asian immigrants in the UK" is tied to a diaspora.

Also unsourced within the extractions: the Unani "mid-rated" label for the cupping review (M1).

---

## Shared events and corroborated exchanges: verdicts

- **Macaulay's Minute.** Real match. Both extractions carry the 2 Feb 1835 date, and both cite the text.
- **Bhore.** Real, counted once. Ayurveda's two entries are correctly merged. One citation slip: the "secondary sources say it did not mainly address indigenous medicine" remark sits in Unani's `suppression_or_marginalization`, not in `disruption.dated_events` as cited.
- **Chopra.** Real match.
- **Mankah and the Abbasid translation.** The match rests on description and overlapping date. The moderate-confidence flag is appropriate, and both ends are uncited.
- **Near-matches.** All handled correctly. The WHO near-match citation is garbled ("unani: disruption..., see ..."). Correct it to the Unani `legal_status.supranational_standards` and `revival_and_institutionalization.dated_events` leaves.
- **Sanskrit-to-Arabic/Persian exchange.** Real for the 8th-c. wave only (O1).
- **Pulse diagnosis.** Not a verified match (O2).
- **Tibetan, Buddhist-to-China, and Tanksuqnama.** Correctly kept single-ended or non-corroborating.

## Supported units (compressed list)

1 Macaulay; 2 Bhore; 3 Chopra; 4 Mankah/Abbasid event match; 5 NMI order as one event in one column; 6 WHO benchmarks near-match; 7 NCISM Act as one statute; 8 1822 events unrelated; 9 Rgyud bzhi near-match; 10 Tibetan as two exchanges; 11 India/Buddhist to China TCM-only; 12 China to Persia versus Unani "convergence" as tension; 13 kinds-distinct table; 14 canon texts and three kinds of dating uncertainty (no ranking); 15 external anchors; 16 scope differences (variants); 17 report adjudications compared as stances; 18 loss of patronage established for none; 19 colonial_power modes; 20 abolition attempts per leaf (TCM, Ayurveda; Unani absent); 21 post-colonial leaf statuses (Ayurveda absent as a gap); 22 survival changes per system; 23 reliability designs listed per system (except U1); 24 no ranking of reliability; 25 sign versus synthesis; 26 pulse-specific figure only in Ayurveda; 27 standardization efforts; 28 field 18 stances labelled as stances; 29 legal table and coding flags (Act 775 once, NCISM scaffold once, PRC footing); 30 Australia contrast; 31 diffusion channels; 32 market figures cannot explain tiers; 33 education and integration direction not comparable; 34 corpus-scale appraisals per system; 35 portal and CTRI volume for Ayurveda and Unani only; 36 registry practice with windows noted; 37 geographic concentration and publication-bias asymmetry stated as coverage; 38 per-system reviews; 39 preclinical kept apart; 40 cupping overlap and TCM "none identified" caveat; 41 methodology disputes; 42 harm mechanism table; 43 measured figures not compared; 44 plant-toxicity asymmetry hedged; 45 deliberate metals hedged; 46 procedural harm; 47 wildlife; 48 shared Indian regulatory measures counted once; 49 descent and shared descent; 50 Ayurveda parallel-contested mismatch and "no content crossed"; 51 state sponsorship with shared Indian machinery counted once; 52 nationalist framing; 53 WHO and ICD-11 no contrast; 54 integration disputes counted once; 55 IP and conservation not comparable; 56 Finding 2; 57 Finding 4; 58 Finding 9; 59 correspondence class untestable; 60 TCM dating incomplete.

## Other defects, not counted as claims

- The "Extraction inconsistencies" section is accurate. It omits that Ayurveda's `who_engagement` still carries "developed with the Jamnagar institute", which the `supranational_standards` leaf removed as unsupported.
- Ajmal Khan's 1921 Congress role is "acting president" in Unani's `dated_events` and "Congress President" in `nationalist_framing`.
- Unani's reliability base (Mojahedi, Shiraz, the ICC study) is Iranian Persian-medicine work. Unani's `system_boundary` codes that as the same system, but the synthesis does not say so when comparing designs. Only Malik 2024 is Indian Unani.
