---
title: "Add a component (or component origin)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/add-a-component-or-component-origin-.html"
content_id: "yiOAAh1y2vOGhU~PDU5x_Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:29.505379+00:00"
content_hash: "61601c815d6f75445a3e61adf028b21f3fc68caf40567d6b5b586dae10015d24"
---

# Add a component (or component origin)

Follow these steps to manually add a component or component origin to a project:

1. Go to Portfolio, select an application, select a project, and open the Components tab.
2. (Optional) If you're adding a component to a non-default branch, select the branch using the dropdown near the top of the page.
3. Select Add Component.

   The Add Component window opens.
4. Use the options on the Add Component window to identify the component, component version, or component origin you wish to add:

   Tip: To add a component origin, the Component and Version you select should already exist in the project/branch.

   1. Component: Enter the name of the component you wish to add in this field. As you type, similarly-named components appear. When you find the component you wish to add, select it.

      [image: component add text search]

      Note: If the component you're looking for isn't captured in the Black Duck KnowledgeBase™, you can submit a request to have it added. Select submit a request, and follow the instructions in Black Duck Community to submit a support case. When you submit your support case, select Black Duck KnowledgeBase using the Product dropdown.
   2. Version: Select the version of the component you wish to add.
   3. Origin (optional): Select the component's origin.

      If you don't select a value, No Origin Specified is used by default. You can use the Filter dropdown to limit values in the Origin dropdown to a specific external namespace.
   4. Comment (optional): Enter a comment that describes why the component was added.

      Tip: The comment you enter appears in the component's Activity Log, which can be viewed when the component is triaged.
   5. Select Add Component.

   A banner appears near the top of the Components tab, indicating the component is being added. After the component is added, select Refresh to update the list of components.

   Tip: Components you add manually have a match type value of Manually Added. If you add an origin to a component detected in a test, Manually Added is added to its match types. You can use the Match Type filter to quickly identify components that were added manually, and components with origins that were added manually.

   Additionally, when you open a test's results, you can use the Found post-test filter to find issues associated with manually-added components. See [Find issues captured after a test](../find-issues-captured-after-a-test.md) for more information.
