from __future__ import annotations

from typing import Callable

from validators.blackduck_sca.client import PROJECT_MEDIA, SCAClient, SCARequestError, collection_count
from validators.core.contract import ValidationRequest, ValidationResult
from validators.core.safety import SAFE_PROJECT_NAME


def _version_compatible(requested: str | None, observed: str | None) -> bool:
    if not requested or not observed:
        return True
    return observed == requested or observed.startswith(requested + ".")


def run_read_only(request: ValidationRequest, client: SCAClient) -> ValidationResult:
    result = ValidationResult(
        validation_id=request.validation_id, result="INCONCLUSIVE", method="api",
        product=request.product, requested_version=request.product_version,
    )
    try:
        observed = client.observed_version()
        result.observed_version = observed
        auth = client.authenticate()
        result.assertions.append({"name": "token_exchange_status", "expected": 200, "actual": auth.status, "pass": auth.status == 200})

        actions: dict[str, Callable[[], None]] = {
            "auth": lambda: None,
            "project-list": lambda: _validate_project_list(client, result),
            "project-media": lambda: _validate_project_media(client, result),
            "isolation-name": lambda: _validate_isolation_name(client, result),
            "current-user": lambda: _validate_current_user(client, result),
        }
        action = request.validation_id.removeprefix("sca-runtime-")
        if action not in actions:
            result.reason = "TEST_DATA_UNAVAILABLE"
            return result
        actions[action]()
        if not _version_compatible(request.product_version, observed):
            result.reason = "VERSION_MISMATCH"
            result.diagnosis = "RUNTIME_INCONCLUSIVE"
            result.observations.append({"type": "version_mismatch", "requested": request.product_version, "observed": observed})
            return result
        if all(assertion.get("pass") is True for assertion in result.assertions):
            result.result = "PASS"
            result.diagnosis = "PASS"
        else:
            result.result = "FAIL"
            result.diagnosis = "DOC_RUNTIME_MISMATCH"
        return result
    except SCARequestError as exc:
        result.reason = exc.category
        result.diagnosis = "RUNTIME_INCONCLUSIVE"
        result.observations.append({"type": "request_failure", "status": exc.status, "category": exc.category})
        return result


def _validate_project_list(client: SCAClient, result: ValidationResult) -> None:
    response = client.projects(limit=1)
    payload = response.json()
    result.assertions.append({"name": "projects_endpoint_status", "expected": 200, "actual": response.status, "pass": response.status == 200})
    result.assertions.append({"name": "projects_collection_shape", "expected": "countable collection", "actual": collection_count(payload), "pass": collection_count(payload) is not None})


def _validate_project_media(client: SCAClient, result: ValidationResult) -> None:
    response = client.projects(limit=1)
    actual = response.headers.get("content-type", "")
    result.assertions.append({"name": "custom_project_media_accepted", "expected": PROJECT_MEDIA, "actual": actual, "pass": response.status == 200})


def _validate_isolation_name(client: SCAClient, result: ValidationResult) -> None:
    response = client.projects(limit=1000)
    payload = response.json()
    exact = [item for item in payload.get("items", []) if isinstance(item, dict) and item.get("name") == SAFE_PROJECT_NAME]
    count = len(exact)
    result.assertions.append({"name": "isolated_project_query_status", "expected": 200, "actual": response.status, "pass": response.status == 200})
    result.assertions.append({"name": "isolated_project_exact_count", "expected": "0 or 1", "actual": count, "pass": count <= 1})
    result.observations.append({"type": "exact_name_match_count", "project_name": SAFE_PROJECT_NAME, "count": count})


def _validate_current_user(client: SCAClient, result: ValidationResult) -> None:
    response = client.get("/api/current-user", "application/vnd.blackducksoftware.user-4+json")
    payload = response.json()
    result.assertions.append({"name": "current_user_status", "expected": 200, "actual": response.status, "pass": response.status == 200})
    result.observations.append({"type": "current_user_object_available", "available": isinstance(payload, dict)})
