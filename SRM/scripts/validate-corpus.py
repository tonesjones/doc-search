#!/usr/bin/env python3
"""Validate SCA manifests, generated indexes, and scraped topic metadata.

This is intentionally read-only by default.  It reports unreferenced Markdown
files but never deletes or rewrites them.  Legacy topic files that predate hash
tracking are warned about, while a partially recorded or incorrect hash fails.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from corpus_utils import content_hash, markdown_body
from products import DEFAULT_PRODUCT_KEY, PRODUCTS, product_paths, validate_registry

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FRONT_MATTER = ("title", "source_url", "content_id", "version", "section", "scraped_at")
VALID_STATUSES = {"pending", "done", "skipped", "error"}
NON_TOPIC_DOC_PATTERNS = ("docs/api/openapi-snapshot-*.md",)


def filesystem_path(path: Path) -> Path:
    """Use the extended-length form for deep Windows corpus paths."""
    if sys.platform == "win32":
        absolute = str(path.resolve())
        if not absolute.startswith("\\\\?\\"):
            return Path("\\\\?\\" + absolute)
    return path


@dataclass
class ValidationResult:
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    legacy_hashes: int = 0


def parse_front_matter(text: str) -> tuple[dict[str, str] | None, str | None]:
    body = markdown_body(text)
    if body is None:
        return None, None
    block = text[4:].partition("\n---\n")[0]
    meta: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body


def computed_stats(topics: list[dict[str, Any]]) -> dict[str, int]:
    stats = {"total": len(topics), "pending": 0, "done": 0, "skipped": 0, "error": 0}
    for topic in topics:
        status = topic.get("status") or "pending"
        if status in VALID_STATUSES:
            stats[status] += 1
    return stats


def validate_product(root: Path, cfg: dict[str, Any], result: ValidationResult) -> set[Path]:
    paths = product_paths(cfg, root)
    key = cfg["key"]
    manifest_path = paths["manifest_path"]
    expected_docs: set[Path] = set()
    if not manifest_path.is_file():
        result.failures.append(f"[{key}] missing manifest: {manifest_path.relative_to(root)}")
        return expected_docs
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"[{key}] unreadable manifest: {exc}")
        return expected_docs

    for manifest_field, expected in (("productKey", key), ("mapId", cfg["map_id"]), ("version", cfg["version"])):
        if manifest.get(manifest_field) != expected:
            result.failures.append(f"[{key}] {manifest_field} mismatch: {manifest.get(manifest_field)!r} != {expected!r}")
    topics = manifest.get("topics")
    if not isinstance(topics, list):
        result.failures.append(f"[{key}] manifest topics is not a list")
        return expected_docs
    actual_stats = computed_stats(topics)
    if manifest.get("stats") != actual_stats:
        result.failures.append(f"[{key}] stats mismatch: manifest={manifest.get('stats')} actual={actual_stats}")

    index_path = paths["index_path"]
    index_text = ""
    if not index_path.is_file():
        result.failures.append(f"[{key}] missing index: {index_path.relative_to(root)}")
    else:
        index_text = index_path.read_text(encoding="utf-8")
        if f"{actual_stats['done']}/{actual_stats['total']} done" not in index_text:
            result.failures.append(f"[{key}] index progress does not match manifest")

    local_paths: dict[str, str] = {}
    for topic in topics:
        status = topic.get("status") or "pending"
        local = str(topic.get("localPath") or "").replace("\\", "/")
        topic_id = str(topic.get("id") or "")
        if status not in VALID_STATUSES:
            result.failures.append(f"[{key}] invalid status {status!r}: {local or topic_id}")
            continue
        if not local or not topic_id:
            result.failures.append(f"[{key}] missing id or localPath: {topic.get('title')!r}")
            continue
        prior_id = local_paths.get(local)
        if prior_id and prior_id != topic_id:
            result.failures.append(f"[{key}] duplicate localPath for {prior_id} and {topic_id}: {local}")
        else:
            local_paths[local] = topic_id
        path = root / local
        expected_docs.add(path.resolve())
        if index_text and f"]({local})" not in index_text:
            result.failures.append(f"[{key}] index link missing: {local}")
        if status != "done":
            continue
        disk_path = filesystem_path(path)
        if not disk_path.is_file():
            result.failures.append(f"[{key}] done file missing: {local}")
            continue
        text = disk_path.read_text(encoding="utf-8")
        meta, body = parse_front_matter(text)
        if meta is None or body is None:
            result.failures.append(f"[{key}] invalid or missing front matter: {local}")
            continue
        missing = [name for name in REQUIRED_FRONT_MATTER if not meta.get(name)]
        if missing:
            result.failures.append(f"[{key}] missing front matter ({', '.join(missing)}): {local}")
        if not body.strip():
            result.failures.append(f"[{key}] empty body: {local}")
        for name, expected in (("content_id", topic_id), ("version", str(manifest["version"])), ("section", str(topic.get("section") or "")), ("source_url", str(topic.get("sourceUrl") or ""))):
            if meta.get(name) != expected:
                result.failures.append(f"[{key}] {name} mismatch: {local}")
        front_hash = meta.get("content_hash")
        manifest_hash = topic.get("contentHash")
        if bool(front_hash) != bool(manifest_hash):
            result.failures.append(f"[{key}] partial content hash metadata: {local}")
        elif front_hash:
            actual_hash = content_hash(body)
            if front_hash != manifest_hash or front_hash != actual_hash:
                result.failures.append(f"[{key}] content hash mismatch: {local}")
        else:
            result.legacy_hashes += 1
    return expected_docs


def validate_corpus(root: Path = ROOT, products: dict[str, dict[str, Any]] = PRODUCTS) -> ValidationResult:
    result = ValidationResult()
    try:
        validate_registry(products)
    except ValueError as exc:
        result.failures.append(f"product registry: {exc}")
        return result
    expected_docs: set[Path] = set()
    initialized: list[dict[str, Any]] = []
    for cfg in products.values():
        manifest_exists = product_paths(cfg, root)["manifest_path"].is_file()
        if manifest_exists:
            initialized.append(cfg)
        elif cfg.get("optional"):
            result.warnings.append(f"[{cfg['key']}] optional product is not initialized")
            continue
        expected_docs.update(validate_product(root, cfg, result))

    hub = root / "corpus-status.md"
    if not hub.is_file():
        result.failures.append("missing corpus-status.md")
    else:
        hub_text = hub.read_text(encoding="utf-8")
        for cfg in initialized:
            link = f"[{cfg['index_file']}]({cfg['index_file']})"
            if link not in hub_text:
                result.failures.append(f"[hub] product index link missing: {cfg['index_file']}")

    docs_root = root / "docs"
    if docs_root.is_dir():
        for path in docs_root.rglob("*.md"):
            relative = path.relative_to(root)
            if any(relative.match(pattern) for pattern in NON_TOPIC_DOC_PATTERNS):
                continue
            if path.resolve() not in expected_docs:
                result.warnings.append(f"orphan Markdown (not deleted): {relative.as_posix()}")
    if result.legacy_hashes:
        result.warnings.append(
            f"{result.legacy_hashes} legacy done topic(s) predate content-hash tracking; "
            "new or refreshed topics require both hashes."
        )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Black Duck SCA corpus without modifying it")
    parser.add_argument("--product", default="all", help="Validate one registered product or all (default)")
    parser.add_argument("--fail-on-orphans", action="store_true", help="Treat reported orphan Markdown files as failures")
    args = parser.parse_args()
    selected = PRODUCTS if args.product == "all" else {args.product: PRODUCTS[args.product]}
    result = validate_corpus(ROOT, selected)
    if args.fail_on_orphans:
        result.failures.extend(warning for warning in result.warnings if warning.startswith("orphan Markdown"))
    for warning in result.warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if result.failures:
        print("Corpus validation failed:", *result.failures, sep="\n", file=sys.stderr)
        return 1
    print(f"Corpus validation passed ({len(selected)} product(s); {result.legacy_hashes} legacy hash record(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
