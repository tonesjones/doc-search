---
title: "Example: Map Coverity fields to Bugzilla fields"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-map-coverity-fields-to-bugzilla-fields.html"
content_id: "ttmpeQeEyQxCnYplGoPtVw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:22.936211+00:00"
---

# Example: Map Coverity fields to Bugzilla fields

The following example maps Impact fields (High, Medium, Low) in Coverity Connect to the
corresponding fields (Highest, Normal, Lowest) in Bugzilla. To accomplish this, create a
`configMap` section in the `variables:` section of the
JSON file.

```
"configMap" : {
                // Map Coverity Impact field to Bugzilla Priority Field
                    "High" : "Highest",
                    "Medium" : "Normal",
                    "Low" : "Low",
                    "Audit" : "Lowest"
              }
```

In the `export_attributes` section of the JSON file, add this line:

```
"priority" : "<configMap[impact]>",
```

When an issue is created in Bugzilla, the impact values from Coverity Connect are looked
up in the `configMap` section, and replaced in the Bugzilla entry with
the corresponding values.
