---
description: Run tradmed passes 6–7 (synthesis and audit) across every finished system
---

Run the cross-system synthesis and audit.

## The isolation rule

Pass each subagent **only** the labeled inputs below, verbatim. Do not describe
the project, summarize the extractions, share your own view of the corpus, or add
anything to the task. Each subagent's instructions are complete.

## Preflight

1. Find every `work/*/final.yml`.
2. Every system with a folder under `reports/` that contains a `v2.md` must have a
   `final.yml`. If any is missing, stop and list them — a partial corpus produces
   a misleading comparison.
3. Every `final.yml` must declare the same `schema_version`, and it must match
   the version in the title line of `reference/codebook.md`. If not, stop and
   list the stale systems: they were mapped against a different codebook and
   must be re-run with `/tradmed <system>`.

## Pass 6 — synthesis

Invoke `tradmed-synthesis` with exactly:

```
CODEBOOK: reference/codebook.md
EXTRACTIONS: <every work/*/final.yml path, comma-separated>
OUT: out/synthesis.md
```

## Pass 7 — audit

Only after pass 6 finishes. Invoke `tradmed-audit` with exactly:

```
ANALYSIS: out/synthesis.md
EXTRACTIONS: <the same paths>
OUT: out/audit.md
```

The audit runs in its own subagent context, so it never sees the synthesis being
written — which is the point.

## Report

Give the user the chapter list, the audit's counts per class, and point them at
`out/synthesis.md` and `out/audit.md`. If the audit found overreaching,
unsupported or miscompared claims, say so plainly — those need fixing before the
analysis is used for anything.
