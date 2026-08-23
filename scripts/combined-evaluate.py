#!/usr/bin/env python3
"""Join Phase 1 RAG signals to Phase 2 runtime signals without collapsing them."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluation.combined import diagnose  # noqa: E402

RUNTIME_TO_EVAL = {
    "sca-runtime-auth": "sca-auth-002",
    "sca-runtime-current-user": "sca-role-001",
    "sca-runtime-isolation-name": "sca-project-003",
    "sca-runtime-project-list": "sca-auth-003",
    "sca-runtime-project-media": "sca-auth-002",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=ROOT / "evaluation" / "results" / "sca-baseline.json")
    parser.add_argument("--runtime", type=Path, default=ROOT / "runtime" / "results" / "sca-runtime.json")
    parser.add_argument("--output", type=Path, default=ROOT / "runtime" / "results" / "combined.json")
    args = parser.parse_args()
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    runtime = json.loads(args.runtime.read_text(encoding="utf-8"))
    rag = {item["case_id"]: item for item in baseline["case_results"]}
    joined = []
    for item in runtime["results"]:
        eval_id = RUNTIME_TO_EVAL[item["validation_id"]]
        failures = rag[eval_id].get("failures", [])
        joined.append({
            "validation_id": item["validation_id"],
            "eval_case_id": eval_id,
            "retrieval_result": "FAIL" if any(name in failures for name in ("RETRIEVAL_FAILURE", "VERSION_FAILURE")) else "PASS",
            "doc_faithfulness_result": "FAIL" if any(name in failures for name in ("SYNTHESIS_FAILURE", "UNSUPPORTED_CLAIM", "ABSTENTION_FAILURE")) else "PASS",
            "corpus_correctness_result": "FAIL" if "VERSION_FAILURE" in failures else "PASS",
            "runtime_validation_result": item["result"],
            "runtime_reason": item.get("reason"),
            "overall_diagnosis": diagnose(failures, item["result"]),
        })
    report = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "baseline_id": baseline["corpus_revision"],
        "environment": runtime["environment"],
        "signals_are_independent": True,
        "results": joined,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
