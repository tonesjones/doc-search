---
title: "Black Duck Alert Environment Variables"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-environment-variables.html"
content_id: "JH0n2BPtinlrdFvlRiOFPw"
version: "8.4.0"
section: "Installation References"
scraped_at: "2026-08-08T23:46:29.592324+00:00"
---

# Black Duck Alert Environment Variables

This page describes environment variables by function and how these vary with different releases.

## Environment variable processing

At startup, Alert processes the default setting of environment variables from configuration files named either `values.yaml` for Helm, or `docker-compose.local-overrides.yml` for Docker Swarm. These files are found in the folder structure of your downloaded `blackduck-alert-<version>-deployment.zip` file.

Important: The `docker-compose.local-overrides.yml` and `values.yaml` settings are only used to initialize the DB when Alert starts for the first time. If the Alert DB already exists, configuration values added here, such as adding a provider, will not be reflected in the configuration.

See [Alert environment variable file in GitLab](https://github.com/blackducksoftware/blackduck-alert/blob/master/deployment/blackduck-alert.env) for example file content.

- The environment variable is written into the database if the value for the corresponding configuration property isn't written in the database. Therefore, the environment variables take precedence over the default values shown in the user interface.
- If there is an existing configuration related to environment variables stored in the database, the environment variables will have no effect.
- Environment variables create a configuration named "default-configuration". The "default-configuration" can be updated via the UI if desired.

## Environment variables for encryption

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_ENCRYPTION_PASSWORD` | Used to encrypt the data. It can be any alphanumeric string between 8 and 24 characters. |  |
| `ALERT_ENCRYPTION_GLOBAL_SALT` | The salt appended to the sensitive information before it is encrypted. |  |

## Environment variables for logging

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_LOGGING_LEVEL` | This sets the verbosity of the application logs. Normally only to be changed if requested by Support | `INFO` by default. Other possible values - `TRACE`, `DEBUG`, `ERROR`, `WARN` |

## Environment variables for Proxy support

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_COMPONENT_SETTINGS_SETTINGS_PROXY_HOST` | The host name of the proxy server to use. |  |
| `ALERT_COMPONENT_SETTINGS_SETTINGS_PROXY_PORT` | The port of the proxy server to use. |  |
| `ALERT_COMPONENT_SETTINGS_SETTINGS_PROXY_USERNAME` | The username to authenticate to the proxy server with | Optional if auth required |
| `ALERT_COMPONENT_SETTINGS_SETTINGS_PROXY_PASSWORD` | The password of the proxy user | Optional if auth required |
| `ALERT_COMPONENT_SETTINGS_SETTINGS_NON_PROXY_HOSTS` | Hosts whos network traffic should not go through the proxy |  |

## Support for running behind a load balancer

Setting `ALERT_FORWARD_HEADERS_STRATEGY` to `native` will signal Alert to use the `X-Forwarded` headers from requests made to Alert API's to construct the URL's to reach Alert.

## Environment variables for the Black Duck provider

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_PROVIDER_BLACKDUCK_BLACKDUCK_URL` | Url of the Black Duck server |  |
| `ALERT_PROVIDER_BLACKDUCK_BLACKDUCK_API_KEY` | Black Duck API Key | The user who generates the token requires one of the following roles to ensure connectivity: `Super User`, `System Administrator`, `Global Project Viewer`, `Global Project Administrator`, `Global Project Group Administrator`, `Global Notification Viewer` OR as of version 7.1.2 the API Token belongs to a user with at least one [Watched Project](https://documentation.blackduck.com/bundle/bd-hub/page/InternalProjects/WatchedProjects.html) with notifications enabled. Notifications for any projects the user has notifications enabled on, will be processed. |
| `ALERT_PROVIDER_BLACKDUCK_BLACKDUCK_TIMEOUT` | Time in seconds for connections to the Black Duck server |  |
| `ALERT_PROVIDER_BLACKDUCK_PROVIDER_COMMON_CONFIG_NAME` | Unique name assigned to this provider |  |
| `ALERT_PROVIDER_BLACKDUCK_PROVIDER_COMMON_CONFIG_ENABLED` | Boolean that controls whether Alert pulls data from the provider |  |

Note: You cannot create more than one Black Duck SCA provider using environment variables. To create multiple providers, use the Alert user interface.

## Environment variables for Alert host name and port

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_HOSTNAME` | Specifies the host name of the Alert server. Do not use a URL for this value | ) |
| `ALERT_SERVER_PORT` | Specifies the port for Alert |  |

## Environment variables for resetting authentication

Use the following environment variables to reset the authentication mechanisms for the initial Alert startup. These are useful if you have forgotten the Admin password, or misconfigured LDAP or SAML.

For example, you might want to disable LDAP or SAML authentication, or reset the admin user password. You can re-enable the previous settings when you complete your changes.

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_LDAP_DISABLED` | When `true` LDAP authentication is disabled. All other LDAP configuration fields remain set. | Introduced in Alert 6.0.0 |
| `ALERT_SAML_DISABLED` | When `true` SAML authentication is diabled. All other SAML configuration fields remain set. | Introduced in Alert 6.0.0 |
| `ALERT_ADMIN_USER_PASSWORD_RESET` | When `true` the sysadmin account password is reset to the default value. |  |

## Environmental variables for user account lockout

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_LOCKOUT_THRESHOLD` | Maximum number of login attempts before locking the account. |  |
| `ALERT_LOCKOUT_MINUTES` | Maximum duration of the lockout in minutes. |  |

## Environmental variables for scheduling

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_COMPONENT_SCHEDULING_SCHEDULING_PURGE_DATA_FREQUENCY` | The frequency for cleaning up provider data. When the purge runs, it deletes all data older than the value. For example, if the value is 3, then data older than 3 days is deleted. |  |
| `ALERT_COMPONENT_SCHEDULING_SCHEDULING_DAILY_PROCESSOR_HOUR` | The hour of the day (0 - 23) to run the daily digest distribution jobs |  |

## Environmental variables for notifications

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_NOTIFICATION_MAPPING_BATCH_LIMIT` | Configuration of the default batch size for notification processing. | The batch size can be set to a value between 1,000 - 10,000. The default is 10,000 |

Note: This value should only be modified on the advice of customer support.

## Environment variables for authentication with LDAP and SAML

These variables are used to configure Alert values during the initial startup.

### LDAP authentication settings

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_ENABLED` | When `true` Alert will attempt to authenticate using the specified configuration |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_SERVER` | URL of the LDAP server |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_AUTHENTICATION_TYPE` | The type of authentication required by the LDAP server | Possible values - `simple` , `none` , `Digest-MD5` |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_GROUP_ROLE_ATTRIBUTE` | The ID of the attribute which contains the role name for a group |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_GROUP_SEARCH_BASE` | Where in the LDAP directory group searches should be done |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_GROUP_SEARCH_FILTER` | The filter used for group membership |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_MANAGER_DN` | Distinguished name of the LDAP manager |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_MANAGER_PASSWORD` | The password of the LDAP manager |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_REFERRAL` | The method to use when handling referrals | Possible values - `ignore`, `follow`, `throw` |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_USER_ATTRIBUTES` | What attributes to retrieve for a user |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_USER_DN_PATTERNS` | The pattern used to supply a DN for a user. This should be the name relative to the root DN |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_USER_SEARCH_BASE` | Where in the LDAP directory user searches should be done |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_LDAP_USER_SEARCH_FILTER` | The filter used for user membership |  |

### SAML

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_SAML_ENABLED` | When `true` Alert will attempt to authenticate using the specified configuration |  |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_SAML_FORCE_AUTH` | When `true` the forceAutn flag is set in the payload to the IDP | Check that this is supported by your IDP |
| `ALERT_COMPONENT_AUTHENTICATION_SETTINGS_SAML_METADATA_URL` | The Metadata URL provided by your IDP |  |

## Environment variables for Azure Boards

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_CHANNEL_AZURE_BOARDS_ORGANISATION_NAME` | The name of the Azure DevOps organization. |  |
| `ALERT_CHANNEL_AZURE_BOARDS_CLIENT_ID` | The App ID created for Alert when registering your Azure DevOps Client Application. |  |
| `ALERT_CHANNEL_AZURE_BOARDS_CLIENT_SECRET` | The Client secret created for Alert when registering your Azure DevOps Application. |  |

## Environment variables for Email Channels

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_CHANNEL_EMAIL_MAIL_SMTP_HOST` | The host name of the SMTP email server. |  |
| `ALERT_CHANNEL_EMAIL_MAIL_SMTP_PORT` | The SMTP server port to connect to. |  |
| `ALERT_CHANNEL_EMAIL_MAIL_SMTP_FROM` | The email address to use as the return address. |  |
| `ALERT_CHANNEL_EMAIL_MAIL_SMTP_AUTH` | The SMTP server requires authentication. | `true` by default. |
| `ALERT_CHANNEL_EMAIL_MAIL_SMTP_USER` | The username to authenticate with the SMTP server. |  |
| `ALERT_CHANNEL_EMAIL_MAIL_SMTP_PASSWORD` | The password to authenticate with the SMTP server. |  |

## Environment variables for Jira Cloud

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_CHANNEL_JIRA_CLOUD_JIRA_CLOUD_URL` | The URL of the Jira Cloud server. |  |
| `ALERT_CHANNEL_JIRA_CLOUD_JIRA_CLOUD_ADMIN_EMAIL_ADDRESS` | The email address of the Jira Cloud user | Unless `Disable Plugin Check` is checked, this user must be a Jira admin. |
| `ALERT_CHANNEL_JIRA_CLOUD_JIRA_CLOUD_ADMIN_API_TOKEN` | The API key of the specified user. |  |

## Common Environment variables for Jira Server

Note: Alert supports either Basic or Token authentication to Jira Server, but not concurrently.

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_CHANNEL_JIRA_SERVER_JIRA_SERVER_URL` | The URL of the Jira Server server. |  |
| `ALERT_CHANNEL_JIRA_SERVER_JIRA_SERVER_AUTHORIZATION_METHOD` | The type of authentication to use when connecting to your Jira Server | Possible Values: `BASIC`, `PERSONAL_ACCESS_TOKEN` Default: `BASIC` |
| `ALERT_CHANNEL_JIRA_SERVER_JIRA_SERVER_DISABLE_PLUGIN_CHECK` | Disables checking whether the `Alert Issue Property Indexer` plugin is installed on the Jira instance. |  |

## Environment variables for Jira Server Basic

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_CHANNEL_JIRA_SERVER_JIRA_USERNAME` | The username of the Jira Server user. | Unless `Disable Plugin Check` is checked, this user must be a Jira admin. |
| `ALERT_CHANNEL_JIRA_SERVER_JIRA_PASSWORD` | The password of the Jira Server user. |  |

## Environment variables for Jira Server Personal Access Token

| Name | Description | Notes |
| --- | --- | --- |
| `ALERT_CHANNEL_JIRA_SERVER_JIRA_SERVER_PERSONAL_ACCESS_TOKEN` | The access token to be used when authenticating to the Jira Server | Input the token string generated in Jira Server |

## Default rabbitMQ Environment Variable Values

| Container | Environment Variable | Default Value |
| --- | --- | --- |
| RabbitMQ Container | `ALERT_RABBITMQ_ERLANG_ASYNC_THREADS` | `1` |
| RabbitMQ Container | `ALERT_RABBITMQ_CONNECTION_CHANNEL_MAX` | `512` |
| RabbitMQ Container | `ALERT_RABBITMQ_CONNECTION_TCP_ACCEPTORS` | `10` |
| RabbitMQ Container | `ALERT_RABBITMQ_CONNECTION_HEARTBEAT` | `60` |
| RabbitMQ Container | `ALERT_RABBITMQ_MEMORY_HIGH_WATERMARK` | `1GB` |
| RabbitMQ Container | `ALERT_RABBITMQ_MEMORY_WATERMARK` | `0.80` |
| Alert Container | `ALERT_RABBITMQ_CONNECTION_MODE` | `CONNECTION` |
| Alert Container | `ALERT_RABBITMQ_CONNECTION_SIZE` | `5` |
| Alert Container | `ALERT_RABBITMQ_LISTENER_CONCURRENCY` | `5` |
| Alert Container | `ALERT_RABBITMQ_LISTENER_MAX_CONCURRENCY` | `15` |
| Alert Container | `ALERT_RABBITMQ_LISTENER_PREFETCH` | `250` |
| Alert Container | `ALERT_RABBITMQ_LISTENER_ACKNOWLEDGE_MODE` | `auto` |
| Alert Container | `ALERT_RABBITMQ_CONNECTION_TIMEOUT` | `30000` |
| Alert Container | `ALERT_RABBITMQ_CONNECTION_HEARTBEAT` | `60` |

## Container Specific Environment Variable Configuration Mappings RabbitMQ Mapping to rabbitmq.conf File Properties

| Environment Variable | RabbitMQ Configuration File Property |
| --- | --- |
| `ALERT_RABBITMQ_ERLANG_ASYNC_THREADS` | `SERVER_ADDITIONAL_ERL_ARGS="A+ <ENV_VALUE>"` |
| `ALERT_RABBITMQ_CONNECTION_CHANNEL_MAX` | `channel_max` |
| `ALERT_RABBITMQ_CONNECTION_TCP_ACCEPTORS` | `num_acceptors.tcp` |
| `ALERT_RABBITMQ_CONNECTION_HEARTBEAT` | `heartbeat` |
| `ALERT_RABBITMQ_MEMORY_HIGH_WATERMARK` | `total_memory_available_override_value`  `vm_memory_high_watermark.absolute` |
| `ALERT_RABBITMQ_MEMORY_WATERMARK` | `vm_memory_high_watermark.relative` |

Documentation for the RabbitMQ configuration file:

<https://www.rabbitmq.com/docs/configure#config-file>

Example configuration with inline comments:

<https://github.com/rabbitmq/rabbitmq-server/blob/main/deps/rabbit/docs/rabbitmq.conf.example>

## Alert Mapping to Spring Application Properties

| Environment Variable | Spring Application Property |
| --- | --- |
| `ALERT_RABBITMQ_CONNECTION_MODE` | `spring.rabbitmq.cache.connection.mode` |
| `ALERT_RABBITMQ_CONNECTION_SIZE` | `spring.rabbitmq.cache.connection.size` |
| `ALERT_RABBITMQ_LISTENER_CONCURRENCY` | `spring.rabbitmq.listener.simple.concurrency` |
| `ALERT_RABBITMQ_LISTENER_MAX_CONCURRENCY` | `spring.rabbitmq.listener.simple.max-concurrency` |
| `ALERT_RABBITMQ_LISTENER_PREFETCH` | `spring.rabbitmq.listener.simple.prefetch` |
| `ALERT_RABBITMQ_LISTENER_ACKNOWLEDGE_MODE` | `spring.rabbitmq.listener.simple.acknowledge-mode` |
| `ALERT_RABBITMQ_CONNECTION_TIMEOUT` | `spring.rabbitmq.connection-timeout` |
| `ALERT_RABBITMQ_CONNECTION_HEARTBEAT` | `spring.rabbitmq.requested-heartbeat` |

For detailed descriptions of Spring Boot application properties, see:

<https://docs.spring.io/spring-boot/appendix/application-properties/index.html>
