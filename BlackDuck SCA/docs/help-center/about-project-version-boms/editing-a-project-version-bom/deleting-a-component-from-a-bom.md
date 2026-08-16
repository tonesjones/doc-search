---
title: "Deleting a component from a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/deleting-a-component-from-a-bom.html"
content_id: "o3jTy0AqExrFvbEKuOnYnw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:35.723689+00:00"
---

# Deleting a component from a BOM

If you added a component manually to a project version BOM, you can delete it so that it
is no longer included in the project version information and risk calculations.

Common reasons to delete a component that was added manually include:

- The same component was discovered in a later component scan and automatically
  added to the BOM.
- The component version that you selected when you added it was not the correct
  version.
- You are no longer using component in that project version.

CAUTION:

You cannot manually delete components that were automatically added to a
project version's BOM. You can ignore an
automatically-added component in the BOM so that it is not included when
calculating the security, license, and operational risks for this version of your
project. If you want to completely remove an automatically-added component from a
project version's BOM, you must remove it from your source code or Docker image and then
rescan. This will automatically update the project version's BOM to reflect only those
component's that were automatically discovered in the mapped scans and manually-added to
the BOM.

To delete a component that was added manually:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab.   
    [image: BOM page]
4. In the List view of the BOM, click [image: image] and select **Delete** to
   open the Delete Component dialog box.
5. Click **Delete**.

   The BOM is updated and the risk is recalculated.
