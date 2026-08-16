---
title: "Enabling SCM Integration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/enabling-scm-integration.html"
content_id: "C~oqqfVix93BeX5Lhe7Y1g"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:11.011785+00:00"
---

# Enabling SCM Integration

This feature is not enabled by default in Black Duck and must be
activated by adding the feature to your Product Registration
key.

To enable SCM integration, you must deploy
`docker-compose.integration.yml`, no further configuration is
required. The following environment variable will be automatically added:

```
  webserver:
    environment: {ENABLE_INTEGRATION_SERVICE: "true"}
```
