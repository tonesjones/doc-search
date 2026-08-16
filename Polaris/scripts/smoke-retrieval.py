#!/usr/bin/env python3
"""Retrieval smoke tests for the local Polaris Platform corpus."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIDGE = Path(r"C:\TestCode\BlackDuck SCA\docs\bridge")
BRIDGE_INDEX = Path(r"C:\TestCode\BlackDuck SCA\index-bridge.md")

CHECKS = (
    (
        "platform",
        ROOT / "docs/platform/understand-polaris/polaris-product-overview.md",
        ("Static Application Security Testing", "Software Composition Analysis", "Dynamic Application Security Testing"),
    ),
    (
        "scanning",
        ROOT / "docs/platform/how-to/how-to-test-from-the-web-ui.md",
        ("SAST", "SCA"),
    ),
    (
        "policy",
        ROOT / "docs/platform/how-to/create-and-manage-policies.md",
        ("Issue policies", "Component policies", "Test scheduling policies"),
    ),
    (
        "roles",
        ROOT / "docs/platform/reference/roles-and-permissions.md",
        ("Organization Admin", "Yes", "No", "View entitlements"),
    ),
    (
        "mcp",
        ROOT / "docs/platform/how-to/issue-management-mcp-server.md",
        ("list_issues", "Model Context Protocol"),
    ),
)


def main() -> int:
    failures: list[str] = []
    for name, path, needles in CHECKS:
        if not path.exists():
            failures.append(f"{name}: missing {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        missing = [needle for needle in needles if needle not in text]
        if missing:
            failures.append(f"{name}: {path.name} missing {missing}")
    if not BRIDGE.exists() or not BRIDGE_INDEX.exists():
        failures.append(f"ci: Bridge corpus not found at {BRIDGE} / {BRIDGE_INDEX}")
    else:
        print("ci: Bridge corpus present")
    if failures:
        print("\n".join(failures))
        return 1
    print("Retrieval smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
