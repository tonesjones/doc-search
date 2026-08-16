---
title: "New Vulnerabilities"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-vulnerabilities.html"
content_id: "IYRAKWNawbddz_bj7jZetQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:18.077682+00:00"
---

# New Vulnerabilities

Black Duck SCA aggregates vulnerability data daily to power the
New Vulnerabilities
dashboard. The **New Vulnerabilities** data retention setting lets
administrators control how many days of this aggregated data the system keeps. Data
older than the configured retention period is automatically purged.

Note: This setting controls only the aggregated dashboard reporting data. It does not delete
vulnerability records from your projects or versions.

## What this setting controls

The New Vulnerabilities data retention period determines:

- How many days of pre-aggregated vulnerability data are stored in the
  system.
- How far back users can select dates in the **New Vulnerabilities**
  dashboard date range filter.
- When automatic purging removes older aggregated records.

For example, if retention is set to 30 days, the dashboard date range filter will
only allow users to view data from the last 30 days. Any aggregated data older than
30 days is removed during the next scheduled purge.

## Before you begin

- You must have **System Administrator** permissions to change data
  retention settings.

## Configure New Vulnerabilities retention

1. Click **Admin** → **System Settings**
2. Click **Data Retention**.
3. Click **New Vulnerabilities**.
4. Enter a value from 7 to 30 representing the data retention period in days
   for new vulnerability data. The default period is 10 days.
5. Click **Save**.

Changes take effect at the next scheduled purge cycle. Data older than the new
retention period will be removed automatically.

## How this affects dashboard users

The retention period directly controls the New Vulnerabilities dashboard
experience:

- **Shorter retention** (e.g., 7 days) — Reduces storage usage but limits
  how far back users can analyze vulnerability trends.
- **Longer retention** (e.g., 30 days) — Provides a wider historical view on
  the dashboard but uses more storage.

If a user tries to select a date range that extends beyond the retention window, no
data will be available for those dates.

## Best practices

- **Start with the default value** (10 days) and adjust based on your
  organization's reporting needs and storage capacity.
- **Review periodically** — If your instance has a large number of
  projects and versions, a shorter retention period can help manage
  database size.
- **Coordinate with dashboard users** — Before reducing the retention
  period, inform users who rely on the New Vulnerabilities dashboard for
  trend analysis, as they will lose visibility into older data.

## Frequently asked questions

1. **Does changing this setting delete vulnerabilities from my
   projects?**

   No. This setting only affects the pre-aggregated data used by the New
   Vulnerabilities dashboard. Vulnerability records associated with your
   projects and versions are not affected.
2. **Why can't dashboard users select dates older than a certain point?**

   The date range filter on the New Vulnerabilities dashboard is limited by the
   retention period. If retention is set to 14 days, users can only view data
   from the last 14 days. If you previously had a longer retention period and
   reduced it, older data has been purged and is no longer available.
3. **Who should change this setting?**

   Only System Administrators should modify data retention settings. Changes
   affect all users who rely on the New Vulnerabilities dashboard.
