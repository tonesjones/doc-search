---
title: "Bomengine container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/bomengine-container.html"
content_id: "9aXio497vZaYJUW2dyBaiw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:19.862704+00:00"
---

# Bomengine container

| Container Name: bomengine | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-bomengine:2026.7.0 |
| Description | The bomengine container is responsible for building BOMs and keeping them up-to-date. |
| Scalability | The container can be scaled |
| Links/Ports | The bomengine container needs to connect to the following container/services:   - postgres - registration - logstash - cfssl |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that any individual service name may be different. For example, you may have an external PostgreSQL endpoint which is resolved through a different service name. To support such use cases, these environment variables can be set to override the default host names:   - postgres: $HUB_POSTGRES_HOST - registration: $HUB_REGISTRATION_HOST - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST |
| Resources/Constraints | - Default max Java heap size: 4GB - Container memory: 4.5GB |
| Users/Groups | This container runs as UID 100  If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing its main process.This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
