# unani — v1 vs v2 field diff

- Leaves: 82
- Filled from v1: 5
- Gap worklist: 4
- Verify worklist: 56 in 7 batches
- Schema errors: 0

## Per leaf

| Leaf | v1 | v2 | Merged from |
|---|---|---|---|
| `identification.system_name` | filled | filled | v2 |
| `identification.alternate_names` | filled | filled | v2 |
| `identification.primary_regions` | filled | filled | v2 |
| `identification.practitioner_estimate` | filled | incidental | v1 fills |
| `identification.system_boundary` | filled | filled | v2 |
| `canon_and_transmission.foundational_texts` | filled | filled | v2 |
| `canon_and_transmission.secondary_canon` | not_requested | partial | v2 |
| `canon_and_transmission.dating_and_authorship_disputes` | not_requested | filled | v2 |
| `canon_and_transmission.transmission_mode` | incidental | filled | v2 |
| `canon_and_transmission.redaction_history` | not_requested | partial | v2 |
| `canon_and_transmission.external_dating_anchors` | incidental | filled | v2 |
| `canon_and_transmission.key_figures` | filled | filled | v2 |
| `canon_and_transmission.dated_events` | filled | filled | v2 |
| `construct_debate.positions` | not_requested | filled | v2 |
| `construct_debate.report_adjudication` | not_requested | filled | v2 |
| `theoretical_primitives.constituents` | filled | filled | v2 |
| `theoretical_primitives.balance_logic` | filled | filled | v2 |
| `theoretical_primitives.correspondence_system` | filled | filled | v2 |
| `theoretical_primitives.etiology` | partial | filled | v2 |
| `theoretical_primitives.nosology` | absent | partial | v2 |
| `theoretical_primitives.relation_to_biomedical_anatomy` | filled | filled | v2 |
| `theoretical_primitives.translation_programs` | partial | partial | v2 |
| `diagnostics.methods` | filled | filled | v2 |
| `diagnostics.reliability_evidence` | not_requested | filled | v2 |
| `diagnostics.sign_vs_synthesis` | not_requested | absent | v2 |
| `diagnostics.standardization_efforts` | not_requested | partial | v2 |
| `diagnostics.evidence_borrowed_from_other_traditions` | not_requested | filled | v2 |
| `modalities.items` | filled | incidental | v1 fills |
| `materia_medica.pharmacological_framework` | incidental | incidental | v2 |
| `materia_medica.flagship_agents` | incidental | incidental | v2 |
| `materia_medica.preparation_traditions` | incidental | incidental | v2 |
| `disruption.loss_of_patronage` | partial | partial | v2 |
| `disruption.period` | partial | filled | v2 |
| `disruption.colonial_power` | partial | filled | v2 |
| `disruption.suppression_or_marginalization` | absent | filled | v2 |
| `disruption.abolition_attempts` | absent | absent | v2 |
| `disruption.practitioner_response` | partial | filled | v2 |
| `disruption.post_colonial_disruption` | absent | filled | v2 |
| `disruption.dated_events` | absent | filled | v2 |
| `revival_and_institutionalization.revival_context` | partial | filled | v2 |
| `revival_and_institutionalization.key_figures` | filled | filled | v2 |
| `revival_and_institutionalization.nationalist_framing` | absent | filled | v2 |
| `revival_and_institutionalization.standardization_events` | partial | filled | v2 |
| `revival_and_institutionalization.internal_factions` | absent | filled | v2 |
| `revival_and_institutionalization.state_sponsorship` | filled | filled | v2 |
| `revival_and_institutionalization.diffusion_abroad` | not_requested | partial | v2 |
| `revival_and_institutionalization.dated_events` | filled | filled | v2 |
| `legal_status.jurisdictions` | partial | filled | v2 |
| `legal_status.supranational_standards` | filled | filled | v2 |
| `education_and_licensure.degree_programs` | partial | incidental | v1 fills |
| `education_and_licensure.duration` | not_requested | incidental | v2 |
| `education_and_licensure.accrediting_body` | partial | incidental | v1 fills |
| `education_and_licensure.licensure_requirements` | not_requested | incidental | v2 |
| `education_and_licensure.biomedical_content_in_curriculum` | not_requested | incidental | v2 |
| `education_and_licensure.tradition_content_in_biomedical_curriculum` | not_requested | not_requested | v2 |
| `literature_state.corpus_scale_appraisal` | absent | absent | v2 |
| `literature_state.trial_counts` | partial | partial | v2 |
| `literature_state.geographic_concentration_of_trials` | absent | filled | v2 |
| `literature_state.publication_bias_findings` | partial | partial | v2 |
| `literature_state.registry_and_reporting_practice` | absent | absent | v2 |
| `evidence_state.reviews` | partial | filled | v2 |
| `evidence_state.preclinical_and_constituent_evidence` | partial | incidental | v1 fills |
| `evidence_state.evidence_borrowed_from_other_traditions` | not_requested | filled | v2 |
| `safety.adulteration_and_contamination` | partial | filled | v2 |
| `safety.intrinsic_toxicity` | filled | filled | v2 |
| `safety.documented_adverse_events` | absent | partial | v2 |
| `safety.regulatory_actions_taken` | absent | filled | v2 |
| `safety.evidence_borrowed_from_other_traditions` | filled | filled | v2 |
| `contact_and_borrowing.relationships` | filled | filled | v2 |
| `contact_and_borrowing.corroborated_by` | deferred | deferred | v2 |
| `contemporary_controversies.who_engagement` | filled | partial | v2 |
| `contemporary_controversies.integration_disputes` | incidental | filled | v2 |
| `contemporary_controversies.conservation_and_sourcing` | not_requested | not_requested | v2 |
| `contemporary_controversies.intellectual_property` | not_requested | not_requested | v2 |
| `contemporary_controversies.politicized_episodes` | not_requested | partial | v2 |
| `contemporary_controversies.research_methodology_disputes` | not_requested | partial | v2 |
| `self_reported_gaps.inventory` | filled | filled | v2 |
| `report_conclusions.revision_thresholds` | filled | filled | v2 |
| `report_conclusions.recommendations` | filled | filled | v2 |
| `economics.domestic_market_size` | not_requested | not_requested | v2 |
| `economics.global_market_estimates` | not_requested | not_requested | v2 |
| `economics.major_manufacturers` | incidental | incidental | v2 |
