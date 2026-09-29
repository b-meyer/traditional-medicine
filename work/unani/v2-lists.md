# Unani v2 extraction: closing lists

## 1. Absent

- `disruption.loss_of_patronage`: no dated decline of Mughal, Awadh or Hyderabad court patronage for Unani hakims. The report names Nizam patronage but gives no dates or decline. Search: dated loss of princely and Mughal court patronage for Unani, 17th-20th c.
- `disruption.abolition_attempts`: no formal colonial-era proposal, vote or ordinance to abolish or de-recognize Unani, despite the report's claim that colonialism "nearly killed it". Search: formal proposals to withdraw state recognition or support from Unani, with dates and outcomes.
- `literature_state.corpus_scale_appraisal`: no corpus-wide appraisal of Unani trials (overview of reviews, whole-system evidence map, bibliometric analysis) and no total trial count. Only modality-level cupping and post-COVID mappings are cited. Search: bibliometric analysis or evidence map of Unani clinical trials with counts by condition and country.

Partial leaves with specific gaps (not absent):
- `literature_state.publication_bias_findings`: no named study quantifying publication bias in Unani trials.
- `literature_state.registry_and_reporting_practice`: no trial-registry (CTRI, ClinicalTrials.gov) registration rates.
- `diagnostics.sign_vs_synthesis`: no sign-level versus integrated-judgment comparison; no kappa study of nabz (pulse) diagnosis (also reported by the report itself).
- `disruption.dated_events`: Mudaliar, Shrivastava and Udupa committee dates missing.
- `canon_and_transmission.secondary_canon`: no list of South Asian Unani compendia.

## 2. Not requested or incidental

- `identification.practitioner_estimate`: incidental
- `modalities.items`: incidental
- `materia_medica.pharmacological_framework`: incidental
- `materia_medica.flagship_agents`: incidental
- `materia_medica.preparation_traditions`: incidental
- `education_and_licensure.degree_programs`: incidental
- `education_and_licensure.duration`: incidental
- `education_and_licensure.accrediting_body`: incidental
- `education_and_licensure.licensure_requirements`: incidental
- `education_and_licensure.biomedical_content_in_curriculum`: incidental
- `education_and_licensure.tradition_content_in_biomedical_curriculum`: not_requested
- `evidence_state.preclinical_and_constituent_evidence`: incidental
- `contemporary_controversies.conservation_and_sourcing`: not_requested
- `contemporary_controversies.intellectual_property`: not_requested
- `economics.domestic_market_size`: not_requested
- `economics.global_market_estimates`: not_requested
- `economics.major_manufacturers`: incidental
- `contact_and_borrowing.corroborated_by`: deferred (not a gap)

## 3. Unclear or indirect sourcing

Indirect sources:
- `construct_debate.positions`: Attewell's thesis reached via a bookseller listing (Exotic India Art, S29); Speziale via an Academia.edu profile (S31).
- `construct_debate.positions`: Alavi's argument cited to a ResearchGate record of the Attewell book (S30). Flagged `claim_match: mismatch`.
- `diagnostics.reliability_evidence`: three-specialist ICC study (0.62, 0.64) cited to Academia.edu S2, titled about mizaj classification tools. Flagged `mismatch`.
- `safety.regulatory_actions_taken`: pharmacovigilance-programme claim cited to Academia.edu S27, about Ayurvedic heavy-metal poisoning. Flagged `mismatch`. The 2005 order comes via a Scribd copy (S25), and the limits via a commercial testing lab page (S26).
- `legal_status.jurisdictions`: Wikipedia (S8, S12), a legal-advice site (S10), an expat guide (S16), a PIB press release (S7, treated as state media).
- `revival_and_institutionalization.diffusion_abroad`, `education_and_licensure.*`: South Africa claims via the expat guide S16.
- `disruption.practitioner_response`, `revival_and_institutionalization.key_figures`, `.internal_factions`: Ajmal Khan facts via the hobbyist site greekmedicine.net (S6).
- `evidence_state.reviews`: wet-cupping mental-health review reached via a catalog record (S20).
- `identification.practitioner_estimate`: Pakistan ~60,000 hakims via a manufacturer-linked foundation quoted through WHO EMRO; Saeed et al. 2011 unlisted.
- `identification.system_boundary`, `contact_and_borrowing.relationships`, `materia_medica.pharmacological_framework`: S8 or S31.

Unclear (no bibliography entry or no citation):
- Studies cited in-text only: Mojahedi 2014 (`diagnostics.reliability_evidence`); Zhang et al. 2024 (`literature_state.trial_counts`, `evidence_state.evidence_borrowed_from_other_traditions`); Mustehasan & Azhar 2022 (`materia_medica.flagship_agents`, `safety.intrinsic_toxicity`); Discover Chemistry 2026 Jawarish Shahi, PMC10061885, PMC8059418, J Forensic Leg Med 2025 (field 14); Bergsträsser and Lamoreaux editions and the Encyclopaedia of Islam entry (field 2).
- Wholly uncited: field 1 (name, aliases, regions), field 2 transmission mode, anchors, key figures, dated events; field 4 (all leaves); field 5 methods; field 6; field 7; field 8 period, colonial power, suppression, post-colonial, dated events; field 9 context, nationalist framing, factions; field 12 geographic concentration, publication bias, registry; field 16 (WHO, integration disputes, politicized episodes, methodology disputes); fields 17 and 18 (the report's own text); Nizam of Hyderabad patronage.

## 4. Schema misfit

Fields whose framing does not fit this tradition:
- `identification.system_boundary` and `diagnostics.evidence_borrowed_from_other_traditions`: the Iranian Persian-medicine studies form most of the mizaj reliability evidence and are treated by the report as Unani evidence. I recorded Persian medicine as `same_system_variant` and left the borrowed leaf empty. Synthesis should decide whether Persian medicine should count as this tradition or a neighbour.
- `theoretical_primitives.correspondence_system`: Unani has quality-humour-element pairings but no wider correspondence system, so the leaf fits only loosely.
- `evidence_state.reviews` versus `evidence_borrowed_from_other_traditions`: cupping (hijama) reviews cover cupping generally with Chinese-cluster trials. I placed them under borrowed evidence, but the report treats hijama as Unani's own modality. This is a judgment call, not a misfit that needs a new field.
- `canon_and_transmission.key_figures`: contains a final entry naming modern scholars (Gutas, Sabra, Janssens, Fancy, Speziale) that fits none of the premodern-figure definitions.
- `revival_and_institutionalization.diffusion_abroad`: the report treats Bangladesh and Sri Lanka only as regional recognition, so their entries there are a stretch.

Proposed new field: none required.
