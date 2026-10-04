---
title: "Update your organization's Coverity configuration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/update-your-organization-s-coverity-configuration.html"
content_id: "9s6beSd1Ihsm5xHX3XTJ~g"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.248247+00:00"
content_hash: "7a2de438c74f661bb87112970b6baf8f47243fde55215a990809234e6eea1e58"
---

# Update your organization's Coverity configuration

Upload or change your organization's Coverity configuration file. The organization-level configuration applies to all applications, projects, and branches in your portfolio, but can be overridden.

Note: Only Organization Administrators can complete these steps.

1. Go to My Organization > Analysis.
2. Under Coverity Configuration, select Edit.
3. Select Browse... and locate the appropriate .yaml or .yml file on your machine.

   Note: Only one configuration file can be uploaded per level. If you've already uploaded a configuration file for your organization, you must remove it before you upload a new one. To remove the existing file, select Clear.
4. Select Save.

The configuration file is now applied to all SAST scans in your organization, unless an application, project, or branch has its own configuration assigned.

Note: To download a copy of the uploaded file, select the download [image: icon central config download] icon in the Coverity Configuration panel. To remove the uploaded file, select Edit, then select Clear next to the filename, and select Save.
