---
title: "Retain Unmatched File Data"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/retain-unmatched-file-data.html"
content_id: "3W1VKHzIrb~gQl8na7LsEQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:15.211134+00:00"
---

# Retain Unmatched File Data

## Changing the Retain Unmatched File Data setting globally

You can change whether or not your system retains unmatched files. By default, this
setting is not enabled.

To enable the retain unmatched files data setting:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: image] .
3. Select **System Settings**.
4. Click **Data Retention**.
5. Click **Unmatched File Data Retention**.

   [image: image]
6. Check the **Retain Unmatched File Data** checkbox.

If enabled, unmatched file data for scans will always be retained. When disabled
(default), unmatched file data will be purged. Note that the global setting only applies
to projects and scans that do not explicitly specify their own setting; similarly,
changing the global setting does not affect projects or scans that do specify their own
setting.

Warning: Once unmatched files are purged, they cannot be recovered except by restoring from backup.

You can also manually purge unmatched data immediately by clicking either of the
following buttons:

**Purge ONLY Archived Project Version Unmatched File Data**: Clicking this button
will purge all unmatched data currently in the Archived project version
phase only.

**Purge ALL Unmatched File Data**: Clicking this button will purge all purge all
unmatched data regardless of its project version phase.

As indicated above, clicking either button only applies to projects and scans that do
not explicitly specify their own setting.

## Changing the Retain Unmatched File Data setting for a project

You can set a project's setting to have its own policy of whether or not the
unmatched file data is purged by following these steps:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the **Settings** tab.
3. Scroll to the **Retain Unmatched File Data** section.

     
    [image: Retain Unmatched File Data section of the Project page Settings tab]
4. Select an option from the dropdown menu:

   **Retain Unmatched File Data**: Selecting this option will prevent
   this project's data from being purged regardless of the global system
   default setting. This also disables the buttons granting the ability to
   manually purge unmatched file data.

   **Don't Retain Unmatched File Data**: Selecting this option will allow
   this project's unmatched file data to be purged. This also enables the
   buttons granting the ability to manually purge unmatched file data.

   **System Default**: Selecting this option will use the global system
   default setting as set above. The buttons granting the ability to
   manually purge unmatched file data will either be enabled or disabled
   depending on how the system setting is configured.
5. Click **Save**.

You can also manually purge unmatched data immediately for this project like from the
Retain Unmatched File Data administration page.
