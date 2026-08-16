---
title: "Current Alert Release Notes"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/current-alert-release-notes.html"
content_id: "ewKr4g6vw1475me0yfa1ug"
version: "8.4.0"
section: "Alert Release Notes"
scraped_at: "2026-08-08T23:46:15.660129+00:00"
---

# Current Alert Release Notes

## Release Notes Version 8.4.0

**New Features**

- It is now possible to set new Alert RabbitMQ  environment variables when installing or upgrading Alert. These variables can be used to tune the performance of RabbitMQ and are set to their default values.
- Administrative users with read level access for Global Content and the Settings Page (Descriptor), are now able to download system diagnostics data via the Alert application homepage. If a user has access, the download option will be visible under the “System Diagnostics” section. The downloaded file will include system information that should be sent if opening a support ticket. See also Contacting Black Duck Support.

**Changes**

- IALERT-3961 The Diagnostics API has been enhanced to provide more data via the `/api/diagnostic` endpoint.

**Resolved issues**

- IALERT-3950 Set the location header when communicating with Black Duck SCA REST APIs to better track Alert requests in Black Duck SCA.
- IALERT-3951 Fixed an issue causing extraneous processing when executing jobs for notifications.
- IALERT-3958 Build of DB image was updated to perform configuration for Postgres upgrades in a builder stage, with the output copied to the final image.
- IALERT-3959 Updated Docker build for Alert Postgres image to eliminate minor vulnerabilities notes in dependencies.
- IALERT-3928 Fixed issues with the queues in RabbitMQ being persistent.
- IALERT-4007 Fixed an issue preventing users assigned custom roles, from accessing UI areas they should otherwise be able to access.
- IALERT-4015 Updated documentation to reflect issue tracking systems, such as Jira, require configuration to ensure ticket status transitions occur for resolution or re-open states.

**Known issues**

- A known issue is preventing the automatic check of ‘Alert Issue Property Indexer’ installation when Jira Server is used with a personal access token. Distribution jobs and the ‘Test Jira Server’ option in the Jira Server configuration page are also prevented from functioning properly. The workaround for this issue is to ensure the checkbox for ‘Disable Plugin Check’ is checked and manually verify that the ‘Alert Issue Property Indexer’ is installed before executing any distribution jobs.
- Azure DevOps OAuth is slated for deprecation in 2026. Existing OAuth applications, created via Azure DevOps, should continue to function. [As of April 23, 2025, the Azure DevOps OAuth app platform is no longer accepting new app registrations.](https://devblogs.microsoft.com/devops/no-new-azure-devops-oauth-apps/) To create new apps, Microsoft is recommending the use of [Microsoft Entra ID OAuth](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app) to integrate with Azure DevOps. It is not yet known if using Microsoft Entra ID presents any issue for Alert.
- After importing the SAML configuration from Black Duck, Alert users may experience issues when attempting Alert login. It it recommended to configure SAML without importing the configuration from Black Duck.
- Initiating the Jira Server installation plugin from within Alert does not work with Jira software 9.5.x+. It is recommended to install the plugin manually on your Jira Server/Datacenter instance.
- Additional email addresses displayed as search results may display incorrect page numbers or empty pages.
- With the configuration value for `ssl:` set to `true`, and the `sslUseFiles:` value set to `false`, an error may be returned. It is recommended to fully enable ssl, set `sslUseFiles` to true, provide client key/certificates and root CA certificate, or provide a root CA certificate as outlined in the following troubleshooting section SSL configuration issue when sslUseFiles is set to false.
- Searches for dates and times in the Distribution and Audit Failure tables do not work as expected. For Audit Failures the date and time searched match the content of the notification. For Distribution Jobs the search for a timestamp does not work.
- Email distribution job notifications may log an error during deletion of a project and not send a notification. This is due to the system attempting to look up a nonexistent email recipient from the deleted project.
- Helm deployments may fail to deploy using certain storage configurations. See the Troubleshooting section of this document for more information.
- Alert installation may fail when running against some PostgreSQL variations, including Enterprise DB. A script is available that allows Alert to be installed with an external EnterpriseDB.
- Use of the "Global Transitions" feature of Jira workflows with Alert may lead to conflict when resolving or reopening tickets and Jira issues may not transition states correctly.

  - Use of basic and well-defined transitions in Jira workflows is recommended. See the Troubleshooting section of this document for more information.
- When Alert retrieves notifications from Black Duck SCA, there is a potential issue with how notifications are paginated and returned. This affects the reliability of receiving notifications, particularly when multiple notifications share the same `createdOn` timestamp.

  - When multiple notifications have the same `createdOn` timestamp and are not all returned in a single GET call, subsequent requests may not guarantee that the notifications not received in the prior request will be returned.

  Consider the following example notifications:

  | ID | createdOn |
  | --- | --- |
  | 13f146d5-26ab-497b-ac2e-4f49105816d7 | 2025-10-13 19:47:45.206+00 |
  | a43f9def-47f8-442d-991c-39c62a9f33fe | 2025-10-13 19:47:45.206+00 |
  | a38f33c2-0a61-40b7-ae62-563da40a3165 | 2025-10-13 19:47:45.206+00 |

  - If the first two notifications (IDs 13f146d5 and a43f9def) are returned as notifications #199 and #200 from a GET call, there is no guarantee that the third notification (ID a38f33c2) will be returned in the next GET call. Instead, it is possible to receive one of the notifications that were already returned.
  - Although Alert correctly identifies duplicates, it may result in missing notifications, as the third notification (a38f33c2) may never be received.
  - This issue can lead to incomplete notification retrieval, causing Alert to miss notifications that share the same createdOn timestamp.
