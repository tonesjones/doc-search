"""Validate reviewed, sanitized Black Duck SCA live-observation records.

A live-observation record keeps what was seen on a live SCA instance separate
from documentation evidence. Only owner-approved, read-only observations are
committed. Raw observations stay in the ignored `.local/live-observations/`.
"""

from __future__ import annotations

import json
from pathlib import Path

from rbac_case import _check_for_secrets, _unique_ids


REQUIRED_FIELDS = {
    "schema_version",
    "observation_id",
    "title",
    "product",
    "product_version",
    "observation_date",
    "environment",
    "principal",
    "method",
    "review",
    "findings",
    "open_gaps",
}
SURFACES = {"UI", "API"}
MODES = {"READ_ONLY"}
OUTCOMES = {"OBSERVED", "PARTIAL", "NOT_TESTED"}
SCOPES = {"GENERAL", "ENVIRONMENT_SPECIFIC"}
DOC_VERDICTS = {"CONSISTENT", "OUTDATED_LABELS", "MISLEADING", "CONTRADICTED", "NOT_COVERED"}
CASE_FILES = ("evaluation/cases/sca-regressions.jsonl", "evaluation/cases/sca-baseline.jsonl")


def load_observation(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def known_case_ids(repo_root: Path) -> set[str]:
    ids: set[str] = set()
    for relative in CASE_FILES:
        path = repo_root / relative
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                ids.add(json.loads(line)["id"])
    return ids


def validate_observation(record: dict, product_root: Path) -> list[str]:
    failures: list[str] = []
    if not isinstance(record, dict):
        return ["observation root must be an object"]
    missing = REQUIRED_FIELDS - set(record)
    extra = set(record) - REQUIRED_FIELDS
    if missing:
        failures.append(f"missing top-level fields: {', '.join(sorted(missing))}")
    if extra:
        failures.append(f"unexpected top-level fields: {', '.join(sorted(extra))}")
    if missing:
        return failures

    for field in ("environment", "principal", "method", "review"):
        if not isinstance(record[field], dict):
            failures.append(f"{field} must be an object")
    for field in ("findings", "open_gaps"):
        if not isinstance(record[field], list):
            failures.append(f"{field} must be an array")
    if isinstance(record["findings"], list) and not all(isinstance(item, dict) for item in record["findings"]):
        failures.append("every finding must be an object")
    if failures:
        return failures

    if record["schema_version"] != 1:
        failures.append("schema_version must be 1")
    if record["product"] != "Black Duck SCA":
        failures.append("product must be Black Duck SCA")
    if not record["environment"].get("sanitized"):
        failures.append("environment.sanitized must be true")
    if record["environment"].get("customer_data") is not False:
        failures.append("environment.customer_data must be false")
    if record["method"].get("mode") not in MODES:
        failures.append("method.mode must be READ_ONLY")
    if not record["method"].get("mutation_check"):
        failures.append("method.mutation_check must describe how no change was confirmed")
    if record["review"].get("status") != "APPROVED":
        failures.append("review.status must be APPROVED; keep unreviewed observations in .local")
    for key in ("reviewed_by", "reviewed_at"):
        if not record["review"].get(key):
            failures.append(f"review.{key} is required")
    if not record["findings"]:
        failures.append("findings must not be empty")

    _check_for_secrets(record, failures)

    _unique_ids(record["findings"], "finding", failures)
    case_ids = known_case_ids(product_root.parent)
    for finding in record["findings"]:
        finding_id = finding.get("id", "<missing>")
        if not finding.get("statement"):
            failures.append(f"finding {finding_id!r} has no statement")
        if finding.get("surface") not in SURFACES:
            failures.append(f"finding {finding_id!r} has invalid surface")
        if finding.get("outcome") not in OUTCOMES:
            failures.append(f"finding {finding_id!r} has invalid outcome")
        if finding.get("scope") not in SCOPES:
            failures.append(f"finding {finding_id!r} has invalid scope")
        for case_id in finding.get("related_cases", []):
            if case_id not in case_ids:
                failures.append(f"finding {finding_id!r} references unknown case {case_id!r}")
        for comparison in finding.get("documentation", []):
            path = comparison.get("source_path")
            if not path or not (product_root / path).is_file():
                failures.append(f"finding {finding_id!r} references missing source_path {path!r}")
            if comparison.get("verdict") not in DOC_VERDICTS:
                failures.append(f"finding {finding_id!r} has invalid documentation verdict")
    return failures
