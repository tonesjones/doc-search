---
title: "CFSSL container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/cfssl-container.html"
content_id: "VAvXNusVW2xC3ZPcoH9Z6A"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:20.428991+00:00"
---

# CFSSL container

| Container Name: blackduck-cfssl | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-cfssl:1.0.2 |
| Description | This container uses CFSSL which is used for certificate generation for PostgreSQL, NGiNX, and clients that need to authenticate to Postgres. This container is also used to generate TLS certificates for the internal containers that make up the application. |
| Scalability | There should only be a single instance of this container. It should not be scaled. |
| Links/Ports | The container needs to expose port 8888 within the Docker network to other containers/services that link to it. |
| Resources/Constraints | - Default max Java heap size: N/A - Container memory: 512MB - Container CPU: Unspecified |
| Users/Groups | This container runs as UID 100. If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
