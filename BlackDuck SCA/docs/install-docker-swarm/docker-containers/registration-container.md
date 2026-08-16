---
title: "Registration container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/registration-container.html"
content_id: "1dcQYq4gkz5Q0IIOw1TqyA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:24.942362+00:00"
---

# Registration container

| Container Name: blackduck-registration | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-registration:2026.7.0 |
| Description | The container is a small service that handles registration requests from the other containers. At periodic intervals, this container connects to the Black Duck Registration Service and obtains registration updates. |
| Scalability | The container should not be scaled. |
| Links/Ports | The Registration container needs to connect to this containers/services:   - logstash - cfssl   The container needs to expose port 8443 to other containers that link to it. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST |
| Resources/Constraints | - Default max Java heap size: 512MB - Container memory: 640MB - Container CPU: Unspecified |
| Users/Groups | This container runs as UID 8080. If the container is started as UID 0 (root) then the user will be switched to UID 8080:root before executing its main process. This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
