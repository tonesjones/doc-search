---
title: "imagePullPolicy Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/imagepullpolicy-helm-keys.html"
content_id: "AfSGC_rDkM910exvnee_sw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:43.204164+00:00"
---

# imagePullPolicy Helm keys

The `imagePullPolicy:` Helm keys control how Kubernetes pulls container
images from a registry. The default value is `IfNotPresent` where:

- `IfNotPresent` - Kubernetes checks if the image exists on the node.
  If it does, it uses the cached copy; otherwise, it pulls the image from the
  registry. With imagePullPolicy set to ifNotPresent, the container images are good
  for the life of the node. Numerous pods can be spun up and down from the cached
  image(s).
- `Always` - Kubernetes always attempts to pull the image from the
  registry to ensure the latest version is used.
- `Never` - Kubernetes never pulls images. The images must already be
  locally available. If an image is not available locally, pod creation fails.

The image pull policy (`imagePullPolicy`) Helm key has the following
default value which can be retained:

```
imagePullPolicy: IfNotPresent
```

If needed, you can override the value with a valid value (`Always` or
`Never`) noted above.

The `imagePullPolicy` key can be configured as a global key or as
service-specific keys that override the global key:

- Both charts: `global.imagePullPolicy: IfNotPresent` See Global Helm keys.

  Note: The `global.imagePullPolicy` key is
  present in both the `cnc` chart and the
  `scan-services` subchart.
- `cnc` chart, `imagePullPolicy: ""` See Root Helm keys.
- `cnc` chart, `# minio:sidecars:imagePullPolicy:
  "IfNotPresent"` See onPrem.minio: Helm keys.
- `scan-services` chart, `scan-services:imagePullPolicy:
  ""` See Root Helm keys.
- `scan-services` chart,
  `scan-services:scan-service:dispatcher:imagePullPolicy:
  IfNotPresent` See scan-service.dispatcher Helm keys.
