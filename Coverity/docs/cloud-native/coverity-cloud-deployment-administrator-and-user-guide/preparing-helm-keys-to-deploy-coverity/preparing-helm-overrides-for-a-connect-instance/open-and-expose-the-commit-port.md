---
title: "Open and expose the commit port"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/open-and-expose-the-commit-port.html"
content_id: "6C~QLiKE33YDjR3ctwog0Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:24.066133+00:00"
---

# Open and expose the commit port

You must open and expose the commit port for Connect. In the `cnc` chart,
ensure that the `cim.cimweb.exposeCommitPort` Helm override is set to
`true`. to open a commit port on a container and service.

```
cim:
  cimweb:
    exposeCommitPort: false
```

For Helm key information see `cim.cimweb.exposeCommitPort` in Open and expose the commit port.
