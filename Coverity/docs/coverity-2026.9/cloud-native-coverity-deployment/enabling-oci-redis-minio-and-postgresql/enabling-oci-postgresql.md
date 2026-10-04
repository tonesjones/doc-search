---
title: "Enabling OCI PostgreSQL"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enabling-oci-postgresql.html"
content_id: "8AVv1EHyzBDTbfqz0gPb1Q"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:34.592239+00:00"
---

# Enabling OCI PostgreSQL

## Integrated Bitnami PostgreSQL chart

The following excerpt from the `cnc` chart
`values.yaml` file contains default values that can be used to
setup PostgreSQL. By default, these Helm keys are commented. If you enable onPrem
(OCI) PostgreSQL, uncomment the following Helm key rows by replacing the
`#` symbol with a space to preserve 2-space YAML indentation.

For further OCI PostgreSQL information, refer to <https://github.com/bitnami/charts/tree/main/bitnami/postgresql>.

```
# postgresql:
#   primary:
#     pgHbaConfiguration: |
#       local   all             all                               md5
#       host    all             all             0.0.0.0/0         md5
#       host    all             all             ::/0              md5
#       host    all             all             127.0.0.1/32      md5
#       host    all             all             ::1/128           md5
#     args:
#       - "-c"
#       - "hba_file=/bitnami/postgresql/conf/pg_hba.conf"
#       # Comment these if TLS is to be disabled. Ensure the certificate filenames
#       # in ssl_cert_file and ssl_key_file match the certFilename and certKeyFilename
#       # specified in the tls section below if tls is enabled (currently: certificate.pem and key.pem)
#       - "-c"
#       - "ssl=on"
#       - "-c"
#       - "ssl_cert_file=/opt/bitnami/postgresql/certs/certificate.pem"
#       - "-c"
#       - "ssl_key_file=/opt/bitnami/postgresql/certs/key.pem"
#     extraVolumes:
#       - name: postgres-run
#         emptyDir: { }
#     extraVolumeMounts:
#       - name: postgres-run
#         mountPath: /var/run/postgresql
#   commonAnnotations:
#     helm.sh/hook: "pre-install, pre-upgrade, pre-rollback"
#     helm.sh/hook-weight: "-13"
#   fullnameOverride: "cim-pg-postgresql"
#   auth:
#     database: "postgres"
#     postgresPassword: "postgres"
#   image:
#     registry: registry-1.docker.io
#     repository: "postgres"
#     tag: "18.4"
#     pullSecrets: ["gar-key"]
#   metrics:
#     enabled: true
#     image:
#       registry: registry-1.docker.io
#       repository: "prometheuscommunity/postgres-exporter"
#       tag: "v0.19.1"
#   volumePermissions:
#     enabled: true
#     image:
#       registry: registry-1.docker.io
#       repository: "alpine"
#       tag: "3.21.7"
#   tls:
#     enabled: true
#     certFilename: "certificate.pem"
#     certKeyFilename: "key.pem"
#     certificatesSecret: "postgres-certificates-tls-secret"
```
