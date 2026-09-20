from __future__ import annotations

import importlib.util
import json
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCT_ROOT = ROOT / "BlackDuck SCA"
MODULE_PATH = PRODUCT_ROOT / "verification/rbac_case.py"
CASE_PATH = PRODUCT_ROOT / "verification/cases/sca-2026-7-rbac-poc.json"
spec = importlib.util.spec_from_file_location("rbac_case", MODULE_PATH)
rbac_case = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rbac_case)


class RbacCaseTests(unittest.TestCase):
    def setUp(self):
        self.case = json.loads(CASE_PATH.read_text(encoding="utf-8"))

    def test_sanitized_case_is_valid(self):
        self.assertEqual(rbac_case.validate_case(self.case, PRODUCT_ROOT), [])

    def test_secret_bearing_field_is_rejected(self):
        case = deepcopy(self.case)
        case["environment"]["access_token"] = "not-a-real-token"
        failures = rbac_case.validate_case(case, PRODUCT_ROOT)
        self.assertIn("secret-bearing key is not allowed at $.environment.access_token", failures)

    def test_private_poc_hostname_is_rejected(self):
        case = deepcopy(self.case)
        case["environment"]["label"] = "https://example.poc.example.com"
        failures = rbac_case.validate_case(case, PRODUCT_ROOT)
        self.assertIn("possible secret or private server value at $.environment.label", failures)

    def test_claim_that_requires_negative_control_is_rejected_without_one(self):
        case = deepcopy(self.case)
        for scenario in case["scenarios"]:
            scenario.pop("negative_control_for", None)
        failures = rbac_case.validate_case(case, PRODUCT_ROOT)
        self.assertIn("claim 'project-group-isolation' requires a negative control", failures)

    def test_untested_negative_control_does_not_prove_isolation(self):
        case = deepcopy(self.case)
        scenario = next(item for item in case["scenarios"] if item["id"] == "ui-bu-a-control-project")
        scenario["outcome"] = "NOT_TESTED"
        failures = rbac_case.validate_case(case, PRODUCT_ROOT)
        self.assertIn("claim 'project-group-isolation' requires a negative control", failures)

    def test_missing_documentation_source_is_rejected(self):
        case = deepcopy(self.case)
        case["evidence"][0]["source_path"] = "docs/missing.md"
        failures = rbac_case.validate_case(case, PRODUCT_ROOT)
        self.assertIn("evidence 'docs-project-group-roles' references missing source_path 'docs/missing.md'", failures)

    def test_wrong_collection_type_returns_a_validation_failure(self):
        case = deepcopy(self.case)
        case["scenarios"] = "not-an-array"
        self.assertEqual(rbac_case.validate_case(case, PRODUCT_ROOT), ["scenarios must be an array"])


if __name__ == "__main__":
    unittest.main()
