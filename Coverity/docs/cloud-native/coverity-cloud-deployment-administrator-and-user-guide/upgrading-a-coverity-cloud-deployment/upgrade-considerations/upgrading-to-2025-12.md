---
title: "Upgrading to 2025.12"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.12.html"
content_id: "nv9TF9a4Ch9y1UOtb3QDQQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:29.895960+00:00"
---

# Upgrading to 2025.12

The 2025.12.0 release introduces the following changes that can impact the upgrade
process:

- This release enables RedHat OpenShift administrators to create routes using new Helm
  keys in the cnc Helm chart. Refer to OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster and cim.route Helm keys for Red Hat OpenShift route creation.
- The `cnc` Helm chart now provides native OpenShift route support.
  Routes automatically inherit configuration values from the ingress controller.
  This enables you to define route parameters through the `cnc`
  Helm chart and eliminates the possibility of duplicate configuration values.
  Refer to OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster.
- Important:

  Do NOT USE or CHANGE ANY `cnc` Helm chart
  `cim.commitrcp4` Helm keys. These are Black Duck
  internal use only.

Additionally, consider the following.

- As recommended, copy all container images from the new Black Duck repository to a
  local repository and use your local repository to deploy Coverity cloud. To create
  your own private Coverity cloud repository, see Create your own private Docker registry.
- Download, modify as needed, and deploy the new Helm chart for the current
  release. See Downloading the Helm chart from the Black Duck public Docker registry.

The following table identifies new Helm keys in the 2025.12.0 release.

Table 1. New Helm keys in 2025.12.0

| Helm key | Notes |
| --- | --- |
| ``` cim:   route:     enabled: false     annotations: {}     hosts: []     targetPort: 8080     tls:       enabled: true       termination: "edge"       secrets: []       insecureEdgeTerminationPolicy: ""     wildcardPolicy: "None" ``` | `cnc` Helm chart:  These are new Helm keys that enable Red Hat OpenShift customers to use the Helm chart to configure routes.  See cim.route Helm keys for Red Hat OpenShift route creation and OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster. |
