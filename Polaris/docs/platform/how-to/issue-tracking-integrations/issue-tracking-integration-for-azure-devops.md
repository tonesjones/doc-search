---
title: "Issue tracking integration for Azure DevOps"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integration-for-azure-devops.html"
content_id: "s2KOT1Uv7rdYUbgZSumaoQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:21.186050+00:00"
content_hash: "03e4aec59be50e1f380be500fb5a82c5c0647a942c19d6ec9c2eca3cd235b9f7"
---

# Issue tracking integration for Azure DevOps

This page describes the issue tracking integration for Azure DevOps. Once configured, the integration allows Polaris to create work items in Azure DevOps for issues. You can also configure integration options to close Azure DevOps work items and keep Polaris triage statuses and Azure DevOps work item statuses in sync automatically.

## Prerequisites and technical requirements

The issue tracking integration for Azure DevOps requires:

- An Azure DevOps Services instance.

  Important: The Azure DevOps instance must be routable over the Internet. Closed networks are not supported at this time. Azure DevOps Server is not supported.
- A Polaris Organization Administrator.
- A personal access token (PAT) created in Azure DevOps for authentication between Azure DevOps and Polaris. For full two-way synchronization, the PAT must be created by an Azure DevOps Project Administrator, Project Collection Administrator, Organization Owner, or a member with "View subscriptions" and "Edit subscriptions" permissions.

  Tip: The user associated with the PAT will be listed as the creator of any tickets created using the integration. Consider using a PAT associated with a service account to distinguish the work items Polaris creates.

### Work item fields

Each ticket Polaris creates in Azure DevOps includes the following fields:

- Title: the format of titles varies, depending on how the ticket was created:
  - Tickets for issues you export manually:

    ```
    Polaris - Project '<Polaris project name>' contains issue '<Issue Type>'
    ```
  - Tickets created for policy violations:

    ```
    Polaris - Project '<Polaris project name>' contains issues violating policy '<Policy name>'
    ```
- Description: the format of descriptions varies, depending on how the ticket was created:
  - Tickets for issues you export manually: detailed information about the issue, evidence (DAST issues only), remediation guidance, and helpful links.
  - Tickets created for policy violations: the name of the violated policy, the names of any violated rules, and links you can use to view violating issues in Polaris.
- Created by: The user associated with the personal access token used for the integration.

Important: If other fields are required by your Azure DevOps project, exports will fail.

## Connect Polaris to Azure DevOps

Connecting Polaris to an Azure DevOps organization requires the following steps:

- Create a personal access token
- Add an Azure DevOps instance to Polaris

### Create a personal access token

To create a personal access token (PAT) in Azure DevOps, follow these steps:

1. After you sign in to Azure DevOps, select User settings > Personal Access Tokens.
2. Select **+ New Token**.
3. Enter a Name for the token and select your Organization.
4. Select the token's Expiration date.

   To avoid issues, we recommend the longest setting, which is one year from creation.
5. Under Scopes, select Custom defined.
6. Under Work Items, select Read, write, & manage.
7. Select Create.
8. Copy the token and store it in a safe place.

### Add an Azure DevOps instance to Polaris

Now, connect Polaris to your Azure DevOps instance. Only an Organization Administrator can complete these steps.

1. In Polaris, go to My Organization > Integrations.
2. Select + Add Integration > Azure DevOps.

   [image: tracking org add]
3. Enter the URL for your Azure DevOps instance (for example, `https://dev.azure.com/organization`) in the Azure URL field.
4. Copy and paste your Azure DevOps token into the Access Token field.
5. Select Save.
6. When the Integrations page opens, select Test next to your Azure DevOps URL to verify the connection is working as expected.

   If the test is successful, a green check mark appears next to the Test button.

## Create integration options for Azure DevOps

After you connect Polaris to Azure DevOps, create integration options to synchronize issue statuses and fix-by dates. You can create multiple options for different work item types.

You must have already completed Connect Polaris to Azure DevOps.

Note: Only Organization Administrators can complete these steps.

Important: If you are configuring two-way status synchronization, note the following:

- Synchronizing issue and work item statuses is not supported for bundled tickets (created when more than one issue in Polaris is exported to Azure DevOps in a single step, by a policy action or a manual export). Synchronization only works for individually exported issues with a 1:1 link between a Polaris issue and an Azure DevOps work item. Bundled tickets can still participate in one-way auto-close, which is triggered when all issues linked to the work item are dismissed or absent in Polaris.
- Triage status changes triggered by two-way synchronization bypass triage approval workflows. When a linked ticket's status changes in the issue tracker, Polaris updates the triage status of the linked issue(s) immediately, even if a triage approval workflow is configured for the organization, application, or project. If you require approval for every triage status change, configure one-way synchronization (Polaris to Azure DevOps) instead.

1. In Polaris, go to My Organization > Integrations.
2. Under Integrations, select the Azure DevOps connection you wish to configure.
3. Under Azure Options, select + New.

   The Create Azure Options window opens. Required fields are marked with an asterisk.
