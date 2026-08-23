#!/usr/bin/env python3
"""Fail closed unless the Phase 1 live baseline is complete and reproducible."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=ROOT / "evaluation" / "results" / "baseline.json")
    args = parser.parse_args()
    required_files = [
        ROOT / "ARCHITECTURE.md",
        ROOT / "baseline" / "BASELINE-SNAPSHOT.json",
        ROOT / "evaluation" / "schema" / "eval-case.schema.json",
        ROOT / "evaluation" / "cases" / "sca-baseline.jsonl",
        ROOT / "evaluation" / "core.py",
        ROOT / "scripts" / "evaluate.py",
        ROOT / "scripts" / "trace-answer.py",
        ROOT / "scripts" / "feedback-to-eval.py",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "rag-answer-feedback.yml",
    ]
    failures = [f"missing deliverable: {path.relative_to(ROOT)}" for path in required_files if not path.is_file()]
    if not args.report.is_file():
        failures.append(f"missing baseline result: {args.report}")
    else:
        report = json.loads(args.report.read_text(encoding="utf-8"))
        metrics = report.get("metrics", {})
        if report.get("evidence_verification") != "PASS":
            failures.append("evaluation evidence verification did not pass")
        if metrics.get("measured_cases") != metrics.get("total_cases"):
            failures.append(f"live production path measured {metrics.get('measured_cases', 0)}/{metrics.get('total_cases', 0)} cases")
        retrieval = metrics.get("retrieval", {})
        answers = metrics.get("answers", {})
        for name in ("recall_at_1", "recall_at_3", "recall_at_5", "version_accuracy"):
            if retrieval.get(name) is None:
                failures.append(f"retrieval metric not measured: {name}")
        if answers.get("abstention_accuracy") is None:
            failures.append("answer metric not measured: abstention_accuracy")
        if report.get("prompt_revision") in (None, "not discoverable; installed skill is external to this git tree"):
            failures.append("production prompt revision is not captured")
        model = report.get("model_config", {}).get("model")
        if model in (None, "not discoverable from repository"):
            failures.append("production model revision is not captured")
    print("PHASE 1 GATE: " + ("FAIL" if failures else "PASS"))
    for failure in failures:
        print(f"- {failure}")
    if failures:
        print("Phase 2 remains queued and must not execute.")
        return 2
    print("Phase 2 may proceed without modifying the preserved baseline.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
