---
title: "Disabling TLS/SSL"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/disabling-tls/ssl.html"
content_id: "haFsx9xtZhgeDoXLezT~ug"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:34.677802+00:00"
---

# Disabling TLS/SSL

If TLS/SSL is not required, the configuration can be simplified by removing SSL-related
arguments and disabling TLS:

Important: When disabling TLS, ensure that your network
environment is secure. Database connections will not be encrypted.

1. Remove SSL arguments from `postgresql.primary.args`:

   ```
   yaml postgresql: primary: args: - "-c" - "hba_file=/bitnami/postgresql/conf/pg_hba.conf" # Remove these SSL-related arguments: # - "-c" # - "ssl=on" # - "-c" # - "ssl_cert_file=/opt/bitnami/postgresql/certs/server.pem" # - "-c" # - "ssl_key_file=/opt/bitnami/postgresql/certs/key-server.pem"
   ```
2. Disable TLS in the configuration:

   ```
   yaml postgresql.tls.enabled: false
   ```

Complete example with TLS disabled:

```
postgresql:
  primary:
    pgHbaConfiguration: |
      local   all             all                               md5
      host    all             all             0.0.0.0/0         md5
      host    all             all             ::/0              md5
      host    all             all             127.0.0.1/32      md5
      host    all             all             ::1/128           md5
    args:
      - "-c"
      - "hba_file=/bitnami/postgresql/conf/pg_hba.conf"
    extraVolumes:
      - name: postgres-run
        emptyDir: { }
    extraVolumeMounts:
      - name: postgres-run
        mountPath: /var/run/postgresql
  commonAnnotations:
    helm.sh/hook: "pre-install, pre-upgrade, pre-rollback"
    helm.sh/hook-weight: "-13"
  fullnameOverride: "cim-pg-postgresql"
  auth:
    database: "postgres"
    postgresPassword: "postgres"
  image:
    registry: registry-1.docker.io
    repository: "postgres"
    tag: "18.4"
    pullSecrets: ["gar-key"]
  metrics:
    enabled: true
    image:
      registry: registry-1.docker.io
      repository: "prometheuscommunity/postgres-exporter"
      tag: "v0.19.1"
  volumePermissions:
    enabled: true
    image:
      registry: registry-1.docker.io
      repository: "alpine"
      tag: "3.21.7"
  tls:
    enabled: false
```
