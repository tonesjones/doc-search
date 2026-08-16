---
title: "Ignoring a component in a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/ignoring-a-component-in-a-bom.html"
content_id: "0T_FVQNEh2SLeo3BNJ33sg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:37.431836+00:00"
---

# Ignoring a component in a BOM

You can ignore an OSS component in the BOM of a project version so that any associated
risks are excluded from the risk calculations. Ignoring a component is considered a
component adjustment. Therefore, if you choose to apply persistent
edits, ignoring a component will apply to all versions of the project.

When you ignore an automatically-added OSS component from a project version BOM, it will
be moved to the Match Review page for further
action. This ensures that users can review and address these components later. Notably,
ignored components will continue to be excluded from risk calculations even if the code
where they were discovered is rescanned to update the BOM.

Note: You cannot ignore manually added components.

## How to ignore one or more components in a BOM

To ignore a single component in a BOM:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab.
4. Click [image: Options button] and select **Ignore** to open the Ignore Component dialog box.
5. Click **Ignore**.

   The component is relocated to the Match Review
   page, will not be included in the risk calculations for the project version,
   and will not be displayed in the BOM.

To ignore multiple components in a project version BOM:

1. Display the project version
   BOM. Ensure you are in the Components view.
2. Check the box next to any number of components.
3. Click the **Bulk Actions** button.
4. Select **Ignore**.

   The **Bulk Action: Ignore** dialog box appears.

     
    [image: Bulk Action: Ignore]
5. Click the **Save** button to perform the action or the **Cancel** button to
   exit the dialog box.

## How to unignore one or more components

To unignore a single component in a BOM:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the version name to open the **Components** tab.
4. Click **Match Review**.
5. Click [image: Options button] and select **Ignore** to open the Ignore Component dialog box.
6. Click **Ignore**.

   The component is relocated to the **Bill of Materials**
   page.

To unignore multiple components in a project version BOM:

1. Display the project version
   BOM. Ensure you are in the Components view.
2. Click **Match Review**.
3. Check the box next to any number of components.
4. Click the **Bulk Actions** button.
5. Select **Unignore**.

   The **Bulk Action: Unignore** dialog box appears.

   [image: Bulk Action: Unignore]

## How to view ignored components

To view ignored components:

1. While in the **Components** tab of the project version BOM, click **Match Review**.
2. Select **Ignored** from the filters list.

   [image: Ignored filter]

   The table displays all ignored components.
