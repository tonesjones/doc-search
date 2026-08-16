#!/usr/bin/env python3
"""Scrape pending Black Duck doc topics via Fluid Topics content API.

Examples:
  python scripts/scrape-pending.py --product detect-11.5.1 --all-pending
  python scripts/scrape-pending.py --product alert-8.4.0 --all-pending
  python scripts/scrape-pending.py --batch-a
  python scripts/scrape-pending.py --section "Black Duck SCA Help Center" --limit 20
  python scripts/scrape-pending.py --retry-errors
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

BATCH_A_PREFIXES = (
    "Welcome to Black Duck SCA",
    "Getting started with Black Duck SCA",
    "Scanning Your Code",
)


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
    path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def is_batch_a(topic: dict) -> bool:
    if topic.get("section") != "Black Duck SCA Help Center":
        return False
    path = topic.get("path") or []
    if len(path) < 2:
        return False
    return path[1] in BATCH_A_PREFIXES


def select_topics(manifest: dict, args: argparse.Namespace) -> list[dict]:
    if args.all_pending:
        statuses = {"pending"}
    elif args.retry_errors and args.include_pending:
        statuses = {"pending", "error"}
    elif args.retry_errors:
        statuses = {"error"}
    else:
        statuses = {"pending"}

    out: list[dict] = []
    for t in manifest["topics"]:
        if t.get("status") not in statuses:
            continue
        if args.batch_a and not is_batch_a(t):
            continue
        if not args.all_pending:
            if args.section and t.get("section") != args.section:
                continue
            if args.path_contains:
                joined = " > ".join(t.get("path") or [])
                if args.path_contains not in joined:
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
    out.write_text(fm, encoding="utf-8")
    # Return logical relative path object for size/reporting
    return path


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
    errors = 0
    version = manifest.get("version") or cfg["version"]
    for i, topic in enumerate(topics, 1):
        cid = topic.get("id")
        title = topic.get("title")
        print(f"[{cfg['key']}] [{i}/{len(topics)}] {title} ({cid})")
        try:
            html = fetch_html(cfg, cid)
            body = html_to_markdown(html, title or "Untitled")
            scraped_at = now_iso()
            path = write_topic_md(topic, body, scraped_at, version)
            topic["status"] = "done"
            topic["error"] = None
            topic["scrapedAt"] = scraped_at
            topic["bytes"] = path.stat().st_size
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
        if i % 5 == 0 or i == len(topics):
            save_manifest(manifest, manifest_path)
        time.sleep(args.delay)

    save_manifest(manifest, manifest_path)
    print(
        f"[{cfg['key']}] Finished: {done} done, {errors} error; stats={manifest['stats']}"
    )
    return 0 if errors == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape pending Black Duck topics")
    parser.add_argument(
        "--product",
        type=str,
        default=DEFAULT_PRODUCT_KEY,
        help=f"Product key (default: {DEFAULT_PRODUCT_KEY})",
    )
    parser.add_argument("--batch-a", action="store_true", help="Help Center intro + Scanning Your Code")
    parser.add_argument(
        "--all-pending",
        action="store_true",
        help="Scrape every topic with status pending (entire remaining corpus)",
    )
    parser.add_argument("--section", type=str, default=None)
    parser.add_argument("--path-contains", type=str, default=None)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--delay", type=float, default=0.35, help="Seconds between requests")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument("--include-pending", action="store_true", help="With --retry-errors also do pending")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--list-products", action="store_true")
    args = parser.parse_args()

    if args.list_products:
        for key, cfg in PRODUCTS.items():
            opt = " (optional)" if cfg.get("optional") else ""
            print(f"{key:20} {cfg['title']}{opt}")
        return 0

    if not any(
        [args.batch_a, args.all_pending, args.section, args.path_contains, args.retry_errors]
    ):
        parser.error(
            "Specify --all-pending, --batch-a, --section, --path-contains, and/or --retry-errors"
        )

    cfg = get_product(args.product)
    return scrape_product(cfg, args)


if __name__ == "__main__":
    raise SystemExit(main())
