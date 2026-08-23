#!/usr/bin/env python3
"""Idempotently provision only the isolated Tony RAG SCA project and case versions."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from validators.blackduck_sca.client import PROJECT_MEDIA, SCAClient, collection_count, load_runtime_env  # noqa: E402
from validators.core.safety import (  # noqa: E402
    SAFE_PROJECT_NAME,
    validate_active_version_capacity,
    validate_mutation_target,
)

PROJECT_MARKER = "Isolated Tony RAG runtime-validation POC. Created only for Codex SCA tests."
VERSION_MEDIA = "application/vnd.blackducksoftware.project-detail-5+json"
VERSION_NAMES = [
    "RAG-VAL-auth",
    "RAG-VAL-current-user",
    "RAG-VAL-isolation-name",
    "RAG-VAL-project-list",
    "RAG-VAL-project-media",
]


def api_path(value: str) -> str:
    path = urlparse(value).path if "://" in value else value
    if path.startswith("/projects/"):
        path = "/api" + path
    if not path.startswith("/api/projects/"):
        raise RuntimeError("UNSAFE_TO_VALIDATE: server returned an unexpected project location")
    return path.rstrip("/")


def project_items(client: SCAClient) -> list[dict]:
    # The 2026.4 q parser tokenizes quoted names unexpectedly; enumerate once
    # and filter exact names locally so a retry can never create a duplicate.
    payload = client.projects(limit=1000).json()
    return [item for item in payload.get("items", []) if isinstance(item, dict) and item.get("name") == SAFE_PROJECT_NAME]


def project_path(item: dict) -> str:
    meta = item.get("_meta", {})
    return api_path(meta.get("href", ""))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-mutations", action="store_true")
    parser.add_argument("--confirm-project", required=True)
    parser.add_argument("--env-file", type=Path, default=ROOT / ".env.runtime")
    parser.add_argument("--output", type=Path, default=ROOT / "runtime" / "results" / "sca-provision.json")
    args = parser.parse_args()
    env = load_runtime_env(args.env_file)
    if not args.allow_mutations or env.get("VALIDATOR_ALLOW_MUTATIONS", "").casefold() != "true":
        raise SystemExit("UNSAFE_TO_VALIDATE: mutation requires both CLI and project-local opt-in")
    if args.confirm_project != SAFE_PROJECT_NAME:
        raise SystemExit("UNSAFE_TO_VALIDATE: confirmation does not match the isolated project")
    for version in VERSION_NAMES:
        validate_mutation_target(SAFE_PROJECT_NAME, version)

    client = SCAClient(env.get("BLACKDUCK_BASE_URL", ""), env.get("BLACKDUCK_API_TOKEN", ""))
    existing = project_items(client)
    if len(existing) > 1:
        raise SystemExit("UNSAFE_TO_VALIDATE: multiple exact-name Tony RAG projects were returned")

    created_project = False
    created_versions: list[str] = []
    if not existing:
        response = client.post_json("/api/projects", {
            "name": SAFE_PROJECT_NAME,
            "description": PROJECT_MARKER,
            "versionRequest": {
                "versionName": VERSION_NAMES[0],
                "phase": "PLANNING",
                "distribution": "EXTERNAL",
                "protectedFromDeletion": False,
            },
        }, PROJECT_MEDIA)
        if response.status != 201:
            raise RuntimeError(f"project creation returned HTTP {response.status}")
        created_project = True
        created_versions.append(VERSION_NAMES[0])
        existing = project_items(client)
        if len(existing) != 1:
            raise RuntimeError("project creation could not be verified by exact-name readback")

    item = existing[0]
    if item.get("description") != PROJECT_MARKER:
        raise SystemExit("UNSAFE_TO_VALIDATE: existing Tony RAG project lacks this validator's ownership marker")
    path = project_path(item)

    capacity_payload = client.project_versions(path, limit=100).json()
    active_versions = [item for item in capacity_payload.get("items", []) if isinstance(item, dict)]
    active_names = {item.get("versionName") for item in active_versions}
    missing_names = [name for name in VERSION_NAMES if name not in active_names]
    try:
        validate_active_version_capacity(len(active_versions), len(missing_names))
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    for name in VERSION_NAMES:
        payload = client.project_versions(path, limit=100).json()
        exact = [version for version in payload.get("items", []) if isinstance(version, dict) and version.get("versionName") == name]
        if len(exact) > 1:
            raise RuntimeError(f"multiple exact versions returned for {name}")
        if exact:
            continue
        response = client.post_json(path + "/versions", {
            "versionName": name,
            "releaseComments": "Runtime-validation case container; no customer data.",
            "phase": "PLANNING",
            "distribution": "EXTERNAL",
            "protectedFromDeletion": False,
        }, VERSION_MEDIA)
        if response.status != 201:
            raise RuntimeError(f"version creation returned HTTP {response.status} for {name}")
        created_versions.append(name)

    final_payload = client.project_versions(path, limit=100).json()
    final_names = sorted(
        version.get("versionName") for version in final_payload.get("items", [])
        if isinstance(version, dict) and version.get("versionName") in VERSION_NAMES
    )
    if final_names != sorted(VERSION_NAMES):
        raise RuntimeError("not all isolated validation versions were verified after creation")

    report = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "environment": "sca.field-test.blackduck.com",
        "observed_version": env.get("BLACKDUCK_OBSERVED_VERSION"),
        "project": SAFE_PROJECT_NAME,
        "project_created": created_project,
        "versions_expected": VERSION_NAMES,
        "versions_created_this_run": created_versions,
        "versions_verified": final_names,
        "other_projects_touched": 0,
        "cleanup_result": "PASS",
        "cleanup_note": "Resources retained by explicit user request; provisioner is idempotent and ownership-marked.",
    }
    encoded = json.dumps(report, indent=2) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
