# tcm — v1 vs v2 field diff

- Leaves: 82
- Filled from v1: 7
- Gap worklist: 3
- Verify worklist: 56 in 7 batches
- Schema errors: 0

## Per leaf

| Leaf | v1 | v2 | Merged from |
|---|---|---|---|
| `identification.system_name` | filled | filled | v2 |
| `identification.alternate_names` | partial | filled | v2 |
| `identification.primary_regions` | partial | partial | v2 |
| `identification.practitioner_estimate` | absent | not_requested | v2 |
| `identification.system_boundary` | filled | filled | v2 |
| `canon_and_transmission.foundational_texts` | filled | filled | v2 |
| `canon_and_transmission.secondary_canon` | partial | partial | v2 |
| `canon_and_transmission.dating_and_authorship_disputes` | absent | filled | v2 |
| `canon_and_transmission.transmission_mode` | partial | partial | v2 |
| `canon_and_transmission.redaction_history` | partial | filled | v2 |
| `canon_and_transmission.external_dating_anchors` | partial | filled | v2 |
| `canon_and_transmission.key_figures` | filled | filled | v2 |
| `canon_and_transmission.dated_events` | filled | filled | v2 |
| `construct_debate.positions` | incidental | filled | v2 |
| `construct_debate.report_adjudication` | incidental | filled | v2 |
| `theoretical_primitives.constituents` | filled | filled | v2 |
| `theoretical_primitives.balance_logic` | filled | filled | v2 |
| `theoretical_primitives.correspondence_system` | filled | filled | v2 |
| `theoretical_primitives.etiology` | filled | filled | v2 |
| `theoretical_primitives.nosology` | filled | filled | v2 |
| `theoretical_primitives.relation_to_biomedical_anatomy` | filled | filled | v2 |
| `theoretical_primitives.translation_programs` | partial | partial | v2 |
| `diagnostics.methods` | filled | filled | v2 |
| `diagnostics.reliability_evidence` | incidental | filled | v2 |
| `diagnostics.sign_vs_synthesis` | incidental | partial | v2 |
| `diagnostics.standardization_efforts` | incidental | filled | v2 |
| `diagnostics.evidence_borrowed_from_other_traditions` | incidental | filled | v2 |
| `modalities.items` | filled | incidental | v1 fills |
| `materia_medica.pharmacological_framework` | incidental | not_requested | v1 fills |
| `materia_medica.flagship_agents` | incidental | incidental | v2 |
| `materia_medica.preparation_traditions` | not_requested | not_requested | v2 |
| `disruption.loss_of_patronage` | absent | filled | v2 |
| `disruption.period` | partial | filled | v2 |
| `disruption.colonial_power` | absent | filled | v2 |
| `disruption.suppression_or_marginalization` | partial | filled | v2 |
| `disruption.abolition_attempts` | filled | partial | v2 |
| `disruption.practitioner_response` | filled | filled | v2 |
| `disruption.post_colonial_disruption` | absent | partial | v2 |
| `disruption.dated_events` | filled | filled | v2 |
| `revival_and_institutionalization.revival_context` | filled | filled | v2 |
| `revival_and_institutionalization.key_figures` | filled | filled | v2 |
| `revival_and_institutionalization.nationalist_framing` | filled | filled | v2 |
| `revival_and_institutionalization.standardization_events` | filled | filled | v2 |
| `revival_and_institutionalization.internal_factions` | absent | absent | v2 |
| `revival_and_institutionalization.state_sponsorship` | filled | filled | v2 |
| `revival_and_institutionalization.diffusion_abroad` | filled | partial | v2 |
| `revival_and_institutionalization.dated_events` | filled | filled | v2 |
| `legal_status.jurisdictions` | partial | filled | v2 |
| `legal_status.supranational_standards` | filled | partial | v2 |
| `education_and_licensure.degree_programs` | incidental | incidental | v2 |
| `education_and_licensure.duration` | not_requested | not_requested | v2 |
| `education_and_licensure.accrediting_body` | not_requested | not_requested | v2 |
| `education_and_licensure.licensure_requirements` | incidental | incidental | v2 |
| `education_and_licensure.biomedical_content_in_curriculum` | incidental | not_requested | v1 fills |
| `education_and_licensure.tradition_content_in_biomedical_curriculum` | incidental | not_requested | v1 fills |
| `literature_state.corpus_scale_appraisal` | absent | absent | v2 |
| `literature_state.trial_counts` | partial | partial | v2 |
| `literature_state.geographic_concentration_of_trials` | filled | filled | v2 |
| `literature_state.publication_bias_findings` | filled | filled | v2 |
| `literature_state.registry_and_reporting_practice` | filled | partial | v2 |
| `evidence_state.reviews` | filled | filled | v2 |
| `evidence_state.preclinical_and_constituent_evidence` | filled | partial | v2 |
| `evidence_state.evidence_borrowed_from_other_traditions` | filled | filled | v2 |
| `safety.adulteration_and_contamination` | filled | partial | v2 |
| `safety.intrinsic_toxicity` | filled | filled | v2 |
| `safety.documented_adverse_events` | filled | filled | v2 |
| `safety.regulatory_actions_taken` | filled | filled | v2 |
| `safety.evidence_borrowed_from_other_traditions` | filled | filled | v2 |
| `contact_and_borrowing.relationships` | partial | filled | v2 |
| `contact_and_borrowing.corroborated_by` | deferred | deferred | v2 |
| `contemporary_controversies.who_engagement` | incidental | filled | v2 |
| `contemporary_controversies.integration_disputes` | incidental | partial | v2 |
| `contemporary_controversies.conservation_and_sourcing` | incidental | filled | v2 |
| `contemporary_controversies.intellectual_property` | incidental | absent | v2 |
| `contemporary_controversies.politicized_episodes` | incidental | filled | v2 |
| `contemporary_controversies.research_methodology_disputes` | incidental | filled | v2 |
| `self_reported_gaps.inventory` | filled | filled | v2 |
| `report_conclusions.revision_thresholds` | filled | filled | v2 |
| `report_conclusions.recommendations` | filled | filled | v2 |
| `economics.domestic_market_size` | incidental | not_requested | v1 fills |
| `economics.global_market_estimates` | incidental | not_requested | v1 fills |
| `economics.major_manufacturers` | incidental | not_requested | v1 fills |
