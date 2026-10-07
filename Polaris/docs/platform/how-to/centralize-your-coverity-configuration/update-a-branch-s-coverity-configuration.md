---
title: "Update a branch's Coverity configuration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/update-a-branch-s-coverity-configuration.html"
content_id: "d9Q7KsoE4pPn90zEic1e_g"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.300374+00:00"
content_hash: "c151431c54cc585e3392d987ca1fc6957bb74bc6bf35d3894f8924e959693bec"
---

# Update a branch's Coverity configuration

Upload or change a branch's Coverity configuration file. Once set, a branch-level configuration overrides project, application, and organization-level configurations.

1. Go to Portfolio, open an application, and open a project.
2. Go to Branches.
3. Select the branch you want to configure.
4. Under Coverity Configuration, select Browse... and locate the appropriate .yaml or .yml file on your machine.

   Note: Only one configuration file can be uploaded per level. If a configuration file is already uploaded, you must remove it before uploading a new one. To remove the existing file, select Clear next to the filename before saving.
5. Select Save.

Modified appears in the Coverity Configuration panel, indicating this branch now uses its own configuration. To revert to the inherited configuration, select Reset. See [Reset a branch's Coverity configuration](reset-a-branch-s-coverity-configuration.md) for more information.
