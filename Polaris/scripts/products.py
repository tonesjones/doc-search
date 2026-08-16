"""Registry for the independently scraped Polaris Platform documentation."""
from __future__ import annotations

from pathlib import Path

BASE_URL = "https://docs.blackduck.com"

# Verified 2026-08-12 against GET /api/khub/maps/5MMaMfDebQ2sCji2eI3ezg/toc.
# Keeping it explicit avoids silently scraping similarly named legacy books.
PRODUCTS = {
    "polaris-platform-latest": {
        "key": "polaris-platform-latest",
        "title": "Black Duck Polaris Platform",
        "version": "latest",
        "map_id": "5MMaMfDebQ2sCji2eI3ezg",
        "reader_path": "r/polaris/black-duck-polaris-platform/",
        "docs_root": "platform",
        "source_dir": "sources/polaris-platform-latest",
        "primary": True,
    },
}
DEFAULT_PRODUCT_KEY = "polaris-platform-latest"

def get_product(key: str | None = None) -> dict:
    key = key or DEFAULT_PRODUCT_KEY
    if key not in PRODUCTS:
        raise SystemExit(f"Unknown product '{key}'. Known: {', '.join(PRODUCTS)}")
    return PRODUCTS[key]

def paths(cfg: dict, root: Path) -> dict[str, Path]:
    source = root / cfg["source_dir"]
    return {"source": source, "toc": source / "toc.json", "manifest": source / "manifest.json", "index": root / f"index-{cfg['key']}.md"}

def toc_url(cfg: dict) -> str:
    if not cfg.get("map_id"):
        raise RuntimeError(f"{cfg['key']} has no verified map_id in scripts/products.py")
    return f"{BASE_URL}/api/khub/maps/{cfg['map_id']}/toc"

def content_url(cfg: dict, content_id: str) -> str:
    if not cfg.get("map_id"):
        raise RuntimeError(f"{cfg['key']} has no verified map_id in scripts/products.py")
    return f"{BASE_URL}/api/khub/maps/{cfg['map_id']}/topics/{content_id}/content"

def reader_url(cfg: dict) -> str:
    return f"{BASE_URL}/{cfg['reader_path']}"
