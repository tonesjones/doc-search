---
title: "Removing components from a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/removing-components-from-a-bom.html"
content_id: "xWJWD_jzOLWVuqskSryEdw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:36.577199+00:00"
---

# Removing components from a BOM

The best way to remove components that were automatically added to a component version
BOM is to remove the link between the component version and the scan that discovered
those components.

Note: If you manually remove automatically-added components from a project version BOM, those
components will be automatically added to the project version BOM again if the code or
Docker image is rescanned.

To remove a scan from a project version to update the BOM:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the BOM.   
    [image: BOM page]
4. Select the **Settings** tab and then select **Scans**.

   Select the name of the scan to display the *Scan Name* page which provides
   information such as the projects and versions mapped to this scan.

     
    [image: Scan Name page]
5. Click [image: image] in the row of the scan
   you want to remove the link (unmap) and then select **Unmap from Project**.

   Black Duck removes the mapping between the
   scan and the project version. This removes all OSS components discovered in that
   scan from the BOM.
