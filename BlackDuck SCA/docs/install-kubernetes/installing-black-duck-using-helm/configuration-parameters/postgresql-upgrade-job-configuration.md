---
title: "PostgreSQL upgrade job configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/postgresql-upgrade-job-configuration.html"
content_id: "uEDHnhEzEVGBV_m50Bq0zA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.039672+00:00"
content_hash: "b32408d6e9e11d9a7f7e420659c74b59f1fff67aa2c4cb67fd7663d5a6f33ca7"
---

# PostgreSQL upgrade job configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `postgresUpgrader.registry` | Image repository |  |
| `postgresUpgrader.podSecurityContext` | Postgres upgrader security context at job level | `{}` |
| `postgresUpgrader.securityContext` | Postgres upgrader security context at container level | `{}` |
