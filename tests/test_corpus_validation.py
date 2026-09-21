import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPORA = ("Coverity", "Sigma", "Signal")
DIGEST = hashlib.sha256(b"\n# Topic\n\nBody").hexdigest()


class CorpusValidationTests(unittest.TestCase):
    def run_fixture(self, corpus, *, stored=DIGEST, backfill=False, failure=False, long_path=False):
        temp_parent = tempfile.gettempdir()
        if sys.platform == "win32":
            temp_parent = "\\\\?\\" + temp_parent
        with tempfile.TemporaryDirectory(dir=temp_parent) as directory:
            root = Path(directory.removeprefix("\\\\?\\"))
            scripts = root / "scripts"
            scripts.mkdir()
            for name in ("validate-corpus.py", "corpus_utils.py", "products.py"):
                shutil.copyfile(ROOT / corpus / "scripts" / name, scripts / name)
            manifest_source = next((ROOT / corpus / "sources").glob("*/manifest.json"))
            manifest = json.loads(manifest_source.read_text(encoding="utf-8"))
            local = "docs/topic.md"
            if long_path:
                local = "docs/" + "/".join(["deep-topic" * 5] * 5) + "/topic.md"
                self.assertGreater(len(str(root / local)), 260)
            topic = {"status": "done", "localPath": local}
            if stored is not None:
                topic["contentHash"] = stored
            manifest["topics"] = [topic]
            if failure:
                manifest["topics"].append({"status": "done", "localPath": "docs/missing.md"})
            manifest["stats"] = {"done": len(manifest["topics"])}
            path = root / local
            if long_path:
                path = Path("\\\\?\\" + str(path))
            path.parent.mkdir(parents=True)
            path.write_bytes(
                b'---\r\ntitle: "Topic"\r\nsource_url: "https://example.test"\r\n'
                b'content_id: "id"\r\nversion: "1"\r\nsection: "Guide"\r\n'
                b'scraped_at: "2026-01-01"\r\n---\r\n\r\n# Topic\r\n\r\nBody\r\n\r\n'
            )
            target = root / "sources" / manifest_source.parent.name / "manifest.json"
            target.parent.mkdir(parents=True)
            target.write_text(json.dumps(manifest), encoding="utf-8")
            before = target.read_bytes()
            command = [sys.executable, "-B", str(scripts / "validate-corpus.py")]
            if backfill:
                command.append("--backfill-hashes")
            result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8",
                                    env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
            return result, before, target.read_bytes()

    def test_normalized_body_hash_is_unchanged(self):
        for corpus in CORPORA:
            with self.subTest(corpus=corpus):
                result, before, after = self.run_fixture(corpus)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(before, after)

    @unittest.skipUnless(sys.platform == "win32", "Windows extended-length paths")
    def test_cli_reads_long_windows_topic_path(self):
        for corpus in CORPORA:
            with self.subTest(corpus=corpus):
                result, before, after = self.run_fixture(corpus, long_path=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(before, after)

    def test_backfill_fills_absent_hash(self):
        for corpus in CORPORA:
            with self.subTest(corpus=corpus):
                result, _, after = self.run_fixture(corpus, stored=None, backfill=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(after)["topics"][0]["contentHash"], DIGEST)

    def test_backfill_rejects_existing_mismatch_without_writing(self):
        for corpus in CORPORA:
            with self.subTest(corpus=corpus):
                result, before, after = self.run_fixture(corpus, stored="0" * 64, backfill=True)
                self.assertEqual(result.returncode, 1)
                self.assertIn("content hash mismatch", result.stderr)
                self.assertEqual(before, after)

    def test_backfill_does_not_write_when_another_topic_fails(self):
        for corpus in CORPORA:
            with self.subTest(corpus=corpus):
                result, before, after = self.run_fixture(corpus, stored=None, backfill=True, failure=True)
                self.assertEqual(result.returncode, 1)
                self.assertIn("missing file", result.stderr)
                self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
