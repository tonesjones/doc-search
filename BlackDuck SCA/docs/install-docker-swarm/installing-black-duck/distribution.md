---
title: "Distribution"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/distribution.html"
content_id: "Uc7BRr_vWKZZ9NosYhXtow"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:36.867440+00:00"
---

# Distribution

The `docker-swarm` directory consists of following files you need to
install or upgrade Black Duck.

- `blackduck-config.env`: Environment file to configure Black Duck settings.
- `docker-compose.bdba.yml`: Docker Compose file used when
  installing Black Duck with Black Duck - Binary Analysis and using the database
  container provided by Black Duck.
- `docker-compose.dbmigrate.yml`: Docker Compose file used to
  migrate the PostgreSQL database when using the database container provided by
  Black Duck.
- `docker-compose.externaldb.yml`: Docker Compose file used with an
  external PostgreSQL database.
- `docker-compose.local-overrides.yml`: Docker Compose file used to
  override any default settings in the `.yml` file.
- `docker-compose.readonly.yml`: Docker Compose file that declares
  the file system as read-only for Swarm services.
- `docker-compose.yml`: Docker Compose file when using the database
  container provided by Black Duck.
- `docker-compose.integration.yaml`: Used to enable SCM integration. No further
  configuration is required. The following environment variable will be
  automatically added:

  ```
    webserver:
      environment: {ENABLE_INTEGRATION_SERVICE: "true"}
  ```
- `external-postgres-init.pgsql`: PostgresSQL.sql file used to
  configure an external PostgreSQL database.
- `hub-bdba.env`: Environment file that contains additional settings
  for Black Duck Binary Analysis. This file should not require any
  modification.
- `hub-postgres.env`: Environment file to configure an external PostgreSQL database.
- `hub-webserver.env`: Environment file to configure web server settings.

In the `bin` directory:

- `bd_get_source_upload_master_key.sh`: Script used to back up the
  master and seal key when uploading source
  files.
- `hub_create_data_dump.sh`: Script used to back up the PostgreSQL
  database when using the database container provided by Black Duck.
- `hub_db_migrate.sh`: Script used to migrate the PostgreSQL
  database when using the database container provided by Black Duck.
- `hub_reportdb_changepassword.sh`: Script used to set and change the report database password.
- `recover_master_key.sh`: Script to create a new seal key used for
  uploading source files.
- `system_check.sh`: Script used to gather your Black Duck system information to send
  to Customer Support.

In the sizes-gen02 directory:

- `resources.yaml`: These are resource definition files for Enhanced
  scanning.

In the sizes-gen03 directory:

- `10sph.yaml`, `120sph.yaml`,
  `250sph.yaml`, `500sph.yaml`,
  `1000sph.yaml`, `1500sph.yaml`,
  `2000sph.yaml:` These are the resource definition files for
  the various scans per hour sizes. See the Hardware
  Requirements section for more information.

In the sizes-gen04 directory:

- `10sph.yaml`, `120sph.yaml`, `250sph.yaml`,
  `500sph.yaml`, `1000sph.yaml`,
  `1500sph.yaml`, `2000sph.yaml:` These are the
  resource definition files for the various scans per hour sizes introduced in
  Black Duck 2024.1.0. See the Hardware
  Requirements section for more information.
