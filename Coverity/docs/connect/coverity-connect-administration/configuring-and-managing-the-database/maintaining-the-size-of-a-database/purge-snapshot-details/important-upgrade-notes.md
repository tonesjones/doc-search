---
title: "Important upgrade notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/important-upgrade-notes.html"
content_id: "WZ0JQFIp4jmD1U3AH4NrLg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:17.998533+00:00"
---

# Important upgrade notes

If you have enabled this option during the upgrade process or if you have configured the
schedule after the upgrade, it is important to note that the first time that the
clean-up process runs it might take a long to complete and might result in performance
degradation due to the following:

- If your pre-6.5.1 Coverity Connect database contains a large amount of deleted
  snapshot data.

  The clean-up process that is executed by the Purge Snapshot Details feature
  performs a full search and removal (garbage-collection) of all of the old and
  superficial information that was not handled by snapshot deletion in previous
  releases. This only occurs the first time the clean-up process is
  executed.
- If your build and commit processes are scheduled at the same time as the Purge
  Snapshot Details process.

  While the snapshot purging process is running, commits might be significantly
  delayed, especially if some of the commits take a long time to run.

To decrease the time of the clean-up process and to avoid performance degradation, it is
highly recommended to reconfigure the default settings (if set) and schedule
"incremental" clean-up processes separately from your scheduled build/commit
process.

The first run should specify a date range of older snapshot data. Subsequent processes
should specify newer date ranges until the process time is manageable.

For example, assume that your pre-6.5.1 database is 1095 days (3 years) old and you do
not have any large commits scheduled to run during the weekend (Friday night through
Sunday night):

Note: The values in the following steps are examples and are not suggested values to be used
in a real deployment. If you need help to determine a work-able clean-up schedule based
on the size and age of your database, contact Coverity Support.

1. Set the Removes information from snapshots that are older than number> days to
   730 and schedule the clean-up process to run on Friday night at 23:59.

   When the process runs at the scheduled time, Coverity Connect will remove
   snapshot information that existed from (day age) 1095 through (day age)
   730.
2. After the clean-up process completes, set the Removes information from snapshots
   that are older than <number> days to 365.

   The clean-up process will, again, run at the scheduled time and will remove the
   snapshot information that existed from (current day age) 730 to (current day
   age) 365.
3. Continue this process once a week, lowering the Removes information from
   snapshots that are older than <number> days number until the setting has
   reached the level at which you want it set long-term (the recommended number of
   days is 120, which is the default).

To ensure that the entire Purge Snapshot Details process is complete, see the cim.log
file. Completion status is displayed as follows:

For the snapshot details purge process:

```
Starting snapshot details purge for {number} streams
Finished snapshot details purge for {number} snapshots in {number}ms
```

For the garbage-collection process:

```
Starting garbage collection batch                
Finished garbage collection batch
```

Note that while garbage collection is running, the above message are continually printed
(not just once). You can identify that the process ends when the "finished" message is
not followed by a new "started" message.
