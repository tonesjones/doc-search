---
title: "Managing comments in a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-comments-in-a-bom.html"
content_id: "9UvVCB_Nf6cG4gVrwhmdwg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:46.750732+00:00"
---

# Managing comments in a BOM

[HUB-3491]Comments apply to a specific
component version or subproject in a BOM. For example, you can use comments to explain
why a component version was ignored or why a policy violation was overridden.

Note:

- Comments are applied to a component version or subproject:
  - If the component version or subproject is deleted in a BOM, the comment
    is deleted. If the component version or subproject is then added back to
    the BOM, the comment(s) will reappear.
  - If the version of a component or subproject is changed in a BOM, the
    comment no longer appears.
- Comments can be persisted to a cloned project if the **Component Edits** option
  is enabled in the Cloning section of the project **Settings** tab.
- Comments by users who become inactive still appear in the BOM.
- A component version or subproject can have multiple comments.
- The search feature is not available for comments.

## Adding a comment in the Components view

Adding comments to components makes your feedback more clear, giving everyone the
ability to discuss any actions to be taken on a particular component. You can add a
comment to a single comment, or you can comment on a number components by using the
Bulk Actions button.

To comment on a single component:

1. Display the project version
   BOM. Ensure you are in the Components view.
2. Click [image: Down arrow] in the row where you want to add a comment and select
   **Comments**.

   The *Component/Subproject Name Version* Comment dialog box appears.

     
    [image: Component/Subproject Name Version Comment dialog box]
3. Enter the comment and click **Add Comment**.

To comment on multiple components simultaneously:

1. Display the project version
   BOM. Ensure you are in the Components view.
2. Check the box next to any number of components.
3. Click the **Bulk Actions** button.
4. Select **Comment**.

   The **Bulk Action: Comment** dialog box appears.

     
    [image: image]
5. Enter the comment and click **Add Comment**.

After either of the actions above, a comment icon ( [image: Comment icon] ) appears in the component version or subproject row indicating a comment
was added. The number shown in the icon indicates the number of comments for this
component version or subproject.

  
 [image: BOM page showing adjustment]

### Viewing a comment

Click [image: Comment icon] in the row where you want to view a comment.

### Editing a comment

Only the original writer can edit their comment.

1. Click [image: Down arrow] or [image: Comment icon] (if there are already comments) in the row where you want to
   edit a comment and select **Comment**.
2. Click [image: Down arrow] next to the comment you want to edit and select
   **Edit**.
3. Edit the comment, click **Update**, and then select **Close**.

### Deleting a comment

Only the original writer of the comment or Project Administrator can delete a
comment.

1. Click [image: Down arrow] or [image: Comment icon] (if there are already comments) in the row where you want to
   edit a comment and select **Comment**.
2. Click [image: Down arrow] next to the comment you want to delete and select
   **Delete**.

## Adding a comment in the Source view

1. Display the project version
   BOM. Ensure you are in the Source view.
2. Click the desired item in the file tree.
3. Click [image: Down arrow] in the row where you want to add a comment and select
   **Comments**, or click [image: image] if there are already
   comments present.

   The Comments dialog box appears.

     
    [image: Component/Subproject Name Version Comment dialog box]
4. Enter the comment and click **Add Comment**.

A comment icon ( [image: Comment icon] ) appears in the entry row indicating a comment was added. The number shown
in the icon indicates the number of comments for this component version or
subproject.

  
 [image: BOM page showing adjustment]

### Viewing a comment

Click [image: Down arrow] in the row where you want to view a comment and select **Comments**,
or click [image: image] if there are
already comments present.

### Editing a comment

Only the original writer can edit their comment.

1. Click [image: Down arrow] or [image: Comment icon] (if there are already comments) in the row where you want to
   edit a comment and select **Comments**.
2. Click [image: Down arrow] next to the comment you want to edit and select
   **Edit**.
3. Edit the comment, click **Save**, and then select **Close**.

### Deleting a comment

Only the original writer of the comment or Project Administrator can delete a
comment.

1. Click [image: Down arrow] or [image: Comment icon] (if there are already comments) in the row where you want to
   edit a comment and select **Comments**.
2. Click [image: Down arrow] next to the comment you want to delete and select
   **Delete**.
