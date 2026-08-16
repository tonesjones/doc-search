---
title: "Black Duck helm chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-helm-chart.html"
content_id: "BhNw_q~dpqL7Q9H5ukJ7uA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:32:59.682729+00:00"
---

# Black Duck helm chart

This chart bootstraps Black Duck deployment on a Kubernetes cluster using the Helm
package manager.

Note: This document describes a quickstart process of installing a
basic deployment. For more configuration options, please refer to the Kubernetes
documentation.

## Prerequisites

- Kubernetes 1.16+

  - A `storageClass` configured that allows persistent
    volumes.

    The `reclaimPolicy` of the
    `storageClass` in use should be set to
    `Retain` to ensure data persistence. AzureFile
    (non-CSI variant) requires a custom storage class for RabbitMQ due
    to it being treated as an SMB mount where file and directory
    permissions are immutable once mounted into a pod.
- Helm 3
- Adding the repository to your local Helm repository:

  ```
  $ helm repo add blackduck https://repo.blackduck.com/cloudnative
  ```
