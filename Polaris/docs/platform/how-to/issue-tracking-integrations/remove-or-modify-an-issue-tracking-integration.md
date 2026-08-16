---
title: "Remove or modify an issue tracking integration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/remove-or-modify-an-issue-tracking-integration.html"
content_id: "LWARxI2LZ8nlW6_EbmMQOg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:32.940305+00:00"
content_hash: "9646f752f92ee1ad351d184aad1738d9371cc597a7172de7d41d45230eca6f41"
---

# Remove or modify an issue tracking integration

Important: When you remove or update a project's issue tracking integration, existing ticket links are preserved. You can manually change or remove ticket links using the triage panel. Any synchronization with external issue trackers stops. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) for more information.

## Remove or update a project's issue tracking integration

To change a Polaris project's issue tracking integration, follow these steps:

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Go to Settings > Integrations.
4. Under Issue Tracker, select Delete.
5. (Optional) Set up the project's issue tracking integration, select Validate, and select Save.

## Remove an Azure DevOps or Jira instance

To remove an Azure DevOps or Jira instance from Polaris, follow these steps:

Note: Only organization administrators can complete these steps.

1. Go to My Organization > Integrations.
2. Select the Remove [image: tracking org delete icon] icon next to the instance you wish to remove.

   A confirmation appears.

   CAUTION:

   When you remove an Azure DevOps or Jira instance, any projects that use the instance are disconnected from it. This action cannot be undone, and any connections that are affected can only be restored manually (one project at a time).
3. Select OK.
