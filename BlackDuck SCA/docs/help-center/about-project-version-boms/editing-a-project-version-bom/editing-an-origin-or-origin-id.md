---
title: "Editing an origin or origin ID"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/editing-an-origin-or-origin-id.html"
content_id: "NS1fjEUot5avPPCLN0ED0Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:39.144903+00:00"
---

# Editing an origin or origin ID

You can select a different origin or origin ID shown for a Linux distribution and used in
a project version's BOM.

To select a different origin or origin ID:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to display the **Components** tab and view the BOM.   
    [image: BOM page]
4. In the component list view of the BOM, click [image: image] and select
   **Edit** to open the Edit component dialog box.

   [image: Edit Component dialog box]
5. If the component you selected does not have a distribution, the **Origin ID**
   lists do not appear. If necessary, select a different component and version to
   display the **Origin ID** lists.
6. Select the name of the distribution and then the version from the **Origin
   ID** lists.

   Tip: You can edit the matched component and version, license, and usage at the same time as you change the origin and origin
   ID.
7. Optionally, enter a purpose for this adjustment and/or select the
   **Modification** checkbox and enter information regarding this
   modification in the field.
8. Click **Save**.

   The origin and/or origin ID is updated. If the new values carry
   a different type of risk than the previous one, the security risk calculations
   for the OSS component and for the project version are updated.
