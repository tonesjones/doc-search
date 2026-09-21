from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.product_registry import load_registry, resolve_products

ROOT = Path(__file__).resolve().parents[1]


class ScaVerificationTests(unittest.TestCase):
    def run_verifier(self, corpus=None):
        product, = resolve_products(["sca"], load_registry(ROOT))
        self.assertTrue((ROOT / product.skill).is_file())
        command = [sys.executable, "-B", str(ROOT / product.verifier)]
        if corpus is not None:
            command.extend(["--root", str(corpus)])
        result = subprocess.run(command, cwd=tempfile.gettempdir(), capture_output=True,
                                text=True, encoding="utf-8", env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        self.assertEqual(result.stderr, "")
        report = json.loads(result.stdout)
        self.assert_report_contract(report)
        self.assertEqual([check["status"] for check in report["checks"] if check["category"] == "live"],
                         ["NOT_RUN", "NOT_RUN"])
        return result.returncode, report

    def assert_report_contract(self, report):
        schema = json.loads((ROOT / "verification-report.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(set(report), set(schema["required"]))
        self.assertEqual(report["product"], "black-duck-sca")
        self.assertEqual(report["version"], "2026.7")
        self.assertIn(report["status"], schema["$defs"]["status"]["enum"])
        for check in report["checks"]:
            self.assertEqual(set(check), set(schema["$defs"]["check"]["required"]))
            self.assertIsInstance(check["name"], str)
            self.assertTrue(check["name"])
            self.assertIn(check["category"], schema["$defs"]["check"]["properties"]["category"]["enum"])
            self.assertIn(check["status"], schema["$defs"]["status"]["enum"])
        for field in ("evidence", "failures"):
            self.assertIsInstance(report[field], list)
            for item in report[field]:
                self.assertIsInstance(item, str)
                self.assertTrue(item)

    def test_registered_verifier_passes_from_another_directory(self):
        code, report = self.run_verifier()
        self.assertEqual(code, 0)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["failures"], [])
        self.assertEqual(sum(check["status"] == "PASS" for check in report["checks"]), 7)

    def test_missing_corpus_fails_with_a_json_report(self):
        with tempfile.TemporaryDirectory() as directory:
            code, report = self.run_verifier(Path(directory) / "missing")
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("missing manifest" in failure for failure in report["failures"]))

    def test_bad_default_routing_fails_even_with_readable_catalogs(self):
        with tempfile.TemporaryDirectory() as directory:
            corpus = Path(directory)
            for path in (ROOT / "BlackDuck SCA").glob("index*.md"):
                shutil.copyfile(path, corpus / path.name)
            routing = corpus / "index-detect.md"
            routing.write_text(routing.read_text(encoding="utf-8").replace(
                "](index-detect-12.0.0.md)", "](index-detect-11.5.1.md)"), encoding="utf-8")
            code, report = self.run_verifier(corpus)
        self.assertEqual(code, 1)
        check = next(item for item in report["checks"] if item["name"] == "Detect default routing")
        self.assertEqual(check["status"], "FAIL")
        self.assertIn("Detect default routing: Default catalog is not Detect 12.0.0", report["failures"])

    def test_malformed_manifest_fails_without_a_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            corpus = Path(directory)
            manifest = corpus / "sources/blackduck-2026.7/manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text("{broken", encoding="utf-8")
            code, report = self.run_verifier(corpus)
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["checks"][0]["status"], "FAIL")

    def test_missing_indexed_topic_fails_retrieval(self):
        with tempfile.TemporaryDirectory() as directory:
            corpus = Path(directory)
            shutil.copyfile(ROOT / "BlackDuck SCA/index-detect-12.0.0.md", corpus / "index-detect-12.0.0.md")
            code, report = self.run_verifier(corpus)
        self.assertEqual(code, 1)
        check = next(item for item in report["checks"] if item["name"] == "Detect 12 rapid scan")
        self.assertEqual(check["status"], "FAIL")
        self.assertTrue(any("Detect 12 rapid scan:" in failure for failure in report["failures"]))


if __name__ == "__main__":
    unittest.main()
