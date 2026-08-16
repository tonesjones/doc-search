---
title: "Working with the migrated Bitnami registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/working-with-the-migrated-bitnami-registry.html"
content_id: "rgbnZSFglrVRB4pXELkQ0Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:31.302048+00:00"
---

# Working with the migrated Bitnami registry

Bitnami moved its open-source images, which include Redis and MinIO images, from the
`bitnami` registry to the new `bitnamilegacy`
registry. Bitnami offers hardened, secure images via purchase plans. See the following
Bitnami documents for further information:

- [How to prepare for the Bitnami Changes
  coming soon](https://community.broadcom.com/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon)
- [Upcoming changes to the Bitnami catalog (effective
  August 28th, 2025) #83267](https://github.com/bitnami/containers/issues/83267)

Deployments on cloud platforms (AWS, GCP, Azure, OpenShift) should not be impacted by the
Bitnami registry migration.

However, starting in the 2024.12.0 release, the `cnc` Helm chart bundles
open-source Bitnami Redis and MinIO charts as subcharts within the `cnc`
chart. If you are installing or upgrading to 2025.9.2 and if you deploy the on-premises
(onPrem) charts, with the onPrem flags enabled, you need to now follow the guidelines
discussed in this section and related onPrem sections to access Bitnami images, namely
Redis and MinIO. You need to pull these images from a new bitnamilegacy image
registry.

Note: For information on deploying onPrem with Coverity cloud versions
2024.12.0 through 2025.9.0, see the knowledgebase article, Managing Bitnami
registry migration in 2024.12 through 2025.9.0 Coverity cloud
deployments.

The 2025.9.2 release incorporates a number of changes to address the Bitnami registry
change, including:

- New `legacy-images-values.yaml` file.
- Revised onPrem keys and values in the `cnc` Helm chart
  `values.yaml` file. See Enabling OCI Redis, MinIO, and PostgreSQL
  and onPrem Helm keys.

These changes result in a revised `helm` command syntax that you now need
to use when either installing or upgrading a Coverity cloud deployment. See 2025.9.2 Helm install or upgrade.

## New legacy-images-values.yaml file

The 2025.9.2 release contains a new `legacy-images-values.yaml` file
which overrides the registry, repository, and tag values of MinIO and Redis images.
You will need to include this file in any helm install or upgrade command to access
the legacy Bitnami files and successfully deploy Coverity.

```
# Bitnami Legacy Images Configuration
# This file provides bitnami legacy images
# 
# Usage:
#   helm install cnc ./cnc-chart -f legacy-images-values.yaml
#   helm upgrade cnc ./cnc-chart -f legacy-images-values.yaml
#

global:
  # Allow using bitnamilegacy images (bypass security validation)
  security:
    allowInsecureImages: true

# Override all MinIO images to use bitnamilegacy
minio:
  image:
    registry: registry-1.docker.io
    repository: bitnamilegacy/minio
    tag: "2025.7.23-debian-12-r3"
  clientImage:
    registry: registry-1.docker.io
    repository: bitnamilegacy/minio-client
    tag: "2025.7.21-debian-12-r2"
  defaultInitContainers:
    volumePermissions:
      image:
        registry: registry-1.docker.io
        repository: bitnamilegacy/os-shell
        tag: "12-debian-12-r51"
  console:
    image:
      registry: registry-1.docker.io
      repository: bitnamilegacy/minio-object-browser
      tag: "2.0.2-debian-12-r3"

# Override all Redis images to use bitnamilegacy  
redis:
  # Aug 22nd, 2025
  image:
    registry: registry-1.docker.io
    repository: bitnamilegacy/redis
    tag: "8.2.1-debian-12-r0"
  # Aug 19th, 2025
  sentinel:
    image:
      registry: registry-1.docker.io
      repository: bitnamilegacy/redis-sentinel
      tag: "8.2.1-debian-12-r0"
  # Aug 24th, 2025
  metrics:
    image:
      registry: registry-1.docker.io
      repository: bitnamilegacy/redis-exporter
      tag: "1.76.0-debian-12-r0"
  # Aug 19th, 2025
  volumePermissions:
    image:
      registry: registry-1.docker.io
      repository: bitnamilegacy/os-shell
      tag: "12-debian-12-r51"
  # Aug 23rd, 2025
  kubectl:
    image:
      registry: registry-1.docker.io
      repository: bitnamilegacy/kubectl
      tag: "1.33.4-debian-12-r0"
  # Aug 19th, 2025
  sysctl:
    image:
      registry: registry-1.docker.io
      repository: bitnamilegacy/os-shell
      tag: "12-debian-12-r51"
```

## Pulling images from bitnamilegacy

If you need to download images from the new bitnamilegacy registry, you can download
the images using the command:

```
docker pull bitnamilegacy/<APP>:<TAG>
```

Bitnamilegacy is an archive of older images, located on Docker Hub at
`https://hub.docker.com/r/bitnamilegacy` Pull and store these
images in your own registry, as the bitnamilegacy repository might be removed in the
future, and the images are not updated.

## 2025.9.2 Helm install or upgrade

The following command format illustrates `helm install` and
`helm upgrade` commands for a 2025.9.2 deployment. The examples
use the following flags:

- `--version` specifies the 2025.9.2 release.
- `--repo` is the Helm chart repository for Coverity cloud.
- `-n` specifies the Coverity namespace.
- `-f` specifies a `.yaml` file that overrides
  default chart values.

To install 2025.9.2:

```
helm install cnc \
    --version "2025.9.2"
    --repo ${repository-path} \
    -n cim \
    -f values.yaml \
    -f legacy-images-values.yaml
```

or:

```
helm install cnc ./cnc-chart -f legacy-images-values.yaml
```

To upgrade to 2025.9.2:

```
helm upgrade cnc \
    --version "2025.9.2"
    --repo ${repository-path} \
    -n cim \
    -f values.yaml \
    -f legacy-images-values.yaml
```

or:

```
helm upgrade cnc ./cnc-chart -f legacy-images-values.yaml
```
