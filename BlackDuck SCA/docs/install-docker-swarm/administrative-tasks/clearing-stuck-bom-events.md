---
title: "Clearing stuck BOM events"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/clearing-stuck-bom-events.html"
content_id: "2094pTuNCD6Fd1G01IlQ7g"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:50.662191+00:00"
---

# Clearing stuck BOM events

The BOM event cleanup job clears BOM events which might be stuck because of processing
errors. By default, the job is run every day at midnight and removes stuck events prior
to last 24 hours. Users can change the cron schedule depending on their system’s quiet
hours if needed, and also, change the last how many hours to keep them for, between 1 -
48.

- Set the retention periods for last how many hours to keep BOM events. This is
  useful to purge BOM events which may have been stuck due to processing errors or
  topology changes. Default is 24 hours. Valid range is 1 - 48 hours. For example,
  if you want to remove all stuck events prior to last 12 hours.

  ```
  BLACKDUCK_BOM_EVENT_CLEANUP_BEFORE_HOURS=12
  ```
- Set the schedule via Cron expression when should job run which clears BOM events.
  It is recommended to run it around system’s quiet hours. By default it runs at
  midnight and value is 0 0 * * * ? For example, if BOM event clean up job should
  run at 2:00am every day

  ```
  BLACKDUCK_BOM_EVENT_CLEANUP_JOB_CRON_TRIGGER="0 2 * * * ?"
  ```

The `VersionBomEventClearnupJob` is enabled by default and you can't
disable this job.
