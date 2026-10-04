---
title: "Create and manage Policies"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-and-manage-policies.html"
content_id: "rIsrv7WBBJhOtYFAQ34JgA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:19.842121+00:00"
content_hash: "06431e4f0b1c5215bf7149030eb806c0615bb303a62e084493b848d164663263"
---

# Create and manage Policies

There are four types of policies in Polaris:

- Issue policies: Use issue policies to automate actions and flag policy violations when issues with specific properties are detected in a test (including setting fix-by dates and creating SAST Fix PRs).
- Pull/merge request policies: Policies that are triggered by a pull request and enable pull request comments with the option to create Fail PRs, when issues with specific properties are detected in a branch.
- Component policies: Use component policies to automate actions, flag policy violations, and/or create SCA Fix PRs when components with specific properties are detected in an SCA test.
- Test scheduling policies: Use test scheduling policies to automate tests of SCM-integrated branches on a weekly or daily basis.

Organization Admins and Organization Application Managers can create and manage policies on the Policies page.

## Default policies

Organization Admins can set the default policies assigned to your organization's applications, projects, and branches, and can choose what types of branches default policies are assigned to. The default policies set at the organization level are automatically applied to applications, projects, and branches in your portfolio, but can be overridden in application, project, and branch settings. See [Manage your default policies](create-and-manage-policies/manage-your-default-policies.md) for details.

## Assign policies to applications

Applications inherit policies from the organization by default. Users with permissions to manage application settings can change the policies assigned to an application. Modified applications no longer receive updates when organization-level policies change.

See Change the policies assigned to an application for more information.

## Assign policies to projects

Projects inherit policies from their parent application by default. Users with permissions to manage project settings can change the policies assigned to a project. Modified projects no longer receive updates when policies change at a higher level.

See Change the policies assigned to a project for more information.

## Assign policies to branches

Branches inherit policies from their parent project by default. Users with permissions to manage branch settings can change the policies assigned to a branch.

See Change the policies assigned to a branch for more information.

## Policy permissions

Before you proceed, review policy-related permissions here: Roles and permissions.
