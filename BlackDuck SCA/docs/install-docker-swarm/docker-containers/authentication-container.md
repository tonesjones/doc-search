---
title: "Authentication container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/authentication-container.html"
content_id: "A~8WXCeBYjcS6~Tg95tLgw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:18.738817+00:00"
---

# Authentication container

| Container Name: blackduck-authentication | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-authentication:2026.7.0 |
| Description | The authentication service is the container that all authentication-related requests are made against. |
| Scalability | There should only be a single instance of this container. It currently cannot be scaled. |
| Links/Ports | Nothing external (8443 internally). This container will need to connect to these other containers/services:   - postgres - cfssl - logstash - registration - webapp   The container needs to expose 8443 to other containers that will link to it. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - postgres - $HUB_POSTGRES_HOST - cfssl - $HUB_CFSSL_HOST - logstash - $HUB_LOGSTASH_HOST - registration - $HUB_REGISTRATION_HOST - webapp - $HUB_WEBAPP_HOST |
| Resources/Constraints | - Default max Java heap size: 512MB - Container memory: 1GB - Container CPU: 1 CPU |
| Users/Groups | This container runs as UID 100. If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
