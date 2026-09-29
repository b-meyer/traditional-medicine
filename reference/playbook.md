> Manual-run reference. The harness in this folder implements it. Where they differ — codebook v1.1 fixes leaf names and moves shared events and corroboration to synthesis — the files in `.claude/agents/` govern.

# Traditional Medicine Comparative Project — Playbook

Seven passes. Run passes 1–5 once per system, then 6–7 once for the whole corpus.
Every pass gets a fresh session. Nothing carries over in context; everything
carries over as an attached file.

**Systems:** TCM, Ayurveda, Unani.
**Run order within each pass:** Unani first — thinnest corpus, so it surfaces
schema problems soonest and a fix costs one re-run instead of three.

**Files you should have before starting:**
- `tradmed-codebook-v1.md`
- `tradmed-research-prompt-final.md` (only needed for new systems later)
- `<system>-v1.md` and `<system>-v2.md` — the six research reports, exported
- the bibliography for each, if it exported separately

**Settings per pass:**

| Pass | Search | Research mode | Notes |
|---|---|---|---|
| 1 Map v2 | off | off | search must be off |
| 2 Map v1 | off | off | search must be off |
| 3 Merge | n/a | n/a | scripted, no model |
| 4 Gap | plain search on | off | targeted only |
| 5 Verify | plain search on | off | targeted only |
| 6 Synthesis | off | off | corpus-constrained |
| 7 Audit | off | off | fresh session, not a continuation |

Search off in passes 1, 2, 6 and 7 is not a cost measure. With search on, the
model quietly fills gaps instead of reporting them, and you lose the gap signal —
which is the output those passes exist to produce.

---

## Pass 1 — Map the v2 report

**Attach:** `tradmed-codebook-v1.md`, `<system>-v2.md`, its bibliography.
**Produce:** `<system>-v2.yml`

Use `tradmed-mapping-prompt-v1.md` unchanged.

**Check before moving on.** If the fourth list (schema misfit) comes back
non-empty for any system, revise the codebook to v2 and re-run pass 1 for all
three. A matrix assembled from two schema versions is worse than no matrix.

---

## Pass 2 — Map the v1 report

**Attach:** `tradmed-codebook-v1.md`, `<system>-v1.md`, its bibliography.
**Produce:** `<system>-v1.yml`

Same prompt as pass 1 with one substitution: the `not_requested` guidance,
because v1 came from a different prompt and therefore has a different coverage
shape. Paste this instead of that bullet:

> The report was produced from an earlier research prompt that asked for history and origins, theoretical foundations, diagnosis, treatment modalities, current institutional status, scientific evidence and safety, and relationships to neighbouring systems — with an instruction to prefer peer-reviewed tertiary sources. It did not ask about diagnostic inter-rater reliability, the invented-tradition debate, demonstrated borrowing versus convergence, or contemporary controversies. Where a field has no corresponding topic behind it, mark it `not_requested` rather than `absent`, and do not write search targets for it.

Everything else in the prompt stands.

---

## Pass 3 — Merge

No model. Script it — the point is a deterministic, auditable merge.

**Precedence, strictly:**

1. v2 wins every field it filled. `filled` or `partial` in v2 → v2's value, always.
2. v1 supplies a field only where v2 is `not_requested`.
3. v1 never supplies a field v2 marked `absent`. If v2 addressed a topic and
   found nothing, v1 having something there means v1 was wrong or was reaching.
4. Every merged value carries `source_report: v1 | v2`.
5. Every v1-sourced value inherits `citation_strength` from the v1 mapping. Any
   `indirect` goes on the pass-5 list, not straight into the matrix.

**Why rule 3 is absolute.** v1 and v2 contradict each other on substance, not
just coverage. Unani v1 called the origins uncontroversial where v2 carries the
full Attewell–Alavi debate, and v1 inferred Unani's heavy-metal risk from
Ayurvedic JAMA data. Restricting v1 to `not_requested` fields confines it to
descriptive material in the tradition's own register, which is where it is
genuinely strongest and where the stakes are lowest.

**Produce:** `<system>-merged.yml`, plus a field-level diff of v1 against v2.
That diff is your prompt-generation comparison, now readable down a column.

---

## Pass 4 — Gap pass

**Attach:** `<system>-merged.yml`. Search on, research mode off.

Work only the `absent` list. Never the `not_requested` list.

> I have a structured extraction for **[SYSTEM]** as a medical tradition, attached. Several fields are marked `absent` — the research pass addressed the topic and the evidence was not found, or was not found in adequate form.
>
> Work only the `absent` entries. For each one, search directly for what the entry says is missing and report one of two outcomes:
>
> - **Found** — the value, with a direct citation. Prefer the study, statute text or scholarly work itself over any summary of it.
> - **Not found** — an explicit statement, naming the searches attempted and what a productive search would need to target.
>
> Rules:
> - Do not touch fields marked `not_requested`. Those were never asked about; their emptiness says nothing about the literature.
> - Do not revise, expand or improve fields already filled. This pass adds to gaps only.
> - For any reliability study you find, report its statistic type, design, population, rater and subject counts, and what was being agreed on — not just the coefficient.
> - For any regulatory claim, name the instrument, jurisdiction and year, and cite the statute or the regulator, not a news report about it.
> - Do not infer a value for one system from what is true of another tradition.
>
> Output as YAML fragments matching the attached schema, ready to merge, with a closing list of entries that stayed `absent`.

