---
title: "Issue tracking integration for ServiceNow"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integration-for-servicenow.html"
content_id: "nanrcSOSMsnk~SG5mpynFA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.860012+00:00"
content_hash: "e919c1cf5c5600ec94de70c407254fd29286786db2780ed037c61fb776d2b7b1"
---

# Issue tracking integration for ServiceNow

Connect Polaris to ServiceNow to export issues captured in DAST, SAST, and SCA tests as ServiceNow incident tickets.

## Prerequisites and technical requirements

The issue tracking integration for ServiceNow requires:

- A ServiceNow instance and an active subscription.
- A Polaris Organization Administrator who is also a ServiceNow System Administrator to configure the integration.
- A REST API key created in ServiceNow for authentication.

Important: If your ServiceNow instance uses mandatory custom fields on incidents, issue export from Polaris will fail. Work with your ServiceNow System Administrator to make any mandatory custom fields optional before configuring this integration.

## Incident fields and attributes

Each ticket Polaris creates in ServiceNow includes the following fields:

- Short Description: the format varies, depending on how the ticket was created:
  - Tickets for individual issues you export manually (single export):

    ```
    Polaris - '<Application name>' / '<Project name>' / '<Branch name>' contains issue '<Issue type>'
    ```
  - Tickets created for policy violations:

    ```
    Polaris - '<Application name>' / '<Project name>' / '<Branch name>' issues violating policy '<Policy name>'
    ```
  - Tickets for multiple issues you export manually (bulk export):

    ```
    Polaris - '<Application name>' / '<Project name>' / '<Branch name>' vulnerabilities ('<Number of issues>' issues)
    ```
- Description: The format of the description includes the Short Description content and a PDF attachment titled Polaris-Issue-Description. The following information is included in the attached PDF:
  - Tickets for issues you export manually: detailed information about the issue, remediation guidance, and a link to the issue in Polaris.
  - Tickets created for policy violations: the name of the violated policy, the names of any violated rules, and links you can use to view violating issues in Polaris.

## Connect Polaris to ServiceNow

Connecting Polaris to a ServiceNow instance requires the following steps:

1. Create an inbound authentication profile
2. Create REST API policies
3. Create an API key
4. Add a ServiceNow instance to Polaris

### Create an inbound authentication profile

To create an inbound authentication profile in ServiceNow, follow these steps:

1. After you sign in to ServiceNow, select All > System Web Services > API Access Policies > Inbound Authentication Profile.

   [image: A screenshot of the user navigation path on the ServiceNow home page.]
2. Select New.
3. Select Create API Key authentication profiles.
4. Enter a Name for the authentication profile.
5. Select the Unlock Auth Parameter button.
6. Select the Lookup using list button next to the Select target record field.
7. Select the Auth Parameter x-sn-apiKey :: Auth Header.

   [image: A screenshot of the inbound profile UI, including a pop-up window with selectable Auth Parameters.]
8. Select Submit.

### Create REST API policies

To create the REST API access policies in ServiceNow, follow these steps:

1. Select All > System Web Services > API Access Policies > REST API Access Policies.
2. Select New.
3. Enter a Name for the API access policy.
4. Select Table API from the REST API dropdown menu.
5. Under the Inbound authentication profile table, double-click the Insert a new row... field and enter the name of the previously-created inbound authentication profile. Click the green check mark to confirm this profile.

   An example API access policy is pictured below.

   [image: A screenshot of a completed API policy form.]
6. Select Submit.
7. Repeat steps 2-6 to create an Aggregator API access policy, selecting Aggregator API from the REST API dropdown menu in step 4.
8. Repeat steps 2-6 to create an Attachment API access policy, selecting Attachment API from the REST API dropdown menu in step 4.

### Create an API key

To create an API key in ServiceNow, follow these steps:

1. After you sign in to ServiceNow, select All > System Web Services > API Access Policies > REST API Key.
2. Select New.
3. Enter a Name and select a User from the dropdown menu.

   Important: The User field should be assigned to a System Administrator that also has the Organization Admin role in Polaris.
4. Select Submit.
5. Click the Preview Global button to view the API key.

   [image: A screenshot of a popover providing information for the API record, including a masked API key.]
6. Copy the key and store it in a safe place.

### Add a ServiceNow instance to Polaris

To connect Polaris to your ServiceNow instance, follow these steps:

Note: Only Organization Administrators can complete these steps.

1. In Polaris, go to My Organization > Integrations.
2. Select + Add Integration > ServiceNow.

   [image: A screenshot of the My Organization page with a dropdown menu of supported integrations.]
3. Enter the URL for your ServiceNow instance (for example, `https://devXXXXX.service-now.com`, where `XXXXX` is the unique ID of your instance) in the ServiceNow URL field.
4. Copy and paste your ServiceNow API key into the Access Token field.
5. Select Save.
6. When the Integrations page refreshes, select Test next to your ServiceNow URL to verify the connection is working as expected.

   If the test is successful, a green check mark appears next to the Test button.

## Create integration options for ServiceNow

Optionally, you can set up integration options that allow Polaris to change the status of tickets automatically when the issues linked to the ticket are absent (no longer detected in tests) or dismissed (via triage) in Polaris.

You must have already completed Connect Polaris to ServiceNow.

Note: Only Organization Administrators can complete these steps.

