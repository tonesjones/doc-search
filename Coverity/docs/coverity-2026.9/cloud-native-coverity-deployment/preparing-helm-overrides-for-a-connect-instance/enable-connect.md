---
title: "Enable Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enable-connect.html"
content_id: "LVUYcR8W2NYiFx85PN1Dcg"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:31.041419+00:00"
---

# Enable Connect

To install a single instance of Coverity Connect within a cluster in the cloud, you must
set the following values in the `cnc` Helm chart `.yaml`
file:

```
cim:
  cimweb:
    enabled: true
```
