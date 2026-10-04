---
title: "Issue tracking integration for Jira Data Center"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integration-for-jira-data-center.html"
content_id: "WGy6nGS45SKWolXXjatgBw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.776505+00:00"
content_hash: "f5939ef4a26bef6484e4ea9d11255cf52d1d771dcb6c4f6e98a560c47935f9f5"
---

# Issue tracking integration for Jira Data Center

Polaris supports issue tracking integrations with on-premises Jira Data Center instances via secure tunnel. Once configured, the integration allows Polaris to export issues to Jira tickets. You can also configure integration options to automatically close Jira tickets and keep Polaris triage statuses and Jira ticket statuses in sync automatically.

Note: This topic covers the procedure for setting up issue tracking integration with on-premises Jira Data Center. To set up issue tracking integration for Jira Cloud, see [Issue tracking integration for Jira Cloud](issue-tracking-integration-for-jira.md).

Important: Atlassian has announced end of support for Jira Data Center on March 28, 2029. Plan accordingly when setting up long-term integrations.

## Prerequisites and technical requirements

The issue tracking integration for Jira requires:

- An on-premises Jira Data Center instance running Jira Software 8.4.0 or later.
- OpenSSL (included on Mac and Linux, but needs to be installed on Windows).
- A secure tunnel that is running and shows a Connected status in Polaris. See [Add and manage secure tunnels in the Polaris UI](../add-and-manage-secure-tunnels-in-the-polaris-ui.md).
- A Polaris Organization Administrator who is also a Jira Administrator (with permissions to link external applications to Jira).
- OAuth keys for authentication between Polaris and Jira. See Create public and private RSA keys.

### Issue fields and attributes

Each ticket Polaris creates in Jira includes the following fields:

- Summary: the format of summaries varies, depending on how the ticket was created:
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
- Reporter: The name of the user who configured the integration.

Important: If other fields are required by your Jira project, exports will fail.

## Connect Polaris to a Jira Data Center instance

Complete the following tasks to connect Polaris to a Jira Data Center instance:

1. Create public and private RSA keys
2. Link Polaris to Jira Data Center with a public key
3. Add a Jira Data Center instance to Polaris

### Create public and private RSA keys

To link Jira to Polaris, you need a public/private OAuth key pair with RSA-SHA1 signing for authentication. If you already have these keys, go to the next section. If not, follow these steps:

1. Open a terminal and run the following `openssl` commands.
2. Generate a new RSA private key:

   ```
   openssl genrsa -out jira_privatekey.pem 1024
   ```

   This command assigns the key name `jira_privatekey.pem` and a length of 1024 bits. The .pem file is written to your working directory; you'll need it in the next step.
3. Create a certificate:

   ```
   openssl req -newkey rsa:1024 -x509 -key jira_privatekey.pem -out jira_publickey.cer -days 365
   ```

   You are prompted to answer a series of questions that are necessary for the certificate creation.

   If successful, the command generates an X509 certificate.

   CAUTION:

   The certificate expires after the specified number of days (default: 365). Schedule periodic rotation of certificates. When updating the certificates, you must repeat this procedure, except that you will update the record rather than create it.
4. Extract the PKCS8 private key:

   ```
   openssl pkcs8 -topk8 -nocrypt -in jira_privatekey.pem -out jira_privatekey.pkcs8
   ```

   This command reads the unencrypted private key and outputs a new key in PKCS8 format with the name specified (`jira_privatekey.pkcs8`). This is the private key that you will provide to Polaris later.
5. Extract the public key:

   ```
   openssl x509 -pubkey -noout -in jira_publickey.cer > jira_publickey.pem
   ```

   This command uses the certificate you created to extract the public key file, `jira_publickey.pem`. This is the public key that you will provide to Jira in the next task.

### Link Polaris to Jira Data Center with a public key

Now, add Polaris to Jira as a linked application with the public OAuth key.

1. In Jira, go to Settings > Applications > Application links.

   The Settings icon is the cog at the top right.   
    [image: A screenshot of the left-hand navigation in Jira Data Center.]
2. Enter your Polaris instance URL into the Enter the URL of the application you want to link field.
3. Select Create new link.

   Note: If a warning message stating `No response was received from the URL you entered` appears, you can safely ignore it and select Continue.
4. On the first screen of the Link Applications dialog, complete three required fields:

   - Enter an Application Name (for example, `Polaris`).
   - Select Generic Application from the Application Type dropdown menu.
   - Select the Create incoming link checkbox.

   CAUTION:

   If you adjust or enter text in the other fields, the form will not be accepted.
5. Select Continue.
6. On the second screen of the Link Applications dialog, complete the following fields:

   - Consumer Key: Enter `OauthKey`.
   - Consumer Name: Enter `Polaris`.
   - Public Key: Copy and paste the public key you created from `jira_publickey.pem` into this field.