---

## Pass 5 — Verification

**Attach:** `<system>-merged.yml`. Search on, research mode off.

> I have a structured extraction for **[SYSTEM]**, attached. Some values carry `citation_strength: indirect` (a real claim reached through a bookseller page, catalog entry, expat guide, practitioner blog, state media outlet or news aggregator) or `type: unclear` (no citation at all).
>
> Work only those entries. For each, find the primary source and report one of three outcomes:
>
> - **Confirmed** — with the direct citation. Update `citation_strength` to `direct`.
> - **Corrected** — the claim is wrong or imprecise; give the corrected value and the direct source.
> - **Unverifiable** — no primary source located; say what you searched.
>
> Rules:
> - Statutes: cite the instrument itself or the regulator's own page. A news article reporting a law's passage is not verification of its contents.
> - Scholars' positions: cite the work. A bookseller listing confirms a book exists, not what it argues.
> - Dates and counts: name the source document and its year. Parliamentary answers relayed through press reports need the answer itself.
> - Do not add new claims. This pass only confirms, corrects or fails what is already there.
>
> Output as YAML fragments ready to merge, plus a list of everything still unverifiable.

**Prioritize.** You don't need to verify everything — verify what load-bears.
Anything used comparatively, anything that appears in only one system's report
and does comparative work, and every statute, date and statistic headed for the
synthesis.

After this, merge passes 4 and 5 into `<system>-final.yml`.

---

## Pass 6 — Synthesis

**Attach:** all three `<system>-final.yml` files and `tradmed-codebook-v1.md`.
Search off. Fresh session.

> Attached are structured extractions for three traditional medical systems — TCM, Ayurveda and Unani — against a shared codebook, plus the codebook itself.
>
> Write the comparative analysis. Work down the columns: one chapter per axis below, each drawing on the same field across all three systems. Do not write a chapter per system; three summaries side by side is what I already have.
>
> Axes:
> 1. Canon and dating — what each tradition's foundational texts are, how contested their dating is, and what external anchors exist
> 2. Construct and continuity — the invented-tradition debate in each, and whether the three debates have the same shape
> 3. Rupture and survival — colonial and modernizing pressure, abolition attempts, and what each system changed in order to survive
> 4. Diagnostic reproducibility — what the reliability literature shows, and what it shows about correspondence medicine as a class
> 5. Institutionalization and legal recognition — recognition tiers by jurisdiction, and what predicts where a tradition sits
> 6. Literature volume against evidence quality — treated as two separate questions
> 7. Harm — mechanism classes, regulatory response, and where enforcement has known gaps
> 8. Borrowing against convergence — demonstrated transmission versus structural parallel
> 9. Politicization — state sponsorship, pandemic-era promotion, integration disputes
>
> Hard constraints:
> - Use only the attached extractions. Do not search, and do not supplement from your own knowledge. If a claim needs a field that is empty, say the comparison cannot be made rather than filling it.
> - Any claim spanning systems must cite a filled field in every system it covers. Where a field is filled for only some, state the claim asymmetrically — "documented for X and Y; not established for Z" — never as a generalization.
> - Never compare reliability coefficients across different study designs. Clinician-versus-clinician agreement, questionnaire validation and instrument-versus-expert concordance are different quantities. Where the designs differ, say the systems cannot be ranked on this and explain why.
> - Events marked `shared_events` are one data point across two systems, not two. Do not count them twice as convergent evidence.
> - Corpus size differs by an order of magnitude between systems. Never let a thinner evidence base read as a weaker one.
> - Harm claims flagged as borrowed from another tradition do not belong in that system's column.
> - Distinguish throughout: what the traditions claim, what historians have established, what biomedical evidence shows, and what is regulatory fact.
>
> Close with: findings that hold across all three, findings that hold for some and not others with an account of why, and questions the corpus cannot answer.

---

## Pass 7 — Audit

**Attach:** the synthesis output and all three `<system>-final.yml` files.
Search off. **Fresh session, not a continuation** — a model does not audit its
own draft well.

> Attached is a comparative analysis of three traditional medical systems and the three structured extractions it was built from.
>
> Audit the analysis against the extractions. For every claim that spans more than one system, check that each system it covers has a filled field supporting it, and report:
>
> - **Supported** — cited fields exist in every system covered
> - **Overreaching** — stated generally but supported in only some systems; give the asymmetric restatement
> - **Unsupported** — no field backs it in any system
> - **Miscompared** — compares values that are not commensurable (different reliability designs, different corpus scales, shared events counted twice, harm data borrowed across traditions)
>
> Also flag any claim in the analysis that does not trace to an extraction at all — those came from the model's own knowledge and must be removed or verified separately.
>
> Be adversarial. The failure mode of comparative work is the elegant claim supported in one cell, and your job is to find those.

---

## Adding a fourth system later

Run the research prompt (`tradmed-research-prompt-final.md`), then passes 1, 4,
5 — skipping 2 and 3, since there is no v1 to mine. Then re-run 6 and 7 for the
whole corpus. The codebook stays fixed; if the new system breaks it, every
system's mapping is re-run against the revised schema.

**Contamination check for every new research run.** Before the report comes back,
read the launched research brief. If it mentions companion reports, a comparative
series, or traditions you did not name, the run is contaminated — kill it and
start again outside the project with memory generation off. Whether the model
reaches for memory is not deterministic, so removing the capability beats hoping.
