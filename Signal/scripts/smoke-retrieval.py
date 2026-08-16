#!/usr/bin/env python3
"""Retrieval smoke tests for the local Black Duck Signal corpus."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = (
    (
        "overview",
        ROOT / "docs/overview/overview-of-black-duck-signal.md",
        ("Signal Developer", "Signal Enterprise", "Black Duck MCP", "Polaris"),
    ),
    (
        "claude",
        ROOT / "docs/scan-changes/with-a-coding-assistant/black-duck-signal-and-claude-code.md",
        ("claude mcp add", "@black-duck/mcp-server", "BLACKDUCK_MCP_GATEWAY_KEY"),
    ),
    (
        "cli-diff",
        ROOT / "docs/scan-changes/from-the-command-line/perform-a-diff-scan.md",
        ("UNCOMMITTED", "BRIDGE_SIGNAL_LLM_KEY", "Bridge CLI"),
    ),
    (
        "polaris",
        ROOT / "docs/scan-project/full-project-scan-and-send-results-to-polaris.md",
        ("BRIDGE_POLARIS_SERVERURL", "BRIDGE_SIGNAL_LLM_KEY", "Signal Enterprise"),
    ),
    (
        "reference",
        ROOT / "docs/reference/reference-guide.md",
        ("BRIDGE_SIGNAL_LLM_KEY", "signal.mode", "UNCOMMITTED", "REFERENCE", "PROJECT"),
    ),
    (
        "ai-security",
        ROOT / "docs/ai-security/ai-security-data-protection-and-trust.md",
        ("LLM Gateway", "data isolation"),
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
    if failures:
        print("\n".join(failures))
        return 1
    print("Retrieval smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