7. Select Continue.

   The link you created for Polaris appears on the Application Links page.

### Add a Jira Data Center instance to Polaris

Configure your Polaris instance with the private OAuth key and verify the connection.

1. In Polaris, go to My Organization > Integrations.
2. Select + Add Integration > Jira Data Center.

   [image: A screenshot of the Organization Integration settings in Polaris.]
3. On the Create Integration page, complete the form as follows:

   - Enter your internal Jira URL in the Enter Jira URL field.

     Note: Use this URL format: `http://jira.internal.company.com`
   - Select URL is in a private network and then select a secure tunnel from the dropdown.

     Note: The secure tunnel must be in a Connected state for a successful connection. See Confirm the tunnel is in a Connected state for more information.
   - Enter `OauthKey` in the Enter Consumer Key field.
   - Copy and paste your private key (from the .pkcs8 file) into the Enter Private Key field.

   Note: Before you proceed, turn off any pop-up blockers or ad blockers to ensure that you receive the verification code.
4. Click Connect.

   Jira opens in a new tab.
5. Under Welcome to JIRA, select Allow.
6. Copy the verification code that appears on the Access Approved page and go back to Polaris.
7. Paste the code into the Verification Code field and select Validate.

   A green confirmation message Accepted appears next to the Verification Code field.
8. Review the information and then click Save.

The new Jira Data Center integration appears in the Integrations list. A Token Issued date and time is shown on the integration record.

## Create integration options for Jira Data Center

After you connect Polaris to Jira, create integration options to control how issue data is exported to Jira tickets, including custom field mappings, ticket title templates, description content, and synchronization settings. Each option is associated with a specific Jira project and issue type. You can create multiple options for different issue types.

You must have already completed Connect Polaris to a Jira Data Center instance.

Note: Only Organization Administrators can complete these steps.

Important: If you are configuring two-way status synchronization, note the following:

- Synchronizing statuses is not supported for bundled tickets (created when more than one issue in Polaris is exported to Jira in a single step, by a policy action or a manual export). Synchronization only works for individually exported issues with a 1:1 link between a Polaris issue and a Jira work item. Bundled tickets can still participate in one-way auto-close, which is triggered when all issues linked to the work item are dismissed or absent in Polaris.
- Triage status changes triggered by two-way synchronization bypass triage approval workflows. When a linked ticket's status changes in the issue tracker, Polaris updates the triage status of the linked issue(s) immediately, even if a triage approval workflow is configured for the organization, application, or project. If you require approval for every triage status change, configure one-way synchronization (Polaris to Jira) instead.

1. In Polaris, go to My Organization > Integrations.
2. Under Integrations, select the Jira connection you want to configure.
3. Under Jira Options, select + New.

   The Create Jira Options window opens. Required fields are marked with an asterisk.
4. Enter a name for the option in the Options name field.

   Tip: To avoid confusion, include the Jira issue type and Jira project name the option applies to in the option's name. For example, `Sync <Jira issue type> in <Jira project name>`.
5. In the Specify Jira Workflow dropdown, select the Jira project this option will export issues to, and then select the Jira issue type this option applies to.

   Each integration option is associated with a specific Jira project and issue type.
6. (Optional) Define a customized ticket title format in the Ticket Title field to specify or include custom information.

   The following variables can be used to customize the ticket title:

   - `<application name>`
   - `<project name>`
   - `<severity>`
   - `<issue type>`

   Note: If a custom title isn't entered, the default ticket title will be

   ```
   Polaris - Project '<project name>' contains issue '<issue type>'
   ```
