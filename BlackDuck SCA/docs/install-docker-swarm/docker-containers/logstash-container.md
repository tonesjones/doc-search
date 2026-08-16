---
title: "Logstash container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/logstash-container.html"
content_id: "shlSqGaCK2P6SjltlSlcAQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:23.234695+00:00"
---

# Logstash container

| Container Name: blackduck-logstash | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-logstash:1.0.10 |
| Description | The Logstash container collects and store logs for all containers. |
| Scalability | There should only be a single instance of this container. It should not be scaled. |
| Links/Ports | The container needs to expose port 5044 within the Docker network to other containers/services that will link to it. |
| Resources/Constraints | - Default max Java heap size: 1GB - Container memory: 1GB - Container CPU: Unspecified |
| Users/Groups | This container runs as UID 100. If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
