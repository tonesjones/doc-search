---
title: "Caching configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/caching-configuration.html"
content_id: "BSnNC6cKmnAhILbijTT2nA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:20.476869+00:00"
---

# Caching configuration

Caching can be used by `capture` and `analysis`, or by `scan`.
The following configuration key enables or disables caching.

| Key | Type | Description |
| --- | --- | --- |
| `enabled` | Boolean | Enables or disables caching.  - `true` enables caching. - `false` disables caching.   Default: `true` |

## Clearing caches

The following option is for the CLI commands `capture` and `scan`.
It clears one or more of the current analysis caches.

Important:
To clear caches, you must have administrator privileges.

For more information about caching, please see "About Scan Service cache in Kubernetes" in the
Coverity Analysis 2026.6.0 User and Administrator Guide.

| Option | Value |
| --- | --- |
| `reset-cache` | all  Clears all cached items.  bytecode  Clears cached bytecode.  tu  Clears cached TUs. A "TU" is a Coverity callgraph metric that is described in the sections "Determining which functions are analyzed and called" and "Tags for phases of command-line transformations" (see the description of the `<trans>` tag). Both these sections are in the Coverity Analysis 2026.6.0 User and Administrator Guide.  wur  Clears cached analysis results. |

For example, the following invocation of `coverity capture` would clear the bytecode cache:

```
coverity capture -–reset-cache bytecode
```
