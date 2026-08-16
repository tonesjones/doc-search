---
title: "Enable Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enable-connect.html"
content_id: "LVUYcR8W2NYiFx85PN1Dcg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:21.457274+00:00"
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
