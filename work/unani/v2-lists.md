# Unani v2 — closing lists

## 1. Absent

- `fields.diagnostics.sign_vs_synthesis` — The report does not separate agreement on individual signs from agreement on the integrated judgment. Missing: Unani/Persian-medicine studies reporting inter-rater agreement on individual signs (pulse characteristics, urine colour/sediment, physique/skin signs) separately from agreement on the final mizaj classification.
- `fields.colonial_disruption.abolition_attempts` — No formal proposal, vote or legislative attempt to abolish or ban Unani/hakim practice in British India or the princely states is reported. Missing: any such proposal, with date and outcome.
- `fields.literature_state.corpus_scale_appraisal` — No bibliometric analysis, evidence map or overview of the Unani clinical literature as a whole. The only corpus-type appraisal is modality-level (Cha et al. 2021 cupping evidence map, given without numbers). Missing: a bibliometric analysis or evidence map of Unani (and/or Traditional Persian Medicine) clinical trials, with total counts and years.
- `fields.literature_state.trial_counts` — Volume is called "substantial" with no numbers. Missing: counts of Unani RCTs and other clinical trials overall and by modality (herbal formulations, hijama, regimenal therapies), e.g., from CTRI/IRCT registries or CCRUM output.
- `fields.contemporary_controversies.conservation_and_sourcing` — Not mentioned. Missing: sustainability or overharvesting of Unani plant, animal and mineral raw materials, and supply-chain substitution disputes.
- `fields.contemporary_controversies.intellectual_property` — Not mentioned. Missing: biopiracy or patent disputes over Unani formulations, inclusion of Unani texts in defensive traditional-knowledge databases, and Nagoya Protocol/ABS exposure.

Specific gaps inside partial leaves (search targets):
- `fields.contemporary_controversies.who_engagement` — Unani's status in ICD-11; WHO collaborating centres for Unani.
- `fields.contemporary_controversies.politicized_episodes` — specific COVID-19 Unani protocols or products promoted by AYUSH/CCRUM, with dates and any regulatory or judicial response.
- `fields.colonial_disruption.practitioner_response` — names and founding dates of hakim professional bodies or conferences in colonial India.
- `fields.literature_state.publication_bias_findings` — any specific study documenting publication bias in Unani/TPM trials.
- `fields.literature_state.registry_and_reporting_practice` — trial-registration rates and reporting-guideline adherence.
- `fields.canon_and_transmission.redaction_history` — when and where the "Unani" label emerged, and the redaction stages of the Indo-Persian corpus.

## 2. Not requested

- `fields.identification.practitioner_estimate`
- `fields.modalities.items`
- `fields.materia_medica.pharmacological_framework`
- `fields.materia_medica.flagship_agents`
- `fields.materia_medica.preparation_traditions`
- `fields.education_and_licensure.degree_programs`
- `fields.education_and_licensure.duration`
- `fields.education_and_licensure.accrediting_body`
- `fields.education_and_licensure.licensure_requirements`
- `fields.education_and_licensure.biomedical_content_in_curriculum`
- `fields.contact_and_borrowing.corroborated_by` (deliberately unset; computed at synthesis, not a prompt gap)

Note: every leaf above except `corroborated_by` carries incidental content in `value`, which the report mentioned in passing. None is a search target.

## 3. Unclear or indirect sourcing

