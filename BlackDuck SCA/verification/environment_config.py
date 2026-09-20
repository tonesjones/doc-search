"""Validate local configuration for a live RBAC test environment."""

from __future__ import annotations

import json
import os
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_FIELDS = {"schema_version", "environment_label", "base_url", "expected_version", "principals"}
PRINCIPAL_FIELDS = {"api_token_env", "ui_username_env", "ui_password_env"}


def load_environment(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_environment(config: dict, require_credentials: bool = False) -> list[str]:
    if not isinstance(config, dict):
        return ["environment root must be an object"]

    failures: list[str] = []
    missing = REQUIRED_FIELDS - set(config)
    extra = set(config) - REQUIRED_FIELDS
    if missing:
        failures.append(f"missing environment fields: {', '.join(sorted(missing))}")
    if extra:
        failures.append(f"unexpected environment fields: {', '.join(sorted(extra))}")
    if failures:
        return failures

    if config["schema_version"] != 1:
        failures.append("schema_version must be 1")
    parsed_url = urlparse(config["base_url"] if isinstance(config["base_url"], str) else "")
    if parsed_url.scheme != "https" or not parsed_url.netloc or parsed_url.path not in ("", "/"):
        failures.append("base_url must be an HTTPS server origin without a path")
    if not isinstance(config["principals"], dict) or not config["principals"]:
        failures.append("principals must be a non-empty object")
        return failures

    for label, principal in config["principals"].items():
        if not isinstance(principal, dict):
            failures.append(f"principal {label!r} must be an object")
            continue
        if set(principal) != PRINCIPAL_FIELDS:
            failures.append(f"principal {label!r} must define only {', '.join(sorted(PRINCIPAL_FIELDS))}")
            continue
        for field, variable in principal.items():
            if not isinstance(variable, str) or not variable:
                failures.append(f"principal {label!r} has an invalid {field}")
            elif require_credentials and not os.environ.get(variable):
                failures.append(f"principal {label!r} requires environment variable {variable}")

    return failures
