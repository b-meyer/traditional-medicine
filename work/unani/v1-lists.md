# Unani v1 — closing lists

## 1. Absent

- `canon_and_transmission.dating_and_authorship_disputes` — no named scholars or positions on dating/authorship/attribution of the Canon, al-Hawi, Kamil al-Sina'a, Kitab al-Tasrif, or the Hippocratic/Galenic works as received in Arabic.
- `theoretical_primitives.nosology` — no Unani disease-classification scheme (by organ, by humour/temperament, simple vs compound) in classical or modern texts or standard terminologies.
- `disruption.colonial_power` — report says only "colonial biomedicine"; the colonial state whose medical policy displaced Unani in South Asia is not named.
- `disruption.suppression_or_marginalization` — no specific colonial-era laws, registration rules, funding withdrawals or institutional exclusions affecting Unani, with dates.
- `disruption.abolition_attempts` — no formal proposals to abolish or ban Unani (colonial or post-colonial South Asia), with votes, outcomes and dates.
- `disruption.post_colonial_disruption` — effect of the 1947 partition on Unani institutions, practitioners and firms (e.g., the Hamdard India/Pakistan division), with dates; the report only mentions "later Hamdard (Pakistan)".
- `disruption.dated_events` — no dated disruption events; the Mughal decline and colonial displacement are undated.
- `revival_and_institutionalization.nationalist_framing` — whether and how the Ajmal Khan / Tibbia College revival was framed in nationalist or communal terms, with named scholarly analyses.
- `revival_and_institutionalization.internal_factions` — named purist vs integrationist (or other) factions in the Unani revival and modern profession (India, Pakistan).
- `literature_state.corpus_scale_appraisal` — no bibliometric analysis, evidence map or overview of reviews covering Unani clinical research as a whole, with counts.
- `literature_state.geographic_concentration_of_trials` — country distribution of Unani clinical trials (India, Pakistan, Iran, other).
- `safety.documented_adverse_events` — Unani-specific case reports, case series or pharmacovigilance data (incl. heavy-metal poisoning from Unani products; adverse events from hijama/fasd). All cases in the report are Ayurvedic.
- `safety.regulatory_actions_taken` — bans, import alerts, recalls or advisories concerning Unani products in any jurisdiction, with dates.

