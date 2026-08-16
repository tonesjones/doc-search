---
title: "Creating scan job node pools and scheduling scan jobs"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-scan-job-node-pools-and-scheduling-scan-jobs.html"
content_id: "JxfciZm6jVINV0PDvxJ5JA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:05.074213+00:00"
---

# Creating scan job node pools and scheduling scan jobs

Scan jobs can be scheduled on nodes using either of the following schedules:

- **Create multiple node pools that can support multiple nodes per pool, and schedule
  each scan job on its own node**: This method can create multiple node pools of
  different sizes. Each node pool supports one or more nodes of that size. Each node
  supports one scan job. This method works well in a cloud environment where nodes can
  be spun up as needed to support many scan jobs.
- **Create a single node pool with a single node, and schedule multiple scan jobs
  concurrently on the single node**: This method creates a single extra large
  node pool. The node pool supports one or more nodes of that size. Each node supports
  one or more scan jobs. You can create a single extra large node pool and schedule
  all or many scan jobs concurrently on a single node within the node pool.
- **Create a single node pool that can support multiple nodes, and schedule multiple
  scan jobs concurrently on each node**: Using ths multiple scan jobs on one
  node feature, you can also allow Kubernetes to create multiple nodes within the
  single extra large node pool, where each node can support multiple scan jobs as
  resources permit. To enable node autoscaling, you need to enable autoscaler and set
  a node count range or limit. If the current node(s) do not have room for another
  job, the new job will trigger the node autoscaler which will scale up a new
  node.
