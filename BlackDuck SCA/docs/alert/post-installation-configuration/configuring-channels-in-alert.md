---
title: "Configuring Channels in Alert"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-channels-in-alert.html"
content_id: "oNuhroeRj2H9YGKwut~mvA"
version: "8.4.0"
section: "Post Installation Configuration"
scraped_at: "2026-08-08T23:46:35.126766+00:00"
---

# Configuring Channels in Alert

Channels are the means by which Alert sends notifications. Alert supports the following channels:

- Azure Boards
- Email
- Jira Cloud
- Jira Server
- MS Teams
- Slack

The following section covers UI configuration for each channel type. If you have configured Alert with environment variables, the relevant variables can be found here: Environment variables.

Important: When an issue tracker is configured, Alert will add a link to the issue within the Black Duck SCA project version where any discovered vulnerabilites are reported. If the configured API Token is for a user that does not have either the ‘Global Project Manager’ or ‘Global Project Administrator’ role, Alert will show a 403 Forbidden error & stack trace in the log. The issue will still be created within the tracking system, but it will not be linked back to Black Duck SCA.

## Azure Boards

Before configuring the Azure Boards channel in Alert you must do the following:

1. Ensure that the `ALERT_HOSTNAME` environment variable is set to the **hostname** of the system where Alert is installed. This is required when the OAuth handshake redirects to the Alert Server.

   - For Docker Swarm, add `ALERT_HOSTNAME` as an environment variable within `docker-compose.local-overrides.yml`
   - For Helm, update the *hostname* variable within `values.yml`
2. Follow [the instructions to create a client application](https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops) in Azure

   - Assign the following scopes to the application:
     - Project and team (read)
     - Work items (full)
   - Assign the redirect URL for Alert replacing the variables for hostname and port: -`https://<ALERT_HOSTNAME>:<ALERT_SERVER_PORT>/alert/api/callbacks/oauth/azure`. For authentication to succeed, this must match the location where Alert is hosted.

Tip: For web app users the `:<ALERT_SERVER_PORT>` portion of the URL above is not required.

- Copy the `Client ID` and `Client Secret` from the Azure Boards instance to use when configuring the Alert channel.

To configure the Azure Boards channel in Alert:

1. Navigate to **Channels** > **Azure Boards** and provide the following values:

   | Field | Description |
   | --- | --- |
   | Name | The name of this Azure board. |
   | Organization Name | The name of the Azure DevOps organization. |
   | App ID | The Client ID generated when registering the application. |
   | Client Secret | The Client Secret generated when registering the application. |
   | Microsoft OAuth | Authenticate to Microsoft and retrieve token. |
2. Click **Authenticate & Save**. This will redirect you to Microsoft's OAuth login which starts the process of allowing access to the application created in Azure and fetching the OAuth tokens.

CAUTION:

If the scopes assigned to the client application are anything other than project and team (read) and work items (full), Alert will not be able to retrieve OAuth tokens.

Tip: When you click the **Authenticate & Save** button Alert validates the configuration and saves it if valid. You don't need to click the Save button first and then the **Authenticate & Save** button.

- When you click Authenticate the configuration is saved and you are redirected to the Azure login page if not already logged in.
- When you're logged in with your Azure credentials you may be asked to allow access to the client application.
- When you allow the client application access Azure redirects to Alert via the redirect URL and Alert starts acquiring the OAuth tokens.
- You are redirected to the Alert user interface when Alert has the OAuth tokens.

1. To test the configuration, click **Test Configuration**
2. Click **Save**.

Figure 1. Azure boards configuration. [image: Azure boards configuration]

CAUTION:

You remain logged into Azure after authenticating and may want to log out for security reasons once finished.

## Email

Note: SMTP configuration is performed on initial deployment if you are a hosted customer.

To configure email:

1. Navigate to **Channels > Email** and populate the following fields

   | Field | Description | Notes |
   | --- | --- | --- |
   | SMTP Host | The hostname of the SMTP server |  |
   | SMTP From | The email address to use in the *FROM* field |  |
   | SMTP Auth | Select Select this checkbox if your SMTP server requires authentication; then complete the SMTP User and SMTP Password fields |  |
   | SMTP User | The username to authenticate with the SMTP server |  |
   | SMTP Password | The password to authenticate with the SMTP server |  |
   | Additional Email Properties | Mapping of additional javamail properties that can be used to appropriately configure your email connection. | For acceptable values see [here](https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html) |
2. Click **Test Configuration** to open a `Test Your Configuration` dialog box, containing an email address field for a test email.
3. In the **Email Address** field enter an email address to send a test message.
4. Click **Send Test Message**.
5. Verify the test message was received.
6. Click **Save**.

To delete the current configuration click the **Delete** button.

Figure 2. Email Configuration. [image: Email Configuration]

## Considerations when using email for Project and Project Version notification

If a project is new it usually does not have any users assigned to it. When projects are deleted the email addresses associated with the project are also deleted leaving no users to notify. This can mean that project and project version notification types do not work well for the email channel.

When projects are deleted, you may receive an email stating that a project has been removed even if you are not a member of that project. This may occur if a distribution job has multiple projects associated with the job and you are a member of one of those projects.

