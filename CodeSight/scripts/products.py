#!/usr/bin/env python3
"""Shared product/map registry for Black Duck Code Sight docs scraping."""

from __future__ import annotations

from collections import OrderedDict
from typing import Any

BASE_URL = "https://docs.blackduck.com"

# Code Sight TOC root section title → docs/ slug (when docs_root is None).
# Verified 2026-10-06 against GET /api/khub/maps/MbKAMeBG9Dkor~tl3lqBXg/toc.
CODESIGHT_ROOT_SLUGS: OrderedDict[str, str] = OrderedDict(
    [
        ("Welcome to Code Sight", "welcome"),
        ("Code Sight Support Matrix", "support-matrix"),
        ("Installing Code Sight", "installing"),
        ("Authenticating to Servers in Code Sight", "authenticating"),
        ("Viewing Issues in Code Sight", "viewing-issues"),
        ("Signal and Code Sight VS Code Extension", "signal-vscode-extension"),
        ("Coverity with Code Sight", "coverity"),
        ("Black Duck SCA with Code Sight", "black-duck-sca"),
        ("Polaris with Code Sight", "polaris"),
        ("Software Risk Manager with Code Sight", "software-risk-manager"),
        ("Code Sight Standard Edition", "standard-edition"),
        ("Code Sight: Preferences and Troubleshooting", "preferences-troubleshooting"),
        ("Code Sight Release Notes and Known Issues", "release-notes"),
        ("General Information", "general-information"),
    ]
)

# Key = CLI --product value / sources/<key>/ folder name
PRODUCTS: dict[str, dict[str, Any]] = {
    "codesight-2026.9.0": {
        "key": "codesight-2026.9.0",
        "map_id": "MbKAMeBG9Dkor~tl3lqBXg",
        "version": "2026.9.0",
        "product": "codesight",
        "title": "Black Duck Code Sight",
        "source_dir": "sources/codesight-2026.9.0",
        # None → map TOC roots via root_slugs to top-level docs/ folders
        "docs_root": None,
        "root_slugs": CODESIGHT_ROOT_SLUGS,
        "reader_product": "codesight",
        "reader_book": "code-sight-documentation",
        "reader_path": "r/codesight/2026.9.0/code-sight-documentation/",
        "index_file": "index.md",
        "default": True,
        "phase": 1,
    },
}

DEFAULT_PRODUCT_KEY = "codesight-2026.9.0"


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
