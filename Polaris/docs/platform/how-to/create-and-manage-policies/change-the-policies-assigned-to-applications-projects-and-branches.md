---
title: "Change the policies assigned to applications, projects, and branches"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/change-the-policies-assigned-to-applications-projects-and-branches.html"
content_id: "T33ZYv~K~ixLez5BZHsp_Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:04.131760+00:00"
content_hash: "e187346eebb6ef084109f96d41c1e3af1f76c496c849bceee08d6af52f205b8d"
---

# Change the policies assigned to applications, projects, and branches

Users with the appropriate permissions can override the default policies assigned to applications, projects, and branches.

Only Organization Admins can set your organization's default policies. See [Manage your default policies](manage-your-default-policies.md) for more information. The procedures below describe how to override those defaults at the application, project, or branch level. Users must have the appropriate permissions to manage settings at each level.

## Change the policies assigned to an application

By default, the applications in your portfolio inherit your organization's default policies. Users with permissions to manage application settings can change the policies assigned to an application.

Important: When you modify the policies assigned to an application, the application stops inheriting your organization's default policies (of the same type), and won't change when your organization's default policies are updated.

1. Go to Portfolio and select an application.
2. Go to Settings > Policies.
3. Select Edit next to the type of policy you wish to assign, and then add or remove policies, as required.
4. Select Save.

## Change the policies assigned to a project

By default, the projects in your portfolio inherit your organization's default policies (or their application's policies, when set). Users with permissions to manage project settings can change the policies assigned to a project.

Important: When you modify the policies assigned to a project, the project stops inheriting your organization's default policies (of the same type), and won't change when your organization's default policies are updated.

1. Go to Portfolio, select an application, and select a project.
2. Go to Settings > Policies.
3. Select Edit next to the type of policy you wish to assign, and then add or remove policies, as required.
4. Select Save.

## Change the policies assigned to a branch

By default, the branches in your portfolio inherit your organization's default policies (or their project's/application's policies, when set). Users with permissions to manage branch settings can change the policies assigned to a branch.

Important: When you modify the policies assigned to a branch, the branch stops inheriting your organization's default policies (of the same type), and won't change when your organization's default policies are updated.

1. Go to Portfolio, select an application, and select a project.
2. Go to Branches and select the branch you wish to modify.

   The Edit Branch window opens.
3. (Optional) Use the Issue Policies, Component Policies, and Pull/merge request policies dropdown menus to add or remove policies, as required.
4. (Optional) Use the options under Test Scheduling to change the test scheduling policy assigned to the branch.

   Options include:
   - None: Disable test scheduling for the branch.
   - Use project policies: Inherit the project's test scheduling policy.
   - Manually select policies: Manually select a test scheduling policy for the branch.
5. Select Save.
