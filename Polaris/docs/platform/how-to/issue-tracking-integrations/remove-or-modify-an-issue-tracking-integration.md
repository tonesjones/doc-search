---
title: "Remove or modify an issue tracking integration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/remove-or-modify-an-issue-tracking-integration.html"
content_id: "LWARxI2LZ8nlW6_EbmMQOg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:21.366127+00:00"
content_hash: "bbf5b7a92d3bc52688c593e075aafb7acce54efa2cb73a0f7d90bef2b155137e"
---

# Remove or modify an issue tracking integration

Important: When you remove or update a project's issue tracking integration, existing ticket links are preserved. You can manually change or remove ticket links using the triage panel. Any synchronization with external issue trackers stops. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.

## Remove or update a project's issue tracking integration

To change a Polaris project's issue tracking integration, follow these steps:

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Go to Settings > Integrations.
4. Under the Issue Tracker heading, click the pencil [image: A small user interface icon denoted by a pencil.] icon to enable the issue tracking editing options.

   - For Azure DevOps, Jira, or ServiceNow integrations, select the No issue tracker radio button to disable issue tracking, or select the Delete button under Use a globally configured issue tracker to remove the issue tracking integration for this project.
   - For GitHub Issues or GitLab Issues integrations, select the No issue tracker radio button to disable issue tracking.

     Note: To remove an SCM integration, see Remove an SCM integration. When an SCM integration is removed, the Issue Tracker option will automatically change to No issue tracker.
5. (Optional) Set up the project's issue tracking integration, select Validate, and select Save.

## Remove an issue tracking instance

To remove an external issue tracking instance from Polaris, follow these steps:

Note: Only Organization Administrators can complete these steps.

1. Go to My Organization > Integrations.
2. Select the Remove [image: tracking org delete icon] icon next to the instance you wish to remove.

   A confirmation appears.

   CAUTION:

   When you remove an issue tracking instance, any projects that use the instance are disconnected from it. This action cannot be undone, and any connections that are affected can only be restored manually (one project at a time).
3. Select OK.
