#!/usr/bin/env python3
"""Convert one answer feedback record into an untrusted candidate eval case."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluation.core import load_json, utc_now  # noqa: E402


def find_trace(answer_id: str, trace_dir: Path) -> dict:
    direct = trace_dir / f"{answer_id}.json"
    candidates = [direct] if direct.is_file() else list(trace_dir.rglob("*.json")) if trace_dir.is_dir() else []
    for path in candidates:
        trace = load_json(path)
        if trace.get("answer_id") == answer_id:
            return trace
    raise FileNotFoundError(f"no trace found for answer_id {answer_id} under {trace_dir}")


def build_candidate(feedback: dict, trace: dict, feedback_id: str) -> dict:
    suggested_source = feedback.get("suggested_source")
    evidence = []
    if isinstance(suggested_source, str) and suggested_source:
        evidence.append({"file": suggested_source, "section": "NEEDS_VERIFICATION", "corpus_revision": trace.get("corpus_revision", "NEEDS_VERIFICATION")})
    return {
        "id": f"feedback-{feedback_id}",
        "question": trace["original_query"],
        "product": trace["product"],
        "product_version": trace.get("requested_product_version"),
        "expected_behavior": feedback.get("suggested_expected_behavior", "answer"),
        "must_retrieve": [],
        "should_retrieve": [suggested_source] if isinstance(suggested_source, str) and suggested_source else [],
        "must_not_retrieve": [],
        "required_facts": [],
        "forbidden_facts": [],
        "source_evidence": evidence,
        "verification_status": "candidate",
        "verified_by": None,
        "origin": "team-feedback",
        "runtime_classification": "UNCLASSIFIED",
        "notes": " | ".join(
            value for value in [
                f"answer_id={trace['answer_id']}",
                f"category={feedback.get('category', 'Other')}",
                f"comment={feedback.get('comment', '')}",
                f"suggested_correction={feedback.get('suggested_correction', '')}",
                f"converted_at={utc_now()}",
            ] if value
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feedback", type=Path, help="JSON export containing answer_id, category, and comment")
    parser.add_argument("--feedback-id", help="Stable issue/feedback identifier; defaults to input stem")
    parser.add_argument("--trace-dir", type=Path, default=ROOT / "evaluation" / "traces")
    parser.add_argument("--output", type=Path, default=ROOT / "feedback" / "candidates" / "candidates.jsonl")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    feedback = load_json(args.feedback)
    answer_id = feedback.get("answer_id")
    if not isinstance(answer_id, str) or not answer_id:
        parser.error("feedback JSON must contain a non-empty answer_id")
    feedback_id = args.feedback_id or args.feedback.stem
    candidate = build_candidate(feedback, find_trace(answer_id, args.trace_dir), feedback_id)
    encoded = json.dumps(candidate, ensure_ascii=False)
    if args.dry_run:
        print(json.dumps(candidate, indent=2, ensure_ascii=False))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    existing_ids = set()
    if args.output.is_file():
        for line in args.output.read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing_ids.add(json.loads(line).get("id"))
    if candidate["id"] in existing_ids:
        raise SystemExit(f"candidate {candidate['id']} already exists in {args.output}")
    with args.output.open("a", encoding="utf-8") as handle:
        handle.write(encoded + "\n")
    print(args.output)
    print(candidate["id"])
    print("verification_status=candidate; human/source verification is required before promotion")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
