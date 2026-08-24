from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from evaluation.core import ROOT, adapter_payload, load_jsonl, redact, score_case, validate_trace, verify_case_evidence
from scripts.codex_production_adapter import corpus_paths, parse_event_stream


class EvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = load_jsonl(ROOT / "evaluation" / "cases" / "baseline.jsonl")

    def test_verified_baseline_has_expected_size(self):
        self.assertGreaterEqual(len(self.cases), 20)
        self.assertTrue(all(case["verification_status"] == "verified" for case in self.cases))

    def test_all_evidence_and_exact_facts_are_verifiable(self):
        errors = {case["id"]: verify_case_evidence(case) for case in self.cases}
        self.assertEqual({key: value for key, value in errors.items() if value}, {})

    def test_adapter_payload_cannot_leak_benchmark_answers(self):
        case = self.cases[0]
        payload = adapter_payload(case)
        self.assertEqual(set(payload), {"question", "product", "product_version"})
        encoded = json.dumps(payload)
        self.assertNotIn(case["id"], encoded)
        self.assertNotIn("required_facts", encoded)
        self.assertNotIn("source_evidence", encoded)

    def test_good_trace_passes_deterministic_layers(self):
        case = next(item for item in self.cases if item["id"] == "signal-002")
        trace = {
            "answer_id": "ans-fixture-good",
            "timestamp": "2026-08-23T00:00:00Z",
            "original_query": case["question"],
            "product": "signal",
            "answer": "Use BRIDGE_SIGNAL_LLM_KEY.",
            "retrieved_chunks": [{
                "file": "Signal/docs/reference/reference-guide.md", "rank": 1,
                "content": "LLM API key BRIDGE_SIGNAL_LLM_KEY", "metadata": {"version": "latest"},
            }],
            "citations": [{"file": "Signal/docs/reference/reference-guide.md"}],
            "latency_ms": 5,
        }
        result = score_case(case, trace)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["recall_at"]["1"], 1.0)

    def test_wrong_source_is_retrieval_failure_even_if_answer_contains_fact(self):
        case = next(item for item in self.cases if item["id"] == "signal-002")
        trace = {
            "answer_id": "ans-fixture-wrong-source", "timestamp": "2026-08-23T00:00:00Z",
            "original_query": case["question"], "product": "signal",
            "answer": "Use BRIDGE_SIGNAL_LLM_KEY.",
            "retrieved_chunks": [{"file": "Sigma/docs/user-guide/command-reference/the-analyze-subcommand.md", "rank": 1, "content": "BRIDGE_SIGNAL_LLM_KEY"}],
            "citations": [],
        }
        result = score_case(case, trace)
        self.assertIn("RETRIEVAL_FAILURE", result["failures"])
        self.assertEqual(result["status"], "FAIL")

    def test_invalid_citation_cannot_be_overridden(self):
        case = next(item for item in self.cases if item["id"] == "signal-002")
        trace = {
            "answer_id": "ans-fixture-bad-cite", "timestamp": "2026-08-23T00:00:00Z",
            "original_query": case["question"], "product": "signal",
            "answer": "Use BRIDGE_SIGNAL_LLM_KEY.",
            "retrieved_chunks": [{"file": "Signal/docs/reference/reference-guide.md", "content": "BRIDGE_SIGNAL_LLM_KEY"}],
            "citations": [{"file": "does/not/exist.md"}],
        }
        result = score_case(case, trace)
        self.assertIn("CITATION_FAILURE", result["failures"])

    def test_missing_citation_is_a_failure_for_answer_cases(self):
        case = next(item for item in self.cases if item["id"] == "signal-002")
        trace = {
            "answer_id": "ans-fixture-no-cite", "timestamp": "2026-08-23T00:00:00Z",
            "original_query": case["question"], "product": "signal",
            "answer": "Use BRIDGE_SIGNAL_LLM_KEY.",
            "retrieved_chunks": [{"file": case["must_retrieve"][0], "content": "BRIDGE_SIGNAL_LLM_KEY"}],
            "citations": [],
        }
        result = score_case(case, trace)
        self.assertIn("CITATION_FAILURE", result["failures"])

    def test_abstention_failure_is_severe(self):
        case = next(item for item in self.cases if item["id"] == "signal-006")
        trace = {
            "answer_id": "ans-fixture-hallucination", "timestamp": "2026-08-23T00:00:00Z",
            "original_query": case["question"], "product": "signal",
            "answer": "Git submodules will be supported on January 1, 2027.",
            "retrieved_chunks": [{"file": case["must_retrieve"][0], "content": "Scanning Git submodules is not yet supported."}],
            "citations": [],
        }
        result = score_case(case, trace)
        self.assertIn("ABSTENTION_FAILURE", result["failures"])
        self.assertIn("UNSUPPORTED_CLAIM", result["failures"])

    def test_trace_requires_reconstruction_fields(self):
        errors = validate_trace({"answer": "x"})
        self.assertIn("trace missing string answer_id", errors)
        self.assertIn("trace missing string original_query", errors)

    def test_secret_redaction_covers_headers_fields_and_assignments(self):
        value = {
            "authorization": "Bearer top-secret-token",
            "nested": {"password": "hunter2"},
            "log": "BRIDGE_POLARIS_ACCESSTOKEN=abc123 next",
        }
        cleaned = redact(value)
        self.assertEqual(cleaned["authorization"], "[REDACTED]")
        self.assertEqual(cleaned["nested"]["password"], "[REDACTED]")
        self.assertNotIn("abc123", cleaned["log"])

    def test_feedback_conversion_stays_candidate(self):
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            traces = temp / "traces"
            traces.mkdir()
            (traces / "ans-test.json").write_text(json.dumps({
                "answer_id": "ans-test", "original_query": "A reported question?",
                "product": "signal", "requested_product_version": "latest",
                "corpus_revision": "fixture",
            }), encoding="utf-8")
            feedback = temp / "feedback.json"
            feedback.write_text(json.dumps({
                "answer_id": "ans-test", "category": "Factually incorrect", "comment": "Needs review",
            }), encoding="utf-8")
            output = temp / "candidate.jsonl"
            completed = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "feedback-to-eval.py"), str(feedback),
                "--feedback-id", "42", "--trace-dir", str(traces), "--output", str(output),
            ], text=True, capture_output=True, check=False)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            candidate = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(candidate["verification_status"], "candidate")
            self.assertEqual(candidate["origin"], "team-feedback")

    def test_sca_baseline_has_verified_evidence(self):
        cases = load_jsonl(ROOT / "evaluation" / "cases" / "sca-baseline.jsonl")
        self.assertGreaterEqual(len(cases), 20)
        self.assertTrue(all(case["product"] == "blackduck-sca" for case in cases))
        errors = {case["id"]: verify_case_evidence(case) for case in cases}
        self.assertEqual({key: value for key, value in errors.items() if value}, {})

    def test_verified_sca_feedback_regressions_have_evidence(self):
        cases = load_jsonl(ROOT / "evaluation" / "cases" / "sca-regressions.jsonl")
        self.assertGreaterEqual(len(cases), 1)
        self.assertTrue(all(case["origin"] == "team-feedback" for case in cases))
        self.assertTrue(all(case["verification_status"] == "verified" for case in cases))
        errors = {case["id"]: verify_case_evidence(case) for case in cases}
        self.assertEqual({key: value for key, value in errors.items() if value}, {})

    def test_sca_human_review_packet_covers_every_baseline_case_once(self):
        cases = load_jsonl(ROOT / "evaluation" / "cases" / "sca-baseline.jsonl")
        adjudications = load_jsonl(ROOT / "evaluation" / "reviews" / "sca-baseline-adjudications.jsonl")
        self.assertEqual([item["case_id"] for item in adjudications], [case["id"] for case in cases])
        packet = (ROOT / "evaluation" / "reviews" / "sca-baseline-human-review.md").read_text(encoding="utf-8")
        for case in cases:
            self.assertEqual(packet.count(f'<a id="case-{case["id"]}"></a>'), 1)

    def test_unreviewed_adjudications_cannot_claim_a_verdict(self):
        adjudications = load_jsonl(ROOT / "evaluation" / "reviews" / "sca-baseline-adjudications.jsonl")
        for item in adjudications:
            if item["review_status"] == "UNREVIEWED":
                self.assertIsNone(item["verdict"])

    def test_corpus_correctness_conflicts_remain_unpromoted_candidates(self):
        candidates = load_jsonl(ROOT / "evaluation" / "reviews" / "corpus-correctness-candidates.jsonl")
        self.assertGreaterEqual(len(candidates), 1)
        for item in candidates:
            self.assertEqual(item["status"], "candidate")
            self.assertFalse(item["automatic_change_allowed"])
            self.assertTrue(item["verification_required"])

    def test_human_review_refresh_preserves_existing_decisions(self):
        script = ROOT / "scripts" / "build-human-review-packet.py"
        spec = importlib.util.spec_from_file_location("build_human_review_packet", script)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cases = [{"id": "case-a"}, {"id": "case-b"}]
        existing = module.blank_adjudication("case-a")
        existing.update({
            "review_status": "REVIEWED",
            "verdict": "TRUE_PASS",
            "reviewer": "human",
            "reviewed_at": "2026-08-24T00:00:00Z",
        })
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "adjudications.jsonl"
            path.write_text(json.dumps(existing) + "\n", encoding="utf-8")
            refreshed = module.load_or_initialize_adjudications(path, cases)
        self.assertEqual(refreshed[0], existing)
        self.assertEqual(refreshed[1]["case_id"], "case-b")
        self.assertEqual(refreshed[1]["review_status"], "UNREVIEWED")

    def test_production_adapter_parses_ranked_sca_context_and_citations(self):
        path = "BlackDuck SCA/docs/api/authenticating-with-the-api.md"
        events = "\n".join([
            json.dumps({"type": "item.completed", "item": {
                "type": "command_execution", "command": f"Get-Content '{path}'",
                "aggregated_output": f"{path}: POST /api/tokens/authenticate",
            }}),
            json.dumps({"type": "item.completed", "item": {
                "type": "agent_message", "text": f"Use the endpoint. [{path}]({path})",
            }}),
            json.dumps({"type": "turn.completed", "usage": {"input_tokens": 10}}),
        ])
        result = parse_event_stream(events)
        self.assertEqual(result["retrieved_chunks"][0]["file"], path)
        self.assertEqual(result["retrieved_chunks"][0]["rank"], 1)
        self.assertEqual(result["citations"], [{"file": path}])
        self.assertEqual(result["adapter_metadata"]["usage"]["input_tokens"], 10)

    def test_adapter_path_parser_rejects_non_sca_and_missing_files(self):
        text = "Signal/docs/reference/reference-guide.md BlackDuck SCA/docs/nope.md"
        self.assertEqual(corpus_paths(text), [])


if __name__ == "__main__":
    unittest.main()
