---
title: "Configuring one scan job per node, multiple node pools"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-one-scan-job-per-node-multiple-node-pools.html"
content_id: "nhSux5HrhlIZb5uwiItYLg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:11.603128+00:00"
---

# Configuring one scan job per node, multiple node pools

To deploy one scan job per node within a scan job node pool, you need to set Helm keys
that specify the pre-defined and/or custom node pool(s) to enable and use. To enable
these node pools:

Note: For information on the node pool Helm keys, see the
`scan-service.environment` Helm keys in scan-service.environment Helm keys.

1. Calculate your node pool requirement based on the frequency, number, and
   sizes of scan jobs.
2. To enable one each of the pre-defined node pools, use the following Helm
   keys, located in the `scan-services` chart.

   - `scan-service.​environment.​SMALLNODEPOOL_ENABLE`
   - `scan-service.​environment.​MEDIUMNODEPOOL_ENABLE`
   - `scan-service.​environment.​LARGENODEPOOL_ENABLE`
   - `scan-service.​environment.​EXTRALARGENODEPOOL_ENABLE`
3. You can optionally deploy a custom node pool. For example, a node of 200 CPUs
   and 850 GiB memory which can run a small, medium, large, or extra large job.
   To deploy scan jobs in a custom node pool, you need to set the following
   Helm keys:

   - `scan-service.​environment.COVANALYSIS_DEFAULTPOOLTYPE:`
   - `scan-service.​environment.CUSTOMNODEPOOL_LABEL:`
   - `scan-service.​environment.CUSTOMNODEPOOL_CPU`
   - `scan-service.​environment.CUSTOMNODEPOOL_MEM`

   The following example enables a custom scan job node pool named "custom" with
   4 vCPUs and 16 GB of RAM:

   ```
   scan-service:
     environment:
       COVANALYSIS_DEFAULTPOOLTYPE: "custom"
       CUSTOMNODEPOOL_LABEL: "custom"
       CUSTOMNODEPOOL_CPU: 4000
       CUSTOMNODEPOOL_MEM: 16000
   ```

   Note: To deploy scans in a custom node pool, both
   `COVANALYSIS_DEFAULTPOOLTYPE` and
   `CUSTOMNODEPOOL_LABEL` must be the same value. Enter the
   value that you assign when you create the custom node pool.
