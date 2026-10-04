---
title: "Alert Task Management"
source_url: "https://docs.blackduck.com/r/alert/8.4.1/black-duck-alert-user-guide/alert-task-management.html"
content_id: "5zskaR~ExvZl9wEg2QKaOQ"
version: "8.4.1"
section: "System and Task Management"
scraped_at: "2026-10-04T23:29:44.727410+00:00"
content_hash: "bf5bd7ce69caff317f724a43358f9126527895977a983dca868c6ce94d71c44d"
---

# Alert Task Management

The task management table is a read-only table that lists data about tasks that are
currently running within the Alert system.

- Access the Task Management page from the left navigation panel.
- To view task details, double click the row or click the view icon.

Figure 1. Task Management.
[image: Task Management]

The following table describes tasks that you might see on the Task Management page.

| Alert Task | Description |
| --- | --- |
| BlackDuckAccumulator | When a Black Duck SCA provider is configured, this task polls the Black Duck SCA system for notification data, and writes that data in Alert to be used for processing distribution jobs. |
| DailyTask | This daily task runs the distribution jobs to send notifications using the Daily frequency set based on the settings in the Scheduling page. |
| BlackDuckDataSyncTask | This task only pulls data from Black Duck SCA only once per day but Alert now retrieves Black Duck SCA project and user data information directly from Black Duck SCA rather than use the database tables in Alert. |
| PhoneHomeTask | Sends Alert usage data. |
| ProvidersMissingTask | Checks the list of providers and validates the configuration of each one. This task determines if a provider can be reached or not. |
| PurgeTask | Removes old data from the database based on the Scheduling page settings. |
| UpdateNotifierTask | Checks if a new version of Alert is available, and sends an email to the system administrators |

Tip: If multiple providers are configured, there will be multiple instances
of `BlackDuckAccumulator` and `BlackDuckDataSyncTask`
on the Task Management page. Each Black Duck SCA provider is associated with separate
`BlackDuckAccumulator` and `BlackDuckDataSyncTask`
tasks. To see which Black Duck SCA provider the task belongs to, click the **View**
button on the task row or double-click the relevant row.
