---
title: "Removing components from a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/removing-components-from-a-bom.html"
content_id: "R0gJKjcvK1_R87AH751jNg"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:12.882632+00:00"
content_hash: "55125ec30aca3937c7fc75b7b13c2b93d1164f816bd1f549bc6f99e0d5c3c7f5"
---

# Removing components from a BOM

The best way to remove components that were automatically added to a component version BOM is to remove the link between the component version and the scan that discovered those components.

Note: If you manually remove automatically-added components from a project version BOM, those components will be automatically added to the project version BOM again if the code or Docker image is rescanned.

To remove a scan from a project version to update the BOM:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects** dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the BOM.   
    [image: BOM page]
4. Select the **Settings** tab and then select **Scans**.

   Select the name of the scan to display the *Scan Name* page which provides information such as the projects and versions mapped to this scan.

     
    [image: Scan Name page]
5. Click [image: image] in the row of the scan you want to remove the link (unmap) and then select **Unmap from Project**.

   Black Duck removes the mapping between the scan and the project version. This removes all OSS components discovered in that scan from the BOM.