Indirect (weak source type):
- `fields.construct_debate.positions` — Attewell's reconstruction thesis. Source: S29, an Exotic India Art bookseller listing.
- `fields.construct_debate.positions` — Seema Alavi's "new Unani and new hakim" claims. Source: S30, a ResearchGate entry for a review of Attewell's book. **The source does not match the claim.**
- `fields.construct_debate.positions`; `fields.contact_and_borrowing.relationships` — Speziale's Persian-Ayurveda translation movement. Source: S31, an academia.edu profile page.
- `fields.colonial_disruption.practitioner_response`; `fields.revival_and_institutionalization.key_figures`; `fields.revival_and_institutionalization.internal_factions` — Ajmal Khan vs. the purist Lucknow (Azizi) school. Source: S6, greekmedicine.net (practitioner/enthusiast website).
- `fields.legal_status.jurisdictions` (India); `fields.revival_and_institutionalization.dated_events` — NCISM Act 2020 repealed the IMCC Act 1970. Source: S7, a PIB state press release about a *proposed amendment*.
- `fields.legal_status.jurisdictions` (India); `fields.education_and_licensure.accrediting_body`; `licensure_requirements` — NCISM operational 2021, Board of Unani/Siddha/Sowa-Rigpa, NEET/NExT. Source: S8, Wikipedia.
- `fields.legal_status.jurisdictions` (India); `fields.safety.regulatory_actions_taken` — Drugs and Cosmetics Act Chapter IVA, Schedule T, Rule 158B. Source: S10, legalcorner.org.
- `fields.legal_status.jurisdictions` (Pakistan); `fields.contemporary_controversies.politicized_episodes` — September 2024 NCT merger. Source: S12, Wikipedia.
- `fields.legal_status.jurisdictions` (South Africa); `fields.identification.alternate_names`; `fields.education_and_licensure.*` — the entire South African entry (2001 recognition, AHPCSA, Act 63 of 1982, 2007 officiation, UWC training, SAHPRA). Source: S16, an Expat Focus expat guide.
- `fields.safety.regulatory_actions_taken`; `fields.revival_and_institutionalization.standardization_events` — AYUSH heavy-metal order of 14 October 2005. Source: S25, a Scribd upload.
- `fields.safety.regulatory_actions_taken`; `fields.safety.evidence_borrowed_from_other_traditions` — permissible limits (Pb 10 / As 3 / Hg 1 / Cd 0.3 ppm) and the kushta/bhasma carve-out. Source: S26, Auriga Research, a commercial testing-lab webpage.
- `fields.evidence_state.reviews` — wet cupping for mental health, trials "of poor quality". Source: S20, a university library catalog record of a DOAJ entry.

Unclear (source-claim mismatch or unresolved):
- `fields.diagnostics.reliability_evidence` — expert-vs-expert ICC 0.62/0.64 (3 raters, 150 volunteers). Source: S2, whose title describes a classification-tool mizaj study that fits the report's J48 work, not a Persian three-expert ICC study.
- `fields.safety.adulteration_and_contamination`; `documented_adverse_events` — Haq & Khan 1982 surma lead levels and UK surma poisoning clusters. Source: S22, whose bibliography title is only "JPMA - Journal Of Pakistan Medical Association". The article cannot be confirmed, and the UK-cluster claim may not be supported by S22.

