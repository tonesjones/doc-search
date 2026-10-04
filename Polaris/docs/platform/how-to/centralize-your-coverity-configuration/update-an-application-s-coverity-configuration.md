---
title: "Update an application's Coverity configuration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/update-an-application-s-coverity-configuration.html"
content_id: "qL1t2M2v2fTyHtujXM2s3w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.266442+00:00"
content_hash: "3a1b42e117c70cccc02a680c80396b967502015e9d7e7eeb8eec0e4901dfa821"
---

# Update an application's Coverity configuration

Upload or change an application's Coverity configuration file. Once set, an application-level configuration overrides the organization-level configuration.

1. Go to Portfolio and open an application.
2. Go to Settings.
3. Under Coverity Configuration, select Edit.
4. Select Browse... and locate the appropriate .yaml or .yml file on your machine.

   Note: Only one configuration file can be uploaded per level. If a configuration file is already uploaded, you must remove it before uploading a new one. To remove the existing file, select Clear next to the filename before saving.
5. Select Save.

Modified appears in the Coverity Configuration panel, indicating this application now uses its own configuration instead of the organization-level configuration. To revert to the organization-level configuration, select Reset. See [Reset an application or project's Coverity configuration](reset-an-application-or-project-s-coverity-configuration.md) for more information.

Note: To download a copy of the uploaded file, select the download [image: icon central config download] icon. To remove the uploaded file, select Edit, then select Clear next to the filename, and select Save.
