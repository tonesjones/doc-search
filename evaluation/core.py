from __future__ import annotations

import hashlib
import json
import re
import subprocess
import time
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "baseline" / "BASELINE-SNAPSHOT.json"
EXPECTED_BEHAVIORS = {"answer", "abstain", "surface_conflict", "version_caveat"}
FACT_TYPES = {"EXACT_FACT", "SEMANTIC_FACT"}
FAILURE_CLASSES = {
    "RETRIEVAL_FAILURE", "INSUFFICIENT_EVIDENCE", "CHUNKING_FAILURE",
    "RANKING_FAILURE", "METADATA_FAILURE", "VERSION_FAILURE",
    "QUERY_UNDERSTANDING_FAILURE", "MISSING_DOCUMENTATION",
    "CONFLICTING_DOCUMENTATION", "SYNTHESIS_FAILURE", "CITATION_FAILURE",
    "UNSUPPORTED_CLAIM", "ABSTENTION_FAILURE",
}
ABSTENTION_RE = re.compile(
    r"\b(does not establish|do not establish|not documented|documentation (?:is|was) silent|"
    r"cannot determine|can't determine|insufficient (?:documentation|evidence)|unable to determine)\b",
    re.IGNORECASE,
)
SENSITIVE_KEY_RE = re.compile(
    r"(^|_)(authorization|password|passwd|secret|api_?key|access_?token|refresh_?token|cookie|session)(_|$)",
    re.IGNORECASE,
)
BEARER_RE = re.compile(r"(?i)(\bBearer\s+)[A-Za-z0-9._~+/=-]+")
ASSIGNMENT_SECRET_RE = re.compile(
    r"(?i)(\b[A-Z0-9_]*(?:PASSWORD|PASSWD|TOKEN|API_KEY|ACCESS_KEY|SECRET|COOKIE)[A-Z0-9_]*\s*=\s*)([^\s,;]+)"
)


