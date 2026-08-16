---
title: "Upgrading to 2026.3"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2026.3.html"
content_id: "Sgv1LFznDqReqWiKF7GFsA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:28.579731+00:00"
---

# Upgrading to 2026.3

The 2026.3.0 release introduces the following changes that can impact the upgrade
process:

- In the 2026.3.0 release, Black Duck is providing Helm chart files and scripts
  designed to simplify Coverity cloud deployments for a number of deployment
  environments and scenarios. These charts are intended to be used for initial basic
  Coverity Kubernetes deployment test and learning. They are not intended to be used
  for more complex production deployments. See Coverity cloud quick-start chart and scripts - simplified version.
- In the 2026.3.0 release, for scans or analyses performed in Kubernetes, you can now
  specify the node pool size to use for an analysis using the
  `pool-size` parameter in the `coverity analyze` or
  `coverity scan` command, or through the
  `connect.yaml` config file. In the Analysis Guide, see the
  section "Initiating a scan in the cloud" in the Coverity Analysis
  Guide, Initiating a scan in the cloud.
- The 2026.3.0 release introduces a new feature, AI-Assisted Triage Plug-in, an
  intelligent service that provides AI-powered triage recommendations for issues
  found by Coverity. Observe the following AI-Assisted Triage Plug-in
  considerations when upgrading or deploying in Coverity cloud:

  Important: AI-Assisted Triage Plug-in is a Beta
  release feature.

  - AI-Assisted Triage Plug-in requires you to pull two new container images:
    `triage-suggestion-service-api:2026.6.0` and `triage-suggestion-service-worker:2026.6.0` from the Black Duck private
    container image registry.

    Note: The `triage-suggestion-service-api:2026.6.0` and
    `triage-suggestion-service-worker:2026.6.0` container images are available
    in the 2026.6.0 release.
  - If you are upgrading from an older release and if
    `triage-suggestion-service` is expected to remain
    disabled (default behavior), **do NOT use**
    `--reuse-values`.
  - AI-Assisted Triage Plug-in introduces new
    `triage-suggestion-service` Helm keys within the
    `cnc` Helm chart. See triage-suggestion-service: Helm keys.
  - AI-Assisted Triage Plug-in introduces a new
    `triage-suggestion-service` Helm sub-chart used to
    configure AI-Assisted Triage Plug-in in a CNC deployment. See triage-suggestion-service Helm subchart
  - If you are using AI-Assisted Triage Plug-in, RabbitMQ is enabled, and you
    try to upgrade from 2025.12 or older to a 2026.3 or newer Helm chart using
    the `helm upgrade --reuse-values` command, the Helm upgrade
    might fail. If the upgrade fails, refer to Chart failure upgrading to 2026.3 or newer Helm chart with AI-Assisted Triage Plug-in enabled.
  - For information on deploying AI-Assisted Triage Plug-in in Coverity cloud,
    see Deploying the AI-Assisted Triage Plug-in.
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
- If you upgrade from 2025.12 or older to a 2026.3 or newer Helm chart, with AI Triage
  enabled, and if the Helm upgrade fails with a PASSWORDS ERROR, see Chart failure upgrading to 2026.3 or newer Helm chart with AI-Assisted Triage Plug-in enabled.
