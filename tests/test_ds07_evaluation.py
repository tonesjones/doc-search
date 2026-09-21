from __future__ import annotations

import unittest
from pathlib import Path

from evaluation.core import load_jsonl, make_trace, validate_trace, verify_case_evidence
from evaluation.profile import evidence_path_allowed, load_profile, profile_metadata
from scripts.codex_checkout_adapter import build_command, validate_output, version_guard

ROOT = Path(__file__).resolve().parents[1]


class Ds07EvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = load_profile()
        cls.cases = load_jsonl(ROOT / "evaluation" / "cases" / "sca-baseline.jsonl")

    def test_reviewed_baseline_has_30_valid_cases(self):
        self.assertEqual(len(self.cases), 30)
        self.assertTrue(all(case["verification_status"] == "verified" for case in self.cases))
        self.assertEqual([error for case in self.cases for error in verify_case_evidence(case)], [])

    def test_reviewed_regressions_have_six_valid_cases(self):
        cases = load_jsonl(ROOT / "evaluation" / "cases" / "sca-regressions.jsonl")
        self.assertEqual(len(cases), 6)
        self.assertEqual([error for case in cases for error in verify_case_evidence(case)], [])

    def test_profile_accepts_markdown_and_openapi_only_inside_sca_roots(self):
        self.assertTrue(evidence_path_allowed(
            "BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md", self.profile
        ))
        self.assertTrue(evidence_path_allowed(
            "BlackDuck SCA/sources/openapi/2026.4.0/openapi3-public.json", self.profile
        ))
        self.assertFalse(evidence_path_allowed("README.md", self.profile))
        self.assertFalse(evidence_path_allowed("Coverity/index.md", self.profile))

    def test_codex_command_is_read_only_and_ephemeral(self):
        command = build_command(Path("answer.json"), "gpt-5.6-terra", "medium")
        self.assertIn("read-only", command)
        self.assertIn("--ephemeral", command)
        self.assertNotIn("danger-full-access", command)
        self.assertNotIn("--ignore-user-config", command)

    def test_adapter_validates_exact_excerpt_and_citation(self):
        relative = "BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md"
        value = {
            "answer": "A project is the base unit.",
            "evidence": [{"file": relative, "excerpt": "A project is the base unit in Black Duck."}],
            "citations": [{"file": relative}],
        }
        result = validate_output(value, {"product_version": "2026.7"}, self.profile)
        self.assertEqual(result["retrieved_chunks"][0]["metadata"]["version"], "2026.7")
        self.assertEqual(result["citations"], [{"file": relative}])

    def test_adapter_rejects_wrong_version_openapi_evidence(self):
        relative = "BlackDuck SCA/sources/openapi/2026.4.0/openapi3-public.json"
        value = {
            "answer": "x", "evidence": [{"file": relative, "excerpt": "openapi"}],
            "citations": [{"file": relative}],
        }
        with self.assertRaisesRegex(Exception, "does not match requested version"):
            validate_output(value, {"product_version": "2026.7"}, self.profile)

    def test_version_guard_abstains_before_model_execution(self):
        self.assertIsNone(version_guard({"product_version": "2026.4.0"}, self.profile))
        result = version_guard({"product_version": "2025.1.0"}, self.profile)
        self.assertIn("does not establish", result["answer"])
        self.assertEqual(result["model"], "deterministic-version-guard")

    def test_trace_requires_current_provenance(self):
        provenance = profile_metadata(self.profile)
        provenance["prompt_revision"] = "sha256:test"
        trace = make_trace(
            {"question": "q", "product": "blackduck-sca", "product_version": "2026.7"},
            {"answer": "a"}, provenance,
        )
        self.assertEqual(validate_trace(trace), [])
        del trace["instruction_revision"]
        self.assertIn("trace missing string instruction_revision", validate_trace(trace))


if __name__ == "__main__":
    unittest.main()
