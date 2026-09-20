from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CORPORA = ("BlackDuck SCA", "Bridge", "Coverity", "Polaris", "Sigma", "Signal", "SRM")


def main() -> int:
    jobs = [("Regression tests", ROOT, ["-m", "unittest", "discover", "-s", "tests", "-v"])]
    for product in ("BlackDuck SCA", "Bridge", "SRM"):
        jobs.append((f"{product} tool tests", ROOT / product,
                     ["-m", "unittest", "discover", "-s", "tests", "-v"]))
    for product in CORPORA:
        jobs.append((f"{product} corpus integrity", ROOT / product, ["scripts/validate-corpus.py"]))
    for product in ("Polaris", "Sigma", "Signal"):
        jobs.append((f"{product} retrieval", ROOT / product, ["scripts/smoke-retrieval.py"]))
    jobs.append(("SCA integrity and retrieval report", ROOT, ["BlackDuck SCA/verification/verify.py"]))

    results = []
    for name, directory, args in jobs:
        result = subprocess.run(
            [sys.executable, "-B", *args], cwd=directory, capture_output=True,
            text=True, encoding="utf-8", errors="replace",
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"},
        )
        status = "PASS" if result.returncode == 0 else "FAIL"
        results.append((name, status))
        print(f"{status}: {name}", flush=True)
        print(result.stdout + result.stderr, end="", flush=True)

    print("\nOffline summary")
    for name, status in results:
        print(f"{status}: {name}")
    print("NOT_RUN: Upstream freshness")
    print("NOT_RUN: Live UI and API behavior")
    print("NOT_RUN: Customer-answer accuracy evaluation")
    return int(any(status == "FAIL" for _, status in results))


if __name__ == "__main__":
    raise SystemExit(main())
