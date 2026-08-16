---
title: "Storage container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/storage-container.html"
content_id: "s3LDi8TV8gZy_~BwauLhIg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:26.073752+00:00"
---

# Storage container

| Container Name: blackduck-storage | |
| --- | --- |
| Image Name | blackducksoftware/blackduck-storage:2026.7.0 |
| Description | The storage service provides functionality for many users with the ability to upload files, download files, and define the default file when a file has multiple available versions. |
| Scalability | This container can be scaled. |
| Links/Ports | This container needs to connect to these containers/services:   - postgres - registration - rabbitmq - logstash - cfssl |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that any individual service name may be different. For example, you may have an external PostgreSQL endpoint which is resolved through a different service name. To support such use cases, these environment variables can be set to override the default host names:   - postgres: $HUB_POSTGRES_HOST - registration: $HUB_REGISTRATION_HOST - rabbitmq: $RABBIT_MQ_HOST - logstash: $HUB_LOGSTASH_HOST - cfssl: $HUB_CFSSL_HOST |
| Resources/Constraints | - Default max java heap size: 512MB - Container memory: 1GB |
| Users/Groups | If the container is started as UID 0 (root) then the user will be switched to UID 100:root before executing its main process. This container is also able to be started as a random UID as long as it is also started within the root group (GID/fsGroup 0). |
| Environment File | `blackduck-config.env` |
