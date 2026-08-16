---
title: "Managing copyrights"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-copyrights.html"
content_id: "FRITDDw1_jb_WC1MbO7rMg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:04.611465+00:00"
---

# Managing copyrights

Users with the Copyright Editor role can
manage open source copyright statements for their organization. Using this feature makes
it easier for you to include the full list of copyright holders for the open source
components you use in your notices file report.

Users with the Copyright Editor role can:

- View all copyright statements for a component version.
- Create or edit custom copyright statements.
- Edit Black Duck KnowledgeBase copyright statements
- Revert an edited Black Duck KnowledgeBase copyright statement to its original
  text.
- Activate or deactivate copyright statements.

Black Duck manages copyright statements by the origin name/id for a component version.
Therefore, edits made to copyright statements for an origin for a component version
apply to all BOMs that use that component version origin. This enables you to reuse data
across your organization and reduce your workload.

To manage copyright statements in Black Duck:

1. Review the existing Black Duck KnowledgeBase copyright statements.
2. If necessary, edit the existing KnowledgeBase copyright statements and/or create
   custom copyright statements.
3. Deactivate any copyright statements that do not apply.
4. Create the Notices file report and select the **Copyright Data** option to
   include copyright statements in your report.

## Viewing and managing copyright statements

To view and manage the copyright statements, do one of the following:

- In the project version BOM, click [image: Down arrow] in the row of the component version you wish to view copyright
  statements and select **Copyrights**.

  The component version **Copyrights** tab appears filtered to display the
  copyright statements for the origin used in your BOM.

    
   [image: Copyrights tab]   

  Note if a component version is not defined in the BOM (as shown by ( [image: Question Mark icon] ) for the version), the **Copyrights** option is not
  available.
- Select to view an open source component version and select the
  **Copyrights** tab.

    
   [image: Copyrights tab]   

  The page is unfiltered and lists all origins for this component version.

  Select an origin to view the copyright statements for that origin.

  Use the component origin name and ID filters to limit the origins displayed
  on the page.

For each copyright statement, the following information appears:

| Column | Description |
| --- | --- |
| **Copyrights** | Copyright text. |
| **Source** | Source for this copyright statement. Possible values are:   - **KB**. An unmodified, active copyright statement from   Black Duck KnowledgeBase. - **KB Modfied**. A copyright statement from Black Duck KnowledgeBase that has been edited,   deactivated, or reactivated. - **Custom**. Copyright statement created by a user with   the Copyright Editor role. |
| **Active** | One of the following icons appears:   - [image: image] Active copyright statement which will appear in your   Notices File report. - [image: image]   Inactive copyright statement which will not appear in   your Notices File report. |
| **Last Updated** | One of the following appears:   - **Never** indicates that the statement from Black Duck KnowledgeBase has never been modified. - Date and username.   - For Black Duck KnowledgeBase copyright     statements, the date when this copyright statement     was modified and the responsible user. A date and     username also appears for Black Duck KnowledgeBase     copyright statements that have been deactivated or     reverted back to their original text.   - For custom copyright statements, the date when     this statement was either created or last edited     and the responsible user. |

## Creating custom copyright statements

To create a custom copyright statement:

1. As copyright statements are based by component origin, select the origin for
   this copyright statement from the **Component Origins** section.
2. Click **Create**. The Create Copyright dialog box appears.

     
    [image: Create Copyrigth dialog box]
3. Enter the copyright text and click **Save**.

Copyright statements are active by default. See below to deactivate this
statement.

## Editing custom copyright statements

To edit a custom copyright statement:

1. In the row of the copyright statement you want to edit, select [image: Down arrow] and select **Edit**.

   The Edit Copyright dialog box appears.

     
    [image: Edit Copyright dialog box]
2. Edit the text and/or select or clear the **Active** option and click
   **Save**.

## Deactivating copyright statements

By default, all copyright statements are active.

To deactivate a copyright statement:

1. Do one of the following:
   - Click [image: Down arrow] in the row of the copyright statement you wish to
     deactivate and select **Deactivate**.
   - Select one or more checkboxes located to the left of the copyright
     statement and click **Deactivate**.

   You can also deactivate a copyright statement when editing it.

## Activating copyright statements

To activate copyright statements:

1. Do one of the following:
   - Click [image: Down arrow] in the row of the copyright statement you wish to activate
     and select **Activate**.
   - Select one or more checkboxes located to the left of the copyright
     statement and click **Activate**.

   You can also activate a copyright statement when editing it.

## Editing KnowledgeBase copyright statements

You can modify an existing Black Duck KnowledgeBase copyright statement.

To edit a KnowledgeBase copyright statement:

1. Click [image: Down arrow] in the row of the copyright statement you wish to edit and select
   **Edit**.

     
    [image: Edit Copyright dialog box]   

   If this is the initial attempt to edit a KnowledgeBase copyright statement,
   the option to revert to the original text is not available.
2. Edit the text and/or clear or select the **Active** option and click
   **Save**.

## Reverting KnowledgeBase copyright statements

If you edited a KnowledgeBase copyright statement, you can revert to the original
text of the KnowledgeBase copyright statement.

To revert a KnowledgeBase copyright statement:

1. Click [image: Down arrow] in the row of the copyright statement you wish to edit and select
   **Edit**.

   The dialog box displays the edited text and the original copyright text from
   the KnowledgeBase.

     
    [image: Edit Copyright dialog box]   

   Note: Reverted text may include poorly formatted and extraneous text not shown in the original
   copyright statement, which was edited to make it more readable.
2. Click **Revert to Original**.
3. Click **Save**.

## Updating KnowledgeBase copyright statements

The Black Duck KnowledgeBase may have updated copyright information.

You can refresh the copyright statements for a component origin: if there is new or
updated data, Black Duck updates the information shown while keeping any edits that
you made.

To update KnowledgeBase copyright statements for an origin:

1. Open the **Copyrights** tab, as described previously.
2. Select a component origin.
3. Click **Refresh**.
