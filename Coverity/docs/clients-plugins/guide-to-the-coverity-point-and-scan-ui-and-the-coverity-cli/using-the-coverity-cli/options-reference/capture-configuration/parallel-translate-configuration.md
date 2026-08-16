---
title: "Parallel translate configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parallel-translate-configuration.html"
content_id: "IRDb31zJMJa1tzNuJIrt1w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:05.277166+00:00"
---

# Parallel translate configuration

The following fields specify how to parallelize translation of C and C++ code.

| Key | Type | Description |
| --- | --- | --- |
| `enabled` | Boolean | Specifies whether `cov-translate` parallelization should be enabled. |
| `processes` | integer | Specifies the number of `cov-emit` processes to be run in parallel by `cov-translate` when multiple files are seen on a single native compiler invocation. A value of `0` will use the number of logical processors in the machine. |