Important: If you are configuring two-way status synchronization, note the following:

- Synchronizing statuses is not supported for bundled tickets (created when more than one issue in Polaris is exported to ServiceNow in a single step, by a policy action or a manual export). Synchronization only works for individually exported issues with a 1:1 link between a Polaris issue and a ServiceNow incident ticket. Bundled tickets can still participate in one-way auto-close, which is triggered when all issues linked to the ticket are dismissed or absent in Polaris.
- Triage status changes triggered by two-way synchronization bypass triage approval workflows. When a linked ticket's status changes in the issue tracker, Polaris updates the triage status of the linked issue(s) immediately, even if a triage approval workflow is configured for the organization, application, or project. If you require approval for every triage status change, configure one-way synchronization (Polaris to ServiceNow) instead.

1. In Polaris, go to My Organization > Integrations.
2. Under Integrations, select the ServiceNow instance you wish to configure.
3. Under ServiceNow Options, select + New.

   The Edit ServiceNow Options window opens. An example of a configured integration option for ServiceNow is shown below.

   [image: An example configured integration option for ServiceNow.]
4. Enter a name for the option in the Options name field.
5. Select the task type from the Specify Task Type dropdown.

   Note: Only the Incident task type is supported at this time.
6. In the Status Mapping form, select the statuses that are assigned to ServiceNow tickets when an issue is absent or dismissed in Polaris.

   Alternatively, select the ServiceNow to Polaris button to assign statuses to issues in Polaris when the ticket status in ServiceNow changes.

   Important: At least one status mapping must be configured to save the integration option. However, the ServiceNow Resolution selection is optional.
7. (Optional) Select Synchronize Polaris Fix-By and ServiceNow Due Date.
8. Select Save.

The new option now appears in the list of ServiceNow Options for that instance. You can now enable this option at the project or branch level. See Connect a Polaris project to ServiceNow for information on enabling options at the project level. See Enable issue tracking for individual branches for information on enabling options at the branch level.

Note: When a triage status in Polaris changes, whether the change originates in Polaris or is triggered by a change in a synchronized ticket, the change is recorded in the triage history. Synchronization errors (for example, mismatched status mapping or an expired API key) are also recorded in the triage history. The cause of the error is included in the entry description. See [Ways to triage issues in Polaris](../ways-to-triage-issues-in-polaris.md) and View issue history for more information.

## Connect a Polaris project to ServiceNow

After an Organization Administrator establishes the connection between Polaris and ServiceNow, follow these steps to connect a project to ServiceNow.

Note: Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage project settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Go to Settings > Integrations.
4. Under Issue Tracker, select a ServiceNow instance from the Instance dropdown menu.

   The ServiceNow Task Type and ServiceNow Options dropdowns appear.

   [image: A screenshot of the options used to connect a project to ServiceNow.]

   Note: Each Polaris project supports one issue tracking instance. You cannot add an issue tracking instance to a project that already has one configured.
5. Select the ServiceNow Task Type Polaris creates when exporting issues.
6. (Optional) Select an integration option from the ServiceNow Options dropdown menu.

   If you created ServiceNow Options (see Create integration options for ServiceNow), you can select an option here to enable status mapping (including auto-close) for this project. When enabled, Polaris automatically assigns a status to tickets in ServiceNow based on the status of the issue in Polaris.
7. Select Validate.

   A green check mark with the message "Configuration is valid" appears next to the Validate button.
8. Select Save.

### Enable issue tracking for individual branches

After connecting a project in Polaris to an issue tracking instance, you can configure issue tracking synchronization (including auto-close) for individual branches. By default, issue tracking synchronization is only enabled on the project's default branch. You can enable or disable this setting for individual branches to control which branches participate in issue tracking synchronization.

Before you can enable issue tracking synchronization at the branch level, you must:

- Create a ServiceNow Option for the ServiceNow issue tracking integration (see Create integration options for ServiceNow).
- Connect the project to the ServiceNow issue tracking instance and select a ServiceNow Option (see Connect a Polaris project to ServiceNow).

Enabling issue tracking synchronization at the branch level allows you to specify which branches Polaris includes when determining whether to automatically change the ticket status or close a ticket. This is useful when you want to track issue resolution across multiple branches (such as feature branches or release branches) or exclude certain branches from the auto-close behavior.

Note: Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage branch settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Select the Branches tab.
4. Select the branch you want to configure.

   The Edit Branch window opens.
5. Under Issue Tracker, select Include this branch in issue tracking synchronization (i.e. auto-close).

   When this option is enabled, Polaris includes this branch when determining whether issues are absent or dismissed across all synchronized branches.

   Note: For policy violations, the export only triggers on the default branch.
6. Select Save.
7. (Optional) Repeat this process for other branches you want to include in issue tracking synchronization.

The branch is now included in issue tracking synchronization. When issues linked to ServiceNow tickets become absent or are dismissed across all synchronized branches, Polaris automatically closes the associated ticket.

Note: If an auto-closed issue reappears in a subsequent scan, Polaris does not reopen the closed incident. If the issue is flagged by a policy, the policy creates a new ServiceNow incident automatically. Otherwise, you must manually export or link a new ticket to the issue. See [Export an issue to an issue tracking instance](export-an-issue-to-azure-devops-or-jira.md) for more information.
