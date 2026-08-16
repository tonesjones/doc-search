---
title: "Integration container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/integration-container.html"
content_id: "AxU1dP3zI2xLoJO2QojPaQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:22.113200+00:00"
---

# Integration container

| Container Name: blackduck-integration | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-integration:2026.7.0 |
| Description | The integration service that is responsible for Artifactory integration and Git SCM provider integration scan functionality. |
| Scalability | There can be multiple instances of this container.   - Requirement that all scan services are on the same Docker   network as the other containers. - Integration services can be present on different hosts or   nodes. |
| Links/Ports | This container must connect to these other containers/services:   - cfssl - postgres - rabbitmq - registration - logstash - scan   The integration container must expose port 8443 to other containers that link to it. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - postgres: $HUB_POSTGRES_HOST - registration: $HUB_REGISTRATION_HOST - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST - rabbitmq: $RABBIT_MQ_HOST, $RABBIT_MQ_PORT |
| Resources/Constraints | - Default Max Java Heap Size: 5120MB - Container Memory: 5120MB - Container CPU: 1 CPU |
| Users/Groups | This container runs as UID 8080. If the container is started as UID 0 (root) then the user will be switched to UID 8080:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
