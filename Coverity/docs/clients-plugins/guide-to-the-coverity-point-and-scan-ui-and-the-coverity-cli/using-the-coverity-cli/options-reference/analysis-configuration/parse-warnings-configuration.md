---
title: "Parse warnings configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parse-warnings-configuration.html"
content_id: "WQi4Tjb_apSrCc3BBi1iAw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:15.205985+00:00"
---

# Parse warnings configuration

The key described here specifies how parse warnings are handled.

| Key | Type | Description |
| --- | --- | --- |
| `enabled` | Boolean | When `true`, enables parse warnings, recovery warnings, and semantic warnings that are produced by the `cov-build` command so that they appear as defects in Coverity Connect. By default, parse warnings are disabled if the aggressiveness level is `low`, and enabled if the aggressiveness level is `medium` or `high`. |
