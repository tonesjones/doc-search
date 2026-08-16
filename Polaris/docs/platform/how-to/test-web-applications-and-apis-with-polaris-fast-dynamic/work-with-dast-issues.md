---
title: "Work with DAST issues"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/work-with-dast-issues.html"
content_id: "I1K0o~74vvP2lE~9fGn9EQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:42.085639+00:00"
content_hash: "505ad38c01aecefdc2b4ed6b92fee8f2e0fd5553e2aade083b98412e65bf8923"
---

# Work with DAST issues

Manage issues captured in DAST tests and find remediation guidance, including
DAST-specific evidence.

## Work with DAST issues

Issues captured in DAST tests are managed like SAST and SCA issues. You can:

- Triage DAST issues (and manually apply fix-by dates). See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md).
- Assign issue policies to DAST projects to automate actions when issues are captured in tests. See [Issue policies](../create-and-manage-policies/issue-policies.md).
- Export DAST issues to CSV or JSON. See [How to export issues to CSV or JSON](../how-to-export-issues-to-csv-or-json.md).
- After you set up a issue tracking integration, you can export DAST issues to Azure DevOps or Jira. See [Issue tracking integrations](../issue-tracking-integrations.md) for more information.

## Find DAST remediation guidance

After you test a DAST project, you can find remediation guidance (along with evidence) for issues captured in DAST tests in the Issue Details panel. To open the Issue Details panel, follow these steps:

1. Go to Portfolio, open an application, open a DAST project, and open the Issues tab.

   Tip: Remember, DAST issues are only available in DAST projects.
2. Select an Issue Type.

   The Issue Details panel opens.
3. Select the Evidence tab to view the following DAST-specific evidence:

   - Location: The API endpoint for which the issue was detected
   - Payload
   - Target
   - Request body
   - Response body
