---
title: "Red Hat OpenShift infrastructure and configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/red-hat-openshift-infrastructure-and-configuration.html"
content_id: "w0gyqupO6NEIkf8_LhnLRg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:51.896290+00:00"
---

# Red Hat OpenShift infrastructure and configuration

This chapter provides Red Hat OpenShift-specific guidance to help you create an
infrastructure to support a Coverity cloud deployment in a cluster within OpenShift.
This chapter is specific to Red Hat OpenShift.

For related high-level procedural guidance while setting up a Coverity cloud deployment,
refer to: Coverity deployment scenarios

Refer to your AWS documentation for procedures that are specific to AWS.

Important: While you are creating the various components
in this deployment, for example PostgreSQL storage, scan services storage and cache,
secrets, ConfigMap, etc, you must retain information for Helm key values in the
`cnc` or `scan-services` Helm charts. Completing these
values in the Helm chart is important for successful cluster deployment and
communication. While setting up the OpenShift infrastructure, refer to the following for
routing and Helm chart guidance:

- For Red Hat OpenShift routing, see OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster.
- For Connect and general chart guidance, Preparing Helm keys to deploy Coverity.
- For Helm chart reference Helm keys for a Coverity cloud deployment.

For related high-level procedural guidance while setting up a Coverity cloud deployment,
refer to: Coverity deployment scenarios

For software and platform support, refer to Third-party software and platform support matrix.

Note: The procedures and examples in this section are a guide to the
types of OpenShift infrastructure components that you might need to configure. Your
configuration and requirements might differ.

Note: If you are not installing scan service, disregard all scan
service, storage service, cache service, and scan job procedures and
requirements.
