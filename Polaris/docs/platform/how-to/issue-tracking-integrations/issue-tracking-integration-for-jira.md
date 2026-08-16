---
title: "Issue tracking integration for Jira"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-tracking-integration-for-jira.html"
content_id: "DIrTqgd96EYX7eyAKSUkjg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:31.431866+00:00"
content_hash: "ec6bed6146a9b671e19e7ed504d8189396c7971617cd871795e37d86c807cf9e"
---

# Issue tracking integration for Jira

This page describes the issue tracking integration for Jira. Once configured, the integration allows Polaris to create tickets in Jira for issues. You can also configure integration options to automatically close Jira tickets and keep Polaris triage statuses and Jira ticket statuses in sync automatically.

## Prerequisites and technical requirements

The issue tracking integration for Jira requires:

- A classic Jira Cloud instance running the latest long term support release.

  Important: The Jira instance must be routable over the Internet. Closed networks are not supported at this time. Jira Next-Gen is not supported.
- Only Organization Administrators can connect Polaris to Jira. The Organization Administrator who configures the integration must also be a Jira Administrator (with permissions to link external applications to Jira).
- Authentication between Jira and Polaris is through OAuth. You will need to create public and private OAuth keys, as described in this article.

### Issue fields and attributes

Each ticket Polaris creates in Jira includes the following fields:

- Summary: the format of summaries vary, depending on how the ticket was created:
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
- Reporter: The name of the user who configured the integration.

Important: If other fields are required by your Jira project, exports will fail.

## Connect Polaris to a Jira instance

Complete the following tasks to connect Polaris to a Jira instance:

1. Create public and private RSA Keys
2. Link Polaris to Jira with a public key
3. Add a Jira instance to Polaris

Important: These tasks can only be completed by an Organization Administrator *who is also a Jira Administrator*. The same person must complete all of the tasks in this section.

Each one of these tasks is explained in more detail below.

### Create public and private RSA Keys

To link Jira to Polaris, you need to create a pair of public and private OAuth keys. If you already have these keys, go to the next section. If not, follow these steps:

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

   The certificate will expire in 365 days – you can change the final value to a different number. A new certificate will be needed after the interval has passed.

   CAUTION:

   Certificates expire after a set period of time. Schedule periodic rotation of certificates. When updating the certificates, you must repeat this procedure, except that you will update the record rather than creating it.
4. Extract a PCKS8 private key:

   ```
   openssl pkcs8 -topk8 -nocrypt -in jira_privatekey.pem -out jira_privatekey.pcks8
   ```

   This command reads the unencrypted private key and outputs a new key in PKCS8 format with the name specified (`jira_privatekey.pcks8`). This is the private key that you will provide to Polaris later.
5. Extract the public key:

   ```
   openssl x509 -pubkey -noout -in jira_publickey.cer > jira_publickey.pem
   ```

   This command uses the certificate you created to extract the public key file, `jira_publickey.pem`. This is the public key that you will provide to Jira in the next task.

### Link Polaris to Jira with a public key

Now, add Polaris to Jira as a linked application with the public OAuth key.

1. In Jira, go to Settings > Products.

   Settings is the cog icon at the top right.
2. Under Integrations, select Application Links.

   [image: A screenshot of the left-hand navigation in Jira.]
3. Select Create Link.

   The Create an application link window opens.
4. Select Direct application link, enter the URL of your Polaris instance in the Application URL field, and select Next.

   [image: A screenshot of the Create an application link window in Jira.]   

   Note: If a warning appears, select Continue.

   The Review Link window opens.
5. On the Review link form, complete three required fields:

   - Enter an Application Name (for example, `Polaris`).
   - Select Generic Application from the Application Type dropdown menu.
   - Select the Create incoming link checkbox.

   Important: If you enter text or place the cursor in the other fields, the form will not be accepted.
6. Select Continue.

   The link you created for Polaris appears on the Application Links page.
7. Select the options icon [image: tracking jira options icon] next to the application link you created for Polaris and then select Edit.

   The Configure window opens.
8. Open the Incoming Authentication tab, and complete the required fields:

   [image: A screenshot of the Incoming Authentication tab.]   
   - Consumer Key: Enter `OauthKey`.
   - Consumer Name: Enter `Polaris`.
   - Public Key: Copy and paste the public key you created into this field.

   Select Save (near the bottom of the form).

### Add a Jira instance to Polaris

Configure your Polaris instance with the private OAuth key and verify the connection.

Important: These steps can only be completed by the user who connects Polaris to Jira (described in the previous task).

1. In Polaris, go to My Organization > Integrations.
2. Select + Add Integration > Jira Cloud.

   [image: tracking org add]
3. On the Jira Integration Set Up page, complete the form as follows:

   - Enter your Jira instance's URL in the Enter Jira URL field.
   - Enter `OauthKey` in the Enter Consumer Key field.
   - Copy and paste your private key (from the .pcks8 file) into the Enter Private Key field.

   Note: Before you proceed, turn off any pop-up blockers or ad blockers to ensure that you receive the verification code.
4. Click Next.

   Jira opens in a new tab.
