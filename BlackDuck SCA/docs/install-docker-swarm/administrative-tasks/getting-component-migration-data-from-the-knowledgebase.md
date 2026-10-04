---
title: "Getting component migration data from the KnowledgeBase"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/getting-component-migration-data-from-the-knowledgebase.html"
content_id: "eBP~nCKPiZoXkm15valmTw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.507540+00:00"
content_hash: "03a3b96310cd5b403b330dc5f9a42823e2f1e1457890f3baa29fe91aae0e5961"
---

# Getting component migration data from the KnowledgeBase

Use the migration APIs to get new or changed component IDs from the Black Duck KnowledgeBase. These APIs return the raw data and new IDs for migrated components in the KnowledgeBase.

You can use the API to submit an old component ID, for example, component ID: `bf368a1d-ef4f-422c-baca-a138737595e7` to get the new component ID from the KnowledgeBase.

The migration tracking APIs can get migration information for a specific component or component version, or get details of migrations that occurred on specific dates.

## Enabling the recording of migrations

To enable the recording of migrations, set the following property in the `blackduck-config.env file.`

RECORD_MIGRATIONS = true (Default is false)

This enables records to be written when migrations are detected.

## Retention of migration data

To set the number of days for which records are returned, configure the following property in the `blackduck-config.env` file:

`MIGRATED_OBJECT_RETENTION_DAYS = <number_of_days>` (Default is 30 days)

## API endpoints

Go to the API documentation to start using the following APIs.

For migrations that occurred after a specific date:

```
GET /api/component-migrations
```

For migrations for a specific component or component version:

```
GET /api/component-migrations/{componentOrVersionId}
```

Refer to the Black Duck API documentation at *https://<blackduck_server>/api-doc/public.html#_component_component_version_migration_endpoints* for more information.