Uncited (named inline without a [Sn] marker, or no source at all):
- `fields.diagnostics.reliability_evidence` — Mojahedi et al. 2014 weighted κ 0.40–0.82.
- `fields.evidence_state.reviews` — Zhang et al. 2024 cupping meta-analysis (11 trials, 921 participants); AlBedah 2011; Kim et al.; IJMR 2018 psoriasis RCT; RA vs. celecoxib RCT.
- `fields.safety.intrinsic_toxicity`; `fields.materia_medica.flagship_agents` — Mustehasan & Azhar 2022 review of lead/arsenic ingredients.
- `fields.safety.adulteration_and_contamination` — Aslam, Davis & Healy 1979 (surma lead up to 86%); Jawarish Shahi 2026 contamination.
- `fields.safety.documented_adverse_events` — PMC10061885; PMC8059418; J Forensic Leg Med 2025 hijama death.
- `fields.identification.practitioner_estimate` — ~60,000 hakims (Hamdard via WHO EMRO); 39,584 (Saeed et al. 2011).
- `fields.canon_and_transmission.external_dating_anchors` — Aga Khan Museum 1052 CE manuscript; NLM MS A 53.
- `fields.canon_and_transmission.*` — Hunayn's 129/~100 titles (Encyclopaedia of Islam; Lamoreaux 2016); dates and authors of al-Hawi, Kamil and Qanun; Speziale on apocrypha; Gutas and Sabra.
- `fields.construct_debate.positions` — Liebeskind, Hardiman, Sivaramakrishnan, Quaiser, Schmidt Stiedenroth, TPM critics, continuity defenders.
- `fields.theoretical_primitives.*` — the entire theoretical framework.
- `fields.colonial_disruption.*` — Macaulay 1835; Bhore Committee 1946.
- `fields.revival_and_institutionalization.*` — Hamdard dates, Chopra Committee 1948, Siddiqi, Nizam patronage (self-flagged as light), Mudaliar/Shrivastava/Udupa committees, Unani Pharmacopoeia and NFUM.
- `fields.legal_status.jurisdictions` — Bangladesh, Sri Lanka, Gulf/UK/US/EU; Ministry of AYUSH; NIUM; UAH Act 1965.
- `fields.contemporary_controversies.who_engagement` — WHO benchmarks of 11 February 2022 and 2010 editions; WHO terminology.
- `fields.contemporary_controversies.integration_disputes` — IMA mixopathy dispute, Maharashtra CCMP, Andhra Pradesh December 2025, Bombay HC/Supreme Court litigation, "Dr" prefix.
- `fields.literature_state.*` — geographic concentration, publication bias, in-house journals.

## 4. Schema misfit

1. **No status for "not requested but incidentally covered."** Fields 6, 7, 11 and `practitioner_estimate` had no prompt question, but the report gives real content for them in passing. They are marked `not_requested` with the content kept in `value`. The `filled`/`partial` vs `not_requested` choice forces a loss either way. Proposed: an `incidental` status (content present, coverage not systematic, not a search target).
2. **No status for synthesis-computed leaves.** `corroborated_by` must be present and carry a status but must be left unset. `not_requested` is used as a stand-in. Proposed: a `deferred` status for leaves computed at synthesis.
3. **Borrowed-evidence flag exists only in field 14.** Three of five reliability studies in field 5 are Iranian "Persian medicine" (TPM) research. The cupping reviews in field 13 draw on trials the report says cluster in China, a tradition it calls convergent. Proposed: add `evidence_borrowed_from_other_traditions` leaves to fields 5 and 13.
4. **System-boundary problem.** The report treats Traditional Persian Medicine (Iran) partly as the same system and partly as a sibling revival, with its own institutions, legal status and evidence base. It also groups Unani with Ayurveda, Siddha and Sowa-Rigpa under ASU/NCISM regulation. Proposed: a field 1 leaf `system_boundary` (sibling or overlapping traditions, and which fields' content derives from them).
5. **Field 15 status vocabulary lacks "common descent."** The report explicitly frames the Greek/Galenic relation as "shared ancestry, not borrowing". Proposed: add `common descent` to the field 15 `status` or `evidence_type` vocabulary.
6. **No place for citation-integrity flags.** S2 and S30 appear attached to claims their titles do not match. This can only go in `notes`. Proposed: an optional `claim_match: matches | mismatch | unverifiable` sub-key on the citation object.
7. **Report content with no field: revision thresholds and recommendations.** The report states conditions that would change its conclusions: a complete critical Qanun edition; a multi-centre mizaj study with kappa >0.6; pre-registered, independently replicated double-blind RCTs; loophole-free heavy-metal limits with post-market surveillance. It also gives staged practice recommendations. Proposed: a field `revision_thresholds` (`{domain, threshold, would_change}`).
8. **Field 8 framing is South Asia-only.** Partition, which split Hamdard into Indian and Pakistani institutions, is a post-colonial disruption the report mentions but does not date. Field 8 has no leaf for post-colonial state partition. Neither field 8 nor field 9 fits Iran's non-colonial state-driven revival well.
9. **Field 10 has no slot for supranational normative instruments.** The WHO Unani training and practice benchmarks (2022) are not a jurisdiction and were placed in field 16 `who_engagement`.
