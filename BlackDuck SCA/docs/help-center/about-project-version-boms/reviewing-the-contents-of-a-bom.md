---
title: "Reviewing the contents of a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/reviewing-the-contents-of-a-bom.html"
content_id: "iNnPodhd55rUFk1ToDx5dA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:31.131854+00:00"
---

# Reviewing the contents of a BOM

[HUB-6022Any user that can edit a BOM
can review the contents and indicate that a component version or subproject is correctly
included in that BOM.

Note: Project members with no roles assigned to them cannot flag BOM contents as
reviewed.

In the component list view of the BOM, next to each component or subproject name is an
icon which indicates whether this item has been reviewed:

  
 [image: BOM components review example]   

- [image: Not reviewed icon] - Not reviewed
- [image: Reviewed icon] - Reviewed

Use this icon to flag component versions and subprojects as reviewed: the icon is a
toggle – select it to change its status.

To review multiple component versions or subprojects:

Use the bulk review feature to indicate that all component versions and/or subprojects
that appear on a *single* page are reviewed or unreviewed.

1. Optionally, filter the BOM so that the component versions and subprojects you
   wish to review/unreview appear on the page.
2. Select **Select all**.

   All components and/or subprojects on this page are selected.

   You can select individual rows so that they are not included.
3. From the **Bulk Actions** menu, select one of the following:
   - **Mark as reviewed** to indicate the component/subproject has been
     reviewed.
   - **Mark as unreviewed** to indicate the component/subproject has not been reviewed.
4. Click **Review** or **Unreview** in the confirmation dialog box.
5. Refresh the page to view your changes. It may take some time for the review
   status to appear.

   Tip: To review or unreview multiple pages, repeat steps 2-5 for each
   additional page in the BOM.

Note:

- Hover over the Reviewed icon ( [image: Reviewed icon] ) to view the username of the user who reviewed this component
  version/subproject and the date and time when it was reviewed.
- If you selected to apply edits to all versions of a project, the review status will
  persist if you rescan the same code into a new project version.
- Use the filters on the BOM page to view the BOM page by review status.
- The `components_date_time.csv` and the
  `bom_component_custom_fields_date_time.csv`
  files in the Project Version report include the review status, the username
  of reviewers, and the review date.
- Changing the review status does not cause the Information icon ( [image: Information icon] ) to appear.
- The review status cannot be changed in the Tree View of the BOM.
