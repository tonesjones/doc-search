---
title: "Black Duck helm chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-helm-chart.html"
content_id: "3G0auI9qysiKwGXrdttvaA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.497088+00:00"
content_hash: "acac17ca124fc31dee2c10e4baebd2895ddb1db3033a67367cfbea6e08b292c2"
---

# Black Duck helm chart

This chart bootstraps Black Duck deployment on a Kubernetes cluster using the Helm package manager.

Note: This document describes a quickstart process of installing a basic deployment. For more configuration options, please refer to the Kubernetes documentation.

## Prerequisites

- Kubernetes 1.16+

  - A `storageClass` configured that allows persistent volumes.

    The `reclaimPolicy` of the `storageClass` in use should be set to `Retain` to ensure data persistence. AzureFile (non-CSI variant) requires a custom storage class for RabbitMQ due to it being treated as an SMB mount where file and directory permissions are immutable once mounted into a pod.
- Helm 3
- Adding the repository to your local Helm repository:

  ```
  $ helm repo add blackduck https://repo.blackduck.com/cloudnative
  ```
