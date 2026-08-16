---
title: "Coverity Connect with Scan Service deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-with-scan-service-deployment.html"
content_id: "COs0~QYZ0FzLGZrJu6hVOQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:17.537560+00:00"
---

# Coverity Connect with Scan Service deployment

The following figure illustrates a Coverity Connect and Scan Service deployment in the
cloud. With Scan Service deployed the cloud, you will create a separate node pool for
ephemeral scan job nodes. Each client system supports either full Coverity Analysis or
Thin Client. If you install full Coverity Analysis, you can perform scans either locally
on the client or by the Scan Service installed in the cloud. If you install Thin Client,
analyses are performed by the Scan Service installed in the cloud.

Figure 1. Coverity Connect with Scan Service deployment
[image: image]

Deploying scan-service in Kubernetes along with Thin Client in client systems enables you
to create scalable analysis containers within a Kubernetes cluster for compute-intensive
analyses, and not rely on local compute resources. Being scalable has cost-performance
advantages, providing scaled compute resources as needed to manage cost.
