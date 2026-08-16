---
title: "Coverity cloud deployments"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-cloud-deployments.html"
content_id: "4HPar9afdRhiDFE1REAX0w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:15.736869+00:00"
---

# Coverity cloud deployments

This section illustrates containerized Coverity cloud deployments running within a
Kubernetes cluster in a hosted cloud environment. It contains the following
subsections:

- Coverity Connect-only deployment illustrates a Connect-only deployment in
  the cloud.
- Coverity Connect with Scan Service deployment illustrates a Coverity Connect and
  Scan Service deployment in the cloud.

Within the Kubernetes cluster, you create a node pool to contain Coverity Connect and
optionally Coverity Scan Service. If Scan Service is deployed, you will create an
additional node pool for the Scan Job nodes. An external Connect PostgreSQL database is
hosted within the VPC.
