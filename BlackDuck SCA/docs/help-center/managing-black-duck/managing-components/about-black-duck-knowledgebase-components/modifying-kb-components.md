---
title: "Modifying KB components"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/modifying-kb-components.html"
content_id: "M7oXtL4huxqVPReaybY44A"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:18.524454+00:00"
---

# Modifying KB components

Users with the Component Manager role can
modify the information shown for a Black Duck KB component or component
version.

The revised information will appear in your current BOMs and in any future BOMs that
contain this component/component version. Note that local edits to a component in a BOM
made by a user, such as the BOM Manager, to a BOM supersede the edits to the
component/component version made by the Component Manager.

To modify a KB component or component version:

1. Add the component and/or component version to Component Management.
2. Modify the KB component or component version.

Note: Setting the status of a KB
component and all versions listed in the Component Management table to **Unreviewed**
removes the KB component and its versions from the Component Management table. Note that
this does not apply to those KB components and versions shown with a source of
**Modified KnowledgeBase**.

To add a KB component or component version to the Component Management table:

1. Log in to Black Duck with the Component Manager role.
2. Click [image: image] > **Components**.

   The **Components** tab appears.

     
    [image: Component Management page]
3. Select **Add** > **Add a KnowledgeBase component** to open the Add
   Component dialog box.
4. Select the KB component and if adding a component version, select a version.
5. Select a status for this component.

   The unreviewed status is not available when adding a KnowledgeBase component.
6. Click **Save**.

The component appears in the **Components** tab with **KnowledgeBase** as the
Source.

To add additional versions, repeat this process, selecting the component and versions
from the Add Component dialog box.

To modify a KB component:

1. Log in to Black Duck with the Component Manager role.
2. Click [image: image] > **Components**.

   The **Components** tab appears.
3. Select the KB component you wish to modify.

   The **Overview** tab for the *Component Name* page appears.

   Note: You can also display the **Overview** tab by searching for the component and selecting
   to view it from the search results.
4. Select the **Settings** tab.
5. Modify the information and click **Save**.

The Source for this component is now **Modified KnowledgeBase**.

To modify a KB component version:

1. Log in to Black Duck with the Component Manager role.
2. Click [image: image] > **Components**.

   The **Components** tab appears.
3. Select the KB component version you wish to modify. Select the version from the
   **Component Versions** tab or in the **Components** tab, select > next
   to the KB component name to display the versions.

   The **Overview** tab for the *Component Name > Version* page appears.
4. Select the **Settings** tab.
   - Select **Component Details** to edit the release date, notes, and
     status for this KB component version.
   - Select **License** to modify the existing license or add a new license or
     group.
5. Modify the information and click **Save**.
