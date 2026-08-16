#!/usr/bin/env python3
"""Build/refresh manifest.json and product index from Fluid Topics TOC.

Usage:
  python scripts/build-index.py                         # rebuild Sigma index from manifest
  python scripts/build-index.py --product sigma-2026.8.0 --init
  python scripts/build-index.py --product sigma-2026.8.0 --refresh-toc
  python scripts/build-index.py --product all --init
  python scripts/build-index.py --list-products
  python scripts/build-index.py --hub
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

from corpus_utils import atomic_write_text
from products import (
    BASE_URL,
    DEFAULT_PRODUCT_KEY,
    PRODUCTS,
    base_reader_url,
    content_api_template,
    get_product,
    list_product_keys,
    product_paths,
    toc_api,
)

ROOT = Path(__file__).resolve().parents[1]

STATUS_MARK = {
    "pending": "[ ]",
    "done": "[x]",
    "skipped": "[-]",
    "error": "[!]",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(title: str, max_len: int = 80) -> str:
    if not title or not title.strip():
        return "untitled"
    s = title.lower()
    s = s.replace("'", "").replace("'", "").replace("'", "")
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "untitled"


# Keep absolute Windows paths under MAX_PATH (260), leaving headroom for the drive root.
MAX_ABS_PATH_LEN = 240


def fit_local_path(parts: list[str], root: Path) -> str:
    """Join path parts; collapse/truncate if absolute path would exceed Windows MAX_PATH."""
    local = "/".join(parts)
    abs_len = len(str(root / local))
    if abs_len <= MAX_ABS_PATH_LEN:
        return local

    # Keep docs/<root>/<first>/<last>.md; drop or compress middle segments
    if len(parts) <= 3:
        # Truncate filename stem
        stem = parts[-1]
        if stem.endswith(".md"):
            name, ext = stem[:-3], ".md"
        else:
            name, ext = stem, ""
        overhead = abs_len - len(name)
        keep = max(20, MAX_ABS_PATH_LEN - overhead)
        parts = parts[:-1] + [name[:keep].rstrip("-") + ext]
        return "/".join(parts)

    # parts: docs, product, section, *mids, file.md
    head = parts[:3]
    tail = parts[-1]
    mids = parts[3:-1]
    # Prefer last mid only, then drop mids entirely
    candidates = []
    if mids:
        candidates.append(head + [mids[-1]] + [tail])
    candidates.append(head + [tail])
    # Shorten each candidate's file stem until it fits
    for cand in candidates:
        local = "/".join(cand)
        if len(str(root / local)) <= MAX_ABS_PATH_LEN:
            return local
    # Last resort: aggressive stem truncate on head+file
    stem = tail[:-3] if tail.endswith(".md") else tail
    ext = ".md" if tail.endswith(".md") else ""
    base = head
    budget = MAX_ABS_PATH_LEN - len(str(root / "/".join(base + [ext]))) - 1
    stem = stem[: max(12, budget)].rstrip("-")
    return "/".join(base + [stem + ext])


def fetch_toc(cfg: dict) -> list:
    url = toc_api(cfg)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def flatten_toc(nodes: list, cfg: dict) -> list[dict]:
    out: list[dict] = []
    path_counts: dict[str, int] = {}
    root_slugs: OrderedDict = cfg.get("root_slugs") or OrderedDict()
    docs_root = cfg.get("docs_root")

    def walk(items: list, path: list[str]) -> None:
        for n in items:
            titles = path + [n.get("title") or "untitled"]
            root_title = titles[0]
            topic_slug = slugify(titles[-1])
            mid = [slugify(t) for t in titles[1:-1]] if len(titles) > 2 else []

            if docs_root:
                # Companion products: everything under docs/<docs_root>/...
                parts = ["docs", docs_root]
                # include root topic slug in path for multi-root TOCs
                if len(titles) == 1:
                    parts.append(f"{topic_slug}.md")
                else:
                    parts.append(slugify(root_title))
                    parts.extend(mid)
                    parts.append(f"{topic_slug}.md")
            else:
                root_slug = root_slugs.get(root_title, slugify(root_title))
                parts = ["docs", root_slug, *mid, f"{topic_slug}.md"]

            local_path = fit_local_path(parts, ROOT)
            if local_path in path_counts:
                path_counts[local_path] += 1
                if local_path.endswith(".md"):
                    local_path = local_path[:-3] + f"-{path_counts[local_path]}.md"
                else:
                    local_path = local_path + f"-{path_counts[local_path]}"
                local_path = fit_local_path(local_path.split("/"), ROOT)
            else:
                path_counts[local_path] = 1

            pretty = n.get("prettyUrl") or ""
            source_url = (
                BASE_URL + pretty if pretty and not pretty.startswith("http") else pretty
            )
            children = n.get("children") or []
            has_children = len(children) > 0

            out.append(
                {
                    "id": n.get("contentId"),
                    "tocId": n.get("tocId"),
                    "title": n.get("title"),
                    "path": titles,
                    "section": root_title,
                    "prettyUrl": pretty,
                    "sourceUrl": source_url,
                    "localPath": local_path,
                    "depth": len(titles),
                    "hasChildren": has_children,
                    "directChildren": len(children),
                    "status": "pending",
                    "error": None,
                    "scrapedAt": None,
                    "lastCheckedAt": None,
                    "contentHash": None,
                    "bytes": None,
                }
            )
            if has_children:
                walk(children, titles)

    walk(nodes, [])
    return out


def compute_stats(topics: list[dict]) -> dict:
    stats = {"total": len(topics), "pending": 0, "done": 0, "skipped": 0, "error": 0}
    for t in topics:
        st = t.get("status") or "pending"
        if st not in stats:
            st = "pending"
        stats[st] = stats.get(st, 0) + 1
    for k in ("pending", "done", "skipped", "error"):
        stats.setdefault(k, 0)
    return stats


def merge_statuses(new_topics: list[dict], old_manifest: dict | None) -> list[dict]:
    if not old_manifest:
        return new_topics
    by_id = {t["id"]: t for t in old_manifest.get("topics", []) if t.get("id")}
    for t in new_topics:
        old = by_id.get(t["id"])
        if not old:
            continue
        for key in ("status", "error", "scrapedAt", "lastCheckedAt", "contentHash", "bytes"):
            if key in old:
                t[key] = old[key]
        if old.get("status") == "done" and old.get("localPath"):
            t["localPath"] = old["localPath"]
    return new_topics


def build_manifest(topics: list[dict], cfg: dict, toc_fetched: bool) -> dict:
    ts = now_iso()
    root_slugs = cfg.get("root_slugs") or OrderedDict()
    if cfg.get("docs_root"):
        # Derive section list from topics for companions
        seen: OrderedDict[str, str] = OrderedDict()
        for t in topics:
            sec = t.get("section") or "untitled"
            if sec not in seen:
                seen[sec] = slugify(sec)
        root_sections = [{"title": k, "slug": v} for k, v in seen.items()]
    else:
        root_sections = [{"title": k, "slug": v} for k, v in root_slugs.items()]

    return {
        "mapId": cfg["map_id"],
        "version": cfg["version"],
        "product": cfg["product"],
        "productKey": cfg["key"],
        "title": cfg["title"],
        "tocApi": toc_api(cfg),
        "contentApiTemplate": content_api_template(cfg),
        "baseReaderUrl": base_reader_url(cfg),
        "docsRoot": cfg.get("docs_root"),
        "lastIndexBuild": ts,
        "lastTocFetch": ts if toc_fetched else None,
        "scrapedAt": None,
        "statusValues": ["pending", "done", "skipped", "error"],
        "stats": compute_stats(topics),
        "rootSections": root_sections,
        "topics": topics,
    }


def write_index(manifest: dict, cfg: dict, index_path: Path) -> None:
    stats = manifest["stats"]
    version = manifest.get("version") or cfg["version"]
    map_id = manifest.get("mapId") or cfg["map_id"]
    total = max(1, stats["total"])
    pct = round(100.0 * stats["done"] / total, 1)
    topics = manifest["topics"]
    source_rel = cfg["source_dir"].replace("\\", "/")
    root_slugs = cfg.get("root_slugs") or OrderedDict()
    docs_root = cfg.get("docs_root") or manifest.get("docsRoot")

    lines: list[str] = []
    a = lines.append
    a(f"# {cfg['title']} Documentation Index")
    a("")
    a(
        "> Auto-generated catalog for local RAG. Do not hand-edit topic rows — "
        f"update `{source_rel}/manifest.json` statuses and run "
        f"`python scripts/build-index.py --product {cfg['key']}`."
    )
    a("")
    a("## Corpus status")
    a("")
    a("| Field | Value |")
    a("|-------|-------|")
    a(f"| Product | {cfg['title']} |")
    a(f"| Product key | `{cfg['key']}` |")
    a(f"| Version | **{version}** |")
    a(f"| Map ID | `{map_id}` |")
    a(f"| TOC nodes | **{stats['total']}** |")
    a(
        f"| Progress | **{stats['done']}/{stats['total']} done** ({pct}%) · "
        f"{stats['pending']} pending · {stats['skipped']} skipped · {stats['error']} error |"
    )
    a(f"| Last index build | {manifest.get('lastIndexBuild')} |")
    a(f"| Manifest | [{source_rel}/manifest.json]({source_rel}/manifest.json) |")
    a(f"| Raw TOC | [{source_rel}/toc.json]({source_rel}/toc.json) |")
    if docs_root:
        a(f"| Docs root | `docs/{docs_root}/` |")
    a("")
    a("### Status legend")
    a("")
    a("| Mark | Status | Meaning |")
    a("|------|--------|---------|")
    a("| `[ ]` | pending | Not scraped yet |")
    a("| `[x]` | done | Markdown written under `docs/` |")
    a("| `[-]` | skipped | Intentionally not scraped |")
    a("| `[!]` | error | Last scrape failed; retry later |")
    a("")
    a("## How to resume")
    a("")
    a(
        "1. Filter `manifest.json` for `status` `pending` (or `error` to retry)."
    )
    a(
        f"2. `python scripts/scrape-pending.py --product {cfg['key']} --all-pending`"
    )
    a(
        f"3. `python scripts/build-index.py --product {cfg['key']}` to refresh this index."
    )
    a("")
    a("**Content API template:**")
    a("")
    a("```")
    a(content_api_template(cfg))
    a("```")
    a("")
    a("## Section overview")
    a("")
    a("| Section | Topics | Pending | Done | Skipped | Error | Local root |")
    a("|---------|--------|---------|------|---------|-------|------------|")

    by_section: dict[str, list] = {}
    for t in topics:
        by_section.setdefault(t["section"], []).append(t)

    for section, items in sorted(by_section.items(), key=lambda kv: -len(kv[1])):
        if docs_root:
            local = f"docs/{docs_root}/{slugify(section)}/"
        else:
            slug = root_slugs.get(section, slugify(section))
            local = f"docs/{slug}/"
        c = compute_stats(items)
        a(
            f"| {section} | {c['total']} | {c['pending']} | {c['done']} | "
            f"{c['skipped']} | {c['error']} | `{local}` |"
        )

    a("")
    a("## Table of contents")
    a("")

    for t in topics:
        indent = "  " * max(0, int(t.get("depth") or 1) - 1)
        mark = STATUS_MARK.get(t.get("status") or "pending", "[ ]")
        title = t.get("title") or "untitled"
        local = t.get("localPath") or ""
        title_link = f"[{title}]({local})"
        src = f" · [source]({t['sourceUrl']})" if t.get("sourceUrl") else ""
        kids = f" _(+{t['directChildren']})_" if t.get("hasChildren") else ""
        a(f"{indent}- {mark} {title_link}{kids}{src}")

    a("")
    a("---")
    a("")
    reader = base_reader_url(cfg)
    a(
        f"*Generated from Fluid Topics map `{map_id}` ({version}). "
        f"Official docs: [{cfg['title']}]({reader}).*"
    )

    atomic_write_text(index_path, "\n".join(lines) + "\n")


def ensure_doc_dirs(cfg: dict) -> None:
    if cfg.get("docs_root"):
        d = ROOT / "docs" / cfg["docs_root"]
        d.mkdir(parents=True, exist_ok=True)
        keep = d / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")
        return
    for slug in (cfg.get("root_slugs") or {}).values():
        d = ROOT / "docs" / slug
        d.mkdir(parents=True, exist_ok=True)
        keep = d / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def write_hub_index() -> None:
    """Write/refresh corpus-status.md progress hub."""
    rows = []
    for key, cfg in PRODUCTS.items():
        paths = product_paths(cfg, ROOT)
        if not paths["manifest_path"].exists():
            rows.append(
                {
                    "key": key,
                    "title": cfg["title"],
                    "version": cfg["version"],
                    "status": "not initialized",
                    "done": 0,
                    "total": 0,
                    "index": cfg["index_file"],
                    "phase": cfg.get("phase", 1),
                    "optional": cfg.get("optional", False),
                }
            )
            continue
        m = load_json(paths["manifest_path"])
        st = m.get("stats") or compute_stats(m.get("topics", []))
        rows.append(
            {
                "key": key,
                "title": cfg["title"],
                "version": m.get("version") or cfg["version"],
                "status": "ready",
                "done": st.get("done", 0),
                "total": st.get("total", 0),
                "pending": st.get("pending", 0),
                "error": st.get("error", 0),
                "index": cfg["index_file"],
                "phase": cfg.get("phase", 1),
                "optional": cfg.get("optional", False),
            }
        )

    lines: list[str] = []
    a = lines.append
    a("# Black Duck Sigma Documentation Corpus")
    a("")
    a(
        "> Local knowledge base for RAG (Black Duck Sigma / Rapid Scan Static). "
        "The product catalog holds the full TOC; this hub tracks scrape progress. "
        "See [PHASE-PLAN.md](PHASE-PLAN.md) and [CHECKPOINT.md](CHECKPOINT.md)."
    )
    a("")
    a("## Products")
    a("")
    a("| Product | Version | Progress | Index | Notes |")
    a("|---------|---------|----------|-------|-------|")
    for r in rows:
        if r["status"] != "ready":
            prog = "not initialized"
            idx = "—"
        else:
            total = max(1, r["total"])
            pct = round(100.0 * r["done"] / total, 1)
            prog = f"**{r['done']}/{r['total']}** ({pct}%)"
            if r.get("pending"):
                prog += f" · {r['pending']} pending"
            if r.get("error"):
                prog += f" · {r['error']} error"
            idx = f"[{r['index']}]({r['index']})"
        note = "optional" if r.get("optional") else "primary"
        a(f"| {r['title']} | {r['version']} | {prog} | {idx} | {note} |")
    a("")
    a("## How to scrape")
    a("")
    a("```powershell")
    a("python scripts/build-index.py --product sigma-2026.8.0 --init")
    a("python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending")
    a("python scripts/build-index.py --product sigma-2026.8.0 --hub")
    a("```")
    a("")
    a("Phased scrape: see [PHASE-PLAN.md](PHASE-PLAN.md).")
    a("")
    a("Registered product keys: `" + "`, `".join(PRODUCTS.keys()) + "`.")
    a("")
    a("---")
    a("")
    a(
        f"*Hub generated {now_iso()}. Full TOC catalog: "
        f"[index.md](index.md).*"
    )
    a("")

    hub = ROOT / "corpus-status.md"
    atomic_write_text(hub, "\n".join(lines) + "\n")
    print(f"Wrote {hub}")


def build_one(cfg: dict, args: argparse.Namespace) -> int:
    paths = product_paths(cfg, ROOT)
    source_dir = paths["source_dir"]
    toc_path = paths["toc_path"]
    manifest_path = paths["manifest_path"]
    index_path = paths["index_path"]

    source_dir.mkdir(parents=True, exist_ok=True)

    toc_fetched = False
    old_manifest = (
        load_json(manifest_path) if manifest_path.exists() and not args.init else None
    )

    need_toc = args.init or args.refresh_toc or not toc_path.exists()
    if need_toc:
        url = toc_api(cfg)
        print(f"[{cfg['key']}] Fetching TOC from {url} ...")
        toc = fetch_toc(cfg)
        atomic_write_text(toc_path, json.dumps(toc, indent=2, ensure_ascii=False) + "\n")
        toc_fetched = True
        print(f"[{cfg['key']}] Wrote {toc_path}")
    else:
        toc = load_json(toc_path)

    rebuild_topics = args.init or args.refresh_toc or not manifest_path.exists()
    if rebuild_topics:
        topics = flatten_toc(toc, cfg)
        if args.refresh_toc and old_manifest:
            topics = merge_statuses(topics, old_manifest)
            print(f"[{cfg['key']}] Merged statuses ({len(topics)} topics)")
        manifest = build_manifest(topics, cfg, toc_fetched=toc_fetched)
        if old_manifest and not args.init:
            manifest["scrapedAt"] = old_manifest.get("scrapedAt")
            if not toc_fetched:
                manifest["lastTocFetch"] = old_manifest.get("lastTocFetch")
        print(f"[{cfg['key']}] Built manifest with {manifest['stats']['total']} topics")
    else:
        manifest = old_manifest or load_json(manifest_path)
        manifest.setdefault("productKey", cfg["key"])
        manifest.setdefault("docsRoot", cfg.get("docs_root"))
        manifest["stats"] = compute_stats(manifest.get("topics", []))
        manifest["lastIndexBuild"] = now_iso()
        print(
            f"[{cfg['key']}] Refreshed stats from existing manifest "
            f"({manifest['stats']['total']} topics)"
        )

    atomic_write_text(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"[{cfg['key']}] Wrote {manifest_path}")

    ensure_doc_dirs(cfg)
    write_index(manifest, cfg, index_path)
    print(f"[{cfg['key']}] Wrote {index_path}")
    print(
        "[{key}] Progress: {done}/{total} done, {pending} pending, "
        "{skipped} skipped, {error} error".format(key=cfg["key"], **manifest["stats"])
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Sigma docs index/manifest")
    parser.add_argument(
        "--product",
        type=str,
        default=DEFAULT_PRODUCT_KEY,
        help=f"Product key (default: {DEFAULT_PRODUCT_KEY}). Use 'all' for every registered product.",
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Fetch TOC and create a fresh manifest (all pending)",
    )
    parser.add_argument(
        "--refresh-toc",
        action="store_true",
        help="Re-fetch TOC and merge existing statuses by content id",
    )
    parser.add_argument(
        "--list-products",
        action="store_true",
        help="List registered product keys and exit",
    )
    parser.add_argument(
        "--hub",
        action="store_true",
        help="Also write corpus-status.md multi-product hub",
    )
    args = parser.parse_args()

    if args.list_products:
        for key, cfg in PRODUCTS.items():
            opt = " (optional)" if cfg.get("optional") else ""
            print(
                f"{key:20} map={cfg['map_id']} ver={cfg['version']} "
                f"docs={cfg.get('docs_root') or '(section slugs)'} phase={cfg.get('phase')}{opt}"
            )
        return 0

    if args.product == "all":
        keys = list_product_keys()
    else:
        keys = [args.product]

    rc = 0
    for key in keys:
        cfg = get_product(key)
        try:
            build_one(cfg, args)
        except Exception as e:
            print(f"[{key}] ERROR: {e}", file=sys.stderr)
            rc = 1

    if args.hub or args.product == "all":
        try:
            write_hub_index()
        except Exception as e:
            print(f"[hub] WARNING: {e}", file=sys.stderr)

    return rc


if __name__ == "__main__":
    sys.exit(main())
