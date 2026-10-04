---
title: "Create a SAST Fix PR on demand"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-a-sast-fix-pr-on-demand.html"
content_id: "aXnYUdeb8VRmLCrK_sqkQA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.512366+00:00"
content_hash: "5075d8922a0174e89997931a5ba2e38b07d593d47997395cac809af275840f8f"
---

# Create a SAST Fix PR on demand

Select one or more eligible SAST issues on the Issues tab to generate AI-assisted fix pull requests on demand.

For overview, requirements, and settings, see [SAST Fix Pull Requests](../sast-fix-pull-requests.md).

Only Organization Admins, Organization Application Managers, Application Admins, Contributors, Members, and other users with permissions to create and manage SAST Fix PRs can complete these steps.

1. Run a SAST test on an SCM-integrated project.
2. Go to Portfolio, select an application, select a project, and if necessary, select a branch.

   The Issues tab opens.
3. Use the checkboxes on the left side of the table to select one or more SAST issues.
4. Click Create Fix Pull Request for SAST Issues.

   While a single issue is selected, messages may appear when you hover over the Create Fix Pull Request for SAST Issues button.

   | Message | Meaning |
   | --- | --- |
   | This issue does not have a fix suggestion. | This message indicates either: - AI Insight (a feature of Black Duck Assist) is not enabled. - The issue you selected is not eligible. Issues without a fix recommendation from Black Duck Assist (like hardcoded secrets) are not eligible. |
   | A fix pull request has already been created for this issue. | This message indicates a fix pull request was already created for this issue. |

Polaris generates fix recommendations for eligible issues and creates pull requests in your connected SCM. Each pull request includes the issue severity, type, file location, a vulnerability summary, code analysis, a confidence score, and a link to the issue in Polaris.

Note: Polaris does not update an issue's triage history when a SAST Fix PR is created. There is no direct link from the Polaris issue to the generated pull request. Navigate to your SCM to review it.

Review and merge (or close) the pull request through your normal code review process.

Important: Generated fixes are proposed changes, not guaranteed fixes. Review and test all changes before merging into a production branch.
