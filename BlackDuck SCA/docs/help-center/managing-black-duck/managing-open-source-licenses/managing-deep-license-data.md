---
title: "Managing deep license data"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-deep-license-data.html"
content_id: "lzBR6jPB6Xwtj1Up9Ay4ew"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:38.054618+00:00"
---

# Managing deep license data

Black Duck displays declared licenses for the components in
your BOM. However, deep licenses (also known as sub-licenses or embedded licenses) may
also exist in your open source components. Managing this deep license data reduces the
risk of license infringement and makes it easier to understand and report on deep
licenses and their risks in the open source being used.

Deep license data is not enabled by default; you must enable including deep license data
to your BOM components. Once enabled, any deep licenses, as determined by Black Duck KnowledgeBase, are automatically active.

Note: Depending upon the number of components and number of deep licenses, enabling the viewing of
deep license data can impact the BOM calculation scan time. Adding deep license data to
your BOM can affect your license risk and can trigger policy violations.

To manage your deep license data:

1. Enable deep level license data. As this feature is enabled at the project level,
   deep license data will be enabled and active for all project versions.

   In your project version BOM, the deep license data icon ( [image: Deep License icon] ) identifies the components with deep level licenses.
2. View the deep license data. You can:
   - Review the evidence as determined by Black Duck KnowledgeBase.

     Evidence consists of the list of files and file content which
     you can view to confirm the inclusion of deep license data.
   - Activate or deactivate the license. By default, deep license data is
     activated for all origins. If there are multiple origins, deep license
     data is activated for all origins.
   - Add licenses.
   - Read the license text.

## Enabling or disabling deep license data

Enabling this checkbox will apply deep license data to your non-snippet components matches and
allow visibility to embedded licenses which may exist in your components beyond
declared licenses. Deep license data is enabled at the project level.

Please note, this can affect the license risk and policy violation for components. It
can also impact the Bill of Materials calculation time depending upon the number of
components and amount of deep licenses.

To enable deep license data:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the **Settings** tab.
3. Click the **Project Details** tab.
4. Check the **Apply Deep License Data to Bill of Materials** checkbox or clear the checkbox
   to disable this feature.

     
    [image: Apply Deep License Data to Bill of Materials]
5. Click **Save**.

## Enabling or disabling deep license data to snippet component matches

If enabled, component snippet matches are included in the deep license data calculation.

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the **Settings** tab.
3. Click the **Project Details** tab.
4. Check the **Apply Deep License Data to Snippet Component Matches** checkbox or clear the
   checkbox to disable this feature.

   [image: Apply Deep License Data to Snippet Component Matches]
5. Click **Save**.

## Reviewing deep license data

1. Open the project version BOM to view the components which have deep license
   data.

     
    [image: BOM with Deep License Data icons]
2. Components with [image: Deep License icon] have deep license data. Click [image: Deep License icon] to open the *Component Name Version* Deep License page.

     
    [image: Deep License Page]   

   This page displays the following information:

   | Column | Description |
   | --- | --- |
   | **License** | License name.  Select the name to display the *License Name* page which displays the license text.  Click > to view the origins for this license. |
   | **Active** | Indicates whether this license is active.  Active licenses are included in the calculation of license risk and policy violations. |
   | **License Family** | The license family for this license. |
   | **Last Updated** | Date and user who last updated the information on this page. |
   | **Status** | The review status for the license. Possible values are:  - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |
3. From this page:
   - View the evidence for the inclusion of this deep license.

     The
     Black Duck KnowledgeBase determines deep license data at the origin
     level. Therefore, click > to display the origins for this
     license.

     Select an origin to open the Reference Files dialog
     box which displays the files and corresponding evidence for
     inclusion of this license.

       
      [image: Reference Files Page]   

     The **Files** section lists the files found containing
     deep license data. Select a file to view the contents of that file.
     Deep license data is highlighted.

       
      [image: Deep License Data]   

     If the file cannot be determined, the file name and path
     display "Unknown."
   - Activate or deactivate the deep license. By default, all deep
     licenses are active.

     You can activate or deactivate a deep
     license by:

     - Selecting a license in the *Component Name Version* Deep
       License page and clicking **Activate** or
       **Deactivate**.
     - Selecting or clearing the **Active** option located in the
       upper right-corner of the Reference Files dialog
       box.
   - Add a license or remove a manually added license.

     - To add a license, click **Add License**, select the
       license, and click [image: OK icon] . The new license appears in the table.
     - To remove a license, click [image: Delete icon] in the row of the manually added license you want to
       delete and select **Remove** in the confirmation dialog
       box.
   - View license text:
     - View the declared license text and obligation information.
       Select the license name in the header to open the
       *Component Name Version* Component License dialog
       box.

         
        [image: Component Name Version Component License dialog box]   

       Note that you can modify the declared license.
     - View deep license text by selecting the license name from the
       table.

         
        [image: License text]
