# Unani v1: closing lists

## 1. Absent

- `fields.canon_and_transmission.dating_and_authorship_disputes`: no named scholars or positions on dating/authorship of the foundational texts (Hippocratic and Galenic works; al-Hawi, Kamil al-Sina'a, Canon, Kitab al-Tasrif).
- `fields.theoretical_primitives.nosology`: no account of the Unani disease-classification scheme (Canon's categories; modern Unani nosology; any mapping of Unani disease terms to ICD).
- `fields.colonial_disruption.colonial_power`: colonial power/administration not named; report says only "colonial biomedicine".
- `fields.colonial_disruption.abolition_attempts`: no formal proposals, votes or outcomes to abolish or de-recognize Unani in India/Pakistan, with dates.
- `fields.colonial_disruption.dated_events`: no dated colonial-era policy events affecting Unani in South Asia.
- `fields.revival_and_institutionalization.nationalist_framing`: no treatment of the role of Unani revival (Ajmal Khan, Tibbia College) in Indian nationalist or Muslim identity politics, or its framing in Pakistani health policy.
- `fields.revival_and_institutionalization.internal_factions`: no named purist versus integrationist factions among hakims.
- `fields.literature_state.corpus_scale_appraisal`: no whole-system bibliometric analysis, evidence map or overview of Unani clinical research with trial counts by condition and design.
- `fields.literature_state.geographic_concentration_of_trials`: no country distribution of Unani clinical trials.
- `fields.safety.documented_adverse_events`: no case reports, case series or pharmacovigilance data for Unani or kushta products specifically (all cited data are Ayurvedic).
- `fields.safety.regulatory_actions_taken`: no bans, import alerts, recalls or advisories against Unani products, with dates and jurisdictions.

## 2. Not requested

- `fields.construct_debate.positions`
- `fields.diagnostics.reliability_evidence`
- `fields.diagnostics.sign_vs_synthesis`
- `fields.diagnostics.standardization_efforts`
- `fields.education_and_licensure.duration`
- `fields.education_and_licensure.licensure_requirements`
- `fields.education_and_licensure.biomedical_content_in_curriculum`
- `fields.contact_and_borrowing.corroborated_by` (deferred to synthesis by codebook rule; see Schema misfit)
- `fields.contemporary_controversies.integration_disputes`
- `fields.contemporary_controversies.conservation_and_sourcing`
- `fields.contemporary_controversies.intellectual_property`
- `fields.contemporary_controversies.politicized_episodes`

## 3. Unclear or indirect sourcing

Indirect ([Sn]-resolved or channel stated by the report):

- `fields.canon_and_transmission.external_dating_anchors`: Ibn al-Nafis's commentary rediscovered in 1924. The report attributes this to Meyerhof (Isis, 1935), but [S3] resolves to Wikipedia ("Commentary on Anatomy in Avicenna's Canon").
- `fields.diagnostics.methods`: nabz/baul/baraz as the three signature diagnostic tools. [S4] is hakeemchichi.in, a commercial Unani/Ayurvedic pharmacy (practitioner) website, and the report does not flag it in-text.
- `fields.revival_and_institutionalization.standardization_events`, `fields.revival_and_institutionalization.dated_events`, `fields.legal_status.jurisdictions`, `fields.education_and_licensure.accrediting_body`: CCIM (IMCC Act 1970) replaced by NCISM (NCISM Act 2020). [S5] is IAS Gyan, an exam-preparation editorial site.
- `fields.identification.practitioner_estimate`: 47,683 registered Unani practitioners in India (2015 Rajya Sabha reply), through Business Standard/PTI. Not in bibliography.
- `fields.revival_and_institutionalization.standardization_events`, `fields.education_and_licensure.degree_programs`: 55 Unani colleges out of 733 AYUSH institutes (Lok Sabha data), through Medical Dialogues. Not in bibliography, year not given.

Unclear (named in report text without an [Sn] marker, so not in the bibliography and not inspectable; or wholly uncited):

- `fields.identification.system_name`, `primary_regions`: uncited.
- `fields.identification.alternate_names`: Ionia etymology and TPM equivalence quote. Uncited, or credited to Britannica with no marker.
- `fields.identification.practitioner_estimate`: ~60,000 registered Hakims in Pakistan. WHO/EMRO & Hamdard Foundation Pakistan document, not in bibliography, undated.
- `fields.canon_and_transmission.foundational_texts`: Canon (1025), al-Tasrif, al-Razi's works. Uncited, or Encyclopedia.com (tertiary, no marker).
- `fields.canon_and_transmission.transmission_mode`, `redaction_history`: translation movement and Hunayn ibn Ishaq. Gutas (1998) and Strohmaier (EI2) named in text, no marker.
- `fields.theoretical_primitives.constituents`, `balance_logic`: seven naturals, humours, tabiyat. Britannica and "multiple scoping reviews", no marker.
- `fields.theoretical_primitives.correspondence_system`: mizaj types and ajnas-e-ashara. Scoping review in Journal of Innovations in Applied Pharmaceutical Science, no marker. The venue is unassessed, and the report says elsewhere that it used some low-impact/predatory journals.
- `fields.theoretical_primitives.etiology`, `translation_programs`: uncited.
- `fields.theoretical_primitives.relation_to_biomedical_anatomy`: humoral theory superseded (Vesalius 1543, Harvey 1628, germ theory). AMA Journal of Ethics and RCP museum named generically, no marker.
- `fields.modalities.items`: about 30 regimens. Journal of Complementary and Integrative Medicine review, no marker. Also "more than 2,000 medicines" credited to Britannica, no marker.
- `fields.materia_medica.pharmacological_framework`, `preparation_traditions`: drug degrees, tadbir, musleh, abdal. Journal of Ethnopharmacology article, no marker.
- `fields.materia_medica.flagship_agents`: Rauwolfia/reserpine (uncited). Kushta metals credited to Britannica, no marker.
- `fields.colonial_disruption.period`, `suppression_or_marginalization`, `practitioner_response`: loss of patronage, Tibbia College, Hamdard 1906. Uncited.
- `fields.revival_and_institutionalization.key_figures`, `state_sponsorship`: Ajmal Khan, Siddiqui, Mughal patronage. Britannica and a Modern Asian Studies article, no marker. Iran TPM "peer-reviewed accounts" unnamed.
- `fields.revival_and_institutionalization.dated_events`: Department of ISM&H 1995, Ministry of AYUSH 2014, WHO benchmarks 2010/2022. Uncited.
- `fields.legal_status.jurisdictions`: Iran and Bangladesh. Uncited.
- `fields.literature_state.trial_counts`, `fields.evidence_state.reviews`: vitiligo systematic review (63 articles, 13 trials) has no marker and no authors, journal or year. Hijama reviews are unnamed.
- `fields.literature_state.publication_bias_findings`, `registry_and_reporting_practice`: uncited assertions.
- `fields.safety.adulteration_and_contamination`: general herbal-medicine contamination. Uncited.
- `fields.safety.intrinsic_toxicity`: kushta toxicity (Britannica, no marker), third/fourth-degree drug toxicity (J Ethnopharmacol, no marker), herb-drug interactions (uncited).
- `fields.safety.evidence_borrowed_from_other_traditions`: Saper et al. JAMA 2004 and 2008, named in text with no marker. The claims also rest on Ayurvedic, not Unani, data.
- `fields.contact_and_borrowing.relationships`: Ayurveda cross-fertilization, early Greek-Indian exchange ("some scholars"), TPM and biomedicine relationships. Uncited.
- `fields.contemporary_controversies.who_engagement`: WHO benchmarks 2010/2022 and the TM Strategy alignment. Uncited.

## 4. Schema misfit

- **Premodern dated events have no `dated_events` leaf.** `dated_events` exists only under fields 8 and 9. The report's dated premodern and scientific-history events (Canon completed 1025; Stephen of Antioch translation 1127; Ibn al-Nafis commentary ~1242; 1924 rediscovery; Vesalius 1543; Harvey 1628) had to go into prose leaves in fields 2 and 4, so synthesis cannot match them across systems. Proposed: a `dated_events` leaf under `canon_and_transmission`, or a new `premodern_history.dated_events` field.
- **Field 8 framing.** The report dates Unani's decline to the Mughal Empire's decline together with colonial biomedicine, and doesn't treat it as a colonial-policy story. The field's policy/abolition/resistance structure fits poorly, so most leaves are absent or partial. Proposed: a `loss_of_patronage` sub-field (pre-colonial or dynastic decline) alongside colonial suppression.
- **Premodern formative figures.** Al-Razi, al-Majusi, Ibn Sina, Ibn al-Nafis, al-Zahrawi and Hunayn ibn Ishaq fit only as attributed authors in field 2. Field 9 `key_figures` is scoped to revival, and there is nowhere for non-author figures such as translators and patrons. Proposed: `canon_and_transmission.key_figures`.
- **Field 15 framing for Traditional Persian Medicine and biomedicine.** The report treats TPM as essentially the same system and biomedicine as a "historical sibling" from shared ancestry. Neither is contact or borrowing, and the direction/evidence_type/status vocabulary doesn't cover shared descent or identity. Proposed: add a relationship kind (`shared_descent` | `same_system_variant` | `exchange`), or an `identification.overlapping_systems` leaf.
- **Field 6 tag vocabulary.** The tradition's own "regimenal" category (ilaj bil tadbeer) bundles procedures the tags would split: venesection, cupping and leeching (procedural, with no tag), massage (manual), and bath/steam/fomentation (thermal). Animal-origin drugs also have no tag. Proposed: add `procedural-evacuative` and `animal-derived` tags, or allow multiple tags per item.
- **Field 13 has no place for preclinical or constituent evidence.** The report's "credible core" is the isolation of pharmacologically active constituents, such as reserpine from Rauwolfia. That is neither a clinical review (13) nor a volume count (12). Proposed: `evidence_state.preclinical_and_constituent_evidence`.
- **Citation `type` vocabulary.** There is no value for a practitioner or commercial pharmacy website (S4) or for an open wiki encyclopedia (S3). S3 was typed `aggregator` and S4 `unclear`. Proposed: add `practitioner-site` and `open-encyclopedia`.
- **Status vocabulary for `corroborated_by`.** Every leaf must carry a status, but `corroborated_by` is deferred to synthesis by rule, so none of the four values is accurate. It was marked `not_requested` with an explanatory note. Proposed: a `deferred` status.
- **Report recommendations.** The patient guidance (e.g., the blood-lead testing threshold: "any unexplained anemia with basophilic stippling, or GI/neurological symptoms while taking such products") and the policy recommendations (ICP-MS screening, pharmacovigilance) have no field. Proposed: leave them out of the comparative schema deliberately, or add an optional `report_recommendations` leaf outside `fields`.
