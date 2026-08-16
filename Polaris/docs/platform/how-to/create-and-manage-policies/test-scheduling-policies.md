---
title: "Test scheduling policies"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/test-scheduling-policies.html"
content_id: "2m8KNKzOk3xcI3Huh1GUEg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:00.950862+00:00"
content_hash: "54c4031a43a92ebb2d044bb2c508f93eb7a2469cba46e0912660e62379b2311e"
---

# Test scheduling policies

Use test scheduling policies to automate tests of SCM-integrated branches on a weekly or daily basis.

Organization Admins and Organization Application Managers can create and manage test scheduling policies on the Policies page.

Important: If you assign a test scheduling policy to a project or branch that isn't connected to an SCM repository, it will not function as expected. Before you use test scheduling policies, set up an SCM integration, and import branches from your repository. For more information, see [Connect a Polaris project to a repository in your SCM](../connect-a-polaris-project-to-a-repository-in-your-scm.md) and Create and manage branches in a project.

## View a test scheduling policy's details

1. Go to Policies and open the Test Scheduling Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select View.

   [image: ui test scheduling policies tab]

## Create a test scheduling policy

1. Go to Policies and open the Test Scheduling Policies tab.
2. Click + Add Policy. The Add Test Schedule Policy screen appears.

   [image: policy scheduling create]   

   Tip: Instead of creating a new test scheduling policy, you can use a preexisting policy as a starting point (and adjust the policy as you wish). Click the icon at the end of a policy's row and select Duplicate.
3. Enter a Policy Name (required) and Short Description (optional).

   Note: Policy names are limited to 255 characters. Policy descriptions are limited to 512 characters.
4. Select how often tests will run on projects or branches the policy is assigned to:

   - Daily: Projects or branches are scanned on a daily basis.
   - Weekly: Projects or branches are scanned on a weekly basis.
5. Click Save.

The test scheduling policy is saved. To apply it, you can:

- Assign it to specific applications, projects, or branches. See [Change the policies assigned to applications, projects, and branches](change-the-policies-assigned-to-applications-projects-and-branches.md) for more information.
- Make it your organization's default test scheduling policy (provided you have Organization Admin permissions). See Change your organization's default test scheduling policy for more information.

## Modify a test scheduling policy

1. Go to Policies and open the Test Scheduling Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Edit.
3. Modify the policy, as required.
4. Select Save.

## Change your organization's default test scheduling policy

Organization Admins can change your organization's default test scheduling policy. See [Manage your default policies](manage-your-default-policies.md) for more information.

## Delete a test scheduling policy

1. Go to Policies and open the Test Scheduling Policies tab.
2. Click the options [image: icon polaris options] icon at the end of the policy's row and select Delete.

   A confirmation appears.
3. Click OK to delete the policy.

   CAUTION:

   Policies you delete cannot be recovered.
