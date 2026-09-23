from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PROMOTION_SCRIPT = ROOT / "scripts" / "promote-candidate.py"
_spec = importlib.util.spec_from_file_location("promote_candidate", PROMOTION_SCRIPT)
promote_candidate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(promote_candidate)


def fixture() -> tuple[dict, dict, dict, dict]:
    expected_provenance = {
        "evaluation_profile": "test-sca-profile",
        "entrypoint": "test-router",
        "checkout_revision": "checkout-1",
        "checkout_dirty": False,
        "instruction_revision": "instructions-1",
        "source_revision": "sources-1",
        "prompt_revision": "sha256:prompt-1",
    }
    candidate = {
        "id": "feedback-version-availability-001",
        "question": "Can this checkout establish the requested product version?",
        "product": "blackduck-sca",
        "product_version": "2099.1",
        "verification_status": "candidate",
        "origin": "team-feedback",
    }
    approved = {
        **candidate,
        "expected_behavior": "abstain",
        "must_retrieve": [],
        "should_retrieve": [],
        "must_not_retrieve": [],
        "required_facts": [],
        "forbidden_facts": [],
        "source_evidence": [{
            "file": "evaluation/guidance/access-token-menu.md",
            "section": "# Current SCA access-token menu",
            "corpus_revision": "local-guidance",
        }],
        "verification_status": "verified",
        "verified_by": "human review",
        "origin": "team-feedback",
        "notes": "The selected local checkout does not establish this requested version.",
    }
    trace = {
        **expected_provenance,
        "answer_id": "answer-1",
        "timestamp": "2026-09-22T00:00:00Z",
        "original_query": approved["question"],
        "product": approved["product"],
        "requested_product_version": approved["product_version"],
        "answer": "This checkout does not establish the answer for that version.",
        "model": "gpt-6-luna",
        "model_parameters": {"model_reasoning_effort": "medium"},
        "retrieved_chunks": [],
        "citations": [],
        "checkout_dirty": False,
    }
    return candidate, approved, trace, expected_provenance


def promotion_errors(candidate: dict, approved: dict, trace: dict, provenance: dict) -> list[str]:
    return promote_candidate.promotion_errors(candidate, approved, trace, provenance)


class Ds08PromotionTests(unittest.TestCase):
    def test_cli_preview_writes_nothing_and_apply_appends_one_case(self) -> None:
        candidate, approved, trace, provenance = fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            candidate_path = root / "candidate.json"
            approved_path = root / "approved.json"
            trace_path = root / "trace.json"
            output_path = root / "regressions.jsonl"
            for path, value in ((candidate_path, candidate), (approved_path, approved), (trace_path, trace)):
                path.write_text(json.dumps(value), encoding="utf-8")
            argv = [
                "promote-candidate.py", "--candidate", str(candidate_path),
                "--candidate-id", candidate["id"], "--approved-case", str(approved_path),
                "--trace", str(trace_path), "--output", str(output_path),
            ]
            current = {key: value for key, value in provenance.items() if key != "prompt_revision"}
            with patch.object(promote_candidate, "profile_metadata", return_value=current), \
                    patch.object(promote_candidate, "prompt_revision", return_value=provenance["prompt_revision"]):
                with patch("sys.argv", argv), redirect_stdout(io.StringIO()) as preview:
                    self.assertEqual(promote_candidate.main(), 0)
                self.assertEqual(preview.getvalue().strip(),
                                 "PROMOTION GATE: PASS (dry run; use --apply to append the verified case)")
                self.assertFalse(output_path.exists())
                with patch("sys.argv", argv + ["--apply"]), redirect_stdout(io.StringIO()) as applied:
                    self.assertEqual(promote_candidate.main(), 0)
            self.assertEqual(applied.getvalue().strip(),
                             f"PROMOTION GATE: PASS (promoted {approved['id']})")
            self.assertEqual([json.loads(line)["id"] for line in output_path.read_text(encoding="utf-8").splitlines()],
                             [approved["id"]])

    def test_matching_candidate_approved_case_and_trace_pass(self) -> None:
        candidate, approved, trace, provenance = fixture()

        self.assertEqual(promotion_errors(candidate, approved, trace, provenance), [])

    def test_candidate_and_approved_ids_must_match(self) -> None:
        candidate, approved, trace, provenance = fixture()
        approved["id"] = "feedback-version-availability-002"

        self.assertEqual(promotion_errors(candidate, approved, trace, provenance), [
            "candidate and approved case IDs differ",
        ])

    def test_approved_case_requires_explicit_product_version(self) -> None:
        candidate, approved, trace, provenance = fixture()
        del approved["product_version"]

        self.assertEqual(promotion_errors(candidate, approved, trace, provenance), [
            "approved case has no explicit product_version",
            "candidate and approved case differ on product_version",
            "production trace requested product version does not match approved case",
        ])

    def test_missing_or_wrong_replay_version_is_rejected(self) -> None:
        candidate, approved, trace, provenance = fixture()
        del trace["requested_product_version"]
        missing = promotion_errors(candidate, approved, trace, provenance)
        trace["requested_product_version"] = "2099.2"
        wrong = promotion_errors(candidate, approved, trace, provenance)

        expected = ["production trace requested product version does not match approved case"]
        self.assertEqual(missing, expected)
        self.assertEqual(wrong, expected)

    def test_replay_requires_model_metadata(self) -> None:
        candidate, approved, trace, provenance = fixture()
        del trace["model"]
        del trace["model_parameters"]

        self.assertEqual(promotion_errors(candidate, approved, trace, provenance), [
            "production trace has no model",
            "production trace has no model parameters",
        ])

    def test_stale_profile_checkout_source_or_prompt_revision_is_rejected(self) -> None:
        candidate, approved, trace, provenance = fixture()
        results = []
        for field in ("checkout_revision", "source_revision", "prompt_revision"):
            stale_trace = json.loads(json.dumps(trace))
            stale_trace[field] = "stale-revision"
            results.append(promotion_errors(candidate, approved, stale_trace, provenance))

        self.assertEqual(results, [["production replay did not pass: METADATA_FAILURE"]] * 3)

    def test_replay_must_use_selected_entrypoint(self) -> None:
        candidate, approved, trace, provenance = fixture()
        trace["entrypoint"] = "other-router"

        self.assertEqual(promotion_errors(candidate, approved, trace, provenance), [
            "production trace entrypoint does not match evaluation profile",
        ])

    def test_dirty_trace_and_current_checkout_are_rejected(self) -> None:
        candidate, approved, trace, provenance = fixture()
        trace["checkout_dirty"] = True
        dirty_trace = promotion_errors(candidate, approved, trace, provenance)
        trace["checkout_dirty"] = False
        dirty_current_checkout = {**provenance, "checkout_dirty": True}

        self.assertEqual(dirty_trace, ["production replay did not pass: METADATA_FAILURE"])
        self.assertEqual(promotion_errors(candidate, approved, trace, dirty_current_checkout), [
            "production replay did not pass: METADATA_FAILURE",
        ])


if __name__ == "__main__":
    unittest.main()
