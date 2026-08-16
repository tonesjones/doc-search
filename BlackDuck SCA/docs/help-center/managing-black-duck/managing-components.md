---
title: "Managing Components"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-components.html"
content_id: "8W0uOm9RoovbsDMtxQLMjQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:11.871323+00:00"
---

# Managing Components

Users with the **Component Manager**
role
can use the **Components** page to create and manage custom components,
component versions, Black Duck
KnowledgeBase components, and unmatched origins.

## Open the Components page

1. Click [image: Manage]
   **> Components**.

The **Components** page provides access to:

- The **Components** tab, which lists available components.
- The **Component Versions** tab, which lists component versions.
- Filtering and search tools.
- Actions for creating custom
  components and KnowledgeBase components.
- The **Unmatched Origins**
  page.

## Components tab

The **Components** tab displays a list of managed components.

Select a component name to open the component details page.

If a component contains multiple versions, expand the component to view its versions.
Select a version to open the component version details page.

The table includes the following information:

| Column | Description |
| --- | --- |
| **Component** | Name of the component.  Select the component name to open the **Overview** tab of the *Component Name* page.  If there are multiple versions for this component, select > to display the versions.  Select a version to open the **Overview** tab of the *Component Name > Version* page.  [image: Note icon] indicates that there is a note for this component or component version. Hover over the icon to view the information. |
| **License** | License for this component. |
| **Source** | Source for this component. Possible values are:   - Custom. A custom component. - KnowledgeBase. An unmodified Black Duck   KnowledgeBase component. - Modified KnowledgeBase. A modified Black Duck KnowledgeBase   component. |
| **Approval Status** | The approval status assigned to the component. You can change the status directly from the component's **Options** menu. Possible values are:   - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |

For custom components, click the [image: Option button] to open the **Options** menu at the end of a row to perform
component-level actions.

From the Options menu,you can:

- Update the component's approval status:
  - Approved
  - Deprecated
  - In Review
  - Limited Approval
  - Rejected
  - Reviewed
  - Unreviewed
- Delete the component.

Note: The available actions may vary depending on the component type and whether the
component is currently in use.

## Component Versions tab

The**Component Versions**tab displays a list of component versions.

Select a version to open the component version details page.

The table includes the following information:

| Column | Description |
| --- | --- |
| **Component Version** | Name of the component version.  Select the component name to open the **Overview** tab of the *Component Name* page.  Select the version to open the **Overview** tab of the *Component Name > Version* page. |
| **License** | License for this component version. |
| **Source** | Source for this component version. Possible values are:   - Custom. A custom component version. - KnowledgeBase. An unmodified Black Duck KnowledgeBase   component version. - Modified KnowledgeBase. A modified Black Duck KnowledgeBase   component version. |
| **Approval Status** | The approval status assigned to the component version. You can change the status directly from the component's **Options** menu. Possible values are:   - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |
| **Last Updated** | Date this component version was last modified and the user who last modified it. |

For custom components versions, click the [image: Option button] to open the **Options** menu at the end of a row to perform
component-level actions.

From the Options menu,you can:

- Update the component version's approval status:
  - Approved
  - Deprecated
  - In Review
  - Limited Approval
  - Rejected
  - Reviewed
  - Unreviewed
- Delete the component version.

Note: The available actions may vary depending on the component type and whether the component
version is currently in use.
