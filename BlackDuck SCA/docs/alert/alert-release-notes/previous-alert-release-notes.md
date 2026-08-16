---
title: "Previous Alert Release Notes"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/previous-alert-release-notes.html"
content_id: "idkqoPTsKhKFJuNUwn6ePw"
version: "8.4.0"
section: "Alert Release Notes"
scraped_at: "2026-08-08T23:46:16.627084+00:00"
---

# Previous Alert Release Notes

## Release Notes Version 8.3.1

**Resolved issues**

- IALERT-3912 Resolved a formatting problem in Jira Cloud where the markdown for links was not functioning properly, resulting in the markdown being displayed as plain text. Links are now operational in Jira Cloud.

## Release Notes Version 8.3.0

**New Features**

- A new environment variable `ALERT_NOTIFICATION_MAPPING_BATCH_LIMIT` has been added that allows the configuration of the default batch size for notification processing.
- Added configuration option to provide a timeout for communications with Jira Cloud channels.
- Added configuration option to provide a timeout for communications with Jira Server channels.

Note: The `ALERT_NOTIFICATION_MAPPING_BATCH_LIMIT` variable is intended to be used only upon the advice of customer support.

**Resolved issues**

- IALERT-3887 Resolved Jira Cloud API endpoint error by upgrading to use of API v3.
- IALERT-3878 Alert dropping notifications from batches without mapping jobs.
  - The Alert startup process has been revised to continue mapping notifications that remain unprocessed to distribution jobs, facilitating the transmission of data to third-party integrations.
  - Only notifications from enabled provider configurations that have not been processed will be mapped to notifications and will resume being sent to third-party integrations.
- IALERT-3831 Implemented timeout configuration capability to resolve an issue with Jira channel read actions timing out when querying for issues.

## Release Notes Version 8.2.0

**New Features**

Jira 10 is now supported when Alert is used with `alert-issue-property-indexer` version 0.1.0 or later.

**Changes**

- IALERT-3803 A script is now available to allow Alert installation against an external EnterpriseDB database.

  - See the following troubleshooting section for EnterpriseDB.

    Note: Alert is tested and supported against PostgreSQL, varriants such as EnterpriseDB may function in PostgreSQL compatibility mode but are not officially supported.
- Upgraded PostgreSQL support from version 15 to 16 for the packaged version of the database.
- For external PostgreSQL support, Alert now supports versions 15 and 16.
- IALERT-3811 Alert no longer supports adding multiple “Descriptor Name” of the same name and context to a role. Duplicates are no longer accepted.

**Resolved issues**

- IALERT-3853 Resolved an error thrown by `deployment/helm/database-utilities.sh` when special characters were used in setting a search keyword.
- IALERT-3855 Restored the ability to edit user information and confirm password change without requiring a username change.
- IALERT-3804 Resolved an issue where the mandatory password field was ignored whan creating a user with only name and email supplied.
- IALERT-3806 Resolved an issue where the "Fill Form" button on the SAML configuration modal may not be fully accessible.
- IALERT-3808 Resolved issue related to user creation validation: "Create" button was available when required fields were not yet populated.

**Dependency updates**

- Upgraded spring boot dependency to version 3.3.13
- node-sass dependency has been replaced by sass 1.69.5
- Internal Black Duck dependencies and their associated third party requirements updated for security and product stability.

## Release Notes Version 8.1.0

**Changes**

- The settings for `mountPath` and instance `name` for Postgres are now configureable with the `values.yaml` file.
- The logic within `postgres.yaml` has been expanded to support a `subPath`.
- `subPath` support has been added to address an issue where some storage classes on cloud create a lost+found directory when initialized and if this occurs within the Postgres data directory, Postgres throws errors.
- Changing the `mountPath` will change where the lost+found directory is created, and the inclusion of a `subPath` will maintain the ability to mount the data directory.

Example customized `values.yaml` content shown below:

```
volumeMounts:
    - mountPath: /var/lib/postgresql<
      name: alert-postgres-data-volume
      subPath: data
```

Note: Differences in storage classes and Postgres versions preclude defining a default value for `subPath`. If a `subPath` is needed for your deployment, please update the `values.yaml`.

- Added support for the Jira Server custom field type of `any`.
- Added support for the Jira Cloud custom field type of `object`.
- Added the option to parse the Jira custom field value as JSON and serialize the JSON as the custom field value.
- Jira custom mapping fields now allow users to configure the override value.

  - Instead or Alert requesting the custom field type from Jira, the override will expect the value field content to be a JSON object or array, parse it, and send the resulting JSON to Jira as the custom field content.

**Resolved issues**

- Fixed an issue where content from edits to existing custom fields was not saved and required the field to be deleted and re-added with the updated value.

## Release Notes Version 8.0.2

**Resolved issues**

- IALERT-3821 Jira Cloud and Server will now update duplicates if duplicate issues are found.
- IALERT-3817 To avoid creating duplicates, Jira Cloud and Server channel configurations and background tasks will be checked on startup to update issues created with Alert issue property indexer 0.0.5 or earlier.

## Release Notes Version 8.0.1

**Resolved issues**

- IALERT-3805 A blank page is no longer displayed at https://<BD_URL>/alert/ when Alert is deployed with Black Duck SCA 2025.1.1 or later. With Alert 8.0.0 and previous Black Duck SCA versions, a blank page would also be displayed when configured to use SAML, and SAML would redirect to the Alert UI.

## Release Notes Version 8.0.0

- The Synopsys alert-issue-property-indexer has been replaced by the Black Duck alert-issue-property-indexer. If using the Synopsys Alert-issue-property-indexer as part of a Jira integration, you must manually replace it with the new Black Duck alert-issue-property-indexer prior to running Alert 8.0.0 or later. See the Jira section in Configuring Channels in Alert for instructions.
  - The download site for Synopsys alert-issue-property-indexer for Alert 7.2.0 and earlier will be discontinued as of February 2025.

**Changes**

- Alert now supports account locking for failed authentication attempts. By default a user has 10 login attempts before the account is locked for 10 minutes.

  - The user login window will display an “Account temporarily locked” message on the login screen if a user exceeds the configured amount of failed local or LDAP account login attempts.
  - See the administrative settings for login attempts and lockout duration Alert environment variables.
