---
title: "Managing daily trend records at the project level"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-daily-trend-records-at-the-project-level.html"
content_id: "AgD30sdzkfx9QpdoNbxiSA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:06.438108+00:00"
---

# Managing daily trend records at the project level

The Daily Trend Records tab allows you to view and rebuild
project-wide issue trends on a daily basis. To exclude the data that belongs to a
deleted snapshot, rebuild the trend data.

By default, Coverity Connect gathers trend issue data nightly at 1 AM. However, you can
choose to rebuild the trend data at any time (see Rebuilding trend data now
for information about the data collection date).

**Trend data management options:**

- Viewing trend data:

  - Total daily trend record
  - Latest daily trend record
  - Earliest daily trend record
- Deleting and rebuilding all trend records:

  This option deletes all trend records from your system and rebuilds the trending
  data based on the most current state of the project.
- Deleting all records and rebuilding only trend records since a certain date:

  This option deletes trend records from a specified date and recomputes trending
  data based on the most current state of the project. You click the calender
  widget to select a date from which you want to recompute. Trending records that
  were computed before the specified date are preserved.
- Deleting and rebuilding the latest trend record:

  This option deletes the most recent trend record and recomputes trending data
  based on the most current state of the project. All previous trending records
  are preserved.
- Rebuilding trend records now:

  The data for the rebuilt records was collected up to 1 AM of the day on which you
  run the rebuild. For example, if you choose to rebuild trend records on October
  5 at 2:30 PM, Coverity Connect will recompute data available up to October 5 at
  1 AM.

For information about monitoring your trend data, see Monitoring issues.
