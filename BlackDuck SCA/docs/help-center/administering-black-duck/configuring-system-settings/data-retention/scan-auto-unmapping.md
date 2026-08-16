---
title: "Scan auto-unmapping"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scan-auto-unmapping.html"
content_id: "bnShU0~Ao1VDFfnTeezINA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:16.950319+00:00"
---

# Scan auto-unmapping

When enabled, inactive scans are scheduled to be unmapped from project versions where at
least one scan of the same type, updated date is older (defined by the combined value of
inactivity and grace periods) than the most recent scan of the same type. They need to
meet the project version phase and inactivity time conditions, and will only be unmapped
after the grace period.

Important: The last scan of a project version of a given type is always
protected. For example, if a project version has 2 signature scans and 1 dependency
scan, only one of the signature scans can end up being unmapped.

Warning: If this is the first time the Project Version Scan Auto-Unmapping is enabled, it may
take a while to finish processing depending on the amount of scans in your
environment.

## Enabling project version scan auto-unmapping

To enable the project version scan auto-unmapping setting:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: image] .
3. Select **System Settings**.
4. Click **Data Retention**.
5. Click **Scan Auto-Unmapping**.

   [image: Scan auto-unmapping]
6. Check the **Enable Project Version Scan Auto-Unmapping** checkbox.
7. Select all applicable project version
   phases.
8. Enter the amount of days of inactivity before scans in the project version
   phases selected above are scheduled to be unmapped. Default is 15 days.
9. Enter the amount of grace period days. Once a scan is scheduled for
   unmapping, this is the number of days before it is unmapped (as long as the
   conditions still apply). Default is 15 days.
10. Click **Save**.

## Start-up grace period

When the system starts for the first time with Scan Auto-Unmapping enabled or when
Scan Auto-Unmapping transitions from disabled to enabled on the Settings page, the
period of time entered in the **Grace Period** will act as a "start-up" grace
period. The Start-up grace period freezes all activity until it ends.

For example, when you enable Scan Auto-Unmapping and set the **Grace Period** to
15 days, the system delays doing anything with scans until 15 days have passed.

## Scan lifecycle with Scan Auto-Unmapping enabled

Scans are considered to be in an active state for a period of time determined by the
**Inactivity Period** starting from their Last Updated date.
They remain active if they are re-scanned during this time frame. When a scan has
not been re-scanned and exceeds the **Inactivity Period**, they enter the
**Grace Period** for a period of time as configured above. During the
**Grace Period**, affected scans will be indicated with a [image: Clock icon] icon and/or warning message.

- On the Project Version page, a scan targetted for unmapping will have a
  [image: Clock icon] at the end of its row. In the screenshot below, note that only the
  fourth scan has been marked for unmapping. The other scans will remain.

  [image: Scan to be unmapped]
- On the Scans page, the scan will have a [image: Clock icon] at the end of its row.

  [image: Scan in grace period]

  Mousing over this icon will display a message stating when this scan will be
  unmapped from its project version.
- On the *Name of scan* scan page, in the **Mapped to Project Version**
  section, a warning message beneath the **Unmap from Project** button is
  displayed, stating when this scan will be unmapped from its project version.

    
   [image: Details page for a scan in grace period]
- On the *Project name* page, the project version will have a [image: Clock icon] at the end of its row.

  [image: Project with versions in grace period]

  Mousing over this icon will display a message stating when this scan will be
  unmapped from its project version.
- On the **Components** tab of the *Project version* page, a banner will be
  displayed on the top of the page with a [image: Clock icon] and a message stating when this scan will be unmapped from this project
  version.

  [image: Project version in the grace period]
- On the **Settings** tab of the *Project version* page, the Scans
  section will display all scans for this project version.

  [image: Scans in grace period]

  Affected scans will have a [image: Clock icon] at the end of its row. Mousing over this icon will display a
  message stating when this scan will be unmapped from this project
  version.

Once the **Grace Period** expires, the Purge Scan Data - Unmap stale scans job will
unmap the scan.

Be aware that your code location could become unmapped even if you are conducting
regular scans. This can occur if the following conditions are met:

- The unmapping period, plus grace periods, is set to a very short amount of
  time (less than 7 days)
- No code changes are made within the system for a period of 7 or more days

We strongly recommend setting the combined unmapping period plus grace period to at
least 7 days to avoid this issue. The default setting is configured to a higher
duration to ensure better mapping continuity.

## Protecting scans by project version

You can prevent scans in designated project versions from being unmapped by **Scan
Auto-Unmapping** by following these steps:

1. Navigate to the desired project
   version.
2. Click the **Settings** tab.
3. In the Version Details pane, find the **Scan Retention** section.
4. Check the **Prevent automatic unmapping of scans** checkbox.

## Disabling auto-unmapping for SBOM import scans

You can globally disable the automatic unmapping of scan types for SBOM (Software
Bill of Materials) imports. This prevents the unintended unmapping of SBOMs when
multiple SBOMs are imported into the same project version. By excluding SBOM scan
types from the automatic unmapping functionality, you can maintain their manual
mappings, ensuring greater accuracy and control over the mapping process.

By default, Exclude SBOM Scans is enabled by default. To disable it:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: image] .
3. Select **System Settings**.
4. Click **Data Retention**.
5. Uncheck the **Exclude SBOM Scans** checkbox.
6. Click **Save**.
