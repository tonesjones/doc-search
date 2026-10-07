---
title: "Detectors"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detectors.html"
content_id: "gw22TvvZI2Sw5EEBpXzFQg"
version: "12.0.0"
section: "Planning and running Detect"
scraped_at: "2026-10-04T23:33:19.710175+00:00"
content_hash: "cba97efff4374546a03aa999c1fae6f7f05eab2b8f6c3556c31b36fa6a2fc870"
---

# Detectors

By default, all detectors are eligible to run to find and extract dependencies from supported package managers.
The set of detectors that actually run depends on the files existing in your project directory, the properties you set, and whether the detector requirements are met.

To limit the eligible detectors to a given list, use:

```
--detect.included.detector.types={comma-separated list of detector names}
```

To exclude specific detectors, use:

```
--detect.excluded.detector.types={comma-separated list of detector names}
```

Note: Exclusions take precedence over inclusions.

Refer to Detectors for the list of detector names.

Refer to Properties for details.
