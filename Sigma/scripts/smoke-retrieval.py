#!/usr/bin/env python3
"""Retrieval smoke tests for the local Black Duck Sigma corpus."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = (
    (
        "introducing",
        ROOT / "docs/sigma-2026.9.1/sigma-user-guide/introducing-sigma.md",
        ("Rapid Scan Static", "sigma analyze", "sigma checkers", "Polaris", "SARIF"),
    ),
    (
        "analyze",
        ROOT / "docs/sigma-2026.9.1/sigma-user-guide/command-reference/the-analyze-subcommand.md",
        ("--base-check-set", "SIGMA_ANALYZE_OUTPUT_FORMAT", "sigma-results.json", "sarif"),
    ),
    (
        "env-vars",
        ROOT / "docs/sigma-2026.9.1/sigma-user-guide/configuring-sigma/environment-variables.md",
        ("SIGMA_CONFIG_FILE", ".sigma-config.yml", "SIGMA_NUM_THREADS", "SIGMA_ENABLE"),
    ),
    (
        "languages",
        ROOT / "docs/sigma-2026.9.1/sigma-user-guide/sigma-support-matrix/language-and-framework-support.md",
        ("Java", "Terraform", "Dart", "Infrastructure as Code"),
    ),
    (
        "policies",
        ROOT / "docs/sigma-2026.9.1/sigma-user-guide/running-sigma-in-ci-cd/using-policies-to-define-a-quality-gate.md",
        (".sigma-policy.yml", "--policy", "quality gate"),
    ),
    (
        "ai-plugin",
        ROOT
        / "docs/sigma-2026.9.1/sigma-user-guide/configuring-sigma/configuring-the-ai-augmented-sast-checker-plug-in.md",
        ("SIGMA_XX_LLM_URL", "SIGMA_XX_LLM_API_KEY", "Anthropic"),
    ),
    (
        "checkers-pointer",
        ROOT / "docs/sigma-2026.9.1/sigma-user-guide/sigma-checkers.md",
        ("sigma_checker_latest-en", "Open Sigma Checkers"),
    ),
    (
        "release-notes-pointer",
        ROOT / "docs/sigma-2026.9.1/sigma-user-guide/release-notes.md",
        ("sigma_release_notes", "Open the release notes"),
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
