---
title: "Using affinities to distribute pods on nodes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-affinities-to-distribute-pods-on-nodes.html"
content_id: "S6grYQCjnWEOFU6jMl0xAA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:27.714988+00:00"
---

# Using affinities to distribute pods on nodes

If desired, you can use affinity or anti-affinity in the `cim.affinity`
Helm key in the `values.yaml` file of the `cnc` chart to
manage the distribution of pods among multiple nodes. Distributing across multiple nodes
ensures that your application continues to run smoothly even when a node restarts.

For information on affinities, refer to the Kubernetes document, [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).

Without affinities, the Kubernetes scheduler schedules pods on nodes that contain
resources sufficient for the pods.

Optionally, you can use affinity and anti-affinity to determine the distribution of pods
in nodes. You can set affinities in the `cnc` chart
`values.yaml` file or another .yaml file. The following example uses
pod anti-affinity to schedule two pods on separate nodes:

```
cim: 
  cimweb: 
    replicas: 2 
  affinity: 
    podAntiAffinity: 
    requiredDuringSchedulingIgnoredDuringExecution: 
      - labelSelector: 
          matchExpressions: 
            - key: app.kubernetes.io/name 
              operator: In 
              values: 
                - cim 
       topologyKey: "kubernetes.io/hostname"
```

In this example, for two replicas, the anti-affinity rule says that the scheduler must
avoid scheduling (`requiredDuringScheduling`) both `cim`
pods on the same node that has the `app.kubernetes.io/name=cim` label;
the second pod must be scheduled on a second node with the same label.
