#!/usr/bin/env python3
"""Summarize why a saved answer missed one reviewed evaluation case."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.codex_checkout_adapter import verified_excerpt  # noqa: E402
from evaluation.core import EvaluationError  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", type=Path)
    parser.add_argument("saved_answer", type=Path)
    args = parser.parse_args()
    case = json.loads(args.case.read_text(encoding="utf-8"))
    output = json.loads(args.saved_answer.read_text(encoding="utf-8"))
    answer = output["answer"]
    cited = {item["file"] for item in output["citations"]}
    print("Missing answer facts:")
    for fact in case["required_facts"]:
        if fact["value"].casefold() not in answer.casefold():
            print(f"  {fact['value']}")
    print("Missing required sources:")
    for path in case["must_retrieve"]:
        if path not in cited:
            print(f"  {path}")
    print("Invalid source excerpts:")
    for item in output["evidence"]:
        try:
            verified_excerpt((ROOT / item["file"]).read_text(encoding="utf-8"), item["excerpt"], item["file"])
        except EvaluationError:
            print(f"  {item['file']}: {item['excerpt'][:70]!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
