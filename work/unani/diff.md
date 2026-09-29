# unani — v1 vs v2 field diff

- Leaves: 76
- Filled from v1: 5
- Gap worklist: 5
- Verify worklist: 56 in 7 batches
- Schema errors: 0

## Per leaf

| Leaf | v1 | v2 | Merged from |
|---|---|---|---|
| `identification.system_name` | filled | filled | v2 |
| `identification.alternate_names` | filled | incidental | v1 fills |
| `identification.primary_regions` | filled | incidental | v1 fills |
| `identification.practitioner_estimate` | filled | incidental | v1 fills |
| `identification.system_boundary` | filled | incidental | v1 fills |
| `canon_and_transmission.foundational_texts` | partial | filled | v2 |
| `canon_and_transmission.secondary_canon` | filled | partial | v2 |
| `canon_and_transmission.dating_and_authorship_disputes` | partial | filled | v2 |
| `canon_and_transmission.transmission_mode` | partial | filled | v2 |
| `canon_and_transmission.redaction_history` | absent | partial | v2 |
| `canon_and_transmission.external_dating_anchors` | partial | filled | v2 |
| `canon_and_transmission.key_figures` | filled | filled | v2 |
| `canon_and_transmission.dated_events` | filled | filled | v2 |
| `construct_debate.positions` | not_requested | filled | v2 |
| `construct_debate.report_adjudication` | incidental | filled | v2 |
| `theoretical_primitives.constituents` | filled | filled | v2 |
| `theoretical_primitives.balance_logic` | filled | filled | v2 |
| `theoretical_primitives.correspondence_system` | filled | partial | v2 |
| `theoretical_primitives.etiology` | filled | filled | v2 |
| `theoretical_primitives.nosology` | absent | partial | v2 |
| `theoretical_primitives.relation_to_biomedical_anatomy` | filled | filled | v2 |
| `theoretical_primitives.translation_programs` | partial | partial | v2 |
| `diagnostics.methods` | filled | filled | v2 |
| `diagnostics.reliability_evidence` | not_requested | filled | v2 |
| `diagnostics.sign_vs_synthesis` | not_requested | partial | v2 |
| `diagnostics.standardization_efforts` | not_requested | partial | v2 |
| `diagnostics.evidence_borrowed_from_other_traditions` | not_requested | filled | v2 |
| `modalities.items` | filled | incidental | v1 fills |
| `materia_medica.pharmacological_framework` | incidental | incidental | v2 |
| `materia_medica.flagship_agents` | incidental | incidental | v2 |
| `materia_medica.preparation_traditions` | incidental | incidental | v2 |
| `disruption.loss_of_patronage` | partial | absent | v2 absent; v1 value refused |
| `disruption.period` | partial | partial | v2 |
| `disruption.colonial_power` | absent | filled | v2 |
| `disruption.suppression_or_marginalization` | absent | filled | v2 |
| `disruption.abolition_attempts` | absent | absent | v2 |
| `disruption.practitioner_response` | partial | partial | v2 |
| `disruption.post_colonial_disruption` | absent | filled | v2 |
| `disruption.dated_events` | absent | filled | v2 |
| `revival_and_institutionalization.revival_context` | partial | filled | v2 |
| `revival_and_institutionalization.key_figures` | filled | filled | v2 |
| `revival_and_institutionalization.nationalist_framing` | absent | filled | v2 |
| `revival_and_institutionalization.standardization_events` | partial | filled | v2 |
| `revival_and_institutionalization.internal_factions` | absent | filled | v2 |
| `revival_and_institutionalization.state_sponsorship` | filled | filled | v2 |
| `revival_and_institutionalization.dated_events` | filled | filled | v2 |
| `legal_status.jurisdictions` | partial | filled | v2 |
| `legal_status.supranational_standards` | filled | filled | v2 |
| `education_and_licensure.degree_programs` | incidental | incidental | v2 |
| `education_and_licensure.duration` | not_requested | incidental | v2 |
| `education_and_licensure.accrediting_body` | incidental | incidental | v2 |
| `education_and_licensure.licensure_requirements` | not_requested | incidental | v2 |
| `education_and_licensure.biomedical_content_in_curriculum` | not_requested | incidental | v2 |
| `literature_state.corpus_scale_appraisal` | absent | absent | v2 |
| `literature_state.trial_counts` | partial | partial | v2 |
| `literature_state.geographic_concentration_of_trials` | absent | filled | v2 |
| `literature_state.publication_bias_findings` | partial | partial | v2 |
| `literature_state.registry_and_reporting_practice` | partial | partial | v2 |
| `evidence_state.reviews` | partial | partial | v2 |
| `evidence_state.preclinical_and_constituent_evidence` | partial | partial | v2 |
| `evidence_state.evidence_borrowed_from_other_traditions` | filled | filled | v2 |
| `safety.adulteration_and_contamination` | partial | filled | v2 |
| `safety.intrinsic_toxicity` | partial | filled | v2 |
| `safety.documented_adverse_events` | absent | filled | v2 |
| `safety.regulatory_actions_taken` | absent | filled | v2 |
| `safety.evidence_borrowed_from_other_traditions` | filled | filled | v2 |
| `contact_and_borrowing.relationships` | filled | filled | v2 |
| `contact_and_borrowing.corroborated_by` | deferred | deferred | v2 |
| `contemporary_controversies.who_engagement` | incidental | filled | v2 |
| `contemporary_controversies.integration_disputes` | incidental | filled | v2 |
| `contemporary_controversies.conservation_and_sourcing` | not_requested | absent | v2 |
| `contemporary_controversies.intellectual_property` | not_requested | absent | v2 |
| `contemporary_controversies.politicized_episodes` | not_requested | partial | v2 |
| `self_reported_gaps.inventory` | filled | filled | v2 |
| `report_conclusions.revision_thresholds` | filled | filled | v2 |
| `report_conclusions.recommendations` | filled | filled | v2 |
