#!/usr/bin/env python3
"""Evaluate production traces without exposing expected facts to the answer path."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluation.core import (  # noqa: E402
    BASELINE_PATH,
    DEFAULT_EQUIVALENTS_PATH,
    EvaluationError,
    aggregate,
    dump_json,
    load_json,
    load_jsonl,
    load_fact_equivalents,
    make_trace,
    revision_hash,
    run_adapter,
    score_case,
    utc_now,
    verify_case_evidence,
)


def percent(value):
    return "NOT MEASURED" if value is None else f"{value * 100:.1f}%"


def render(report: dict) -> str:
    metrics = report["metrics"]
    lines = [
        f"Evaluation: {report['label']}",
        f"Evaluation revision: {report['evaluation_revision']}",
        f"Git revision: {report['git_revision']}",
        f"Corpus/index revision: {report['corpus_revision']}",
        f"Prompt revision: {report['prompt_revision']}",
        f"Model/config: {report['model_config']}",
        "",
        f"Total: {metrics['total_cases']}",
        f"Measured: {metrics['measured_cases']}",
        f"Not measured: {metrics['not_measured_cases']}",
        f"Pass: {metrics['pass']}",
        f"Fail: {metrics['fail']}",
        "",
        "Retrieval:",
        f"  Recall@1: {percent(metrics['retrieval']['recall_at_1'])}",
        f"  Recall@3: {percent(metrics['retrieval']['recall_at_3'])}",
        f"  Recall@5: {percent(metrics['retrieval']['recall_at_5'])}",
        f"  Version accuracy: {percent(metrics['retrieval']['version_accuracy'])}",
        f"  Insufficient-evidence cases: {metrics['retrieval']['insufficient_evidence_cases']}",
        "",
        "Answers:",
        f"  Unsupported claims: {metrics['answers']['unsupported_claims']}",
        f"  Citation failures: {metrics['answers']['citation_failures']}",
        f"  Abstention accuracy: {percent(metrics['answers']['abstention_accuracy'])}",
        "",
        "Failures by class:",
    ]
    if metrics["failures_by_class"]:
        lines.extend(f"  {key}: {value}" for key, value in metrics["failures_by_class"].items())
    else:
        lines.append("  none measured")
    lines.extend(["", "Latency (ms):"])
    for key, value in metrics["latency_ms"].items():
        lines.append(f"  {key}: {'NOT MEASURED' if value is None else round(value, 3)}")
    if report["not_measured_reasons"]:
        lines.extend(["", "NOT MEASURED — reasons:"])
        lines.extend(f"  - {reason}" for reason in report["not_measured_reasons"])
    failures = [item for item in report["case_results"] if item.get("status") == "FAIL"]
    if failures:
        lines.extend(["", "Individual failures:"])
        for item in failures:
            lines.append(f"  {item['case_id']}: {', '.join(item['failures'])}")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=ROOT / "evaluation" / "cases" / "sca-baseline.jsonl")
    parser.add_argument("--case-id", action="append", help="Run only the named case; may be repeated")
    parser.add_argument("--trace-dir", type=Path, help="Read production traces named <case-id>.json")
    parser.add_argument("--adapter", nargs="+", help="Actual production answer command; reads query JSON on stdin and returns trace JSON")
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--include-candidates", action="store_true")
    parser.add_argument("--deterministic-only", action="store_true", help="Validate schema/evidence without claiming live RAG metrics")
    parser.add_argument("--allow-unmeasured", action="store_true", help="Return success while the production adapter is unavailable")
    parser.add_argument("--label", default="BASELINE")
    parser.add_argument("--output", type=Path, default=ROOT / "evaluation" / "results" / "latest.json")
    parser.add_argument("--trace-output", type=Path, default=ROOT / "evaluation" / "traces")
    parser.add_argument(
        "--scoring-equivalents",
        type=Path,
        default=DEFAULT_EQUIVALENTS_PATH,
        help="Human-verified deterministic fact equivalents; use an empty/missing file to disable",
    )
    parser.add_argument("--resume", action="store_true", help="Reuse an existing trace-output file before invoking the adapter")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.trace_dir and args.adapter:
        raise SystemExit("Use either --trace-dir or --adapter, not both")
    baseline = load_json(BASELINE_PATH)
    cases = load_jsonl(args.cases)
    fact_equivalents = load_fact_equivalents(args.scoring_equivalents)
    if not args.include_candidates:
        cases = [case for case in cases if case.get("verification_status") == "verified"]
    if args.case_id:
        selected = set(args.case_id)
        cases = [case for case in cases if case.get("id") in selected]
        missing = sorted(selected - {case.get("id") for case in cases})
        if missing:
            raise SystemExit(f"Unknown or excluded case ID(s): {', '.join(missing)}")
    verification: dict[str, list[str]] = {case.get("id", f"case-{i}"): verify_case_evidence(case) for i, case in enumerate(cases)}
    invalid = {case_id: errors for case_id, errors in verification.items() if errors}
    if invalid:
        for case_id, errors in invalid.items():
            for error in errors:
                print(f"{case_id}: {error}", file=sys.stderr)
        return 1

    results: list[dict] = []
    measured_traces: list[dict] = []
    not_measured_reasons: list[str] = []
    if args.deterministic_only:
        not_measured_reasons.append("deterministic-only mode validates cases and evidence but does not invoke retrieval or generation")
    elif args.trace_dir:
        for case in cases:
            path = args.trace_dir / f"{case['id']}.json"
            if not path.is_file():
                results.append({"case_id": case["id"], "status": "NOT_MEASURED", "reason": f"trace missing: {path}"})
                continue
            trace = load_json(path)
            measured_traces.append(trace)
            results.append(score_case(case, trace, fact_equivalents=fact_equivalents))
    elif args.adapter:
        for position, case in enumerate(cases, start=1):
            existing_trace = args.trace_output / f"{case['id']}.json"
            if args.resume and existing_trace.is_file():
                trace = load_json(existing_trace)
                measured_traces.append(trace)
                results.append(score_case(case, trace, fact_equivalents=fact_equivalents))
                print(f"[{position}/{len(cases)}] {case['id']}: reused {results[-1]['status']}", file=sys.stderr, flush=True)
                continue
            print(f"[{position}/{len(cases)}] {case['id']}: invoking production path", file=sys.stderr, flush=True)
            try:
                raw = run_adapter(args.adapter, case, args.timeout)
                trace = make_trace(case, raw, baseline)
                measured_traces.append(trace)
                dump_json(args.trace_output / f"{case['id']}.json", trace)
                results.append(score_case(case, trace, fact_equivalents=fact_equivalents))
                print(f"[{position}/{len(cases)}] {case['id']}: {results[-1]['status']}", file=sys.stderr, flush=True)
            except (EvaluationError, OSError, TimeoutError) as exc:
                results.append({"case_id": case["id"], "status": "NOT_MEASURED", "reason": str(exc)})
                print(f"[{position}/{len(cases)}] {case['id']}: NOT_MEASURED", file=sys.stderr, flush=True)
    else:
        not_measured_reasons.append("no callable production retrieval/answer adapter or captured production traces were supplied")

    metrics = aggregate(results, len(cases))
    for item in results:
        if item.get("status") == "NOT_MEASURED" and item.get("reason") not in not_measured_reasons:
            not_measured_reasons.append(item["reason"])
    eval_paths = [args.cases, ROOT / "evaluation" / "schema" / "eval-case.schema.json", ROOT / "evaluation" / "core.py", Path(__file__)]
    if args.scoring_equivalents.is_file():
        eval_paths.append(args.scoring_equivalents)
    prompt_revisions = {trace.get("prompt_revision") for trace in measured_traces if trace.get("prompt_revision")}
    model_configs = {
        json.dumps({"model": trace.get("model"), "parameters": trace.get("model_parameters")}, sort_keys=True)
        for trace in measured_traces if trace.get("model")
    }
    effective_prompt_revision = next(iter(prompt_revisions)) if len(prompt_revisions) == 1 else baseline["generation"]["prompt_revision"]
    effective_model_config = json.loads(next(iter(model_configs))) if len(model_configs) == 1 else {
        "model": baseline["generation"]["model"], "parameters": baseline["generation"]["parameters"]
    }
    report = {
        "label": args.label,
        "created_at": utc_now(),
        "evaluation_revision": revision_hash(eval_paths),
        "git_revision": baseline["git"]["sha"],
        "corpus_revision": baseline["baseline_id"],
        "prompt_revision": effective_prompt_revision,
        "model_config": effective_model_config,
        "case_set": str(args.cases.relative_to(ROOT) if args.cases.is_relative_to(ROOT) else args.cases),
        "verified_cases": len(cases),
        "evidence_verification": "PASS",
        "metrics": metrics,
        "not_measured_reasons": not_measured_reasons,
        "case_results": results,
    }
    dump_json(args.output, report)
    print(render(report), end="")
    if metrics["not_measured_cases"] and not args.allow_unmeasured:
        return 2
    return 1 if metrics["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
