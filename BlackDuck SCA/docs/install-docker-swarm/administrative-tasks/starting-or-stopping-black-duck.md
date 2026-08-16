---
title: "Starting or stopping Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/starting-or-stopping-black-duck.html"
content_id: "kPxEugGTB0K~wVKhitvVQA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:57.086859+00:00"
---

# Starting or stopping Black Duck

Use these commands to start up or shut down Black Duck.

## Starting up Black Duck

Use these commands if you have not used the override file to modify the default
configuration settings.

- Run the following command to start up Black Duck with the
  PostgreSQL database container:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.yml hub
  ```
- Run the following command to start up Black Duck with Black Duck Binary Analysis and using the PostgreSQL database
  container:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.yml -c docker-compose.bdba.yml  hub
  ```

- Run the following command to start up Black Duck with an
  external database:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.externaldb.yml  hub
  ```
- Run the following command to start up Black Duck with Black Duck Binary Analysis using an external database:

  ```
  docker swarm init
  docker stack deploy deploy -c docker-compose.externaldb.yml -c docker-compose.bdba.yml hub
  ```
- If you are running Black Duck with a read-only file system for Swarm
  services, add the `docker-compose.readonly.yml` file to the
  previous instructions.

  For example, to install Black Duck with the PostgreSQL
  database container, enter the follow command:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.yml -c docker-compose.readonly.yml hub
  ```

## Starting up Black Duck when using the override file

Use these commands if you have used the override file to modify the default
configuration settings.

Note: The `docker-compose.local-overrides.yml` file *must* be the last
`.yml` file used in the `docker-compose`
command.

- Run the following command to start up Black Duck with the
  PostgreSQL database container:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.yml -c docker-compose.local-overrides.yml hub
  ```
- Run the following command to start up Black Duck with Black Duck Binary Analysis and using the PostgreSQL database
  container:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.yml -c docker-compose.bdba.yml -c docker-compose.local-overrides.yml hub
  ```

- Run the following command to start up Black Duck with an
  external database:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.externaldb.yml -c docker-compose.local-overrides.yml hub
  ```
- Run the following command to start up Black Duck with Black Duck Binary Analysis using an external database:

  ```
  docker swarm init
  docker stack deploy deploy -c docker-compose.externaldb.yml -c docker-compose.bdba.yml -c docker-compose.local-overrides.yml hub
  ```
- If you are running Black Duck with a read-only file system for Swarm
  services, add the `docker-compose.readonly.yml` file to the
  previous instructions.

  For example, to install Black Duck with the PostgreSQL
  database container, enter the follow command:

  ```
  docker swarm init
  docker stack deploy -c docker-compose.yml -c docker-compose.readonly.yml -c docker-compose.local-overrides.yml hub
  ```

## Shutting down Black Duck

- Run the following command to shut down Black Duck:

  ```
  docker stack rm hub
  ```
