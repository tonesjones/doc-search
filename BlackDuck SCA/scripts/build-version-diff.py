#!/usr/bin/env python3
"""Build a compact, path-based comparison between two versioned corpora."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from corpus_utils import write_text_if_changed
from products import PRODUCTS

ROOT = Path(__file__).resolve().parents[1]


def normalized_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2]
    return re.sub(r"\s+", " ", text).strip()


def topic_map(cfg: dict) -> dict[str, dict]:
    manifest_path = ROOT / cfg["source_dir"] / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    docs_prefix = f"docs/{cfg['docs_root']}/"
    result: dict[str, dict] = {}
    for topic in manifest.get("topics", []):
        local_path = str(topic.get("localPath") or "").replace("\\", "/")
        if topic.get("status") != "done" or not local_path.startswith(docs_prefix):
            continue
        logical_path = local_path.removeprefix(docs_prefix)
        path = ROOT / local_path
        if not path.is_file():
            raise ValueError(f"Done topic is missing its Markdown file: {local_path}")
        result[logical_path] = {
            "title": topic.get("title") or logical_path,
            "local_path": local_path,
            "digest": hashlib.sha256(normalized_body(path).encode("utf-8")).hexdigest(),
        }
    return result


def link(topic: dict | None) -> str:
    if topic is None:
        return "—"
    return f"[{topic['title']}]({topic['local_path']})"


def build_markdown(from_key: str, to_key: str) -> str:
    before, after = PRODUCTS[from_key], PRODUCTS[to_key]
    before_topics, after_topics = topic_map(before), topic_map(after)
    before_paths, after_paths = set(before_topics), set(after_topics)
    shared = sorted(before_paths & after_paths)
    unchanged = [path for path in shared if before_topics[path]["digest"] == after_topics[path]["digest"]]
    changed = [path for path in shared if before_topics[path]["digest"] != after_topics[path]["digest"]]
    added, removed = sorted(after_paths - before_paths), sorted(before_paths - after_paths)

    lines = [
        f"# {before['title']} {before['version']} to {after['version']} Comparison",
        "",
        "> Generated from normalized Markdown bodies. This is a retrieval aid, not a semantic release changelog.",
        "",
        "## Retrieval policy",
        "",
        f"- Use **{after['version']}** for unversioned Detect questions: [current catalog]({after['index_file']}).",
        f"- Use **{before['version']}** only when that installed version is named or when comparing behavior: [historical catalog]({before['index_file']}).",
        f"- Start release-change questions with the {after['version']} release notes, then use the changed-topic list below for detail.",
        "",
        "## Snapshot summary",
        "",
        "| Category | Topics |",
        "|----------|-------:|",
        f"| Unchanged bodies | {len(unchanged)} |",
        f"| Changed bodies | {len(changed)} |",
        f"| Added in {after['version']} | {len(added)} |",
        f"| Removed after {before['version']} | {len(removed)} |",
        "",
        "## Changed or added topics",
        "",
        "| Logical path | Earlier snapshot | Later snapshot |",
        "|--------------|------------------|----------------|",
    ]
    for path in changed:
        lines.append(f"| `{path}` | {link(before_topics[path])} | {link(after_topics[path])} |")
    for path in added:
        lines.append(f"| `{path}` | — | {link(after_topics[path])} |")
    if removed:
        lines.extend(["", "## Removed topics", "", "| Logical path | Earlier snapshot |", "|--------------|------------------|"])
        for path in removed:
            lines.append(f"| `{path}` | {link(before_topics[path])} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="from_key", required=True, choices=PRODUCTS)
    parser.add_argument("--to", dest="to_key", required=True, choices=PRODUCTS)
    parser.add_argument("--output", required=True, help="Output Markdown path relative to the corpus root")
    args = parser.parse_args()
    before, after = PRODUCTS[args.from_key], PRODUCTS[args.to_key]
    if before.get("product") != after.get("product"):
        parser.error("both product keys must represent the same product")
    output = ROOT / args.output
    changed = write_text_if_changed(output, build_markdown(args.from_key, args.to_key))
    print(f"{'Wrote' if changed else 'Unchanged'} {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
