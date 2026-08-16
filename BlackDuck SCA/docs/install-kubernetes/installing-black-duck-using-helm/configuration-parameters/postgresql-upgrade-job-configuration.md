---
title: "PostgreSQL upgrade job configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/postgresql-upgrade-job-configuration.html"
content_id: "Nnb6MzNOUnEFLTePQDTw~w"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:11.782111+00:00"
---

# PostgreSQL upgrade job configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `postgresUpgrader.registry` | Image repository |  |
| `postgresUpgrader.podSecurityContext` | Postgres upgrader security context at job level | `{}` |
| `postgresUpgrader.securityContext` | Postgres upgrader security context at container level | `{}` |
