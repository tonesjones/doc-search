#!/usr/bin/env python3
"""Validate Coverity topic files, metadata, and stored content hashes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from corpus_utils import atomic_write_text, content_hash, markdown_body
from products import DEFAULT_PRODUCT_KEY, get_product, product_paths

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = ("title:", "source_url:", "content_id:", "version:", "section:", "scraped_at:")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Coverity corpus files and manifest metadata")
    parser.add_argument("--product", default=DEFAULT_PRODUCT_KEY)
    parser.add_argument(
        "--backfill-hashes",
        action="store_true",
        help="Store hashes for already-scraped files that predate contentHash tracking",
    )
    args = parser.parse_args()

    cfg = get_product(args.product)
    manifest_path = product_paths(cfg, ROOT)["manifest_path"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures: list[str] = []
    backfilled = 0

    for topic in manifest.get("topics", []):
        if topic.get("status") != "done":
            continue
        local = topic.get("localPath") or ""
        path = ROOT / local
        if not path.is_file():
            failures.append(f"missing file: {local}")
            continue
        text = path.read_text(encoding="utf-8")
        missing = [field for field in REQUIRED_FIELDS if field not in text[:2000]]
        if missing:
            failures.append(f"missing metadata ({', '.join(missing)}): {local}")
            continue
        body = markdown_body(text)
        if body is None:
            failures.append(f"invalid front matter: {local}")
            continue
        digest = content_hash(body)
        expected = topic.get("contentHash")
        if args.backfill_hashes and expected != digest:
            topic["contentHash"] = digest
            backfilled += 1
        elif expected != digest:
            failures.append(f"content hash mismatch: {local}")

    if args.backfill_hashes and backfilled:
        atomic_write_text(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    if failures:
        print("Corpus validation failed:", *failures, sep="\n", file=sys.stderr)
        return 1
    print(
        f"[{cfg['key']}] Corpus validation passed "
        f"({manifest.get('stats', {}).get('done', 0)} done topics; {backfilled} hashes backfilled)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
