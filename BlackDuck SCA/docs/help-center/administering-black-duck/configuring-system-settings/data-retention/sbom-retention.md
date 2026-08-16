---
title: "SBOM Retention"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/sbom-retention.html"
content_id: "yIYlJRujSa3c17ptIxeNBQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:14.389026+00:00"
---

# SBOM Retention

When you generate an SBOM that is meant to be distributed, it's important that an SBOM
management solution retains the SBOM so it can be reproduced if needed. This is
different than other type of Black Duck reports and while it typically
happens as part of the release process at a point in time when no further changes are
expected to the BOM, that’s not always the case. With SBM Retention, you have more
control over how long SBOMs are retained for both active and long-term support
projects.

To change the data retention period for SBOM reports:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: image] .
3. Select **System Settings**.
4. Click **Data Retention**.
5. Click **SBOM Retention**.

     
    [image: image]
6. Enter a valid value for the desired project version status:

   - **Active SBOM Retention (Days)**. Enter a value ranging from 1 to 9125
     days. The default period is 30 days. Changing this value will affect all
     active project version SBOM reports.
   - **Long-Term Support SBOM Retention (Days)**. Enter a value ranging
     from 1 to 9125 days. The default period is 1825 days. Changing this
     value will affect all long-term support (LTS) project version SBOM
     reports.

Note: Updating these values can take several minutes to take effect.
