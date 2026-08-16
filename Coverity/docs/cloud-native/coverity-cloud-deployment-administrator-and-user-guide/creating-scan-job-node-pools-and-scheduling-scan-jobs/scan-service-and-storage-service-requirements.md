---
title: "Scan Service and Storage Service requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-service-and-storage-service-requirements.html"
content_id: "eZ5cJHQVarY8Q6ol8klyOw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:08.241086+00:00"
---

# Scan Service and Storage Service requirements

Scan Service provides APIs to create and retrieve scans, and schedule each scan as a
Kubernetes job on a node pool. Storage Service transports captured artifacts from the
client to S3-compatible storage buckets.

If you are deploying Scan Service in the cloud, before you run a Helm install, you must
set up a scan job node pool and create a Scan Service storage bucket:

## Multiple scan jobs in multiple nodes

To set up and schedule multiple scan jobs on multiple nodes where each scan job runs
on its own scan job node:

1. Create a Scan Service Storage Bucket in your infrastructure. Refer to the
   section: Create a storage bucket for Scan Service.
2. Estimate the needed scan job node pool size(s). Refer to Scan job node pool sizing.
3. Create scan job node pools as needed. Refer to Creating a scan job node pool.
4. Optionally, set up node autoscaler to create additional nodes to meet demand.
   Refer to Using node autoscaler to scale nodes and meet demand.
5. Enable multiple scan jobs on multiple nodes. Refer to Enabling single vs multiple scan jobs per node.
6. Configure scheduling scan jobs on multiple nodes. Refer to Configuring one scan job per node, multiple node pools.
7. Set up taints, labels, and tolerations in the new node pool to separate scan
   workflows from other workflows. Refer to the section: Taints and tolerations

## Multiple scan jobs in a single node

If you use a single node pool for all Scan Jobs,

1. Create a Scan Service Storage Bucket in your infrastructure. Refer to the
   section: Create a storage bucket for Scan Service.
2. Estimate the needed scan job node pool size. Refer to Scan job node pool sizing.
3. Create a single scan job node pool. Refer to Creating a scan job node pool.
4. Optionally, set up node autoscaler to create additional nodes to meet demand.
   Refer to Using node autoscaler to scale nodes and meet demand.
5. Enable multiple scan jobs on a single node. Refer to Enabling single vs multiple scan jobs per node.
6. Configure scheduling scan jobs on a single node. Refer to Configuring multiple scan jobs per node, single node pool.
7. Set up taints, labels, and tolerations in that node pool to separate scan
   workflows from other workflows. Refer to the section: Taints and tolerations
