#!/usr/bin/env python3
"""Scrape pending Signal doc topics via Fluid Topics content API.

Examples:
  python scripts/scrape-pending.py --product signal-latest --all-pending
  python scripts/scrape-pending.py --section "Overview of Black Duck Signal" --all-pending
  python scripts/scrape-pending.py --section "Scan your code changes"
  python scripts/scrape-pending.py --path-contains "Claude Code" --limit 20
  python scripts/scrape-pending.py --retry-errors
  python scripts/scrape-pending.py --refresh-changed --limit 100
  python scripts/scrape-pending.py --repair-empty
  python scripts/scrape-pending.py --list-products
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md

from corpus_utils import atomic_write_text, content_hash, markdown_body

from products import (
    DEFAULT_PRODUCT_KEY,
    PRODUCTS,
    content_url,
    get_product,
    product_paths,
)

ROOT = Path(__file__).resolve().parents[1]


def win_long_path(path: Path) -> Path:
    """Return a Path usable for open/mkdir on Windows when >260 chars."""
    path = path if path.is_absolute() else (ROOT / path)
    # resolve() can fail if parents missing; build absolute manually
    try:
        abs_path = path.resolve()
    except OSError:
        abs_path = path if path.is_absolute() else ROOT / path
        abs_path = Path(os.path.abspath(str(abs_path)))
    if os.name != "nt":
        return abs_path
    s = str(abs_path)
    if s.startswith("\\\\?\\"):
        return Path(s)
    # Extended-length path prefix
    if s.startswith("\\\\"):
        # UNC: \\server\share -> \\?\UNC\server\share
        return Path("\\\\?\\UNC\\" + s[2:])
    return Path("\\\\?\\" + s)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_manifest(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_manifest(manifest: dict, path: Path) -> None:
    stats = {"total": len(manifest["topics"]), "pending": 0, "done": 0, "skipped": 0, "error": 0}
    for t in manifest["topics"]:
        st = t.get("status") or "pending"
        if st not in stats:
            st = "pending"
        stats[st] = stats.get(st, 0) + 1
    for k in ("pending", "done", "skipped", "error"):
        stats.setdefault(k, 0)
    manifest["stats"] = stats
    manifest["scrapedAt"] = now_iso()
    atomic_write_text(path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def path_joined(topic: dict) -> str:
    return " > ".join(topic.get("path") or [])


PLACEHOLDER = "_(No extractable content.)_"


def posix_relpath(from_file: str, to_file: str) -> str:
    start = os.path.dirname(from_file.replace("\\", "/")) or "."
    return os.path.relpath(to_file.replace("\\", "/"), start).replace("\\", "/")


def index_direct_children(topics: list[dict]) -> dict[tuple, list[dict]]:
    by_parent: dict[tuple, list[dict]] = {}
    for topic in topics:
        path = tuple(topic.get("path") or [])
        if len(path) < 2:
            continue
        by_parent.setdefault(path[:-1], []).append(topic)
    return by_parent


def markdown_is_placeholder(text: str) -> bool:
    if not text or not text.strip():
        return True
    stripped = re.sub(r"^#\s+.+\n*", "", text.strip(), count=1).strip()
    return stripped in {"", PLACEHOLDER}


def child_index_markdown(topic: dict, children: list[dict]) -> str:
    title = topic.get("title") or "Untitled"
    lines = [
        f"# {title}",
        "",
        "This official topic has no body of its own. Topics in this section:",
        "",
    ]
    parent_path = topic.get("localPath") or ""
    for child in children:
        name = child.get("title") or "untitled"
        child_path = child.get("localPath") or ""
        if parent_path and child_path:
            lines.append(f"- [{name}]({posix_relpath(parent_path, child_path)})")
        else:
            lines.append(f"- {name}")
    return "\n".join(lines)


def empty_leaf_markdown(topic: dict) -> str:
    title = topic.get("title") or "Untitled"
    return (
        f"# {title}\n\n"
        "This official topic has no extractable body in Black Duck Signal."
    )


def fill_empty_topic(
    topic: dict, body: str, children_index: dict[tuple, list[dict]]
) -> str:
    if not markdown_is_placeholder(body):
        return body
    children = children_index.get(tuple(topic.get("path") or []), [])
    if children:
        return child_index_markdown(topic, children)
    return empty_leaf_markdown(topic)


def hash_written_topic(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    body = markdown_body(text)
    if body is None:
        raise ValueError(f"invalid front matter after write: {path}")
    return content_hash(body)


def file_has_placeholder(path: Path) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    body = markdown_body(text)
    return markdown_is_placeholder(body or "")


def select_topics(manifest: dict, args: argparse.Namespace) -> list[dict]:
    if args.refresh_changed:
        statuses = {"done"}
    elif args.all_pending:
        statuses = {"pending"}
    elif args.retry_errors and args.include_pending:
        statuses = {"pending", "error"}
    elif args.retry_errors:
        statuses = {"error"}
    else:
        statuses = {"pending"}

    excludes = [e for e in (args.exclude_path or []) if e]
    out: list[dict] = []
    for t in manifest["topics"]:
        if t.get("status") not in statuses:
            continue
        joined = path_joined(t)
        if args.section and t.get("section") != args.section:
            continue
        if args.path_contains and args.path_contains not in joined:
            continue
        if excludes and any(ex in joined for ex in excludes):
            continue
        out.append(t)
        if args.limit and len(out) >= args.limit:
            break
    return out


def fetch_html(cfg: dict, content_id: str, timeout: int = 60) -> str:
    url = content_url(cfg, content_id)
    req = urllib.request.Request(url, headers={"Accept": "text/html, application/json, */*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def clean_html(html: str) -> BeautifulSoup:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    for img in soup.find_all("img"):
        src = img.get("src") or ""
        alt = img.get("alt") or "image"
        if src.startswith("data:"):
            img.replace_with(soup.new_string(f" [image: {alt}] "))
        elif src and not src.startswith("http"):
            img.replace_with(soup.new_string(f" [image: {alt}] "))
    return soup


def html_to_markdown(html: str, title: str) -> str:
    soup = clean_html(html)
    body = soup.body or soup
    main = body.find(class_=re.compile(r"content-locale|body|topic", re.I)) or body
    text = md(
        str(main),
        heading_style="ATX",
        bullets="-",
        strip=["span"],
        escape_asterisks=False,
        escape_underscores=False,
    )
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not text:
        text = "_(No extractable content.)_"
    if not re.match(r"^#\s+", text):
        text = f"# {title}\n\n{text}"
    return text


def write_topic_md(topic: dict, body_md: str, scraped_at: str, version: str) -> Path:
    rel = topic["localPath"]
    path = ROOT / rel
    out = win_long_path(path)
    out.parent.mkdir(parents=True, exist_ok=True)

    def yq(s: str) -> str:
        return (s or "").replace('"', '\\"')

    fm = "\n".join(
        [
            "---",
            f'title: "{yq(topic.get("title") or "")}"',
            f'source_url: "{yq(topic.get("sourceUrl") or "")}"',
            f'content_id: "{yq(topic.get("id") or "")}"',
            f'version: "{yq(version)}"',
            f'section: "{yq(topic.get("section") or "")}"',
            f'scraped_at: "{scraped_at}"',
            "---",
            "",
            body_md,
            "",
        ]
    )
    atomic_write_text(out, fm)
    # Return logical relative path object for size/reporting
    return path


def select_empty_topics(manifest: dict, args: argparse.Namespace) -> list[dict]:
    excludes = [e for e in (args.exclude_path or []) if e]
    out: list[dict] = []
    for topic in manifest["topics"]:
        if topic.get("status") != "done":
            continue
        joined = path_joined(topic)
        if args.section and topic.get("section") != args.section:
            continue
        if args.path_contains and args.path_contains not in joined:
            continue
        if excludes and any(ex in joined for ex in excludes):
            continue
        local = topic.get("localPath") or ""
        if not file_has_placeholder(ROOT / local):
            continue
        out.append(topic)
        if args.limit and len(out) >= args.limit:
            break
    return out


def repair_empty_topics(
    cfg: dict,
    args: argparse.Namespace,
    manifest: dict,
    manifest_path: Path,
    children_index: dict[tuple, list[dict]],
) -> int:
    topics = select_empty_topics(manifest, args)
    print(f"[{cfg['key']}] Selected {len(topics)} empty topics to repair")
    if args.dry_run:
        for topic in topics:
            kids = children_index.get(tuple(topic.get("path") or []), [])
            kind = f"child-index ({len(kids)})" if kids else "empty-leaf"
            print(f"  {kind:22} {topic['localPath']}")
        return 0
    if not topics:
        print(f"[{cfg['key']}] Nothing to repair.")
        return 0

    version = manifest.get("version") or cfg["version"]
    repaired = 0
    for i, topic in enumerate(topics, 1):
        title = topic.get("title")
        print(f"[{cfg['key']}] [{i}/{len(topics)}] {title} ({topic.get('id')})")
        body = fill_empty_topic(topic, PLACEHOLDER, children_index)
        scraped_at = now_iso()
        path = write_topic_md(topic, body, scraped_at, version)
        written = win_long_path(path)
        topic["status"] = "done"
        topic["error"] = None
        topic["scrapedAt"] = scraped_at
        topic["lastCheckedAt"] = scraped_at
        topic["contentHash"] = hash_written_topic(written)
        topic["bytes"] = written.stat().st_size
        repaired += 1
        kind = "child-index" if "Topics in this section:" in body else "empty-leaf"
        print(f"  -> {kind} {path.relative_to(ROOT)} ({topic['bytes']} bytes)")
        save_manifest(manifest, manifest_path)

    save_manifest(manifest, manifest_path)
    print(f"[{cfg['key']}] Repaired {repaired} empty topics; stats={manifest['stats']}")
    return 0


def scrape_product(cfg: dict, args: argparse.Namespace) -> int:
    paths = product_paths(cfg, ROOT)
    manifest_path = paths["manifest_path"]
    if not manifest_path.exists():
        print(
            f"[{cfg['key']}] No manifest at {manifest_path}. "
            f"Run: python scripts/build-index.py --product {cfg['key']} --init"
        )
        return 2

    manifest = load_manifest(manifest_path)
    children_index = index_direct_children(manifest["topics"])

    if args.repair_empty:
        return repair_empty_topics(cfg, args, manifest, manifest_path, children_index)

    topics = select_topics(manifest, args)
    print(f"[{cfg['key']}] Selected {len(topics)} topics")
    if args.dry_run:
        for t in topics:
            print(f"  {t['status']:7} {t['localPath']}")
        return 0

    if not topics:
        print(f"[{cfg['key']}] Nothing to scrape.")
        return 0

    done = 0
    unchanged = 0
    errors = 0
    version = manifest.get("version") or cfg["version"]
    for i, topic in enumerate(topics, 1):
        cid = topic.get("id")
        title = topic.get("title")
        print(f"[{cfg['key']}] [{i}/{len(topics)}] {title} ({cid})")
        try:
            html = fetch_html(cfg, cid)
            body = fill_empty_topic(
                topic, html_to_markdown(html, title or "Untitled"), children_index
            )
            scraped_at = now_iso()
            digest = content_hash("\n" + body)
            if args.refresh_changed and topic.get("contentHash") == digest:
                topic["lastCheckedAt"] = scraped_at
                unchanged += 1
                print("  -> unchanged")
                save_manifest(manifest, manifest_path)
                time.sleep(args.delay)
                continue
            path = write_topic_md(topic, body, scraped_at, version)
            topic["status"] = "done"
            topic["error"] = None
            topic["scrapedAt"] = scraped_at
            topic["lastCheckedAt"] = scraped_at
            topic["contentHash"] = hash_written_topic(win_long_path(path))
            topic["bytes"] = win_long_path(path).stat().st_size
            done += 1
            print(f"  -> {path.relative_to(ROOT)} ({topic['bytes']} bytes)")
        except urllib.error.HTTPError as e:
            topic["status"] = "error"
            topic["error"] = f"HTTP {e.code}: {e.reason}"
            errors += 1
            print(f"  !! {topic['error']}")
            if e.code == 429:
                print("  rate limited; sleeping 10s")
                time.sleep(10)
        except Exception as e:
            topic["status"] = "error"
            topic["error"] = str(e)
            errors += 1
            print(f"  !! {e}")
        # Persist every result so a stopped batch loses no more than the active request.
        save_manifest(manifest, manifest_path)
        time.sleep(args.delay)

    save_manifest(manifest, manifest_path)
    print(
        f"[{cfg['key']}] Finished: {done} updated, {unchanged} unchanged, "
        f"{errors} error; stats={manifest['stats']}"
    )
    return 0 if errors == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape pending Signal topics")
    parser.add_argument(
        "--product",
        type=str,
        default=DEFAULT_PRODUCT_KEY,
        help=f"Product key (default: {DEFAULT_PRODUCT_KEY})",
    )
    parser.add_argument(
        "--all-pending",
        action="store_true",
        help="Scrape every selected topic with status pending",
    )
    parser.add_argument("--section", type=str, default=None, help="TOC root section title")
    parser.add_argument(
        "--path-contains",
        type=str,
        default=None,
        help="Only topics whose path string contains this text",
    )
    parser.add_argument(
        "--exclude-path",
        action="append",
        default=[],
        help="Skip topics whose path contains this text (repeatable)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Maximum selected topics; use 100 for resumable, timeout-safe batches (0 = no limit)",
    )
    parser.add_argument("--delay", type=float, default=0.35, help="Seconds between requests")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument(
        "--refresh-changed",
        action="store_true",
        help="Re-fetch completed topics and rewrite only whose normalized Markdown hash changed",
    )
    parser.add_argument(
        "--include-pending",
        action="store_true",
        help="With --retry-errors also do pending",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--list-products", action="store_true")
    parser.add_argument(
        "--repair-empty",
        action="store_true",
        help="Rewrite done topics whose official body was empty (child index or empty-leaf note)",
    )
    args = parser.parse_args()

    if args.list_products:
        for key, cfg in PRODUCTS.items():
            opt = " (optional)" if cfg.get("optional") else ""
            print(f"{key:20} {cfg['title']}{opt}")
        return 0

    if not any(
        [
            args.all_pending,
            args.section,
            args.path_contains,
            args.retry_errors,
            args.refresh_changed,
            args.repair_empty,
        ]
    ):
        parser.error(
            "Specify --all-pending, --section, --path-contains, --retry-errors, "
            "--refresh-changed, and/or --repair-empty"
        )

    # Section/path filters imply pending scrape unless retry-errors only
    if (
        (args.section or args.path_contains or args.exclude_path)
        and not args.retry_errors
        and not args.refresh_changed
    ):
        args.all_pending = True

    cfg = get_product(args.product)
    return scrape_product(cfg, args)


if __name__ == "__main__":
    raise SystemExit(main())