- Base Docker images have been updated to Alpine Linux 3.20, Postgres 15.8, and RabbitMQ 3.13.
- IALERT-3554 Resolved an issue with Alert failing to connect Azure PostgreSQL flexible server.

  - A new flag `postgres.sslMode` has been added when using an external DB with helm. This flag should be configured to use a valid ssl mode supported by Postgres [See Postgres SSL](https://www.postgresql.org/docs/current/libpq-ssl.html#LIBPQ-SSL-PROTECTION).
    - The default ssl mode is now set as ‘disable' throughout the deployment files.
    - With SSL enabled, if `postgres.sslUseFiles` is true, Alert will now individually verify the settings; `postgres.sslSecrets`, `postgres.sslSecrets.sslKeyKey`, `postgres.sslSecrets.sslCertKey`, and `postgres.sslSecrets.sslRootCertKey`. For any flags set, the deployment will add the secret to the pod.
    - The docker-entrypoint script for Alert will now dynamically configure the DB connection string for sslkey, sslcert, and sslrootcert. If the script finds the value to be set, it will include it in the connection string otherwise it will not be included.

      Note: `sslKeyKey` and `sslCertKey` values must both be specified. Configuring just one or the other is invalid, and they will be ignored when Alert starts.
- IALERT-3739 Upgraded UI dependency bootstrap to 5.x to prevent high vulnerability.
- IALERT-3679 As of 8.0.0 when creating a new user, or updating an existing user’s password, the following password rules apply:

  - Contains at least:
    - one lower case character
    - one upper case character
    - one number
    - one symbol
  - Must be between 8 and 128 characters long
  - Not an easy to guess password (i.e. “password”)

**Resolved issues**

- IALERT-2901 Resolved a bug in the audit-statuses API where sorting by name separates lowercase and uppercase distribution names instead of sorting them together.
- IALERT-3615 Link to the "API Documentation (Preview)" in Alert UI missing the port number.
- IALERT-3685 Validation has been added for the password confirmation field when adding a user or updating the password for an existing user.
- IALERT-3765 Resolved an issue occuring when editing distribution jobs with projects under "Filter by Projects," causing projects to appear blank.
- IALERT-3554 Addressed an issue where Alert fails to connect to an Azure PostgreSQL flexible server due to SSL configuration issues.

  - See change note above re: `postgres.sslMode`
- IALERT-3676 Resolved an issue of missing Content-Security-Policy (CSP) header in the server HTTP responses improving security.
- IALERT-3563 Resolved an issue in email distribution jobs where the number of pages returned while filtering additional email addresses was incorrect.

## Release Notes Version 7.2.0

**Changes**

- Upgraded Postgres support from version 14 to 15.

**Resolved Issues**

- IALERT-3610 Updated the following third party libraries to resolve known vulnerabilities: spring-boot

## Release Notes Version 7.1.2

**New Features**

- You can now filter a paginated list when searching by name for Projects on the Distribution page.

**Changes**

- When configuring a Black Duck provider the test of the provider configuration previously validated the API Token user’s access for notifications by confirming they had one of Global Project Viewer, System Administrator, Super User, Global Project Administrator, or Global Project Group Administrator roles. As of this release, Alert first verifies if an appropriate role is assigned to the user and if not, their [Watched Projects](https://documentation.blackduck.com/bundle/bd-hub/page/InternalProjects/WatchedProjects.html) are checked to see if they have notifications enabled for at least one project. If the user has notifications enabled on at least one watched project, the specified role is not required and Alert will process notifications for any projects for which the user has notifications enabled.

  - When an issue tracker (e.g. Jira), is configured, Alert will add a link to the issue within the Black Duck project version where any discovered vulnerabilites are reported. To link an issue back to Black Duck the user requires either the ‘Global Project Manager’ or ‘Global Project Administrator’ role. If the configured API Token is for a user where the "Watched Projects" functionality is used, Alert will show a 403 Forbidden error & stack trace in the log if they do not also have either the ‘Global Project Manager’ or ‘Global Project Administrator’ role. The issue will still be created within the tracking system, but it will not be linked back to Black Duck.

Tip: The ‘Global Project Administrator’ role is also used for role based validation. If you are trying to limit the notifications sent to Alert, you should instead use ‘Global Project Manager’.

- Removed the unused channel name when configuring a Slack distribution job.

**Dependency updates**

- alert-issue-property-indexer plugin updated to remove redundant EULA.txt.

**Known issues**

- Jira Server installation plugin does not work with Jira software 9.5.x+. It is recommended to install the plugin manually on your Jira Server/Datacenter instance.
- Additional email addresses displayed as search results may display incorrect page numbers or empty pages.
- With the configuration value for `ssl:` set to `true`, and the `sslUseFiles:` value set to `false`, an error may be returned. It is recommended to fully enable ssl, set `sslUseFiles` to true, provide client key/certificates and root CA certificate, or provide a root CA certificate as outlined in the following troubleshooting section SSL configuration issue when sslUseFiles is set to false.
- Searches for dates and times in the Distribution and Audit Failure tables do not work as expected. For Audit Failures the date and time searched match the content of the notification. For Distribution Jobs the search for a timestamp does not work.
- Email distribution job notifications may log an error during deletion of a project and not send a notification. This is due to the system attempting to look up a nonexistent email recipient from the deleted project.
- Helm deployments may fail to deploy using certain storage configurations. See the Troubleshooting section of this document for more information. Troubleshooting.

## Release Notes Version 7.1.1

**Resolved Issues**

- IALERT-3617 Resolved an issue where the “Retain Unmatched File Data” setting has been changed via Black Duck, either globally or for an individual project, and you try to configure specific projects within a distribution job, Alert was throwing an exception and would not display any projects in the project drop down.
- IALERT-3640 Updated the following third party libraries to resolve known vulnerabilities: snakeyaml, santuario:xmlsec

**Known issues**

- Jira Server installation plugin does not work with Jira software 9.5.x+. It is recommended to install the plugin manually on your Jira Server/Datacenter instance.
- Additional email addresses displayed as search results may display incorrect page numbers or empty pages.
- With the configuration value for `ssl:` set to `true`, and the `sslUseFiles:` value set to `false`, an error may be returned. It is recommended to fully enable ssl, set `sslUseFiles` to true, provide client key/certificates and root CA certificate, or provide a root CA certificate as outlined in the following troubleshooting section SSL configuration issue when sslUseFiles is set to false.
- Searches for dates and times in the Distribution and Audit Failure tables do not work as expected. For Audit Failures the date and time searched match the content of the notification. For Distribution Jobs the search for a timestamp does not work.
- Email distribution job notifications may log an error during deletion of a project and not send a notification. This is due to the system attempting to look up a nonexistent email recipient from the deleted project.
- Helm deployments may fail to deploy using certain storage configurations. See the Troubleshooting section of this document for more information. Troubleshooting.

## Release Notes Version 7.1.0

**New features**

- Alert now supports client certificate configuration to allow for establishing Mutual TLS connections to the channels.
  - See the certificate configuration page.

**Resolved Issues**

- IALERT-3640 Updated the following third party libraries to resolve known vulnerabilities: spring-security-core, spring-security-config, tomcat-embed-core, spring-webmvc, spring-web

**Changes**

- Updated the Atlassian Jira plugin for compatibility with Jira 9.12.0.

**Known issues**

- When the “Retain Unmatched File Data” setting has been changed via Black Duck, either globally or for an individual project and you try to configure specific projects within a distribution job, Alert will throw an exception in the log (“Could not parse the provided jsonElement with Gson”) AND will not display any projects in the project drop down.

  - See the following troubleshooting section Retain Unmatched File Data configuration error
- Jira Server installation plugin does not work with Jira software 9.5.x+. It is recommended to install the plugin manually on your Jira Server/Datacenter instance.
- Additional email addresses displayed as search results may display incorrect page numbers or empty pages.
- With the configuration value for `ssl:` set to `true`, and the `sslUseFiles:` value set to `false`, an error may be returned. It is recommended to fully enable ssl, set `sslUseFiles` to true, provide client key/certificates and root CA certificate, or provide a root CA certificate as outlined in the following troubleshooting section SSL configuration issue when sslUseFiles is set to false.
- Searches for dates and times in the Distribution and Audit Failure tables do not work as expected. For Audit Failures the date and time searched match the content of the notification. For Distribution Jobs the search for a timestamp does not work.
- Email distribution job notifications may log an error during deletion of a project and not send a notification. This is due to the system attempting to look up a nonexistent email recipient from the deleted project.
- Helm deployments may fail to deploy using certain storage configurations. See the Troubleshooting section of this document for more information. Troubleshooting.

## Release Notes Version 7.0.1

**Resolved Issues**

- Resolved an issue where the selection of more than 10 email addresses when configuring email distributions was only configuring 10.

**Known issues**

- Additional email addresses displayed as search results may display incorrect page numbers or empty pages.
- With the configuration value for `ssl:` set to `true`, and the `sslUseFiles:` value set to `false`, an error may be returned. It is recommended to fully enable ssl, set `sslUseFiles` to true, provide client key/certificates and root CA certificate, or provide a root CA certificate as outlined in the following troubleshooting section SSL configuration issue when sslUseFiles is set to false.
- When upgrading from 6.12.X, data in Audit Failure and Distribution Jobs tables will be lost due to table and data format differences as of release 6.13.0. These tables will be populated with the new data generated by jobs executed after upgrade.
- Searches for dates and times in the Distribution and Audit Failure tables do not work as expected. For Audit Failures the date and time searched match the content of the notification. For Distribution Jobs the search for a timestamp does not work.
- Email distribution job notifications may log an error during deletion of a project and not send a notification. This is due to the system attempting to look up a nonexistent email recipient from the deleted project.
- Helm deployments may fail to deploy using certain storage configurations. See the Troubleshooting section of this document for more information. Troubleshooting.

## Release Notes Version 7.0.0

Important: Customers that are still on PostgreSQL 12.11 should upgrade to Alert 6.13.x before upgrading to 7.0.0.

**Resolved issues**

- IALERT-3242 To resolve high severity security vulnerabilities identified in PostgreSQL Database Server 12.11 we will be updating the base supported migration version to PostgreSQL 14.8.

  - Deployments utilizing external databases are supported for version 14.5 or greater, however it is recommended to upgrade to 14.8
- IALERT-3243 Update RabbitMQ Docker image to 3.11-alpine to resolve security issues.
- IALERT-3454 Resolved an issue where editing existing SAML users, role changes were not persisting. The SAML user roles were rewritten upon logging in.

  The behaviour is now the following:

  - SAML users will be regranted additional roles that were added via Alert.
  - Roles that are granted by the SAML provider app will be regranted if they were removed via Alert.
- IALERT-3374 Resolved an issue with pagination on the 'Audit Failures' page displaying rows incorrectly. We now display the data as showing an audit failure, where the user can click the intended row's 'View' icon cell to show the amount of failing jobs within that row.

**Changes**

- Added support for Jira Server version 9 and authentication using personal access tokens.

  - See new environment variables
- Alert, and associated Docker images, have been upgraded from Java 11 to Java 17 in anticipation of active support for Java 11 ending September 2023.
- Removed the "Assertion Signing" option from SAML configuration in alignment with its removal from the spring-security SAML library.
- The look and feel of the UI has been updated, including table appearance, data entry, and associated operation improvements for usability.

**Known issues**

- With the configuration value for `ssl:` set to `true`, and the `sslUseFiles:` value set to `false`, an error may be returned. It is recommended to fully enable ssl, set `sslUseFiles` to true, provide client key/certificates and root CA certificate, or provide a root CA certificate as outlined in the following troubleshooting section SSL configuration issue when sslUseFiles is set to false.
- When upgrading from 6.12.X, data in Audit Failure and Distribution Jobs tables will be lost due to table and data format differences as of release 6.13.0. These tables will be populated with the new data generated by jobs executed after upgrade.
- Searches for dates and times in the Distribution and Audit Failure tables do not work as expected. For Audit Failures the date and time searched match the content of the notification. For Distribution Jobs the search for a timestamp does not work.
- Email distribution job notifications may log an error during deletion of a project and not send a notification. This is due to the system attempting to look up a nonexistent email recipient from the deleted project.
- Helm deployments may fail to deploy using certain storage configurations. See the Troubleshooting section of this document for more information. Troubleshooting.

## Release Notes Version 6.13.2

**Resolved issues**

- IALERT-3448 Resolved issue with Alert failing to start in a hosted GCP environment due to the default Postgres ID for PG admin not having sufficient permission.
- IALERT-3456 Resolved an issue with Alert failing when not restarted after a DB import.

  - Alert supports the restoration of a database dump into an Alert instance of the same version as the dump. After restoring a database, Alert must be restarted.

## Release Notes Version 6.13.1

**Resolved issues**

- IALERT-3041 Logging validation errors on initial startup when non-required fields are not configured
- IALERT-3347 psql can fail but still return a 0 exit status
- IALERT-3307 When distributing multiple email alerts simultaneously, the contents of the CSV attached could contain entries for the wrong project.
- IALERT-3337 Multiple rule violation notifications occurring at the same time could cause Alert to incorrectly include filtered policies when creating messages.
- IALERT-3285 Resolved an issue where Alert didn't receive Issue tracker (Jira Server, Jira Cloud, Azure Boards) ticket updates.
- IALERT-3419 Resolved an issue with column sorting, by notification type, on Audit Failures.
- IALERT-2535 Alert now throws a 400 error instead of 500, when updating a user if the User ID is incorrect.

**Changes**

- For Helm deployments, we will now confirm that the Postgres admin user configured in the values.yaml, has admin permissions. If the configured Postgres admin user does not, the pod will not start and you will get an error:

```
<date stamp> Validating postgres admin permissions
<date stamp> ERROR: Validating postgres admin permissions (Code: 1).
```

- On startup, Alert will now only perform validation for a handler (proxy, encryption, Azure Boards, LDAP, SAML, Email, Jira Server if that handler has at least one environment variable configured. If no environment variables are configured for a handler, that handlers' validation is not run. If some environment variables are configured for a handler, but not all required, ERROR messages will be logged.Previously, validation was always performed and multiple extraneous ERROR messages would be logged on startup.
- Validation is now performed when testing LDAP configuration to ensure a valid LDAP configuration has been provided, including a valid test username and password. Users will be prevented from clicking the "Send Test Message" until a valid test username and password is provided.
- When mismatched data is passed in via API's for User, Group, or Certificate, users will now receive an appropriate error instead of a 500. See example below.

```
{
    "timestamp": "2023-02-27T13:40:49.659+00:00",
    "status": 400,
    "error": "Bad Request",
    "message": "IDs in request do not match",
    "path": "/alert/api/configuration/user/4"
}
```

- Updated the databaseUtilities scripts for Docker and Helm deployments to default to plain text backup and restores.
- Added a new option -t to specify the format of 'plain' for plain text or 'binary' for the binary format for backups and restores.

**Known issues**

- Searches for dates and times in the Distribution and Audit Failure tables do not work properly. For Audit Failures the date and time searched match the content of the notification. For Distribution Jobs the search for a timestamp does not work.
- Email distribution job notifications may log an error during deletion of a project and not send a notification. This is due to the system attempting to look up a nonexistent email recipient from the deleted project.
- Helm deployments may fail to deploy using certain storage configurations. See the Troubleshooting section of this document for more information. Troubleshooting.
- Rows in the Audit failure table represent a grouping of data by notification, therefor fewer rows may be displayed than the selected page size due to multiple entries appearing under each notification type. (Counting the number of jobs from the details dialog of each row in the table will equal the page size displayed in the UI.)
- In the latest spring-security SAML library implementation, the `WantAssertionsSigned` flag was removed due to the option causing responses not to be signed. [SAML metadata WantAssertionsSigned might cause Identity Providers to not sign response](https://github.com/spring-projects/spring-security/issues/10844)

  - SAML responses must be signed for encrypted assertions to be decrypted. For Alert users that checked the option we emulate assertion signing any authorization request by passing in a filter to check if the assertion is signed. While this gives users a bit more security, it prevents an option which is valid under SAML specification, (signed response, unsigned assertions). Users may or may not be aware of this and to prevent confusion, we will remove the option in a future release of Alert. It is advised to turn this option off in the meantime unless the IDP is configured to have assertions signed.
- In Alert versions 6.6.0 to 6.13.2, `package-lock.json` has references to the internal Synopsys Artifactory instance. This means trying to run a server locally `(./gradlew runServer)` that is not in the Synopsys network will fail. Delete the file `ui/package-lock.json` and the folder `ui/node_modules` as a workaround for the correct `package-lock.json` to be generated.

## Release Notes Version 6.13.0

**Resolved issues**

- IALERT-3059 Fixed an issue where testing Jira Server global configuration would fail if there were no issues for any projects against a freshly installed Jira Server instance.
- IALERT-3117 Upgraded SAML implementation to spring-security-saml2-service-provider in order to address security vulnerabilities.
- IALERT-3330 Extraneous whitespace removed from Alert quickstart guide yaml example.

**Changes**

- LDAP and SAML settings have been separated into multiple configurations and are now presented in the UI under indiviudal tabs in the Authentication section. Current SAML users will need to modify configuration settings in the IdP. See the Authentication section for more information.
- Project version links, in Alert Distributed Job emails, now point to the Components tab instead of the Details tab.
- Improved validation and logging related to LDAP Group configuration.
- Fixed an issue where testing the global configuration for Jira Server would fail if the Jira Server has "disabled empty JQL queries" enabled.
- With the new SAML configuration for Alert, user email addresses are now preserved and updated into the Alert database.
- The Audit page has been renamed, Audit Failures, as it now displays only those notifications that failed to send.

## Release Notes Version 6.12.2

**Resolved issues**

- IALERT-3277 Resolved an issue with duplicate email notifications being sent at different times from daily scheduled distribution jobs.

## Release Notes Version 6.12.1

**Resolved issues**

- IALERT-1814 Corrected an orchestration file typo for the ALERT_CHANNEL_EMAIL_MAIL_SMTP_DSN_RET environment variable that was incorrectly specified as ALERT_CHANNEL_EMAIL_MAIL_SMTP_DNS_RET. (An additional change was made to be backwards compatible, and not break existing deployments using the incorrectly named variable.)

## Release Notes Version 6.12.0

**Changes**

- Upgraded Postgres from version 12 to 14

**Please see the migration/upgrading instructions in this document before upgrading to Alert 6.12.x**

- Swarm orchestration has been updated to comment out default DB settings for Postgres service. These defaults are now in the alertdb entry point script. Customer will need to set these in the orchestration as they did previously if they are not using the defaults
- Helm orchestration has been updated to consistently set imagePullPolicy to IfNotPresent for all images. This means if you already have an image with the name listed in the orchestration, Helm will not try to pull the image.
- Helm orchestration has been updated to use the same Docker image for Postgres as Swarm. Both now use blackducksoftware/blackduck-alert-db. (Previously Helm used a CentOS based image.)
- Helm orchestration variable names have been updated to reflect the new image source.

  - POSTGRESQL_MAX_CONNECTIONS —> POSTGRES_MAX_CONNECTIONS
  - POSTGRESQL_SHARED_BUFFERS —> POSTGRES_SHARED_BUFFERS
  - POSTGRESQL_USER —> POSTGRES_USER
  - POSTGRESQL_DATABASE —> POSTGRES_DB
  - POSTGRESQL_PASSWORD —> POSTGRES_PASSWORD
  - POSTGRESQL_ADMIN_PASSWORD —> POSTGRES_ADMIN_PASSWORD
- Helm orchestration has been updated to add a liveness Probe for Postgres.

**New features**

- Now supporting the configuration and use of multiple Azure boards.
- Database backup and restore scripts for Docker and Helm installs are now included with the installation files.

**Resolved issues**

- IALERT-3146 Update Postgresql to address high severity vulnerabilities.
- IALERT-3151 Update Spring Boot to resolve high severity vulnerabilities with its dependencies.
- IALERT-3195 Old REST endpoints not properly updating the global configuration model.
- IALERT-3138 Azure Boards may not authenticate when Alert is installed as part of an Alert deployment.

**Known issues**

- When running in environments using Ubuntu v18.04 with Docker v19.03 the blackducksoftware/blackduck-alert-db image will fail. The solution to this issue is upgrading Docker to a minimum of V20.10.

## Release Notes Version 6.11.1

**Resolved issues**

- Resolved an issue where Alert could not be deployed with a helm chart on a Kubernetes cluster (IALERT-3186)
- Resolved a security vulnerability issue with Apache Commons Text. (IALERT-3192)

## Release Notes Version 6.11.0

**New features**

- Added new endpoint to gather diagnostic information on Alert notifications and audit statuses (IALERT-3055)
- Alert will no longer perform validation of the Black Duck instance prior to each invocation of the Accumulator. The validation is done when the Provider is configured and when performing a Test Configuration of a Distribution (IALERT-3051)
- Created a reusable Page Header component to reduce the three in use and decouple the page header from the page content (IALERT-3032)
- Updated minimum requirements for CPU and memory of the containers (IALERT-2928)
- The container alert-database has been renamed and re-versioned. The new name is blackduck-alert-db. The version of the blackduck-alert-db image version will now match the Alert release version. (IALERT-2925)
- Changed the internal queuing mechanism to use RabbitMQ (IALERT-2770)

**Resolved issues**

- Resolved an issue where distribution jobs for email and Jira server were incorrectly marked as "global configuration missing" when in fact global configurations were properly configured (IALERT-3084)
- Resolved an issue when testing the provider portion of the Black Duck distribution job configuration. Ensure connection to Alert is valid (IALERT-3071)
- Updated Docker Swarm README files with the note (IALERT-3047)
- Fixed an issue where the "install-plugin" endpoint for Jira Server was not returning content after successfully installing the plugin (IALERT-3015)
- Upgraded internal container packages to address vulnerabilities (IALERT-3005)
- Upgraded JDK runtime to address security issues (IALERT-2945)
- Added search and sort capabilities to the Jira Server configuration table (IALERT-2848)

## Release Notes Version 6.10.0

**New features**

- Added the ability to select the Jira Server configuration to use for distribution for the Jira Server channel Distribution Jobs.(IALERT-2808)

**Resolved issues**

- Resolved an issue where the "Item URL" column of a CSV email attachment is not aligned properly. (IALERT-2907)
- Upgraded PostgreSQL JDBC Driver to address vulnerabilities. (IALERT-2882)
- Upgraded BusyBox linux library to address vulnerabilities. (IALERT-2931)

## Release Notes Version 6.9.0

**New features**

- The settings encryption page now disables configuration fields if the encryption password or encryption global salt are configured through environment variables or secrets during Alert installation.
- The policies and vulnerabilities are sorted by severity in the messages and created issues.
- The Proxy settings now have a Delete button for deleting the proxy configuration.
- Split the encryption and proxy configurations on the Alert Settings page into separate tabs.
- The Proxy settings now have a Test Connection button that validates the configuration.
- Added a new API endpoint that retrieves combined Audit and Job information.
- The 'Type' column in the Distribution table is now called 'Channel' to more accurately reflect the contents of that column.
- Removed audit sorting because limitations in JPA do not yet enable supporting sorting for the Distribution job table.
- Added a new API for global Email settings to Create, Read, Update, or Delete the configuration.
- In Distribution Jobs now enable specifying a Project Version Name Pattern to filter by version.

**Resolved issues**

- Configuring email channels through environment variables requires all required fields to create new email configurations.
- Configuring proxy settings through environment variables now requires all required fields to create a new proxy configuration.
- Changed the Audit Event Type column to Channel to represent its content more accurately.
- Upgraded JDK 11 to address vulnerabilities.
- Updated the version of OpenSSL in the container.
- The Distribution Job Test Configuration now shows a warning if the selected projects don't exist when the Black Duck configuration changes.
- HTTP status errors without any associated status are now more clear.
- Fixed an issue where a user without permissions needed to configure a channel would get a link to the configuration page, resulting in a blank page. If a user does not have permission to configure the channel, they only see the channel's name and not a link to the configuration page.
- Resolved an issue with the Jira Cloud error messages when the API token was invalid.
- You can now sort the Distribution Job columns.
- Updated Spring Transaction to address vulnerabilities.

## Release Notes Version 6.8.0

**New features**

- Optimized notification purging logic for faster cleanup and to prevent memory issues.
- Changed the Daily Task to check for Daily frequency jobs before starting to process the notifications. Now, the Daily Task notifications are processed a page at a time rather than trying to process them all at once.
- The Jira replacement values no longer list `providerName`as an option. Instead, they now show `providerType`. Previously, when we use the `providerName`variable, it showed only 'Blackduck'. In the non-custom summary, it now shows the Black Duck provider hostname, which is more useful information, especially since we have only 1 provider. For example:

  Previous Alert: Black Duck, P1 [v2], jQuery [1.7.0], HIGH

  vs

  Current Alert: Black Duck us1a-qa-hub07.nprd.testsys.com, P1[v1], Apache JMeter[3.2], Vulnerability
- Added support to enable/disable Postgres SSL for external Postgres database.
- Added a new field to the Jira cloud and server distribution jobs which allows the user to customize the summary of the issue that Alert creates. The following variables can be used to enter content from the message `providerName`, `projectName`, `projectVersion`, `componentName`, `componentVersion`, and `severity`.
- Added policy category placeholder value for Jira Custom fields
- "Non-proxy hosts" can now be specified in the global proxy settings. When a host is specified in the non-proxy hosts' field, Alert will not send network traffic to that host through the proxy. This field supports the wildcard character '*' (e.g. specifying* *.example.com* will match [*https://org.example.com*](https://org.example.com/) and [*server.example.com*](http://server.example.com/), but not [http://my-example.com](http://my-example.com/)).
- Added policy description when creating new policy notifications for issue trackers. Black Duck policies that contain a description will include a new "Policy Description:" message in the issue tracker description containing the description used in Black Duck.
- Slack messages sent via Apps/webhooks use the App name and no longer support setting the sender username.
- Added short and long-term upgrade guidance for security vulnerabilities as replacement fields for Jira Server/Cloud issue tracker.
- Added component usage and component license as replacement fields for Jira Server/Cloud issue tracker.
- Created a new Email Configuration API alongside the original Email API offering the same functionality with a payload that is easier to understand.
- Job name is now added for all channels at the top of the Alert message.
- These environment variable are no longer supported:

  `ALERT_COMPONENT_SETTINGS_SETTINGS_ROLE_MAPPING_NAME_ADMIN`

  `ALERT_COMPONENT_SETTINGS_SETTINGS_ROLE_MAPPING_NAME_JOB_MANAGER`

  `ALERT_COMPONENT_SETTINGS_SETTINGS_ROLE_MAPPING_NAME_USER`

**Resolved issues**

- Resolved an issue when using database credential secrets in Docker swarm where the Alert container could not connect to an external Postgres database (IALERT-2698).
- Resolved an issue with the Azure Boards channel where issues for a specific project or version were not resolved if a project or project version deletion notification was processed by Alert (IALERT-2695).
- Fixed Helm indentation issues that caused issues with deployment (IALERT-2682).
- Fixed an issue where Alert> would update Work Items in the wrong ADO Board if multiple Distribution Jobs were configured for the same notification (IALERT-2635).
- Resolved an issue where the Component License had an invalid link (IALERT-2634).
- Fixed an issue that would cause Alert not to process some notifications when more than 100 jobs are configured (IALERT-2618).
- Fixed an issue where not all the component additional attributes were aggregated correctly (Upgrade Guidance information, Policy Overridden by, Usage, License, and Provider Configuration) (IALERT-2603).
- Added upgrade guidance to the email with the JSON file attachment (IALERT-2601).
- Fixed an issue causing severities in summary notifications to use an unformatted label (IALERT-2564).
- Fixed an issue where notification messages could be received out of order. This issue also occasionally manifested itself as Audit failures in Azure Boards (IALERT-2562).
- Fixed Azure Boards connections to properly use proxy settings (IALERT-2540).
- Alert> no longer adds the user associated with the API Token in the Black Duck configuration to projects selected in the Distribution Jobs (IALERT-2532).
- The Black Duck API token in Black Duck global configuration is to be for a user with either the SuperUser role or the Global Project Viewer role (IALERT-2531).

## Release Notes Version 6.7.0

**New features**

- Added a new notification type called`COMPONENT_UNKNOWN_VERSION`. This notification will be created when a component is added to the BOM that does not have a version. When the User sets the version for the component, a notification will be created for the "Fuzzy version" component being deleted, and a new VULNERABILITY notification will be created if the version selected has vulnerabilities.
- Implemented Gradle build caching that can be enabled to significantly improve the performance of a `./gradlew` clean build.
- Now, `updateNpmVersion` runs whenever the version in the root`build.gradle` is changed.

**Resolved issues**

- Fixed an issue with COMPONENT_UNKNOWN_VERSION in the Distribution Notification Types dropdown being out of view(IALERT-2703).

## Release Notes Version 6.6.0

**New features**

- Added policy and vulnerability severity as a placeholder value for Jira Custom fields.
- Jira issue trackers will now display the highest vulnerability severity in the description of newly created issues. Updates to the issue will now include the current highest vulnerability severity in the comments.
- Added a flag to let the user decide if they want to sign their assertions when using SAML. This was defaulted to true originally and thus should be marked true for any users that upgrade.
- Added support for additional Array type fields in Jira Cloud and Jira Server. This includes Checkbox fields, Multi-Select fields, and the Component's field.
- Added support for the *ignoreSAML=true* query parameter to allow users to login as a local Alert user even if SAML is enabled. You no longer need to restart the server if there are issues with SAML, you can use this to login and disable SAML or fix the SAML configuration.
- Added a new button called *Fill Form* to the *SAML configuration* in the *Authentication* tab. This will fill in some of the SAML information from the selected Black Duck server
- When an LDAP user logs into Alert for the first time, the email address associated with the LDAP account will be included when saving a newly created Alert user.
- Added a checkbox to the SAML configuration to let the user decide if they want Alert to sign their assertions when using SAML
- Added documentation for the requirements to use an external database, refer to External Database Requirements
- Added policy and vulnerability severity as the dynamic field *{{severity}}* to populate custom fields for Jira Server and Jira Cloud. Jira Cloud and Jira Server issues will now also include the policy severity or the highest vulnerability severity in the description of the issue.
- Distribution Jobs that are selected across different pages of the Distribution Jobs Table will now appear in the Delete Jobs Modal.

Remember: If the checkbox to "unselect all" is clicked, it will remove all selected Distribution Jobs (including those on different pages).

- Added template support for Jira custom fields using replacement values.
- Added validation to prevent Users from removing the admin role from the default admin user.

**Resolved issues**

- Fixed an issue with distribution job names getting cut off. The names will now wrap if they are too long.
- Fixed an issue with styling that caused our tables to expand indefinitely when interacting with the table.
- Fixed an issue with Alert failing to create Jira tickets because the summary is too long.
- Fixed an issue where the CSV attachment in emails was empty for PROJECT_VERSION notifications (IALERT-2635).
- Fixed an issue that could cause Alert not to process some notifications when more than 100 jobs were configured.
- Resolved an issue wherein the Component License had an invalid link.
- Fixed an issue wherein Alert could update Work Items in the wrong ADO Board if multiple Distribution Jobs were configured for the same notification.
- Resolved an issue with the help text for the Processing field (IALERT-2643).
- Resolved an issue where the UI would show 'Task' as the Issue Type even after you changed it for Jira Server distribution jobs.

## Release Notes Version 6.5.4

**Resolved issues**

- Changed the Daily Task to check if there are any jobs configured for the Daily frequency before starting to process the notifications.
- Changed the Daily Task to handle a page of notifications at a time rather than trying to process them all at once.

## Version 6.5.3

**Resolved issues**

- Improved the initialization of Alert to tune and improve the embedded message queue system in the following ways:

  - Perform processing of notifications in a different thread
  - Reduce the queue prefetch limit for consumers to 100 from the default of 1000.
  - Split the memory usage limits for producers and consumers
- Resolved an issue when using database credential secrets in docker swarm where the Alert container could not connect to an external Postgres database.

## Release Notes Version 6.5.2

**Resolved issues**

- Reduced the number of connections/logins that Alert uses when sending emails (IALERT-2668).

## Release Notes Version 6.5.1

**New feature**

- We have created a new log file named alert_notification.log that can be found in the Alert container alongside the alert_audit.log. This new file will contain logs about the lifecycle of Black Duck notifications as they move through Alert. To see these new log messages in the file, DEBUG logging will need to be enabled for Alert, please refer to Enviornment variables for logging to configure the logging level.
- Optimized notification purging logic for faster cleanup and to prevent memory issues.

**Resolved issues**

- Fixed an issue when using the Project Owner Only field in the Email Distribution Jobs, where the code to collect the Project Owner email address was returning an empty value. (IALERT-2629)
- Fixed an issue with the way Alert requests pages of notifications from Black Duck and creates the next search range, which was causing duplicate notifications to be processed. (IALERT-2558)
- Fixed an issue which could cause Alert not to process some notifications when more than 100 jobs were configured. (IALERT-2618)
- Fixed an issue where Alert would sometimes fail to find jobs matching the notifications, due an issue with inconsistent ordering when retrieving jobs from the database. (IALERT-2577)
- Resolved an issue wherein the Component License had an invalid link. (IALERT-2634)

## Release Notes Version 6.5.0

**New feature**

- Enabled support for running Alert behind a load balancer by adding the `ALERT_FORWARD_HEADERS_STRATEGY` environment variable.
- Setting the `ALERT_FORWARD_HEADERS_STRATEGY` to `native` will signal Alert to use the `X-Forwarded` headers from requests made to Alert API's to construct the URL's to reach Alert. This will impact the Swagger URL that is shown in the user interface as well as the Azure OAuth handshake.

**Resolved issues**

- Resolved an issue wherein an action to manually remediate all vulnerabilities on a BOM component did not resolve the associated issue-tracker issue. (IALERT-2129)
- Resolved an issue with transitioning Jira tickets from the intermediate state to the resolved state. (IALERT-2382)
- Resolved a vulnerability concern about the Alert version 6.3.1 Docker image relating to an unused transitive dependency. (IALERT-2194)
- Fixed an issue wherein upgrades from previous patch versions of 6.4 could fail to upgrade to 6.4.3. (IALERT-2396)

**Changed features**

- Improved BOM Edit comments relevance for Jira/Azure issues.
- Alert notification accumulation is now presented in pages rather that one lot.
- Messages not tied to a Black Duck BOM Component will now have a simpler format.
- Improved error messages when invalid additional email addresses are used in a distribution job.
- Message content that is longer than the configured limit is now truncated and split into multiple messages instead of throwing an exception.
- Improved the admin password reset functionality to enable the capability for the reset to succeed in cases where the sysadmin username was changed.

## Release Notes Version 6.4.4

**Resolved issue**

- Resolved an issue wherein upgrades from previous patch versions of Alert 6.4 might fail to upgrade to 6.4.3. (IALERT-2399)

## Release Notes Version 6.4.3

**Resolved issues**

- Resolved an issue with timing out and returning a 400 error message when integrating Alert with Azure Boards. (IALERT-2365)
- Resolved an issue with an Alert liquibase changeset that was causing an error for some customers when upgrading to the latest version of Alert. (IALERT-2369)

## Release Notes Version 6.4.2

**Resolved issue**

- Resolved an issue where Alert threw a null point exception when Black Duck responded with unknown or null *UsageTypes* for components. (IALERT-2351)

## Release Notes Version 6.4.1

**Resolved issues**

- Resolved an issue upgrading to Alert> 6.4.0 wherein database migration would fail with a non-unique index error if any distribution jobs had multiple Black Duck projects configured. (IALERT-2289)
- Resolved an issue upgrading to Alert 6.4.0 wherein null values could exist for some Black Duck projects selected in distribution jobs. (IALERT-2286)

## Release Notes Version 6.4.0

**New features**

- Added capability to populate a limited set of custom Jira fields in Alert distribution jobs with the capability to map static values or a limited set of information from Black Duck notifications. Jira Server and Jira Cloud distribution jobs have an Advanced Jira Configuration section where you can configure custom Jira fields.
- Added caching for the requests made to Back Duck to reduce the volume of repeated requests.

**Resolved issues**

- Resolved an issue wherein asterisks (**) were added as placeholder text in plain-text fields, which led to the discovery of the following issue that is also resolved:

  - Resolved an issue with Azure Boards' global configuration that caused the *Client Id* field to be visible in plain-text when a user typed a new value (when the configuration was saved, the value became secret, but before it was saved there was no obfuscation in the text field). (IALERT-2112)

**Changed features**

- The Black Duck project and user data is no longer synced with the Alert database tables every minute. The sync now occurs once a day until systems can safely retrieve the information on-demand. The repository objects and entities relating to the Black Duck provider project and user tables in Alert are deprecated.
- Black Duck request-caching is used when saving Distribution Jobs that *filter by project*.
- Black Duck projects and users that were updated/deleted less than 2 minutes prior to creating a Distribution Job might not be updated by Alert. This can be resolved by waiting 2 minutes after creating a new project or user before saving the Distribution Job, or resaving the Distribution Job after such a change in Black Duck>.
- Alert (ProviderDataAccessor) now retrieves Black Duck project and user data information directly from Black Duck rather than using the database tables in Alert>.

## Release Notes Version 6.3.1

**Resolved issues**

- To Resolve an authentication issue with Azure Boards when Alert> is installed using Helm, users must manually configure the exposedNodePort. (IALERT-2069)
- To resolve an issue with the Alert Swagger UI link defaulting to port 8443 when Alert is installed using Helm, users must manually configure the exposedNodePort. (IALERT-2080)

**Changed feature**

- For Black Duck versions 2020.10.0 and later, Synopsys will show the upgrade-guidance to replace the remediating information that was removed from Black Duck.

## Release Notes Version 6.3.0

**New features**

- Added additional audit logging for User and Role changes in Alert.
- Added the project version to the email subject line of emails that Alert sends.
- Added API documentation **API Documentation (Preview)** on the Alert **About** page. This API documentation is labelled as Preview and is not stable in this first release.
- Added a **Disable Plugin Check** field to Jira Cloud and Server channels, which can be used to disable checking for the installation of the **Alert Issue Property Indexer** plugin on the Jira instance. This enables non-admin users to be configured in the Alert Jira channels with the required access to manage issues create by Alert in Jira.

  - Added the capability to configure non-admin users in the Jira channels instead of being forced to use an admin user. This capability is used in conjunction with the **Disable Plugin Check** option.

**Changed features**

- Improved LDAP role mapping by enabling it to read the database role assignments for LDAP users.
- LDAP and SAML user's that login into Alert> now have the ALERT_USER role assigned to them on first login, by default.
- Users can now verify that the SAML configuration is valid at startup.

**Resolved issues**

- Resolved an issue that occurred when the **Alert Issue Property Indexer*** plugin was already installed, the Jira Cloud *Test Configuration* would succeed. The fix forces Alert to explicitly check for the Jira *ADMINISTRATOR* permission for both Jira Cloud and Jira Server users that are configured with Alert. If the *ADMINISTRATOR* permission is not granted and ***Disable Plugin Check*** is not checked, the ***Test Configuration*** will fail. (IALERT-1888)
- Resolved an issue where an error message was not displayed to the user when an error occurs authenticating with LDAP. (IALERT-1865)

**Known issues**

- When you install Alert using Helm, the correct links are not created for the following:

  - The Azure Boards channel will not work because the callback URL will have the wrong port. (IALERT-2095)
  - The swagger link in the about page will have the wrong port. (IALERT-2095)
  - Any links back to Alert in the messages to channels will have the wrong port. (IALERT-2095)
- Vulnerability notifications do not include remediation information in Alert when Black Duck 2020.10.0 or later is used. (IALERT-2083)

## Release Notes Version 6.2.1

**Resolved issue**

- Resolved an issue where the proxy settings were not being used in connections to Jira Cloud and Jira Server.

## Release Notes Version 6.2.0

**New features**

- Added a **View** column to the Task Management screen to enable users to click the icon on a specific row to view task details.
- Added Azure Boards Channel in Alert, which enables the creation of Work Items in Azure, which are based on Black Duck notifications.
- Added hostname value to `values.yml` file for deploying Alert using Helm.
- Alert now adds issue links in Black Duck for issues that are created through Alert's issue tracking channels such as Jira Cloud and Azure. The issue links in Black Duck provide an easy way to find Alert-created issues for specific BOM Components.

These links can be found in Black Duck Project BOMs that have at least one component for which:

```
-   Alert has created an Issue Tracking Channel issue.

-   Alert has created/updated an Issue Tracking Channel issue for the component since upgrading Alert to version 6.2.0.
```

**Changed features**

- Only policy rules that are enabled in Black Duck will be listed as filterable options in distribution jobs.
- Moved the **Provider Configuration** Name field under the **Provider Type** field.
- Improved error messaging for when Jira ticket creation/transition fails because the status category is not set appropriately in Jira.
- Added warning message when transition fields are not populated by the user in a distribution job that is configured for Jira Cloud or Jira Server.
- In a distribution job, disabled policies are no longer available for selection in the **Policy Notification Type Filter**.
- The *Summary* processing type is removed as an option in the user interface when you create a Distribution Job for the issue tracker channels such as Jira Cloud, Jira Server, or Azure Boards. Using the *Summary* processing type with the issue tracker channels will result in unexpected behavior with the issues that are created.

**Resolved issues**

- Resolved an issue that blocked Azure AD SAML configuration.
- Resolved an issue wherein errors that occurred with Jira issue creation when using Test Configuration in Alert Distribution screen are not shown to users.
- Resolved an issue with the volume mount path in the Helm chart for the PostgreSQL database to preserve data.

## Release Notes Version 6.1.1

**Resolved issues**

Resolved an issue with the volume mount path in the Helm chart for the PostgreSQL database to preserve data.

## Release Notes Version 6.1.0

**New features**

- Select fields that contain a select button and display a table, now have a clear button to remove all the selections from the field, which makes it easier to reset the field and be able to change the selection to a subset of all the possible values.

**Resolved issues**

- Resolved a consistency issue with date-time fields in the Audit table.

  The format is now as follows: *yyyy/MM/dd HH:mm:ss*

  For example: 2020/06/10 12:33:17
- Updated tooltip text in the Jobs table.
- Resolved an issue wherein the configured Provider information is not displayed on the About screen when a user is logged with the Alert user role.
- Resolved an issue with misaligned text on the certificate import screen.
- Resolved issues with testing the configuration and saving the Global Configurations for email, Jira Cloud, and Jira Server channels when adding or editing a provider configuration.
- Resolve an issue with text-overflow on the Audit page.
- Resolved an issue wherein a custom role that was created with all global permissions and no distribution level permissions had no navigation and the About screen information was minimal.
- Resolved an issue wherein testing a Black Duck Provider Configuration did not display an error message in the modal when Black Duck was not connected.
- Resolved an issue wherein the **Select** and **Clear** buttons were overflowing the screen area when a long name was added to the Projects field on the Job Distribution screen.

**Changed features**

- Improved the 404 error messaging that occurs when the message is about the marketplace listing of the Alert Issue Property Indexer app not supporting your version of Jira.
- Improved the 403 error messages in the user interface, depending on the action you are attempting in the user interface, for example, 'you are not permitted to view its information' or 'you are not permitted to perform this action'.
- Moved the Provider Configuration field under the Provider Type field in the Distribution Job screen.

## Release Notes Version 6.0.2

**Resolved issues**

- Resolved an issue with the volume mount path in the Helm chart for the PostgreSQL database to preserve data.

## Release Notes Version 6.0.1

**Resolved issues**

- Resolved an issue wherein renaming a Provider Configuration did not update the Distribution jobs configured for it properly.

## Release Notes Version 6.0.0

**New features**

- Added the Certificates page to enable Alert users to manage certificates.
- Added the option to enable or disable providers and to provide a unique name for the provider configuration.
- Added the **Enabled** checkbox to enable/disable the use of the provider, and the **Provider Configuration** *name* field to the Provider page.
- Added new field to the Distribution screen, where users can select a specific **Provider Configuration** by name for the distribution job.
- The **Provider Configuration** name field is added to the CSV file attachment for emails.
- Added the capability to add multiple Black Duck provider configurations on the Black Duck provider screen.
- Added the Task Management page that shows data about the tasks that are currently running within the Alert system.
- Added a SAML and LDAP configuration test capability to the authentication screen that enables users to test the configuration.
- Added capability in Alert to connect to an external PostgreSQL database, which can be configured in the Alert YAML file.
- Added a hyperlink to the project field in Alert notifications that links to the project in Black Duck.

**Changed features**

- Several LDAP and SAML environment variables that start with: *ALERT_COMPONENT_SETTINGS_SETTINGS_*... are no longer supported and have changed to *ALERT_COMPONENT_AUTHENTICATION_SETTINGS_*..., for example, *ALERT_COMPONENT_SETTINGS_SETTINGS_LDAP_SERVER* has changed to *ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_SERVER*.
- The environment variables: PUBLIC_HUB_WEBSERVER_HOST and PUBLIC_HUB_WEBSERVER_PORT are removed from Alert> and have been replaced by ALERT_HOSTNAME and ALERT_SERVER_PORT.
- The volumes for the Alert> container and the new AlertDB container must point to the same location.
- The minimum compatible Black Duck version for Alert 6.0.0 and later is 2019.12.0.
- The **Format** field name in the distribution job configuration is renamed as **Processing**.
- The memory default value configured in the deployment files is changed from 512M to 640M to enable a better distribution between machine and application.
- Removed the deployment files for Docker Compose because Black Duck no longer supports Docker Compose.
- Added two new environment variables that are used to configure the Black Duck Provider.
- Removed the environment override variable.
- Added a new LDAP, SAML, and password reset environmental variables.
- Alert only supports TLS 1.2 and 1.3.
- Alert no longer creates a backup.zip of the database on startup, because it now uses a separate PostgreSQL database.

**Resolved issues**

- Resolved an issue wherein users were unable to add security contexts in Alert 5.1.0 by adding the capability to add security contexts for Alert.

## Release Notes Version 5.3.2

**Resolved issues**

- Resolved an issue with Alert checking that the Alert Issue Property Indexer is installed on the Jira server.

## Release Notes Version 5.3.1

**Resolved issues**

- Resolved an issue wherein a null pointer exception occurred when trying to connect to Jira from Alert.
- Resolved an issue wherein users could not log in to Alert as an LDAP user when LDAP authentication was configured in Alert.
- Made improvements in retrieving the severities of vulnerabilities that helps to prevent null pointer exceptions (NPE).

## Release Notes Version 5.3.0

**New features**

- Added a **Delete** button to the Black Duck Provider and Channels that enables the deletion of global configurations from the Alert server.
- You can now add CSV, JSON, or XML attachments to your email distributions.
- Added the **Enabled** column to the Distribution table that displays a checkmark or an **x** to show the enabled state of the job.
- When using Black Duck as the provider, new notification filtering options are available. Policies can now be filtered by policy name, and vulnerabilities can be filtered by severity.
- Added functionality to specify types of access for each user role.
- Added functionality to create custom roles.
- Added user management feature to the Alert user interface, which you use to add, remove, and modify Alert> users, and to edit roles and their permissions.
- You can update the passwords for the sysadmin, Job Manager, and Alert user default users in the User Management section.
- Added error messaging to notify users about missing global configuration in channels when you create new distribution jobs or open existing distribution jobs in Alert.
- A required field symbol (red asterisk) has been added to fields that require input.

**Changed features**

- Distribution jobs can now be enabled or disabled.
- Added messaging improvements for channels.
- You can edit rows in the Users/Roles table by double-clicking the selected row.
- The distribution jobs now display the name in red with a warning icon in the table when there are validation errors.
- Moved the default system administration settings from **Settings** to **User Management**.
- Improved messaging for users who log in with insufficient credentials to view the application.
- When changing a user password, you are prompted to confirm the password in the **Confirm Password** field.
- User roles from external systems such as LDAP and SAML, are added to the current role configuration in the Alert database for the logged-in user.

**Resolved issues**

- Resolved an issue wherein providing a webhook with an incorrect URL (Slack and MS Teams) returns no error or success shown in the job, and a stack trace printed to the Alert log.
- Resolved an issue wherein the **Jira Project** field in distribution jobs only accepted the name of the Jira project but not the key.

## Release Notes Version 5.2.3

**Resolved Issues**

- Resolved issue wherein users could not turn off comments in issues that were created in Jira Cloud and Jira Server; the issue description is now truncated to fit the allowed length of the Jira description field if **add comments** is unselected and no additional comments are added.
- Resolved an issue wherein a 404 error message that was generated when attempting to add a comment in a Jira Cloud issue; Alert now logs the error that occurred and continues processing.

## Release Notes Version 5.2.2

**Resolved Issues**

- Resolved an issue that occurred when Jira Cloud changed the expected payload for creating an issue.

## Release Notes Version 5.2.1

**Resolved Issues**

- Resolved an issue wherein users couldn't disable SAML so that they could log into Alert using the administrator account.

## Release Notes Version 5.2.0

**New features**

- Added*jobmanager* and *alertuser* as default users.
- Added the Jira Server channel.
- A last modified timestamp displays when clicking **Save** for any configuration provider, channel, or distribution configuration.

**Changed features**

- All authentication functionality is now moved from **Settings** to the **Authentication** section.
- Alert now sends notification emails even if an asterisk is included in the notification target project name in the Distribution job.
- LDAP, SAML, and User Management settings can be expanded or collapsed.
- Added support for Jira 8.x.
- Several environment variables from ALERT_COMPONENT_SETTINGS_SETTINGS_... have moved to ALERT_COMPONENT_AUTHENTICATION_SETTINGS_..., The old environment variables are supported until Alert version 6.0.0.

**Resolved issues**

- Resolved an issue wherein the wrong email addresses may be used for a project.
- Resolved issue with Alert becoming unhealthy when Black Duck project names were over 255 characters long by increasing the maximum length of project names accepted by Alert.

## Release Notes Version 5.1.0

**New features**

- Added a checkbox in the email channel for using only the additional email addresses.
- Slack now displays in the **Global** channel section to show that it is available for use. It does not require configuration.
- The descriptor configuration is now logged at startup.
- Added vulnerability information to security-related policy notifications, including remediation content.
- Tables that require you to select data; for example, the **Project** distribution table, are now replaced with a new type of field that hides the table and loads the data after you select the button to add data.
- Added **Project** and **Project Version** notification types.
- Added support for Microsoft teams.
- Usage information is now included in Black Duck-related notifications.
- Alert now accepts XML metadata files for SAML/SSO settings configurations.
- Added functionality for adding or removing uploaded metadata files.
- Added user role management, so that you can manually map LDAP users to Alert user roles. This contains the ability to customize or override the group names.
- Added the **Projects** table project selection options when creating a new distribution job.

**Changed features**

- The **About** screen is now accessed from the Alert logo, and contains your configuration information and your Alert version.
- Double-clicking a row in the **Distribution** table now opens the edit page.
- The **Notification** column in the **Distribution** and **Audit** tables no longer displays icons; instead, descriptive text displays.
- Summary messages now specify that they are in the summary format.
- Messages are now condensed.
- The *alert.templates.dir* property and the ALERT_TEMPLATES_DIR environment variable are now deprecated.
- Removed all non-functional, visual-only icons.
- Additional email addresses now display only after the provider is selected.
- The **Send Message** dialog box now enables you to send customized messages and subject lines when testing new distribution jobs.

**Resolved issues**

- Resolved an issue wherein installing Alert inside Black Duck may cause a 502 error.
- Resolved an issue wherein deploying Alert inside Black Duck with custom certificates may fail.
- Resolved an issue wherein the ALERT_ALWAYS_TRUST_CERT environment variable was not being used when checking for updates.
- Resolved an issue where importing a custom certificate could result in an error of *PKIX path building failed*.

## Release Notes Version 5.0.3

**Resolved Issues**

- Resolved an issue that prevented the removal of old notification data from the database.

## Release Notes Version 5.0.2

**Resolved Issues**

- Resolved an issue wherein users couldn't disable SAML so that they could log into Alert using the administrator account.

## Release Notes Version 5.0.0

**New features**

- You can now copy an existing distribution job. Therefore, you are no longer required to re-enter the same distribution job data.
- Added support for Jira Cloud as a channel.
- The default format collapses similar items for easier viewing.
- Added support for BOM edit notifications.
- Added support for installing the plugin remotely.
- Tickets can now be created based on Black Duck notifications.
- Added a new distribution job type for JIRA Cloud.
- Emails sent from Alert now feature a clickable link in the header to return you to Alert, and includes a footer with the Alert server URL.
- Added cloud environment variables.
- An automatic backup of the database is now performed. A zip file of the database is created every time prior to starting the process.

**Changed features**

- Changed **Include All Projects** to **Filter By Project.**
- Alert now assigns the configured user to the Black Duck projects configured in the jobs.
- Removed the **Reset Password** button.
- Ended support for HipChat.
- Existing tickets are automatically updated with status changes.
- Updated Alert host name environment variables.
- Added remediation information to regular vulnerability notification *ComponentItems.*
- Deployment files now have updated environment variables.
- Changed name of the secret salt encryption file.

**Resolved issues**

- Resolved an issue wherein Alert was reporting availability of a newer version when the newer version was the same as the current instance.
- Resolved an issue wherein the Alert server shown in update emails contained the wrong port number.

## Release Notes Version 4.2.0

**New features**

- Added Alert sensitive data storage options.
- When a new version of Alert is available, a *Warning* system message displays informing you that there is a new version available.
- Added new user roles.
- Black Duck default and digest messages now include component links to filtered listings depending on the selected component.
- Added SAML authentication.
- Added new variables for SAML.

**Changed features**

- **Save** and **Cancel** buttons for Email and Settings now remain in a fixed position; scrolling to the bottom to access these is no longer required.
- In the channel output, Black Duck policy entries now display their severity next to the name if the severity is set for that policy in Black Duck.
- The plugin now sorts the vulnerabilities listed by severity from high to low in all channels.
- Removed the Policy link from the email output.
- Added new summary format.
- Improved the Alert digest options.
- Improved component/version linking in email distributions.

**Resolved issues**

- Policy information now combines duplicates info into a single message when possible.
- Resolved an issue wherein some Slack messages, based on size, may be split into multiple messages by the Slack server.

## Release Notes Version 4.1.0

**New features**

- For each field in the user interface with description text, a help icon displays at the right of that field label. Clicking the help icon displays the description until you click elsewhere.
- You can now delete global configurations if all fields are empty.
- If the global configuration of a provider is cleared, then the related tasks that pull data from those providers is cancelled.
- Renamed Black Duck Alert to Synopsys Alert.

**Changed features**

- The field **Collecting Black Duck notifications in** is now changed to **Collecting Provider data in**, and the field **Notification Purge Frequency** is changed to **Data Purge Frequency**.
- Slack and HipChat distribution jobs now validate the **Project Name Pattern** field to verify that the pattern matches at least one existing project.
- Improved the process for running Alert and Black Duck in the same deployment.
- The Slack code limit notification now includes a link to the server referenced in the notification.

**Resolved issues**

- Resolved an issue wherein global configuration processes may be running without global process configurations being set up.
- Resolved an issue wherein background tasks were stuck waiting for other tasks to finish before executing.
- The next run time now correctly rounds to the nearest minute to resolve the extra minute issue that was happening.
- Resolved an issue wherein code limit emails may not have been sent.
- Deleting a provider configuration now deletes all of that provider's projects from the database until that provider is recreated.
- Resolved an issue wherein Alert does not send an email notification if the project names contain commas.
- Resolved an issue wherein the project information was not being updated in the Alert database.

## Release Notes Version 4.0.0

**Changed features**

- Added support for Java v.11.0.
- The provider timeout now supports decimals and displays timeout in seconds.
- Improved and expanded **Audit** table functionality.
- Added support for CFSSL container version 4.7.0.
- Improved error messaging for **Distribution** configuration.
- Improved text length limits for configuration fields, which can now handle up to 511 characters.
- Invalid email addresses are now logged as warnings and ignored prior to sending.
- Improved the job deletion confirmation which now displays complete information about jobs selected for deletion.
- Added new properties for configurable values and new fields.

**Resolved issues**

- Resolved an issue wherein reading the common configuration may prevent displaying of the job configuration.
- Resolved an issue wherein clicking **Show Advanced** in the email channel may erase all entered values.
- Resolved an issue wherein testing the email configuration test messages with invalid SMTP resulted in no action.
- Resolved an issue wherein information may have been missing in the **Audit** page.
- Resolved an issue wherein failing to provide an encryption password or SALT will not set the password fields.
- Resolved an issue wherein Black Duck Alert may not function properly with Black Duck when project names contain greater than 255 characters.
- Resolved an issue occurring when upgrading from Alert version 2.0.0 to version 3.0.0.
- Resolved an issue wherein affirmation messages on the email channel remain on screen, even after navigating away.
- Resolved an issue with the daily digest wherein removing the policy violation Alert lists the last type as DELETE rather than omitting the policy notification.
- Resolved an issue wherein global configuration processes may be running without global process configurations being set up.

**New features**

- Alert now authenticates through LDAP.
- Users can authenticate as the default administrator user.
- Email notifications are now sent to Black Duck administrators to inform them of the percentage of reaching their code limit.
- Added a new setup menu to configure the required data for Alert.
- Added **Environment Variables Override** setup option.
- You can now reset the administrator password from the login screen.

**Known issues**

- There is a known issue with sending LICENSE_LIMIT notification data over email. The LICENSE_LIMIT notification data is not sent over email; it appears in Slack and HipChat channels.

## Release Notes Version 3.1.0

**Changed features**

- Alert> now displays the message *Missing global configuration* where appropriate when setting up HipChat distribution jobs.
- HipChat **Test Configuration** now opens a dialog box for a test room for sending test messages to validate your HipChat configuration.
- Email **Test Configuration** now opens a dialog box for a test email address for sending test messages to validate your email configuration.

**Resolved issues**

- Resolved an issue wherein the audit table search was case-sensitive; this search is now case-insensitive.
- Resolved an issue wherein components with multiple origins may display duplicate linked items.
- Resolved an issue wherein proxy settings for email servers may not always function as expected.
- Resolved an issue wherein the component name may be missing from the output of policy rule violation messages.
- Resolved an issue wherein multiple policies attached to a single project may link violations to incorrect policies.
- Resolved an issue wherein the Black Duck Alert emails may not contain the component name.

**New features**

- Configuration errors now display on the login screen.
- If stored variable and credentials are missing, a form displays at login for completing the missing items.
- Alert can now send notifications about projects matching a regular expression.
- Environment variables now take precedence over settings in the user interface.

## Release Notes Version 3.0.0

**Changed features**

- Updated Black Duck Alert properties and environment variables.
- Can now send alerts to individual users or to all members of a project.
- Alert no longer sends emails to a group specified in the distribution job; instead it now sends emails to the users/groups assigned to the projects configured in the job.
- The Distribution job provider now defaults to Black Duck.

**Resolved issues**

- Resolved an issue wherein the browse was caching the API key when saving.
- Resolved an issue wherein *Template Exceptions* errors were thrown when dealing with versionless components.
- Resolved an issue wherein the distribution jobs fields may not retain changes.
- Resolved an issue wherein editing a distribution job while auto-refresh is enabled may remove edits and changes to the job.
- Resolved an issue wherein the **Audit** table may not have been correctly displaying the audit data.
- Resolved an issue wherein required properties for the `SchedulingConfiguration` component `purgeDataFrequencyDays` and `dailyDigestHourOfDay` were not being set and causing UI errors.
- Resolved an issue wherein the UI may request an incorrect page size and page number when using the **Search** function in the **Audit** table.
- Resolved an issue wherein some group roles were not allowing access to the Alert user interface.
- Resolved an issue wherein the **Audit** table pages may not be updating correctly.
- Resolved an issue with the environment variables in the deployment files.
- Resolved an issue wherein the browser was caching the API key.

**New features**

- Added an *About* menu in the user interface.
- Added links to the vulnerability record on the Hub from the email generated by Alert.
- Direct links are now included in notification emails.
- Alert now acquires the severity of each vulnerability and adds it to the list of linkable items displaying the severity of the notifications in the channel.
- Added new properties for HipChat, scheduling, and required properties.

## Release Notes Version 2.1.0

**Changed features**

- In the `*.yml` file, the user was previously `hubalert` This is now updated to the user name `alert`.

**Resolved issues**

- Resolved an issue wherein the Audit table search bar and table sorting were not functioning as expected.
- Resolved an issue wherein the Audit table search function may request an incorrect page size and page number.
- Resolved an issue wherein the Audit table pages were not updating as expected.
- Resolved an issue wherein the high vulnerability email generated by Alert contains repetitions of the same data.
- Resolved an issue with the *SchedulingConfiguration* component in the user interface.
- Resolved an issue wherein enabling auto-refresh did not persist between pages.
- Resolved an issue wherein some group roles were not allowing access to the Alert user interface.

## Release Notes Version 2.0.1

**Changed features**

- Resolved an issue wherein after upgrading from Alert version 1.0.0 to version 2.0.0, the distribution jobs may have been broken.

## Release Notes Version 2.0.0

**Changed features**

- The *hub-alert.env* file is renamed to *blackduck-alert.env*.
- The container name is renamed from *hub-alert* to *blackduck-alert*. You can find it in Docker Hub as *blackduck-alert*.

**New features**

- Added support for Kubernetes.
- Added support for Docker Swarm.
- Added a new universal channel controller.

## Release Notes Version 1.1.0

**Resolved** **issues**

- Resolved an issue involving multiple Slack notifications.
- Resolved an issue wherein the **Notification Types** field was not filtering the notifications sent using email, Slack, or HipChat.
- Resolved an issue wherein a single new vulnerability could result in nine identical changes in Slack notifications.
- Resolved an issue wherein a null pointer exception (NPE) could occur when adding components to jobs having their distributions removed.
- Resolved an issue wherein selecting multiple projects does not work if a single project is de-selected.
- Resolved an issue wherein the HipChat distribution **Notify** checkbox may not create HipChat notifications.
- Resolved an issue with the audit stack trace display.
- Resolved an issue wherein the **Test Configuration** button may not always work as expected.

**New features**

- Added support for nginx.
- Added support for using Alert in a Hub SaaS environment.
- Added support for self-hosted HipChat environments.
- Added support for configuring logging levels for debugging issues.
- The Alert version now displays in the user interface.

**Release Notes Version 1.0.0**

- First release of the Alert product.
