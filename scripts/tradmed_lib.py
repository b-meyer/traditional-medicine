"""Shared helpers for the tradmed pipeline scripts.

A "leaf" is any mapping that carries a `status` key. The codebook requires every
sub-field to be a leaf, which is what makes merging and patching deterministic.
"""

import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install -r scripts/requirements.txt")

FILLED = {"filled", "partial"}
# Content present but not systematically covered: never a gap target.
INCIDENTAL = "incidental"
STATUSES = {"filled", "partial", "incidental", "absent", "not_requested", "deferred"}
CODEBOOK = "reference/codebook.md"


def codebook_version(path=CODEBOOK):
    """The version in the codebook's title line, e.g. "1.2"."""
    with open(path, encoding="utf-8") as f:
        m = re.search(r"— v(\d+(?:\.\d+)*)", f.readline())
    if not m:
        sys.exit(f"{path}: no version in the title line")
    return m.group(1)


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        sys.exit(f"Missing file: {path}")
    except yaml.YAMLError as e:
        sys.exit(f"YAML parse error in {path}:\n{e}")
    if not isinstance(data, dict):
        sys.exit(f"{path}: expected a mapping at the top level")
    return data


def dump(data, path):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=100)


def is_leaf(node):
    return isinstance(node, dict) and "status" in node


def leaves(node, prefix=""):
    """Yield (dotted_path, leaf) for every leaf under node, in document order."""
    if is_leaf(node):
        yield prefix, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            yield from leaves(v, f"{prefix}.{k}" if prefix else str(k))


def get_path(root, path):
    node = root
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def set_path(root, path, value):
    parts = path.split(".")
    node = root
    for part in parts[:-1]:
        node = node[part]
    node[parts[-1]] = value


def weak_citations(leaf):
    """Citations that are indirect, untyped, or don't match their claim."""
    out = []
    for c in leaf.get("citations") or []:
        if not isinstance(c, dict):
            continue
        if (c.get("citation_strength") == "indirect" or c.get("type") == "unclear"
                or c.get("claim_match") == "mismatch"):
            out.append(c)
    return out