## Slack and MS Teams channels for Project and Project Version notification

The Slack and MS Teams channels work well for Project and Project Version notification types because they can send these updates without any issues related to projects without users. These notification types are also used in the Jira Cloud and Jira Server channel; when you configure a Distribution Job in Alert for the Jira Cloud and Jira Server channels, the Project and Project Version deletions are used to help determine which Jira issues to resolve.

## Jira Cloud

To Configure Jira Cloud:

1. Navigate to **Channels > Jira Cloud**, and provide the following values:

   | Field | Description | Notes |
   | --- | --- | --- |
   | URL | The URL of the Jira Cloud instance | |
   | Email Address | The email address of the Jira Cloud User | This **MUST** be a Jira Admin user, unless the **Disable Plugin Check** checkbox is selected |
   | API Token | The API token associated with the email address | To learn more about generating a Jira Cloud token, refer to [Atlassian API tokens](https://confluence.atlassian.com/cloud/api-tokens-938839638.html). |
   | Timeout | The timeout, in seconds, for communicating with the Jira Cloud instance | Defaults to a 300 second timeout |
   | Disable plugin check | Select this option to disable checking whether the **Alert Issue Property Indexer** plugin is installed on the Jira instance | If selected, you must ensure the plugin is installed manually, otherwise issues won't be updated properly |
   | Configure Jira Cloud Plugin | Installs the **Alert Issue Property Indexer** plugin on your Jira Cloud server | |
2. Click **Test Configuration** to validate your configuration.
3. Click **Save**.

To delete the current configuration click the **Delete** button.

Figure 3. Jira Cloud Configuration. [image: Jira Cloud Configuration]

## Jira Server

Note: Alert supports either Basic or Token authentication to Jira Server, but not concurrently.

### Jira Server configuration for Basic Authentication:

1. Navigate to **Channels > Jira Server**, select **Create Jira Server**, and provide the following values:

   | Field | Description | Notes |
   | --- | --- | --- |
   | Name | The unique name for the Jira Server Instance |  |
   | URL | The URL of the Jira Server Instance |  |
   | Authentication Method | The type of authentication to use when connecting to your Jira Server | Provide Username and Password when selecting **Basic** as the authentication method |
   | User name | The user name of the Jira Server User | This **MUST** be a Jira Admin user, unless the **Disable Plugin Check** checkbox is selected |
   | Password | The password associated with the user name |  |
   | Timeout | The timeout, in seconds, for communicating with the Jira Cloud instance | Defaults to a 300 second timeout |
   | Disable plugin check | Select this option to disable checking whether the **Alert Issue Property Indexer** plugin is installed on the Jira instance | If selected, you must ensure the plugin is installed manually, otherwise issues won't be updated properly |
   | Configure Jira Server Plugin | Installs the **Alert Issue Property Indexer** plugin on your Jira server | |
2. Click **Test Jira Server** to validate your configuration.
3. Click **Create** to create the new Jira Server connection.

Figure 4. Jira Server Basic Authentication Configuration. [image: Jira Server Basic Authentication Configuration]

### Jira Server configuration for Personal Access Token:

1. Navigate to **Channels > Jira Server**, select **Create Jira Server**, and provide the following values:

   | Field | Description | Notes |
   | --- | --- | --- |
   | Name | The unique name for the Jira Server Instance |  |
   | URL | The URL of the Jira Server Instance |  |
   | Authentication Method | The type of authentication to use when connecting to your Jira Server | Provide the BD access token when selecting **Personal Access Token** |
   | Access Token | The access token to be used when authenticating to the Jira Server | Input the token string generated in Jira Server |
   | Timeout | The timeout, in seconds, for communicating with the Jira Cloud instance | Defaults to a 300 second timeout |
   | Disable plugin check | Select this option to disable checking whether the **Alert Issue Property Indexer** plugin is installed on the Jira instance | If selected, you must ensure the plugin is installed manually, otherwise issues won't be updated properly |
   | Configure Jira Server Plugin | Installs the **AlertIssue Property Indexer** plugin on your Jira server | |
2. Click **Test Jira Server** to validate your configuration.
3. Click **Create** to create the new Jira Server connection.

Figure 5. Jira Server Personal Access Token Configuration. [image: Jira Server Personal Access Token Configuration]

See the following Atlassian page for information on how to generate a [Personal Access Token](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)

### Jira Server configuration edit

To edit, copy or delete a Jira configuration, select the instance to remove and click the appropriate button.

Figure 6. Jira Server List. [image: Jira Server List]

## MS Teams

There is no global configuration for **MS Teams.**

1. Navigate to **Jobs > Distribution** and select **MS Teams** for the Channel Type in a new distribution job where you configure a Webhook to post messages from Alert.
2. To generate a **MS Teams** Webhook, follow the instructions for [Setting up a custom incoming webhook](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/connectors/connectors-using#setting-up-a-custom-incoming-webhook).

## Slack

There is no global configuration for Slack

1. Navigate to **Jobs > Distribution** and select **Slack** for the *Channel Type* in a new distribution job where you can configure a Webhook to post messages from Alert.
2. To generate a Slack Webhook, follow the instructions for Setting up a custom incoming webhook
