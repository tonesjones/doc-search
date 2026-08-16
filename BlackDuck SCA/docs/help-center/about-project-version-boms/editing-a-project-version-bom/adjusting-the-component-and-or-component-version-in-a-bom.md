---
title: "Adjusting the component and/or component version in a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/adjusting-the-component-and/or-component-version-in-a-bom.html"
content_id: "dtLLXYuh~yCfwcfAwkQ2DQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:38.301020+00:00"
---

# Adjusting the component and/or component version in a BOM

Once you have mapped a component scan to a project version, the scan results
automatically create the project version's BOM. Although component scanning
automatically discovers the open source component and component version from most
archive files by comparing them to components in Black Duck KB, you may be
using a version of the component that is not available in Black Duck KB, or
you may be using a modified version of a component. You can adjust the component and
version for a component in a BOM.

- If the component/version is available in Black Duck KB, users with
  the appropriate role
  can adjust the component or component version, as described below.
- If the component version of a component is not available in Black Duck KB, users with the Component Manager role can create a custom version and add it to the
  BOM.

To select an alternate component and/or version match for a component in a BOM:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the BOM.   
    [image: BOM page]
4. In the component list view of the BOM, click [image: image] and select
   **Edit** to open the Edit component dialog box.
5. Type the name of the OSS component in the **Component** field and select the
   alternate match.
6. Select the version of the component from the **Version** list. The list
   contains all versions of the component that are available in Black Duck KB.
7. Optionally, enter a purpose for this adjustment and/or select the
   **Modification** checkbox and optionally, enter information regarding
   this modification in the field.
8. Click **Save**.

   The component and version for the BOM entry are updated. The Information
   indicator ( [image: Information icon] ) appears in the table row to indicate that the component and/or version
   were changed from the one automatically discovered in the component
   scan:

     
    [image: BOM page showing an adjustment]
