# Traditional Medicine Comparative Codebook — v1.6

A fixed extraction schema. Every system report is mapped to these fields, in this
order, using this vocabulary. The point is commensurability: fields must be
readable down the column across systems, not just down the page within one system.

Changes in v1.6: no new leaves and no enum changes; every change is a routing
rule that turns a recurring judgment call into a stated answer, so a mapper
need not report it as a misfit. Added the Misfit rule (below). `system_boundary`
now says where a variant's evidence goes; `key_figures` excludes modern
scholars; `correspondence_system` states what an absent wider system looks
like; `diffusion_abroad` covers traditions with no single country of origin;
`evidence_borrowed_from_other_traditions` (fields 5, 13) states when a modality
is the tradition's own.

Changes in v1.5: field 19 `economics` holds market and industry scale, which no
earlier field could. `disruption.colonial_power` becomes a structured leaf with
a `mode`, so a tradition displaced by semi-colonial or indirect foreign
pressure, or by domestic modernization alone, is no longer coded as a gap.
New leaves: `revival_and_institutionalization.diffusion_abroad` for spread
outside the country of origin,
`education_and_licensure.tradition_content_in_biomedical_curriculum` for the
reverse direction of `biomedical_content_in_curriculum`, and
`contemporary_controversies.research_methodology_disputes` for disputes over
how the tradition's interventions can be tested. Field 1 `relation` gains
`premodern_predecessor`. The `economic` register and the `market-research`
source type are added. Field 6 tags record intentional use only.

Changes in v1.4: field 3 gains a `report_adjudication` leaf, so the report's
own verdict on the continuity debate has a place of its own instead of riding in
`positions.notes`. Field 3's leaves are now listed explicitly.

Changes in v1.3: enum additions only, no new leaves. Field 1 `relation` gains
`absorbed_strand`; field 14's mechanism classes gain `pharmaceutical
adulterant` and `indirect`; field 15 `kind` gains `descent` and `parallel`, so
direct ancestry and similarity without contact are no longer entered as
`exchange`.

Changes in v1.2: two new statuses, `incidental` (covered in passing without
being asked) and `deferred` (computed at synthesis, so `corroborated_by` no
longer borrows `not_requested`); an optional `claim_match` flag and two new
source types on citations; new leaves for system boundaries (1), formative
figures and premodern dated events (2), borrowed evidence (5, 13), preclinical
and constituent evidence (13), loss of patronage and post-colonial disruption
(8), revival context (9) and supranational standards (10); multiple tags and a
native category per modality (6); a relationship `kind` distinguishing exchange
from shared descent (15); and field 18 for the report's own conclusions. Field 8
is renamed `disruption`, since not every tradition's rupture was colonial.

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
  status: filled | partial | incidental | absent | not_requested | deferred
  value: <content, or null>
  citations:
    - source: <author/title/year or institution/document>
      type: tertiary-review | systematic-review | meta-analysis | reference-work |
            institutional | primary-study | historical-monograph | statute |
            news | aggregator | catalog-listing | practitioner-site |
            open-encyclopedia | market-research | unclear
      citation_strength: direct | indirect | unclear
      claim_match: matches | mismatch    # optional
  register: emic | historical-scholarship | biomedical-evidence | regulatory |
            economic
  notes: <disputes, caveats, why absent — optional>
```

**Status values.**
- `filled` / `partial` — the report covers it.
- `incidental` — the source research prompt never asked, but the report covers
  the topic in passing. Keep the content in `value`. Coverage is not systematic,
  so its thinness says nothing about the literature: **not a gap-pass search
  target**, and another system's silence on the same leaf is not a contrast.
- `absent` — the report addressed the topic and the literature came up short, or
  the report should plausibly have covered it and did not. A real gap.
- `not_requested` — the source research prompt never asked, so silence here says
  nothing about the literature. **Do not send these to the gap pass as search
  targets for missing evidence; they are prompt-coverage gaps, not evidence gaps.**
  Expect this status, or `incidental`, on fields 6, 7, 11, 19 and parts of 1.
- `deferred` — a leaf the codebook says is computed at synthesis. `value` stays
  null. Mappers never fill it and no pass searches for it.

