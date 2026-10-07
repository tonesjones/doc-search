---
title: "enabling-oci-minio"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enabling-oci-minio.html"
content_id: "_fFi4oGrE25peNt8gH~cXg"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:34.547868+00:00"
---

# enabling-oci-minio

## Integrated OCI Bitnami MinIO chart

The following excerpt from the `cnc` chart
`values.yaml` file contains default values that can be used to
setup MinIO in-memory cache. By default, these Helm keys are commented. If you
enable onPrem (OCI) MinIO, uncomment the following Helm key rows by replacing the
`#` symbol with a space to preserve 2-space YAML indentation.

For further Bitnami OCI MinIO information, refer to <https://github.com/bitnami/charts/blob/main/bitnami/minio/README.md>.

In the following chart segment, the sidecar is required when cache-service is
enabled. It sets the lifecycle configuration for the cache-service bucket. The
sidecar needs a secret containing the following keys: minio-access-key and
minio-secret-key.

Update the cache_bucket_name, retention-days and other environment variables as
needed.

```
# minio:
#   global:
#     security:
#       allowInsecureImages: true
#   fullnameOverride: "cnc-minio"
#   # MinIO Server - July 23rd, 2025
#   image:
#     registry: registry-1.docker.io
#     repository: bitnamilegacy/minio
#     tag: "2025.7.23-debian-12-r3"
#     debug: true
#   # MinIO Client - July 21st, 2025
#   clientImage:
#     registry: registry-1.docker.io
#     repository: bitnamilegacy/minio-client
#     tag: "2025.7.21-debian-12-r2"
#   # Default Init Containers Volume Permissions
#   defaultInitContainers:
#     volumePermissions:
#       image:
#         registry: registry-1.docker.io
#         repository: bitnamilegacy/os-shell
#         tag: "12-debian-12-r51"
#   # Console/Gateway Image
#   console:
#     image:
#       registry: registry-1.docker.io
#       repository: bitnamilegacy/minio-object-browser
#       tag: "2.0.2-debian-12-r3"
#   ingress:
#     enabled: true
#     ingressClassName: nginx
#     hostname: local.connect.example.com
#     extraTls:
#     - hosts:
#         - local.connect.example.com
#       secretName: cnc-cim-tls-nginx
#     path: "/upload(/|$)(.*)"
#     annotations:
#       ingress.kubernetes.io/hsts: "true"
#       ingress.kubernetes.io/ssl-redirect: "true"
#       nginx.ingress.kubernetes.io/enable-access-log: "true"
#       nginx.ingress.kubernetes.io/proxy-body-size: 8g
#       nginx.ingress.kubernetes.io/proxy-connect-timeout: "5"
#       nginx.ingress.kubernetes.io/proxy-next-upstream: error timeout
#       nginx.ingress.kubernetes.io/proxy-next-upstream-timeout: "0"
#       nginx.ingress.kubernetes.io/proxy-next-upstream-tries: "3"
#       nginx.ingress.kubernetes.io/rewrite-target: /$2

#   podAnnotations:
#     prometheus.io/scrape: "true"
#     prometheus.io/path: "/minio/v2/metrics/cluster"
#     prometheus.io/port: "9000"
#   persistence:
#     size: 50Gi

#   # This sidecar is needed when the cache-service is enabled which will set the lifecycle configuration for the cache-service bucket
#   #   This sidecar needs a secret with key minio-access-key, minio-secret-key which will be created by minio helm chart itself with minio release name
#   #   Please update the cache_bucket_name, retention-days and other env's accordingly
#   sidecars:
#     - name: minio-lifecycle
#       image: registry-1.docker.io/bitnamilegacy/minio-client:2025.7.21-debian-12-r2
#       imagePullPolicy: IfNotPresent
#       env:
#         - name: cache_bucket_name
#           value: coverity-cache
#         - name: cache-retention-limit
#           value: "30"
#         - name: minio-host
#           value: cnc-minio
#         - name: minio-port
#           value: "9000"
#         - name: minio-access-key
#           valueFrom:
#             secretKeyRef:
#               name: cnc-minio
#               key: root-user
#         - name: minio-secret-key
#           valueFrom:
#             secretKeyRef:
#               name: cnc-minio
#               key: root-password
#       command: ["/bin/bash","-c"]
#       args:
#         - |
#           echo "waiting for minio..."

#           until (mc alias set cnc http://$(minio-host):$(minio-port) $(minio-access-key) $(minio-secret-key) && mc ls cnc/$(CACHE_BUCKET_NAME))
#           do sleep 5;
#           done;
#           mc ilm add --expiry-days $(cache-retention-limit) cnc/$(cache_bucket_name);
#           tail -f /dev/null;
```

Note: The `sidecars:` above are needed if
cache-service is enabled.
