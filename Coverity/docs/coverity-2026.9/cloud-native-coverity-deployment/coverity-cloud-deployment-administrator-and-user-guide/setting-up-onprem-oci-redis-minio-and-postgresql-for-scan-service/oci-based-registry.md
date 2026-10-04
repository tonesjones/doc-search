---
title: "OCI-based registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/oci-based-registry.html"
content_id: "HugzKmJwLUT1Sda_QMdeDQ"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:34.325562+00:00"
---

# OCI-based registry

The 2024.12.0 release:

- integrates the onPrem open-source OCI-based MinIO Helm chart, Redis Helm chart, and
  PostgreSQL Helm chart into the `cnc` chart.
- introduces MinIO, Redis, and PostgreSQL dependencies in the Chart.yaml file, based
  on the Helm overide (onPrem.minio, onPrem.redis, and onPrem PostgreSQL) it will
  install the onPrem resources.

Important: We recommend using Helm version 3.8.0 or
greater to use OCI based Helm repositories.

For information about OCI based Helm
registries, see <https://helm.sh/docs/topics/registries/>.
