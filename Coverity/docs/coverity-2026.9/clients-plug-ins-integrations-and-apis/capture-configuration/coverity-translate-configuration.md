---
title: "Coverity translate configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/coverity-translate-configuration.html"
content_id: "vRgpzWVhAbjDr8ynenPeEw"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:03.525240+00:00"
---

# Coverity translate configuration

The following keys configure `cov-translate` capture.

Attention:
For the Coverity CLI, `cov-translate` is supported only on macOS systems.

| Key | Type | Description |
| --- | --- | --- |
| `command` | String | Specifies a command that will invoke `cov-translate` in cases where the user is doing a `cov-translate` capture. |
| `cov-build-args` | array of strings | Additional arguments to pass to `cov-build` when doing build capture. |
| `defer-decomp` | Boolean | Specifies whether the build should only record the decompilations of byte code during the build and not attempt to decompile and emit the byte code. During the analysis phase, `cov-build` will be rerun with --replay-decomp to decompile and emit the byte code. |
| `parallel-translate` | Parallel translate configuration | Specifies how to parallelize translation of C and C++ code. |
| `scan-transparency` | Boolean | Specifies whether to enable the collection of scan transparency data for `cov-translate` capture. This setting must be enabled if the Coverity Connect instance has `scan.transparency.enabled=true` in its configuration. For more information, see "Enabling collection of scan transparency data" in the Coverity Platform User and Administrator Guide.  Default: `true` |
