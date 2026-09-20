"""Validate sanitized Black Duck SCA RBAC evidence cases."""

from __future__ import annotations

import json
import re
from pathlib import Path


REQUIRED_FIELDS = {
    "schema_version",
    "case_id",
    "title",
    "product",
    "product_version",
    "observation_date",
    "environment",
    "principals",
    "role_assignments",
    "resources",
    "evidence",
    "scenarios",
    "claims",
    "open_gaps",
    "restoration",
}
SURFACES = {"UI", "API", "MCP", "DETECT"}
EXPECTATIONS = {"ALLOW", "DENY"}
OUTCOMES = {"OBSERVED_SUCCESS", "OBSERVED_DENIAL", "DOCUMENTED_EXPECTATION", "NOT_TESTED"}
SECRET_KEYS = {"password", "token", "api_token", "access_token", "authorization", "cookie", "secret"}
SECRET_PATTERNS = (
    re.compile(r"(?i)\b(?:password|api[ _-]?token|access[ _-]?token|authorization|cookie|secret)\b\s*[:=]"),
    re.compile(r"(?i)\bbearer\s+[a-z0-9._~+/=-]{12,}"),
    re.compile(r"https?://[^/\s]*\.(?:poc|customer)\.[^/\s]+", re.IGNORECASE),
)


def load_case(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_case(case: dict, product_root: Path) -> list[str]:
    failures: list[str] = []
    if not isinstance(case, dict):
        return ["case root must be an object"]
    missing = REQUIRED_FIELDS - set(case)
    extra = set(case) - REQUIRED_FIELDS
    if missing:
        failures.append(f"missing top-level fields: {', '.join(sorted(missing))}")
    if extra:
        failures.append(f"unexpected top-level fields: {', '.join(sorted(extra))}")
    if missing:
        return failures

    object_fields = ("environment", "resources", "restoration")
    collection_fields = ("principals", "role_assignments", "evidence", "scenarios", "claims", "open_gaps")
    for field in object_fields:
        if not isinstance(case[field], dict):
            failures.append(f"{field} must be an object")
    for field in collection_fields:
        if not isinstance(case[field], list):
            failures.append(f"{field} must be an array")
    for field in ("principals", "role_assignments", "evidence", "scenarios", "claims"):
        if isinstance(case[field], list) and not all(isinstance(item, dict) for item in case[field]):
            failures.append(f"every {field} item must be an object")
    if failures:
        return failures

    if case["schema_version"] != 1:
        failures.append("schema_version must be 1")
    if case["product"] != "Black Duck SCA":
        failures.append("product must be Black Duck SCA")
    if not case["environment"].get("sanitized"):
        failures.append("environment.sanitized must be true")

    _check_for_secrets(case, failures)

    principal_ids = _unique_ids(case["principals"], "principal", failures)
    evidence_ids = _unique_ids(case["evidence"], "evidence", failures)
    scenario_ids = _unique_ids(case["scenarios"], "scenario", failures)
    scenarios_by_id = {item["id"]: item for item in case["scenarios"] if isinstance(item.get("id"), str)}

    for assignment in case["role_assignments"]:
        if assignment.get("principal") not in principal_ids:
            failures.append(f"role assignment references unknown principal {assignment.get('principal')!r}")

    for source in case["evidence"]:
        path = source.get("source_path")
        if path and not (product_root / path).is_file():
            failures.append(f"evidence {source.get('id')!r} references missing source_path {path!r}")

    negative_controls: dict[str, int] = {}
    for scenario in case["scenarios"]:
        scenario_id = scenario.get("id", "<missing>")
        if scenario.get("surface") not in SURFACES:
            failures.append(f"scenario {scenario_id!r} has invalid surface")
        if scenario.get("expectation") not in EXPECTATIONS:
            failures.append(f"scenario {scenario_id!r} has invalid expectation")
        if scenario.get("outcome") not in OUTCOMES:
            failures.append(f"scenario {scenario_id!r} has invalid outcome")
        if scenario.get("principal") not in principal_ids:
            failures.append(f"scenario {scenario_id!r} references an unknown principal")
        for evidence_id in scenario.get("evidence", []):
            if evidence_id not in evidence_ids:
                failures.append(f"scenario {scenario_id!r} references unknown evidence {evidence_id!r}")
        control_for = scenario.get("negative_control_for")
        if control_for:
            if control_for not in scenario_ids:
                failures.append(f"scenario {scenario_id!r} references unknown positive scenario {control_for!r}")
            elif scenario.get("expectation") != "DENY":
                failures.append(f"scenario {scenario_id!r} is a negative control but does not expect DENY")
            if scenario.get("outcome") == "OBSERVED_DENIAL":
                negative_controls[control_for] = negative_controls.get(control_for, 0) + 1

    for claim in case["claims"]:
        supports = claim.get("supported_by", [])
        if not supports:
            failures.append(f"claim {claim.get('id')!r} has no supporting scenarios")
        for scenario_id in supports:
            if scenario_id not in scenario_ids:
                failures.append(f"claim {claim.get('id')!r} references unknown scenario {scenario_id!r}")
            else:
                scenario = scenarios_by_id[scenario_id]
                if scenario.get("outcome") == "NOT_TESTED":
                    failures.append(f"claim {claim.get('id')!r} relies on untested scenario {scenario_id!r}")
        if claim.get("requires_negative_control") and not any(negative_controls.get(item) for item in supports):
            failures.append(f"claim {claim.get('id')!r} requires a negative control")

    return failures


def _unique_ids(items: list[dict], label: str, failures: list[str]) -> set[str]:
    ids: set[str] = set()
    for item in items:
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            failures.append(f"{label} is missing a non-empty id")
        elif item_id in ids:
            failures.append(f"duplicate {label} id {item_id!r}")
        else:
            ids.add(item_id)
    return ids


def _check_for_secrets(value, failures: list[str], path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key.lower() in SECRET_KEYS:
                failures.append(f"secret-bearing key is not allowed at {path}.{key}")
            _check_for_secrets(child, failures, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _check_for_secrets(child, failures, f"{path}[{index}]")
    elif isinstance(value, str):
        for pattern in SECRET_PATTERNS:
            if pattern.search(value):
                failures.append(f"possible secret or private server value at {path}")
                break
