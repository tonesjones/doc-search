---
title: "Create and manage branches in a project"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-and-manage-branches-in-a-project.html"
content_id: "cZCjgcYMtGhd8ThTn7Y0yQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:26.053017+00:00"
content_hash: "1d44c9f2c6e2439349e77ba6320cfbe6db8c6af3b09c98fe977c9488a0354bc1"
---

# Create and manage branches in a project

How to add a branch to your SAST & SCA project, or modify a branch that already exists.

## Add a branch to a project

Follow these steps to add a branch to a SAST & SCA project. By default, each project can include up to 10 branches.

Note: When you create a project, Polaris creates the project's first (default) branch automatically.

1. After you open a SAST & SCA project, open the Branches tab.
2. Select + Create New Branch.

   The Create New Branch window opens.
3. To create a branch that isn't connected to a repository:
   1. Select Manually create new branch.
   2. Enter a Branch Name. Limit is 255 characters.

      Note: Branch names must be unique within projects.
4. To add a branch from an SCM repository:

   Note: You cannot use this option until you set up an SCM integration. See [Connect a Polaris project to a repository in your SCM](connect-a-polaris-project-to-a-repository-in-your-scm.md) or Connect Polaris to Multiple SCM Repositories for more information.

   1. Select Create new branch from SCM integration.
   2. Select a branch in your repository with the SCM Branch dropdown.
5. (Optional) Enter a Branch Description. Limit is 256 characters.
6. (Optional) Select Set as Default Branch for Project to make the branch the default branch for the project.

   Note: Default branches automatically inherit the project's policies. When you change a project's default branch:
   - The project's policies are automatically applied to, and enabled on, the new default branch (replacing any policies that were previously assigned to the branch). Organization Admins, Organization Application Admins, Application Managers, and other users with permissions to manage branch settings can disable policies on the default branch.
   - Policies are automatically disabled on the old default branch.
7. (Optional) Use the Labels dropdown to apply one or more labels to the branch. Enter a text string to view all matching labels, or create a new label (if this allowed by your Organization Administrator).
8. (Optional) Enable issue, pull/merge request, and/or component policies using the Issue Policies, Component Policies, and Pull/merge request policies dropdowns.

   Note: By default, issue, component, and pull/merge request policies are disabled for new branches.

   Each dropdown allows you to select specific policies, use the policies assigned to the branch's project (Use Project Policies), or leave policies disabled (None).

   Note: Organization Admins, Organization Application Admins, Application Managers, and users with permissions to manage branch settings can customize policies for non-default branches. Default branches automatically inherit the project's policies.
9. (Optional) Enable a test scheduling policy:

   Note: By default, test scheduling policies are disabled for new branches.

   - Select Use project policies to inherit the project's test scheduling policy.
   - To assign a specific test scheduling policy to the branch, select Manually select policies and choose the policy from the dropdown menu.
10. Select Add.

## Edit a branch (manually created)

Follow these steps to modify a manually created branch.

1. After you open a SAST & SCA project, open the Branches tab.
2. Select the branch you wish to edit.

   The Edit Branch window opens.
3. Edit the branch, as required. You can:

   - Change a branch's name or description (for branches that aren't connected to a repository).
   - Change the project's default branch.

     Note: Default branches automatically inherit the project's policies. When you change a project's default branch:
     - The project's policies are automatically applied to, and enabled on, the new default branch (replacing any policies that were previously assigned to the branch). Organization Admins, Organization Application Admins, Application Managers, and other users with permissions to manage branch settings can disable policies on the default branch.
     - Policies are automatically disabled on the old default branch.
   - Change a non-default branch's automatic deletion setting.
   - Enable, disable, or customize a branch's policies.
   - Change which labels are applied to the branch.
   - Include or exclude this branch in issue tracking synchronization. When enabled, this branch will be considered when determining if issues should be automatically closed in external issue trackers. See Automatically close tickets and synchronize triage statuses for more information.
4. Select Save.

## Edit a branch (SCM Integration)

Follow these steps to modify a branch from a SCM integration.

1. After you open a SAST & SCA project, open the Branches tab.
2. Select the branch you wish to edit.

   The Edit Branch window opens.
3. Options available (varies by type of integration) can include:

   - Change the project's default branch.
   - Change **Test Automation** for this branch. See [Event-Based Test Automation in Polaris for SCM Integrations](event-based-test-automation-in-polaris-for-scm-integrations.md).
   - Enable, disable, or customize a branch's policies.
   - Include or exclude this branch in issue tracking synchronization. When enabled, this branch will be considered when determining if issues should be automatically closed in external issue trackers. See Automatically close tickets and synchronize triage statuses for more information.
   - Manage the Fix Pull Request settings for the branch including maximum number of Fix PRs and upgrade guidance, if applicable (see [Fix Pull Requests (Fix PR)](fix-pull-requests-fix-pr.md)).
4. Select Save.

## Change a project's default branch

Follow these steps to change a SAST & SCA project's default branch.

1. After you open a SAST & SCA project, open the Branches tab.
2. (Optional) Select the toggle near Show IDE Branches to show branches created using Code Sight.

   Although it is possible to make an IDE branch a project's default branch, we recommend using a branch created in Polaris instead. Using an IDE branch as a project's default branch may cause confusion, as:
   - By default, IDE branches are hidden on the Branches tab.
   - By default, tests of IDE branches are hidden on the Tests page.
   - IDE branches are not compatible with SCM integrations.
3. Click the icon at the end of the branch's row and select Make Default Branch.

   Note: Default branches automatically inherit the project's policies. When you change a project's default branch:
   - The project's policies are automatically applied to, and enabled on, the new default branch (replacing any policies that were previously assigned to the branch). Organization Admins, Organization Application Admins, Application Managers, and other users with permissions to manage branch settings can disable policies on the default branch.
   - Policies are automatically disabled on the old default branch.

   Note: Non-default branches may be deleted after a period of inactivity. When you change a project's default branch, the previous default branch inherits the project's branch deletion setting. Edit the previous default branch to modify its automatic deletion setting.

## Configure automatic branch deletion

You can configure Polaris to automatically delete non-default branches that aren't tested for a period between 1 and 90 days. By default, non-default branches are retained indefinitely. You can adjust this in each application, project, and branch's settings.

Note: A branch's automatic deletion setting overrides project and application settings; a project's automatic deletion setting overrides application settings. This way, even if an application is configured so non-default branches that aren't tested for a day are deleted, you can still preserve specific branches (or branches in specific projects) indefinitely, or for a longer duration.

Triage data is preserved when a non-default branch is deleted automatically. This way, if you recreate the branch (using the same name) and test the same code, your triage history is restored.

### Change an application's automatic branch deletion setting

1. Go to Portfolio and select an application.
2. Go to Settings > General.
3. Adjust the application's Automatic Branch Deletion setting, as required.
4. Select Save.

### Change a project's automatic branch deletion setting

By default, each project follows its application's branch deletion setting.

1. Go to Portfolio, select an application, and select a project.
2. Go to Settings > General.
3. Adjust the project's Automatic Branch Deletion setting, as required.
4. Select Save.

### Change a branch's automatic branch deletion setting

Note: See Edit a branch (manually created) for more information.

## Delete a branch

Follow these steps to delete a SAST & SCA project's branch.

1. After you open a SAST & SCA project, open the Branches tab.
2. (Optional) Select the toggle near Show IDE Branches to show branches created using Code Sight.
3. Click the icon at the end of the branch's row and select Delete.

   CAUTION:

   Deleting a branch will also delete all linked test results. This action cannot be undone.
