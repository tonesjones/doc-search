---
title: "Mounting additional volumes to pods"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/mounting-additional-volumes-to-pods.html"
content_id: "Ha~25M5njbvHGxyTJxjXtw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:32.775965+00:00"
---

# Mounting additional volumes to pods

You can mount extra volumes in the following pods:

- cim-tools
- cim-setup
- cnc-db-admin
- scan-service
- scan-service-migration job
- storage-service
- storage-service-migration job

To mount an extra volume in a pod, override the appropriate `extraVolumes`
Helm key values for that pod. For example, to add a scan-service-secret volume to the
scan-service pod, add the volume secret name under the
`scan-service.extraVolumes` Helm key in the
`scan-services` subchart:

```
scan-service:
  extraVolumes:
    - name: scan-service-secret
      secret:
        secretName: scansvc-secret
```

See scan-services Helm subchart: Helm keys.