4. Enter a name for the option in the Options name field.

   Tip: To avoid confusion, include the Azure DevOps project and work item type the option applies to in the option's name. For example, `Sync <work item type> in <Azure project name>`.
5. In the Specify Azure Workflow dropdown, select the Azure DevOps project this option will export issues to, and then select the work item type this option applies to.

   Each integration option is associated with a specific Azure DevOps project and work item type.
6. (Optional) Set up mappings between issue statuses in Polaris and work item statuses in Azure DevOps with the Status Mapping table.
   1. On the Polaris to Azure tab, select Azure work item statuses using dropdowns in the Azure Status column.

      The Polaris issue statuses include:
      - Not Triaged
      - To Be Fixed
      - Dismissed - Intentional
      - Dismissed - False Positive
      - Dismissed - Other
      - Absent

      Important: Polaris can map to Azure DevOps work item statuses, but does not validate the transitions an Azure DevOps workflow requires. If an Azure DevOps workflow requires an intermediate state before reaching the target state, or requires mandatory fields during a transition that Polaris does not populate, the sync attempt will fail. When this happens, the Polaris triage status reverts to its previous value and an error is logged in the issue's triage history. Configure your Azure DevOps workflows to allow the transitions you need, and ensure that any required custom fields are populated.
   2. Open the Azure to Polaris tab.
   3. Select the add [image: The add icon.] icon to add a row to the table.
   4. Select a work item status with the dropdown in the Azure Status column.

      Note: Azure DevOps work item statuses that have no configured mapping do not trigger any change in Polaris. If a Polaris issue was dismissed as a result of an Azure DevOps work item state change, and you then manually change the Polaris triage status back to an active state (for example, To Be Fixed), the linked work item is automatically reopened.
   5. Select a Polaris issue status with the dropdown in the Polaris Issue Status column.
   6. Repeat the previous steps to set up additional mappings, as required.
7. (Optional) Select Synchronize Polaris Fix-By and Azure Due Date to synchronize issue fix-by dates with Azure DevOps due dates.

   Note: For Agile templates, `Microsoft.VSTS.Scheduling.DueDate` is used. For Scrum, Basic, or CMMI templates, `Microsoft.VSTS.Scheduling.TargetDate` is used. `FinishDate` is also supported. Verify that one of these fields exists in your Azure DevOps project before configuring this mapping.

   An example of a configured integration option for Azure DevOps is shown below.

   [image: An example configured integration option for Azure DevOps.]
8. Select Save.

The new option appears in the list of Azure Options for that integration. You can now enable this option at the project level. See Connect a Polaris project to Azure DevOps for information on enabling integration options for a project.

If necessary, repeat these steps to create options for other work item types.

## Connect a Polaris project to Azure DevOps

After an Organization Administrator establishes the connection between Polaris and Azure DevOps, follow these steps to connect a project to Azure DevOps. Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage project settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Go to Settings > Integrations.
4. Under Issue Tracker, select an Azure DevOps instance from the Instance dropdown menu.

   The Azure Project, Work Item Type, and Azure Options dropdowns appear.

   [image: A screenshot of the options used to connect a project to Azure DevOps.]

   Note: Each Polaris project supports one issue tracking integration. You cannot add an issue tracking integration to a project that already has one configured.
5. Select the Azure Project exported issues will be sent to.
6. Select the Work Item Type Polaris creates when exporting issues.
7. (Optional) Select an integration option from the Azure Options dropdown menu.

   If you created Azure Options (see Create integration options for Azure DevOps), you can select an option here to enable auto-close and triage status sync for this project. When an option with triage status sync mappings is selected, triage status changes in Polaris and work item state changes in Azure DevOps will be kept in sync automatically.
8. Select Validate.
9. Select Save.

### Enable synchronization for individual branches

After you set up integration options, you can configure synchronization settings for individual branches. By default, synchronization is only enabled on the project's default branch.

Before you can enable auto-close at the branch level, you must:

- Create Azure Options for auto-close (see Create integration options for Azure DevOps).
- Connect the project to Azure DevOps and select an Azure Option (see Connect a Polaris project to Azure DevOps).

Enabling synchronization at the branch level allows you to specify which branches Polaris considers when synchronizing issues with work items. This is useful when you want to track issue resolution across multiple branches (such as feature branches or release branches) or exclude certain branches from the synchronization.

Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage branch settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Open the Branches tab.
4. Select the branch you want to configure.

   The Edit Branch window opens.
5. Under Issue Tracker, select Include this branch in issue tracking synchronization (ie. auto-close).

   When this option is enabled, Polaris synchronizes issues with work items in Azure DevOps. If an issue linked to a work item is absent or dismissed across all synchronized branches, Polaris automatically closes the work item.

   Note: This option only appears if the project has an issue tracking integration configured with Azure Options enabled.
6. Select Save.
7. (Optional) Repeat this process for other branches you want to include in issue tracking synchronization.

The branch is now included in issue tracking synchronization.
