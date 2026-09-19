"""Produce an offline SCA verification report without changing the corpus."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
PRODUCT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRODUCT_ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("sca_corpus_validator", PRODUCT_ROOT / "scripts/validate-corpus.py")
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)

CASES = (
    ("SCA project creation", "index.md", "docs/help-center/understanding-projects-in-black-duck/creating-a-project.md", "2026.7", "project"),
    ("Detect 12 rapid scan", "index-detect-12.0.0.md", "docs/detect-12.0.0/planning-and-running-detect/rapid-scan.md", "12.0.0", "--detect.blackduck.scan.mode=RAPID"),
    ("Detect 11 historical rapid scan", "index-detect-11.5.1.md", "docs/detect/planning-and-running-detect/rapid-scan.md", "11.5.1", "--detect.blackduck.scan.mode=RAPID"),
    ("Alert distribution jobs", "index-alert.md", "docs/alert/post-installation-configuration/configuring-distribution-jobs.md", "8.4.0", "Distribution"),
)


def verify(root: Path) -> dict:
    report = dict(product="black-duck-sca", version="2026.7", checks=[], evidence=[], failures=[], status="PASS")

    def record(name, category, failures, evidence=()):
        report["checks"].append(dict(name=name, category=category, status="FAIL" if failures else "PASS"))
        report["failures"].extend(f"{name}: {failure}" for failure in failures)
        if not failures:
            report["evidence"].extend(evidence)

    try:
        result = validator.validate_corpus(root)
        record("SCA corpus integrity", "corpus", result.failures)
        report["evidence"].extend(f"Warning: {warning}" for warning in result.warnings)
        report["evidence"].extend(f"Corpus {key}: {cfg['version']}" for key, cfg in validator.PRODUCTS.items()
                                  if (root / cfg["source_dir"] / "manifest.json").is_file())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        record("SCA corpus integrity", "corpus", [str(exc)])

    for name, index, topic, version, phrase in CASES:
        try:
            catalog = (root / index).read_text(encoding="utf-8")
            text = validator.filesystem_path(root / topic).read_text(encoding="utf-8")
            meta, body = validator.parse_front_matter(text)
            failures = []
            if f"]({topic})" not in catalog:
                failures.append(f"{index} does not link to {topic}")
            if not meta or meta.get("version") != version:
                failures.append(f"{topic} does not declare version {version}")
            if not body or phrase not in body:
                failures.append(f"{topic} lacks expected topic content")
            record(name, "retrieval", failures, [f"{index} -> {topic} [{version}]"])
        except (OSError, ValueError) as exc:
            record(name, "retrieval", [str(exc)])

    try:
        routing = (root / "index-detect.md").read_text(encoding="utf-8")
        default_section = routing.split("## Default: Detect 12.0.0", 1)[1].split("## ", 1)[0]
        failures = [] if "](index-detect-12.0.0.md)" in default_section else ["Default catalog is not Detect 12.0.0"]
        record("Detect default routing", "retrieval", failures, ["index-detect.md default section selects Detect 12.0.0"])
    except (OSError, ValueError, IndexError) as exc:
        record("Detect default routing", "retrieval", [str(exc)])

    for name in ("Live UI", "Live API"):
        report["checks"].append(dict(name=name, category="live", status="NOT_RUN"))
    report["evidence"].append("Offline checks only. No live UI or API verification was performed.")
    if report["failures"]:
        report["status"] = "FAIL"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=PRODUCT_ROOT, help="SCA corpus directory to inspect")
    args = parser.parse_args()
    report = verify(args.root.resolve())
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return int(report["status"] == "FAIL")


if __name__ == "__main__":
    raise SystemExit(main())
