---
title: "Workflow for restoring databases in a cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/workflow-for-restoring-databases-in-a-cluster.html"
content_id: "EI8xFR6qAywqB7JmnX9eJA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:44.408232+00:00"
---

# Workflow for restoring databases in a cluster

**To restore the embedded PostgreSQL database for a Subscriber instance or a Coordinator
instance in a clustered deployment:**

1. On each *Subscriber* instance, put the embedded database into maintenance
   mode:

   ```
   > cov-im-ctl maintenance
   ```
2. After all Subscriber databases are in maintenance mode, put the Coordinator
   database into maintenance mode:

   ```
   > cov-im-ctl maintenance
   ```
3. On each Subscriber instance, run the following commands to restore the database
   and immediately put it back into maintenance mode:

   ```
   > cov-im-ctl maintenance
   > cov-admin-db restore <archive_file>
   > cov-im-ctl maintenance
   ```
4. On the Coordinator instance, run the following commands to restore the
   database.

   ```
   > cov-im-ctl maintenance
   > cov-admin-db restore <archive_file>
   ```
5. After running the `cov-admin-db restore` command on the
   Coordinator instance, wait until the Coordinator instance starts.
6. Start each Subscriber instance:

   Note: Wait until each instance has started before starting the next instance.

   ```
   > cov-im-ctl start
   ```
7. After all Subscriber instances have started, allow the cluster synchronization
   process to complete before carrying out new commits, triage, or other updates on
   the Subscriber instances.
