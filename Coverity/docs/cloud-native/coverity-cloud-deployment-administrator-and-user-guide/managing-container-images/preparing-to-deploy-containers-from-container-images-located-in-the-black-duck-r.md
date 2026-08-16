---
title: "Preparing to deploy containers from container images located in the Black Duck registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preparing-to-deploy-containers-from-container-images-located-in-the-black-duck-registry.html"
content_id: "6ATkLR4GZXZgErJAv8bBpw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:47.107100+00:00"
---

# Preparing to deploy containers from container images located in the Black Duck registry

To prepare to deploy Coverity cloud containers from container images located in the Black
Duck private registry:

Important: Optional method. Not recommended.

- You do not need to create your own private registry for the container images.
- You do not need to pull any container images. They will be automatically downloaded
  when you deploy Coverity.
- You need to set a few of the following Helm keys. You can accept the default values
  for most of the following Helm keys. Most of the image Helm keys are already
  configured to automatically download container images from the Black Duck registry
  when you deploy Coverity
  cloud.

  ```
  Either cnc chart or scan-services subchart:
  global:
    imagePullPolicy: IfNotPresent
    imagePullSecret: ""     # To apply globally, provide the name of the image pull secret.
    imageRegistry: "COVERITY_IMAGE_REGISTRY"
    imageVersion: ""
    imageTagSuffix: ""      # If you are deploying on Open Shift, you need to set this to "-ubi".

  # The only time you might need to set these is if you use different registries for cnc chart container images
  # vs scan-services chart container images.
  imagePullPolicy: ""
  imagePullSecret: ""       # Use this key to provide separate values for the Connect and scan service repositories.
  imageRegistry: ""
  imageVersion: ""
  imageTagSuffix: ""

  cnc chart:

  cim:
   cimdownloads:
      enabled: true
      image: "cim-downloads"
      registry: ""
      version: "CIM_VERSION"

   cimtools:
      enabled: true
      image: "cim-tools"
      registry: ""
      version: "CIM_VERSION"

    cimweb:
      image: "cim-web"
      registry: ""
      version: "CIM_VERSION"

  scan-services subchart:

  cache-service:
    image: "cache-service"
    registry: ""
    version: "CACHE_SERVICE_VERSION"

    # Storage Provider : Accepted values are `minio`, `gcp`, `aws` and `azure`
    storageProvider: "minio"

  common-infra:
    image: "common-infra"
    version: "COMMON_INFRA_VERSION"
    registry: ""

  scan-service:
    image: "scan-service"
    registry: ""
    version: "SCAN_SERVICE_VERSION"

    dispatcher:
      imagePullPolicy: "IfNotPresent"

    migrateJob:
      image: "scan-service-migration"
      registry: ""
      version: "SCAN_SERVICE_VERSION"

      # if true, run the scan db schema upgrade; otherwise skip this db upgrade
      enabled: true

    jobRunner:
      image: "job-runner"
      registry: ""
      version: "RUNNER_VERSION"

  storage-service:

    image: "storage-service"
    registry: ""
    version: "STORAGE_SERVICE_VERSION"

    # the name for the backing storage type; must be one of: s3, s3Express, gcs, azure
    storageType: ""

    migrateJob:
      image: "storage-service-migration"
      registry: ""
      version: "STORAGE_SERVICE_VERSION"

      # if true, run the storage db schema upgrade; otherwise skip this db upgrade
      enabled: true
  ```
- Create a container image pull secret to access your registry. See Create a container image pull secret.
- Update the following Helm key(s) with the name of the image pull secret.

  For a single repository that is stores both cnc and scan-services container
  images:

  ```
  global:
    imagePullSecret: ""
  ```

  For separate repositories, one for Connect images (cnc chart) and one for scan
  services images (scan-services chart):

  ```
  cnc:
    imagePullSecret: ""

  scan-services:
    imagePullSecret: ""
  ```
- If you are deploying on Red Hat Open Shift, you need to set the -ubi tag as shown in
  the following Helm key:

  ```
  global:
    imageTagSuffix: "-ubi"
  ```

## Third-party container images

```
cim:
  cimweb:
    tlsSidecar:

      # The image name to use
      image: "nginx"

      # The image registry to use
      registry: ""

      # The image version to use
      version: "1.27.4"

      # this will enable the tlsSidecar
      enabled: false

  pgpool:
    # if true, install pgpool. This is not needed to run Connect.
    # make sure atleast one db read-replica is available.
    # Note: It will enable commit-server and redirect all commit-defects traffic to the commit server.
    enabled: false

    # The image name to use
    image: "pgpool"

    # The image registry to use
    registry: ""

    # The image version to use
    version: "4.6.0"
```
