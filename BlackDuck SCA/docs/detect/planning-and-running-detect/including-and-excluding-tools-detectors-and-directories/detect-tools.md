---
title: "Detect Tools"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-tools.html"
content_id: "QpfLLQzKiQQTAJE5QEsIFw"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:33.199567+00:00"
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
