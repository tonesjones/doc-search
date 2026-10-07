---
title: "Webserver container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/webserver-container.html"
content_id: "zFmbftBM6Td0OGcxaryOZw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:26.299986+00:00"
content_hash: "6f2d7bca72446a18403ffd3a80a612c2545b87798bd6adea39a1bcf3090de847"
---

# Webserver container

| Container Name: blackduck-webserver | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-nginx:1.0.32 |
| Description | The WebServer container is a reverse proxy for containers with the application. It has a port exposed outside of the Docker network. This is the container configured for HTTPS. There are config volumes here to allow for the configuration of HTTPS.  HTTP/2 and TLS 1.3 are supported |
| Scalability | The container should not be scaled. |
| Links/Ports | The Web App container needs to connect to these containers/services:   - webapp - cfssl - documentation - scan - authentication   This container exposes port 443 outside of the Docker network. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - webapp: $HUB_WEBAPP_HOST - cfssl: $HUB_CFSSL_HOST - scan: $HUB_SCAN_HOST - documentation: $HUB_DOC_HOST - authentication: $HUB_AUTHENTICATION_HOST |
| Resources/Constraints | - Default max Java heap size: N/A - Container memory: 512MB - Container CPU: Unspecified |
| Users/Groups | This container runs as UID 100. If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `hub-webserver.env`, `blackduck-config.env` |
