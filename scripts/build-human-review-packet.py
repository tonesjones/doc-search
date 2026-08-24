#!/usr/bin/env python3
"""Build a human-review packet from preserved cases, results, and answer traces."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

VERDICTS = (
    "TRUE_PASS",
    "FALSE_PASS",
    "TRUE_FAILURE",
    "SCORING_FALSE_NEGATIVE",
    "BENCHMARK_NEEDS_REVISION",
    "NEEDS_PRODUCT_EXPERT",
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: expected a JSON object")
        values.append(value)
    return values


def dump_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = "\n".join(json.dumps(value, ensure_ascii=False, separators=(",", ":")) for value in values) + "\n"
    path.write_text(encoded, encoding="utf-8")


def blank_adjudication(case_id: str) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "review_status": "UNREVIEWED",
        "verdict": None,
        "reviewer": None,
        "reviewed_at": None,
        "correctness": None,
        "scope": None,
        "evidence_support": None,
        "version_handling": None,
        "citation_quality": None,
        "notes": "",
    }


def load_or_initialize_adjudications(path: Path, cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    existing = load_jsonl(path) if path.is_file() else []
    by_id: dict[str, dict[str, Any]] = {}
    for item in existing:
        case_id = item.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            raise ValueError(f"{path}: adjudication missing case_id")
        if case_id in by_id:
            raise ValueError(f"{path}: duplicate adjudication for {case_id}")
        if item.get("verdict") not in (None, *VERDICTS):
            raise ValueError(f"{path}: invalid verdict for {case_id}")
        by_id[case_id] = item

    case_ids = {case["id"] for case in cases}
    unknown = sorted(set(by_id) - case_ids)
    if unknown:
        raise ValueError(f"{path}: adjudications reference unknown cases: {', '.join(unknown)}")

    ordered = [by_id.get(case["id"], blank_adjudication(case["id"])) for case in cases]
    dump_jsonl(path, ordered)
    return ordered


def repo_link(file_name: str) -> str:
    return f"[{file_name}](<../../{file_name}>)"


def fact_text(fact: dict[str, Any]) -> str:
    sensitivity = "case-sensitive" if fact.get("case_sensitive") else "case-insensitive"
    return f"`{fact.get('value', '')}` ({fact.get('type', 'UNKNOWN')}, {sensitivity})"


def list_or_none(values: list[str]) -> list[str]:
    return values or ["None"]


def fenced(value: str) -> list[str]:
    return ["~~~~text", value.rstrip(), "~~~~"]


def build_packet(
    cases: list[dict[str, Any]],
    report: dict[str, Any],
    traces: dict[str, dict[str, Any]],
    adjudications: list[dict[str, Any]],
) -> str:
    results = {item["case_id"]: item for item in report.get("case_results", [])}
    reviews = {item["case_id"]: item for item in adjudications}
    missing_results = [case["id"] for case in cases if case["id"] not in results]
    missing_traces = [case["id"] for case in cases if case["id"] not in traces]
    if missing_results or missing_traces:
        raise ValueError(
            "packet inputs are incomplete; "
            f"missing results={missing_results or 'none'}, missing traces={missing_traces or 'none'}"
        )

    status_counts = Counter(results[case["id"]].get("status", "UNKNOWN") for case in cases)
    failure_counts = Counter(
        failure
        for case in cases
        for failure in results[case["id"]].get("failures", [])
    )
    reviewed = sum(1 for item in adjudications if item.get("review_status") == "REVIEWED")
    generated = datetime.now(timezone.utc).isoformat()

    lines = [
        "# SCA baseline human-review packet",
        "",
        f"Generated: `{generated}`  ",
        f"Cases: **{len(cases)}** · machine pass: **{status_counts['PASS']}** · machine fail: **{status_counts['FAIL']}** · human reviewed: **{reviewed}/{len(cases)}**",
        "",
        "This packet is derived from the preserved SCA baseline, its production traces, and its machine report. It does not modify the baseline. The machine-readable human decisions belong in `sca-baseline-adjudications.jsonl`.",
        "",
        "## Review method",
        "",
        "1. Complete **Pass A** from the customer-visible question and answer before opening the evidence details.",
        "2. Judge correctness, requested scope, clarity, and whether the answer abstained when it should have.",
        "3. Open **Pass B** and compare the answer with the version-matched evidence, citations, retrieval, and machine scoring.",
        "4. Record exactly one verdict in the companion JSONL: `TRUE_PASS`, `FALSE_PASS`, `TRUE_FAILURE`, `SCORING_FALSE_NEGATIVE`, `BENCHMARK_NEEDS_REVISION`, or `NEEDS_PRODUCT_EXPERT`.",
        "5. Set `review_status` to `REVIEWED`, add the reviewer and review time, and explain every verdict except an obvious `TRUE_PASS`.",
        "",
        "Do not change expected facts during review. If the benchmark is wrong or overly literal, use `BENCHMARK_NEEDS_REVISION` or `SCORING_FALSE_NEGATIVE`; preserve the original case until that decision is reviewed separately.",
        "",
        "## Machine summary",
        "",
        "| Result | Count |",
        "|---|---:|",
        f"| PASS | {status_counts['PASS']} |",
        f"| FAIL | {status_counts['FAIL']} |",
        "",
        "| Failure class | Count |",
        "|---|---:|",
    ]
    lines.extend(f"| {name} | {count} |" for name, count in sorted(failure_counts.items()))
    lines.extend([
        "",
        "## Review queue",
        "",
        "| # | Case | Machine | Failures | Human verdict |",
        "|---:|---|---|---|---|",
    ])
    for index, case in enumerate(cases, 1):
        result = results[case["id"]]
        review = reviews[case["id"]]
        failures = ", ".join(result.get("failures", [])) or "—"
        verdict = review.get("verdict") or "UNREVIEWED"
        lines.append(
            f"| {index} | [`{case['id']}`](#case-{case['id']}) | {result.get('status', 'UNKNOWN')} | {failures} | {verdict} |"
        )
    lines.extend(["", "## Cases", ""])

    for index, case in enumerate(cases, 1):
        case_id = case["id"]
        result = results[case_id]
        trace = traces[case_id]
        review = reviews[case_id]
        verdict = review.get("verdict") or "UNREVIEWED"
        lines.extend([
            f"<a id=\"case-{case_id}\"></a>",
            "",
            f"### {index}. `{case_id}` — machine {result.get('status', 'UNKNOWN')}",
            "",
            f"Human review: **{verdict}** · status: `{review.get('review_status', 'UNREVIEWED')}`",
            "",
            "#### Pass A — customer view",
            "",
            f"**Question:** {case['question']}",
            "",
            f"**Requested product/version:** `{case.get('product')}` / `{case.get('product_version', 'unspecified')}`",
            "",
            f"**Answer ID:** `{trace.get('answer_id', result.get('answer_id', 'missing'))}`",
            "",
            "**Production answer:**",
            "",
            *fenced(str(trace.get("answer", ""))),
            "",
            "**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.",
            "",
            "<details>",
            "<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>",
            "",
            f"**Expected behavior:** `{case.get('expected_behavior')}`",
            "",
            "**Required facts:**",
            "",
        ])
        lines.extend(f"- {value}" for value in list_or_none([fact_text(fact) for fact in case.get("required_facts", [])]))
        lines.extend(["", "**Forbidden facts:**", ""])
        lines.extend(f"- {value}" for value in list_or_none([fact_text(fact) for fact in case.get("forbidden_facts", [])]))
        lines.extend(["", "**Authoritative evidence:**", ""])
        evidence_values = [
            f"{repo_link(item['file'])} — section `{item['section']}` — corpus `{item['corpus_revision']}`"
            for item in case.get("source_evidence", [])
        ]
        lines.extend(f"- {value}" for value in list_or_none(evidence_values))
        lines.extend(["", "**Citations emitted by the answer:**", ""])
        citation_values = [repo_link(item["file"]) for item in trace.get("citations", []) if isinstance(item, dict) and item.get("file")]
        lines.extend(f"- {value}" for value in list_or_none(citation_values))
        lines.extend(["", "**Top retrieved files:**", ""])
        retrieved_values = [
            f"rank {item.get('rank', '?')}: {repo_link(item['file'])} — version `{item.get('metadata', {}).get('version', 'unknown')}`"
            for item in trace.get("retrieved_chunks", [])[:5]
            if isinstance(item, dict) and item.get("file")
        ]
        lines.extend(f"- {value}" for value in list_or_none(retrieved_values))
        lines.extend([
            "",
            f"**Machine failures:** `{', '.join(result.get('failures', [])) or 'none'}`",
            "",
            f"**Recall@1/3/5:** `{result.get('recall_at', {}).get('1', 0)}` / `{result.get('recall_at', {}).get('3', 0)}` / `{result.get('recall_at', {}).get('5', 0)}`",
            "",
            f"**Version accuracy:** `{result.get('version_accuracy')}`",
            "",
            "**Machine fact results:**",
            "",
        ])
        fact_results = result.get("fact_results", [])
        if fact_results:
            for item in fact_results:
                marker = "forbidden" if item.get("forbidden") else "required"
                lines.append(f"- `{item.get('result')}` {marker}: {fact_text(item.get('fact', {}))}")
        else:
            lines.append("- None")
        lines.extend([
            "",
            "**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.",
            "",
            "</details>",
            "",
            "---",
            "",
        ])

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=ROOT / "evaluation" / "cases" / "sca-baseline.jsonl")
    parser.add_argument("--report", type=Path, default=ROOT / "evaluation" / "results" / "sca-baseline.json")
    parser.add_argument("--trace-dir", type=Path, default=ROOT / "evaluation" / "traces" / "sca-baseline")
    parser.add_argument("--output", type=Path, default=ROOT / "evaluation" / "reviews" / "sca-baseline-human-review.md")
    parser.add_argument("--adjudications", type=Path, default=ROOT / "evaluation" / "reviews" / "sca-baseline-adjudications.jsonl")
    args = parser.parse_args()

    cases = load_jsonl(args.cases)
    report = load_json(args.report)
    traces = {case["id"]: load_json(args.trace_dir / f"{case['id']}.json") for case in cases}
    adjudications = load_or_initialize_adjudications(args.adjudications, cases)
    packet = build_packet(cases, report, traces, adjudications)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(packet, encoding="utf-8")
    print(f"Wrote {len(cases)} cases to {args.output}")
    print(f"Adjudications: {args.adjudications}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
