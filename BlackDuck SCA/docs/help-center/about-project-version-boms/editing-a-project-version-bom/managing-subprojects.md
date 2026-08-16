---
title: "Managing subprojects"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-subprojects.html"
content_id: "Kx3PrkeSD4AMrdHRh0JyKA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:42.532305+00:00"
---

# Managing subprojects

[HUB-9934, 1452]You may have
applications that include code from other projects, for example, a user management
module that is included in several other applications. You can see risk information
about the user management module as a project with its own BOM but may also want to see
the same information in the BOM for every application that uses that module without
having to re-scan the code.

Adding projects to your application's BOM gives you a complete view of this application
and all associated risks, including vulnerabilities, license, and operational risk.

For these subprojects:

- You must have permission to the project to add it to the BOM.
- Users who do not have permission to the subproject will not be able to drill down
  to view additional data about that project version.
- Modifications made to a project outside of the BOM will propagate to the
  subproject in the BOM. For example, if additional scans are completed for scans
  mapped to this project, those changes will propagate to the subproject.

  An exception to this is the subproject version license: edits made to the project
  version license may or may not propagate to the license shown for the subproject
  in the BOM:

  - If you modify the project version license outside of the BOM and have
    *not* edited the subproject license from within the BOM, the
    edited license will appear in the BOM for the subproject.
  - If you modify the project version license outside of the BOM and have
    edited the subproject license from within the BOM, the license edit will
    *not* appear in the BOM for the subproject.

  If you modify the subproject version license from within the BOM, that change is
  *not* propagated outside of the BOM.
- Policy violations within the subproject will not appear in the BOM. However, a
  policy violation will appear in the BOM for the subproject if a policy rule is
  violated at the project level. For example, if you specified a policy rule that
  triggers a violation for unknown licenses and the project is added to the BOM
  with an unknown license, a policy violation will be triggered for that
  subproject.
- Subprojects and their associated licenses are included in the Notices File
  report. You can exclude the subproject from the Notices File report.
- Subproject security risks are added to the sum in the parent project.
- You cannot add a Project Version to itself. However, you can add a Project
  Version to another version of the same project, provided that this addition does
  not create a dependency cycle.

To add a subproject:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the version name to open the **Components** tab.  
    [image: BOM page]
3. Click **Add** and select **Project** to open the Add Project dialog
   box.
4. Enter the name and version of the project.

   Note: You must have permission to the project to add it to the BOM.
5. Optionally add a license for this project or modify the existing license. If you do not enter
   a license, "Unknown License" appears in the BOM for the license for this
   project. The license selected for the subproject will determine its license risk.
6. Click **Save**.

   Black Duck adds the selected project to the BOM.

To edit a project:

1. Select the BOM as described in the previous section.
2. Click [image: Down arrow] and select **Edit** to open the Edit Component dialog box.
3. Select one or more different values and click **Update**.

To delete a subproject from a BOM:

1. Select the BOM as described in the previous section.
2. Click [image: Down arrow] and select **Delete** to open the Delete Component dialog box.
3. Click **Delete**.

   The BOM is updated and the risk is recalculated.

To view where projects are included as subprojects:

The **Where Used** table lists the projects where this project version is included in
the BOM.

1. Locate the project using the **Projects** tab on the Dashboard by selecting
   the name of the project to go to the *Project Name* page.
2. Select the version name which opens the **Components** tab.
3. Select the **Details** tab to view where this project version is included as
   subprojects.

     
    [image: Details tab]   

   The **Where Used** table lists the project name, project version, tier,
   release date, distribution, and phase for all projects where this project
   version is a subproject.
