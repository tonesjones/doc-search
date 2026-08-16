---
title: "Infrastructure and configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/infrastructure-and-configuration.html"
content_id: "A55nQKQQaR1yxh_te_ppEQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:47.757184+00:00"
---

# Infrastructure and configuration

Before you can install services and deploy Coverity, you must set up a cloud
infrastructure in which to install and run Coverity in a cloud-based Kubernetes cluster.
This chapter introduces these infrastructure prerequisites. Additionally, you need to
maintain the infrastructure.

Important: While you are creating the various components
in this deployment, for example PostgreSQL storage, scan services storage and cache,
secrets, ConfigMap, etc, you must retain information to complete many related Helm keys
in the cnc or scan-services Helm charts. Completing these values in the Helm chart is
important for successful cluster deployment and communication. While setting up the
infrastructure, refer to the following for Helm chart guidance:

- For Connect and general keys, Preparing Helm keys to deploy Coverity.
- For scan services keys, Configuring Helm keys to support onPrem or non-platform-specific deployments using Redis and Minio.
- The Helm chart reference sections in Helm keys for a Coverity cloud deployment.

For related high-level procedural guidance while setting up a Coverity cloud deployment,
refer to: Coverity deployment scenarios

For software and platform support, refer to Third-party software and platform support matrix.

For platform-specific guidance and requirements, see also:

- Amazon AWS infrastructure and configuration
- Google GCP infrastructure and configuration
- Microsoft Azure infrastructure and configuration
