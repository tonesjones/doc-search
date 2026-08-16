---
title: "Configuring Distribution Jobs"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-distribution-jobs.html"
content_id: "qYNvMQvjxehKDyfrLwer6w"
version: "8.4.0"
section: "Post Installation Configuration"
scraped_at: "2026-08-08T23:46:36.219251+00:00"
---

# Configuring Distribution Jobs

A distribution job is a set of instructions for using specific channels to send certain alerts to Black Duck SCA users. This section explains how you configure and manage these jobs.

## About Distribution Jobs

You use the Black Duck providers and channels that you configure to create distribution jobs in Alert.

Go to the **Jobs > Distribution** page in Alert to define and manage your Alert jobs. When you create a distribution job, you create and save instructions for sending specific types of alerts to selected audiences. The Distribution page lists all currently saved jobs. From here, you can create, edit, or delete jobs. Selecting a project includes all versions of that project. You get alerts for notifications that any version of a project configured in the distribution job generates. The notifications match notification types configured in the distribution job. Alerts are sent through email, Jira Cloud, Jira Server, MS Teams, Azure Boards, or Slack.

Figure 1. Alert distribution jobs. [image: Alert distribution jobs]

Note: The notification types available are for the selected Black Duck provider in the distribution job.

The **Distribution** page contains the following fields, displayed in a table format. You can sort in ascending or descending order on any column heading.

- **Name**: The names of the distribution job.
- **Channel**: Azure Boards, Email, Jira Cloud, Jira Server, MS Teams, or Slack.
- **Provider**: The selected provider; in this case, Black Duck.
- **Frequency Type**: Specifies when this distribution job runs, either*Daily* or*Real-Time.*
- **Last Run**: Date/time of the most recent distribution.
- **Status**: Success, Failure, or Unknown.
- **Enabled**: Displays a checkmark or an **X** depending on the enabled state of the job.

You can enable or disable a distribution job by selecting a checkbox on the **Edit Distribution Job** or **New Distribution Job** screen.

- **Edit:** Click the pencil icon at the far right to edit a distribution job.
- **Copy:** Click the copy icon at the far right to copy a distribution job. For more information, refer to the Copying a distribution job section.
- **Auto-Refresh:** This slider configures the page to auto refresh.
- **Refresh** button enables you to refresh the view on-demand.

Figure 2. Distribution jobs list. [image: Distribution jobs list]

You can search for specific names or types of distribution jobs using the search field.

Distribution jobs display an error under the following conditions:

- When you create a new distribution job, but the global configuration is not set for the Channel or Provider.
- When you open an existing Distribution Job, and the global configuration for the Channel is missing.

Note: When upgrading, distribution jobs that are configured incorrectly are disabled.

## **Creating a distribution job**

Use the following process to create a distribution job. Required fields are denoted by a red asterisk ( ***** ).

1. Navigate to **Jobs** > **Distribution**, click **+New**. The **New Distribution Job** dialog displays.
2. To enable the distribution job, leave the **Enabled** checkbox selected or deselect the checkbox to disable the job.
3. Using the **Channel Type** dropdown menu, select the job type; either **Azure Boards**, **Email**, **Jira Cloud**, **Jira Server**, **MS Teams**, or **Slack**.

Notifications generated through Alert are sent using this channel. The **New Distribution Job** dialog expands to display the appropriate fields for the selected job type.

Tip: The distribution jobs display an error message when there are validation errors relating to global configurations.

1. Complete the fields as follows.

Tip: The following are *common for all job types:*

**Name:** Enter a unique name for the distribution job.

**Frequency:** Use the dropdown to select how frequently you want Alert to check for notifications to send: *Real-Time*, as triggers occur or *Daily.*

**Provider:** Select Black Duck. This displays additional fields, which are described in the following steps.

1. **Provider Configuration**: Enter the unique name assigned to this provider configuration, which is set on the Providers page.
2. After completing the previous fields, additional fields pertinent to your selected provider type are shown:

**Notification Types:** Select one or more types from the dropdown list. Only the selected notification types are included for this distribution job. Your selections display in the **Notification Types** box.

