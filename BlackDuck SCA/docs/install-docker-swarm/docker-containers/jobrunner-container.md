---
title: "Jobrunner container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/jobrunner-container.html"
content_id: "CeNyByvsm_Z8LtPyVR8T9w"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:26.078703+00:00"
content_hash: "c99ab7f7f67071747f97b01cca894ca0c13f962b54a55d5d37c4f4e3b1ab24b0"
---

# Jobrunner container

| Container Name: blackduck-Jobrunner | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-jobrunner:2026.7.1 |
| Description | The Job Runner container is the container that is responsible for running all of the application's jobs. This includes matching, BOM building, reports, data updates, and so on. This container does not have any exposed ports. |
| Scalability | This container can be scaled. |
| Links/Ports | The Job Runner container needs to connect to these containers/services:   - postgres - registration - logstash - cfssl |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that any individual service name may be different. For example, you may have an external PostgreSQL endpoint which is resolved through a different service name. To support such use cases, these environment variables can be set to override the default host names:   - postgres: $HUB_POSTGRES_HOST - registration: $HUB_REGISTRATION_HOST - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST |
| Resources/Constraints | - Default max Java heap size: 4GB - Container memory: 4.5GB - Container CPU: 1 CPU |
| Users/Groups | This container runs as UID 100. If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing its main process.  This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
