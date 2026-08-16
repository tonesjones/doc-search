---
title: "Configuring Black Duck Providers"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-black-duck-providers.html"
content_id: "uYHuyN13m9jubIZx9eje7Q"
version: "8.4.0"
section: "Post Installation Configuration"
scraped_at: "2026-08-08T23:46:34.114484+00:00"
---

# Configuring Black Duck Providers

Before you can use Alert, you must configure at least one Black Duck provider by
navigating to the Black Duck providers on the navigation panel. The Black Duck provider
provides the source of messages and notifications that are sent to Alert and are
distributed to channels in a distribution job. You can configure more than one Black
Duck provider to provide notifications to Alert but each Black Duck instance must be
unique.

## Creating a Black Duck provider

The configuration of your Black Duck provider determines how your Alert instance
communicates with your Black Duck server. Configure your provider as follows:

Note: If you are configuring your system with environment variables, the
relevant provider properties are here.

1. Navigate to **Provider > Blackduck > New** and complete the
   following fields.

   | Field | Value | Notes |
   | --- | --- | --- |
   | Enabled | Select the checkbox to enable or disable this configuration |  |
   | Provider configuration | A unique name for this provider configuration |  |
   | URL | The URL of your Black Duck Server |  |
   | API Token | The API Token of the Black Duck User | The user who generates the token requires one of the following roles to ensure connectivity: `Super User`, `System Administrator`, `Global Project Viewer`, `Global Project Administrator`, `Global Project Group Administrator`, `Global Notification Viewer` OR as of version 7.1.2 the API Token belongs to a user with at least one [Watched Project](https://documentation.blackduck.com/bundle/bd-hub/page/InternalProjects/WatchedProjects.html) with notifications enabled. Notifications for any projects the user has notifications enabled on, will be processed. |
   | Timeout | The connection timeout to the Black Duck server in Seconds | Defaults to 300 seconds |
2. Click **Test Configuration** to ensure the connection is valid.
3. Click **Save**.

## Editing or Deleting a Black Duck provider

To edit or delete a configuration, navigate to **Provider > Blackduck**.

To edit a configuration, double click the provider name, or click the edit
column.

To copy a configuration, click the copy icon and ensure that the new provider you
wish to configure has a unique *Provider Configuration* value.
