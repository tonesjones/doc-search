---
title: "Enable license jobs"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enable-license-jobs.html"
content_id: "m4DLaZeNwN4aTsMBnlYYGA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:39.071077+00:00"
---

# Enable license jobs

In the `cnc` chart, `values.yaml` file, verify that the
following license keys are set for your deployment:

```
cim:
  cimweb:
    updateLicense:
      enabled: true
      force: true
```

Refer also to Specify the name of the Scan Service license secret and to the
`cim.cimweb.updateLicense` keys in cnc Helm chart: Helm keys.
