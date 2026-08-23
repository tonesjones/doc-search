#!/usr/bin/env python3
"""Run one real production answer command and store a redaction-safe raw trace."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluation.core import BASELINE_PATH, dump_json, load_json, make_trace, run_adapter  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--question", required=True)
    parser.add_argument("--product", required=True)
    parser.add_argument("--product-version")
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "evaluation" / "traces")
    parser.add_argument("adapter", nargs=argparse.REMAINDER, help="Production command after --")
    args = parser.parse_args()
    command = args.adapter[1:] if args.adapter[:1] == ["--"] else args.adapter
    if not command:
        parser.error("a production adapter command is required")
    case = {"question": args.question, "product": args.product, "product_version": args.product_version}
    trace = make_trace(case, run_adapter(command, case, args.timeout), load_json(BASELINE_PATH))
    path = args.output_dir / f"{trace['answer_id']}.json"
    dump_json(path, trace)
    print(trace["answer_id"])
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

