---
title: "Upgrading to 2025.6"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.6.html"
content_id: "XvZUZ_vnGjTRkIYHm7f1AQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:33.349396+00:00"
---

# Upgrading to 2025.6

The 2025.6.0 release introduces the following changes that can impact the upgrade
process:

- For deployments in Microsoft Azure, the 2025.6.0 release introduces using a
  Microsoft Azure AD client secret for secure Storage Service access to the Azure
  storage blob. See Configure Storage Service access to the storage blob.
- This 2025.6.0 document specifies supported third-party software and platform
  versions within a single comprehensive table. See Third-party software and platform support matrix.
- This 2025.6.0 release provides greater security and resolves some issues associated
  with writing and persisting data in the `cim-tools` pod and the
  `cnc-db-admin` pod. This includes:
  - Adds readOnly root file system support for Coverity Connect pods and
    outlines how to create a persistent `/data` volume for
    Connect software to write and read logs and other data. See Coverity tools in a Coverity cloud deployment. The following Helm key must be
    set to `true` for the `/data` volume to be
    mounted to the `cim-tools`
    pod:

    ```
    cim.cimtools.volume.enabled: true
    ```

    See
    also Create and mount a /data persistent volume and cim.cimtools.volume Helm keys: create and mount a /data volume.
  - Creates a new `/workdir` volume mounted to the
    `cim-tools` pod and the `cnc-db-admin`
    pod. `/workdir` is a writable volume in which you can write
    and store files. See Read-only file system error.
  - Provides new volumes in the static-tuning-suggest and static-tuning-write
    tools templates. See static-tuning-suggest.yaml - Acquiring database static tuning suggestions
    and static-tuning-write.yaml - Tuning-write template.
  - See also Coverity tools in a Coverity cloud deployment and Read-only file system error.
- In the 2024.9.0 release, the Coverity Connect web app administrator default password
  was changed, and the 2024.9.0 release supports a new Web application administrator
  password feature that enables you to create and change the Web application
  administrator password. This document, for the current 2025.6.0 release, highly
  recommends that you change the password during initial deployment. If you do not
  create a password, to re-connect to the web app as administrator, you will need to
  manually create a password secret, or contact Black Duck Software for the default
  password.

  Important: If you are upgrading from
  Coverity 2024.6.x or older, or if you have not yet created a Coverity Connect
  web app administrator password, you must create a new Connect web app
  administrator password as part of the upgrade in order to retain login
  access.
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

The following table identifies a Helm key added in the 2025.6.0 release.

Table 1. Helm key added in 2025.6.0

| Helm key | Notes |
| --- | --- |
| ``` storage-service:   azure:     ​​authMode: ``` | `scan-services` Helm subchart:  New `authMode` Helm key to select from new `sharedKey` and `aadClientSecret`authorization modes.  See storage-service.azure Helm keys. |

The following table identifies a Helm key whose functionality expanded in the 2025.6.0
release.

Table 2. Helm key with expanded functionality in 2025.6.0

| Helm key | Notes |
| --- | --- |
| ``` storage-service:   ​​azure:     storageAccountName: "" ``` | `scan-services` Helm subchart:  Redesigned to support both `sharedKey` and `aadClientSecret` authorization modes.  See storage-service.azure Helm keys. |
