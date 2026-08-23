from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

Result = Literal["PASS", "FAIL", "INCONCLUSIVE"]


@dataclass(frozen=True)
class ValidationRequest:
    validation_id: str
    eval_case_id: str
    product: str
    product_version: str | None
    claim: str
    claim_type: str
    documentation_evidence: list[dict[str, str]]
    environment: str


@dataclass
class ValidationResult:
    validation_id: str
    result: Result
    method: str
    product: str
    requested_version: str | None
    observed_version: str | None = None
    observations: list[dict[str, Any]] = field(default_factory=list)
    assertions: list[dict[str, Any]] = field(default_factory=list)
    artifacts: list[str] = field(default_factory=list)
    cleanup_result: Result = "PASS"
    reason: str | None = None
    diagnosis: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


INCONCLUSIVE_REASONS = {
    "AUTHENTICATION_FAILED", "AUTHORIZATION_FAILED", "LICENSE_MISSING",
    "ENVIRONMENT_UNAVAILABLE", "VERSION_MISMATCH", "RATE_LIMITED", "TIMEOUT",
    "TEST_DATA_UNAVAILABLE", "API_UNAVAILABLE", "DEPENDENCY_FAILURE",
    "SELECTOR_AMBIGUOUS", "UI_CHANGED_UNEXPECTEDLY", "UNSAFE_TO_VALIDATE",
    "CLEANUP_FAILED",
}
