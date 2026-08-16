---
title: "Reset an edited component"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/reset-an-edited-component.html"
content_id: "~QMz1Z1F1kikzKv5voTFPA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:30.762517+00:00"
content_hash: "e15ab06553b8cfc5a4d40e1287c3bdade6e77d5232d2ee7bcfda99f03d4232bf"
---

# Reset an edited component

After you modify a component captured in an SCA test, you can reset the component to its original state. To do so, follow these steps:

1. Go to Portfolio, select an application, select a project, and open the Components tab.
2. (Optional) If you're editing a component that only exists on a non-default branch, select the branch using the dropdown near the top of the page.
3. Select the options [image: icon polaris options] icon at the end of the component's row and select Reset.

   The Reset Confirmation window opens.

   Note: You can only reset components with a match type of Manually Edited.
4. (Optional) Enter a comment in the Add Comment field.

   Tip: The comment you enter appears in the component's Activity Log, which can be viewed when the component is triaged.
5. Select Reset Changes.

   A notification appears, indicating the reset will be applied upon completion of the next test.

   Important: You must retest the project/branch in which the component is detected for the reset to take effect.
