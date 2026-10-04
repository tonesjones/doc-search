---
title: "Configuring SBOM Reports"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-sbom-reports.html"
content_id: "3fa4kK3cv04SkWIh0_IVJw"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:20.784466+00:00"
content_hash: "0e5e96ef1211f12afd2934c98720ab383aa915bc996263d5057b0944e48b2a3d"
---

# Configuring SBOM Reports

This page explains how to configure key settings for SBOM (Software Bill of Materials) reports in Black Duck. You can set a default license for unmatched components found during report uploads.

## Configuring the default license for unmatched components

The licence for auto-created unmatched components found when uploading a report file on the Scans page can be configured from the SBOM page in the System Settings.

Important: This license will exclusively apply to components where the SBOM license value is `NOASSERTION`. It will not add the default license to components where license has no value.

To set the default license:

1. Log in to Black Duck as a System Administrator.
2. Click [image: Admin button] and select **System Settings**.
3. Select **SBOM** from the lefthand menu.
4. Select the desired license from the **License Name** dropdown box. By default, the selected license is Unknown License.
