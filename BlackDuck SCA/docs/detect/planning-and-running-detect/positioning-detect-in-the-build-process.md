---
title: "Positioning Detect in the build process"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/positioning-detect-in-the-build-process.html"
content_id: "TeKHB_FVtk8JLtDHXtmuKQ"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:27.541057+00:00"
---

# Positioning Detect in the build process

For best results, execute Detect post-build step in the build environment of the project.
Building your project prior to running Detect is required for many detectors to run successfully,
tends to produce the most accurate results, and helps ensure that the build artifacts are available for signature scanning.

When higher accuracy detectors are unable to run (due to, for example, the absence of package manager executables they need),
and a lower accuracy detector is also available,
Detect makes its best effort to discover dependencies by running the lower accuracy detector.

See Detector search and accuracy for more information.
