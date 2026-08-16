---
title: "Configuring SBOM Reports"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-sbom-reports.html"
content_id: "9vAZViDFnAr8vjCyIGu9GQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:20.252483+00:00"
---

# Configuring SBOM Reports

This page explains how to configure key settings for SBOM (Software Bill of Materials)
reports in Black Duck. You can set a default license for unmatched components found
during report uploads.

## Configuring the default license for unmatched components

The licence for auto-created
unmatched components found when uploading a report file on the
Scans page can be configured from the SBOM page in the System Settings.

Important: This license will exclusively apply to components where the SBOM
license value is `NOASSERTION`. It will not add the default license
to components where license has no value.

To set the default license:

1. Log in to Black Duck as a System Administrator.
2. Click [image: Admin button] and select **System Settings**.
3. Select **SBOM** from the lefthand menu.
4. Select the desired license from the **License Name** dropdown box. By
   default, the selected license is Unknown License.
