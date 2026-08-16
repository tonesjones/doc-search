---
title: "Upgrading from an existing Docker architecture"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/upgrading-from-an-existing-docker-architecture.html"
content_id: "9MOtzfVP2ws17fqlq4Y_MA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:16.787112+00:00"
---

# Upgrading from an existing Docker architecture

To upgrade from a previous version of Black Duck:

1. Migrate your PostgreSQL database.
2. Upgrade Black Duck.

## Migrating your PostgreSQL databases

Black Duck 2022.10.0 has migrated its PostgreSQL image from version 11 to version 13
and supports upgrading from versions using either the PostgreSQL 9.6 container
(versions 4.2 through and including 2021.10.x) or the PostgreSQL 11 container
(versions 2022.2.0 through and including 2022.7.x). During installation, the
`blackduck-postgres-upgrader` container will migrate the existing
database to PostgreSQL 13 and then exit upon completion.

Please note the following:

- Customers with non-core PG extensions are STRONGLY encouraged to uninstall them
  before migrating and reinstall them after the migration completes successfully;
  otherwise, the migration is likely to fail.
- Customers with replication set up will need to follow the instructions in the
  pg_upgrade documentation BEFORE they migrate. If the preparations described
  there are not made, the migration will likely succeed, but the replication setup
  will break.
- Customers not using the Black Duck-supplied PostgreSQL image must ensure that they are using a
  supported version. Black Duck 2022.10.0 supports PostgreSQL versions 13.x and
  14.x, and Black Duck recommends using the latest release of 14.x.
  - Community PostgreSQL users must follow PostgreSQL 14 instructions (<https://www.postgresql.org/docs/14/pgupgrade.html>)
    for PostgreSQL upgrades.
  - Users of third-party PostgreSQL, for example, RDS, must follow
    instructions from their providers.
- Users of the internal PostgreSQL container, PostgreSQL will be upgraded
  automatically if needed.
- Black Duck users on Black Duck versions prior to 4.2.0 should contact Black Duck
  Technical Support before upgrading.

Important: Before starting the migration:

- Ensure that you have an extra 10% disk space to avoid unexpected issues
  arising from disk usage due to the data copying of system catalogs.
- Review root directory space and volume mounts to avoid running out of
  disk space as this can cause Linux system disruptions.

The migration is completely automatic; no extra actions are needed beyond those for
a standard Black Duck upgrade. The `blackduck-postgres-upgrader`
container MUST run as root in order to make the layout and UID changes described
above.

On subsequent Black Duck restarts, `blackduck-postgres-upgrader` will
determine that no migration is needed and immediately exit.

## Upgrading Black Duck

To upgrade Black Duck:

1. Do one of the following:

   - If you did not use the `docker-compose.local-overrides.yml` to modify the
     `.yml` file, run one of the following commands,
     using the files located in the `docker-swarm`
     directory in the newer version of Black Duck:
     - ```
       docker stack deploy -c docker-compose.yml -c sizes-gen04/120sph.yaml hub
       ```

       (using the DB container)
     - ```
       docker stack deploy -c docker-compose.externaldb.yml -c sizes-gen04/120sph.yaml hub
       ```

       (using an external PostgreSQL instance)
   - If you are upgrading Black Duck Binary Analysis, run one of the following commands,
     using the files located in the `docker-swarm` directory
     in the newer version of Black Duck:
     - ```
       docker stack deploy -c docker-compose.yml -c sizes-gen04/120sph.yaml -c docker-compose.bdba.yml hub
       ```

       (using the DB container with Black Duck Binary Analysis)
     - ```
       docker stack deploy -c docker-compose.externaldb.yml -c sizes-gen04/120sph.yaml -c docker-compose.bdba.yml hub
       ```

       (using an external database with Black Duck Binary Analysis)
   - If you used the `docker-compose.local-overrides.yml` to modify the
     `.yml` file, run one of the following commands. Use
     the version of the version of the
     `docker-compose.local-overrides.yml` file that
     contains your modifications; for all other files, use the files located
     in the `docker-swarm` directory in the newer version of
     Black Duck:
     - ```
       docker stack deploy -c docker-compose.yml -c sizes-gen04/120sph.yaml -c docker-compose.local-overrides.yml hub
       ```

       (using the DB container)
     - ```
       docker stack deploy -c docker-compose.externaldb.yml -c sizes-gen04/120sph.yaml -c docker-compose.local-overrides.yml hub
       ```

       (using an external PostgreSQL instance)
     - ```
       docker stack deploy -c docker-compose.yml -c docker-compose.bdba.yml -c sizes-gen04/120sph.yaml -c docker-compose.local-overrides.yml hub
       ```

       (using the DB container with Black Duck Binary Analysis)
     - ```
       docker stack deploy -c docker-compose.externaldb.yml -c docker-compose.bdba.yml -c sizes-gen04/120sph.yaml -c docker-compose.local-overrides.yml hub
       ```

       (using an external database with Black Duck Binary Analysis)
   - To upgrade Black Duck with a file system as
     read-only for Swarm services, add the
     `docker-compose.readonly.yml` file to the
     previous examples.

     For example, If you used the `docker-compose.local-overrides.yml` to modify
     the `.yml` file and wish to upgrade a Black Duck
     installation that uses the DB container, run the following command:

     ```
     docker stack deploy -c docker-compose.yml -c sizes-gen04/120sph.yaml  -c docker-compose.readonly.yml -c docker-compose.local-overrides.yml hub
     ```

Note: The resource definition file used in the commands above can be changed to better fit your
scanning patterns and usage. See the Distribution section for a
list of all available options. Please note the [system
requirements](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for each option as they increase
with greater resource definitions.

Note: If you previously edited the `hub-proxy.env` file, those edits must be
copied over to the `blackduck-config.env` file.
