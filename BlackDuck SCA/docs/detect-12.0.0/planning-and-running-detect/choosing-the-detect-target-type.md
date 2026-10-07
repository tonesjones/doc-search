---
title: "Choosing the Detect target type"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/choosing-the-detect-target-type.html"
content_id: "OwsBcZHsQwCqfxSmNTanqg"
version: "12.0.0"
section: "Planning and running Detect"
scraped_at: "2026-10-04T23:33:19.602794+00:00"
content_hash: "4ca50c8c7ceeef15778e88265d53cdddf3359d2bb5b0661c9bfa45f0cca3b2ba"
---

# Choosing the Detect target type

Detect will select a workflow based in part on the target type you select via the detect.target.type property.

When running Detect on project source code, you can set *detect.target.type* to *SOURCE*, or leave *detect.target.type* unset (since *SOURCE* is the default value).

When running Detect on a Docker image, you will want to set *detect.target.type* to *IMAGE*.

## Common workflows

By default (detect.target.type=SOURCE), Detect will run the following on the source directory:

1. Any applicable detectors
2. Black Duck Signature Scanner

When a Docker image is provided and property *detect.target.type* is set to IMAGE, Detect will run the following on the image:

1. Docker Inspector
2. Black Duck Signature Scanner
3. Black Duck Binary Analysis
