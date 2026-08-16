---
title: "Enabling single vs multiple scan jobs per node"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-single-vs-multiple-scan-jobs-per-node.html"
content_id: "KuW47A~giIVmNZsspUElyA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:10.939491+00:00"
---

# Enabling single vs multiple scan jobs per node

To enable a deployment that is able to create multiple scan job node pools, each with
multiple nodes, and schedule one scan job per node, you need to set the value of the
following `MULTIPLEJOBSPERNODE_ENABLE` Helm key to
`false`. This Helm key is in the `scan-services` Helm
subchart. The following shows this Helm key set to `false`, which is with
the default value. This value distributes multiple scan jobs on multiple nodes, where
each job runs on its own node:

```
scan-service:
  environment:
    MULTIPLEJOBSPERNODE_ENABLE: false
```

To enable a deployment that creates an extra large scan job node pool that contains a
single node, and schedule multiple scan jobs concurrently on the node, set the
`MULTIPLEJOBSPERNODE_ENABLE` Helm key to `true`:

```
scan-service:
  environment:
    MULTIPLEJOBSPERNODE_ENABLE: true
```

For Helm key reference information, see scan-service.environment Helm keys.
