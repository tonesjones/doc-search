---
title: "PostgreSQL readiness init container configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/postgresql-readiness-init-container-configuration.html"
content_id: "reza9X0dCaZJdUG6eMdp4g"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:11.182035+00:00"
---

# PostgreSQL readiness init container configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `postgresWaiter.registry` | Image repository |  |
| `postgresWaiter.podSecurityContext` | Postgres readiness check security context at pod level | `{}` |
| `postgresWaiter.securityContext` | Postgres readiness check context at container level | `{}` |
