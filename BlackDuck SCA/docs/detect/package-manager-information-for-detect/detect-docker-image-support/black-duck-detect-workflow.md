---
title: "Black Duck® Detect workflow"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/black-duck-detect-workflow.html"
content_id: "sSya0Y~lxx3lD9hF5CCzeg"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:56.074586+00:00"
---

# Black Duck® Detect workflow

When running Black Duck® Detect on a Docker image, you'll probably want to
set *detect.target.type* to *IMAGE*.

When a Docker image is provided and property *detect.target.type* is set to IMAGE, Detect will run:

1. Docker Inspector (on the image)
2. Black Duck Signature Scanner (on the image)
3. Black Duck Binary Analysis (on the image)

When a Docker Image is provided and property *detect.target.type* is set to *SOURCE* (the default), Detect will run:

1. Docker Inspector (on the image)
2. Any applicable detectors (on the source directory)
3. Black Duck Signature Scanner (on the image)
4. Black Duck Binary Analysis (on the image)

Detect by default runs
the Black Duck Signature Scanner on an image built from the "container file system".
This image is referred to as
the squashed image (because it has only one layer, to eliminate the chance of false positives from lower layers).
This scan creates another code location.

Detect by default
runs Black Duck Binary Analysis on the container file system.
Refer to Detect's scan target for more details.
This also creates a code location.
