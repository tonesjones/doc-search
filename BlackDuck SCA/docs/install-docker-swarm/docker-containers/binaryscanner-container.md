---
title: "Binaryscanner container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/binaryscanner-container.html"
content_id: "W09L7HXCsURZR8AlSi85jg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:19.306318+00:00"
---

# Binaryscanner container

The following container will only be installed if you have Black Duck Binary Analysis.

| Container Name: bdba-worker | |
| --- | --- |
| Image Name | image: blackducksoftware/bdba-worker:2023.03 |
| Description | This container analyzes binary files.  This container is currently only used if Black Duck - Binary Analysis is enabled. |
| Scalability | This container can be scaled. |
| Links/Ports | This container needs to connect to these containers/services:   - cfssl - logstash - rabbitmq - webserver   The container will need to expose port 5671 to other containers that will link to it. |
| Alternate Host Name Environment Variables | There are times when running in other types of orchestrations that it is useful to have host names set for these containers that are not the default that Docker Swarm uses. These environment variables can be set to override the default host names:   - cfssl: $HUB_CFSSL_HOST - logstash: $HUB_LOGSTASH_HOST - rabbitmq: $RABBIT_MQ_HOST - webserver: $HUB_WEBSERVER_HOST |
| Resources/Constraints | - Default max Java heap size: N/A - Container memory: 2GB - Container CPU: 1 CPU |
| Users/Groups | This container runs as UID 0. |
| Environment File | hub-bdba.env |
