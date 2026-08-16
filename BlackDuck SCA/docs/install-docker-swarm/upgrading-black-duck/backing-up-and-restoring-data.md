---
title: "Backing up and restoring data"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/backing-up-and-restoring-data.html"
content_id: "gMcmlAklfZNWqwjThSbqNg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:17.339530+00:00"
---

# Backing up and restoring data

If the database is internal (i.e. using the postgres container as the backend database),
you could make use of the scripts under the `docker-swarm/bin` folder for
the backup and restore.

## Backing up your data

1. Start HUB as database migrate mode:

   ```
   docker stack rm hub
   docker stack deploy -c docker-compose.dbmigrate.yml hub
   ```
2. Run the following command:

   ```
   ./hub_create_data_dump.sh /pathtodbdump
   ```

   You will have the following files under `/pathtodbdump` after the
   script completes:

   - `bds_hub.dump`
   - `globals.sql`

## Restoring your data

You must first delete the existing `hub_postgres96-data-volume` before
you can restore your database. Use the following command to do so:

```
STACK=${STACK:-hub}  -- change the "hub" part to match your actual deployment
docker volume rm ${STACK}_postgres96-data-volume
```

Once you have deleted the existing volume, you can restore your database by following
these steps:

1. Start a brand new HUB as database migrate mode and then use
   `hub_db_migrate.sh` to restore the data:

   ```
   docker stack deploy -c docker-compose.dbmigrate.yml hub
   ./hub_db_migrate.sh /pathtodbdump
   ```
2. And finally, start HUB normally:

   ```
   docker stack rm hub
   docker stack deploy -c docker-compose.yml -c sizes-gen04/120sph.yaml -c docker-compose.local-overrides.yml hub
   ```

   The resource definition file used above can be changed to better fit your
   scanning patterns and usage. See the Distribution
   section for a list of all available options. Please note the [system
   requirements](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for each option as they
   increase with greater resource definitions.

If the database is external, please contact your database administrator for the data
backup.
