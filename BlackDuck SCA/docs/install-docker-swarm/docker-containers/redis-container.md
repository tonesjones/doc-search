---
title: "Redis container"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/redis-container.html"
content_id: "mzL0O51DehzCT5thykHHmA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:24.394150+00:00"
---

# Redis container

| Container Name: blackduck-redis | |
| --- | --- |
| Image Name | redis:7.0.9-alpine3.17 |
| Description | This container enables more consistent caching functionality in Black Duck and is used to improve application performance.  Redis is enabled by default as a primary cache mechanism. |
| Configuration | To configure Redis, use the following settings:   - blackduck-config.env environment file to configure redis   settings   - Redis settings:     - BLACKDUCK_REDIS_MODE:  Redis mode can       be standalone or sentinel     - BLACKDUCK_REDIS_TLS_ENABLED:  Whether       to enforce TLS/SSL connections between Redis       client and server. - Use docker-compose.yml for Redis standalone mode which   requires 1,024 MB additional memory - Use both docker-compose.yml and   docker-compose.redis.sentinel.yml for redis sentinel   mode which provides high availability but also requires   3,168 MB additional memory. - Redis container integrates with logstash and filebeat   like other services. - Redis container has a health status check. - In Black Duck Hub system info page,   there is a redis-cache tab where Redis debug info is   shown. |
| Scalability | The container should not be scaled. |
| Links/Ports | The Redis container needs to connect to these containers/services:   - logstash - cfssl |
| Alternate Host Name Environment Variables | N/A |
| Resources/Constraints | - Default max Java heap size: N/A - Container memory:   - Standalone 1024 MB   - Sentinel mode 3168 MB - Container CPU: 1 |
| Users/Groups | Can run as any user/group, for example. {"runAsUser": 4567, "runAsGroup": 4567} |
| Environment File | `blackduck-config.env` |