Keeping these apart is the whole point. A field can be empty because nobody
looked, because nobody asked, or because nothing exists, and the three lead to
completely different next actions.

The source research prompt never asks for fields 18 or 19, so they are never
`absent`: either the report volunteers them (`filled`, `partial` or, for field
19, `incidental`) or they are `not_requested`.

**citation_strength.**
- `direct` — the work itself, the statute text, the journal article.
- `indirect` — a real claim reached through a bookseller page, catalog entry,
  expat guide, practitioner blog, state media outlet or news aggregator.
- `unclear` — cannot tell from the report.

**Source types.** `practitioner-site` is a clinic, pharmacy, manufacturer or
practitioner's own website. `open-encyclopedia` is an openly edited reference
such as Wikipedia. `market-research` is a commercial market-research or
industry-analyst firm's estimate. All three are `indirect` by rule 4.

**claim_match** (optional). Set `mismatch` where the cited source, judged from
its title or description, does not appear to be about the claim it is cited for
— for example, a bibliography entry that names a different study. Set `matches`
only where you can see that it is. Omit it otherwise. A `mismatch` is a
verification target like any `indirect`.

Every `indirect` is a verification target. These cluster in fields 8, 9 and 10.

**register** keeps the tradition's own claims, historical scholarship, biomedical
evidence, regulatory fact and economic figures from blending together.

## Leaf naming

Leaf keys are exactly the codebook's sub-field names — never invented keys.
Where a field holds a variable number of items, they go as a list inside one
leaf's `value`. List-valued leaves use these names and item shapes:

| Field | Leaf | Value is a list of |
|---|---|---|
| 1 identification | `system_boundary` | `{tradition, relation, fields_affected, description}` |
| 2 canon_and_transmission | `key_figures` | `{name, dates, role}` |
| 3 construct_debate | `positions` | `{scholar, work, year, position, evidence_base}` |
| 6 modalities | `items` | `{name, native_category, tags, description}` |
| 8 disruption | `colonial_power` | `{power, mode, period, description}` |
| 8 disruption | `post_colonial_disruption` | `{label, date, description}` |
| 9 revival_and_institutionalization | `diffusion_abroad` | `{region, period, channel, description}` |
| 10 legal_status | `jurisdictions` | `{jurisdiction, regulator, statute, year, scope_of_practice, prescribing_rights, integration_with_public_health_system, recognition_tier}` |
| 10 legal_status | `supranational_standards` | `{body, instrument, year, scope}` |
| 13 evidence_state | `reviews` | `{modality, best_available_review, type, year, size, conclusion, certainty_rating, methodological_limitations_noted}` |
| 13 evidence_state | `preclinical_and_constituent_evidence` | `{agent, finding, type, year, citation}` |
| 15 contact_and_borrowing | `relationships` | `{other_tradition, kind, direction, period, evidence_type, status}` |
| 17 self_reported_gaps | `inventory` | `{kind, text}` |
| 18 report_conclusions | `revision_thresholds` | `{domain, threshold, would_change}` |
| 18 report_conclusions | `recommendations` | `{audience, text}` |
| 19 economics | `domestic_market_size` | `{figure, currency, year, measure, estimator}` |
| 19 economics | `global_market_estimates` | `{figure, currency, year, measure, estimator}` |
| 19 economics | `major_manufacturers` | `{name, products, figure, currency, year, measure}` |

Likewise `diagnostics.reliability_evidence`, every
`evidence_borrowed_from_other_traditions` and every `dated_events` (fields 2, 8
and 9) are single leaves whose value is a list. A jurisdiction or study
appearing in one report and not another is then a difference in content, not in schema — which is what keeps
schema errors meaningful.

## Misfit rule

A **schema misfit** is report content for which no leaf, enum value or routing
rule in this codebook gives a place. It is what a mapper lists in the fourth
closing list. These are not misfits and belong in the leaf's `notes`: content
that fits a leaf imperfectly, a leaf that suits this tradition loosely, a choice
between two leaves the codebook already ranks, and a leaf holding one awkward
entry. When a routing rule above answers the question, follow it and report
nothing. Report a misfit only if you can name the content, name the field or
enum value you would add, and say why no existing rule reaches it. Write `None`
otherwise.

## Fields

