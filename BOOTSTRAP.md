# Bootstrap

Run once, in the first Claude Code session on the repo the zip was uploaded to.
Do not run the pipeline in this session.

1. **Flatten.** The zip extracts to a top-level `tradmed/` folder. Move its entire
   contents — including the hidden `.claude/` directory — to the repository
   root, so `.claude/`, `scripts/`, `reference/`, `reports/`, `work/`, `out/`,
   `README.md` and this file sit at the root. Then delete the zip and the empty
   `tradmed/` folder.

2. **Dependencies.** Run `pip install -r scripts/requirements.txt`, then confirm
   `python -c "import yaml"` succeeds. If pip is blocked by the environment's
   network settings, say so plainly — the merge and patch scripts need PyYAML.

3. **Check the harness.** Confirm all of these exist:
   - `.claude/agents/`: tradmed-map-v2, tradmed-map-v1, tradmed-gap,
     tradmed-verify, tradmed-synthesis, tradmed-audit (`.md` each)
   - `.claude/commands/`: `tradmed.md`, `tradmed-synthesize.md`
   - `reports/unani/`, `reports/tcm/`, `reports/ayurveda/`: each with `v1.md`,
     `v2.md`, `v1-bib.md`, `v2-bib.md`

4. **Smoke-test the scripts.** Run `python -m py_compile scripts/*.py`.

5. **Commit and push** everything to the default branch. If the environment only
   allows a branch and pull request, open the PR and say it must be merged
   before the next step.

6. **Report**, briefly: what was moved, whether PyYAML works, anything missing,
   and where the commit or PR landed. Then tell the user:

   > Start a new Claude Code session on this repo and run `/tradmed unani`.
   > The agents and commands load when a session starts, so this session can't
   > run them — and running the pipeline here would fall back to general-purpose
   > agents with web access, which the harness exists to prevent.
