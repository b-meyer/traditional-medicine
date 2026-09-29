"""Pass 3 — deterministic merge of a system's v1 and v2 extractions.

Usage:  python scripts/merge.py <system>

Reads   work/<system>/v2.yml, work/<system>/v1.yml (optional)
Writes  work/<system>/merged.yml
        work/<system>/diff.md
        work/<system>/gap-worklist.yml
        work/<system>/verify-worklist.yml

Precedence, per leaf:
  1. v2 filled/partial        -> v2, always
  2. v2 incidental            -> v1 if v1 is filled/partial, else v2
  3. v2 not_requested         -> v1 if v1 is filled/partial/incidental, else v2
  4. v2 absent or deferred    -> v2, always. v1 never fills a field v2 searched
                                 and came up empty on.
Every leaf is tagged source_report: v1 | v2.
Leaves present in v1 but not v2 are schema errors: reported, never merged.
Both mappings must declare the codebook's schema_version.
"""

import copy
import os
import sys

from tradmed_lib import (FILLED, INCIDENTAL, STATUSES, codebook_version, dump, leaves, load,
                         set_path, weak_citations)

# How much content a leaf carries; v1 replaces v2 only where it ranks higher
# and v2 was never asked (rules 2 and 3).
RANK = {"filled": 2, "partial": 2, INCIDENTAL: 1}
V1_MAY_REPLACE = {INCIDENTAL, "not_requested"}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    system = sys.argv[1]
    d = os.path.join("work", system)
    v2 = load(os.path.join(d, "v2.yml"))
    v1_path = os.path.join(d, "v1.yml")
    if os.path.exists(v1_path):
        v1 = load(v1_path)
    else:
        # New systems have no earlier generation to mine: merge is a pass-through.
        print(f"{system}: no v1.yml — merging v2 alone")
        v1 = None

    version = codebook_version()
    for name, doc in (("v2", v2), ("v1", v1)):
        if doc is None:
            continue
        if "fields" not in doc:
            sys.exit(f"{name}.yml has no top-level 'fields' key")
        if str(doc.get("schema_version")) != version:
            sys.exit(f"{name}.yml declares schema_version {doc.get('schema_version')!r}, "
                     f"codebook is {version!r}. Re-run /tradmed {system}.")
    if v1 is None:
        v1 = {"fields": {}}

    merged = copy.deepcopy(v2)
    merged["source_report"] = "merged"

    v1_leaves = dict(leaves(v1["fields"]))
    v2_leaves = dict(leaves(v2["fields"]))

    rows, errors, from_v1 = [], [], []

    for path, leaf2 in v2_leaves.items():
        s2 = leaf2.get("status")
        if s2 not in STATUSES:
            errors.append(f"`{path}` has invalid status in v2: {s2!r}")
        leaf1 = v1_leaves.get(path)
        s1 = leaf1.get("status") if leaf1 else "—"

        if s2 in V1_MAY_REPLACE and leaf1 and RANK.get(s1, 0) > RANK.get(s2, 0):
            chosen = copy.deepcopy(leaf1)
            chosen["source_report"] = "v1"
            from_v1.append(path)
            outcome = "v1 fills"
        else:
            chosen = copy.deepcopy(leaf2)
            chosen["source_report"] = "v2"
            if s2 == "absent" and s1 in FILLED:
                outcome = "v2 absent; v1 value refused"
            else:
                outcome = "v2"
        set_path(merged["fields"], path, chosen)
        rows.append((path, s1, s2, outcome))

    for path in v1_leaves:
        if path not in v2_leaves:
            errors.append(f"`{path}` exists in v1 but not v2 — schema mismatch, not merged")

    dump(merged, os.path.join(d, "merged.yml"))

    # Worklists are computed from the merged result, so v1-sourced values with
    # weak citations land on the verification list rather than going straight in.
    gap, verify = [], []
    for path, leaf in leaves(merged["fields"]):
        if leaf.get("status") == "absent":
            gap.append({"path": path, "missing": leaf.get("notes") or "(no note given)"})
        weak = weak_citations(leaf)
        if weak and (leaf.get("status") in FILLED or leaf.get("status") == INCIDENTAL):
            verify.append({
                "path": path,
                "source_report": leaf.get("source_report"),
                "value": leaf.get("value"),
                "weak_citations": weak,
            })

    dump({"system": system, "pass": "gap", "entries": gap},
         os.path.join(d, "gap-worklist.yml"))
    dump({"system": system, "pass": "verify", "entries": verify},
         os.path.join(d, "verify-worklist.yml"))

    with open(os.path.join(d, "diff.md"), "w", encoding="utf-8") as f:
        f.write(f"# {system} — v1 vs v2 field diff\n\n")
        f.write(f"- Leaves: {len(v2_leaves)}\n")
        f.write(f"- Filled from v1: {len(from_v1)}\n")
        f.write(f"- Gap worklist: {len(gap)}\n")
        f.write(f"- Verify worklist: {len(verify)}\n")
        f.write(f"- Schema errors: {len(errors)}\n\n")
        if errors:
            f.write("## Schema errors\n\n")
            f.writelines(f"- {e}\n" for e in errors)
            f.write("\n")
        f.write("## Per leaf\n\n| Leaf | v1 | v2 | Merged from |\n|---|---|---|---|\n")
        f.writelines(f"| `{p}` | {a} | {b} | {o} |\n" for p, a, b, o in rows)

    print(f"{system}: {len(v2_leaves)} leaves, {len(from_v1)} filled from v1, "
          f"{len(gap)} gap, {len(verify)} verify, {len(errors)} schema errors")
    if errors:
        print("Schema errors found — see diff.md. Resolve before continuing.")
        sys.exit(2)


if __name__ == "__main__":
    main()
