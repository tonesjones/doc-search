---
title: "Create and manage labels"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-and-manage-labels.html"
content_id: "D7mPFPaCkap7IR3wi0OLbA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:27.645572+00:00"
content_hash: "7523b247ec11e6338e20fa80945ae45b60e067e473edbf2dbdd8c9f95dfc7516"
---

# Create and manage labels

As an Organization Administrator, you can create labels that users can apply to Polaris objects to categorize them in ways that make sense to your organization. For example, labels can represent business units, development teams, or environments. When used consistently, labels offer enhanced filtering and navigation of applications, projects, and dashboards, as well as more granular reporting capabilities.

Note: Labels have replaced *Application Tags* in the Polaris UI. Tags you previously assigned to your applications were converted to labels automatically.

Labels can be applied to the following objects:

- Applications
- Projects
- Branches (SAST & SCA projects only)

In My Organization > Labels, you can create labels, merge or duplicate existing labels, and control whether non-Admin users have the ability to create their own labels. Once you have created a set of labels, users with the appropriate permissions can apply them to Polaris objects, as shown in the following table.

Table 1. Where labels can be applied

| To apply labels to… | See… |
| --- | --- |
| Applications | - Create an application - Settings tab (Applications) |
| Projects | - Add a SAST & SCA project to an application - Settings tab (Projects) |
| Branches (SAST & SCA) | - Add a branch to a project |

**Using labels as report and dashboard filters**

Once applied to objects, labels are available to use as filters on the Reporting and Dashboards pages.

When creating a report or report configuration, filter by label when adjusting the report scope. For example, the report scope can include only branches with the selected labels applied (but this is not supported for SBOM reports). For more details, see [Create a report](create-a-report.md) and Create and manage report configurations.

On most dashboards, you can filter data by one or more application, project, and branch labels. For more details, see [Work with dashboards](work-with-dashboards.md).

## Work with labels

To access labels in Polaris, go to My Organization > Labels.

| How to... | Steps |
| --- | --- |
| Create a label | - Click Create Label. - Enter a name and an optional description (max. 255 characters). - Click Save. |
| Allow non-Admin users to create new labels | - Under Label Options, select the Allow new labels to be created within applications and projects checkbox. |
| Edit a label and view its usage across applications, projects, and branches. | - Select the three-dot menu next to the label, then select Edit. - Edit label details, then click Save. - Usage displays a count of the applications, projects, and branches (if any) that this label is applied to. - Click the link on applications to view the Portfolio page filtered by the label you are currently editing. |
| Duplicate a label | - Select the three-dot menu next to the label, then select Duplicate. - The duplicated label is created with “-1” appended to the name. |
| Merge labels  CAUTION:  Merging labels cannot be undone. Any report configurations that include merged labels in their report scope will fail to run (including on a schedule). You must update these report configurations to exclude merged labels from their scope; see [Create and manage report configurations](create-a-report/create-and-manage-report-configurations.md). | - Select two or more labels. - Click Merge Selected. - In the Merge Labels dialog, enter a name and optional description for the merged label. - Click Merge. |
| Delete a label  CAUTION:  Any report configurations that include a deleted label in their report scope will fail to run (including on a schedule). You must update these report configurations to exclude deleted labels from their scope; see [Create and manage report configurations](create-a-report/create-and-manage-report-configurations.md). | - Select the three-dot menu and then select Delete. - In the dialog, select DELETE LABEL. |
| Search for a label | - Enter an alphanumeric string to search for all matching labels. |

## Tutorial: Create and manage labels

Note: Interactive tutorials are updated periodically and may change without notice.

Figure 1. Tutorial: Create and Manage Labels. *This interactive tutorial demonstrates how to create and manage labels in Polaris. Labels can apply to applications, projects, and branches.*
[Open in new tab.](https://www.iorad.com/player/2594291/Polaris--Create-and-Manage-Labels)
