---
title: "Google GCP infrastructure and configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/google-gcp-infrastructure-and-configuration.html"
content_id: "T9el9jLQx7pHKdvmuUnh4g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:21.299228+00:00"
---

# Google GCP infrastructure and configuration

This chapter provides Google GCP-specific guidance to help you create an infrastructure
to support a Coverity cloud deployment in a cluster within GCP. If you are deploying
scan service, it refers to creating and configuring Google storage for the scan service
and cache service. It also describes Helm keys that you must configure as you create and
configure the Kubernetes cluster and related components. This chapter is specific to
Google GCP.

Refer to your GCP documentation for procedures that are specific to GCP.

Important: While you are creating the various components
in this deployment, for example PostgreSQL storage, scan services storage and cache,
secrets, ConfigMap, etc, you must retain information to complete many related Helm keys
in the cnc or scan-services Helm charts. Completing these values in the Helm chart is
important for successful cluster deployment and communication. While setting up the
Google GCP infrastructure, refer to the following for Helm chart guidance:

- For Connect and general keys, Preparing Helm keys to deploy Coverity.
- For scan services keys, Configure Helm keys to support GCP using GCS.
- The Helm chart reference sections in Helm keys for a Coverity cloud deployment.

For related high-level procedural guidance while setting up a Coverity cloud deployment,
refer to: Coverity deployment scenarios

For software and platform support, refer to Third-party software and platform support matrix.

Note: The procedures and examples in this section are a guide to the
types of GCP infrastructure components that you might need to configure. Your
configuration and requirements will likely differ.

Note: If you are not installing scan service, disregard all scan
service, storage service, cache service, and scan job procedures and
requirements.
