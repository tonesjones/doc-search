---
title: "Create and manage automatic Fix PRs"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-and-manage-automatic-fix-prs.html"
content_id: "v6whJzSIf5XaqSLgBLB7Ng"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:19.254468+00:00"
content_hash: "417360ba4aeceecb92aa8c6c532b9c08fc4f24b4aebd03c328a50630800b2475"
---

# Create and manage automatic Fix PRs

Use a component policy to automatically create SCA Fix PRs for findings after each scan.

For overview, prerequisites, and inheritance, see [SCA Fix Pull Requests](../fix-pull-requests-fix-pr.md).

1. Create a Component Policy that uses the Create a fix pull request action.

   See [Component policies](../create-and-manage-policies/component-policies.md) for more information. A component policy (that includes the fix pull request action) defines the conditions under which Polaris creates SCA fix pull requests.
2. Assign the component policy to your organization, an application, a project, or a branch.
   - Organization Admins can add the component policy to your organization's default policies. See [Change your organization's default policies](../create-and-manage-policies/manage-your-default-policies/change-your-organization-s-default-policies.md) for more information.
   - Users with permissions to manage application, project, or branch settings can assign the component policy to specific applications, projects, or branches. See [Change the policies assigned to applications, projects, and branches](../create-and-manage-policies/change-the-policies-assigned-to-applications-projects-and-branches.md) for more information.
3. (Optional) Review and update SCA Fix PR settings.

   Fix PR settings can be customized at the organization, application, project, or branch level.
   - **Organization:** My Organization > Integrations
   - **Application:** Portfolio > select an application > Settings > Integrations
   - **Project:** Portfolio > select an application > select a project > Settings > Integrations
   - **Branch:** Portfolio > select an application > select a project > Branches tab > select a branch

   Navigate to the appropriate level and click the Edit icon next to Fix Pull Request Settings. The following settings are available:

   Table 1. SCA Fix PR settings

   | Setting | Description |
   | --- | --- |
   | Maximum pull requests per branch | The maximum number of Fix PRs created by Polaris (SAST and SCA combined) that can be open on a branch at a time. The default is 5, but can be edited to suit project requirements.  Important: When the maximum PR limit is reached and open PRs are merged or closed, Polaris does not automatically create additional Fix PRs for remaining vulnerabilities. Run a new test to create the next batch of Fix PRs.  Consider the following when configuring this value:  - If the limit is set to 5 and 10 vulnerabilities are detected, only 5 Fix PRs are created. Once the existing 5 Fix PRs are closed or merged, run a new scan to create the remaining 5 Fix PRs. - To address all known vulnerabilities in a single scan, increase Maximum Pull Requests per Branch, or set it to Unlimited. - Setting the limit too low creates a procedural burden; each round of remediation requires a follow-up scan to generate the next batch of Fix PRs. |
   | Upgrade guidance | Sets the preferred upgrade path for remediation recommendations. The default is **Short term preferred**. Options:  - **Short term only:** No Fix PR is created if no short-term upgrade guidance is available. - **Long term only:** No Fix PR is created if no long-term upgrade guidance is available. - **Short term preferred:** Creates a Fix PR using short-term upgrade guidance when available; otherwise uses long-term guidance. - **Long term preferred:** Creates a Fix PR using long-term upgrade guidance when available; otherwise uses short-term guidance. |
4. Run an SCA test.

   Polaris creates Fix PRs for issues that match the policy rules and Fix PR settings for the branch (for components that include dependency upgrades that resolve detected vulnerabilities).

Fix PRs appear in the SCM within a few minutes of the scan completing. Each Fix PR states the vulnerable version being replaced and the recommended upgrade (for example, upgrade from 2.12.1 to 2.25.4).

Fix PR information can also be viewed in Polaris under Components tab > Triage Panel > Activity Logs and Component Details.

Note: When the maximum Fix PR limit is reached and open Fix PRs are merged or closed, Polaris does not automatically create additional Fix PRs for remaining vulnerabilities. This limit is shared with SAST Fix PRs — open Fix PRs of either type count toward the total. Run another SCA test to generate the next batch of Fix PRs.

Review and merge (or close) the pull requests through your normal code review process.
