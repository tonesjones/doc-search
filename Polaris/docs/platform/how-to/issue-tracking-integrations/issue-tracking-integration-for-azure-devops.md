---
title: "Issue tracking integration for Azure DevOps"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integration-for-azure-devops.html"
content_id: "s2KOT1Uv7rdYUbgZSumaoQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:30.315006+00:00"
content_hash: "1ed7e4391fe287259f282a6ffd803cbd97909ba5d67b439be8c2b0f978214e1f"
---

# Issue tracking integration for Azure DevOps

This page describes the issue tracking integration for Azure DevOps, and what you need to do to connect Polaris to Azure DevOps. Once configured, the issue tracking integration allows Polaris to create tickets in Azure DevOps for issues captured in Polaris.

## Prerequisites and technical requirements

The issue tracking integration for Azure DevOps requires:

- An Azure DevOps Services instance.

  Important: The Azure DevOps instance must be routable over the Internet. Closed networks are not supported at this time. Azure DevOps Server is not supported.
- Only organization administrators can connect Polaris to Azure DevOps.
- Authentication between Azure DevOps and Polaris is managed with a personal access token (PAT) that you create in Azure DevOps. The user associated with the PAT will be listed as the creator of any tickets created using the integration.

  Tip: Consider using a PAT associated with a service account to better-identify the work items Polaris creates.

### Work item fields

Each ticket Polaris creates in Azure DevOps includes the following fields:

- Title: the format of titles vary, depending on how the ticket was created:
  - Tickets for issues you export manually:

    ```
    Polaris - Project '<Polaris project name>' contains issue '<Issue Type>'
    ```
  - Tickets created for policy violations:

    ```
    Polaris - Project '<Polaris project name>' contains issues violating policy '<Policy name>'
    ```
- Description: the format of descriptions vary, depending on how the ticket was created:
  - Tickets for issues you export manually: detailed information about the issue, evidence (DAST issues only), remediation guidance, and helpful links.
  - Tickets created for policy violations: the name of the violated policy, the names of any violated rules, and links you can use to view violating issues in Polaris.
- Created by: The user associated with the personal access token used for the integration.

Important: If other fields are required by your Azure DevOps project, exports will fail.

## Connect Polaris to Azure DevOps

Connecting Polaris to an Azure DevOps organization requires the following steps:

- Create a personal access token
- Add an Azure DevOps instance to Polaris

### Create a personal access token

To create an personal access token (PAT) in Azure DevOps, follow these steps:

1. After you sign in to Azure DevOps, select User settings > Personal Access Tokens.
2. Select **+ New Token**.
3. Enter a Name for the token and select your Organization.
4. Select the token's Expiration date.

   To avoid issues, we recommend the longest setting which is one year from creation.
5. Under Scopes, select Custom defined.
6. Under Work Items, select Read, write, & manage.
7. Select Create.
8. Copy the token and store it in a safe place.

### Add an Azure DevOps instance to Polaris

Now, connect Polaris to your Azure DevOps instance. Only an organization administrator can complete these steps.

1. In Polaris, go to My Organization > Integrations.
2. Select + Add Integration > Azure DevOps.

   [image: tracking org add]
3. Enter the URL for your Azure DevOps instance (for example, `https://dev.azure.com/organization`) in the Azure URL field.
4. Copy and paste your Azure DevOps token into the Access Token field.
5. Select Save.
6. When the Integrations page opens, select Test next to your Azure DevOps URL to verify the connection is working as expected.

   If the test is successful, a green check mark appears next to the Test button.

## Create integration options for Azure DevOps

Optionally, you can set up integration options that allow Polaris to close work items automatically, when the issues linked to the work item are absent (no longer detected in tests) or dismissed (via triage) in Polaris.

To set up integration options (and enable the auto-close behavior), follow these steps:

Note: Only Organization Administrators can complete these steps.

1. In Polaris, go to My Organization > Integrations.
2. Under Integrations, select the Azure DevOps connection you wish to configure.
3. Under Azure Options, select New.

   The Create Azure Options window opens. An example integration option (completed) for Azure DevOps is pictured below.

   [image: An example integration option (completed) for Azure DevOps.]
4. Enter a name for the option in the Options name field.

   Tip: To avoid confusion, we recommend you include the work item type the option applies to (which you'll select later on) in the option's name. For example, `Auto-close <work item type> in Azure DevOps`.
5. Select Automatically close Azure work item when Polaris issue is absent or dismissed (in all configured branches).

   The Specify Azure Process and Azure Status dropdowns appear.
6. In the Specify Azure Process dropdown, select an Azure DevOps project and then select the type of work item Polaris that you want to close automatically.

   This must match the work item type you plan to use when exporting issues from Polaris.
7. In the Azure Status dropdown, select the status that will be assigned to work items when an issue is absent or dismissed in Polaris.

   The available statuses are determined by your Azure DevOps project configuration and the work item type you selected.
8. Select Save.

The new option appears in the list of Azure Options for that integration. You can now enable this option at the project or branch level. See Connect a Polaris project to Azure DevOps for information on enabling auto-close at the project level.

If necessary, repeat these steps to create options for other work item types.

## Connect a Polaris project to Azure DevOps

After an organization administrator establishes the connection between Polaris and Azure DevOps, follow these steps to connect a project to Azure DevOps. Organization administrators, organization application managers, application administrators, application contributors, and other users with permissions to manage project settings can complete these steps.

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

   If you created Azure Options for auto-close (see Create integration options for Azure DevOps), you can select an option here to enable auto-close for this project. When enabled, Polaris will automatically close work items in Azure DevOps when the associated issue becomes absent across all synchronized branches or is dismissed.
8. Select Validate.
9. Select Save.

### Enable auto-close for individual branches

After enabling auto-close for a project, you can configure auto-close settings for individual branches. By default, auto-close is only enabled on the project's default branch. You can enable or disable auto-close for individual branches to control which branches participate in issue tracking synchronization.

Before you can enable auto-close at the branch level, you must:

- Create Azure Options for auto-close (see Create integration options for Azure DevOps).
- Connect the project to Azure DevOps and select an Azure Option (see Connect a Polaris project to Azure DevOps).

Enabling auto-close at the branch level allows you to specify which branches Polaris considers when determining whether to automatically close work items. This is useful when you want to track issue resolution across multiple branches (such as feature branches or release branches) or exclude certain branches from the auto-close behavior.

Organization administrators, organization application managers, application administrators, application contributors, and other users with permissions to manage branch settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Open the Branches tab.
4. Select the branch you want to configure.

   The Edit Branch window opens.
5. Under Issue Tracker, select Include this branch in issue tracking synchronization (ie. auto-close).

   When this option is enabled, Polaris will include this branch when determining whether issues are absent or dismissed across all synchronized branches. If an issue linked to a work item is absent or dismissed across all synchronized branches, Polaris will automatically close the work item.

   Note: This option only appears if the project has an issue tracking integration configured with Azure Options enabled.
6. Select Save.
7. (Optional) Repeat this process for other branches you want to include in issue tracking synchronization.

The branch is now included in issue tracking synchronization. When issues linked to Azure DevOps work items become absent or are dismissed across all synchronized branches (including this one), Polaris will automatically close the associated work items.
