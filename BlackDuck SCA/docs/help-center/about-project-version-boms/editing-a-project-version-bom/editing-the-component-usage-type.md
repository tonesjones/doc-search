---
title: "Editing the component usage type"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/editing-the-component-usage-type.html"
content_id: "~7uEtgObMhxEDXjBzfGyFw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:40.006091+00:00"
---

# Editing the component usage type

A component's usage indicates how it is intended to be included in the released version
of the project.

The usage statuses are:

- Dynamically Linked
- Statically Linked
- Source Code
- Separate Work
- Implementation of Standard
- Merely Aggregated
- Prerequisite
- Dev. Tool / Excluded
- Unspecified

Click here
for more information on usage.

Note: It is not possible to edit the usage type for binaries and snippets through the Source
view. Usage can only be edited via the BOM component.

To change a component's usage type:

1. Log into Black Duck.
2. Select the project name using the **Watching** or **My Projects** dashboard.
   The *Project Name* page appears.
3. Select the version name to open the **Components** tab and view the BOM.   
    [image: BOM page]
4. In the component list view of the BOM, click [image: image] and
   select **Edit** to open the Edit Component dialog box.
5. Select any of the options from the **Usage** list.
6. Click **Save**.

To change multiple component's usage type:

1. Display the project version
   BOM. Ensure you are in the Components view.
2. Check the box next to any number of components.
3. Click the **Bulk Actions** button.
4. Select **Component Usage**.

   The **Bulk Action: Component Usage** dialog box appears.

   [image: Bulk Action: Component Usage]
5. Select any of the options from the **Usage** list.
6. Click **Save**.
