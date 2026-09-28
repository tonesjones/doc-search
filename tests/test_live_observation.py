from __future__ import annotations

import importlib.util
import sys
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCT_ROOT = ROOT / "BlackDuck SCA"
VERIFICATION = PRODUCT_ROOT / "verification"
sys.path.insert(0, str(VERIFICATION))
spec = importlib.util.spec_from_file_location("live_observation", VERIFICATION / "live_observation.py")
live_observation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(live_observation)
RECORDS = sorted((VERIFICATION / "live-observations").glob("*.json"))


class LiveObservationTests(unittest.TestCase):
    def setUp(self):
        self.record = live_observation.load_observation(RECORDS[0])

    def test_committed_records_are_valid(self):
        self.assertTrue(RECORDS)
        for path in RECORDS:
            with self.subTest(path=path.name):
                record = live_observation.load_observation(path)
                self.assertEqual(live_observation.validate_observation(record, PRODUCT_ROOT), [])

    def test_unreviewed_observation_is_rejected(self):
        record = deepcopy(self.record)
        record["review"]["status"] = "UNREVIEWED"
        self.assertIn(
            "review.status must be APPROVED; keep unreviewed observations in .local",
            live_observation.validate_observation(record, PRODUCT_ROOT),
        )

    def test_write_mode_is_rejected(self):
        record = deepcopy(self.record)
        record["method"]["mode"] = "WRITE"
        self.assertIn("method.mode must be READ_ONLY", live_observation.validate_observation(record, PRODUCT_ROOT))

    def test_customer_data_is_rejected(self):
        record = deepcopy(self.record)
        record["environment"]["customer_data"] = True
        self.assertIn("environment.customer_data must be false", live_observation.validate_observation(record, PRODUCT_ROOT))

    def test_private_server_url_is_rejected(self):
        record = deepcopy(self.record)
        record["findings"][0]["statement"] += " Seen at https://sca1.poc.example.com/ui."
        failures = live_observation.validate_observation(record, PRODUCT_ROOT)
        self.assertTrue(any("possible secret or private server value" in item for item in failures))

    def test_secret_key_is_rejected(self):
        record = deepcopy(self.record)
        record["principal"]["api_token"] = "redacted"
        failures = live_observation.validate_observation(record, PRODUCT_ROOT)
        self.assertTrue(any("secret-bearing key" in item for item in failures))

    def test_unknown_case_and_missing_source_are_rejected(self):
        record = deepcopy(self.record)
        record["findings"][0]["related_cases"] = ["no-such-case"]
        record["findings"][0]["documentation"] = [{"source_path": "docs/missing.md", "verdict": "CONSISTENT"}]
        failures = live_observation.validate_observation(record, PRODUCT_ROOT)
        self.assertTrue(any("unknown case 'no-such-case'" in item for item in failures))
        self.assertTrue(any("missing source_path 'docs/missing.md'" in item for item in failures))

    def test_invalid_scope_and_verdict_are_rejected(self):
        record = deepcopy(self.record)
        record["findings"][0]["scope"] = "UNIVERSAL"
        record["findings"][0]["documentation"][0]["verdict"] = "WRONG"
        failures = live_observation.validate_observation(record, PRODUCT_ROOT)
        self.assertTrue(any("invalid scope" in item for item in failures))
        self.assertTrue(any("invalid documentation verdict" in item for item in failures))

    def test_duplicate_finding_ids_are_rejected(self):
        record = deepcopy(self.record)
        record["findings"].append(deepcopy(record["findings"][0]))
        failures = live_observation.validate_observation(record, PRODUCT_ROOT)
        self.assertTrue(any("duplicate finding id" in item for item in failures))

    def test_unexpected_field_is_rejected(self):
        record = deepcopy(self.record)
        record["raw_response"] = {}
        self.assertEqual(
            live_observation.validate_observation(record, PRODUCT_ROOT),
            ["unexpected top-level fields: raw_response"],
        )


if __name__ == "__main__":
    unittest.main()
