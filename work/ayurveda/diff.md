# ayurveda — v1 vs v2 field diff

- Leaves: 82
- Filled from v1: 7
- Gap worklist: 7
- Verify worklist: 58 in 8 batches
- Schema errors: 0

## Per leaf

| Leaf | v1 | v2 | Merged from |
|---|---|---|---|
| `identification.system_name` | filled | filled | v2 |
| `identification.alternate_names` | filled | incidental | v1 fills |
| `identification.primary_regions` | filled | incidental | v1 fills |
| `identification.practitioner_estimate` | not_requested | incidental | v2 |
| `identification.system_boundary` | filled | filled | v2 |
| `canon_and_transmission.foundational_texts` | filled | filled | v2 |
| `canon_and_transmission.secondary_canon` | filled | filled | v2 |
| `canon_and_transmission.dating_and_authorship_disputes` | partial | filled | v2 |
| `canon_and_transmission.transmission_mode` | partial | partial | v2 |
| `canon_and_transmission.redaction_history` | partial | filled | v2 |
| `canon_and_transmission.external_dating_anchors` | absent | filled | v2 |
| `canon_and_transmission.key_figures` | partial | filled | v2 |
| `canon_and_transmission.dated_events` | filled | filled | v2 |
| `construct_debate.positions` | incidental | filled | v2 |
| `construct_debate.report_adjudication` | not_requested | filled | v2 |
| `theoretical_primitives.constituents` | filled | filled | v2 |
| `theoretical_primitives.balance_logic` | filled | filled | v2 |
| `theoretical_primitives.correspondence_system` | partial | absent | v2 absent; v1 value refused |
| `theoretical_primitives.etiology` | filled | partial | v2 |
| `theoretical_primitives.nosology` | absent | partial | v2 |
| `theoretical_primitives.relation_to_biomedical_anatomy` | partial | filled | v2 |
| `theoretical_primitives.translation_programs` | filled | filled | v2 |
| `diagnostics.methods` | filled | filled | v2 |
| `diagnostics.reliability_evidence` | filled | filled | v2 |
| `diagnostics.sign_vs_synthesis` | not_requested | filled | v2 |
| `diagnostics.standardization_efforts` | partial | filled | v2 |
| `diagnostics.evidence_borrowed_from_other_traditions` | not_requested | filled | v2 |
| `modalities.items` | filled | incidental | v1 fills |
| `materia_medica.pharmacological_framework` | filled | not_requested | v1 fills |
| `materia_medica.flagship_agents` | filled | incidental | v1 fills |
| `materia_medica.preparation_traditions` | filled | incidental | v1 fills |
| `disruption.loss_of_patronage` | absent | absent | v2 |
| `disruption.period` | partial | filled | v2 |
| `disruption.colonial_power` | filled | filled | v2 |
| `disruption.suppression_or_marginalization` | partial | filled | v2 |
| `disruption.abolition_attempts` | absent | filled | v2 |
| `disruption.practitioner_response` | absent | filled | v2 |
| `disruption.post_colonial_disruption` | absent | absent | v2 |
| `disruption.dated_events` | absent | filled | v2 |
| `revival_and_institutionalization.revival_context` | partial | filled | v2 |
| `revival_and_institutionalization.key_figures` | partial | filled | v2 |
| `revival_and_institutionalization.nationalist_framing` | partial | partial | v2 |
| `revival_and_institutionalization.standardization_events` | partial | filled | v2 |
| `revival_and_institutionalization.internal_factions` | partial | filled | v2 |
| `revival_and_institutionalization.state_sponsorship` | filled | filled | v2 |
| `revival_and_institutionalization.diffusion_abroad` | partial | partial | v2 |
| `revival_and_institutionalization.dated_events` | filled | filled | v2 |
| `legal_status.jurisdictions` | partial | filled | v2 |
| `legal_status.supranational_standards` | absent | filled | v2 |
| `education_and_licensure.degree_programs` | incidental | incidental | v2 |
| `education_and_licensure.duration` | not_requested | not_requested | v2 |
| `education_and_licensure.accrediting_body` | incidental | incidental | v2 |
| `education_and_licensure.licensure_requirements` | incidental | incidental | v2 |
| `education_and_licensure.biomedical_content_in_curriculum` | incidental | incidental | v2 |
| `education_and_licensure.tradition_content_in_biomedical_curriculum` | not_requested | incidental | v2 |
| `literature_state.corpus_scale_appraisal` | absent | absent | v2 |
| `literature_state.trial_counts` | partial | absent | v2 absent; v1 value refused |
| `literature_state.geographic_concentration_of_trials` | partial | partial | v2 |
| `literature_state.publication_bias_findings` | partial | absent | v2 absent; v1 value refused |
| `literature_state.registry_and_reporting_practice` | partial | absent | v2 absent; v1 value refused |
| `evidence_state.reviews` | filled | filled | v2 |
| `evidence_state.preclinical_and_constituent_evidence` | partial | not_requested | v1 fills |
| `evidence_state.evidence_borrowed_from_other_traditions` | not_requested | filled | v2 |
| `safety.adulteration_and_contamination` | filled | filled | v2 |
| `safety.intrinsic_toxicity` | filled | filled | v2 |
| `safety.documented_adverse_events` | filled | filled | v2 |
| `safety.regulatory_actions_taken` | partial | filled | v2 |
| `safety.evidence_borrowed_from_other_traditions` | not_requested | filled | v2 |
| `contact_and_borrowing.relationships` | filled | filled | v2 |
| `contact_and_borrowing.corroborated_by` | deferred | deferred | v2 |
| `contemporary_controversies.who_engagement` | incidental | filled | v2 |
| `contemporary_controversies.integration_disputes` | incidental | filled | v2 |
| `contemporary_controversies.conservation_and_sourcing` | not_requested | not_requested | v2 |
| `contemporary_controversies.intellectual_property` | incidental | filled | v2 |
| `contemporary_controversies.politicized_episodes` | incidental | filled | v2 |
| `contemporary_controversies.research_methodology_disputes` | incidental | partial | v2 |
| `self_reported_gaps.inventory` | filled | filled | v2 |
| `report_conclusions.revision_thresholds` | filled | filled | v2 |
| `report_conclusions.recommendations` | filled | filled | v2 |
| `economics.domestic_market_size` | not_requested | not_requested | v2 |
| `economics.global_market_estimates` | not_requested | not_requested | v2 |
| `economics.major_manufacturers` | incidental | incidental | v2 |
