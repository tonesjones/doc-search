---
title: "Project schema elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/project-schema-elements.html"
content_id: "v2KkZIgqktl2bE10INN3SA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:58.312198+00:00"
---

# Project schema elements

The project schema must include the following key:

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `project` | String | Lists the name of the Coverity Connect project. | N/A | Yes |

Note: The project name you specify with the `--project` command option on the
command line will override this key setting.
