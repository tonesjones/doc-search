---
title: "Commit considerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/commit-considerations.html"
content_id: "GJ~qX0jAtlqSPOzQ8VStDw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:52.782245+00:00"
---

# Commit considerations

- Commit throughput values represent the maximum sustained or regular load on the
  Coverity cloud system. Although spikes exceeding commit load can be handled by
  the system, you should avoid regularly exceeding the maximum commit throughput
  of your Coverity cloud system.

  If the load exceeds these values on a consistent basis, you should upsize your
  *commitPoolThreads*, processors, and memory available to the system.
  You should track the size of the largest idir over time and determine if the
  usage is outgrowing the current size.
- Coverity cloud has telemetry data and two key metrics to help with this:
  `Commits in Progress` and `Commit Queue Size`.
  If `Commits in Progress` is consistently at the
  commitPoolThreads level and/or if the `Commit
  Queue Size` is consistently growing, the system does not have enough
  resources to handle the load. You should also provide allowance for daily
  quiet-periods, or after hours time to allow background application maintenance
  to occur.

  For best commit performance, we recommend that you set
  commitPoolThreads to the total number of CPUs/threads
  available, however do not exceed this amount. Setting
  commitPoolThreads more than the CPUs/threads available to
  the system provides no benefit and might degrade performance. Also, refer to the
  Coverity documentation regarding the cim.property
  commitPoolThreads.
- There are scaling benefits to increasing the resources for
  commitPoolThreads beyond 30 as well as increasing CPU
  cores and memory. However, we are unable to guarantee the results as they are
  beyond the testing that was performed.
- The tables use a default commitWorkQueueCapacity of 80. If you
  increase the commit work queue capacity, refer to the Queue tables for maximum
  memory requirements. The general formula for the maximum queue memory
  requirement is:

  QueueMemoryUsage < 1% × 𝑖𝑑𝑖𝑟_𝑠𝑖𝑧𝑒 ×
  NumberofQueues
- The resource recommendations consider committing to a large database (276 GB).
  However, your database size and characteristics might also impact the resource
  requirements.
- Coverity cloud does not currently track all API statistics, therefore these
  values are obtained from the external services which interact with and call
  Coverity cloud APIs. We recommend monitoring disk utilization on Coverity cloud
  servers to prevent disks from filling to capacity, thereby preventing related
  Coverity cloud issues.
