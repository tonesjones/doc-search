---
title: "Overview: Scheduling each scan job on its own node"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview-scheduling-each-scan-job-on-its-own-node.html"
content_id: "B_iHGQf4ajseY2gSeQooFQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:06.595519+00:00"
---

# Overview: Scheduling each scan job on its own node

In a cloud environment where nodes can be easily spun up to manage scan jobs, scheduling
each job on a node that matches the job parameters enables multiple jobs to each be run
on their 'own' node.. The nodes within a node pool share CPU and storage resources. The
following properties make this scheduling possible:

**Node Selector** schedules jobs on nodes that have a specific label. For example,
jobs can be scheduled on nodes based on job size, where a small job can be scheduled on
a node labeled small, and a large job can be scheduled on a node labeled large.

**Taints and Tolerations** ensures that nodes designated for scan jobs are exclusively
reserved for scan job workloads.. Only jobs with matching tolerations are scheduled on
these dedicated nodes. This prevents scan jobs from running on application pods, thereby
preventing interference.

**Labels and Anti Affinity** runs each job on a separate node, ensuring that jobs are
spread out across nodes. Anti-affinity prevents jobs that have the same label from being
scheduled on the same node.

These properties enable each scan job to be scheduled on its own node, and precisely
target each job to the appropriate node based on properties such as node size, node
label, and affinities. The following diagram illustrates a simple deployment with five
different node pools and only one node per node pool. Each node handles one scan
job.

[image: image]

The following diagram shows five different node pools with differing numbers of nodes.
This configuration uses node autoscaler to scale up and down nodes within the node pools
as needed to run scan jobs. It illustrates a new small node being created to support a
new small scan job.

[image: image]

For information on node autoscaling, see Using node autoscaler to scale nodes and meet demand.
