from __future__ import annotations

import unittest
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from evaluation.core import load_fact_equivalents, load_jsonl, make_trace, score_case, validate_trace, verify_case_evidence
from evaluation.profile import evidence_path_allowed, load_profile, profile_metadata
from scripts.codex_checkout_adapter import (
    PROMPT_TEMPLATE,
    build_command,
    repository_relative,
    validate_output,
    verified_excerpt,
    version_guard,
)

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

    def test_cpp_scan_case_includes_build_for_normal_first_scan(self):
        case = next(case for case in load_jsonl(ROOT / "evaluation" / "cases" / "sca-regressions.jsonl")
                    if case["id"] == "feedback-bd-cpp-standard-scope-001")
        self.assertEqual(
            [fact["value"] for fact in case["required_facts"]],
            ["blackduck-c-cpp", "--build_cmd", "--build_dir", "--project_name", "--project_version", "--bd_url", "--api_token"],
        )
        path = case["must_retrieve"][0]
        trace = {
            "answer_id": "ans-cpp", "timestamp": "2026-09-22T00:00:00Z",
            "original_query": case["question"], "product": case["product"],
            "answer": "Run blackduck-c-cpp -bc BUILD_COMMAND -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token.",
            "retrieved_chunks": [{"file": path, "content": "-bc build_cmd --build_cmd build_cmd -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token",
                                  "metadata": {"version": "latest"}}],
            "citations": [{"file": path}],
            "evaluation_profile": "test", "entrypoint": "test", "checkout_revision": "test",
            "checkout_dirty": False, "instruction_revision": "test", "source_revision": "test",
            "prompt_revision": "test",
        }
        self.assertEqual(score_case(case, trace, fact_equivalents=load_fact_equivalents())["status"], "PASS")

    def test_smoke_manifest_selects_six_cases_without_model_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "result.json"
            result = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "evaluate.py"),
                "--cases", str(ROOT / "evaluation" / "cases" / "sca-regressions.jsonl"),
                "--case-id-file", str(ROOT / "evaluation" / "cases" / "sca-smoke.txt"),
                "--deterministic-only", "--allow-unmeasured", "--output", str(output),
            ], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["verified_cases"], 6)

    def test_reviewed_project_definition_answer_passes_plain_language_equivalent(self):
        case = next(case for case in load_jsonl(ROOT / "evaluation" / "cases" / "sca-regressions.jsonl")
                    if case["id"] == "feedback-sca-project-definition-001")
        path = case["must_retrieve_any"][0]
        trace = {
            "answer_id": "ans-test", "timestamp": "2026-09-22T00:00:00Z",
            "original_query": case["question"], "product": case["product"],
            "answer": "A project is a top-level record. It can stand alone or be included in a larger project. Each release has a project version.",
            "retrieved_chunks": [{"file": path, "content": "A project can be part of another project.",
                                  "metadata": {"version": "2026.7"}}],
            "citations": [{"file": path}],
            "evaluation_profile": "test", "entrypoint": "test", "checkout_revision": "test",
            "checkout_dirty": False, "instruction_revision": "test", "source_revision": "test",
            "prompt_revision": "test",
        }
        equivalents = load_fact_equivalents()
        self.assertEqual(score_case(case, trace, fact_equivalents=equivalents)["status"], "PASS")

    def test_project_definition_accepts_either_version_matched_definition_page(self):
        case = next(
            case for case in load_jsonl(ROOT / "evaluation" / "cases" / "sca-regressions.jsonl")
            if case["id"] == "feedback-sca-project-definition-001"
        )
        for path in case["must_retrieve_any"]:
            trace = {
                "answer_id": "ans-test", "timestamp": "2026-09-21T00:00:00Z",
                "original_query": case["question"], "product": case["product"],
                "answer": "base unit stand-alone development project part of another project project version",
                "retrieved_chunks": [{"file": path, "content": "base unit project version", "metadata": {"version": "2026.7"}}],
                "citations": [{"file": path}], "evaluation_profile": "test", "entrypoint": "test",
                "checkout_revision": "test", "checkout_dirty": False, "instruction_revision": "test",
                "source_revision": "test", "prompt_revision": "test",
            }
            result = score_case(case, trace)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["recall_at"]["1"], 1.0)
        self.assertNotIn("base unit", [fact["value"] for fact in case["required_facts"]])

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
        self.assertIn("Do not return SKILL.md", PROMPT_TEMPLATE)
        self.assertIn("support every material step", PROMPT_TEMPLATE)
        self.assertIn("prefer the self-documenting long options", PROMPT_TEMPLATE)
        self.assertIn("environment variable for a secret", PROMPT_TEMPLATE)

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

    def test_adapter_normalizes_checkout_path_and_source_whitespace(self):
        relative = "BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md"
        absolute = str(ROOT / relative)
        self.assertEqual(repository_relative(absolute), relative)
        matched = verified_excerpt("one\n  two three", "one two three", relative)
        self.assertEqual(matched, "one\n  two three")

    def test_adapter_returns_source_text_when_markdown_punctuation_differs(self):
        relative = "example.md"
        source = "| `--build_cmd build_cmd` | Command used to execute the build. |"
        claimed = "--build_cmd build_cmd Command used to execute the build."
        self.assertEqual(
            verified_excerpt(source, claimed, relative),
            "--build_cmd build_cmd` | Command used to execute the build.",
        )

    def test_adapter_rejects_a_noncontiguous_excerpt(self):
        with self.assertRaisesRegex(Exception, "not present in source"):
            verified_excerpt("one two omitted three four", "one two three four", "example.md")

    def test_adapter_rejects_wrong_version_openapi_evidence(self):
        relative = "BlackDuck SCA/sources/openapi/2026.4.0/openapi3-public.json"
        value = {
            "answer": "x", "evidence": [{"file": relative, "excerpt": "openapi"}],
            "citations": [{"file": relative}],
        }
        with self.assertRaisesRegex(Exception, "does not match requested version"):
            validate_output(value, {"product_version": "2026.7"}, self.profile)

    def test_latest_accepts_the_profile_current_version(self):
        relative = "BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md"
        value = {
            "answer": "x",
            "evidence": [{"file": relative, "excerpt": "A project is the base unit in Black Duck."}],
            "citations": [{"file": relative}],
        }
        result = validate_output(value, {"product_version": "latest"}, self.profile)
        self.assertEqual(result["retrieved_chunks"][0]["metadata"]["version"], "2026.7")

    def test_version_guard_abstains_before_model_execution(self):
        self.assertIsNone(version_guard({"product_version": "2026.4.0"}, self.profile))
        result = version_guard({"product_version": "2025.1.0"}, self.profile)
        self.assertIn("does not establish", result["answer"])
        self.assertEqual(result["model"], "deterministic-version-guard")

    def test_successful_version_abstention_does_not_require_unavailable_sources(self):
        case = next(case for case in self.cases if case["id"] == "sca-version-caveat-001")
        result = version_guard({"product_version": case["product_version"]}, {
            **self.profile, "available_versions": [self.profile["product_version"]],
        })
        provenance = profile_metadata(self.profile)
        provenance["checkout_dirty"] = False
        provenance["prompt_revision"] = "sha256:test"
        trace = make_trace(case, result, provenance)
        self.assertEqual(score_case(case, trace)["status"], "PASS")

    def test_trace_requires_current_provenance(self):
        provenance = profile_metadata(self.profile)
        provenance["checkout_dirty"] = False
        provenance["prompt_revision"] = "sha256:test"
        trace = make_trace(
            {"question": "q", "product": "blackduck-sca", "product_version": "2026.7"},
            {"answer": "a"}, provenance,
        )
        self.assertEqual(validate_trace(trace), [])
        del trace["instruction_revision"]
        self.assertIn("trace missing string instruction_revision", validate_trace(trace))

    def test_stale_trace_cannot_score_as_current(self):
        provenance = profile_metadata(self.profile)
        provenance["checkout_dirty"] = False
        provenance["prompt_revision"] = "sha256:test"
        trace = make_trace(
            {"question": "q", "product": "blackduck-sca", "product_version": "2026.7"},
            {"answer": "a"}, provenance,
        )
        expected = dict(provenance)
        expected["source_revision"] = "new-tree"
        self.assertIn(
            "trace source_revision does not match the current evaluation profile",
            validate_trace(trace, expected),
        )

    def test_stale_prompt_trace_cannot_score_as_current(self):
        provenance = profile_metadata(self.profile)
        provenance["checkout_dirty"] = False
        provenance["prompt_revision"] = "sha256:old"
        trace = make_trace(
            {"question": "q", "product": "blackduck-sca", "product_version": "2026.7"},
            {"answer": "a"}, provenance,
        )
        expected = dict(provenance)
        expected["prompt_revision"] = "sha256:current"
        self.assertIn(
            "trace prompt_revision does not match the current evaluation profile",
            validate_trace(trace, expected),
        )

    def test_dirty_checkout_cannot_claim_a_current_trace(self):
        provenance = profile_metadata(self.profile)
        provenance["checkout_dirty"] = False
        provenance["prompt_revision"] = "sha256:test"
        trace = make_trace(
            {"question": "q", "product": "blackduck-sca", "product_version": "2026.7"},
            {"answer": "a"}, provenance,
        )
        expected = dict(provenance)
        expected["checkout_dirty"] = True
        self.assertIn("current checkout has tracked changes", validate_trace(trace, expected))


if __name__ == "__main__":
    unittest.main()
