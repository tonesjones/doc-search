---
title: "Upgrading to 2026.6"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2026.6.html"
content_id: "ww3gfx1zZh8gd5Lflswa5A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:27.928231+00:00"
---

# Upgrading to 2026.6

The 2026.6.0 release introduces the following changes that can impact the upgrade
process:

- This release deprecates the NGINX ingress controller as it is now end-of-life and
  not supported. However, it does retain support of other NGINX ingress-class
  controllers.
- This release introduces the use of an ingress gateway API to deploy and manage
  compatible Kubernetes ingress controllers. See:
  - Gateway API
  - cim.gateway Helm keys
  - minioGateway Helm keys
- A set of new Helm keys has been added to the `cnc` Helm chart for
  OpenShift route creation. See cim.route Helm keys for OpenShift.
- This release introduces the following new Helm keys for Triage Suggestion
  Service:
  - cim.cimweb.triage-suggestion-service Helm keys
  - global.artifactStorage Helm keys
- This release introduces the following new Helm key blocks or categories:
  - `cnc` Helm chart: global.artifactStorage Helm keys
  - `cnc` Helm chart: cim.gateway Helm keys.
  - `cnc` Helm chart: minioGateway Helm keys
  - `cnc` Helm chart: cim.route Helm keys for Red Hat OpenShift route creation.
  - `cnc` Helm chart: cim.cimweb.triage-suggestion-service Helm keys for service-level overrides of global values.
  - `triage-suggestion-service` Helm subchart: Ingress.
- Important:

  Do NOT USE or CHANGE ANY `cnc` Helm chart
  `cim.commitrcp4` Helm keys. These are Black Duck internal
  use only.
- Important: Keygen is Black Duck internal use only.
  Do NOT enable Keygen.
- Important: Known issue in this release: Using
  multiple `cim` replicas with AI Assisted Triage causes
  AI-Assisted triage to fail.
- Important: In an onPrem deployment where
  `onPrem.postgres=true`, the upgrade will fail because of a
  change present in PostgreSQL Version 18, which is the supported version in the
  Coverity 2026.6 release.

Additionally, consider the following.

- As recommended, copy all container images from the new Black Duck repository to a
  local repository and use your local repository to deploy Coverity cloud. To create
  your own private Coverity cloud repository, see Create your own private Docker registry.
- Download, modify as needed, and deploy the new Helm chart for the current
  release. See Downloading the Helm chart from the Black Duck public Docker registry.

## Reduced the number of Helm key override layers for simpler override management

This release reduces the number of layers of Helm key duplication, previously used
for overrides, to simplify the Helm charts.

The following Helm keys can be found as needed at four layers in the Helm charts
(global, chart, subchart, and service) to enable override flexibility:

- imagePullPolicy
- imagePullSecret
- imageRegistry
- imageTagSuffix
- imageVersion
- postgres.*
- proxy.*
- redis.*
- trust-stores.*

The following Helm keys can be found in two Helm chart layers, global and
service:

- postgres.database

The 2026.6 release **removes** the following chart and subchart helm key override
layers.

- imagePullPolicy
- imageRegistry
- postgres.*
- proxy.*
- redis.*
- trust-stores.*
