---
title: "Helm - look for failed Helm releases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/helm-look-for-failed-helm-releases.html"
content_id: "HG2d3B~3bA1B1wn4fFIeGw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:20.010761+00:00"
---

# Helm - look for failed Helm releases

Using the following command, look for any releases that do not have the status
`deployed`.

```
helm list -n "$NS" -a
```

"$NS" is the namespace name.
