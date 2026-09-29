# Traditional Medicine Comparative Codebook — v1.1

A fixed extraction schema. Every system report is mapped to these fields, in this
order, using this vocabulary. The point is commensurability: fields must be
readable down the column across systems, not just down the page within one system.

Changes in v1.1: every codebook sub-field is its own leaf carrying `status`,
with fixed leaf names and list-valued collections (see Leaf naming — this is
what makes the merge deterministic); `shared_events` and
`corroborated_by` are no longer filled at mapping — an isolated mapper sees one
report and cannot know what other reports contain, so these are computed at
synthesis, the first pass that sees the whole corpus. The mapper records every
dated event and every exchange instead, with a canonical label.

Changes from v0: added the `not_requested` status; added study-design sub-fields
to reliability; added shared-event marking; added the citation-strength flag;
added corpus-scale appraisal to field 12; added field 17 for self-reported gaps.

## Output contract

One YAML file per system: `<system-slug>.yml`.

Every field is an object with this shape:

```yaml
field_name:
  status: filled | partial | absent | not_requested
  value: <content, or null>
  citations:
    - source: <author/title/year or institution/document>
      type: tertiary-review | systematic-review | meta-analysis | reference-work |
            institutional | primary-study | historical-monograph | statute |
            news | aggregator | catalog-listing | unclear
      citation_strength: direct | indirect | unclear
  register: emic | historical-scholarship | biomedical-evidence | regulatory
  notes: <disputes, caveats, why absent — optional>
```

**Status values.**
- `filled` / `partial` — the report covers it.
- `absent` — the report addressed the topic and the literature came up short, or
  the report should plausibly have covered it and did not. A real gap.
- `not_requested` — the source research prompt never asked, so silence here says
  nothing about the literature. **Do not send these to the gap pass as search
  targets for missing evidence; they are prompt-coverage gaps, not evidence gaps.**
  Expect this status on fields 6, 7, 11 and parts of 1.

Keeping these apart is the whole point. A field can be empty because nobody
looked, because nobody asked, or because nothing exists, and the three lead to
completely different next actions.

**citation_strength.**
- `direct` — the work itself, the statute text, the journal article.
- `indirect` — a real claim reached through a bookseller page, catalog entry,
  expat guide, practitioner blog, state media outlet or news aggregator.
- `unclear` — cannot tell from the report.

Every `indirect` is a verification target. These cluster in fields 8, 9 and 10.

**register** keeps the tradition's own claims, historical scholarship, biomedical
evidence and regulatory fact from blending together.

## Leaf naming (v1.1)

Leaf keys are exactly the codebook's sub-field names — never invented keys.
Where a field holds a variable number of items, they go as a list inside one
leaf's `value`. Fields without named sub-fields use these leaf names:

| Field | Leaf | Value is a list of |
|---|---|---|
| 3 construct_debate | `positions` | `{scholar, work, year, position, evidence_base}` |
| 6 modalities | `items` | `{name, tag, description}` |
| 10 legal_status | `jurisdictions` | `{jurisdiction, regulator, statute, year, scope_of_practice, prescribing_rights, integration_with_public_health_system, recognition_tier}` |
| 13 evidence_state | `reviews` | `{modality, best_available_review, type, year, size, conclusion, certainty_rating, methodological_limitations_noted}` |
| 15 contact_and_borrowing | `relationships` | `{other_tradition, direction, period, evidence_type, status}` |
| 17 self_reported_gaps | `inventory` | `{kind, text}` |

Likewise `diagnostics.reliability_evidence` and `dated_events` are single leaves
whose value is a list. A jurisdiction or study appearing in one report and not
another is then a difference in content, not in schema — which is what keeps
schema errors meaningful.

## Fields

### 1. identification
- `system_name`, `alternate_names` (including endonyms), `primary_regions`
- `practitioner_estimate` — count, source, year

### 2. canon_and_transmission
- `foundational_texts` — title, approximate date, attributed author
- `secondary_canon`
- `dating_and_authorship_disputes` — named scholars and their positions
- `transmission_mode` — textual, oral, lineage-based, mixed
- `redaction_history`
- `external_dating_anchors` — excavated manuscripts, dated copies, translations

### 3. construct_debate
Whether the modern system is continuous with premodern practice or substantially
a 19th–20th century construction. Named scholars, their specific positions, and
what each side's evidence base actually is. Record any adjudication the report
offers as its own, not as consensus.

### 4. theoretical_primitives
- `constituents`, `balance_logic`, `correspondence_system`, `etiology`, `nosology`
- `relation_to_biomedical_anatomy` — where it maps and where it explicitly refuses
- `translation_programs` — attempts to find biomedical correlates, with their
  stated maturity (established / preliminary / speculative)

### 5. diagnostics
- `methods` — each named, with what it examines
- `reliability_evidence` — one entry per study, each with:
  - `statistic` — Cohen κ | weighted κ | Gwet AC2 | ICC | percent agreement
  - `value` and confidence interval where given
  - `design` — clinician-vs-clinician | questionnaire-validation |
    instrument-vs-expert | intra-rater | software-vs-clinician
  - `population` — healthy volunteers | patients | mixed
  - `n_raters`, `n_subjects`
  - `target` — what was being agreed on (a single sign, a constitutional type,
    a whole pattern, a final diagnosis)
  - `citation`
