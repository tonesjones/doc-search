---
title: "Analysis Tools"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/analysis-tools.html"
content_id: "Y69G1Wx~YVrhXkw03U2hzw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:29.822062+00:00"
content_hash: "481125063b35eb44d19b82999e2b02a598fd7ed66b8d396a0c0b10e4d3e9cbf3"
---

# Analysis Tools

Click the Integrations icon in the navigation bar and select Analysis Tools to open the
Analysis Tools page.

[image: image]

Use the Search field to search for a specific tool.

## Configuring an Analysis Tool

**To configure an analysis tool:**

1. Click the Integrations icon in the navigation bar and select Analysis Tools to
   open the Analysis Tools page.
2. Click the Set Up button for the tool you want to configure.

   Not all tools are
   configurable.

   [image: image]
3. Click Add Connection.

   [image: image]

   1. Add an API token with "API Security Audit" rights in the API Token
      field.

      To test the connection, click the Test Connection
      button.
   2. Select sharing options with users or user groups.
   3. Select permissions.
4. Click Add Options.

   [image: image]
5. Enter a name in the Options Name field and select which options to include.
6. Click Save Options.

   Note that you can edit existing options.
7. Select Schedules from the upper menu.
8. Click Add Schedule.

   [image: image]
9. Add projects.

   [image: image]

## Migrating Existing Tools to SRM

SRM’s centralized configuration functionality allows Software Risk Manager to act as
a hub for interacting with tool connectors. For Code Dx users migrating to Software
Risk Manager, existing tool connectors can be converted to take full advantage of
SRM’s centralized configuration. (In an upcoming release of SRM, legacy tool
connectors will be converted automatically, consolidating common information, such
as connection URLs and credentials, into more-easily-managed shared entities.)

To migrate legacy tool connectors (Code Dx) to take advantage of centralized
configuration, SRM provides two URLs that an administrator can use to perform the conversion:

- The first URL performs a "dry run" of the conversion, providing a report of
  all the decisions and consolidations that will be made during the actual
  conversion process.
- The second URL performs the conversion.

To perform the dry run and see a text-based report, log in as an admin and enter the
following into your browser: `<SRM Base
URL>/x/integrations/tool-connector/migration/dry-run`. You can also use
your HTTP client-of-choice to send a `GET` request to that URL to
obtain the report.

To trigger the actual conversion, use `<SRM Base
URL>/x/integrations/tool-connector/migration/commit-run`. This URL
responds with a `204 No Content` upon success.

Warning: Running the conversion is irreversible.
Making a backup of your database prior to performing this action is highly
recommended.
