---
title: "Specify the image version and type for OpenShift"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-the-image-version-and-type-for-openshift.html"
content_id: "acQV_e4tauDTlBnnd23l1A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:35.179911+00:00"
---

# Specify the image version and type for OpenShift

To point to the correct image when deploying Coverity in OpenShift, set the following
root Helm keys:

- Set the `imageVersion` Helm key to `2026.6.0`.
- Set the `imageTagSuffix` Helm key to `-ubi`.

For example:

```
imageVersion: "2026.6.0"

imageTagSuffix: "-ubi"
```

You can find these keys as `global.` or root Helm keys in the
`cnc` chart.
