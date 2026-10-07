---
title: "Configuring the nightly IMT prefill job"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configuring-the-nightly-imt-prefill-job.html"
content_id: "zpl8HH7KEmPnrx3w8Kj2tA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:07.449937+00:00"
---

# Configuring the nightly IMT prefill job

Enable and optionally adjust the schedule for the nightly background job that refreshes
stale or missing IMT data for all streams.

- You must have administrator access to the Coverity Connect server.
- You must be able to restart the Connect server process.
- IMT must be enabled (`issue-view.imt.enabled=true`).

The nightly prefill job catches up streams whose materialized data is missing or out of
date. This includes streams where a commit-refresh failed, streams not yet materialized after
an upgrade, and streams that became stale while IMT was temporarily disabled. Enabling this
job is recommended for production deployments.

1. Open the cim.properties file on the Connect server in a text
   editor.
2. Set `issue-view.imt.nightly-prefill.enabled=true` to enable the nightly
   prefill job.
3. **Optional:** 
   To change the schedule from the default of 2:00 AM local time, set the
   `issue-view.imt.nightly-prefill.cron` property to a Quartz 6-field cron
   expression.

   To run the nightly prefill at 3:30 AM:

   ```
   issue-view.imt.nightly-prefill.cron=0 30 3 * * ?
   ```
4. Save and close the file.
5. Restart the Coverity Connect server for the changes to take effect.

The nightly prefill job runs at the configured schedule and refreshes all streams whose
materialized data is missing or out of date.
