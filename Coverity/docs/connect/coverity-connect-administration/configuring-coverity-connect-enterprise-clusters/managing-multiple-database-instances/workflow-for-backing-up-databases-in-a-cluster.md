---
title: "Workflow for backing up databases in a cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/workflow-for-backing-up-databases-in-a-cluster.html"
content_id: "K8AV1t15Z9XVh9br3bSQgA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:43.793736+00:00"
---

# Workflow for backing up databases in a cluster

**Important notes:**

- A Coordinator database backup must be made from the same or later point in time
  than from when the Subscriber database backup is made.
- If possible, put Subscriber and Coordinator database instances into maintenance mode
  (`cov-im-ctl maintenance`) prior to using this workflow. Do
  this when the cluster is not synchronizing data and when commits are not
  running. If you can put the database instances into maintenance mode, start with
  the Subscriber databases and put the Coordinator database in maintenance mode
  last.
- If your cluster's workload does not provide a convenient time when data is not
  synchronizing and commits are not running, schedule the backups to a time with
  the least activity and make sure the Subscriber database backups complete before
  backing up the Coordinator database.

**To back up the embedded PostgreSQL database for a Subscriber instance or a Coordinator
instance in a clustered deployment:**

1. Read the important notes above.
2. Back up the database. See Backing up an embedded database
3. Regularly test the integrity of the backups by restoring them as described in
   Backing up an embedded database
