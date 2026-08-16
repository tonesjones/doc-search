---
title: "Manage your default policies"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/manage-your-default-policies.html"
content_id: "tdhKR1JIv9oPxe3Ac_6vNA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:01.596873+00:00"
content_hash: "44050d43892b3e56ee24b8e0716e1b848c11f9e8e7f4256462e2eb887ef1285f"
---

# Manage your default policies

Organization Admins can set the default policies assigned to applications, projects, and branches in your portfolio, and can choose what types of branches default policies are assigned to.

## Policy inheritance

The default policies set at the organization level are automatically applied to applications, projects, and branches in your portfolio, but can be overridden. The policies assigned to applications, projects, and branches take precedence:

- Policies assigned to an application override your organization's default policies
- Policies assigned to a project override organization and application-level policies
- Policies assigned to a branch override organization, application, and project policies

When policy assignments change at a higher level, the change is automatically applied to all lower levels that have not been overridden.

Note: When you modify your organization's default policies, changes do not affect applications, projects, or branches that have already been customized. Organization Admins can force updates to propagate to overridden levels if necessary. See [Apply your default policies to your portfolio](manage-your-default-policies/apply-your-default-policies-to-your-portfolio.md) for information.

To check how many projects and branches are using your organization's default policies throughout your portfolio, go to My Organization > Policies. At the bottom of each panel, the number of projects and branches using the default policies is displayed. For example "3 out of 3 DAST projects and 43 out of 50 branches inherit these settings".

Users with access to application and project settings can check how many projects/branches inherit your organization's default policies.

- For an application, go to Portfolio, select an application, and go to Settings.
- For a project, go to Portfolio, select an application, select a project, and go to Settings.

When Inherited appears next to a policy type, the policies that apply to the application (example below) or project are inherited.

[image: Screenshot of inherited issue policies in an application's settings.]

## Default and non-default branches

Organization Admins can control what types of branches default policies are applied to (or prevent default policies from being assigned to branches altogether). See [Control how default policies are applied to branches](manage-your-default-policies/control-how-default-policies-are-applied-to-branches.md) for more information.
