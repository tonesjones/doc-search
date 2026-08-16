---
title: "Schema version element"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/schema-version-element.html"
content_id: "dW0l_FmRTAnL0JvIVncRYA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:00.929376+00:00"
---

# Schema version element

The schema version element must include the following key:

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `schema-version` | Integer | Sets the version number for the schema. Changes that alter the semantics of the parts of the schema that are independent of the report in a non-additive way must trigger an increment of this number. | N/A | Yes |
