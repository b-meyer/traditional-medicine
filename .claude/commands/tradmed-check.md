---
description: Check the codebook against every system's v1 and v2 reports (mapping passes only, no merge)
argument-hint: [system ...]
---

Run the codebook conformance check: mapping passes 1 and 2 only, for `$ARGUMENTS`
(default: every folder under `reports/`). Its one output is whether any mapper
reports a schema misfit. It does not merge, gap-fill or verify, and it never
touches `work/<system>/`.

The isolation rule from `/tradmed` applies unchanged. Pass each subagent only the
labeled inputs below, verbatim, one per line, and add nothing else: no project
description, no earlier results, no hint of what was flagged before.

## Preflight

1. For each system, `reports/<system>/v2.md` must exist. Note whether `v1.md`
   exists; if not, that system runs v2 alone.
2. Bibliographies are optional: pass `none` where `v1-bib.md` or `v2-bib.md` is
   missing.
3. Delete `work/check/` if it exists, then create `work/check/<system>/` for each
   system. `work/check/` is git-ignored scratch space.

## Mapping

Launch every mapper for every system in one parallel batch. For each system,
invoke `tradmed-map-v2` with:

```
CODEBOOK: reference/codebook.md
REPORT: reports/<system>/v2.md
BIB: reports/<system>/v2-bib.md   (or none)
OUT_YAML: work/check/<system>/v2.yml
OUT_LISTS: work/check/<system>/v2-lists.md
```

and, if v1 exists, `tradmed-map-v1` with the same five labels pointed at the v1
files and `v1.yml` / `v1-lists.md`.

## Result

Read the **Schema misfit** section of every `-lists.md`. Report one table, a row
per system and report version: `None`, or the misfit entries verbatim. Also give
the status counts each mapper returned.

- **Pass**: every section is `None`.
- **Fail**: anything else. Show the entries and stop. Do not edit the codebook
  from this command; revising it is a separate step, and the check is re-run
  afterwards from scratch.

Mapper judgment varies from run to run, so one clean pass is not convergence.
The codebook has converged when the check passes on **two consecutive runs with
no codebook change between them**. Say which run this was if you know, and say
that a second unchanged run is still owed after a first pass.

After convergence, the full pipeline is `/tradmed <system>` for each system.
Every system must be re-run there whenever the codebook version changes.
