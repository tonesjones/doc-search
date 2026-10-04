"""Manifest publication survives temporary sharing locks without losing data."""
from pathlib import Path
import runpy
import tempfile
import unittest
from unittest.mock import patch

HELPERS = runpy.run_path(str(Path(__file__).resolve().parents[1] / "Coverity/scripts/corpus_utils.py"))


class AtomicManifestWriteTests(unittest.TestCase):
    def test_temporary_lock_then_publish(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text("old", encoding="utf-8")
            replace = HELPERS["os"].replace
            attempts = []

            def sharing_lock(source, target):
                attempts.append(target)
                if len(attempts) < 3:
                    raise PermissionError("sharing lock")
                return replace(source, target)

            with patch.object(HELPERS["os"], "replace", side_effect=sharing_lock), \
                 patch.object(HELPERS["time"], "sleep"):
                HELPERS["atomic_write_text"](path, "new")
            self.assertEqual(path.read_text(encoding="utf-8"), "new")
            self.assertEqual(list(Path(directory).iterdir()), [path])

    def test_persistent_lock_preserves_original(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text("old", encoding="utf-8")
            with patch.object(HELPERS["os"], "replace", side_effect=PermissionError("locked")), \
                 patch.object(HELPERS["time"], "sleep"), self.assertRaises(PermissionError):
                HELPERS["atomic_write_text"](path, "new")
            self.assertEqual(path.read_text(encoding="utf-8"), "old")
            self.assertEqual(list(Path(directory).iterdir()), [path])


if __name__ == "__main__":
    unittest.main()
