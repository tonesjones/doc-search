---
title: "Tools"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/tools.html"
content_id: "dS5GfwG0AOqFaHVuoSo7QA"
version: "12.0.0"
section: "Detect Components"
scraped_at: "2026-10-04T23:33:20.158017+00:00"
content_hash: "ae6556c48eced422fab159e70a192b66ca32fcad3f0b1f880b72ec274307a7d4"
---

# Tools

Each Detect run consists of running any applicable Detect tools.

The available Detect tools in order of potential execution, with the corresponding detect tools property
value specified in parentheses are:

- Docker Inspector (--detect.tools=DOCKER)
- Bazel (--detect.tools=BAZEL)
- Detector (--detect.tools=DETECTOR)
- Black Duck Signature Scanner (--detect.tools=SIGNATURE_SCAN)
- Black Duck - Binary Analysis (--detect.tools=BINARY_SCAN)
- IaC Scanner (--detect.tools=IAC_SCAN)
- Container Scan (--detect.tools=CONTAINER_SCAN)

The detector tool runs any applicable detectors.
