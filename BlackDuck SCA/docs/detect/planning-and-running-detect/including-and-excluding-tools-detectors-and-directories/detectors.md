---
title: "Detectors"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detectors.html"
content_id: "gw22TvvZI2Sw5EEBpXzFQg"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:33.821939+00:00"
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
