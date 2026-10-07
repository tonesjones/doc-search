---
title: "Update a project's Coverity configuration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/update-a-project-s-coverity-configuration.html"
content_id: "h2Z1KHcz59qQS81L3XOTHg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.285394+00:00"
content_hash: "72a9a2c0b46a73e517bd88e95dff4b8a58878bf9aefb27cf3b84a086b1363cf1"
---

# Update a project's Coverity configuration

Upload or change a project's Coverity configuration file. Once set, a project-level configuration overrides application and organization-level configurations.

1. Go to Portfolio, open an application, and open a project.
2. Go to Settings.
3. Under Coverity Configuration, select Edit.
4. Select Browse... and locate the appropriate .yaml or .yml file on your machine.

   Note: Only one configuration file can be uploaded per level. If a configuration file is already uploaded, you must remove it before uploading a new one. To remove the existing file, select Clear next to the filename before saving.
5. Select Save.

Modified appears in the Coverity Configuration panel, indicating this project now uses its own configuration. To revert to the inherited configuration, select Reset. See [Reset an application or project's Coverity configuration](reset-an-application-or-project-s-coverity-configuration.md) for more information.

Note: To download a copy of the uploaded file, select the download [image: icon central config download] icon. To remove the uploaded file, select Edit, then select Clear next to the filename, and select Save.
