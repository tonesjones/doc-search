---
title: "SBOM Retention"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/sbom-retention.html"
content_id: "quAYh9JPY8p3LyG746YPbw"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:20.544244+00:00"
content_hash: "be53410d2f82bc412c7284c83a9f7fdab0bb8173501361eb54abf45d00b35609"
---

# SBOM Retention

When you generate an SBOM that is meant to be distributed, it's important that an SBOM management solution retains the SBOM so it can be reproduced if needed. This is different than other type of Black Duck reports and while it typically happens as part of the release process at a point in time when no further changes are expected to the BOM, that’s not always the case. With SBM Retention, you have more control over how long SBOMs are retained for both active and long-term support projects.

To change the data retention period for SBOM reports:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: image] .
3. Select **System Settings**.
4. Click **Data Retention**.
5. Click **SBOM Retention**.

     
    [image: image]
6. Enter a valid value for the desired project version status:

   - **Active SBOM Retention (Days)**. Enter a value ranging from 1 to 9125 days. The default period is 30 days. Changing this value will affect all active project version SBOM reports.
   - **Long-Term Support SBOM Retention (Days)**. Enter a value ranging from 1 to 9125 days. The default period is 1825 days. Changing this value will affect all long-term support (LTS) project version SBOM reports.

Note: Updating these values can take several minutes to take effect.