- Click **X** at the right of a notification type to remove it from your selections.
- In **Distribution Job** configurations with Black Duck selected as the provider, BOM_EDIT displays as an option in the dropdown selector for **Notification Types**. The BOM_EDIT notification is primarily used in Jira Cloud, Jira Server, Azure Boards to keep component information on issues as up-to-date as possible.
- When used with Jira Cloud, Jira Server, or Azure Boards, the deletion of either project or project version triggers a *Resolve Transition*, when enabled, for all issues related to it.

Tip: For information about notifications in Black Duck SCA, see  "Working with Notifications".

**Notification Types** are as follows:

- **BOM_EDIT** - Changes to a BOM component such as updating its license or usage.
- **PROJECT** - Projects have been deleted.
- **PROJECT VERSION** - When an individual project version is deleted, a notification is generated. If a project version, or versions, are deleted as part of deleting an entire project, a notification is not generated for the deleted version(s).
- **LICENSE_LIMIT** - License restrictions are near or exceeding capacity.
- **POLICY_OVERRIDE** - A policy has been overridden.
- **RULE_VIOLATION**- A policy violation has occured.
- **RULE_VIOLATION_CLEARED** - A policy violation has been cleared (either the affected BOM component was deleted or the policy itself was updated).
- **VULNERABILITY** - Vulnerabilities have been introduced, updated, or removed.
- **COMPONENT_UNKNOWN_VERSION** - A component has been added to the BOM that does not have a version.

Important:

When utilizing one of the "ticketing" channels, such as Jira Server, and employing `Rule Violation`, `Vulnerability⁣`, or `Component Unknown Version⁣` in the configuration for a distribution job, it is advisable to also include `Project⁣` and `Project Version⁣`. When these are included, if a project or project version is deleted, any tickets opened for that project or project version will be updated and resolved. If they are not included, Alert will leave the tickets open.

In addition to `Project` and `Project Version` it is advised to include `Policy Override` and `Rule Violation Cleared` if you are using one of the ticketing channels and using `Rule Violation`. If your component is no longer violating the policy or you override the policy violation, and you do not have `Policy Override` and `Rule Violation Cleared`, Alert will not update and resolve the associated tickets.

**Processing:** Select one of the following to determine the notification message processing:

- **Default:** Displays the notifications as they are.
- **Digest:** The Digest format presents a streamlined version of the notifications; it collapses the Add and Delete operations, for example, if a component is added and then deleted with a policy violation in between the time Alert collects notifications, then Alert excludes the component. This configuration works better when the Alert job is set to a daily frequency as it is less likely that the Add and Delete will be processed in the same batch with real-time frequency.
- **Summary:** The Summary format does the same as Digest but instead of listing all the components, it summarizes them, for example, it shows the number of components in violation of a policy rather than listing each component.

Note: The *Summary* processing type is not available as an option for the issue tracker channels such as Jira Cloud, Jira Server, or Azure Boards.

1. **Filter by Project:** If selected, only notifications from the selected projects table are processed. Otherwise, notifications from all projects are processed. Selecting this checkbox displays these additional fields:

Note: Alert (ProviderDataAccessor) now retrieves Black Duck SCA project and user data information directly from Black Duck rather than using the database tables in Alert.

- **Project Name Pattern:** Enter the regular expression to determine the projects to include. These are in addition to the projects selected in the table in the next step.

  The **Project Name Pattern** field displays after selecting *Black* *Duck* as the provider type and then selecting the **Filter by Project** checkbox. You can supply a regular expression that Alert can use to match multiple Black Duck projects. If you are not familiar with regular expressions, refer to: [https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html.](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)

  The project name pattern you specify selects projects in addition to the projects selected in the table. Use this feature when you want to specify multiple projects that have similar names. This saves time in specifying existing projects as well as avoiding the work of adding future projects whose names match the pattern.

  For example, assume there's a distribution job called *Job1*. An administrator creates *Job1* with this regular expression in the distribution job field: *TestProject[0-9]*.* If a new project is added named *TestProject3*, *Job1* sends notifications for *TestProject3* because the new project name satisfies the regular expression matches An administrator didn't have to manually edit *Job1* to include *TestProject3*.

  - The **Project Version Name Pattern** field is similar to the Project Name Pattern field, except it allows further filtering based on the version. If you specify a project name pattern or select any projects, the Project Version Name Pattern only checks the projects that apply when filtering.
  - **Projects:** Select a project or projects for which you want to retrieve notifications.

    - Clicking **Select** displays the **Projects** table Select the projects to include in notifications by clicking the checkbox at the left of the project name.
    - Click **Show Selected Only** to display only your selected projects.
    - Click **Show All** to display all projects.
    - When you are finished selecting your projects, click **OK** to return to **New Distribution Job**.

    Your selected projects now display in the **Projects** field when projects are selected, but not returned in the request and you navigate to the listing, these items are added to the list and are removable.

