from __future__ import annotations

import json
import unittest

from validators.blackduck_sca.client import Response, SCARequestError, collection_count
from validators.blackduck_sca.validator import run_read_only
from validators.core.contract import ValidationRequest
from validators.core.safety import (
    redact_text,
    validate_active_version_capacity,
    validate_mutation_target,
    validate_sca_base_url,
)
from evaluation.combined import diagnose
from evaluation.core import ROOT


def request(validation_id: str = "sca-runtime-auth", version: str = "2026.7") -> ValidationRequest:
    return ValidationRequest(validation_id, "eval", "blackduck-sca", version, "claim", "API_VALIDATABLE", [], "test")


class FakeClient:
    def __init__(self, version="2026.7", error=None):
        self.version = version
        self.error = error

    def observed_version(self):
        return self.version

    def authenticate(self):
        if self.error:
            raise self.error
        return Response(200, {}, b"{}")


class RuntimeValidatorTests(unittest.TestCase):
    def test_host_allowlist_is_exact(self):
        self.assertEqual(validate_sca_base_url("https://sca.field-test.blackduck.com/"), "https://sca.field-test.blackduck.com")
        with self.assertRaises(ValueError):
            validate_sca_base_url("https://sca.field-test.blackduck.com.example.org")

    def test_mutations_are_restricted_to_isolated_names(self):
        validate_mutation_target("Tony RAG", "RAG-VAL-test")
        with self.assertRaises(ValueError):
            validate_mutation_target("Somebody Else's Project", "RAG-VAL-test")

    def test_active_test_version_limit_is_enforced(self):
        validate_active_version_capacity(9, 1)
        with self.assertRaises(ValueError):
            validate_active_version_capacity(10, 1)
        with self.assertRaises(ValueError):
            validate_active_version_capacity(9, 2)

    def test_account_inactivation_runtime_case_is_approval_gated(self):
        candidate = json.loads(
            (ROOT / "runtime" / "cases" / "sca-user-inactivation-token.json").read_text(encoding="utf-8")
        )
        self.assertEqual(candidate["status"], "candidate")
        self.assertTrue(candidate["approval"]["required"])
        self.assertFalse(candidate["cleanup"]["automatic"])
        self.assertEqual(candidate["cleanup"]["controller_account_change"], "forbidden")
        self.assertEqual(candidate["execution_history"], [])

    def test_clone_bom_retention_runtime_case_is_approval_gated(self):
        candidate = json.loads(
            (ROOT / "runtime" / "cases" / "sca-version-clone-bom-retention.json").read_text(encoding="utf-8")
        )
        self.assertEqual(candidate["related_eval_case"], "sca-version-007")
        self.assertEqual(candidate["status"], "candidate")
        self.assertTrue(candidate["approval"]["required"])
        self.assertEqual(candidate["current_version_disposition"], "INCONCLUSIVE_VERSION_MISMATCH")
        self.assertFalse(candidate["cleanup"]["automatic"])
        self.assertEqual(candidate["cleanup"]["other_project_change"], "forbidden")
        self.assertEqual(candidate["execution_history"], [])

    def test_version_mismatch_is_inconclusive(self):
        result = run_read_only(request(), FakeClient(version="2026.4.0"))
        self.assertEqual(result.result, "INCONCLUSIVE")
        self.assertEqual(result.reason, "VERSION_MISMATCH")

    def test_auth_failure_is_inconclusive(self):
        error = SCARequestError(401, "AUTHENTICATION_FAILED", "no")
        result = run_read_only(request(), FakeClient(error=error))
        self.assertEqual(result.result, "INCONCLUSIVE")
        self.assertEqual(result.reason, "AUTHENTICATION_FAILED")

    def test_secret_redaction(self):
        cleaned = redact_text("Authorization: BearerSecret API_TOKEN=abc123")
        self.assertNotIn("BearerSecret", cleaned)
        self.assertNotIn("abc123", cleaned)

    def test_collection_count(self):
        self.assertEqual(collection_count({"totalCount": 5, "items": []}), 5)
        self.assertEqual(collection_count({"items": [{}, {}]}), 2)

    def test_combined_diagnosis_keeps_runtime_inconclusive_separate(self):
        self.assertEqual(diagnose(["SYNTHESIS_FAILURE"], "INCONCLUSIVE"), "RUNTIME_INCONCLUSIVE")
        self.assertEqual(diagnose(["SYNTHESIS_FAILURE"], "PASS"), "RAG_FAILURE")


if __name__ == "__main__":
    unittest.main()
