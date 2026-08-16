#!/usr/bin/env python3
"""Initialize or rebuild Polaris Fluid Topics manifests and indexes."""
from __future__ import annotations

import argparse, json, re, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

from products import DEFAULT_PRODUCT_KEY, PRODUCTS, get_product, paths, reader_url, toc_url

ROOT = Path(__file__).resolve().parents[1]

def now() -> str: return datetime.now(timezone.utc).isoformat()
def slug(text: str) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", (text or "untitled").lower()).strip("-")
    return (text[:80].rstrip("-") or "untitled")
def read_json(path: Path): return json.loads(path.read_text(encoding="utf-8"))
def stats(topics):
    out = {"total":len(topics), "pending":0, "done":0, "skipped":0, "error":0}
    for item in topics: out[item.get("status") if item.get("status") in out else "pending"] += 1
    return out
def fetch(url: str):
    request = urllib.request.Request(url, headers={"Accept":"application/json", "User-Agent":"PolarisDocsCorpus/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))

def flatten(nodes, cfg):
    topics, used = [], {}
    def walk(items, parents):
        for node in items:
            title = node.get("title") or "untitled"
            hierarchy = parents + [title]
            fragments = ["docs", cfg["docs_root"], *[slug(x) for x in hierarchy[:-1]], slug(title)+".md"]
            local = "/".join(fragments)
            if local in used:
                used[local] += 1; local = local[:-3] + f"-{used[local]}.md"
            else: used[local] = 1
            pretty = node.get("prettyUrl") or ""
            source = pretty if pretty.startswith("http") else ("https://docs.blackduck.com" + pretty if pretty else "")
            children = node.get("children") or []
            topics.append({"id":node.get("contentId"), "tocId":node.get("tocId"), "title":title, "path":hierarchy,
                "section":hierarchy[0], "prettyUrl":pretty, "sourceUrl":source, "localPath":local,
                "depth":len(hierarchy), "status":"pending", "error":None, "scrapedAt":None,
                "contentHash":None, "bytes":None, "hasChildren":bool(children)})
            walk(children, hierarchy)
    walk(nodes, [])
    return topics

def preserve(new, old):
    prior = {x.get("id"):x for x in old.get("topics", []) if x.get("id")}
    for item in new:
        previous = prior.get(item.get("id"))
        if previous:
            for key in ("status", "error", "scrapedAt", "contentHash", "bytes", "localPath"):
                item[key] = previous.get(key)
    return new

def write_index(cfg, manifest, destination):
    st = manifest["stats"]; lines = [f"# {cfg['title']} index", "", "> Generated local RAG catalog. Do not hand-edit topic rows.", "",
        "| Field | Value |", "|---|---|", f"| Product key | `{cfg['key']}` |", f"| Version | `{cfg['version']}` |",
        f"| Map ID | `{cfg['map_id']}` |", f"| Progress | {st['done']}/{st['total']} done · {st['pending']} pending · {st['error']} error |", "", "## Topics", ""]
    for topic in manifest["topics"]:
        mark = {"pending":"[ ]", "done":"[x]", "skipped":"[-]", "error":"[!]"}.get(topic["status"], "[ ]")
        indent = "  " * (topic["depth"] - 1)
        source = f" · [source]({topic['sourceUrl']})" if topic["sourceUrl"] else ""
        lines.append(f"{indent}- {mark} [{topic['title']}]({topic['localPath']}){source}")
    destination.write_text("\n".join(lines)+"\n", encoding="utf-8")
    if cfg.get("primary"):
        preamble = [
            "# Polaris Documentation Corpus",
            "",
            "> Generated local RAG catalog. Do not hand-edit topic rows.",
            "",
            "Polaris CI, Bridge CLI, SARIF, and pull-request workflows live in `C:\\TestCode\\BlackDuck SCA\\docs\\bridge\\` and `index-bridge.md`.",
            "",
        ]
        (ROOT / "index.md").write_text("\n".join(preamble) + "\n" + "\n".join(lines) + "\n", encoding="utf-8")

def build(cfg, args):
    p = paths(cfg, ROOT); p["source"].mkdir(parents=True, exist_ok=True)
    old = read_json(p["manifest"]) if p["manifest"].exists() else None
    if args.init or args.refresh_toc or not p["toc"].exists():
        raw = fetch(toc_url(cfg)); p["toc"].write_text(json.dumps(raw, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
        topics = flatten(raw, cfg)
        if old and args.refresh_toc: topics = preserve(topics, old)
        manifest = {"productKey":cfg["key"], "title":cfg["title"], "version":cfg["version"], "mapId":cfg["map_id"], "readerUrl":reader_url(cfg), "tocUrl":toc_url(cfg), "lastTocFetch":now(), "lastIndexBuild":now(), "topics":topics}
    elif old:
        manifest = old; manifest["lastIndexBuild"] = now()
    else: raise RuntimeError("Manifest does not exist; use --init")
    manifest["stats"] = stats(manifest["topics"])
    p["manifest"].write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    write_index(cfg, manifest, p["index"])
    print(f"[{cfg['key']}] {manifest['stats']} -> {p['index'].name}")

def hub():
    lines=["# Polaris Documentation Corpus", "", "> Generated progress hub for the local Polaris knowledge base.", "", "| Product | Version | Progress | Index |", "|---|---|---|---|"]
    for cfg in PRODUCTS.values():
        p=paths(cfg, ROOT)
        if p["manifest"].exists():
            st=read_json(p["manifest"]).get("stats",{}); progress=f"{st.get('done',0)}/{st.get('total',0)} done · {st.get('pending',0)} pending"
        else: progress="not initialized"
        lines.append(f"| {cfg['title']} | {cfg['version']} | {progress} | [index-{cfg['key']}.md](index-{cfg['key']}.md) |")
    (ROOT/"corpus-status.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    for cfg in PRODUCTS.values():
        product_paths = paths(cfg, ROOT)
        if cfg.get("primary") and product_paths["manifest"].exists():
            write_index(cfg, read_json(product_paths["manifest"]), product_paths["index"])

parser=argparse.ArgumentParser()
parser.add_argument("--product", default=DEFAULT_PRODUCT_KEY); parser.add_argument("--init",action="store_true"); parser.add_argument("--refresh-toc",action="store_true"); parser.add_argument("--hub",action="store_true"); parser.add_argument("--list-products",action="store_true")
args=parser.parse_args()
if args.list_products:
    for key,cfg in PRODUCTS.items(): print(f"{key:28} map={cfg['map_id'] or 'UNVERIFIED'}")
    raise SystemExit()
keys=PRODUCTS if args.product=="all" else {args.product:get_product(args.product)}
rc=0
for cfg in keys.values():
    if args.product == "all" and not (args.init or args.refresh_toc) and not paths(cfg, ROOT)["manifest"].exists():
        print(f"[{cfg['key']}] not initialized; skipped")
        continue
    try: build(cfg,args)
    except Exception as exc: print(f"[{cfg['key']}] ERROR: {exc}",file=sys.stderr); rc=1
if args.hub or args.product=="all": hub()
raise SystemExit(rc)
