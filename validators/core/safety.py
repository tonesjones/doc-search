from __future__ import annotations

import re
from urllib.parse import urlparse

ALLOWED_SCA_HOSTS = {"sca.field-test.blackduck.com"}
SAFE_PROJECT_NAME = "Tony RAG"
SAFE_VERSION_PREFIX = "RAG-VAL-"
MAX_ACTIVE_TEST_VERSIONS = 10
SECRET_ASSIGNMENT_RE = re.compile(
    r"(?i)(authorization|password|passwd|secret|api_?key|(?:api_?|access_?|refresh_?)?token|cookie)(\s*[:=]\s*)([^\s,;]+)"
)


def validate_sca_base_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_SCA_HOSTS:
        raise ValueError("UNSAFE_TO_VALIDATE: SCA host is not allowlisted HTTPS")
    if parsed.path not in ("", "/") or parsed.query or parsed.fragment:
        raise ValueError("UNSAFE_TO_VALIDATE: base URL must not contain a path, query, or fragment")
    return f"https://{parsed.hostname}"


def validate_mutation_target(project_name: str, version_name: str | None = None) -> None:
    if project_name != SAFE_PROJECT_NAME:
        raise ValueError("UNSAFE_TO_VALIDATE: mutations are restricted to the exact isolated project name")
    if version_name is not None and not version_name.startswith(SAFE_VERSION_PREFIX):
        raise ValueError("UNSAFE_TO_VALIDATE: version name lacks the required RAG validation prefix")


def validate_active_version_capacity(active_count: int, requested_new_count: int) -> None:
    if active_count < 0 or requested_new_count < 0:
        raise ValueError("UNSAFE_TO_VALIDATE: active-version counts cannot be negative")
    if active_count + requested_new_count > MAX_ACTIVE_TEST_VERSIONS:
        raise ValueError(
            "UNSAFE_TO_VALIDATE: Tony RAG would exceed the shared-instance limit of "
            f"{MAX_ACTIVE_TEST_VERSIONS} active versions; explicitly delete an obsolete test "
            "version or convert an appropriate released version to LTS before provisioning"
        )


def redact_text(value: str) -> str:
    return SECRET_ASSIGNMENT_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}[REDACTED]", value)
