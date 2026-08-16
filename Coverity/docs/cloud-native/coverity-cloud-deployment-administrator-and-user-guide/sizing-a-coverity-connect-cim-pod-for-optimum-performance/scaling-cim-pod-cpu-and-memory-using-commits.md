---
title: "Scaling cim pod CPU and memory using commits"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scaling-cim-pod-cpu-and-memory-using-commits.html"
content_id: "o~LuU9eDxUVD4ugdDqa5Tg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:50.183406+00:00"
---

# Scaling cim pod CPU and memory using commits

The following sections contain tables that enable you to scale your CPU and memory
resources to provide estimated commit throughput for various IDIR sizes and commit pool
threads submitted. The estimated response time is called the commit throughput. The
tables are a guide to scale your cloud hardware resources for expected performance given
your commit count and IDIR size.

Important: In a deployment with multiple Coverity Connect
(cim) pods, the resource guidance applies equally to all pods deployed. Provide the full
resources for each pod that you deploy; do not split up calculated CPU and memory
resources between pods.

To use the hardware scaling tables for commit performance:

1. Find your target intermediate directory (IDIR) size. Find either the largest IDIR
   or the slowest commit, and use the corresponding IDIR size on disk. Refer to the
   corresponding table:

   - Medium – up to 2.6 GB
   - Large – up to 12 GB
   - Extra large – up to 36 GB

   Note: When selecting an IDIR size, if your largest IDIR is
   not typical (not committed very often), then consider using the next smaller
   IDIR size.
2. Choose the target throughput (commits/hr) and use the corresponding minimum
   requirements for `commitPoolThreads`, processors, and memory
   available to the Coverity cloud system.
3. If you are using a non-default Commit Queue size higher than 80, adjust the
   system memory accordingly.