7. (Optional) Set up field mapping and synchronization between Polaris and Jira in the Field Mapping table. The fields available in the dropdowns are determined by the workflow and issue type you selected.

   1. Select the add [image: A small user interface icon with a plus symbol within a circle.] icon to add a row to the table.
   2. Use the Polaris Field dropdown to select a field in Polaris you want to export or synchronize with your Jira project.

      Note: Only fields with the Bi-directional tag can be configured for bi-directional synchronization between Polaris and Jira. For example, to sync fix-by dates, map the Fix-By Polaris field to the Due Date Jira field.

      The Jira project must have the Due Date field enabled for this mapping to work.
   3. Use the Jira Field dropdown to select the Jira field to link to the previously-selected Polaris Field option.

      Note: Custom fields created in Jira are marked with the Custom tag in this dropdown. Custom fields must be created in your Jira project before they appear here.
   4. Use the arrows [image: A small user interface icon showing a left-facing arrow over a right-facing arrow.] icon to control the direction of the field synchronization or enable bi-directional synchronization.

      Important: Each Polaris field can only be mapped to one Jira field, and each Jira field can only be mapped to one Polaris field. If you attempt to map a field that is already in use, the duplicate mapping will not be saved.
   5. For fields that require modular mapping (such as Status or Priority), select the Configure button with the gear icon to customize the status mapping. The Polaris triage statuses are:
      - Not Triaged
      - To Be Fixed
      - Dismissed > False Positive
      - Dismissed > Intentional
      - Dismissed > Other

      Important: Polaris can map to Jira ticket statuses, but does not verify Jira resolutions. If a Jira workflow requires an intermediate state before reaching the target status (for example, a ticket cannot transition directly from "To Do" to "Closed"), the sync attempt will fail. When this happens, the Polaris triage status reverts to its previous value and an error is logged in the issue's triage history. Configure your Jira workflows to allow the transitions you need.
   6. Use the trash [image: A small user interface icon showing a trash bin.] icon to remove a field mapping option.

   Jira ticket statuses that have no configured mapping do not trigger any change in Polaris. If a Polaris issue was dismissed as a result of a Jira ticket status change, and you then manually change the Polaris triage status back to an active state (for example, To Be Fixed), the linked Jira ticket is automatically reopened.
8. (Optional) Choose which Jira Description Content items to include in the Jira ticket. Use the toggles to select or deselect which Polaris issue details will be included in the description body of the Jira ticket. Drag and drop properties with the move [image: A small user interface icon showing a grid of dots.] icon to change the order of the description content.

   An example of a completed integration option form is pictured below:

   [image: A screenshot of customized integration options for a Jira project.]
9. Select Save.

The new option appears in the list of Jira Options for that integration. You can now enable this option at the project level. See Connect a Polaris project to Jira Data Center for information on enabling integration options for a project.

If necessary, repeat these steps to create options for other Jira issue types.

## Connect a Polaris project to Jira Data Center

After an Organization Administrator establishes the connection between Polaris and Jira, follow these steps to connect a project to Jira. Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage project settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Go to Settings > Integrations.
4. Under Issue Tracker, select a Jira Data Center instance from the Instance dropdown menu.

   [image: A screenshot of the options used to connect a project to Jira.]

   Note: Each Polaris project supports one issue tracking integration. You cannot add an issue tracking integration to a project that already has one configured.
5. Select the Jira Project exported issues will be sent to.
6. Select the Jira Issue Type Polaris creates when exporting issues.
7. (Optional) Select an integration option from the Jira Options dropdown menu.

   In the Jira Data Center integration options (see Create integration options for Jira Data Center), you can select an option to enable auto-close and triage status synchronization for this project. When an option with triage status sync mappings is selected, triage status changes in Polaris and ticket status changes in Jira will be kept in sync automatically.
8. (Optional) If you selected a Jira Option, configure the branch scope for synchronization.

   The branch scope determines which branches Polaris considers when deciding whether to auto-close a Jira ticket:

   - Default branch only: Auto-close triggers when the issue is absent on the default branch, regardless of whether the issue is still present on other branches.
   - All branches: Auto-close only triggers when the issue is absent on every synchronized branch.

   By default, synchronization is limited to the default branch.
9. Select Validate.
10. Select Save.

### Include individual branches in issue tracking synchronization

When the project-level branch scope is set to All branches, you can control which individual branches participate in issue tracking synchronization.

Before you can configure individual branches, you must:

- Create Jira Data Center integration options (see Create integration options for Jira Data Center).
- Connect the project to a Jira Data Center instance, select an integration option, and set the branch scope to All branches (see Connect a Polaris project to Jira Data Center).

When the branch scope is All branches, Polaris considers all synchronized branches when determining whether to automatically close a Jira ticket. You can include or exclude individual branches from synchronization to control which branches participate. This is useful when you want to track issue resolution across specific branches (such as release branches) or exclude branches such as feature branches from auto-close behavior. An exported issue must be dismissed or absent across all participating branches before the associated ticket is closed.

Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage branch settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Open the Branches tab.
4. Select the branch you want to configure.

   The Edit Branch window opens.
5. Under Issue Tracker, select Include this branch in issue tracking synchronization (ie. auto-close).

   When this option is enabled, Polaris will include this branch when determining whether issues are absent or dismissed across all synchronized branches. When an issue linked to a Jira ticket is absent or dismissed across all synchronized branches, Polaris will automatically close the Jira ticket.

   Note: This option only appears if the project has an issue tracking integration configured with a Jira Option enabled and the branch scope set to All branches.
6. Select Save.
7. (Optional) Repeat this process for other branches you want to include in issue tracking synchronization.

The branch is now included in issue tracking synchronization. When issues linked to Jira tickets become absent or are dismissed across all synchronized branches (including this one), Polaris will automatically close the associated Jira tickets.
