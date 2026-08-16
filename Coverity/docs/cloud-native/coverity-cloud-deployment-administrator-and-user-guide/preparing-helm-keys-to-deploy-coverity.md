---
title: "Preparing Helm keys to deploy Coverity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preparing-helm-keys-to-deploy-coverity.html"
content_id: "jav3v3UEiCJhXkG_pIvHNw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:18.838669+00:00"
---

# Preparing Helm keys to deploy Coverity

This chapter outlines Helm keys that you edit to set up various features in your Coverity
cloud deployment. This covers the following major topics:

- Create Helm overrides to install a single instance of Connect.
- Create Helm overrides for PostgreSQL database, schema, users, and TLS.
- Create Helm overrides to install Coverity on OpenShift.
- Enable metrics.
- Specify logging levels.
- Create Helm overrides to install Scan Service, Storage Service, and Cache
  Service.

Note: The topics in this chapter describe Helm keys supported in the
2026.6.0 release. If you are upgrading from an older release to
2026.6.0, refer to Upgrade considerations for
upgrade considerations and lists of Helm keys added, removed, or renamed.

In addition to the topics in this chapter, before you run a `helm
install`, you might need to additionally address the following for your
deployment:

Table 1. Other important deployment configurations

| Feature | Refer to this chapter: |
| --- | --- |
| - Configuring container image pull keys | - Preparing container image and registry keys |
| - Configuring pod and container security | - Configuring pod and container security |
| - Creating scan job node pools and scheduling scan jobs | - Creating scan job node pools and scheduling scan jobs |
| - Configuring TLS forward proxy | - Configuring TLS forward proxy |
| - Setting up onPrem OCI Redis and MinIO for Scan Services | - Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service |
| - Building a full analysis kit and automatically uploading the kit   to Connect during deployment | - Building a full analysis kit and automatically uploading the kit to Connect during deployment |
| - Connect Web application high availability | - Connect Web application high availability |
| - PostgreSQL database read replicas | - Using PostgreSQL read replicas and Pgpool to balance database loads |
| - Specify logging levels | - Specifying logging levels |
| - Enable metrics via Helm keys and work with metrics | - Metrics |