Partial leaves with specific missing elements (see each leaf's `notes`): `identification.practitioner_estimate`, `canon_and_transmission.transmission_mode`, `.redaction_history`, `.external_dating_anchors`, `theoretical_primitives.etiology`, `.translation_programs`, `disruption.loss_of_patronage`, `.period`, `.practitioner_response`, `revival_and_institutionalization.revival_context`, `.standardization_events`, `legal_status.jurisdictions` (scope of practice, prescribing rights, public-health integration for India; regulator/statute for Pakistan, Bangladesh, Iran), `literature_state.trial_counts`, `.publication_bias_findings`, `.registry_and_reporting_practice`, `evidence_state.reviews`, `.preclinical_and_constituent_evidence`, `safety.adulteration_and_contamination`, `contemporary_controversies.who_engagement` (ICD-11 status; WHO collaborating centres).

## 2. Not requested or incidental

- `construct_debate.positions` — incidental (report asserts continuity in passing; no scholars named)
- `diagnostics.reliability_evidence` — not_requested
- `diagnostics.sign_vs_synthesis` — not_requested
- `diagnostics.standardization_efforts` — not_requested
- `diagnostics.evidence_borrowed_from_other_traditions` — not_requested
- `materia_medica.pharmacological_framework` — incidental
- `materia_medica.flagship_agents` — incidental
- `materia_medica.preparation_traditions` — incidental
- `education_and_licensure.degree_programs` — incidental
- `education_and_licensure.duration` — not_requested
- `education_and_licensure.accrediting_body` — incidental
- `education_and_licensure.licensure_requirements` — incidental
- `education_and_licensure.biomedical_content_in_curriculum` — not_requested
- `contemporary_controversies.integration_disputes` — incidental (Iran/TPM implementation challenges)
- `contemporary_controversies.conservation_and_sourcing` — not_requested
- `contemporary_controversies.intellectual_property` — not_requested
- `contemporary_controversies.politicized_episodes` — not_requested
- `contact_and_borrowing.corroborated_by` — deferred (not a search target)

## 3. Unclear or indirect sourcing

Bibliography-resolved weak sources:

- `canon_and_transmission.dated_events` — Rediscovery of Ibn al-Nafis's work in 1924 — [S3] Wikipedia, "Commentary on Anatomy in Avicenna's Canon" (open-encyclopedia, indirect). The report text attributes this to Meyerhof (Isis, 1935), but the marker resolves to Wikipedia.
- `diagnostics.methods` — the nabz/baul/baraz diagnostic triad — [S4] hakeemchichi.in "Diagnosis | Unani & Ayurvedic Pharmacy" (practitioner-site, indirect). Not flagged in the text as a practitioner source.
- `revival_and_institutionalization.standardization_events`, `.dated_events`, `legal_status.jurisdictions`, `education_and_licensure.accrediting_body` — CCIM replaced by NCISM (NCISM Act 2020) — [S5] IAS Gyan exam-prep daily editorial (aggregator, indirect). The title concerns AYUSH practitioners' scope of practice; claim_match was left out as not plainly mismatched.
- `contemporary_controversies.who_engagement`, `revival_and_institutionalization.dated_events` — WHO recognition of Unani in 1976 — [S6] Britannica "Modes of treatment" page (reference-work, direct). The page title is about treatment modes; the WHO claim could not be confirmed from the title, so claim_match was left out.

News-channel claims named in the text without a [Sn] marker (indirect):

- `identification.practitioner_estimate` — 47,683 registered Unani practitioners in India (2015) — Business Standard/PTI report of a Rajya Sabha reply.
- `identification.practitioner_estimate`, `education_and_licensure.degree_programs` — 55 Unani colleges — Medical Dialogues report of Lok Sabha data.

Unresolvable (type `unclear`): most of the report's substantive claims name a source in the text but carry no [Sn] marker and have no bibliography entry. These sources are Britannica beyond S6, Gutas, Gutas & van Bladel, Strohmaier, Iskandar, Meyerhof, the Modern Asian Studies article, Encyclopedia.com (Rhazes), the J Complement Integr Med regimenal review, the J Ethnopharmacology islah-e-advia article, the J Innov Appl Pharm Sci scoping review, the AMA J Ethics and RCP museum, the vitiligo systematic review, the hijama reviews, Saper 2004 and Saper 2008 (JAMA), and the WHO/EMRO Hamdard Pakistan document. Other claims have no attribution at all. These include the Ibn Sina and Canon dates; al-Zahrawi; the AYUSH and CCRUM dates; the WHO 2010 and 2022 benchmarks; the humour-mapping programs; publication-bias and reporting-practice assertions; the Rauwolfia/reserpine isolation; the general herbal contamination claim; and most of section 7 (relationships). Leaf-by-leaf detail is in the YAML `citations`.

## 4. Schema misfit

- Content not accommodated: none of substance. The report's "far less precise" remark on pulse and urine diagnosis (in `theoretical_primitives.relation_to_biomedical_anatomy` and `diagnostics.reliability_evidence` notes) and the Iran/TPM implementation challenges (`contemporary_controversies.integration_disputes`, `legal_status.jurisdictions`) fit existing leaves, with notes.
- Framing misfits:
  - `disruption` sub-fields assume a named colonial power and policies. The report treats disruption only as the loss of Mughal patronage together with an unnamed "colonial biomedicine". The fields fit; the report does not fill them, so they are recorded as absent rather than as a misfit.
  - `contact_and_borrowing.relationships` has no `kind` for direct descent. The Greek-to-Arabic transmission is direct ancestry rather than exchange between contemporaries or a common ancestor, and it was recorded as `exchange` with a note. This is a small framing gap: a `kind: descent` value could be proposed.
