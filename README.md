# tradmed — comparative traditional medicine pipeline

Claude Code harness for the seven-pass playbook in `reference/playbook.md`.
Each model pass runs in an isolated subagent; merges and patches are scripts.

## Setup

The harness is installed at the repo root and the six research reports are
already in `reports/`, so there is nothing to export or unpack. Start a fresh
Claude Code session on the repo (agents and commands load at session start) and
run `/tradmed unani`.

```
reports/
  unani/     v1.md  v2.md  v1-bib.md  v2-bib.md
  tcm/       v1.md  v2.md  v1-bib.md  v2-bib.md     (v2 is the clean re-run)
  ayurveda/  v1.md  v2.md  v1-bib.md  v2-bib.md
```

**About these report files.** They were rebuilt from the chat record of each
research session rather than exported, with `[Sn]` markers placed at the end of
each span the research tool attributed to a source, numbered to match the
`-bib.md` file. Marker placement follows the tool's own character offsets, so
occasionally a marker lands a few words from the clause it supports. The report
text is otherwise the research output as delivered.

## Running

```
/tradmed unani            passes 1–5 for one system, from scratch
/tradmed unani --resume   pick up an interrupted run, skipping finished passes
/tradmed-synthesize       passes 6–7 across every finished system
```

Run order: unani, then tcm, then ayurveda, then synthesize. Unani first because
its corpus is thinnest, so schema problems surface on the cheapest run.

The run stops by itself at two checkpoints: a non-empty schema-misfit list after
mapping, and schema errors from the merge. Both mean the codebook needs revising
and **every** system must be re-run — mixed schema versions make the matrix
unusable. Every run starts by deleting `work/<system>/`, so a plain re-run is
always clean. `--resume` exists only for a run cut off partway with the codebook
unchanged; `merge.py` rejects any mapping whose `schema_version` differs from the
codebook's, so a stale resume fails loudly rather than mixing versions.

## What the harness enforces

| Rule | How |
|---|---|
| No search during mapping, synthesis or audit | Those agents have no web tools |
| No orchestrator framing leaking into passes | Prompts pinned in agent files; commands pass file paths only |
| v1 never overrides v2, never fills a v2 `absent` | `scripts/merge.py` precedence |
| Gap pass touches only `absent` leaves | `apply_fragments.py` rejects off-worklist paths |
| Verify pass touches only weakly-cited leaves | same |
| One schema version per matrix | `merge.py` checks `schema_version` against the codebook |
| Every value traceable | `source_report` tag on each leaf: v1, v2, gap or verify |
| Audit independent of synthesis | Separate subagent context |

## Outputs

```
work/<system>/
  v2.yml  v1.yml               raw mappings
  v2-lists.md  v1-lists.md     absent, not requested, weak sourcing, misfit
  merged.yml  diff.md          merge result and per-leaf v1/v2 diff
  gap-worklist.yml             absent leaves, sent to pass 4
  verify-worklist-NN.yml       indirect/unclear-cited leaves, in batches of 8,
                               one pass-5 agent per batch
  gap-fragments.yml  verify-fragments-NN.yml
  final.yml  apply-log.md      patched extraction; what was applied or rejected
out/
  synthesis.md  audit.md
```

`diff.md` doubles as the v1-versus-v2 prompt-generation comparison.

## Contamination

The whole design assumes each pass sees only what it's handed.

- **No project CLAUDE.md.** Don't add one describing the comparative project. If
  you run this inside a repo that has one, make sure it says nothing about the
  series, other traditions or expected findings.
- **No agent memory.** None of the agent files declares a `memory` field. Keep it
  that way.
- **Don't coach the orchestrator.** If you add context when invoking a command
  ("remember TCM had that aristolochic acid thing"), it may pass that on. Invoke
  the commands bare.

## Adding a system

Run the research prompt in `reference/research-prompt.md` in claude.ai with
research mode on, outside any project, with memory generation off. Check the
launched research brief before it finishes: if it mentions companion reports or
traditions you didn't name, discard and re-run. Save as
`reports/<system>/v2.md`, then `/tradmed <system>` — with no `v1.md`, the merge
simply passes v2 through — then re-run `/tradmed-synthesize`.

## Files

```
.claude/agents/     tradmed-map-v2  tradmed-map-v1  tradmed-gap
                    tradmed-verify  tradmed-synthesis  tradmed-audit
.claude/commands/   tradmed  tradmed-synthesize
scripts/            merge.py  apply_fragments.py  tradmed_lib.py
reference/          codebook.md (v1.5)  playbook.md  research-prompt.md
```
