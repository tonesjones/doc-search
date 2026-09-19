"""Validate the root product routing registry."""

from __future__ import annotations

import argparse
from pathlib import Path

from product_registry import RegistryError, load_registry


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    try:
        products = load_registry(args.repo_root.resolve())
    except RegistryError as exc:
        parser.error(str(exc))
    print(f"Product registry valid with {len(products)} products")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