Note: Black Duck request-caching is employed when saving Distribution Jobs that *filter by project*.

Black Duck projects and users that were updated/deleted less than 2 minutes prior to creating a Distribution Job might not be updated by Alert. This can be resolved by waiting 2 minutes after creating a new project or user before saving the Distribution Job or resaving the Distribution Job after such a change in Black Duck.

- **Black Duck Notification Filtering:** The following filters are available:

  - **Policy Notification Type Filter:** To use this filter, select a policy notification.
  - Click **Select** to show a list of policies.
  - Select the checkbox for each policy that you want to add, and click **OK**.

Alert includes vulnerability information in security-related policy notifications.

- **Vulnerability Notification Contains Severities**: To use this filter, select a vulnerability notification.
- Click the dropdown menu to show a list of vulnerability severities.
- **Test Configuration**

Click **Test Configuration** to send a test alert to ensure the configuration is valid. You are notified if the validation fails and the cause of the failure. Incorrect fields are indicated, informing you of the information to correct.

Click **Save** to save the new job. You are returned to the **Distribution** screen, and the new job is listed.

### Channel specific fields

Depending on the selected **Channel Type**, the fields available in the distribution job will be presented as per the listed Channel Types below:

Important: When configuring distribution jobs for ticket tracking channels (like Jira or Azure Boards), you must configure `Resolve Transition` OR `Re-open Transition` to ensure that the transition is performed when Alert receives a notification that would trigger such transitions.

### Azure Boards

- **Comment on Work Items**: When selected, Alert comments on Work Items it created when updates occur.
- **Azure Board**: The name of the desired Azure Board as configured in **Distribution Channels**.
- **Azure Project**: The project name or ID in Azure Boards.
- **Work Item Type**: The work item type in Azure Boards.
- **Work Item Completed State**: The work item state when Alert receives a DELETE operation for the work item.
- **Work Item Reopen State**: The resulting state of a work item when Alert receives an ADD operation and the work item is in a completed state.

Figure 3. Configuring Azure board distribution jobs. [image: Configuring Azure distribution jobs]