### 1. identification
- `system_name`, `alternate_names` (including endonyms), `primary_regions`
- `practitioner_estimate` — count, source, year
- `system_boundary` — traditions the report treats as the same system, a
  variant, a sibling sharing its origins, or a grouping it is regulated under.
  Per entry: `relation` (same_system_variant | sibling | absorbed_strand |
  regulatory_grouping | premodern_predecessor), and `fields_affected` — which fields in this
  extraction draw on content that really belongs to that other tradition.
  `absorbed_strand` is a distinct tradition this system has partly
  incorporated while it also persists, or persisted, on its own terms.
  `premodern_predecessor` is the premodern tradition or traditions the modern
  system was selectively rebuilt from, where the report treats the relation as
  reconstruction rather than simple continuity. Whether that reconstruction
  amounts to invention is field 3's question, not this leaf's.
  Evidence from a `same_system_variant` (texts, reliability studies, clinical
  trials) is this tradition's own: record it in the ordinary leaf and list the
  leaf in `fields_affected`. It is never `evidence_borrowed_from_other_traditions`,
  which is only for a tradition the report itself treats as different.

### 2. canon_and_transmission
- `foundational_texts` — title, approximate date, attributed author
- `secondary_canon`
- `dating_and_authorship_disputes` — named scholars and their positions
- `transmission_mode` — textual, oral, lineage-based, mixed
- `redaction_history`
- `external_dating_anchors` — excavated manuscripts, dated copies, translations
- `key_figures` — formative figures of the premodern tradition: authors,
  commentators, translators, patrons, with dates and role. Revival-era figures
  belong in field 9. Modern scholars of the tradition belong in
  `dating_and_authorship_disputes` or field 3's `positions`, never here.
- `dated_events` — every dated premodern event (composition, translation,
  commentary, rediscovery), as in field 8

### 3. construct_debate
Whether the modern system is continuous with premodern practice or substantially
a 19th–20th century construction. Named scholars, their specific positions, and
what each side's evidence base actually is.
- `positions` — each named scholar's position and its evidence base (see Leaf
  naming)
