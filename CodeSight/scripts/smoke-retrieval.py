#!/usr/bin/env python3
"""Retrieval smoke tests for the local Black Duck Code Sight corpus."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = (
    (
        "welcome",
        ROOT / "docs/welcome/welcome-to-code-sight.md",
        ("Code Sight", "source code"),
    ),
    (
        "install-vscode",
        ROOT / "docs/installing/installing-code-sight-in-visual-studio-code.md",
        ("Visual Studio Code",),
    ),
    (
        "authenticate-sca",
        ROOT / "docs/authenticating/to-authenticate-black-duck-sca-within-code-sight.md",
        ("KnowledgeBase", "Black Duck SCA server"),
    ),
    (
        "supported-ides",
        ROOT / "docs/support-matrix/supported-ides.md",
        ("Eclipse", "IntelliJ", "Visual Studio Code"),
    ),
    (
        "release-notes",
        ROOT / "docs/release-notes/code-sight-version-2026-9-0.md",
        ("2026.9.0",),
    ),
    (
        "coverity",
        ROOT / "docs/coverity/coverity-with-code-sight.md",
        ("Coverity",),
    ),
)


def main() -> int:
    failures: list[str] = []
    catalog = (ROOT / "index.md").read_text(encoding="utf-8")
    for name, path, needles in CHECKS:
        if f"]({path.relative_to(ROOT).as_posix()})" not in catalog:
            failures.append(f"{name}: topic is absent from the current index")
        if not path.exists():
            failures.append(f"{name}: missing {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        missing = [needle for needle in needles if needle not in text]
        if missing:
            failures.append(f"{name}: {path.name} missing {missing}")
    if failures:
        print("\n".join(failures))
        return 1
    print("Retrieval smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