Important: When you create a distribution job for the Azure Boards channel, ensure that the Azure project you are using in the Job is not using a template process. You must create an [inherited process](https://docs.microsoft.com/en-us/azure/devops/organizations/settings/work/manage-process?view=azure-devops#create-an-inherited-process) and then change the project to use that new process. No change is required if the project is already using an inherited process.

### Email

- **Subject Line:** Enter the text for the Alert email subject line.
- **Additional Email Addresses:** Additional email addresses for valid users of the provider to which notifications of this job should be sent.

  - Click the drop-down to display the Additional Email Addresses dialog box.
  - Click the checkbox for each email address you want to add and click **Submit**.
  - Click the checkbox for **Email Address** to deselect all previously selected email addresses.

Figure 4. Additional email recipients [image: Additional email recipients]

- **Additional Email Addresses Only:** You can select the **Additional Email Addresses Only** checkbox to customize email recipients. By selecting this checkbox, you exclude the configured emails on projects and enable sending emails only to the users selected in the **Additional Email Addresses** field.
- **Project Owner Only:** Select this checkbox to have Alert sends email alerts to project administrators.

  If this is not selected, then all users assigned to the project, including the project administrators, receive alerts. More information is available through clickable links that are included in the notification emails.

Note: Project Owner Only cannot be set if **Additional Email Addresses Only** is set.

- **Attachment File Type:** You can provide an external file type to be used as an email attachment in the Distribution job.

  Click the dropdown menu for **Attachment File Type**, and select a file type. Attachment options are **CSV**, **JSON**, **XML**, and **NONE** (which is the default).

  If a file type is selected, then a file of that type that shows the message content is attached to the email.

Figure 5. Alert email distribution job. [image: Alert email distribution job]

### Email Considerations

For email, one message is sent per project, rather than per project version. This occurs only if the notifications are processed in the same batch.

When projects are deleted, you may receive an email stating that a project has been removed even if you are not a member of that project. This may occur if a distribution job has multiple projects associated, and you are a member of one of those projects. When a project is deleted, Alert removes the project data within minutes. When this happens, no email addresses associated with that project in Alert, meaning that Alert treats this scenario like a system-wide notification, and sends the notification to all other email addresses for the projects associated with the job. This happens when the distribution job is configured for a *Daily* frequency. For distribution jobs with *Real-Time* frequency, this does not happen. An example of a system-wide notification is license limit notifications.

### Slack

Slack messages sent via Apps/webhooks use the App name and no longer support setting the sender username. Existing webhooks created before Slack made this change will still support setting the sender username.

When creating new webhooks the field `Channel Username` will have no effect and will instead show the name of the Slack Application that the webhook was created for.

- **Webhook:** Enter the appropriate Slack URL to receive alerts.
- **Channel Username:** Enter the user name to display as the message sender in the Slack channel.

Figure 6. Alert distribution job for Slack. [image: Alert distribution job for Slack]

### Microsoft Teams

- **Webhook:** Enter the MS Teams URL to receive alerts.

Figure 7. Alert distribution job for MS Teams. [image: Alert distribution job for MS Teams]

### Jira Cloud / Jira Server

Note: Specific Jira Server versions are supported, see requirements for more information.

Distribution jobs can be configured to send notifications to the Jira server channel. Such notifications create new tickets, or update tickets matching the notification content. The ticket data displays in a format similar to an email or Slack message containing a single piece of data.

- **Provider Type**: Select the provider. Only notifications from the selected provider are processed in the distribution job.
- **Add Comments:** If this checkbox is selected, comments are added to the Jira ticket with the latest changes.
- **Issue Creator:** The user name of the Jira server user to assign to the Issue Creator field in the Jira issue.
- **Jira Project:** The name of the Jira project for which this job creates/updates Jira tickets.
- **Issue Type:** Specify the issue type; for example, bug or task.
- **Resolve Transition:** If a transition is listed (case sensitive), it is used when resolving an issue. This happens when Alert receives a *DELETE* operation from a provider.

This must be in the *Done* status category.

- **Re-open Transition:** Used for re-opening issues. If a transition is listed (case sensitive), it is used when you reopen an issue. This happens when Alert receives an ADD/UPDATE operation from a provider.

This must be in the *To Do* status category.

- **Issue Summary:** Summary of the issue that Alert creates. The following variables can be used to enter content from the message `providerName`, `projectName`, `projectVersion`, `componentName`, `componentVersion`, and `severity`.

Tip: When configuring distribution jobs, required fields are denoted by a red asterisk ( ***** ).

Figure 8. Configuring Jira distribution jobs. [image: Configuring Jira distribution jobs]

### Advanced Jira Configuration

Configure custom fields for Jira Server and Jira Cloud distribution jobs. In the **Advanced Jira Configuration** section, expand this panel to open a field mapping dialog box. Use this field to provide static values to Jira fields or map them to information from the notifications.

Figure 9. Advanced Jira Configuration. [image: Advanced Jira Configuration]

**To add a custom Jira field:**

1. Click **+ Add Jira Field Mapping** to create a new mapping
2. Enter a name for the **Jira Field**

   Supported field types are:

   - String - i.e. text fields: single and multi-line)
   - Array - A space-separated list of values with the following supported item types:

     - String (for example, labels)
     - Component (for example, Component/s field)
     - Option (for example, Checkboxes)
   - Option (for example, single-select field)
   - Priority – for example, high
   - User - Use *username* on Jira Server and Jira Data Center. Use *account_id* on Jira Cloud. ([Find an account ID](https://community.atlassian.com/t5/Jira-questions/In-CLOUD-how-to-update-a-User-picker-single-select-value-in-a/qaq-p/819219) for a Jira Cloud user.)
3. Enter a static value or select one of the following placeholders.

   1. `{{providerType}}` - The name of the Alert provider (Black Duck) from which the notification was received.
   2. `{{projectName}}` - The name of the project in Black Duck SCA.
   3. `{{projectVersion}}` - The version of the project in Black Duck SCA.
   4. `{{componentName}}` - The name of the component from the project-version in Black Duck SCA.
   5. `{{severity}}` - The policy severity or the highest vulnerability severity for the component in Black Duck SCA.
   6. `{{componentVersion}}` - The version of the component from the project-version in Black Duck SCA.
   7. `{{policyCategory}}` - The policy category field for a policy violation in Black Duck SCA.
   8. `{{shortTermUpgradeGuidance}}` - The short term upgrade recommendation for security vulnerabilities of a component in Black Duck SCA.
   9. `{{longTermUpgradeGuidance}}` - The long term upgrade recommendation for security vulnerabilities of a component in Black Duck SCA.
   10. `{{componentUsage}}` - The usage option of the component in Black Duck SCA.
   11. `{{componentLicense}}` - The license name of the component in Black Duck SCA.

Templates can be used along with placeholder values to create custom field values.

For example using the following template:

```
"Project Name: {{projectName}} | Project Version Name: {{projectVersion}}"
```

Would produce the following value in the Jira Custom field:

```
"Project Name: my_project | Project Version Name: my_version"
```

Note: For the Jira Server and Jira Cloud distribution jobs, when adding a custom field in the Advanced Jira section, the value of the custom field can be a JSON string for custom fields with the field type of ‘any’ or ‘object’.

Example value content:

JSON Object:

```
{"firstAttribute": 1001, "secondAttribute": "String value" }
```

JSON array:

```
[ { “key”: “value-1” }, { “key”: “value-2” }, { “key”: “value-3” }]
```

Figure 10. Jira distribution job custom mapping. [image: Jira distribution job custom mapping]

Alert will parse the value as JSON and send the JSON as the content for the custom field if **Treat Value as JSON** is checked. This overrides any custom field processing that Alert does by inspecting the custom field type.

Figure 11. Test Jira distribution job configuration. [image: Test Jira distribution job configuration]

After you have made your selections for the new distribution job, click **Test Configuration**. Clicking **Test Configuration** displays a dialog that is pre-populated with a default message.

Figure 12. Testing Jira distribution job. [image: Testing Jira distribution job]

Click **Send Message** to test the job configuration. You can customize the topic displayed in the message and the message content. When clicking **Send Message**, the configuration is validated and the contents are sent to the channel specified by the job.

If information is missing, the notification *Required field missing* displays in red above the affected field. Complete the required fields, and click **Test Configuration**. When the test is successful, click **Save**.

Note: If you are using a Jira Data Center, use the Jira Server channel when you configure a distribution job in Alert. The Jira Server channel works for on-premise Jira Server installations, and Jira Data Center installations.

A non-admin Jira user (Cloud and Server), configured for Alert must have the following permissions for all Jira projects that Alert might need to update:

- *Browse Projects*
- *Create Issues*
- *Edit Issues*
- *Assign Issues*
- *Modify Reporter*
- *Transition Issues*
- *Resolve Issues*
- *Add comments*

### Copying a distribution job

The **Distribution** table includes an additional column containing a *copy* button. This enables you to copy existing jobs quickly where only a small number of fields differ.

To copy a distribution job:

- In the **Distribution** table, click on the copy icon in the last column.
- Edit the details as required, making sure to provide a unique job **Name**.
- Click **Save**.

### Identical distribution jobs that include transitions

If you configure two distribution jobs for Jira that are identical in their settings, and those settings include transitions, they will clash. When one of the jobs transitions the issue, the next job will fail to transition the issue because the issue is already transitioned.

When resending a notification to a Jira distribution job from the Audit page, if that distribution job includes transitions and has already succeeded, then an attempt to resend a message to it fails because Jira has already executed the transition for that message.

### Editing a distribution job

- In **Jobs > Distribution**, double click the row which contains the Distribution Job to display the **Distribution Configuration** screen.
- Make the desired edits.
- Click **Test Configuration** to validate the configuration changes are correct.
- Click **Save** to persist the edits.

### Deleting a distribution job

- In **Jobs > Distribution** click the row that contains the job which you would like to delete.
- Click **Delete**. A popup will display asking you confirm.
- Click **Confirm** to delete the job.
