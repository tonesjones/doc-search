#!/usr/bin/env python3
"""Shared product/map registry for multi-corpus Black Duck docs scraping."""

from __future__ import annotations

from collections import OrderedDict
from typing import Any

BASE_URL = "https://docs.blackduck.com"

# SCA root section title → docs/ slug (only used when docs_root is None).
BLACKDUCK_ROOT_SLUGS: OrderedDict[str, str] = OrderedDict(
    [
        ("Black Duck SCA Help Center", "help-center"),
        ("Getting Started with Black Duck", "getting-started"),
        ("Getting Started with the Black Duck API", "api"),
        ("Architecture and Network Communications", "architecture"),
        ("Hosted Architecture and Network Communications", "architecture-hosted"),
        ("Installing Black Duck using Kubernetes and OpenShift", "install-kubernetes"),
        ("Installing Black Duck using Docker Swarm", "install-docker-swarm"),
        ("Scanning Best Practices", "scanning-best-practices"),
        ("Reporting Database", "reporting-database"),
        ("Release Notes", "release-notes"),
    ]
)

# Key = CLI --product value / sources/<key>/ folder name
PRODUCTS: dict[str, dict[str, Any]] = {
    "blackduck-2026.7": {
        "key": "blackduck-2026.7",
        "map_id": "1WqD3iF0wWDzpOGfy2mr8Q",
        "version": "2026.7",
        "product": "blackduck",
        "title": "Black Duck Documentation",
        "source_dir": "sources/blackduck-2026.7",
        # None → map TOC roots via root_slugs to top-level docs/ folders
        "docs_root": None,
        "root_slugs": BLACKDUCK_ROOT_SLUGS,
        "reader_product": "blackduck",
        "reader_book": "black-duck-documentation",
        "index_file": "index.md",
        "default": True,
        "phase": 1,
    },
    "detect-11.5.1": {
        "key": "detect-11.5.1",
        "map_id": "bMVbOgKqSRm_N11~2Mv5gg",
        "version": "11.5.1",
        "product": "detect",
        "title": "Black Duck Detect",
        "source_dir": "sources/detect-11.5.1",
        "docs_root": "detect",
        "root_slugs": OrderedDict(),
        "reader_product": "detect",
        "reader_book": "black-duck-detect",
        "index_file": "index-detect.md",
        "default": False,
        "phase": 2,
    },
    "alert-8.4.0": {
        "key": "alert-8.4.0",
        "map_id": "QEB0e_qPG~BdIwQfv5eDZQ",
        "version": "8.4.0",
        "product": "alert",
        "title": "Black Duck Alert",
        "source_dir": "sources/alert-8.4.0",
        "docs_root": "alert",
        "root_slugs": OrderedDict(),
        "reader_product": "alert",
        "reader_book": "black-duck-alert-user-guide",
        "index_file": "index-alert.md",
        "default": False,
        "phase": 2,
    },
    "bridge-latest": {
        "key": "bridge-latest",
        "map_id": "ilBVZr_kR5v3KVjK1p~wbw",
        "version": "latest",
        "product": "bridge",
        "title": "Bridge CLI",
        "source_dir": "sources/bridge-latest",
        "docs_root": "bridge",
        "root_slugs": OrderedDict(),
        "reader_product": "bridge",
        "reader_book": "bridge-cli-guide",
        "index_file": "index-bridge.md",
        "default": False,
        "phase": 2,
    },
    "c-cpp-tool-latest": {
        "key": "c-cpp-tool-latest",
        "map_id": "2GUQEgoyKxsQAcOtWsqdDA",
        "version": "latest",
        "product": "c-cpp-tool",
        "title": "Black Duck C/CPP Tool",
        "source_dir": "sources/c-cpp-tool-latest",
        "docs_root": "c-cpp-tool",
        "root_slugs": OrderedDict(),
        "reader_product": "blackduck-tools",
        "reader_book": "black-duck-tools",
        "index_file": "index-c-cpp-tool.md",
        "default": False,
        "phase": 2,
    },
    "airgap-kb-latest": {
        "key": "airgap-kb-latest",
        "map_id": "YsDtm_HKwGM6efkx~2HVvQ",
        "version": "latest",
        "product": "airgap-kb",
        "title": "Black Duck Air-gapped KnowledgeBase",
        "source_dir": "sources/airgap-kb-latest",
        "docs_root": "airgap-kb",
        "root_slugs": OrderedDict(),
        "reader_product": "blackduck-onprem",
        "reader_book": "black-duck-air-gapped-knowledgebase",
        "index_file": "index-airgap-kb.md",
        "default": False,
        "phase": 2,
        "optional": True,
    },
}

DEFAULT_PRODUCT_KEY = "blackduck-2026.7"


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
