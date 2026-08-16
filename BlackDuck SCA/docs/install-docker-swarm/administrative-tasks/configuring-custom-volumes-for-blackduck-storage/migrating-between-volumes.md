---
title: "Migrating between volumes"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/migrating-between-volumes.html"
content_id: "sem3tNvapYLvRoly_Iurew"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:08.224524+00:00"
---

# Migrating between volumes

With multiple volumes configured, it is possible to migrate content from one or more
provider volumes to a new provider volume. This can only be done for providers that
are not the highest priority (lowest preference). To do this, configure the volumes
with one of the following migration modes. Once configured, Black Duck needs to be
restarted in order to initiate the migration which is performed by a job in the
background until it is completed.

| Migration Mode | Details |
| --- | --- |
| `none` | **Purpose**: To indicate no migration is in progress.  **Notes**: The default migration mode. |
| `drain` | **Purpose**: This mode moves content from the configured provider to the highest priority (lowest preference number) provider. Once content is moved, it is immediately removed from the source provider.  **Notes**: This is a straight move operation - adding it to the target provider and removing it from the source. |
| `delete` | **Purpose**: This mode copies content from the configured provider to the highest priority (lowest preference number) provider. Once content is copied, it is marked for deletion in the source provider. The standard deletion retention periods apply - after that period the content is removed.  **Notes**: This is a move that allows for the ability for the system to be recovered from backup within the retention window so that content in the source provider remains viable. The default retention period is 6 hours. |
| `duplicate` | **Purpose**: This mode copies content from the configured provider to the highest priority (lowest preference number) provider. Once content is copied, the source is left unaltered, including the metadata.  **Notes**: After the duplicate migration, you will have two volumes with all of the content and the metadata in the database. If you take the next step in the “duplicate and dump” process and unconfigure the original volume, the files will be deleted but the metadata will remain in the database - referencing an unknown volume generating a warning in the pruner jobs (a job error). To resolve the error, use the following property to enable the pruning of the orphaned metadata records:  ``` storage.pruner.orphaned.data.pruning.enable=true ``` |
