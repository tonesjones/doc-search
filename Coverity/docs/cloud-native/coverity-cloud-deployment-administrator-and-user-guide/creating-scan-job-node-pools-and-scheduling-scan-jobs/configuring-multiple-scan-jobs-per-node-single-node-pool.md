---
title: "Configuring multiple scan jobs per node, single node pool"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-multiple-scan-jobs-per-node-single-node-pool.html"
content_id: "WNM2aL3MhtOwNw8V9MKOKA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:12.274041+00:00"
---

# Configuring multiple scan jobs per node, single node pool

This section describes how to set up scan job scheduling to schedule multiple scan jobs
on a single node. To schedule multiple scan jobs on a single node:

Note: Refer to the Helm keys reference section: scan-service.environment Helm keys.

1. Calculate your node pool requirement based on the frequency, number, and sizes of
   scan jobs.
2. Create a single extra large node pool. The node pool can be any of the following:
   small, medium, large, extra large or custom. For example, to enable an
   `extra-large` node pool, set the following Helm keys to
   enable the extra-large node pool and disable all others node
   pools:

   ```
   scan-service:
     environment:
       EXTRALARGENODEPOOL_ENABLE: true
       LARGENODEPOOL_ENABLE: false
       MEDIUMNODEPOOL_ENABLE: false
       SMALLNODEPOOL_ENABLE: false
       CUSTOMNODEPOOL_ENABLE: false
   ```

   For a single scan job node pool
   configuration, regardless of the node pool size, the default
   `NodeLabel` value is `“common-pool: scanfarm”`.
   The scan service schedules scan jobs using the `NodeLabel` default
   value or a value that you provide. Without autoscaling, the scan service will
   schedule all scan jobs on the single node within the node pool. With autoscaling, if
   the node is full, a new node will be scaled up for the new scan job(s).
3. If you are creating a custom node pool, enable the custom pool, configure the
   node pool CPU and memory, and enter the node pool label name:

   1. Enable custom node pool and disable all other node pool types

      ```
      scan-service:
        environment:
          CUSTOMNODEPOOL_ENABLE: true
          EXTRALARGENODEPOOL_ENABLE: false
          LARGENODEPOOL_ENABLE: false
          MEDIUMNODEPOOL_ENABLE: false
          SMALLNODEPOOL_ENABLE: false
      ```
   2. Set the number of CPUs and memory using the following Helm keys:

      ```
      scan-service:
        environment:
          CUSTOMNODEPOOL_CPU: <cpu>
          CUSTOMNODEPOOL_MEM: <mem>
      ```

      Note: If you are creating a custom nodepool with
      single-large node, the `CUSTOMNODEPOOL_CPU` and
      `CUSTOMNODEPOOL_MEM` values should be less than the
      created single-large-node pool's CPU and memory.
   3. Enter a node pool label name using the following Helm key:

      ```
      scan-service:
        environment:
          CUSTOMNODEPOOL_LABEL: "<node-pool name>"
      ```

      The default custom node pool label is:

      ```
      CUSTOMNODEPOOL_LABEL: “custom-pool: scanfarm”
      ```

      If single node is enabled and with custom node pool, you can use the node
      name as the label. The scan service will schedule scan jobs to whatever
      node name you provide.
4. Configure Taints and Tolerations.

   Taints and Tolerations ensure that nodes designated for scan jobs are exclusively
   reserved for scan job workloads. Only jobs with matching tolerations are
   scheduled on these dedicated nodes. This prevents application jobs from
   interfering with scan jobs.

   For additional information, refer to the section, [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/_print/#pg-ede4960b56a3529ee0bfe7c8fe2d09a5).

   See also the following Kubernetes documentation: [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)

Important: When you upgrade or reinstall a chart, ensure
that all jobs and scan workflows work as expected when you toggle the deployment
flag.
