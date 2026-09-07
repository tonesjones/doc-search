from __future__ import annotations

import json
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from corpus_utils import content_hash, write_text_if_changed  # noqa: E402
from products import validate_registry  # noqa: E402
_validator_spec = importlib.util.spec_from_file_location("validate_corpus", SCRIPTS / "validate-corpus.py")
assert _validator_spec and _validator_spec.loader
_validator = importlib.util.module_from_spec(_validator_spec)
sys.modules[_validator_spec.name] = _validator
_validator_spec.loader.exec_module(_validator)
validate_corpus = _validator.validate_corpus


class CorpusToolTests(unittest.TestCase):
    def config(self) -> dict[str, dict]:
        return {
            "fixture": {
                "key": "fixture", "map_id": "map", "version": "1.0",
                "product": "fixture", "title": "Fixture", "source_dir": "sources/fixture",
                "docs_root": "fixture", "root_slugs": {}, "index_file": "index-fixture.md",
            }
        }

    def test_registry_rejects_colliding_generated_paths(self):
        for field, value in (("source_dir", "sources/fixture"), ("docs_root", "fixture"), ("index_file", "index-fixture.md")):
            with self.subTest(field=field):
                products = self.config()
                duplicate = {**products["fixture"], "key": "second", "source_dir": "sources/second",
                             "docs_root": "second", "index_file": "index-second.md"}
                duplicate[field] = value
                products["second"] = duplicate
                with self.assertRaisesRegex(ValueError, field):
                    validate_registry(products)

    def test_atomic_changed_only_write(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "generated.md"
            self.assertTrue(write_text_if_changed(path, "same\n"))
            self.assertFalse(write_text_if_changed(path, "same\n"))
            self.assertTrue(write_text_if_changed(path, "changed\n"))

    def test_validator_accepts_hashed_fixture_and_reports_orphan(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cfg = self.config()
            body = "\n# Topic\n\nBody"
            digest = content_hash(body)
            topic = {
                "id": "id-1", "title": "Topic", "section": "Guide", "sourceUrl": "https://example.test/topic",
                "localPath": "docs/fixture/topic.md", "status": "done", "contentHash": digest,
            }
            path = root / topic["localPath"]
            path.parent.mkdir(parents=True)
            path.write_text(
                "---\ntitle: \"Topic\"\nsource_url: \"https://example.test/topic\"\ncontent_id: \"id-1\"\n"
                "version: \"1.0\"\nsection: \"Guide\"\nscraped_at: \"2026-01-01T00:00:00Z\"\n"
                f"content_hash: \"{digest}\"\n---\n{body}\n", encoding="utf-8",
            )
            (root / "sources/fixture").mkdir(parents=True)
            manifest = {"productKey": "fixture", "mapId": "map", "version": "1.0", "topics": [topic],
                        "stats": {"total": 1, "pending": 0, "done": 1, "skipped": 0, "error": 0}}
            (root / "sources/fixture/manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            (root / "index-fixture.md").write_text("1/1 done\n- [Topic](docs/fixture/topic.md)\n", encoding="utf-8")
            (root / "corpus-status.md").write_text("[index-fixture.md](index-fixture.md)\n", encoding="utf-8")
            orphan = root / "docs/fixture/orphan.md"
            orphan.write_text("orphan\n", encoding="utf-8")
            result = validate_corpus(root, cfg)
            self.assertEqual(result.failures, [])
            self.assertTrue(any("orphan.md" in warning for warning in result.warnings))


if __name__ == "__main__":
    unittest.main()