- `sign_vs_synthesis` — where the report distinguishes agreement on individual
  observable signs from agreement on the integrated judgment
- `standardization_efforts` — questionnaires, software, official scales, and
  the agreement threshold they target

**Do not summarize this field into a verdict.** Values from different designs
are not comparable and must not be averaged, ranked or collapsed.

### 6. modalities
For each: name, tag, description. Tags: `herbal` | `mineral-metal` | `manual` |
`needle` | `thermal` | `dietary` | `regimenal` | `surgical` | `mind-body` | `ritual`

### 7. materia_medica
- `pharmacological_framework`, `flagship_agents`, `preparation_traditions`

### 8. colonial_disruption
- `period`, `colonial_power`
- `suppression_or_marginalization` — specific policies with dates
- `abolition_attempts` — formal proposals, votes, outcomes, dates
- `practitioner_response` — organized resistance, dates, bodies formed
- `dated_events` — every dated event, as `{label, date, description}`. Use a
  plain canonical label (for example "Macaulay's Minute", "Bhore Committee").
  Consistent labels are what let synthesis detect events shared across systems.
  Do **not** attempt to mark events as shared — that is computed at synthesis.

### 9. revival_and_institutionalization
- `key_figures` and dates
- `nationalist_framing`
- `standardization_events` — textbooks, curricula, colleges, dates
- `internal_factions` — purist versus integrationist splits, named
- `state_sponsorship`
- `dated_events` — as in field 8

### 10. legal_status
One entry per jurisdiction: `jurisdiction`, `regulator`, `statute` with year,
`scope_of_practice`, `prescribing_rights`, `integration_with_public_health_system`,
`recognition_tier` (full medical system | statutory registration | title
protection | supplement/wellness only | unregulated).

### 11. education_and_licensure
- `degree_programs`, `duration`, `accrediting_body`
- `licensure_requirements`
- `biomedical_content_in_curriculum`

### 12. literature_state
**Volume and provenance only. No quality judgment here.**
- `corpus_scale_appraisal` — whether a study exists that characterizes the whole
  corpus (a Cochrane overview, evidence map, bibliometric analysis), with its
  numbers. Record `absent` explicitly where none exists; the absence of a
  corpus-scale appraisal is itself a comparative fact.
- `trial_counts` — by modality where available
- `geographic_concentration_of_trials`
- `publication_bias_findings` — specific studies documenting it
- `registry_and_reporting_practice`

A system with few trials is under-studied, which is not the same as studied and
found wanting. Never let field 12 imply field 13.

### 13. evidence_state
**Quality and conclusions only.**
Per modality: `best_available_review` (type, year, size), `conclusion`,
`certainty_rating` as the reviewers gave it, `methodological_limitations_noted`.
Use the reviewers' own hedging. Do not sharpen a qualified conclusion.

### 14. safety
- `adulteration_and_contamination` — with measured figures where given
- `intrinsic_toxicity` — agents with documented harm, and the mechanism class
  (heavy metal | plant toxin | procedural | interaction)
- `documented_adverse_events` — case series, surveillance, with citations
- `regulatory_actions_taken` — bans, import alerts, advisories, with dates
- `evidence_borrowed_from_other_traditions` — flag any harm claim resting on
  data from a different system. These do not belong in this system's cell.

### 15. contact_and_borrowing
Per relationship: `other_tradition`, `direction`, `period`, `evidence_type`
(documented translation | textual attestation | structural parallel),
`status` (demonstrated | contested | convergence).
- `corroborated_by` — leave unset. Computed at synthesis, where the whole corpus
  is visible. Independent corroboration from the other end of an exchange is a
  finding, but a mapper seeing one report cannot establish it.

### 16. contemporary_controversies
- `who_engagement` — strategies, benchmarks, ICD-11, centres
- `integration_disputes` — within the country of origin, with litigation status
- `conservation_and_sourcing`
- `intellectual_property` — biopiracy cases, defensive databases, Nagoya exposure
- `politicized_episodes` — pandemic-era promotion, state endorsement, court cases

### 17. self_reported_gaps
Verbatim inventory of what the source report itself said it searched for and did
not find, plus its own source-quality caveats and contested-item flags.

Kept separate from the extraction's own `absent` findings. Where the two diverge,
that divergence is informative: self-reported gaps are the ones the research pass
noticed, and the rest are the ones it could not see in itself.

## Mapping rules

1. Extract only. Do not supplement the report with outside knowledge.
2. Preserve the source report's citation for every value carried over.
3. Uncited claim → `type: unclear` and note it. These are verification targets.
4. Claim sourced through an aggregator, bookseller, blog or news outlet →
   `citation_strength: indirect`, regardless of how solid the claim itself is.
5. Where the report's framing does not fit a field, record what it does say and
   note the mismatch rather than forcing it.
6. Where a field is `absent`, say what specifically is missing, precisely enough
   to become a search target.
7. Where a field is `not_requested`, say so plainly and do not write a search
   target for it.

## Schema revision

If a report contains something substantial that no field accommodates, propose
the field rather than discarding the content. Schema changes apply to all
systems, and earlier mappings are re-run.
