---
title: "Choosing the Detect target type"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/choosing-the-detect-target-type.html"
content_id: "OwsBcZHsQwCqfxSmNTanqg"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:31.295922+00:00"
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
