---
title: "Install required software"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/install-required-software.html"
content_id: "u0f3khyidczEwnBRtvZXCA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:48.456879+00:00"
---

# Install required software

You will need to install the following tools on any platform that will support Kubernetes
containers:

- Install `kubectl` as described in <https://kubernetes.io/docs/tasks/tools/>. The version must be the same as the Kubernetes server
  version.
- Install Helm as described in [https://helm.sh/docs/intro/install](https://helm.sh/docs/intro/install/).
- Install Docker as described in <https://docs.docker.com/engine/install/>.

Note: For supported software versions, see .

The following sections provide platform-specific information on installing the tools on
the cloud platform:

- For a deployment in Amazon AWS, in addition to the software noted above, you must
  install the Amazon `eksctl` CLI software and perform many other
  functions as described in Amazon AWS infrastructure and configuration.
- For a deployment in Google GCP, in addition to the software noted above, you must
  install the Google `gcloud` CLI software and perform many other
  functions as described in Google GCP infrastructure and configuration.
- For a deployment in Microsoft Azure, in addition to the software noted above, you
  must install the Microsoft Azure CLI software and perform many other functions
  as described in Microsoft Azure infrastructure and configuration.
