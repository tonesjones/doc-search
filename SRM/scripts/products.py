#!/usr/bin/env python3
"""Product/map registry for the Software Risk Manager documentation corpus."""

from __future__ import annotations

from collections import OrderedDict
from typing import Any

BASE_URL = "https://docs.blackduck.com"

SRM_ROOT_SLUGS: OrderedDict[str, str] = OrderedDict(
    [
        ("Software Risk Manager User Guide", "software-risk-manager-user-guide"),
        ("Software Risk Manager Install Guide", "software-risk-manager-install-guide"),
        ("Software Risk Manager Plugins Guide", "software-risk-manager-plugins-guide"),
        ("Software Risk Manager API Guide", "software-risk-manager-api-guide"),
    ]
)

PRODUCTS: dict[str, dict[str, Any]] = {
    "srm-latest": {
        "key": "srm-latest",
        "map_id": "6dyNreOMuOAenymg0Owm8A",
        "version": "latest",
        "product": "srm",
        "title": "Software Risk Manager Documentation",
        "source_dir": "sources/srm-latest",
        "docs_root": None,
        "root_slugs": SRM_ROOT_SLUGS,
        "reader_product": "srm",
        "reader_book": "software-risk-manager-documentation",
        "index_file": "index.md",
        "default": True,
        "phase": 1,
    },
}

DEFAULT_PRODUCT_KEY = "srm-latest"


def validate_registry(products: dict[str, dict[str, Any]] = PRODUCTS) -> None:
    """Reject product entries that would overwrite another product's corpus files."""
    required = ("key", "map_id", "version", "source_dir", "index_file")
    seen: dict[str, dict[str, str]] = {"source_dir": {}, "index_file": {}}
    none_root_entries: list[dict[str, Any]] = []
    docs_roots: dict[str, str] = {}
    for name, cfg in products.items():
        missing = [field for field in required if not cfg.get(field)]
        if missing:
            raise ValueError(f"Product {name!r} missing required fields: {', '.join(missing)}")
        if cfg["key"] != name:
            raise ValueError(f"Product registry key mismatch: {name!r} != {cfg['key']!r}")
        for field in seen:
            value = str(cfg[field]).replace("\\", "/").rstrip("/").lower()
            previous = seen[field].get(value)
            if previous is not None:
                raise ValueError(f"Product registry collision on {field}: {previous!r} and {name!r} use {cfg[field]!r}")
            seen[field][value] = name
        docs_root = cfg.get("docs_root")
        if docs_root is None:
            none_root_entries.append(cfg)
            continue
        value = str(docs_root).replace("\\", "/").strip("/").lower()
        previous = docs_roots.get(value)
        if previous is not None:
            raise ValueError(f"Product registry collision on docs_root: {previous!r} and {name!r} use {docs_root!r}")
        docs_roots[value] = name

    if len(none_root_entries) > 1:
        root_sets = [set((cfg.get("root_slugs") or {}).values()) for cfg in none_root_entries]
        if not all(root_sets) or any(left & right for i, left in enumerate(root_sets) for right in root_sets[i + 1:]):
            keys = ", ".join(cfg["key"] for cfg in none_root_entries)
            raise ValueError(f"Unsafe null docs_root registry entries: {keys}")


validate_registry()


def get_product(key: str | None = None) -> dict[str, Any]:
    k = key or DEFAULT_PRODUCT_KEY
    if k not in PRODUCTS:
        known = ", ".join(sorted(PRODUCTS))
        raise SystemExit(f"Unknown product '{k}'. Known: {known}")
    return PRODUCTS[k]


def product_paths(cfg: dict[str, Any], root) -> dict[str, Any]:
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
    return f"{BASE_URL}/r/{cfg['reader_product']}/{cfg['version']}/{cfg['reader_book']}/"


def list_product_keys(phase: int | None = None) -> list[str]:
    return [key for key, cfg in PRODUCTS.items() if phase is None or cfg.get("phase") == phase]
