---
title: "Reset policy inheritance for applications, projects, and branches"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/reset-policy-inheritance-for-applications-projects-and-branches.html"
content_id: "ftgTvW~V76BOWLn6M0D6_Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:04.821819+00:00"
content_hash: "b31b778f0223c7312cf4b1b3aa129b1c858672b8869451b9f57f4cb932cb29f7"
---

# Reset policy inheritance for applications, projects, and branches

Users with the appropriate permissions can reset the policies assigned to an application, project, or branch.

The procedures below describe how to reset policy assignments at the application, project, or branch level. After resetting, the entity inherits policies from its parent and will receive future policy updates automatically. Additionally, the procedures below describe how to apply an application or project's policies to a lower level entity.

## Reset policy inheritance for an application

When an application's policies have been customized, you can reset them so that the application inherits your organization's default policies again.

1. Go to Portfolio and select an application.
2. Go to Settings > Policies.
3. (Optional) To reset policy assignments so the application inherits your organization's default policies, follow these steps: 
   1. Select Reset next to the type of policy you wish to reset.

      Note: The Reset button only appears when the policies assigned to the application have been customized.

      The Reset Settings window appears.
   2. Select Reset.
4. (Optional) To reset policy assignments in the application's projects or branches (so that the policies assigned to the application are assigned to its projects or branches), follow these steps:
   1. Select Reset Inheritance next to the type of policy you wish to reset.

      The Reset inheritance for window appears.
   2. Use the Projects and Branches checkboxes to select the scope of the reset.

      - Select the Projects checkbox to assign the application's policies to the projects in the application.
      - Select the Branches checkbox to assign the application's policies to the branches in the application.
   3. Select Reset Inheritance.

The policy types you reset are now inherited from your organization's default policies. When your organization's default policies change, the application will be updated automatically.

## Reset policy inheritance for a project

When a project's policies have been customized, you can reset them so that the project inherits policies from its parent application (or your organization's defaults, if the application has not been customized).

1. Go to Portfolio, select an application, and select a project.
2. Go to Settings > Policies.
3. (Optional) To reset policy assignments so the project inherits policies assigned to its application, follow these steps: 
   1. Select Reset next to the type of policy you wish to reset.

      Note: The Reset button only appears when the policies assigned to the project have been customized.

      The Reset Settings window appears.
   2. Select Reset.
4. (Optional) To reset policy assignments in the project's branches (so that the branches inherit the policies assigned to the project), follow these steps:
   1. Select Reset Inheritance next to the type of policy you wish to reset.

      The Reset inheritance for window appears.
   2. Select the Branches checkbox to assign the project's policies to the branches in the project.
   3. Select Reset Inheritance.

The policy types you reset are now inherited from the application. When the policies assigned to the application change, the project will be updated automatically.

## Reset policy inheritance for a branch

After you customize the policies assigned to a branch, you can reset them so that the branch inherits policies from its project.

1. Go to Portfolio, select an application, and select a project.
2. Go to Branches and select the branch you wish to modify.

   The Edit Branch window opens.
3. (Optional) Under Policies, select Use Project Policies using the Issue Policies, Component Policies, or Pull/merge request policies dropdowns to inherit the respective policies from the parent project.
4. (Optional) Under Test Scheduling, select Use project policies to inherit the project's test scheduling policy.
5. Select Save.

The policy types you reset are now inherited from the project. When the policies assigned to the project change, the branch will be updated automatically.