class EvaluationError(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def redact_text(value: str) -> str:
    value = BEARER_RE.sub(r"\1[REDACTED]", value)
    return ASSIGNMENT_SECRET_RE.sub(r"\1[REDACTED]", value)


def redact(value: Any, key: str = "") -> Any:
    if SENSITIVE_KEY_RE.search(key):
        return "[REDACTED]"
    if isinstance(value, dict):
        return {str(child_key): redact(child_value, str(child_key)) for child_key, child_value in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, str):
        return redact_text(value)
    return value


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise EvaluationError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(item, dict):
            raise EvaluationError(f"{path}:{line_number}: expected an object")
        cases.append(item)
    return cases


def dump_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def validate_case(case: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "id", "question", "product", "expected_behavior", "must_retrieve",
        "should_retrieve", "must_not_retrieve", "required_facts", "forbidden_facts",
        "source_evidence", "verification_status", "verified_by", "origin", "notes",
    }
    missing = sorted(required - case.keys())
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
    if case.get("expected_behavior") not in EXPECTED_BEHAVIORS:
        errors.append("invalid expected_behavior")
    if case.get("verification_status") not in {"candidate", "verified", "rejected"}:
        errors.append("invalid verification_status")
    for field in ("must_retrieve", "should_retrieve", "must_not_retrieve", "required_facts", "forbidden_facts", "source_evidence"):
        if field in case and not isinstance(case[field], list):
            errors.append(f"{field} must be a list")
    for field in ("required_facts", "forbidden_facts"):
        for index, fact in enumerate(case.get(field, [])):
            if not isinstance(fact, dict) or fact.get("type") not in FACT_TYPES or not isinstance(fact.get("value"), str) or not fact.get("value"):
                errors.append(f"{field}[{index}] is invalid")
    for index, evidence in enumerate(case.get("source_evidence", [])):
        if not isinstance(evidence, dict) or not all(isinstance(evidence.get(k), str) and evidence.get(k) for k in ("file", "section", "corpus_revision")):
            errors.append(f"source_evidence[{index}] is invalid")
    return errors


def _contains(text: str, value: str, case_sensitive: bool = False) -> bool:
    flags = 0 if case_sensitive else re.IGNORECASE
    if re.fullmatch(r"[A-Za-z0-9_.-]+", value):
        pattern = rf"(?<![A-Za-z0-9_]){re.escape(value)}(?![A-Za-z0-9_])"
        return re.search(pattern, text, flags) is not None
    if case_sensitive:
        return value in text
    return value.casefold() in text.casefold()


def verify_case_evidence(case: dict[str, Any], root: Path = ROOT) -> list[str]:
    """Verify only deterministic evidence properties; never infer product facts."""
    errors = validate_case(case)
    source_texts: list[str] = []
    for evidence in case.get("source_evidence", []):
        path = root / evidence["file"]
        try:
            resolved = path.resolve()
            resolved.relative_to(root.resolve())
        except (OSError, ValueError):
            errors.append(f"evidence escapes repository: {evidence['file']}")
            continue
        if not path.is_file():
            errors.append(f"evidence file missing: {evidence['file']}")
            continue
        text = path.read_text(encoding="utf-8")
        source_texts.append(text)
        section = evidence["section"]
        if section not in text:
            errors.append(f"section not found in {evidence['file']}: {section}")
    joined = "\n".join(source_texts)
    if case.get("expected_behavior") != "abstain":
        for fact in case.get("required_facts", []):
            if fact["type"] == "EXACT_FACT" and not _contains(joined, fact["value"], fact.get("case_sensitive", False)):
                errors.append(f"required exact fact absent from evidence: {fact['value']}")
    for pattern in case.get("must_retrieve", []):
        if not (root / pattern).is_file():
            errors.append(f"must_retrieve path missing: {pattern}")
    return errors


def revision_hash(paths: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda p: p.as_posix()):
        digest.update(path.as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def adapter_payload(case: dict[str, Any]) -> dict[str, Any]:
    """Deliberately excludes eval ID, expected behavior, facts, and evidence."""
    return {
        "question": case["question"],
        "product": case["product"],
        "product_version": case.get("product_version"),
    }


def run_adapter(command: list[str], case: dict[str, Any], timeout_seconds: float) -> dict[str, Any]:
    started = time.perf_counter()
    completed = subprocess.run(
        command,
        input=json.dumps(adapter_payload(case)),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
    )
    latency_ms = round((time.perf_counter() - started) * 1000, 3)
    if completed.returncode != 0:
        raise EvaluationError(f"production adapter exited {completed.returncode}: {redact_text(completed.stderr.strip())}")
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise EvaluationError("production adapter did not return one JSON object on stdout") from exc
    if not isinstance(result, dict) or not isinstance(result.get("answer"), str):
        raise EvaluationError("production adapter result must contain string field 'answer'")
    result.setdefault("latency_ms", latency_ms)
    return result


def make_trace(case: dict[str, Any], result: dict[str, Any], baseline: dict[str, Any]) -> dict[str, Any]:
    trace = redact(dict(result))
    trace.setdefault("answer_id", f"ans-{uuid.uuid4().hex}")
    trace.setdefault("timestamp", utc_now())
    trace["original_query"] = redact_text(case["question"])
    trace.setdefault("processed_query", None)
    trace["product"] = case["product"]
    trace["requested_product_version"] = case.get("product_version")
    trace.setdefault("retrieved_chunks", [])
    trace.setdefault("citations", [])
    trace.setdefault("model", None)
    trace.setdefault("model_parameters", None)
    trace.setdefault("prompt_revision", baseline["generation"]["prompt_revision"])
    trace.setdefault("corpus_revision", baseline["baseline_id"])
    trace.setdefault("index_revision", baseline["retrieval"]["index_revision"])
    return trace


def validate_trace(trace: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("answer_id", "timestamp", "original_query", "product", "answer"):
        if not isinstance(trace.get(field), str) or not trace.get(field):
            errors.append(f"trace missing string {field}")
    if not isinstance(trace.get("retrieved_chunks", []), list):
        errors.append("retrieved_chunks must be a list")
    if not isinstance(trace.get("citations", []), list):
        errors.append("citations must be a list")
    return errors


def _chunk_file(chunk: Any) -> str | None:
    if isinstance(chunk, str):
        return chunk.replace("\\", "/")
    if isinstance(chunk, dict) and isinstance(chunk.get("file"), str):
        return chunk["file"].replace("\\", "/")
    return None


def _matches(path: str, expected: str) -> bool:
    path = path.replace("\\", "/").casefold()
    expected = expected.replace("\\", "/").casefold()
    return path == expected or path.endswith("/" + expected)


def score_case(case: dict[str, Any], trace: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    failures: list[str] = []
    trace_errors = validate_trace(trace)
    if trace_errors:
        failures.append("METADATA_FAILURE")

    chunks = trace.get("retrieved_chunks", [])
    files = [path for path in (_chunk_file(chunk) for chunk in chunks) if path]
    must = case.get("must_retrieve", [])
    recall: dict[str, float | None] = {}
    for k in (1, 3, 5):
        if not must:
            recall[str(k)] = None
        else:
            hits = sum(any(_matches(path, expected) for path in files[:k]) for expected in must)
            recall[str(k)] = hits / len(must)
    missing_sources = [expected for expected in must if not any(_matches(path, expected) for path in files)]
    if missing_sources:
        failures.append("RETRIEVAL_FAILURE")

    must_not_violations = [expected for expected in case.get("must_not_retrieve", []) if any(_matches(path, expected) for path in files)]
    if must_not_violations:
        failures.append("RETRIEVAL_FAILURE")

    version_accuracy: bool | None = None
    requested = case.get("product_version")
    if requested:
        relevant_chunks = [
            chunk for chunk in chunks
            if isinstance(chunk, dict)
            and (not must or any(_matches(_chunk_file(chunk) or "", expected) for expected in must))
        ]
        versions = [chunk.get("metadata", {}).get("version") for chunk in relevant_chunks]
        versions = [str(value) for value in versions if value is not None]
        if versions:
            version_accuracy = all(value == requested for value in versions)
            if not version_accuracy:
                failures.append("VERSION_FAILURE")

    answer = trace.get("answer", "")
    fact_results: list[dict[str, Any]] = []
    context = "\n".join(str(chunk.get("content", "")) for chunk in chunks if isinstance(chunk, dict))
    for fact in case.get("required_facts", []):
        if fact["type"] == "SEMANTIC_FACT":
            fact_results.append({"fact": fact, "result": "NOT_MEASURED", "reason": "semantic evaluator not configured"})
            continue
        in_answer = _contains(answer, fact["value"], fact.get("case_sensitive", False))
        in_context = _contains(context, fact["value"], fact.get("case_sensitive", False)) if context else None
        fact_results.append({"fact": fact, "result": "PASS" if in_answer else "FAIL", "in_context": in_context})
        if not in_answer:
            failures.append("INSUFFICIENT_EVIDENCE" if in_context is False and not missing_sources else "SYNTHESIS_FAILURE")
    for fact in case.get("forbidden_facts", []):
        if fact["type"] == "SEMANTIC_FACT":
            fact_results.append({"fact": fact, "result": "NOT_MEASURED", "reason": "semantic evaluator not configured"})
            continue
        absent = not _contains(answer, fact["value"], fact.get("case_sensitive", False))
        fact_results.append({"fact": fact, "result": "PASS" if absent else "FAIL", "forbidden": True})
        if not absent:
            failures.append("UNSUPPORTED_CLAIM")

    abstained = bool(ABSTENTION_RE.search(answer))
    abstention_result: bool | None = None
    if case["expected_behavior"] == "abstain":
        abstention_result = abstained
        if not abstained:
            failures.extend(["ABSTENTION_FAILURE", "UNSUPPORTED_CLAIM"])
    elif abstained:
        abstention_result = False
        failures.append("ABSTENTION_FAILURE")
    if case["expected_behavior"] == "surface_conflict" and not re.search(r"\b(conflict|inconsistent|disagree|different)\b", answer, re.IGNORECASE):
        failures.append("SYNTHESIS_FAILURE")

    retrieved_set = {path.replace("\\", "/").casefold() for path in files}
    citation_errors: list[str] = []
    if case["expected_behavior"] != "abstain" and must and not trace.get("citations"):
        citation_errors.append("answer has no citation")
    for citation in trace.get("citations", []):
        file = citation.get("file") if isinstance(citation, dict) else citation
        if not isinstance(file, str):
            citation_errors.append("citation has no file")
            continue
        normalized = file.replace("\\", "/").casefold()
        if not any(_matches(path, file) for path in retrieved_set):
            citation_errors.append(f"citation not retrieved: {file}")
        if not (root / file).is_file():
            citation_errors.append(f"citation missing from corpus: {file}")
    if citation_errors:
        failures.append("CITATION_FAILURE")

    failures = sorted(set(failures))
    measured_fact_failures = [item for item in fact_results if item["result"] == "FAIL"]
    return {
        "case_id": case["id"],
        "answer_id": trace.get("answer_id"),
        "status": "PASS" if not failures and not measured_fact_failures else "FAIL",
        "recall_at": recall,
        "must_retrieve_missing": missing_sources,
        "must_not_retrieve_violations": must_not_violations,
        "version_accuracy": version_accuracy,
        "fact_results": fact_results,
        "abstention_result": abstention_result,
        "citation_errors": citation_errors,
        "failures": failures,
        "trace_errors": trace_errors,
        "latency_ms": trace.get("latency_ms"),
    }


def aggregate(results: list[dict[str, Any]], total_cases: int) -> dict[str, Any]:
    measured = [item for item in results if item.get("status") in {"PASS", "FAIL"}]
    recalls: dict[str, float | None] = {}
    for k in ("1", "3", "5"):
        values = [item["recall_at"][k] for item in measured if item["recall_at"][k] is not None]
        recalls[k] = sum(values) / len(values) if values else None
    versions = [item["version_accuracy"] for item in measured if item["version_accuracy"] is not None]
    abstentions = [item["abstention_result"] for item in measured if item["abstention_result"] is not None]
    latencies = [float(item["latency_ms"]) for item in measured if isinstance(item.get("latency_ms"), (int, float))]
    classes = Counter(failure for item in measured for failure in item["failures"])
    return {
        "total_cases": total_cases,
        "measured_cases": len(measured),
        "not_measured_cases": total_cases - len(measured),
        "pass": sum(item["status"] == "PASS" for item in measured),
        "fail": sum(item["status"] == "FAIL" for item in measured),
        "retrieval": {
            "recall_at_1": recalls["1"],
            "recall_at_3": recalls["3"],
            "recall_at_5": recalls["5"],
            "version_accuracy": sum(versions) / len(versions) if versions else None,
            "insufficient_evidence_cases": classes["INSUFFICIENT_EVIDENCE"],
        },
        "answers": {
            "unsupported_claims": classes["UNSUPPORTED_CLAIM"],
            "citation_failures": classes["CITATION_FAILURE"],
            "abstention_accuracy": sum(abstentions) / len(abstentions) if abstentions else None,
        },
        "failures_by_class": dict(sorted(classes.items())),
        "latency_ms": {
            "mean": sum(latencies) / len(latencies) if latencies else None,
            "min": min(latencies) if latencies else None,
            "max": max(latencies) if latencies else None,
        },
    }
