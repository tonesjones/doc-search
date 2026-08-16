#!/usr/bin/env python3
"""Scrape selected Polaris manifest topics via the official Fluid Topics API."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

from products import DEFAULT_PRODUCT_KEY, PRODUCTS, content_url, get_product, paths

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "PolarisDocsCorpus/1.0"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(manifest: dict, path: Path) -> None:
    counts = {"total": len(manifest["topics"]), "pending": 0, "done": 0, "skipped": 0, "error": 0}
    for topic in manifest["topics"]:
        counts[topic.get("status") if topic.get("status") in counts else "pending"] += 1
    manifest["stats"] = counts
    manifest["lastScrapeAt"] = now()
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def quote(value: str | None) -> str:
    return (value or "").replace('"', '\\"')


def rel_link(from_local: str, to_local: str) -> str:
    src = (ROOT / from_local).parent
    dst = ROOT / to_local
    return Path(os.path.relpath(dst, src)).as_posix()


def unique_title_links(topic: dict, topics: list[dict]) -> list[tuple[str, str]]:
    grouped: dict[str, list[str]] = {}
    for item in topics:
        title = item.get("title") or ""
        path = item.get("localPath")
        if title and path:
            grouped.setdefault(title, []).append(path)
    links = []
    for title, locals_ in grouped.items():
        if len(locals_) != 1 or locals_[0] == topic.get("localPath"):
            continue
        links.append((title, rel_link(topic["localPath"], locals_[0])))
    links.sort(key=lambda item: len(item[0]), reverse=True)
    return links


def unique_url_map(topics: list[dict]) -> dict[str, str]:
    grouped: dict[str, set[str]] = {}
    for item in topics:
        local = item.get("localPath")
        if not local:
            continue
        for key in (item.get("prettyUrl"), item.get("sourceUrl")):
            if not key:
                continue
            grouped.setdefault(key, set()).add(local)
            if key.startswith("https://docs.blackduck.com"):
                grouped.setdefault(key.removeprefix("https://docs.blackduck.com"), set()).add(local)
            elif key.startswith("/"):
                grouped.setdefault("https://docs.blackduck.com" + key, set()).add(local)
    return {url: next(iter(paths_)) for url, paths_ in grouped.items() if len(paths_) == 1}


def icon_mark(stem: str) -> str | None:
    words = re.sub(r"[^a-z0-9]+", " ", stem.lower()).split()
    if any(word in {"check", "checkmark", "tick", "allowed"} for word in words):
        return "Yes"
    if any(word in {"forbidden", "deny", "denied", "disallowed"} for word in words):
        return "No"
    return None


def replace_image(image) -> None:
    alt = (image.get("alt") or "").strip()
    if alt and alt.lower() not in {"image", "img"}:
        image.replace_with(f" [image: {alt}] ")
        return
    name = (image.get("data-ft-asset-display-name") or "").strip()
    stem = Path(name).stem if name else ""
    mark = icon_mark(stem)
    if mark:
        image.replace_with(f" {mark} ")
        return
    if stem:
        image.replace_with(f" [image: {stem.replace('-', ' ').replace('_', ' ')}] ")
        return
    image.replace_with(" [image: image] ")


def rewrite_links(soup: BeautifulSoup, topic: dict, topics: list[dict]) -> None:
    by_url = unique_url_map(topics)
    for anchor in soup.find_all("a"):
        href = (anchor.get("href") or "").strip()
        if not href or href.startswith("#"):
            continue
        local = by_url.get(href)
        if local:
            anchor["href"] = rel_link(topic["localPath"], local)


def section_outline(topic: dict, topics: list[dict]) -> str | None:
    prefix = topic.get("path") or []
    depth = topic.get("depth") or len(prefix)
    children = [
        item
        for item in topics
        if (item.get("path") or [])[:depth] == prefix and (item.get("depth") or 0) == depth + 1
    ]
    if not children:
        return None
    lines = [f"# {topic['title']}", "", "This section includes:", ""]
    for child in children:
        lines.append(f"- [{child['title']}]({rel_link(topic['localPath'], child['localPath'])})")
    return "\n".join(lines)


def is_placeholder(text: str, title: str) -> bool:
    body = re.sub(rf"^#\s+{re.escape(title)}\s*", "", text.strip())
    return (not body) or body == "_(No extractable content.)_"


def link_see_also(text: str, topic: dict, topics: list[dict]) -> str:
    for title, href in unique_title_links(topic, topics):
        pattern = re.compile(rf"(?<!\[)(See|see) {re.escape(title)}(?!\])")
        text = pattern.sub(rf"\1 [{title}]({href})", text)
    return text


def markdown(html: str, topic: dict, topics: list[dict]) -> str:
    title = topic["title"]
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    for image in soup.find_all("img"):
        replace_image(image)
    rewrite_links(soup, topic, topics)
    body = soup.find(class_=re.compile(r"content-locale")) or soup.body or soup
    text = markdownify(str(body), heading_style="ATX", bullets="-").strip()
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if is_placeholder(text, title):
        text = section_outline(topic, topics) or f"# {title}\n\n_(No extractable content.)_"
    elif not re.match(r"^#\s", text):
        text = f"# {title}\n\n{text}"
    return link_see_also(text, topic, topics)


def write(topic: dict, body: str, cfg: dict, source_hash: str) -> tuple[str, Path, str]:
    path = ROOT / topic["localPath"]
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = now()
    front = "\n".join(
        [
            "---",
            f'title: "{quote(topic["title"])}"',
            f'source_url: "{quote(topic["sourceUrl"])}"',
            f'content_id: "{quote(topic["id"])}"',
            f'product_key: "{cfg["key"]}"',
            f'section: "{quote(topic["section"])}"',
            f'scraped_at: "{stamp}"',
            f'content_hash: "{source_hash}"',
            "---",
            "",
            body,
            "",
        ]
    )
    path.write_text(front, encoding="utf-8")
    return stamp, path, source_hash


def select(topics: list[dict], args: argparse.Namespace) -> list[dict]:
    allowed: set[str] = set()
    if args.all_pending:
        allowed.add("pending")
    if args.retry_errors:
        allowed.add("error")
    if args.refresh_changed or args.refresh_all:
        allowed.add("done")
    if (args.section or args.path_contains) and not allowed:
        allowed.add("pending")
    result = []
    for topic in topics:
        if topic.get("status") not in allowed:
            continue
        joined = " > ".join(topic.get("path", []))
        if args.section and topic.get("section") != args.section:
            continue
        if args.path_contains and args.path_contains.lower() not in joined.lower():
            continue
        result.append(topic)
        if args.limit and len(result) >= args.limit:
            break
    return result


def fetch_content(cfg: dict, content_id: str, attempts: int = 3) -> str:
    url = content_url(cfg, content_id)
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(
                url,
                headers={"Accept": "text/html, application/json", "User-Agent": USER_AGENT},
            )
            with urllib.request.urlopen(request, timeout=90) as response:
                raw = response.read().decode("utf-8", errors="replace")
            stripped = raw.lstrip()
            if stripped.startswith("{"):
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    return raw
                raw = data.get("content") or data.get("body") or data.get("html") or raw
            return raw
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise last or RuntimeError(f"failed to fetch {content_id}")


def scrape(cfg: dict, args: argparse.Namespace) -> None:
    product_paths = paths(cfg, ROOT)
    if not product_paths["manifest"].exists():
        raise RuntimeError("No manifest; run build-index.py --init first")
    manifest = load(product_paths["manifest"])
    chosen = select(manifest["topics"], args)
    print(f"[{cfg['key']}] selected {len(chosen)}")
    for index, topic in enumerate(chosen, 1):
        try:
            raw = fetch_content(cfg, topic["id"])
            source_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
            if (
                args.refresh_changed
                and not args.refresh_all
                and topic.get("status") == "done"
                and topic.get("contentHash") == source_hash
            ):
                print(f"[{index}/{len(chosen)}] unchanged {topic['localPath']}")
            else:
                stamp, path, digest = write(topic, markdown(raw, topic, manifest["topics"]), cfg, source_hash)
                topic.update(
                    status="done",
                    error=None,
                    scrapedAt=stamp,
                    contentHash=digest,
                    bytes=path.stat().st_size,
                )
                print(f"[{index}/{len(chosen)}] done {path.relative_to(ROOT)}")
        except Exception as exc:
            topic.update(status="error", error=str(exc))
            print(f"[{index}/{len(chosen)}] ERROR {topic['title']}: {exc}", file=sys.stderr)
        save(manifest, product_paths["manifest"])
        time.sleep(args.delay)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", default=DEFAULT_PRODUCT_KEY)
    parser.add_argument("--all-pending", action="store_true")
    parser.add_argument("--section")
    parser.add_argument("--path-contains")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument("--refresh-changed", action="store_true")
    parser.add_argument("--refresh-all", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--delay", type=float, default=0.35)
    args = parser.parse_args(argv)
    if not any(
        (
            args.all_pending,
            args.section,
            args.path_contains,
            args.retry_errors,
            args.refresh_changed,
            args.refresh_all,
        )
    ):
        parser.error("Select --all-pending, --section, --path-contains, --retry-errors, --refresh-changed, or --refresh-all")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    keys = PRODUCTS if args.product == "all" else {args.product: get_product(args.product)}
    for cfg in keys.values():
        scrape(cfg, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
