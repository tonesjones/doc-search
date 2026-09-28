#!/usr/bin/env python3
"""Fail-closed promotion of one reviewed feedback candidate into SCA regressions."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluation.core import (  # noqa: E402
    EvaluationError,
    load_fact_equivalents,
    load_json,
    load_jsonl,
    score_case,
    verify_case_evidence,
)
from evaluation.profile import DEFAULT_PROFILE_PATH, load_profile, profile_metadata  # noqa: E402
from scripts.codex_checkout_adapter import prompt_revision  # noqa: E402


def load_records(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return load_jsonl(path)
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list) and all(isinstance(item, dict) for item in value):
        return value
    raise EvaluationError(f"{path}: expected a JSON object, array, or JSONL objects")


def promotion_errors(
    candidate: dict, approved: dict, trace: dict, expected_provenance: dict,
    companion_versions: dict[str, str] | None = None,
) -> list[str]:
    errors: list[str] = []
    if candidate.get("verification_status") != "candidate":
        errors.append("source record is not an untrusted candidate")
    if candidate.get("origin") != "team-feedback":
        errors.append("source candidate is not team feedback")
    if approved.get("verification_status") != "verified":
        errors.append("approved case is not marked verified")
    if not isinstance(approved.get("verified_by"), str) or not approved["verified_by"].strip():
        errors.append("approved case has no human/source verifier")
    if approved.get("origin") != "team-feedback":
        errors.append("approved case must retain team-feedback origin")
    if candidate.get("id") != approved.get("id"):
        errors.append("candidate and approved case IDs differ")
    if not isinstance(approved.get("product_version"), str) or not approved["product_version"].strip():
        errors.append("approved case has no explicit product_version")
    for field in ("question", "product", "product_version"):
        if candidate.get(field) != approved.get(field):
            errors.append(f"candidate and approved case differ on {field}")
    if trace.get("original_query") != approved.get("question"):
        errors.append("production trace question does not match approved case")
    if trace.get("product") != approved.get("product"):
        errors.append("production trace product does not match approved case")
    if trace.get("requested_product_version") != approved.get("product_version"):
        errors.append("production trace requested product version does not match approved case")
    if trace.get("entrypoint") != expected_provenance.get("entrypoint"):
        errors.append("production trace entrypoint does not match evaluation profile")
    if not isinstance(trace.get("model"), str) or not trace["model"].strip():
        errors.append("production trace has no model")
    if not isinstance(trace.get("model_parameters"), dict):
        errors.append("production trace has no model parameters")
    errors.extend(verify_case_evidence(approved))
    result = score_case(
        approved,
        trace,
        fact_equivalents=load_fact_equivalents(),
        expected_provenance=expected_provenance,
        companion_versions=companion_versions,
    )
    if result["status"] != "PASS":
        errors.append("production replay did not pass: " + ", ".join(result["failures"] or ["unmeasured facts"]))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, type=Path, help="Candidate JSON or JSONL file")
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--approved-case", required=True, type=Path, help="Human-completed verified eval case JSON")
    parser.add_argument("--trace", required=True, type=Path, help="Production replay trace JSON")
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE_PATH, help="Evaluation profile used for the production replay")
    parser.add_argument("--output", type=Path, default=ROOT / "evaluation" / "cases" / "sca-regressions.jsonl")
    parser.add_argument("--apply", action="store_true", help="Append after every promotion gate passes")
    args = parser.parse_args()

    matches = [item for item in load_records(args.candidate) if item.get("id") == args.candidate_id]
    if len(matches) != 1:
        parser.error(f"expected exactly one candidate with id {args.candidate_id}, found {len(matches)}")
    candidate = matches[0]
    approved = load_json(args.approved_case)
    trace = load_json(args.trace)
    profile = load_profile(args.profile)
    if profile["product"] != "blackduck-sca":
        parser.error("DS-08 promotion requires a Black Duck SCA evaluation profile")
    expected_provenance = profile_metadata(profile)
    expected_provenance["prompt_revision"] = prompt_revision(profile)
    errors = promotion_errors(
        candidate, approved, trace, expected_provenance, profile.get("companion_evidence_versions"),
    )
    if approved.get("product") != profile["product"]:
        errors.append("approved case product does not match evaluation profile")
    if errors:
        print("PROMOTION GATE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    existing = {item.get("id") for item in load_jsonl(args.output)} if args.output.is_file() else set()
    if approved["id"] in existing:
        print("PROMOTION GATE: FAIL")
        print(f"- regression id already exists: {approved['id']}")
        return 1
    if not args.apply:
        print("PROMOTION GATE: PASS (dry run; use --apply to append the verified case)")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(approved, ensure_ascii=False) + "\n")
    print(f"PROMOTION GATE: PASS (promoted {approved['id']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
