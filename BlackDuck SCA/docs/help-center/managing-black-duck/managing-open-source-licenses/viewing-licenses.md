---
title: "Viewing licenses"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-licenses.html"
content_id: "TJWRSg6nmQArgBLlUP4KzA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:31.655628+00:00"
---

# Viewing licenses

The **Licenses** tab in the License Management page displays custom licenses you have
created and the licenses from Black Duck KnowledgeBase that are used in all projects in
your organization.

Users with the License Manager role can
use the License Management page to manage licenses.

Note: The License Manager role is intended to be a cross-project, enterprise role. Typically,
attorneys or privileged users that have broad access to information would have this
role. Therefore, License Managers can view the licenses for *all* projects,
including projects in which they are not project members.

From this page, you can:

- Create,
  edit, or
  delete
  custom licenses.
- Edit KnowledgeBase
  licenses.
- View the full text of
  custom and Black Duck KnowledgeBase licenses.
- View the number of
  components in your projects that use a specific license.

Note: Edits made locally by a BOM manager or Project Manager to the license text of a custom or
KnowledgeBase license will not appear on this page.

To view the License Management page:

1. Log in to Black Duck with the License Manager role.
2. Click [image: image] > **License
   Management**.

   The License Management page appears.

     
    [image: License Management page]

Select the **Licenses** tab to view a table with the following information.

Note: Newly added Black Duck KnowledgeBase licenses or modifications made to Black Duck
KnowledgeBase licenses may not be visible here for up to 30 minutes.

| Column | Description |
| --- | --- |
| **License** | License name.  Select the name to display the *License Name* page. Use the:   - **Settings** tab to view information for this license,   such as the license family and license   text. - **License Terms** tab to view the terms for this   license. - **Where Used** tab to view the component and subproject   versions where this license is used. |
| **Components** | Number of components or subprojects in all projects that have this license.  Note: The value shown here does *not* include projects assigned with this custom license.  Select the component value to display a page which lists the component versions or subprojects where this license is used. |
| **License Family** | The license family for this license.  Select a license family to view a definition and risk profile for that license family:   [image: risk profile] |
| **Last Updated** | Time, if updated today, or date that the license was last updated. |
| **User** | Username of the user who created or last updated the license.  This field is empty for licenses from Black Duck KnowledgeBase that have not been edited. |
| **Source** | Source for this license. Possible values are:   - KnowledgeBase. From Black Duck KnowledgeBase. - Modified KnowledgeBase. An edited Black Duck KnowledgeBase license. - Custom. Custom license. |
| **Status** | The review status for the license. Possible values are:   - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |

Use the filters to limit the information shown on this page. You can filter by:

- License Source: KnowledgeBase, Modified KnowledgeBase, or Custom.
- License Family: a KnowledgeBase license family or a custom license family.
- License Status.
- In Use. Only displays those licenses associated with a component version or
  subproject. This filter is selected by default.
