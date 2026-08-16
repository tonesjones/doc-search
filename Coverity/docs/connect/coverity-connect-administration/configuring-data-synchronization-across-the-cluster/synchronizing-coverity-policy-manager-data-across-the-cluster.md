---
title: "Synchronizing Coverity Policy Manager data across the cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synchronizing-coverity-policy-manager-data-across-the-cluster.html"
content_id: "SkBLU5ljE4f6xkqno_pRUg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:42.546194+00:00"
---

# Synchronizing Coverity Policy Manager data across the cluster

All Policy Manager data is synchronized across the cluster once a day, for each
subscriber in the cluster (function counts are excluded). The coordinator aggregates the
data collected from all of its subscribers, but the subscribers do not receive any
Policy Manager data back from the coordinator. This process is detailed in the following steps:

1. The daily trend report update runs on Subscriber 1. This starts sometime
   between midnight and 1:00 am local time for the subscriber, and may take
   several hours to finish.
2. Once the update is complete on Subscriber 1, the Coordinator (which checks
   periodically for any newly available data from its subscribers) requests the
   new data, and Subscriber 1 sends it.
3. Extract Transform Load (ETL) runs on the Coordinator and picks up the new
   data from Subscriber 1. The Coordinator runs ETL periodically throughout the
   day, waiting one hour after the end of each update to start the next one. So
   if the ETL run takes 30 minutes, the Coordinator will be updated
   approximately every 90 minutes.

   Note: The Policy Manager needs to run the ETL process whether a cluster is in
   use, or not. See Scheduling the Extract Transform Load (ETL) process.

Note: Hierarchies are not synchronized between subscribers and coordinators. Instead, when
creating or editing a hierarchy on the coordinator, you can create individual nodes that
contain projects from subscriber instances of Coverity Connect. See Configuring a hierarchy for more information.
