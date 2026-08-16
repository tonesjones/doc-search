---
title: "Tools"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/tools.html"
content_id: "dS5GfwG0AOqFaHVuoSo7QA"
version: "11.5.1"
section: "Detect Components"
scraped_at: "2026-08-08T23:44:45.506042+00:00"
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
