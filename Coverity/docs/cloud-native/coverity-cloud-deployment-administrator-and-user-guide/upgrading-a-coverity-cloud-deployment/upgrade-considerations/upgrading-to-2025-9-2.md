---
title: "Upgrading to 2025.9.2"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.9.2.html"
content_id: "RMWzr98qmFjEDEY2V~gp0A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:30.642699+00:00"
---

# Upgrading to 2025.9.2

The 2025.9.2 release introduces the following changes that can impact the upgrade
process:

- For Dell ECS and for generic custom domains, this release includes new environment
  variables for custom certificates and new Coverity Connect Helm keys that accept
  annotations to mount additional storage service storage volumes. Also, the
  documentation provides more thorough guidance on deploying custom domains for
  storage service configurations. Refer to:
  - For Dell ECS storage, see Configure Dell ECS storage support.
  - For generic custom storage domains, see Storage service custom domains.
- For an on-premises Coverity cloud 2025.9.2 release deployment that uses OCI Redis
  and MinIO, this release provides new files, Helm keys, and documentation designed to
  enable you to pull and manage Bitnami images that have been migrated to a new
  bitnamilegacy repository. See Working with the migrated Bitnami registry.
- This release increases the maximum hostname size from a limit of 36 characters to
  a tested limit of 46 characters. For example, see the following note which
  appears in Generating a Coverity Connect TLS certificate signed by a Certificate Authority.

  Important: The Connect (cim) hostname that you
  specify in `cim.ingress.hosts` must not exceed 46 characters in
  length. This restriction excludes the `https://` characters that
  are used when you specify the URL, as well as any port specification.
- Documentation: Defined certificates, keystores, secrets, and truststore ConfigMaps,
  and clarified their use and creation. See Create TLS certificate, keystore, and secrets and
  Create a truststore ConfigMap for Connect communication over TLS.
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

The following table identifies new Helm keys in the 2025.9.2 release.

Table 1. New Helm keys in 2025.9.2

| Helm key | Notes |
| --- | --- |
| ``` scan-service:   environment:     TLS_CUSTOM_ENABLED: false     TLS_CUSTOM_CERT_PATH: "" ``` | `scan-services` Helm chart:  These new Helm keys configure custom TLS environment variables.  For further information, see:   - for generic custom storage, see Storage service custom domains. - for Dell ECS S3 storage, see Configure Dell ECS storage support. - for the Helm keys, see scan-service Helm keys in the chart chapter scan-services Helm subchart: Helm keys. |
| ``` scan-service:   extraVolumeMounts: [] storage-service:   extraVolumeMounts: [] ``` | `scan-services` Helm chart:  These new Helm keys mount additional storage volumes to scan service and storage service pods.  For further information, see:   - for generic custom storage, see Storage service custom domains. - for Dell ECS S3 storage, see Configure Dell ECS storage support. - for the Helm chart, see scan-services Helm subchart: Helm keys. |
| ``` # onPrem helm overrides for open-source sub-charts # redis: #   global: #     security: #       allowInsecureImages: true ``` | Bitnami: See Working with the migrated Bitnami registry. |
| ``` # redis: #   # Redis bitnami legacy images - Aug 22nd, 2025 #   image: #     registry: registry-1.docker.io #     repository: bitnamilegacy/redis #     tag: "8.2.1-debian-12-r0" #   # Redis Sentinel - Aug 19th, 2025 #   sentinel: #     image: #       registry: registry-1.docker.io #       repository: bitnamilegacy/redis-sentinel #       tag: "8.2.1-debian-12-r0" ``` | Bitnami: See Working with the migrated Bitnami registry. |
| ``` # redis: ... #     # Redis Exporter - Aug 24th, 2025 #     image: #       registry: registry-1.docker.io #       repository: bitnamilegacy/redis-exporter #       tag: "1.76.0-debian-12-r0" #   # Volume Permissions - Aug 19th, 2025 #   volumePermissions: #     image: #       registry: registry-1.docker.io #       repository: bitnamilegacy/os-shell #       tag: "12-debian-12-r51" #   # Kubectl - Aug 23rd, 2025 #   kubectl: #     image: #       registry: registry-1.docker.io #       repository: bitnamilegacy/kubectl #       tag: "1.33.4-debian-12-r0" #   # Sysctl - Aug 19th, 2025 #   sysctl: #     image: #       registry: registry-1.docker.io #       repository: bitnamilegacy/os-shell #       tag: "12-debian-12-r51" ``` | Bitnami: See Working with the migrated Bitnami registry. |
| ``` # minio: #   onPrem: true #   global: #     security: #       allowInsecureImages: true #   fullnameOverride: "cnc-minio"  #   # MinIO Server - July 23rd, 2025 #   image: #     registry: registry-1.docker.io #     repository: bitnamilegacy/minio #     tag: "2025.7.23-debian-12-r3" #     debug: true  #   # MinIO Client - July 21st, 2025 #   clientImage: #     registry: registry-1.docker.io #     repository: bitnamilegacy/minio-client #     tag: "2025.7.21-debian-12-r2" #   # Default Init Containers Volume Permissions #   defaultInitContainers: #     volumePermissions: #       image: #         registry: registry-1.docker.io #         repository: bitnamilegacy/os-shell #         tag: "12-debian-12-r51" #   # Console/Gateway Image #   console: #     image: #       registry: registry-1.docker.io #       repository: bitnamilegacy/minio-object-browser #       tag: "2.0.2-debian-12-r3" #   ingress: #     enabled: true #     ingressClassName: nginx #   # Update cache_bucket_name, retention-days, and other environment values. #   sidecars: #     - name: minio-lifecycle #       image: docker.io/minio/mc:latest #       image: registry-1.docker.io/bitnamilegacy/minio-client:2025.7.21-debian-12-r2 #       imagePullPolicy: IfNotPresent ``` | Bitnami: See Working with the migrated Bitnami registry. |

Table 2. Removed Helm keys in 2025.9.2

| Helm key | Notes |
| --- | --- |
| ``` # minio.onPrem: true ``` |  |
| ``` # minio.sidecars.image: docker.io/minio/mc:latest ``` | The value of this Helm key is changed:   - from: `docker.io/minio/mc:latest` - to:   `registry-1.docker.io/bitnamilegacy/minio-client:2025.7.21-debian-12-r2` |

Table 3. Changed Helm keys in 2025.9.2

| Helm key | Notes |
| --- | --- |
| ``` # minio.apiIngress ``` | Changed to:   ``` # minio.ingress ``` |
