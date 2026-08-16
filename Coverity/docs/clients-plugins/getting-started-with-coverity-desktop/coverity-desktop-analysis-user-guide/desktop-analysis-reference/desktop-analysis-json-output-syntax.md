---
title: "Desktop Analysis JSON output syntax"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/desktop-analysis-json-output-syntax.html"
content_id: "OLjZNRnKIjZ4Uo4_WpAxuQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:03.915737+00:00"
---

# Desktop Analysis JSON output syntax

When specified with the `--json-output-v10` option,
`cov-run-desktop` will write its output to a [JSON](http://www.json.org/)  file. This
section describes the objects and attributes of the JSON output in detail.

Note: `--json-output-v1` through `--json-output-v9` are supported
for backward compatibility. It is recommended that you use
`--json-output-v10` in order to see the most complete set of
information.

The structure of the JSON output (v10) is represented below.

[image: image]