5. Under Welcome to JIRA, select Allow.
6. Copy the verification code that appears on the Access Approved page and go back to Polaris.
7. Paste the code into the Enter Verification Code field and select Validate.
8. Click Next.
9. Review the information and then click Finish.
10. When the Integrations page opens, select Test next to your Jira URL to verify the connection is working as expected.

    If the test is successful, a green check mark appears next to the Test button.

## Create integration options for Jira

After you connect Polaris to Jira, create integration options to control how issue data is exported to Jira tickets, including custom field mappings, ticket title templates, description content, and synchronization settings. Each option is associated with a specific Jira project and issue type. You can create multiple options for different issue types.

You must have already completed Connect Polaris to a Jira instance.

Note: Only Organization Administrators can complete these steps.

Important: Synchronizing issue and ticket statuses is only supported for Jira Cloud. Jira Data Center is not supported. Synchronizing statuses is not supported by bundled tickets (created when more than one issue in Polaris is exported to Jira in a single step, by a policy action or a manual export).

1. In Polaris, go to My Organization > Integrations.
2. Under Integrations, select the Jira connection you wish to configure.
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

   1. Select the add [image: issue tracking options add icon] icon to add a row to the table.
   2. Use the Polaris Field dropdown to select a field in Polaris you want to export or synchronize with your Jira project.

      Note: Only fields with the Bi-directional tag can be configured for bi-directional synchronization between Polaris and Jira. For example, to sync fix-by dates, map the Fix-By Polaris field to the Due Date Jira field.

      The Jira project must have the Due Date field enabled for this mapping to work.
   3. Use the Jira Field dropdown to select the Jira field to link to the previously-selected Polaris Field option.

      Note: Custom fields created in Jira are marked with the Custom tag in this dropdown. Custom fields must be created in your Jira project before they appear here.
   4. Use the arrows [image: integration options sync icon] icon to control the direction of the field synchronization or enable bi-directional synchronization.

      Important: Each Polaris field can only be mapped to one Jira field, and each Jira field can only be mapped to one Polaris field. If you attempt to map a field that is already in use, the duplicate mapping will not be saved.
   5. For fields that require modular mapping (such as Status or Priority), select the Configure button with the gear icon to customize the status mapping. The Polaris triage statuses are:
      - Not Triaged
      - To Be Fixed
      - Dismissed > False Positive
      - Dismissed > Intentional
      - Dismissed > Other

      Important: Polaris can map to Jira ticket statuses, but does not verify Jira resolutions. If a Jira workflow requires an intermediate state before reaching the target status (for example, a ticket cannot transition directly from "To Do" to "Closed"), the sync attempt will fail. When this happens, the Polaris triage status reverts to its previous value and an error is logged in the issue's triage history. Configure your Jira workflows to allow the transitions you need.
   6. Use the trash [image: trash icon] icon to remove a field mapping option.

   Jira ticket statuses that have no configured mapping do not trigger any change in Polaris. If a Polaris issue was dismissed as a result of a Jira ticket status change, and you then manually change the Polaris triage status back to an active state (for example, To Be Fixed), the linked Jira ticket is automatically reopened.
8. (Optional) Choose which Jira Description Content items to include in the Jira ticket. Use the toggles to select or deselect which Polaris issue details will be included in the description body of the Jira ticket. Drag and drop properties with the move [image: grip dots icon] icon to change the order of the description content.

   An example of a completed integration option form is pictured below:

   [image: A screenshot of customized integration options for a Jira project.]
9. Select Save.

The new option appears in the list of Jira Options for that integration. You can now enable this option at the project level. See Connect a Polaris project to Jira for information on enabling integration options for a project.

If necessary, repeat these steps to create options for other Jira issue types.

## Connect a Polaris project to Jira

After an Organization Administrator establishes the connection between Polaris and Jira, follow these steps to connect a project to Jira. Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage project settings can complete these steps.

1. In Polaris, go to Portfolio.
2. Open an application and then open a project.
3. Go to Settings > Integrations.
4. Under Issue Tracker, select a Jira instance from the Instance dropdown menu.

   [image: A screenshot of the options used to connect a project to Jira.]

   Note: Each Polaris project supports one issue tracking integration. You cannot add an issue tracking integration to a project that already has one configured.
5. Select the Jira Project exported issues will be sent to.
6. Select the Jira Issue Type Polaris creates when exporting issues.
7. (Optional) Select an integration option from the Jira Options dropdown menu.

   If you created Jira Options (see Create integration options for Jira), you can select an option here to enable auto-close and triage status sync for this project. When an option with triage status sync mappings is selected, triage status changes in Polaris and ticket status changes in Jira will be kept in sync automatically.
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

- Create Jira Options (see Create integration options for Jira).
- Connect the project to Jira, select a Jira Option, and set the branch scope to All branches (see Connect a Polaris project to Jira).

When the branch scope is All branches, Polaris considers all synchronized branches when determining whether to automatically close a Jira ticket. You can include or exclude individual branches from synchronization to control which branches participate. This is useful when you want to track issue resolution across specific branches (such as release branches) or exclude branches such as feature branches from auto-close behavior.

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
