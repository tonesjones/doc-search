---
title: "Managing project license conflicts"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-project-license-conflicts.html"
content_id: "BqpFGLppPaTRcccp3UPjKQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:09.957404+00:00"
---

# Managing project license conflicts

As a BOM reviewer, you need to understand when a component or subproject in your BOM has a
license with terms that are incompatible with the declared license of a project. Black
Duck identifies the specific license and term that is causing the incompatibility,
thereby letting you manage this conflict and reducing the risk of license
infringement.

Black Duck identifies the Black Duck KnowledgeBase conflicts (license terms that have the
same name but opposing
responsibilities) and the custom license terms that you defined as
in conflict with Black Duck KnowledgeBase terms for a project version.

Note the following:

- License conflict information is not automatically enabled. System Administrators
  must enable the **Legal** and **License Conflicts** tab for all
  *future* project versions. Use the project's **Settings** tabs to
  enable the feature for *current* projects.
- Note that Black Duck only determines license conflicts for subprojects and component versions
  with high license risk. For the Black Duck license risk model, "high risk" means
  that licenses in this family tend to have license conflicts under this business
  scenario (combination of distribution type and component usage) making them
  incompatible. Medium or low risks means it may have risks if the business
  scenario changes (or is defined incorrectly) or due to other, non-license
  conflicts factors.
- Black Duck calculates license risk during a scan or if you select to enable the
  feature for a current project.

  Manual edits to a BOM, including changing the usage for a component or the
  license of the project version using the **License Conflict** or
  **Components** tab will trigger a recalculation of the license
  conflict.
- License conflicts for snippets are not shown until the snippet is confirmed.
- You can create a
  policy rule that is triggered when a component's license conflicts
  with the license for a project version.

## Viewing project license conflicts

From a project version BOM, select the **Legal** tab, and if necessary,
select the **License Conflicts** tab to view a list of components that
have a license that conflicts with the project license.

  
 [image: License Conflict tab]   

The table displays the following information:

| Column | Description |
| --- | --- |
| [image: Policy Violation icon] | Policy violation.  Hover over the icon to view the policy rule(s) this component violates.  Select the icon to open the Policy Violations dialog box. |
| **Component** | Component or subproject name. If a license conflict is detected in a subproject of this project, the component name will be displayed along with the subproject in parentheses.  [image: Component of a subproject] |
| **Usage** | Indicates the usage of this component. |
| **License** | The license for this component.  Select the license name to open the *Component Name Version* Component License dialog box.   [image: image]   Use this dialog box to edit the existing license(s), view obligations, and view/edit the license text. |
| **Conflict** | Indicates there is a conflict. Select **Conflict** to open the Project License Conflicting Terms dialog box.   [image: Project License Conflicting Terms dialog box]   Use this dialog box to view the list of project license terms and conflicting component version license terms. |

## Editing a component or subproject with license conflicts

You can edit the component or subproject by clicking [image: Options] in the row of the component and select **Edit** to open the Edit
Component modal.

[image: Edit Component modal]

If the component or subproject is found in the parent project itself, a warning at the
top of the Edie Component modal notifying you that any changes made to the Component
details will be reflected in all versions of the project it is located in. Once you
have made the desired updates, click the **Save** button to accept your
changes.

If you are editing a component found in a subproject, a warning will appear at the top of the
modal notifying you that you are editing a component belonging to another project
along with the project's name and version. Clicking the project name will take you
to that project version's Details page.

[image: Editing a component belonging to another project]

## Adding comments to a component or subproject with license conflicts

Optionally, to add a comment, click [image: Options] in the row of the component and select **Comment** to open the
*Component/Subproject Name Version* Comment dialog box.

Enter the comment and click **Add Comment**. The comment appears for this
component in the BOM.
