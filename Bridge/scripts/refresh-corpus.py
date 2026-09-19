#!/usr/bin/env python3
"""Safely refresh one or more already-initialized SCA documentation maps.

The wrapper deliberately never deletes files, commits, or pushes.  It refuses
to overwrite generated files that were already dirty before the run, and it
ends with the read-only corpus validator.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from products import PRODUCTS, product_paths, validate_registry

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent


def git_status() -> dict[str, str]:
    completed = subprocess.run(
        ["git", "status", "--porcelain", "--", ROOT.name], cwd=REPO_ROOT,
        text=True, capture_output=True, check=False,
    )
    if completed.returncode:
        return {}
    return {line[3:].replace("\\", "/"): line[:2] for line in completed.stdout.splitlines() if len(line) >= 4}


def protected_dirty_paths(status: dict[str, str]) -> list[str]:
    protected: list[str] = []
    for path in status:
        relative = path.split("/", 1)[-1] if "/" in path else path
        if relative == "corpus-status.md" or relative.startswith("index") and relative.endswith(".md"):
            protected.append(path)
        elif relative.startswith("sources/") and relative.endswith(("/manifest.json", "/toc.json")):
            protected.append(path)
    return sorted(protected)


def command(label: str, args: list[str], dry_run: bool) -> int:
    rendered = " ".join(args)
    print(f"{label}: {rendered}")
    if dry_run:
        return 0
    completed = subprocess.run(args, cwd=ROOT, check=False)
    return completed.returncode


def existing_products() -> list[str]:
    return [key for key, cfg in PRODUCTS.items() if product_paths(cfg, ROOT)["manifest_path"].is_file()]


def describe_work(keys: list[str]) -> None:
    for key in keys:
        manifest_path = product_paths(PRODUCTS[key], ROOT)["manifest_path"]
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        stats = manifest.get("stats") or {}
        print(f"[{key}] preview: {stats.get('pending', 0)} pending, {stats.get('error', 0)} error, {stats.get('done', 0)} done")


def print_scoped_summary(before: dict[str, str]) -> None:
    after = git_status()
    changed = sorted(path for path, state in after.items() if before.get(path) != state)
    print("Scoped Git summary (no commit or push was performed):")
    if changed:
        for path in changed:
            print(f"  {after[path]} {path}")
    else:
        print("  no new working-tree changes")


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh initialized Black Duck SCA corpora safely")
    parser.add_argument("--product", default="all", help="Registered product key, or all initialized products")
    parser.add_argument("--content-check", action="store_true", help="Opt in to network checks of every done topic; only changed pages are rewritten")
    parser.add_argument("--dry-run", action="store_true", help="Preview selected work and commands without network calls or writes")
    args = parser.parse_args()
    validate_registry()
    keys = existing_products() if args.product == "all" else [args.product]
    unknown = [key for key in keys if key not in PRODUCTS]
    if unknown:
        parser.error(f"Unknown product(s): {', '.join(unknown)}")
    before = git_status()
    dirty = protected_dirty_paths(before)
    if dirty and not args.dry_run:
        print("Refusing to overwrite pre-existing generated-file changes:", *dirty, sep="\n", file=sys.stderr)
        print("Use a clean/staged generated corpus before a real refresh; dry-run remains safe.", file=sys.stderr)
        return 2
    describe_work(keys)
    if args.dry_run:
        for key in keys:
            command("would refresh TOC", [sys.executable, "scripts/build-index.py", "--product", key, "--refresh-toc"], True)
            command("would scrape pending", [sys.executable, "scripts/scrape-pending.py", "--product", key, "--all-pending"], True)
            command("would retry errors", [sys.executable, "scripts/scrape-pending.py", "--product", key, "--retry-errors"], True)
            if args.content_check:
                command("would check done content", [sys.executable, "scripts/scrape-pending.py", "--product", key, "--refresh-changed"], True)
        for index, key in enumerate(keys):
            rebuild = [sys.executable, "scripts/build-index.py", "--product", key]
            if index == len(keys) - 1:
                rebuild.append("--hub")
            command("would rebuild hub/index", rebuild, True)
        command("would validate", [sys.executable, "scripts/validate-corpus.py", "--product", "all"], True)
        print_scoped_summary(before)
        return 0

    for key in keys:
        for label, cmd in (
            ("refresh TOC", [sys.executable, "scripts/build-index.py", "--product", key, "--refresh-toc"]),
            ("scrape pending", [sys.executable, "scripts/scrape-pending.py", "--product", key, "--all-pending"]),
            ("retry errors", [sys.executable, "scripts/scrape-pending.py", "--product", key, "--retry-errors"]),
        ):
            if command(label, cmd, False):
                print_scoped_summary(before)
                return 1
        if args.content_check and command("check done content", [sys.executable, "scripts/scrape-pending.py", "--product", key, "--refresh-changed"], False):
            print_scoped_summary(before)
            return 1
    for index, key in enumerate(keys):
        rebuild = [sys.executable, "scripts/build-index.py", "--product", key]
        if index == len(keys) - 1:
            rebuild.append("--hub")
        if command("rebuild hub/index", rebuild, False):
            print_scoped_summary(before)
            return 1
    rc = command("validate", [sys.executable, "scripts/validate-corpus.py", "--product", "all"], False)
    print_scoped_summary(before)
    return 0 if rc == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
