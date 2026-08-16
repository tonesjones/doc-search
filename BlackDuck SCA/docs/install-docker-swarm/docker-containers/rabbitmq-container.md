---
title: "Rabbitmq container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/rabbitmq-container.html"
content_id: "D27tBpA~E6SMm6CMQFyyxw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:23.811158+00:00"
---

# Rabbitmq container

| Container Name: rabbitmq | |
| --- | --- |
| Image Name | blackducksoftware/rabbitmq:1.2.2 |
| Description | This container facilitates upload information to the binary analysis worker. It also enables the bomengine container to receive notification to start BOM computation. It exposes ports within the Docker network, but not outside the Docker network. |
| Scalability | There should only be a single instance of this container. It should not be scaled. |
| Links/Ports | This container needs to connect to these other containers/services:   - cfssl   The container needs to expose port 5671 to other containers that will link to it. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - cfssl: $HUB_CFSSL_HOST |
| Constraints | - Default max Java heap size: N/A - Container memory: 1GB - Container CPU: Unspecified |
| Users/Groups | This container runs as UID 100. If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing it's main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
