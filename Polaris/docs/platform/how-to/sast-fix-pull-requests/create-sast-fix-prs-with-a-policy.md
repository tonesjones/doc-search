---
title: "Create SAST Fix PRs with a policy"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-sast-fix-prs-with-a-policy.html"
content_id: "zJtPP_Phqbf5HoAIrbMLMQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.538534+00:00"
content_hash: "212d45a2fe751b93e4d301559525aa52ba63df1d57fef0e5ddc4179e97669aa4"
---

# Create SAST Fix PRs with a policy

Use an issue policy to automatically create SAST Fix PRs for eligible findings after each scan.

For overview, requirements, and settings, see [SAST Fix Pull Requests](../sast-fix-pull-requests.md).

1. Create an issue policy that includes the Create a fix pull/merge request (SAST issues only) action.

   See [Issue policies](../create-and-manage-policies/issue-policies.md) for more information. An issue policy (that includes the fix pull/merge request action) defines the conditions under which Polaris creates SAST fix pull requests. Policies are rule-based and can be scoped by security risk level.
2. Assign the issue policy to your organization, an application, a project, or a branch.
   - Organization Admins can add the issue policy to your organization's default policies. See [Change your organization's default policies](../create-and-manage-policies/manage-your-default-policies/change-your-organization-s-default-policies.md) for more information.
   - Users with permissions to manage application, project, or branch settings can assign the policy to specific applications, projects, or branches. See [Change the policies assigned to applications, projects, and branches](../create-and-manage-policies/change-the-policies-assigned-to-applications-projects-and-branches.md) for more information.
3. (Optional) Review and update SAST Fix PR settings.

   Fix PR settings can be customized at the organization, application, project, or branch level.
   - **Organization:** My Organization > Integrations
   - **Application:** Portfolio > select an application > Settings > Integrations
   - **Project:** Portfolio > select an application > select a project > Settings > Integrations
   - **Branch:** Portfolio > select an application > select a project > Branches tab > select a branch

   Navigate to the appropriate level and click the Edit icon next to Fix Pull Request Settings. Settings that affect SAST Fix PRs include:

   Table 1. SAST Fix PR settings

   | Setting | Description |
   | --- | --- |
   | Maximum pull requests per branch | The maximum number of Fix PRs created by Polaris (SAST and SCA combined) that can be open on a branch at a time. The default is 5, but can be edited to suit project requirements.  Important: When the maximum PR limit is reached and open PRs are merged or closed, Polaris does not automatically create additional Fix PRs for remaining vulnerabilities. Run a new test to create the next batch of Fix PRs.  Consider the following when configuring this value:  - If the limit is set to 5 and 10 vulnerabilities are detected, only 5 Fix PRs are created. Once the existing 5 Fix PRs are closed or merged, run a new scan to create the remaining 5 Fix PRs. - To address all known vulnerabilities in a single scan, increase Maximum Pull Requests per Branch, or set it to Unlimited. - Setting the limit too low creates a procedural burden; each round of remediation requires a follow-up scan to generate the next batch of Fix PRs. |
   | SAST Vulnerabilities Exclusion List | A list of SAST issue types for which Fix PRs will not be created. Click the Select issue types to exclude... dropdown to add or remove issue types. Use the Search field to find specific types. |
4. Run a SAST test.

   After the scan completes, Polaris evaluates each SAST finding against the policy rules. Eligible issues that match the policy rules trigger Fix PR creation. Ineligible issues are skipped silently.

   Important: If running the test with Bridge, the scan must use Remote or Hybrid mode. SAST Fix PRs are not created for Local mode scans. SAST Fix PRs are not created for scans triggered by a pull or merge request. If the triggering event is a PR scan, the action is skipped.

Fix PRs for eligible issues appear in your connected SCM within a few minutes of the scan completing. Each pull request includes the issue severity, type, and file location, a vulnerability summary, code analysis, and a link back to the issue in Polaris.

Note: When the maximum Fix PR limit is reached and open Fix PRs are merged or closed, Polaris does not automatically create additional Fix PRs for remaining vulnerabilities. Run another SAST test to generate the next batch of Fix PRs.

Review and merge (or close) the pull requests through your normal code review process.
