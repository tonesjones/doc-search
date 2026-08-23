#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from validators.blackduck_sca.client import SCAClient, load_runtime_env  # noqa: E402
from validators.blackduck_sca.validator import run_read_only  # noqa: E402
from validators.core.contract import ValidationRequest  # noqa: E402

CASES = {
    "sca-runtime-auth": ("sca-auth-002", "The API token exchange endpoint accepts a token and returns a bearer token.", "API_VALIDATABLE", "BlackDuck SCA/docs/api/authenticating-with-the-api.md"),
    "sca-runtime-project-list": ("sca-auth-003", "An authenticated bearer token can access the projects endpoint.", "API_VALIDATABLE", "BlackDuck SCA/docs/api/authenticating-with-the-api.md"),
    "sca-runtime-project-media": ("sca-auth-002", "The projects endpoint accepts the documented custom project media type.", "API_VALIDATABLE", "BlackDuck SCA/docs/api/using-the-right-media-types.md"),
    "sca-runtime-isolation-name": ("sca-project-003", "The isolated Tony RAG project name can be queried before any mutation.", "API_VALIDATABLE", "BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md"),
    "sca-runtime-current-user": ("sca-role-001", "The authenticated API exposes the current-user resource for permission preflight.", "API_VALIDATABLE", "BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md"),
}


def build_request(case_id: str, requested_version: str) -> ValidationRequest:
    eval_case, claim, classification, evidence = CASES[case_id]
    return ValidationRequest(
        validation_id=case_id, eval_case_id=eval_case, product="blackduck-sca",
        product_version=requested_version, claim=claim, claim_type=classification,
        documentation_evidence=[{"file": evidence, "version": "2026.7"}],
        environment="sca.field-test.blackduck.com",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Black Duck SCA runtime validation safely")
    parser.add_argument("--product", choices=["blackduck-sca"], required=True)
    parser.add_argument("--eval-case", choices=sorted(CASES))
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--requested-version", default="2026.7")
    parser.add_argument("--env-file", type=Path, default=ROOT / ".env.runtime")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.all == bool(args.eval_case):
        parser.error("choose exactly one of --all or --eval-case")
    env = load_runtime_env(args.env_file)
    client = SCAClient(
        env.get("BLACKDUCK_BASE_URL", ""), env.get("BLACKDUCK_API_TOKEN", ""),
        observed_version_hint=env.get("BLACKDUCK_OBSERVED_VERSION"),
    )
    selected = sorted(CASES) if args.all else [args.eval_case]
    results = [run_read_only(build_request(case_id, args.requested_version), client).to_dict() for case_id in selected]
    report = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "environment": "sca.field-test.blackduck.com",
        "mutation_mode": "disabled",
        "results": results,
    }
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0 if all(item["result"] == "PASS" for item in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
