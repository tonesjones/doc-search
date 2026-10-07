---
title: "SAST Fix Pull Requests"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/sast-fix-pull-requests.html"
content_id: "QksShZwdjLe7eeQdBNKpdg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.493634+00:00"
content_hash: "bda971fd37e8e3b647e5c3a719a37541647ad501ead103f6cc4986383b22da56"
---

# SAST Fix Pull Requests

Use AI-Assisted SAST Fix PRs to generate suggested code fixes for eligible SAST findings and submit them to your SCM as pull requests.

SAST Fix Pull Requests use Black Duck Assist to generate a fix recommendation for an eligible SAST finding and create a pull request (or merge request in GitLab) in your connected SCM. You can create SAST Fix PRs in two ways:

- **Automatic:** Create an issue policy with the Create a fix pull/merge request (SAST issues only) action. Polaris automatically creates Fix PRs for eligible issues found after each scan. See [Create SAST Fix PRs with a policy](sast-fix-pull-requests/create-sast-fix-prs-with-a-policy.md).
- **On-demand:** Select one or more eligible issues on the Issues tab and click Create Fix Pull Request for SAST Issues. See [Create a SAST Fix PR on demand](sast-fix-pull-requests/create-a-sast-fix-pr-on-demand.md).

## Requirements

- A supported SCM integration (GitHub, GitLab, Azure DevOps, or Bitbucket) connected to Polaris. Source uploads and CLI-based projects are not supported.
- A SAST entitlement, or a bundled test type that includes SAST.
- CI scans run in Remote or Hybrid mode via Bridge. Local scans do not support SAST Fix PR creation.
- Black Duck Assist (AI Insight) must be enabled to create SAST Fix PRs from the Polaris user interface. See Enable Black Duck Assist (AI Insight).
- For on-demand creation, the Create SAST Fix PR permission.
- For automatic Fix PRs, an issue policy with the Create a fix pull/merge request (SAST issues only) action assigned to your organization, application, project, or branch.
- An access token created by an **Organization Owner** in your SCM organization, or by a user with the "Manage organization webhooks" permission.

Important: Hybrid mode requires uploading source code to Polaris. Ensure your organization's policies allow this before you run Hybrid mode scans to generate Fix PRs.

Important: Bridge cannot create pull requests with an access token that lacks organization-level permissions in your SCM. Although other users may be able to select the required scopes when creating a token, the token will not work without the permissions required to manage organization webhooks.

## Security considerations

Polaris sends eligible SAST issue data and relevant source code context to a large language model (LLM) to generate suggested code fixes and create pull requests. The scope of data sharing is limited to what is necessary for fix generation, and may include:

- SAST issue identifiers and metadata
- Issue type, checker/rule information, and CWE data
- File paths, line numbers, and event trace details
- Relevant source files from the scanned revision
- Issue descriptions and remediation context from the analysis tool

Using the AI-assisted Fix PR feature constitutes opting-in and accepting this exchange. To opt out, stop using AI-Assisted Fix PR generation. Customers are responsible for securing their environment, protecting configured credentials, and reviewing all generated code changes before merge. Ensure that your use of this capability complies with your organization's internal security, privacy, and regulatory requirements. Future versions of this capability may have different security considerations.

Important: Generated fixes are proposed changes, not guaranteed fixes. Review and test all changes before merging into a production branch.

## Issue eligibility

A SAST Fix PR can only be created for issues that Black Duck Assist can generate a fix recommendation for. Issues without a fix recommendation (like hardcoded secrets) are not eligible. Additional eligibility criteria are configured in Fix PR settings (see Fix PR settings).

A SAST Fix PR will not be created in the following cases:

- The issue does not have a fix recommendation.
- The issue type is on the SAST Vulnerabilities Exclusion List.
- The scan was triggered by a pull or merge request (automatic Fix PRs are skipped for PR scans).
- The number of open SAST and SCA Fix PRs created by Polaris on the branch has reached the configured limit (see Fix PR settings).
- The scan was run in Local mode.

## Fix PR settings

Fix PR settings can be customized at the organization, application, project, or branch level. Navigate to the appropriate level and click Edit next to Fix Pull Requests in the Integrations settings:

- **Organization**: My Organization > Integrations
- **Application**: Portfolio > select an application > Settings > Integrations
- **Project**: Portfolio > select an application > select a project > Settings > Integrations
- **Branch**: Portfolio > select an application > select a project > Branches tab > select a branch

The following settings affect SAST Fix PRs:

Table 1. SAST Fix PR settings

| Setting | Description |
| --- | --- |
| Maximum number of Fix PRs per branch | The maximum number of Fix PRs (SAST and SCA combined) that can be open on a branch at a time. The default is 5, but this can be adjusted, as required. |
| SAST Vulnerabilities Exclusion List | A list of SAST issue types for which Fix PRs will not be created. Click the Select issue types to exclude... dropdown to add or remove issue types. Use the Search field to find specific types. |

## Fix PR settings inheritance

Organization-level Fix PR settings are applied to all applications, projects, and branches by default, but can be overridden. Settings at lower levels take precedence:

- Application settings override organization-level settings for that application.
- Project settings override organization and application-level settings for that project.
- Branch settings override organization, application, and project settings for that branch.

When Inherited is shown at the top of the Fix Pull Requests settings panel, the settings at that level come from a higher level. When settings have been customized at a level, Modified is shown instead. Select Reset to return customized settings to Inherited.

**Related tasks**  

- Create a SAST Fix PR on demand
- Create SAST Fix PRs with a policy
