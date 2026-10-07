---
title: "Alert Issue Property Indexer"
source_url: "https://docs.blackduck.com/r/alert/8.4.1/black-duck-alert-user-guide/alert-issue-property-indexer.html"
content_id: "8tspIXWhN71Be4o~QeFCtg"
version: "8.4.1"
section: "Installation References"
scraped_at: "2026-10-04T23:29:44.410646+00:00"
content_hash: "8f02257ea169af8eb79050e2160ad043049eb93fcdede075b1f724d8aef8e68a"
---

# Alert Issue Property Indexer

**Compatible with:** Jira Data Center and Jira Cloud

**Atlassian Marketplace:** [Alert Issue Property Indexer](https://marketplace.atlassian.com/apps/1235608/alert-issue-property-indexer)

## Overview

The Alert Issue Property Indexer is a **required dependency** for any Jira instance integrated with [Black Duck Alert](https://github.com/blackducksoftware/blackduck-alert).

Without this app installed, Black Duck Alert cannot reliably locate Jira tickets it previously created. As a result, Alert may lose track of existing issues, causing duplicate tickets to be created, existing tickets to remain out of date, and tickets to remain open after vulnerabilities or policy violations have been resolved.

The Alert Issue Property Indexer enables Jira to efficiently search the issue properties that Alert uses to identify and manage its tickets.

## Do I Need This Plugin?

You need the Alert Issue Property Indexer if:

- You use Black Duck Alert with Jira.
- Alert creates or updates Jira issues.
- You want Alert to recognise existing tickets and avoid creating duplicates.
- You want Alert to update or close previously created tickets when findings change status.

You do not need this plugin if:

- You are not using Jira.
- You are not integrating Jira with Black Duck Alert.
- Alert does not create Jira issues in your environment.

## Terminology

Throughout this document:

- A **finding** is information received from Black Duck, such as a vulnerability or policy violation.
- A **notification** is the Alert message that describes a finding.
- A **ticket** refers to the Jira issue created or managed by Alert.

## Background: What Are Jira Issue Properties?

Jira allows applications to attach arbitrary metadata to issues in the form of **issue properties**. These are key-value pairs stored directly on a Jira issue and are separate from standard Jira fields such as Summary, Description, Priority, or Status.

Issue properties are not displayed in the Jira user interface by default, but they can be accessed through the Jira REST API.

Black Duck Alert uses issue properties to tag every Jira ticket it creates. These tags contain information identifying the specific finding represented by the ticket, such as:

- The Black Duck instance that generated the finding
- The project and project version
- The affected component and component version
- The notification category

This metadata allows Alert to determine whether a Jira ticket already exists for a specific finding.

## Why the Indexer Is Required

Jira does not automatically index issue properties for efficient searching. Without indexing, searching for issues by multiple property values can become resource intensive and slow, particularly in larger Jira environments.

The Alert Issue Property Indexer solves this problem by registering an issue property index configuration with Jira. Jira then automatically maintains searchable indexes for the specific issue property fields written by Alert.

This makes it possible for Alert to quickly locate previously created tickets regardless of the size of the Jira instance.

The plugin does not perform any business processing of Alert notifications. Its sole purpose is to register an issue property index configuration with Jira so that Jira can maintain searchable indexes for Alert-managed issue properties.

Once installed, it operates silently in the background and requires no configuration or ongoing maintenance.

## How Black Duck Alert Uses Issue Properties

When Alert creates a Jira ticket, it immediately writes a structured property to the issue under the property key:

```
com-blackduck-integration-alert
```

This property records information about the finding that the ticket represents, including the originating Black Duck instance, project, project version, component, component version, and notification category.

Later, when Alert receives a new notification, it needs to determine whether a Jira ticket already exists for that same finding.

Using the indexed issue property values, Alert searches Jira for matching tickets.

If a matching ticket is found, Alert performs the appropriate action, such as:

- Adding a comment
- Updating ticket content
- Transitioning the ticket to a closed state

If no matching ticket is found, Alert follows the behaviour configured for that notification type, which most commonly involves creating a new Jira ticket.

Fast property lookups are the core capability that the Alert Issue Property Indexer enables.

## Issue Property Field Reference

Alert stores a JSON object under the property key `com-blackduck-integration-alert`.

Table 1. Issue property fields

| Field | Type | Description |
| --- | --- | --- |
| `provider` | string | Display name of the originating provider. Example: `"Black Duck"` |
| `providerUrl` | string | Base URL of the originating Black Duck instance. |
| `topicName` | string | Top-level entity label. Currently `Project`. |
| `topicValue` | string | UUID of the Black Duck project. |
| `subTopicName` | string | Secondary entity label. Currently `Project Version`. |
| `subTopicValue` | string | UUID of the Black Duck project version. |
| `category` | string | Notification category, such as `Vulnerability` or `Policy Violation`. |
| `componentName` | string | Component label. Currently `Component`. |
| `componentValue` | string | Name of the affected component. |
| `subComponentName` | string | Component version label. Currently `Component Version`. |
| `subComponentValue` | string | Version of the affected component. |
| `additionalKey` | string | Optional supplemental identifier used by certain notification types. |

## Viewing Issue Properties Through the Jira REST API

Issue properties are not shown in the Jira user interface but can be inspected using the Jira REST API.

This can be useful when troubleshooting Alert integrations or verifying that Alert correctly tagged a Jira issue.

## Step 1: List All Property Keys on an Issue

To view all property keys associated with a Jira issue:

```
GET https://<YOUR_JIRA_URL>/rest/api/2/issue/<ISSUE_KEY>/properties/
```

Example:

```
GET https://blackduck.internal.jira.com/rest/api/2/issue/TEST-1234/properties/
```

Example response:

```
{
  "keys": [
    {
      "self": "https://blackduck.internal.jira.com/rest/api/2/issue/9876/properties/com-blackduck-integration-alert",
      "key": "com-blackduck-integration-alert"
    }
  ]
}
```

The presence of the `com-blackduck-integration-alert` property confirms that Alert created and tagged the ticket.

## Step 2: Retrieve the Property Value

To view the complete property contents:

```
GET https://<YOUR_JIRA_URL>/rest/api/2/issue/<ISSUE_KEY>/properties/com-blackduck-integration-alert
```

Example:

```
GET https://blackduck.internal.jira.com/rest/api/2/issue/TEST-1234/properties/com-blackduck-integration-alert
```

Example response:

```
{
  "key": "com-blackduck-integration-alert",
  "value": {
    "provider": "Black Duck",
    "providerUrl": "https://blackduck.internal.sca.com/",
    "topicName": "Project",
    "topicValue": "8fb604b6-24dd-4a82-bf36-d9df0a35e006",
    "subTopicName": "Project Version",
    "subTopicValue": "d39370cf-4d73-4cac-9569-e190777b9578",
    "category": "Vulnerability",
    "componentName": "Component",
    "componentValue": "Apache HTTPComponents Core",
    "subComponentName": "Component Version",
    "subComponentValue": "4.2.5"
  }
}
```

This example indicates that the Jira ticket represents a vulnerability associated with Apache HTTPComponents Core version 4.2.5 within a specific Black Duck project version.

## Installing the Alert Issue Property Indexer

The app is available through the Atlassian Marketplace and can be installed directly from within Jira.

Note: You must have Jira administrator permissions to install apps. If you do not have administrator access, see the non-administrator installation request instructions below.

## Installation Steps for Administrators

1. Log in to Jira as an administrator.
2. Open the Apps menu and select Explore new apps.
3. Search for Alert Issue Property Indexer.
4. Open the app details page.
5. Select Get app.
6. Wait for the installation to complete.

No additional configuration is required.

## Requesting Installation as a Non-Administrator

If you are not a Jira administrator:

1. Locate the app through the Atlassian Marketplace or the Explore new apps screen.
2. Select Get it now.
3. Select Submit request.
4. Your Jira administrator will receive a request to review and install the app.

## Verifying Installation

After installation:

1. Navigate to Apps > Manage apps.
2. Confirm that Alert Issue Property Indexer is installed and enabled.
3. Create or update a Jira issue through Black Duck Alert.
4. Use the Jira REST API examples in this document to verify that the issue contains the `com-blackduck-integration-alert` property.
5. Confirm that Alert can recognise and update previously created tickets as expected.

## After Installation

Once the Alert Issue Property Indexer is installed, no further action is required.

After installation, Jira automatically maintains indexes for the Alert issue property fields defined by the plugin. Once Jira has completed indexing, Alert can use those indexes to efficiently locate both newly created and existing tickets.

The app operates entirely in the background and remains transparent to normal Jira usage.

## Additional Resources

- [Alert Issue Property Indexer on the Atlassian Marketplace](https://marketplace.atlassian.com/apps/1235608/alert-issue-property-indexer)
- [Black Duck Alert on GitHub](https://github.com/blackducksoftware/blackduck-alert)
- [Black Duck Software](https://www.blackduck.com/)

Note: This plugin is an infrastructure component used by Black Duck Alert. It provides issue property indexing capabilities only and does not modify Jira workflows, projects, permissions, or issue content.
