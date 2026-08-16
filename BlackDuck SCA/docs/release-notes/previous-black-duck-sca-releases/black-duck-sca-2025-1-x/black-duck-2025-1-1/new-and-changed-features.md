---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "~XvJ2DDP0ATzj1VRKkmpCw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:43.621379+00:00"
---

# New and changed features

## Added support for IPv6 ingress and egress communication

Black Duck now supports IPv6-exclusive networks for both internal and external
communication. This enhancement ensures compatibility with IPv6-only environments,
enabling seamless communication between Black Duck components, the KnowledgeBase,
customer systems, and internet-facing networking pods.

## Added `justification` field to the `component_vulnerability` table

A new `justification` field has been added to the
`component_vulnerability` table in the reporting database. This
field store the justification details for vulnerabilities, providing additional
context for remediation decisions and analysis.

## Container versions

- blackducksoftware/blackduck-postgres:15-1.10
- blackducksoftware/blackduck-postgres-upgrader:15-1.3
- blackducksoftware/blackduck-postgres-waiter:1.0.14
- blackducksoftware/blackduck-cfssl:1.0.30
- blackducksoftware/blackduck-nginx:2025.1.1
- blackducksoftware/blackduck-logstash:1.0.40
- blackducksoftware/bdba-worker:2024.12.2
- blackducksoftware/rabbitmq:1.2.42
- blackducksoftware/blackduck-authentication:2025.1.1
- blackducksoftware/blackduck-bomengine:2025.1.1
- blackducksoftware/blackduck-documentation:2025.1.1
- blackducksoftware/blackduck-integration:2025.1.1
- blackducksoftware/blackduck-jobrunner:2025.1.1
- blackducksoftware/blackduck-matchengine:2025.1.1
- blackducksoftware/blackduck-redis:2025.1.1
- blackducksoftware/blackduck-registration:2025.1.1
- blackducksoftware/blackduck-scan:2025.1.1
- blackducksoftware/blackduck-storage:2025.1.1
- blackducksoftware/blackduck-webapp:2025.1.1
