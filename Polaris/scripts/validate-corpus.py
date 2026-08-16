#!/usr/bin/env python3
"""Validate that Polaris manifests, topic metadata, and indexes agree."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from products import PRODUCTS, paths

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = (
    "title",
    "source_url",
    "content_id",
    "product_key",
    "section",
    "scraped_at",
    "content_hash",
)


def front_matter(text: str) -> tuple[dict[str, str] | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    meta: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, parts[2]


def stats(topics: list[dict]) -> dict[str, int]:
    out = {"total": len(topics), "pending": 0, "done": 0, "skipped": 0, "error": 0}
    for item in topics:
        out[item.get("status") if item.get("status") in out else "pending"] += 1
    return out


def validate() -> list[str]:
    failures: list[str] = []
    if not (ROOT / "index.md").exists():
        failures.append("missing index.md")
    if not (ROOT / "corpus-status.md").exists():
        failures.append("missing corpus-status.md")
    for cfg in PRODUCTS.values():
        product_paths = paths(cfg, ROOT)
        if not product_paths["manifest"].exists():
            print(f"[{cfg['key']}] not initialized")
            continue
        manifest = json.loads(product_paths["manifest"].read_text(encoding="utf-8"))
        topics = manifest.get("topics", [])
        actual = stats(topics)
        if actual != manifest.get("stats"):
            failures.append(f"[{cfg['key']}] stats mismatch: manifest={manifest.get('stats')} actual={actual}")
        if not product_paths["index"].exists():
            failures.append(f"missing index: {product_paths['index']}")
        else:
            index_text = product_paths["index"].read_text(encoding="utf-8")
            if f"{actual['done']}/{actual['total']} done" not in index_text:
                failures.append(f"[{cfg['key']}] index progress does not match manifest")
        for topic in topics:
            if topic.get("status") != "done":
                continue
            file = ROOT / topic["localPath"]
            if not file.exists():
                failures.append(f"missing: {file}")
                continue
            content = file.read_text(encoding="utf-8")
            meta, body = front_matter(content)
            if meta is None:
                failures.append(f"front matter missing: {file}")
                continue
            for field in REQUIRED_FIELDS:
                if not meta.get(field):
                    failures.append(f"metadata {field} missing: {file}")
            digest = meta.get("content_hash")
            if digest and topic.get("contentHash") and digest != topic["contentHash"]:
                failures.append(f"content_hash mismatch: {file}")
            if re.search(r"_\(No extractable content\.\)_", body):
                failures.append(f"empty body: {file}")
            if file.name == "roles-and-permissions.md":
                if not re.search(r"\|\s*Yes\s*\|", body) or not re.search(r"\|\s*No\s*\|", body):
                    failures.append(f"roles table missing Yes/No marks: {file}")
                if "[image: image]" in body:
                    failures.append(f"roles table still has unlabeled icons: {file}")
    return failures


def main() -> int:
    failures = validate()
    print("Corpus validation passed." if not failures else "\n".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
