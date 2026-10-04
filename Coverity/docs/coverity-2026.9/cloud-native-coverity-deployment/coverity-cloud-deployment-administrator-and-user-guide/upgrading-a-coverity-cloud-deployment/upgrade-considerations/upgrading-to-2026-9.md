---
title: "Upgrading to 2026.9"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/upgrading-to-2026.9.html"
content_id: "OX8SZvT3~qysjEPjPnzJrw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:38.910610+00:00"
---

# Upgrading to 2026.9

The 2026.9 release introduces the following changes that can impact the upgrade
process:

- The on-cluster Redis deployment now uses official Docker Hub images instead of
  Bitnami-packaged images.
- If your deployment uses on-cluster Redis, update the Redis configuration in
  `values.yaml` before upgrading. The Helm chart does not
  automatically migrate existing Redis image settings. Legacy Bitnami image references
  are no longer supported and must be replaced with the supported image values. For
  more information, see enabling_oci_redis.dita.
- Set `redis.global.security.allowInsecureImages` to
  `true`. This setting is required when using the official Docker
  Hub Redis images. For more information, see 
  enabling_oci_redis.dita.
- The Redis metrics exporter configuration has changed. Update the metrics exporter
  configuration before upgrading. For more information, see enabling_oci_redis.dita.
- If onfigure
  `redis.auth.existingSecret` and
  `redis.auth.existingSecretPasswordKey` to preserve the existing
  Redis password during upgrade.
- The LDAP encryption key configuration has changed. The
  `cim.ldap.cimKey.value` Helm key has been removed and replaced by
  `cim.ldap.keySecret.existingSecret`. If your deployment uses a
  custom LDAP encryption key, migrate the key to a Kubernetes Secret before
  upgrading. For more information, see
  Migrating the LDAP encryption key to a Kubernetes Secret.

Important: If `redis.auth.existingSecret` and
`redis.auth.existingSecretPasswordKey` are not configured during
upgrade, the Redis subchart can generate a new password and overwrite the existing
secret. This can prevent CNC services from connecting to Redis after the upgrade.

Important: If your deployment uses a custom LDAP encryption key,
create a Kubernetes Secret containing the key and configure
`cim.ldap.keySecret.existingSecret` before upgrading. If
`cim.ldap.keySecret.existingSecret` is not configured, the chart
uses a chart-managed Secret containing the default LDAP encryption key. This can
cause LDAP authentication to fail.

Additionally, consider the following:

- As recommended, copy all container images from the new Black Duck repository to a
  local repository and use your local repository to deploy Coverity cloud.
- Download, modify as needed, and deploy the new Helm chart for the current
  release.
