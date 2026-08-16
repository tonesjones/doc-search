---
title: "Docker containers"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/docker-containers.html"
content_id: "5b8vV2jNaAS6ttM_lGh4~Q"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:18.161245+00:00"
---

# Docker containers

These are the containers within the Docker network that comprise the Black Duck application:

## Application services

- Authentication
- Binary Analysis - Required if Black Duck Binary Analysis is enabled.
- BOM Engine
- DB - This container is not included in the
  Black Duck application if you use an external PostgreSQL
  instance.
- Documentation
- Integration
- Jobrunner
- Registration
- Scanmatch
- Storage
- Web application
- Web server

## Infrastructure services

- CFSSL
- Logstash
- Rabbitmq
- Redis

The following diagram shows the basic relationships among the containers and which ports
are exposed outside of the Docker network.

  
 [image: Black Duck Architecture]   

This diagram makes no assumptions about which
Docker hosts are running which container: it is possible that each container runs on a
separate Docker host. All containers are contained within a Docker network. The only two
ports exposed outside of the Docker network are the HTTPS port for Black Duck (via NGiNX) and a read-only database port from Postgres for
reporting. All other external communication will go through a proxy or another NGiNX
instance. All other communication will be among the containers within the Docker
network.

The Zookeeper container was removed in Black Duck version 2020.4.0. You can
manually remove the following zookeeper volumes because they are no longer used:

- zookeeper-data-volume
- zookeeper-datalog-volume

The following tables provide more information on each container.
