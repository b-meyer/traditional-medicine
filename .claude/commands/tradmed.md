---
description: Run tradmed passes 1–5 (map, merge, gap, verify, apply) for one system
argument-hint: <system> [--resume]
---

Run the tradmed extraction pipeline for one medical system: `$ARGUMENTS`

The first word of the arguments is the system slug — the folder name under
`reports/`.

Every run starts fresh: delete `work/<system>/` before starting, unless
`--resume` is present. A run from scratch is the only way to be sure every
output was built against the current codebook.

## The isolation rule — read before invoking anything

Each pass runs in a subagent whose instructions are complete and pinned in its
own definition file. When you invoke a subagent, pass **only** the labeled
inputs listed for that pass, verbatim, one per line. Nothing else.

Do not describe the project, the pipeline, its purpose, other systems in the
corpus, earlier results, or what you expect the subagent to find. Do not
paraphrase or add to its task. Contamination of isolated passes through
orchestrator-authored framing is the specific failure this harness exists to
prevent. If you are tempted to add helpful context, don't.

## Preflight

1. `reports/<system>/v2.md` must exist. If not, stop and say so.
2. Note whether `reports/<system>/v1.md` exists. If not, skip pass 2 — the merge
   runs v2 alone.
3. Bibliographies are optional: `reports/<system>/v2-bib.md`,
   `reports/<system>/v1-bib.md`. Pass `none` where missing.
4. Confirm PyYAML imports (`python -c "import yaml"`). If not, run
   `pip install -r scripts/requirements.txt`.
5. Unless `--resume` is present, delete `work/<system>/`. Then create it.

**Resuming** (`--resume` only): skip any pass whose output files already exist,
and say which passes you skipped. Use it only to pick up a run that was
interrupted without the codebook changing — never after a checkpoint stop, since
those mean the codebook is being revised. `merge.py` refuses mappings whose
`schema_version` doesn't match the codebook, so a stale resume fails at pass 3.

## Pass 1 and pass 2 — mapping (run in parallel)

Invoke `tradmed-map-v2` with exactly:

```
CODEBOOK: reference/codebook.md
REPORT: reports/<system>/v2.md
BIB: reports/<system>/v2-bib.md   (or none)
OUT_YAML: work/<system>/v2.yml
OUT_LISTS: work/<system>/v2-lists.md
```

If v1 exists, invoke `tradmed-map-v1` in parallel with the same five labels,
pointing at the v1 files and `v1.yml` / `v1-lists.md`.

### Checkpoint A — schema misfit

Read the **Schema misfit** section of each `-lists.md` file. If any is not
`None`, **stop**. Show the user the misfit entries and say the codebook needs
revising before continuing, and that every system must then be re-run. Do not
continue to pass 3. A matrix built from two schema
versions is worse than none.

## Pass 3 — merge (script, no model)

Run `python scripts/merge.py <system>` from the repository root.

### Checkpoint B — schema errors

If it exits with any non-zero status, **stop** and show the user its output. A
`schema_version` mismatch means a stale mapping — re-run without `--resume`.

If it exits with status 2, **stop**. Show the user the schema errors from
`work/<system>/diff.md`. These mean the two mappings disagree on leaf structure,
usually a mapper inventing keys. Do not continue.

## Pass 4 and pass 5 — gap and verify (run in parallel)

Skip the gap pass if its worklist has no entries. The verify worklist comes in
batches, `work/<system>/verify-worklist-NN.yml` (01, 02, …); if there are none,
skip pass 5.

Invoke `tradmed-gap` with exactly:

```
SYSTEM: <system>
WORKLIST: work/<system>/gap-worklist.yml
CODEBOOK: reference/codebook.md
OUT: work/<system>/gap-fragments.yml
```

For each verify batch, invoke a separate `tradmed-verify` in parallel with
exactly:

```
SYSTEM: <system>
WORKLIST: work/<system>/verify-worklist-NN.yml
CODEBOOK: reference/codebook.md
OUT: work/<system>/verify-fragments-NN.yml
```

Launch the gap agent and every verify agent together. Each verify agent gets
only its own batch; the isolation rule applies to each one individually. When
resuming, skip only the batches whose fragments file already exists.

## Apply

Run `python scripts/apply_fragments.py <system>`.

## Report

Tell the user, briefly:

- counts per status after merge, and how many leaves v1 filled
- gap: found vs not_found
- verify: confirmed, corrected, unverifiable, summed across batches, and how
  many batches ran
- anything rejected in `apply-log.md` — rejections mean an agent went off its
  worklist, which is worth knowing
- which fields are `not_requested` or `incidental` after the merge. If
  modalities or another field is `not_requested` for this system, flag it: that
  is a question-set gap, not an evidence gap, and it may affect the comparison.
  `incidental` means some content exists but coverage is not systematic.

Point them at `work/<system>/final.yml`, `diff.md` and `apply-log.md`. Do not
paste the YAML.
