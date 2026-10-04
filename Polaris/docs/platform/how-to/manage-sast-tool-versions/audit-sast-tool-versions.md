---
title: "Audit SAST tool versions"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/audit-sast-tool-versions.html"
content_id: "GnsFpFGqIv0451xUSlnZHg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:18.668120+00:00"
content_hash: "8b082c852952eef2b32af8586f2d03758143629ef701b759fc2c718febcc7ab0"
---

# Audit SAST tool versions

Organization Administrators can audit SAST tool versions used throughout their organization. To show how SAST tool versions are used throughout your organization, follow these steps:

Note: Only Organization Administrators can complete these steps.

1. Go to My Organization > Analysis.
2. Under SAST Analysis, select Show customized versions.

   A table appears that lists applications, projects, and branches that use a specific Coverity version. If you customized the default Coverity version for your organization, it will be listed here, too.   
    [image: A screenshot of the Analysis tab, after the Show Customized Versions button is selected.]   

   Use links in the Location column to open an application, project, or branch's settings, where you can quickly reset overrides, if necessary.

   Important: If the SAST Analysis panel doesn't appear, the ability to change tool versions hasn't been enabled for your organization. See [Enable SAST tool version customization](enable-sast-tool-version-customization.md) for more information.

   Important: AI-assisted triage requires a minimum Coverity version of 2026.6.0. Attempting to use an earlier version will result in an error.
