---
title: "Installing Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/installing-black-duck.html"
content_id: "RrmTSadvQa9gFjT9844fTQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:37.435618+00:00"
---

# Installing Black Duck

Prior to installing Black Duck, determine if there are any settings that need
to be configured. See the Administrative tasks section for additional assistance with
system configuration.

Note: These instructions are for new installations of Black Duck. Refer to
Chapter 6 for more information about upgrading Black Duck.

In the following instructions to install Black Duck, you may need to be
a user in the docker group, a root user, or have `sudo` access. See the
next section to install Black Duck as a non-root user.

## Installing Black Duck with the PostgreSQL database container

1. ```
   docker swarm init
   ```

   The `docker swarm init` command creates a single-node
   swarm.
2. ```
   docker stack deploy -c docker-compose.yml -c sizes-gen05/120sph.yaml -c docker-compose.local-overrides.yml hub
   ```

   With Black Duck 2022.4.0 and later, you no longer allocate container
   resources directly in `docker-compose.yml`. Instead,
   resources are specified in a separate overrides file. The resource
   allocations used before Black Duck 2022.4.0 are
   found in `sizes-gen02/resources.yaml`. For Black Duck 2024.1.0 and later, multiple possible
   allocations are provided in the `sizes-gen05` folder.
   There are 7
   allocations based on load as measured in average scans per
   hour; if your anticipated load does not match one of the predefined
   allocations, round up.

   In the
   example above:

   - `docker-compose.yml`: Stock deployment, this file is
     not to be edited.
   - `sizes-gen05/120.yaml`: The resource definition file. In this example,
     `sizes-gen05/120.yaml` is used as the desired
     resource definition, but this can be changed to better fit your
     scanning patterns and usage. See the Distribution section for a list of all available options. Please note the
     [system
     requirements](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for each option as they increase
     with greater resource definitions.
   - `docker-compose.local-overrides.yml`: This is an
     optional file if your installation has custom configurations like
     secrets, memory limits, etc.

## Installing Black Duck with Black Duck Binary Analysis using the PostgreSQL database container

1. ```
   docker swarm init
   ```

   The `docker swarm init` command creates a single-node
   swarm.
2. ```
   docker stack deploy -c docker-compose.yml -c sizes-gen05/120sph.yaml -c docker-compose.bdba.yml hub
   ```

   The resource definition file used above can be changed to better fit your scanning patterns
   and usage. See the Distribution section for a list
   of all available options. Please note the [system
   requirements](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for each option as they
   increase with greater resource definitions.

## Installing Black Duck with an external PostgreSQL instance

1. ```
   docker swarm init
   ```

   The `docker swarm init` command creates a single-node
   swarm.
2. ```
   docker stack deploy -c docker-compose.externaldb.yml -c sizes-gen05/120sph.yaml hub
   ```

   The resource definition file used above can be changed to better fit your scanning patterns
   and usage. See the Distribution section for a list
   of all available options. Please note the [system
   requirements](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for each option as they
   increase with greater resource definitions.

## Installing Black Duck with Black Duck Binary Analysis using an external PostgreSQL instance

1. ```
   docker swarm init
   ```

   The `docker swarm init` command creates a single-node
   swarm.
2. ```
   docker stack deploy -c docker-compose.externaldb.yml -c sizes-gen05/120sph.yaml -c docker-compose.bdba.yml hub
   ```

   The resource definition file used above can be changed to better fit your scanning patterns
   and usage. See the Distribution section for a list
   of all available options. Please note the [system
   requirements](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for each option as they
   increase with greater resource definitions.

   Note: When using the new guidance files (for deployment sizing) with
   external database, remove postgres and postgres-upgrader services from
   the tshirt size file to be used before deploying.

## Installing Black Duck with a file system as read-only

1. ```
   docker swarm init
   ```

   The `docker swarm init` command creates a single-node
   swarm.
2. ```
   docker stack deploy -c docker-compose.yml -c sizes-gen05/120sph.yaml -c docker-compose.readonly.yml hub
   ```

   The resource definition file used above can be changed to better fit your scanning patterns
   and usage. See the Distribution section for a list
   of all available options. Please note the [system
   requirements](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for each option as they
   increase with greater resource definitions.

   To install Black Duck with a file system as read-only
   for Swarm services, add the `docker-compose.readonly.yml`
   file to the previous instructions.

Note: There are some versions of Docker where if the images live in a private repository, docker
stack will not pull them unless the following flag is added to the above commands:
`--with-registry-auth`.

## Verifying the installation

You can confirm that the installation was successful by running the `docker
ps` command to view the status of each container. A "healthy" status
indicates that the installation was successful. Note that the containers may be in a
"starting" state for a few minutes post-installation.

Once all of the containers for Black Duck are up, the web application
for Black Duck will be exposed on port 443 to the docker host. Be sure
that you have configured the hostname and
then you can access Black Duck by entering the following:

https://hub.example.com

The first time you access Black Duck, the Registration & End User
License Agreement appears. You must accept the terms and conditions to use Black Duck.

Enter the registration key provided to you to access Black Duck.

Note: If you need to reregister, you must accept the terms and conditions of the End User License
Agreement again.