- `report_adjudication` — the verdict the report itself offers on the debate, if
  any, recorded as the report's stance and not as consensus. `register:
  historical-scholarship`. Where the report lays out the positions without
  judging between them, mark it `partial` and say so in `notes`; `absent` only
  where the report covers the debate and should plausibly have weighed it.
  Synthesis may compare these but must not treat them as evidence, as with
  field 18.

### 4. theoretical_primitives
- `constituents`, `balance_logic`, `correspondence_system`, `etiology`, `nosology`
  `correspondence_system` is a wider cosmological or seasonal scheme the
  tradition maps onto its constituents. Pairings inside the constituent scheme
  (quality-humour-element and the like) go in `constituents` and
  `balance_logic`. Where the tradition has no wider scheme, mark the leaf
  `filled` with value `not_applicable` and say why in `notes`.
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
- `evidence_borrowed_from_other_traditions` — reliability studies conducted
  on a different or neighbouring tradition that the report applies to this one.
  List them here, not under `reliability_evidence`.

**Do not summarize this field into a verdict.** Values from different designs
are not comparable and must not be averaged, ranked or collapsed.

### 6. modalities
For each: `name`, `native_category` (the tradition's own grouping, if the report
gives one), `tags` (one or more), `description`. Tags: `herbal` |
`animal-derived` | `mineral-metal` | `manual` | `needle` | `procedural` |
`thermal` | `dietary` | `regimenal` | `surgical` | `mind-body` | `ritual`.
`procedural` covers evacuative and blood-drawing procedures such as
venesection, cupping, leeching and induced purging. Where the tradition's own
category bundles several tags, keep one item with all of them rather than
splitting it.
Tags record what the tradition uses on purpose. A substance that appears only
as a contaminant or adulterant (heavy metals in herbal products, for example)
does not earn a tag; it belongs in field 14.

### 7. materia_medica
- `pharmacological_framework`, `flagship_agents`, `preparation_traditions`

### 8. disruption
Pressure that broke or displaced the tradition, whatever its source. Where the
report establishes that a sub-field does not apply — a tradition never
colonized, a state never partitioned — mark it `filled` with value
`not_applicable` and say why in `notes`. That is a finding, not a gap. Use
`absent` only where the report leaves it unclear.
- `loss_of_patronage` — pre-colonial or dynastic decline: collapse of a court,
  state or institution that sustained the tradition, with dates
- `period`
- `colonial_power` — the external power or powers whose pressure displaced the
  tradition. Per entry: `power`, `mode` (colonial_rule | semi_colonial |
  indirect_foreign_pressure), `period`, `description`. `semi_colonial` is
  partial foreign control short of annexation — treaty ports, concessions,
  extraterritoriality; `indirect_foreign_pressure` is the influence of a
  foreign medical system or a foreign modernization model adopted by a state
  that was never under foreign rule. Where the rupture was domestic alone, mark
  it `filled` with value `not_applicable` and say so in `notes`; the domestic
  drivers go under `suppression_or_marginalization`.
- `suppression_or_marginalization` — specific policies with dates
- `abolition_attempts` — formal proposals, votes, outcomes, dates
- `practitioner_response` — organized resistance, dates, bodies formed
- `post_colonial_disruption` — partition, state succession, revolution or other
  breaks after the colonial or dynastic period that split or relocated
  institutions, each dated
- `dated_events` — every dated event, as `{label, date, description}`. Use a
  plain canonical label (for example "Macaulay's Minute", "Bhore Committee").
  Consistent labels are what let synthesis detect events shared across systems.
  Do **not** attempt to mark events as shared — that is computed at synthesis.

### 9. revival_and_institutionalization
- `revival_context` — what the revival responded to: anti-colonial nationalism,
  state-led modernization, post-revolutionary policy, market demand, or other
- `key_figures` and dates
- `nationalist_framing`
- `standardization_events` — textbooks, curricula, colleges, dates
- `internal_factions` — purist versus integrationist splits, named
- `state_sponsorship`
- `diffusion_abroad` — spread and institutionalization outside the country of
  origin: where, when, by what channel (emigration, diplomatic opening, training
  programs, commercial export). This is not revival; `revival_context` is about
  the country of origin. Where the tradition has no single country of origin,
  "abroad" means outside every region the report places its home. Recognition
  in neighbouring states belongs in field 10 `jurisdictions`, not here. Where
  the report records no such spread, mark it `absent` or `not_requested` as
  usual.
- `dated_events` — as in field 8

### 10. legal_status
One entry per jurisdiction: `jurisdiction`, `regulator`, `statute` with year,
`scope_of_practice`, `prescribing_rights`, `integration_with_public_health_system`,
`recognition_tier` (full medical system | statutory registration | title
protection | supplement/wellness only | unregulated).
- `supranational_standards` — normative instruments above the level of a
  jurisdiction that set training, practice or product standards (WHO
  benchmarks, regional pharmacopoeias, harmonization agreements). WHO strategy,
  ICD-11 and collaborating centres stay in field 16 `who_engagement`.

### 11. education_and_licensure
- `degree_programs`, `duration`, `accrediting_body`
- `licensure_requirements`
- `biomedical_content_in_curriculum` — biomedical teaching within the
  tradition's own programs
- `tradition_content_in_biomedical_curriculum` — the reverse: teaching of this
  tradition within biomedical degree programs

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
- `preclinical_and_constituent_evidence` — isolation of active constituents,
  animal and in-vitro pharmacology. Record it, but never let it stand in for a
  clinical review.
- `evidence_borrowed_from_other_traditions` — clinical reviews or trials the
  report applies to this tradition that were conducted on a different one, or
  that cluster in another tradition's practice. List them here, not in
  `reviews`. This applies only where the report itself frames the evidence as
  another tradition's. Where the report treats a modality as this tradition's
  own but the reviews cover the modality in general or cluster elsewhere, put
  them in `reviews` and say so in the entry's `methodological_limitations_noted`.

### 14. safety
- `adulteration_and_contamination` — with measured figures where given
- `intrinsic_toxicity` — agents with documented harm, and the mechanism class
  (heavy metal | plant toxin | procedural | interaction | pharmaceutical
  adulterant | indirect). `pharmaceutical adulterant` is undeclared biomedical
  drugs (steroids, antibiotics and the like) found in products; `indirect` is
  harm from delayed, forgone or displaced biomedical care rather than from the
  agent itself.
- `documented_adverse_events` — case series, surveillance, with citations
- `regulatory_actions_taken` — bans, import alerts, advisories, with dates
- `evidence_borrowed_from_other_traditions` — flag any harm claim resting on
  data from a different system. These do not belong in this system's cell.

### 15. contact_and_borrowing
Per relationship: `other_tradition`, `kind` (exchange | descent |
shared_descent | parallel | same_system_variant), `direction`, `period`,
`evidence_type` (documented translation | textual attestation | structural
parallel), `status` (demonstrated | contested | convergence). `exchange` is
borrowing between contemporaries; `descent` is direct ancestry, where one
tradition derives from the other, and `direction` runs ancestor → descendant;
`shared_descent` is a common ancestor, not borrowing between the two;
`parallel` is similarity with no contact the report can show, and pairs with
status `convergence`; `same_system_variant` is a tradition the report treats as
the same system under another name. For `shared_descent`, `parallel` and
`same_system_variant`, `direction` may be null.
- `corroborated_by` — status `deferred`, value null. Computed at synthesis,
  where the whole corpus is visible. Independent corroboration from the other
  end of an exchange is a finding, but a mapper seeing one report cannot
  establish it.

### 16. contemporary_controversies
- `who_engagement` — strategies, benchmarks, ICD-11, centres
- `integration_disputes` — within the country of origin, with litigation status
- `conservation_and_sourcing`
- `intellectual_property` — biopiracy cases, defensive databases, Nagoya exposure
- `politicized_episodes` — pandemic-era promotion, state endorsement, court cases
- `research_methodology_disputes` — disputes over how the tradition's
  interventions can be tested: the validity of sham or placebo controls,
  individualized or pattern-stratified trial designs, and competing readings of
  the same effect sizes, with the named parties on each side. The trial results
  themselves stay in field 13.

### 17. self_reported_gaps
Verbatim inventory of what the source report itself said it searched for and did
not find, plus its own source-quality caveats and contested-item flags.

Kept separate from the extraction's own `absent` findings. Where the two diverge,
that divergence is informative: self-reported gaps are the ones the research pass
noticed, and the rest are the ones it could not see in itself.

### 18. report_conclusions
What the report itself concludes beyond answering its questions. Never `absent`
— see Status values.
- `revision_thresholds` — conditions the report says would change its
  conclusions: the domain, the evidence threshold, and what would change
- `recommendations` — practice, patient or policy recommendations it makes,
  with their audience

These are the report author's stance, not findings. Synthesis may compare them
but must not treat them as evidence.

### 19. economics
Commercial and industrial scale. `register: economic`. Neither research prompt
asks about it, so expect `not_requested` or `incidental`; never `absent`.
- `domestic_market_size` — industry output or market size in the country of
  origin, each figure with its year, what it measures (output, revenue, retail
  sales) and who estimated it
- `global_market_estimates` — as above, worldwide. Keep every estimate the
  report gives, however far apart; do not reconcile or average them, and carry
  the report's own caveats on their reliability into `notes`
- `major_manufacturers` — named firms, their principal products, and any
  revenue figure with its year

Estimates from commercial market-research firms are `type: market-research`,
`citation_strength: indirect`. Market size says nothing about efficacy, safety
or use; never let field 19 stand in for fields 12 or 13.

## Mapping rules

1. Extract only. Do not supplement the report with outside knowledge.
2. Preserve the source report's citation for every value carried over.
3. Uncited claim → `type: unclear` and note it. These are verification targets.
4. Claim sourced through an aggregator, bookseller, blog, news outlet or
   market-research firm →
   `citation_strength: indirect`, regardless of how solid the claim itself is.
5. Where the report's framing does not fit a field, record what it does say and
   note the mismatch rather than forcing it.
6. Where a field is `absent`, say what specifically is missing, precisely enough
   to become a search target.
7. Where a field is `not_requested` or `incidental`, say so plainly and do not
   write a search target for it.
8. Where a leaf is `deferred`, leave `value` null.

## Schema revision

If a report contains something substantial that no field accommodates, propose
the field rather than discarding the content. Schema changes apply to all
systems, and earlier mappings are re-run. Every mapping declares
`schema_version`, and the merge refuses one that does not match this file.
