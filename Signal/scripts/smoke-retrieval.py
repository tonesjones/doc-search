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
        ("Signal Developer", "Signal Enterprise", "Language support"),
    ),
    (
        "claude",
        ROOT / "docs/scan-changes/with-a-coding-assistant/black-duck-signal-and-claude-code.md",
        ("claude mcp add", "@black-duck/mcp-server", "BLACKDUCK_MCP_GATEWAY_KEY"),
    ),
    (
        "bridge-scans",
        ROOT / "docs/get-started/using-bridge-cli-with-signal.md",
        ("Project mode", "Polaris", "SARIF"),
    ),
    (
        "codex",
        ROOT / "docs/get-started/coding-assistants/signal-and-codex-cli.md",
        ("Codex", "BLACKDUCK_MCP_GATEWAY_KEY", "@blackducksoftware/mcp-server"),
    ),
    (
        "reference",
        ROOT / "docs/reference/signal-reference-guide.md",
        ("BYOLLM", "UNCOMMITTED", "REFERENCE", "PROJECT", "Polaris Flags"),
    ),
    (
        "byollm",
        ROOT / "docs/byollm/byollm.md",
        ("Bring Your Own Large Language Model", "Azure", "Vertex AI"),
    ),
    (
        "ai-security",
        ROOT / "docs/ai-security/ai-security-data-protection-and-trust.md",
        ("LLM Gateway", "data isolation"),
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
