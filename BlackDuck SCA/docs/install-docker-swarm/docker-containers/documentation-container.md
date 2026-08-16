---
title: "Documentation container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/documentation-container.html"
content_id: "NsHjDaGPGYyidjJ~3NaOzA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:21.549639+00:00"
---

# Documentation container

| Container Name: blackduck-documentation | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-documentation:2026.7.0 |
| Description | The Documentation container supplies documentation for the application. |
| Scalability | There is a single instance of this container. It should not be scaled. |
| Links/Ports | This container must connect to these other containers/services:   - logstash - cfssl   The documentation container must expose port 8443 to other containers that link to it. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST |
| Resources/Constraints | - Default Max Java Heap Size: 512MB - Container Memory: 512MB - Container CPU: unspecified |
| Users/Groups | This container runs as UID 8080. If the container is started as UID 0 (root) then the user will be switched to UID 8080:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
