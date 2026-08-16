---
title: "Edit a component"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/edit-a-component.html"
content_id: "nS8RcDljrNVQviw0lNGWYA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:30.130502+00:00"
content_hash: "bff6569eed4080380a020d350796d6acf15d5cbcb5cd43a8ecae3da4822412f9"
---

# Edit a component

Follow these steps to manually modify a component:

1. Go to Portfolio, select an application, select a project, and open the Components tab.
2. (Optional) If you're editing a component that only exists on a non-default branch, select the branch using the dropdown near the top of the page.
3. Select the options [image: icon polaris options] icon at the end of the component's row and select Edit.

   The Edit Component window opens.
4. Modify the component, as required.

   Important: When you modify a component captured in a test with multiple origins, if you select a specific origin, only that origin will be preserved. All of the component's other origins (and the issues associated with them) will be removed.
5. (Optional) Select Only apply changes to this branch to only modify the component on the current branch. By default, changes you make are applied across branches in the project.
6. Select Save.

   A banner appears near the top of the Components tab, indicating the component is being updated. After the component is updated, select Refresh to update the list of components.

   Tip: When you modify a component that you added manually, its match type value (Manually Added) does not change. When you modify a component captured in a test, its match type value changes to Manually Edited. You can use the Match Type filter to quickly identify components that were added manually, and edited components.

   Note: If you edit a component detected in both package manager and signature analysis tests, the component may have more than one origin after changes are applied.
