#!/usr/bin/env python3
"""Shared product/map registry for Coverity docs scraping."""

from __future__ import annotations

from collections import OrderedDict
from typing import Any

BASE_URL = "https://docs.blackduck.com"

# Coverity TOC root section title → docs/ slug (when docs_root is None).
COVERITY_ROOT_SLUGS: OrderedDict[str, str] = OrderedDict(
    [
        ("Acknowledgements", "misc"),
        ("Coverity overview", "overview"),
        ("Coverity Connect", "connect"),
        ("Coverity Analysis", "analysis"),
        ("Clients, plug-ins, integrations, and APIs", "clients-plugins"),
        ("Coverity Connect APIs", "connect-apis"),
        ("Cloud Native Coverity deployment", "cloud-native"),
        ("All checkers", "checkers"),
        ("SpotBugs™ Checker Reference", "checkers"),
        ("Coverity release notes and upgrade considerations", "release-notes"),
        ("Coverity glossary", "glossary"),
        ("Legal notice", "legal"),
        ("Black Duck statement on inclusivity and diversity", "misc"),
    ]
)

# Key = CLI --product value / sources/<key>/ folder name
PRODUCTS: dict[str, dict[str, Any]] = {
    "coverity-2026.6": {
        "key": "coverity-2026.6",
        "map_id": "Ul9eg_yUOJh8gKU4cs1xrg",
        "version": "2026.6",
        "product": "coverity",
        "title": "Coverity Documentation",
        "source_dir": "sources/coverity-2026.6",
        # None → map TOC roots via root_slugs to top-level docs/ folders
        "docs_root": None,
        "root_slugs": COVERITY_ROOT_SLUGS,
        "reader_product": "coverity",
        "reader_book": "coverity-documentation",
        "index_file": "index.md",
        "default": True,
        "phase": 1,
    },
}

DEFAULT_PRODUCT_KEY = "coverity-2026.6"


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
