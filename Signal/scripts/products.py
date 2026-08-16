#!/usr/bin/env python3
"""Shared product/map registry for Black Duck Signal docs scraping."""

from __future__ import annotations

from collections import OrderedDict
from typing import Any

BASE_URL = "https://docs.blackduck.com"

# Signal TOC root section title → docs/ slug (when docs_root is None).
# Verified 2026-08-12 against GET /api/khub/maps/xmDr3Yryk7OYDGb__OGKlg/toc.
SIGNAL_ROOT_SLUGS: OrderedDict[str, str] = OrderedDict(
    [
        ("Overview of Black Duck Signal", "overview"),
        ("Scan your code changes", "scan-changes"),
        ("Scan a full project from the CLI", "scan-project"),
        ("Reference guide", "reference"),
        ("AI security, data protection, and trust", "ai-security"),
        ("Signal release notes", "release-notes"),
    ]
)

# Key = CLI --product value / sources/<key>/ folder name
PRODUCTS: dict[str, dict[str, Any]] = {
    "signal-latest": {
        "key": "signal-latest",
        "map_id": "xmDr3Yryk7OYDGb__OGKlg",
        "version": "latest",
        "product": "signal",
        "title": "Black Duck Signal",
        "source_dir": "sources/signal-latest",
        # None → map TOC roots via root_slugs to top-level docs/ folders
        "docs_root": None,
        "root_slugs": SIGNAL_ROOT_SLUGS,
        "reader_product": "signal",
        "reader_book": "black-duck-signal",
        # Signal reader URLs have no year/version segment.
        "reader_path": "r/signal/black-duck-signal/",
        "index_file": "index.md",
        "default": True,
        "phase": 1,
    },
}

DEFAULT_PRODUCT_KEY = "signal-latest"


def get_product(key: str | None = None) -> dict[str, Any]:
    k = key or DEFAULT_PRODUCT_KEY
    if k not in PRODUCTS:
        known = ", ".join(sorted(PRODUCTS))
        raise SystemExit(f"Unknown product '{k}'. Known: {known}")
    return PRODUCTS[k]


def product_paths(cfg: dict[str, Any], root) -> dict[str, Any]:
    """Resolve Path objects for a product config against repo root."""
    source = root / cfg["source_dir"]
    return {
        "source_dir": source,
        "toc_path": source / "toc.json",
        "manifest_path": source / "manifest.json",
        "index_path": root / cfg["index_file"],
    }


def toc_api(cfg: dict[str, Any]) -> str:
    return f"{BASE_URL}/api/khub/maps/{cfg['map_id']}/toc"


def content_api_template(cfg: dict[str, Any]) -> str:
    return f"{BASE_URL}/api/khub/maps/{cfg['map_id']}/topics/{{contentId}}/content"


def content_url(cfg: dict[str, Any], content_id: str) -> str:
    return f"{BASE_URL}/api/khub/maps/{cfg['map_id']}/topics/{content_id}/content"


def base_reader_url(cfg: dict[str, Any]) -> str:
    if cfg.get("reader_path"):
        path = str(cfg["reader_path"]).lstrip("/")
        if not path.endswith("/"):
            path += "/"
        return f"{BASE_URL}/{path}"
    return (
        f"{BASE_URL}/r/{cfg['reader_product']}/{cfg['version']}/"
        f"{cfg['reader_book']}/"
    )


def list_product_keys(phase: int | None = None) -> list[str]:
    keys = []
    for k, p in PRODUCTS.items():
        if phase is not None and p.get("phase") != phase:
            continue
        keys.append(k)
    return keys
