---
title: "Adding init containers within pods"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-init-containers-within-pods.html"
content_id: "mRF54D0YHQ5Nl_HmaefA_g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:47.355298+00:00"
---

# Adding init containers within pods

Init containers can be used within some pods to provide a specific momentary function,
then expire. You can create init containers in a pod by adding a list under the
`initContainers` key. in the following Helm keys within the
appropriate `cnc` chart or `scan-services` subchart:

- `cnc` chart: See cnc Helm chart: Helm keys.
  - `cim.cimtools.initContainers`
  - `cim.cimweb.initContainers`
  - `cim.setupJob.initContainers`
- `scan-services` subchart: See scan-services Helm subchart: Helm keys.
  - `cache-service.initContainers`
  - `scan-service.initContainers`
  - `scan-service.migrateJob.initContainers`
  - `storage-service.initContainers`

To add a sidecar init container within a pod, within the `initContainer`
Helm key for that pod definition, list the sidecar init container name and image values
that define the init container. For example, to attach an init container to the Scan
Service pod, add or update the list of container values in the
`scan-service.initContainers` Helm key:

```
scan-service:
  initContainers:
    - name: <init-container-name>
      image: <init-container-image>
```

where:

- `<init-container-name>` Assign an init container name.
- `<init-container-image>` Specify the init container image.
  Include the path to the image, if needed.

Note: If you add an `initContainer` within a pod, the
main container will continue to live after the init container completes its task and
expires.

For further information on init containers, see

- <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#understanding-init-containers>
