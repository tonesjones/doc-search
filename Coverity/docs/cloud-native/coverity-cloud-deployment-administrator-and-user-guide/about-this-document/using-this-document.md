---
title: "Using this document"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-this-document.html"
content_id: "nEG9qLRdk7VOVJGjqwe~PQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:13.124847+00:00"
---

# Using this document

This document describes how to set up and manage a deployment of Coverity Connect and
optionally Scan Service in a Kubernetes cluster in the cloud. It is intended for:

- administrators who are experienced in the cloud and in Kubernetes containerization,
  and who need to install and manage a cloud deployment of Coverity.
- users who are experienced with Coverity and who need to learn about differences in
  commands, operations, and troubleshooting of Coverity deployed in the cloud.

Administrators who are setting up and maintaining this environment must:

- if deploying in the cloud, understand and be able to deploy in the cloud
  environment
- understand Helm
- understand Kubernetes
- understand how to deploy and maintain applications on Kubernetes
- understand Docker images and be able to work with image registries
- understand image pull secrets
- understand networking
- understand cloud-native tech stacks and how these interact with applications such as
  certificate managers or telemetry.
- understand what dependencies provide and how to work with them

Note: See also Customer responsibility and deployment workflow.
