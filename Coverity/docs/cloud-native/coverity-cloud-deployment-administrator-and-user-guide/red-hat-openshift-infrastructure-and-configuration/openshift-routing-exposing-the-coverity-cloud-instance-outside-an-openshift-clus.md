---
title: "OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/openshift-routing-exposing-the-coverity-cloud-instance-outside-an-openshift-cluster.html"
content_id: "WzHNKFY6qKK1TZCTuZLTtg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:52.557505+00:00"
---

# OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster

When deploying within a Red Hat OpenShift cluster, to expose your software and manage
access, networking, and routes, you can use the preferred default OpenShift Ingress
Controller, you do not need to use an NGINX ingress controller. You can set parameters
to create an OpenShift secured route that exposes your application outside the cluster.
As part of this release, in addition to configuring route parameters using the OpenShift
UI, you can now configure OpenShift routing parameters through the `cnc`
Helm chart.

## Prerequisites

You need to complete the following prerequisites before you can configure route
parameters:

- Create an OpenShift cluster with the `route.openshift.io/v1` API
  available.
- Create an ingress configuration. This is recommended to have values available
  for automatic inheritance (see Advanced OpenShift route considerations).
- Optional: Create TLS certificates stored in Kubernetes secrets.

## Route configuration methods

To configure route creation parameters for routes that expose Coverity cloud cluster
software outside the cluster, you can use one of the following methods:

- In the `cnc` Helm chart, enable automatic route creation and use
  the default or pre-configured ingress configuration. This is the easiest
  solution. See Manage automatic route creation using existing ingress settings.
- In the `cnc` Helm chart, you can optionally manage route creation
  using Helm key overrides and annotations. This method enables greater control
  and customization. See Manage route creation using the cnc Helm chart.
- To configure Red Hat OpenShift routing using the OpenShift UI: OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster
- To configure an ingress route to MinIO. See Configure an ingress route to MinIO in OpenShift.

For OpenShift routing information, also refer to the Red Hat OpenShift documentation:
[Configuring ingress cluster traffic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.12/html/networking/configuring-ingress-cluster-traffic#overview-traffic)
