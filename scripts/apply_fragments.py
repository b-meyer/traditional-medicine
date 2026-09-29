"""Apply gap (pass 4) and verify (pass 5) fragments to a merged extraction.

Usage:  python scripts/apply_fragments.py <system>

Reads   work/<system>/merged.yml
        work/<system>/gap-worklist.yml,    work/<system>/gap-fragments.yml
        work/<system>/verify-worklist-NN.yml, work/<system>/verify-fragments-NN.yml
Writes  work/<system>/final.yml
        work/<system>/apply-log.md

Enforcement — the agents are told these rules; this script makes them binding:
  - A gap update is accepted only for a path on the gap worklist.
  - A verify update is accepted only for a path on its own batch's worklist.
  - Anything else is rejected and logged, never applied.
"""

import copy
import glob
import os
import sys

from tradmed_lib import FILLED, INCIDENTAL, dump, get_path, load, set_path

GAP_OK = {"found", "not_found"}
VERIFY_OK = {"confirmed", "corrected", "unverifiable"}


def apply(doc, frag, allowed, outcomes, tag, log, worklist_name):
    applied = 0
    for u in frag.get("updates") or []:
        path, outcome = u.get("path"), u.get("outcome")
        if path not in allowed:
            log.append(f"- REJECTED {tag} `{path}`: not on {worklist_name}")
            continue
        if outcome not in outcomes:
            log.append(f"- REJECTED {tag} `{path}`: unknown outcome {outcome!r}")
            continue
        leaf = get_path(doc["fields"], path)
        if leaf is None:
            log.append(f"- REJECTED {tag} `{path}`: path not found in merged extraction")
            continue

        searches = u.get("searches") or []
        if outcome in ("not_found", "unverifiable"):
            leaf = copy.deepcopy(leaf)
            note = f"{tag} pass: {outcome}. Searched: {'; '.join(searches) or '(none recorded)'}"
            if u.get("target"):
                note += f". Target: {u['target']}"
            leaf["notes"] = f"{leaf['notes']}\n{note}" if leaf.get("notes") else note
            leaf[f"{tag}_outcome"] = outcome
            set_path(doc["fields"], path, leaf)
            log.append(f"- {tag} `{path}`: {outcome}")
            continue

        new = u.get("field")
        # Verify may keep an incidental leaf incidental; it must not blank one.
        if not isinstance(new, dict) or new.get("status") not in FILLED | {INCIDENTAL}:
            log.append(f"- REJECTED {tag} `{path}`: {outcome} without a filled replacement leaf")
            continue
        new = copy.deepcopy(new)
        new["source_report"] = tag
        new[f"{tag}_outcome"] = outcome
        new["replaced_from"] = leaf.get("source_report")
        set_path(doc["fields"], path, new)
        applied += 1
        log.append(f"- {tag} `{path}`: {outcome}")
    return applied


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    system = sys.argv[1]
    d = os.path.join("work", system)
    doc = load(os.path.join(d, "merged.yml"))
    log = []

    # (worklist, fragments) pairs. Gap is one pair; verify is one per batch,
    # and each batch's agent may touch only its own batch's paths.
    passes = [("gap", GAP_OK, [("gap-worklist.yml", "gap-fragments.yml")]),
              ("verify", VERIFY_OK,
               [(os.path.basename(w), os.path.basename(w).replace("worklist", "fragments"))
                for w in sorted(glob.glob(os.path.join(d, "verify-worklist-*.yml")))])]

    counts = {}
    for tag, outcomes, pairs in passes:
        for wl_name, frag_name in pairs:
            frag_path = os.path.join(d, frag_name)
            if not os.path.exists(frag_path):
                log.append(f"- {tag}: no {frag_name}, skipped")
                continue
            worklist = load(os.path.join(d, wl_name))
            allowed = {e["path"] for e in worklist.get("entries") or []}
            counts[tag] = counts.get(tag, 0) + apply(doc, load(frag_path), allowed,
                                                     outcomes, tag, log, wl_name)

    doc["source_report"] = "final"
    dump(doc, os.path.join(d, "final.yml"))

    rejected = sum(1 for line in log if "REJECTED" in line)
    with open(os.path.join(d, "apply-log.md"), "w", encoding="utf-8") as f:
        f.write(f"# {system} — fragment application log\n\n")
        f.write(f"- Applied: {counts}\n- Rejected: {rejected}\n\n")
        f.writelines(line + "\n" for line in log)

    print(f"{system}: applied {counts}, rejected {rejected} — final.yml written")


if __name__ == "__main__":
    main()
