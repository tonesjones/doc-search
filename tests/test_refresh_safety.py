from __future__ import annotations

import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
PRODUCTS = ("BlackDuck SCA", "Bridge", "SRM")


def load_refresh(product):
    scripts = REPO / product / "scripts"
    previous = sys.modules.pop("products", None)
    sys.path.insert(0, str(scripts))
    try:
        spec = importlib.util.spec_from_file_location("refresh_under_test", scripts / "refresh-corpus.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)
        sys.modules.pop("products", None)
        if previous is not None:
            sys.modules["products"] = previous


class RefreshSafetyTests(unittest.TestCase):
    def test_dirty_generated_files_stop_before_any_refresh(self):
        for product in PRODUCTS:
            for relative in ("docs/topic.md", "docs/with space é.md", "index.md",
                             "sources/fixture/manifest.json", "sources/fixture/toc.json"):
                with self.subTest(product=product, path=relative), tempfile.TemporaryDirectory() as directory:
                    repo = Path(directory)
                    subprocess.run(["git", "init", "-q", str(repo)], check=True)
                    root = repo / product
                    topic = root / relative
                    topic.parent.mkdir(parents=True)
                    topic.write_text("local work", encoding="utf-8")
                    module = load_refresh(product)
                    with patch.object(module, "ROOT", root), patch.object(module, "REPO_ROOT", repo), \
                         patch.object(module, "existing_products", return_value=[]), \
                         patch.object(module, "describe_work") as describe, \
                         patch.object(module, "command") as command, \
                         patch.object(sys, "argv", ["refresh-corpus.py"]), \
                         contextlib.redirect_stderr(io.StringIO()):
                        self.assertEqual(module.main(), 2)
                        describe.assert_not_called()
                        command.assert_not_called()
                    self.assertEqual(topic.read_text(encoding="utf-8"), "local work")

    def test_unavailable_git_status_stops_before_refresh(self):
        for product in PRODUCTS:
            with self.subTest(product=product):
                module = load_refresh(product)
                failed = subprocess.CompletedProcess([], 128, "", "not a git repository")
                with patch.object(module.subprocess, "run", return_value=failed), \
                     patch.object(module, "existing_products", return_value=[]), \
                     patch.object(module, "describe_work") as describe, \
                     patch.object(module, "command") as command, \
                     patch.object(sys, "argv", ["refresh-corpus.py"]), \
                     contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(module.main(), 2)
                    describe.assert_not_called()
                    command.assert_not_called()

    def test_staged_rename_preserves_both_paths(self):
        for product in PRODUCTS:
            with self.subTest(product=product), tempfile.TemporaryDirectory() as directory:
                repo = Path(directory)
                subprocess.run(["git", "init", "-q", str(repo)], check=True)
                root = repo / product
                root.mkdir()
                old = root / "index.md"
                old.write_text("index", encoding="utf-8")
                subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
                subprocess.run(["git", "-C", str(repo), "-c", "user.name=Test", "-c",
                                "user.email=test@example.invalid", "commit", "-qm", "fixture"], check=True)
                subprocess.run(["git", "-C", str(repo), "mv", f"{product}/index.md",
                                f"{product}/notes.md"], check=True)
                module = load_refresh(product)
                with patch.object(module, "ROOT", root), patch.object(module, "REPO_ROOT", repo):
                    self.assertIn(f"{product}/index.md", module.protected_dirty_paths(module.git_status()))


if __name__ == "__main__":
    unittest.main()
