---
title: "PostgreSQL readiness init container configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/postgresql-readiness-init-container-configuration.html"
content_id: "2gvHg9vo7dLuzzuTI0U3kA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.016462+00:00"
content_hash: "b4a34f9f5f196f4fae57aa0c89284e7b7ea37712f7570f2600ca41f59fd8d2b3"
---

# PostgreSQL readiness init container configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `postgresWaiter.registry` | Image repository |  |
| `postgresWaiter.podSecurityContext` | Postgres readiness check security context at pod level | `{}` |
| `postgresWaiter.securityContext` | Postgres readiness check context at container level | `{}` |
