---
title: "Setting or modify a component's status"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/setting-or-modify-a-component-s-status.html"
content_id: "mDg919Ekjjk3OR6ZFwowEA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:24.655689+00:00"
---

# Setting or modify a component's status

You may want to approve versions or restrict usage in your BOM to approved Black Duck KB or custom components and/or component versions.

Users with the Component Manager role can
set a review/approval status on the component or component version at the global level
and then use that status in policy rules.

For example, to ensure that only approved components are included in your BOM:

1. Determine the components (from Black Duck KB and custom components)
   that are approved for your BOMs.
2. Set the status for each of these components and/or component versions to
   "Approved".
3. Create policy
   rules such that any component or component version that does not have
   an "Approved" status triggers a policy violation.

Policy violations appear in your BOM for all components that do not have an approved
status.

## Changing the status of components and/or versions

- For KB components, you set the initial status of a KB component and/or
  component version when you added it to Component Management.

  The unreviewed status is not available for KB components.
- By default, a custom component/custom component version has a status of
  "Unreviewed".

Note that the status of a component is independent of the status of its versions.

To modify the status for a component:

1. Log in to Black Duck with the Component Manager role.
2. Click [image: image] > **Components**.

   The **Components** tab appears.

     
    [image: Components tab]
3. Do one of the following:

   - Click [image: image] in the
     row of the component that you want to change the status and select a
     status from the list.
   - Modify the status using the **Settings** tab in the *Component
     Name* page:
     1. Select the component you wish to modify from the
        **Components** tab.

        The **Overview** tab of
        the *Component Name* page appears.
     2. Select the **Settings** tab.
     3. Select a status from the **Approval Status** list and
        click **Save**.

To modify the status for a component version:

1. Log in to Black Duck with the Component Manager role.
2. Click [image: image] > **Components**.

   The **Components** tab appears.

     
    [image: Components tab]
3. Select the **Component Versions** tab.

     
    [image: Component Versions tab]
4. Do one of the following:

   - Click [image: image] in the
     row of the component version that you want to change the status and
     select a status from the list.
   - Modify the status using the **Settings** tab in the *Component Name
     > Version* page:
     1. Select the component version you wish to modify from the
        **Component Versions** tab.

        The **Overview**
        tab of the *Component Name > Version* page
        appears.
     2. Select the **Settings** tab.
     3. Select a status from the **Approval Status** list and
        click **Save**.
