---
title: "Mapping a scan to a project"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/mapping-a-scan-to-a-project.html"
content_id: "HNzm1lZjiI7LFO8WKc79dA"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:11.437123+00:00"
content_hash: "7df0edf0e7e1bdb6b5641722bb409f10c244baa5c8c1b1863ea5743471dd9034"
---

# Mapping a scan to a project

Mapping a scan adds the scan data to the BOM of a project version.

Note: You can scan a Docker image or file directory location or archive more than once, but you only have to map it to a project version once. The host and path may be changed, but as long as code location name is the same, Black Duck automatically updates the BOM of the project with any new information discovered during subsequent scans.

To map a scan to a project:

1. Log in to Black Duck SCA.
2. Click [image: image] .

     
    [image: Scans page]
3. Do one of the following:
   - Click [image: Down arrow] and select **Map to Project** in the row of the scan that you want to map.
   - Select the path of the scan you want to map to open the *Scan Name* page.

       
      [image: Scan Name Page]
4. Start typing the name of a project to progressively display matches in the **Project** field.

   If necessary, select **Create Project** to create a new project and version.
5. Select the project version to which you want to map the component scan.

   If necessary, select **Create Version** to create a new version for a project.
6. Click **Save**.

   Black Duck displays the name and version of the project to which you mapped the component scan. Select the link to open the BOM page.

   Note: Black Duck displays an aggregate project version BOM. If a component version appears more than once in an archive, it is only displayed in the BOM once.
