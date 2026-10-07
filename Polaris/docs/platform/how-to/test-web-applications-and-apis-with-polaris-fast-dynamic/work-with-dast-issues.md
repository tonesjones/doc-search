---
title: "Work with DAST issues"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/work-with-dast-issues.html"
content_id: "I1K0o~74vvP2lE~9fGn9EQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:21.871030+00:00"
content_hash: "d350d68d83c89537b7921df826be7b725eb815fe52d488bb5184d27558adf4d2"
---

# Work with DAST issues

Manage issues captured in DAST tests, find remediation guidance (including DAST-specific evidence), and view sitemaps for completed tests.

## Work with DAST issues

Issues captured in DAST tests are managed like SAST and SCA issues. You can:

- Triage DAST issues (and manually apply fix-by dates). See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md).
- Assign issue policies to DAST projects to automate actions when issues are captured in tests. See [Issue policies](../create-and-manage-policies/issue-policies.md).
- Export DAST issues to CSV or JSON. See [How to export issues to CSV or JSON](../how-to-export-issues-to-csv-or-json.md).
- After you set up an issue tracking integration, you can export DAST issues to an external issue tracking instance such as Jira, Azure DevOps, or ServiceNow. See [Issue tracking integrations](../issue-tracking-integrations.md) for more information.

  Important: DAST issue export to GitHub Issues or GitLab Issues is not supported.

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

## View sitemaps for completed DAST tests

After a DAST test completes, you can view a sitemap of the target web application or API. The sitemap visualizes all endpoints, links, and resources found by the DAST test, helping you understand test coverage and the structure of the target. Sitemaps are available only for successful DAST tests and are retained for 30 days.

To view the sitemap for a DAST test, follow these steps:

1. Go to Tests.

   Note: Alternatively, go to Portfolio, select an application, select a project, then open the Tests tab.
2. (Optional) Use the Test Types pulldown to filter by DAST tests only.
3. Select the Test ID of a DAST test.
4. Select the Sitemap tab to load the sitemap for the target web application or API. This might take a few minutes.

   [image: Example DAST sitemap showing all endpoints, links and resources found.]

   - The left panel shows all endpoints, links, and resources discovered during the scan.
   - Each node represents an HTTP request sent by the DAST scanner to the target, containing the endpoint, HTTP method, and any query parameters used.
   - Resources discovered during the crawl phase of the scan are shown. Requests sent for each individual checker or attack are not shown.
   - The Request tab shows the full detail of the selected request, including the host, request headers, and request body (if available).
   - The Response tab shows the HTTP response returned from the DAST target, including the server code, response headers, and response body (if one was returned).
5. (Optional) Enter text in the Filter by URL box to filter the nodes in the left panel by the URL of the endpoint.
