---
title: "Scanmatch container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scanmatch-container.html"
content_id: "BkzMmt3xtLW7rsVqHoBFIg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:25.515036+00:00"
---

# Scanmatch container

| Container Name: blackduck-scanmatch | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-scanmatch:2026.7.0 |
| Description | The scanmatch service functions as the container that handles all scan data requests and retrieves component match information from the Cloud Knowledge Base. |
| Scalability | This container can be scaled. |
| Links/Ports | This container needs to connect to these containers/services:   - postgres - registration - logstash - cfssl - rabbitmq   The container needs to expose port 8443 to other containers that will link to it.  Connects externally to Cloud KB services. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - postgres: HUB_POSTGRES_HOST, HUB_POSTGRES_PORT - registration: HUB_REGISTRATION_HOST,   HUB_REGISTRATION_PORT - logstash: HUB_LOGSTASH_HOST - cfssl: HUB_CFSSL_HOST, HUB_CFSSL_PORT - rabbitmq: RABBIT_MQ_HOST, RABBIT_MQ_PORT |
| Resources/Constraints | Set in the `gen05` sizings. |
| Users/Groups | This container runs as UID 8080. If the container is started as UID 0 (root) then the user will be switched to UID 8080:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
