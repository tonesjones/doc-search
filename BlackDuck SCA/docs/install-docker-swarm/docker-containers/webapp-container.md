---
title: "Webapp container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/webapp-container.html"
content_id: "c2dabwK7mlGS6CTLZ~~1xg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:26.647408+00:00"
---

# Webapp container

| Container Name: blackduck-webapp | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-webapp:2026.7.0 |
| Description | The webapp container is the container that all Web/UI/API requests are made against. It also processes any UI requests. In the diagram, the ports for the webapp are not exposed outside of the Docker network. There is an NGiNX reverse proxy (as described in the WebServer container) that is exposed outside of the Docker network instead. |
| Scalability | There should only be a single instance of this container. It should not be scaled. |
| Links/Ports | The webapp container needs to connect to these containers/services:   - postgres - registration - logstash - cfssl   The container needs to expose port 8443 to other containers that will link to it. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - postgres: $HUB_POSTGRES_HOST - registration: $HUB_REGISTRATION_HOST - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST |
| Resources/Constraints | - Default max Java heap size: 2GB - Container memory: 2.5GB - Container CPU: 1 CPU |
| Users/Groups | This container runs as UID 8080. If the container is started as UID 0 (root) then the user will be switched to UID 8080:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
