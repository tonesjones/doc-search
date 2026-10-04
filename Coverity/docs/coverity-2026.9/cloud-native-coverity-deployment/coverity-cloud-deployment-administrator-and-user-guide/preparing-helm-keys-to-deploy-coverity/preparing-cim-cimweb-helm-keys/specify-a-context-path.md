---
title: "Specify a context path"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/specify-a-context-path.html"
content_id: "JKNaN_VzhfqPcy_xd_d8mw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:31.577604+00:00"
---

# Specify a context path

If needed, in the `cnc` Helm chart, you can specify a context path. Add
context path under Coverity host. For example: if you set this field to
`$CONTEXT_PATH`, Coverity will be accessible under
`https://$HOST/$CONTEXT_PATH`. if a context path is not needed, leave
this as the default empty string "".

```
cim:
  cimweb:
    contextPath: ""
```
