---
title: "Create and manage automatic Fix PRs"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-and-manage-automatic-fix-prs.html"
content_id: "v6whJzSIf5XaqSLgBLB7Ng"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:36.643419+00:00"
content_hash: "93e0ca63bce89f9d72d5573cb8d6578e77be114896abef38b1f5ebe7307ad326"
---

# Create and manage automatic Fix PRs

For overview, prerequisites and inheritance, see [Fix Pull Requests (Fix PR)](../fix-pull-requests-fix-pr.md).

1. Create a Component Policy that uses the Create a fix pull request action. See [Component policies](../create-and-manage-policies/component-policies.md) for more information.

   A component policy (that includes the fix pull request action) defines the conditions under which Polaris creates fix pull requests. Policies are rule-based and can be scoped by security risk level.
2. Assign the component policy to applications, projects, or branches in your portfolio.
   - Organization Admins can add the component policy to your organization's default policies. See [Change your organization's default policies](../create-and-manage-policies/manage-your-default-policies/change-your-organization-s-default-policies.md) and Apply your default policies to your portfolio for more information.
   - Users with permissions to manage application, project, or branch settings can assign the component policy to specific applications, projects, or branches. See [Change the policies assigned to applications, projects, and branches](../create-and-manage-policies/change-the-policies-assigned-to-applications-projects-and-branches.md) for more information.
3. Configure Fix PR Settings.

   Fix PR settings can be customized at the organization, application, project, or branch level.
   - **Organization:** My Organization > Integrations
   - **Application:** Portfolio > select an application > Settings > Integrations
   - **Project:** Portfolio > select an application > select a project > Settings > Integrations
   - **Branch:** Portfolio > select an application > select a project > Branches tab > select a branch

   Navigate to the appropriate level and click the Edit icon next to the Fix Pull Request Settings header. The following settings are available:

   Maximum pull requests per branch
   :   Controls how many Fix PRs Polaris can create per branch per scan. The default is 5, but can be edited to suit project requirements.

       Important: When the maximum PR limit is reached and open PRs are merged or closed, Polaris does not automatically create additional Fix PRs for remaining vulnerabilities. A new scan must be triggered to generate the next batch.

       Consider the following when configuring this value:
       - If the limit is set to 5 and 10 vulnerabilities are detected, only 5 Fix PRs are created. Once the existing 5 Fix PRs are closed or merged, triggering a new scan will create the remaining 5 Fix PRs.
       - To address all known vulnerabilities in a single scan, set the maximum value to match or exceed the number of expected fixes — for example, set the limit to 20 if 10 or more fixes are anticipated.
       - Setting the limit too low creates a procedural burden: each round of remediation requires a follow-up scan to generate the next batch of Fix PRs.

   Upgrade guidance
   :   Sets the preferred upgrade path for remediation recommendations. The default is **Short term preferred**. Options:
       - **Short term only:** No Fix PR is created if no short-term upgrade guidance is available.
       - **Long term only:** No Fix PR is created if no long-term upgrade guidance is available.
       - **Short term preferred:** Creates a Fix PR using short-term upgrade guidance when available; otherwise uses long-term guidance.
       - **Long term preferred:** Creates a Fix PR using long-term upgrade guidance when available; otherwise uses short-term guidance.
4. Trigger a scan.

   Once the policy and settings are configured, trigger a scan. Polaris automatically creates Fix PRs for all issues that match the policy rules and Fix PR settings for the branch (inherited or modified), for components that include dependency upgrades resolving detected vulnerabilities.
   - Fix PRs appear in the SCM within a few minutes of the scan completing. Each Fix PR states the vulnerable version being replaced and the recommended upgrade — for example, upgrading from 2.12.1 to 2.25.4.
   - Fix PR information can also be viewed in the Polaris UI under Components tab > Triage Panel > Activity Logs and Component Details.

   Note: When the maximum Fix PR limit is reached and open Fix PRs are merged or closed, Polaris does not automatically create additional Fix PRs for remaining vulnerabilities. A new scan must be triggered to generate the next batch.
