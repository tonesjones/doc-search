---
title: "Excluding a component from a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/excluding-a-component-from-a-bom.html"
content_id: "hsYYAXdeaeSKxNODqgg9WA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:34.949584+00:00"
---

# Excluding a component from a BOM

A component's usage indicates how it is intended to be included in the released version
of the project.

The usage statuses are:

- Dynamically Linked
- Statically Linked
- Source Code
- Separate Work
- Implementation of Standard
- Merely Aggregated
- Prerequisite
- Dev. Tool / Excluded
- Unspecified

Click here for more information on usage.

You can change a component's usage to indicate that it is not included in the project
version's BOM because it is not actually being distributed with the released project
version. For example, if scanning identified development tools in scanned code or a
Docker image mapped to the project version, but they will not actually be included in
the released version of the project, you should change their usage to exclude them from
the project version's BOM.

Note: If you choose to exclude an automatically-added component from a project version's BOM, it
will continue to be excluded even if the code or Docker image where it was discovered is
rescanned and the BOM is updated.

Important: When you exclude a component from a project version's BOM, the license
associated with that component *is not considered* when calculating the
project version's license risk. The security and operational risks associated
with an excluded component **are still considered** when calculating the project
version's security and operational risk.

To exclude a component from a project version's BOM:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the BOM.   
    [image: BOM page]
4. In the component list view of the BOM, click [image: image] and select **Edit** to
   open the Edit Component dialog box.
5. Select **Dev. Tool / Excluded** from the **Usage** list,
6. Optionally, enter a purpose for this change and/or select the **Modification**
   checkbox and enter information regarding this modification in the field.
7. Click **Save**.

   Tip: You can change the matched component and version and license at the same time as you change the OSS component's
   usage.
