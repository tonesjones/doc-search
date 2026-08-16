---
title: "Scheduling Notifications"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/scheduling-notifications.html"
content_id: "MtVWoI~YbUoHcVTkZu9O2w"
version: "8.4.0"
section: "Post Installation Configuration"
scraped_at: "2026-08-08T23:46:36.999422+00:00"
---

# Scheduling Notifications

Navigate to the **Scheduling** configuration page to schedule the delivery of
notifications.

Figure 1. Notification Scheduling.
[image: Notification Scheduling]

The following settings in **Scheduling** apply to all jobs created under
Configuration.

| Field | Description |
| --- | --- |
| Daily Digest Hour Of Day | Use the drop-down tool to select the hour of the day to run the daily digest distribution jobs. |
| Daily Digest Cron Next Run | Displays the date/time of the next daily digest run in UTC (Coordinated Universal Time) time. |
| Purge Notification Data | Use the drop-down tool to select the frequency for cleaning up Black Duck data; the default value is three days. When the purge runs, it deletes all data that is older than the selected value. |
| Purge Notification Data Cron Next Run | Displays the date/time of the next purge of provider data in UTC time. |
| Purge Audit Failed Data | Use the drop-down tool to select the frequency for cleaning up failed audit data; the default value is three days. When the purge runs, it deletes all data that is older than the selected value. |
| Purge Audit Failed Data Cron Next Run | Displays the date/time of the next purge of data in UTC time. |

When you are done, click **Save** to retain your scheduling preferences.
