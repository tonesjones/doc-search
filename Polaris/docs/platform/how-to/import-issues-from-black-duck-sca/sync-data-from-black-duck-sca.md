---
title: "Sync data from Black Duck SCA"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/sync-data-from-black-duck-sca.html"
content_id: "rNBEeZcZgbPMwKB2_VasXA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:27.533121+00:00"
content_hash: "3767f837b7be0265f1c503c0a0e5616e12a2f2925ef8a1b5c6e913f910508948"
---

# Sync data from Black Duck SCA

An active connection syncs vulnerability data from Black Duck SCA to Polaris at least once a day. You can also manually sync data at the organization or project level.

Vulnerabilities are synced from Black Duck SCA to Polaris once every 24 hours. You can also manually trigger a sync, either at the organization level or for individual projects.

When a sync is triggered, Polaris retrieves a list of modified projects and versions from Black Duck SCA via the connection. External Analysis tests are then started for every mapped Polaris branch that has data available to import.

## Sync Black Duck SCA data for your organization

From the My Organization > Integrations page:

In the Black Duck SCA section, identify the connection to sync, then select Sync now from the three-dot menu.

The Last Synced column is updated when the sync task is complete. A completed sync means that Black Duck SCA data has been mapped to Polaris, and new external analysis tests have been submitted to the test scheduler to run.

## Sync Black Duck SCA data for a project

For projects already mapped to Black Duck SCA from previous syncs, you can trigger a sync from the Project Settings page.

1. Select Portfolio on the left side bar.
2. In the External Analysis section, select Sync now next to the Black Duck SCA connection you want to sync.

   Note: The External Analysis section displays a list of external analysis projects (used for importing data automatically from third-party tools). Future releases will add support for additional third-party security tools.

Data is synced to all the branches in the project.
