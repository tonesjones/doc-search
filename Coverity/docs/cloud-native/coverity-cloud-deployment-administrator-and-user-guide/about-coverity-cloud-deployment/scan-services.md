---
title: "Scan Services"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-services.html"
content_id: "OkDClHLIW6n5Xn_Z0no3BA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:19.468948+00:00"
---

# Scan Services

Important: Coverity Scan Services is optional.

You can optionally deploy Coverity Scan Services in the Kubernetes cluster. This enables
you to run scans in the Kubernetes cluster as opposed to on the client system.

Scan Services performs a scan in two phases:

1. Thin Client, installed on the client, captures the artifacts to be analyzed.
2. Scan Services, installed in the Kubernetes cluster, performs the analysis.

Each scan performed by the Scan Services is identified by a unique scan identifier.
Coverity Connect saves and manages scan data in the PostgreSQL database. Scan Services
notifies the client of the scan status. To review and manage analyses, you can use
either the Coverity API or the Coverity Connect UI.

Scan Services consists of the following services:

- **Scan Service** is the scan orchestrator. It provides APIs to create, retrieve,
  and schedule scans using Kubernetes jobs.
- **Storage Service** manages storage, provides APIs to create new storage objects,
  and provides pre-signed URLs to upload and download artifacts.
- **Cache Service** manages caching.
