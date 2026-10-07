---
title: "Changing the data retention period for unmapped scans"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-the-data-retention-period-for-unmapped-scans.html"
content_id: "DeAvvFb6FBe~gym9NBhSIw"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:20.514218+00:00"
content_hash: "f3bcd8890893174cf3b8b8cc45c7970a49227f650de64595b50e4ceabce777e0"
---

# Changing the data retention period for unmapped scans

You can change the period of time unmapped scans are retained. By default, the time frame is set to 30 days and can be set to as low as 1 day and to as high as 730 days.

To change the data retention period for unmapped scans:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: image] .
3. Select **System Settings**.
4. Click **Data Retention**.
5. Click **Unmatched Scans Retention**.

  
 [image: image]   

Note: Changing this setting will take effect the next time ScanPurgeJob runs, which occurs every 15 minutes.

## Protecting scans by project version

You can prevent scans in designated project versions from being unmapped by **Scan Auto-Unmapping** by following these steps:

1. Navigate to the desired project version.
2. Click the **Settings** tab.
3. In the Version Details pane, find the **Scan Retention** section.
4. Check the **Prevent automatic unmapping of scans** checkbox.
