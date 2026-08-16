---
title: "Find component license information (including terms)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/find-component-license-information-including-terms-.html"
content_id: "R7sPf_OmmZOL4HzojgWl5A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:34.492990+00:00"
content_hash: "d75cef85c6ca6ad83b187d974f7d3752674f0259481a8bb2a18749a2326c51f8"
---

# Find component license information (including terms)

How to find licenses for components in a project.

## How to find licenses for components in a project

After you run an SCA test, follow these
steps:

1. Go to Portfolio, select an application, select a
   project, and open the Components tab.
2. Select a component.

   In the bottom section of the page, select the
   Licenses tab.   
    [image: component licenses tab]   

   From this tab, you can:

   - Change the license.
     1. Click Change.

        Note: The Change
        button only appears when more than one licensing option
        is available (when one license/group of licenses
        *OR* a different license/group of licenses is
        available for the component).
     2. Select the best license for the use case from the
        Select a License pulldown
        menu.

        Note: Click the
        x button in the pulldown menu
        to reset the selection.
     3. Click Save.

        This change is for all
        the branches included in the project.
   - If two or more licenses are available for the component, you can see
     the different terms for each license by clicking on the box with the
     license's name.
   - Review **Terms** definitions and obligations, categorized as
     **Required**, **Forbidden**, and **Permitted**.

   Note: Changes to license terms in the Black Duck KnowledgeBase™ are automatically synchronized
   with Polaris. See  for more
   information. Another SCA test is not required.

## How to view all licenses from a project

After you run an SCA test, follow these
steps:

Go to Portfolio, select an application, select a
project, and open the Licenses tab.

[image: license tab]   

From this tab, you can:

- Click the filter icon to open and close the filter panel. Filter
  a project's licenses by **License** (name) and/or **License
  Family**.
- View the list of your project's applicable licenses, the number of
  components each license applies to, and each license's family
  (Permissive, Restrictive Third Party Proprietary, Reciprocal,
  etc.).
- Click on a license's name to view **License Details**,
  including a list of components that use the license.
