---
title: "Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-onprem-oci-redis-minio-and-postgresql-for-scan-service.html"
content_id: "0kiWsLE~qnMJFs2F0qaojQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:14.266016+00:00"
---

# Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service

This chapter describes an optional feature that uses onPrem open-source (OCI) Redis,
MinIO, and PostgreSQL Helm subcharts which are integrated within the
`cnc` chart.​ You have the option of using either:

- the external Redis, MinIO, and PostgreSQL resources, or
- the optional onPrem OCI Redis, MinIO, and PostgreSQL resources.

The onPrem MinIO, Redis, and PostgreSQL chart keys are commented out using
`#` symbols. Clearing the comments, enabling onPrem MinIO, Redis, and
PostgreSQL, and completing other tasks as described in this chapter enables the
deployment of onPrem OCI MinIO, Redis, and PostgreSQL. When deploying this way, you do
not need to create cache or storage buckets; they are created as part of this new
feature during Scan Services deployment. This simplifies infrastructure
provisioning.

The `cnc` chart's `values.yaml` file now incorporates
OCI-based Redis subchart, MinIO subchart, and PostgreSQL subchart Helm keys, with
default values enabling easy deployment of Scan Service. The new onPrem MinIO, Redis,
and PostgreSQL Helm keys contain default values which you can either use as is or
override if needed.
