from __future__ import annotations

import importlib.util
import json
import os
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PRODUCT_ROOT = ROOT / "BlackDuck SCA"
MODULE_PATH = PRODUCT_ROOT / "verification/environment_config.py"
EXAMPLE_PATH = PRODUCT_ROOT / "verification/environment.example.json"
spec = importlib.util.spec_from_file_location("environment_config", MODULE_PATH)
environment_config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(environment_config)


class RbacEnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))

    def test_committed_example_is_valid_without_credentials(self):
        self.assertEqual(environment_config.validate_environment(self.config), [])

    def test_server_url_must_be_an_https_origin(self):
        config = deepcopy(self.config)
        config["base_url"] = "http://sca.example.test/api"
        self.assertEqual(
            environment_config.validate_environment(config),
            ["base_url must be an HTTPS server origin without a path"],
        )

    def test_credentials_are_resolved_from_environment_variables(self):
        variable_names = {
            value
            for principal in self.config["principals"].values()
            for value in principal.values()
        }
        with patch.dict(os.environ, {name: "configured" for name in variable_names}, clear=True):
            self.assertEqual(environment_config.validate_environment(self.config, require_credentials=True), [])

    def test_missing_credential_reports_variable_name_without_reading_secret(self):
        with patch.dict(os.environ, {}, clear=True):
            failures = environment_config.validate_environment(self.config, require_credentials=True)
        self.assertIn("principal 'admin' requires environment variable BD_RBAC_ADMIN_TOKEN", failures)
        self.assertNotIn("configured", " ".join(failures))


if __name__ == "__main__":
    unittest.main()
