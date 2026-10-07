---
title: "Detect Tools"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-tools.html"
content_id: "QpfLLQzKiQQTAJE5QEsIFw"
version: "12.0.0"
section: "Planning and running Detect"
scraped_at: "2026-10-04T23:33:19.691212+00:00"
content_hash: "717cf9bc427f4cf234c5a47d41817ef77b6b0a893a30e8d71fa5275acb581acb"
---

# Detect Tools

By default, all detection tools are eligible to run; the set of tools that will run
depends on your configuration, type of files you are scanning, and the properties you set.

When no `--detect.tools=` parameter or the `--detect.tools=ALL` parameter is provided, Black Duck® Detect will attempt to run all tools for which the tool itself is available, the configuration parameters are set, and any required dependencies are met. The existence of applicable file types (for scanning), will also determine whether tools return results when they run.

If you wish to specifically determine which tools are run, use the following command to list the tools:

```
--detect.tools={comma-separated list of tool names in uppercase}
```

To exclude specific tools from execution, use:

```
--detect.tools.excluded={comma-separated list of tool names, all uppercase}
```

Note: Exclusions take precedence over inclusions.

Refer to Tools for the list of tool names.

Refer to Properties for additional details.

Note: Some Detect tools may be appropriate to run independantly of others for reporting purposes, or require a specific Black Duck SCA license.
