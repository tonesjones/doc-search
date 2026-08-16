---
title: "Removing a scan from a project"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/removing-a-scan-from-a-project.html"
content_id: "Kzm4W3pSeFJrd_WK13DVbw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:54.963309+00:00"
---

# Removing a scan from a project

Removing the mapping of a scan removes the scan data from the BOM.

To remove a mapping:

1. Log in to Black Duck SCA.
2. Do one of the following:

   - Click [image: image] .

       
      [image: Scans page]
   - From the **Settings** tab for a project version, select
     **Scans**.

       
      [image: Project Version Scans tab]
3. Click [image: Down arrow] and select **Unmap from Project** in the row of the scan that you
   want to remove the mapping.
4. Click **Remove** to confirm.

## Un-mapping and re-mapping scan files

Please be aware that remapping scan files to a project does not initiate the matching process.
After you remap the files, the BOM computation will continue to utilize the
Knowledge Base (KB) IDs that were identified during the initial matching phase. This
means that any changes made during the remapping will not affect the existing
mappings or the resulting BOM until the matching process is run again.
