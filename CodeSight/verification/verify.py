#!/usr/bin/env python3
"""Run offline integrity and retrieval checks for the Code Sight corpus."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    ("Code Sight corpus integrity", "corpus", "scripts/validate-corpus.py"),
    ("Code Sight retrieval smoke checks", "retrieval", "scripts/smoke-retrieval.py"),
)


def main() -> int:
    results: list[dict[str, str]] = []
    evidence: list[str] = []
    failures: list[str] = []

    for name, category, script in CHECKS:
        result = subprocess.run(
            [sys.executable, "-B", script],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"},
        )
        status = "PASS" if result.returncode == 0 else "FAIL"
        results.append({"name": name, "category": category, "status": status})
        detail = (result.stdout + result.stderr).strip()
        evidence.append(f"{name}: {detail or status}")
        if status == "FAIL":
            failures.append(f"{name} failed with exit code {result.returncode}")

    report = {
        "product": "codesight",
        "version": "2026.9.0",
        "checks": results,
        "evidence": evidence,
        "failures": failures,
        "status": "FAIL" if failures else "PASS",
    }
    print(json.dumps(report, ensure_ascii=False))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
