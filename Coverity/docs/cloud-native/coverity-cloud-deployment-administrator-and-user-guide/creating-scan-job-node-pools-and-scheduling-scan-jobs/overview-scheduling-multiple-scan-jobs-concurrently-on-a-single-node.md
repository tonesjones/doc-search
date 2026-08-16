---
title: "Overview: Scheduling multiple scan jobs concurrently on a single node"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview-scheduling-multiple-scan-jobs-concurrently-on-a-single-node.html"
content_id: "FsEI58txrQWeRxAlznWFpw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:07.586361+00:00"
---

# Overview: Scheduling multiple scan jobs concurrently on a single node

If you have an on-prem deployment with limited resources, you can elect to create a
single node on which to run all analysis jobs. Single-node scan enables you to run
multiple scan jobs on a single node, assuming that the node has adequate resources.
Single-node scan uses the following methods to schedule scan jobs on that single
node:

**Taints and Tolerations** ensures that nodes designated for scan jobs are exclusively
reserved for scan job workloads. Only jobs with matching tolerations are scheduled on
these dedicated nodes. This prevents application pods from interfering with analysis
jobs.

**NodeLabel** for every job type is `“common-pool: scanfarm”`. This
schedules all jobs on a single node. All nodes should have the new label. Steering jobs
is controlled by the label. The single-node feature uses the user-provided label.
otherwise will use our internal job-size names in label.

With single-node analysys enabled, you cannot use pod anti affinity since it prevents
jobs from spreading out across nodes.

Single-node analysis uses job-sizes: small, medium, large, extralarge, and custom node
pool sizes.

These properties enable you to schedule jobs on a single node that is sized to handle the
multiple jobs. You can target multiple jobs to a single node based on the following
characteristics/properties: node size, node label, etc. The following diagram
illustrates this scheduling method.

[image: image]

You can optionally enable and configure node autoscaler to create additional nodes to
meet demand. With this feature enabled, if a node is unavailable to run a scheduled scan
job, Kubernetes creates an additional node which can run additional scan jobs as
resources permit.

The following diagram shows a case where node autoscaler is enabled and configured,
permitting Kubernetes to create a new node within the node pool to handle a new scan job
that would otherwise be queued.

[image: image]

For information on node autoscaling, see Using node autoscaler to scale nodes and meet demand.
