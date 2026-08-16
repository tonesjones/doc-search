---
title: "Attaching a Cloud SQL proxy native sidecar container in GCP"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/attaching-a-cloud-sql-proxy-native-sidecar-container-in-gcp.html"
content_id: "9TevDs~roPyioZEnMu~p8A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:46.695639+00:00"
---

# Attaching a Cloud SQL proxy native sidecar container in GCP

Important: To use this feature, the Kubernetes version
must be 1.28 or greater.

In GCP, you can optionally attach a Cloud SQL proxy as a native sidecar container within
all pods that require a database connection. You do this using the
`postgres.sidecars` and `postgres.jobSidecars` Helm
keys associated with the PostgreSQL pod definition.

You can create Cloud SQL proxy sidecar containers within the following Coverity cloud
pods:

- cim-tools
- cim-setup
- cnc-db-admin
- scan-service
- scan-service-migration job
- storage-service
- storage-service-migration job

Also, within these pods, you can mount volumes for each Cloud SQL proxy sidecar container
using the `volumeMounts:` Helm key associated with the Cloud SQL proxy
sidecar container definition.

Refer to the following pages for additional sidecar container information:

- For information on Cloud SQL proxy containers, refer to <https://www.digitalocean.com/community/tutorials/cloud-sql-proxy-in-gke>.
- For information on using native sidecar containers, see <https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/>
