"""Keep local reference notes when official Signal navigation changes."""
import json
from pathlib import Path
import subprocess
import sys
import unittest


class SignalRefreshTests(unittest.TestCase):
    def test_local_note_survives_repeated_toc_refresh(self):
        script = """
import json, runpy, sys
sys.path.insert(0, 'scripts')
merge = runpy.run_path('scripts/build-index.py')['merge_statuses']
note = {'id':'local-signal-cli-reference', 'title':'Local notes',
        'localPath':'docs/reference/signal-cli-local-notes.md', 'status':'done'}
old = {'topics':[note, {'id':'removed-official-topic', 'status':'done'}]}
first = merge([{'id':'new-official-topic', 'status':'pending'}], old)
second = merge([{'id':'new-official-topic', 'status':'pending'}], {'topics':first})
print(json.dumps({'first':first, 'second':second}))
"""
        expected = [
            {"id": "new-official-topic", "status": "pending"},
            {"id": "local-signal-cli-reference", "title": "Local notes",
             "localPath": "docs/reference/signal-cli-local-notes.md", "status": "done"},
        ]
        for corpus in ("Signal", "BlackDuck SCA"):
            with self.subTest(corpus=corpus):
                result = subprocess.run([sys.executable, "-B", "-c", script],
                                        cwd=Path(__file__).resolve().parents[1] / corpus,
                                        capture_output=True, text=True, check=True)
                data = json.loads(result.stdout)
                self.assertEqual(data["first"], expected)
                self.assertEqual(data["second"], expected)


if __name__ == "__main__":
    unittest.main()
