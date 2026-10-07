---
title: "Enabling SCM Integration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/enabling-scm-integration.html"
content_id: "eAWAkCE~V7Da_5EBi0kLEg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.585808+00:00"
content_hash: "b970fbf682ba2958cea483f4062206a60debd3348031cdf7a2bd6c7f625ff115"
---

# Enabling SCM Integration

This feature is not enabled by default in Black Duck and must be activated by adding the feature to your Product Registration key.

To enable SCM integration, you must deploy `docker-compose.integration.yml`, no further configuration is required. The following environment variable will be automatically added:

```
  webserver:
    environment: {ENABLE_INTEGRATION_SERVICE: "true"}
```
