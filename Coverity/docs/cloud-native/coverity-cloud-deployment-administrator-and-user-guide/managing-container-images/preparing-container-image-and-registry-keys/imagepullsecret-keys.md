---
title: "imagePullSecret keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/imagepullsecret-keys.html"
content_id: "215tkoeQWTbJCQ7wSZvzAw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:42.555486+00:00"
---

# imagePullSecret keys

The `imagePullSecret` Helm key, shown below, specifies the secret that you
created to access the registry to pull container images from the registry. You need to
provide this secret for all Connect and Scan Services deployments.

You can configure the `imagePullSecret` key as a global key or as
service-specific keys that override the global key:

- `global.imagePullSecret` key

  Note: The `global.imagePullSecret` key is
  present in both the `cnc` chart and the
  `scan-services` subchart.
- `cnc` chart, `imagePullSecret` key
- `scan-services` chart, `imagePullSecret` key

See also:

- For the name of the secret, see Create a container image pull secret.
- For global root keys, see global root Helm keys.
- For root keys, see Root Helm keys.
