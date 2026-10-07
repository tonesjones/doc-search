---
title: "Desktop Analysis JSON output syntax"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/desktop-analysis-json-output-syntax.html"
content_id: "OLjZNRnKIjZ4Uo4_WpAxuQ"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:07.636780+00:00"
---

# Desktop Analysis JSON output syntax

When specified with the `--json-output-v11` option,
`cov-run-desktop` will write its output to a [JSON](http://www.json.org/)  file. This
section describes the objects and attributes of the JSON output in detail.

Note: `--json-output-v1` through
`--json-output-v10` are supported for backward compatibility. It is
recommended that you use `--json-output-v11` in order to see the most
complete set of information.

The structure of the JSON output (v11) is represented below.

[image: image]
