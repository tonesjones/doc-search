---
title: "Viewing a project's or project version's activity"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-a-project-s-or-project-version-s-activity.html"
content_id: "whrwa3B5f4eanCBzh7WJpQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:09.010425+00:00"
---

# Viewing a project's or project version's activity

The **Activity** tab displays the records of user actions and key events affecting
this project or project version.

Note: Activity records are available only for actions and events that occur while audit
tracking is enabled. If audit tracking is enabled after a project or project version has
already been created or modified, earlier activities are not backfilled and will not
appear in the Activity tab. This behavior applies to existing projects and project
versions.

## The events table

The Activity page contains an events table that lists activities recorded for the
project or project version.

The table includes the following information:

| Field | Description |
| --- | --- |
| **Object** | The object type and name associated with the activity, such as a project, component, vulnerability, source file, or user. |
| **Event** | The action or event that generated the activity record. |
| **Cause** | The entity that triggered the action, such as a user, policy, or scan. |
| **Date and Time** | The date and time when the event occurred. |

Select an event to expand the row and view additional details about the activity.

## Filtering the events table

Use filters to narrow the displayed activity records:

- Click**+ Filter**.
- Select one or more of the following filters:

  | Filter | Description |
  | --- | --- |
  | **Cause Names** | Filter events by the name of the user or entity that triggered the activity. |
  | **Date** | Display events that occurred within a specified date range. |
  | **Events** | Filter the table by event type. |
  | **Object Names** | Display events related to a specific object name. |
  | **Object Types** | Display events associated with a selected object type. |

After applying filters, the events table updates to display only matching activity
records.
