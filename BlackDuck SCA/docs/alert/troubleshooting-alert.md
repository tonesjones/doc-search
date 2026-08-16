---
title: "Troubleshooting Alert"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/troubleshooting-alert.html"
content_id: "~Nh13gfYVU8zfYmOKjJAGQ"
version: "8.4.0"
section: "Troubleshooting Alert"
scraped_at: "2026-08-08T23:46:45.203154+00:00"
---

# Troubleshooting Alert

## Alert installation issue with EnterpriseDB

Alert installations may fail when executed against PostgreSQL variants such as
EnterpriseDB, which does not execute the Liquibase scripts correctly for creation of
functions. Liquibase is not throwing an error when these functions fail to be created
which causes Liquibase failure when attempting to use the missing function.

The following error will be logged in the above scenario:

```
ERROR: Exception Primary Reason: ERROR: function get_descriptor_type_id(unknown) does not exist
```

To resolve this error the Liquibase function creation logic has been added to a file
named `init_alert_functions.sql`.

A successful creation log message will look like the following:

```
psql:/opt/blackduck/alert/alert-tar/upgradeResources/init_alert_functions.sql:25: INFO:  Function GET_CONTEXT_ID created successfully.
```

This sql script is included in the orchestration zip file, and can be run manually as
needed prior to Alert installation.

Note: Alert is tested and supported against PostgreSQL, variants such as
EnterpriseDB may function in PostgreSQL compatibility mode but are not
officially supported.

## Jira workflows using Global Transitions failing to transition state

Issue states may not correctly transition when using "Global Transitions" within Jira
Server and Cloud workflows.

When "Global Transitions," those allowing issues to be transitioned from any status
to the target status, are used, Alert will retrieve a list of ALL transitions, and
the desired state may not be applied.

Use of a workflow with well-defined transitions between issue states is recommended.
Avoid the use of "Global Transitions" with simplified workflows and instead use
common transitions within the workflow of the target Jira project.

## SSL configuration issue when sslUseFiles is set to false

1. To work around this issue, obtain the CA certificate from your provider and create
a secret with it:

`kubectl create secret generic alert-ssl-root -n <namespace>
--from-file=ALERT_DB_SSL_ROOT_CERT_PATH=<CA-certificate-from-provider>`

2. Download the Alert files, as needed, modifying `values.yaml` with
the external Postgres details and setting the following:

```
  isExternal: true # false for running Postgres as a container and true for using External Postgres database
  ssl: true # If true, Alert uses SSL for external Postgres connection
  sslUseFiles: true # If true, Alert will expect to find ssl certs for communicating with the External Postgres database
  sslSecrets: # Secret that contains all the ssl file paths
    secretName: "alert-ssl-root"
    sslRootCertKey: "ALERT_DB_SSL_ROOT_CERT_PATH"
  host: <postgres-host-url> # required only for external postgres, for postgres as a container, it will point to <name>-postgres
  port: 5432
```

3. Run Helm and write the resulting file into a file named
`alert.yaml`

`helm install alert blackduck-alert/deployment/helm/blackduck-alert/
--namespace alert --dry-run > alert.yaml`

4. Edit the resulting yaml file to set ALERT_DB_SSL_KEY_PATH and
ALERT_DB_SSL_CERT_PATH as empty:

```
        - name: ALERT_DB_SSL_KEY_PATH
          value: 
        - name: ALERT_DB_SSL_CERT_PATH
          value:
```

5. Edit the yaml file so both secrets mounted as a result of the empty sslCertKey and
sslKeyKey are deleted:

From this:

```
        volumeMounts:
        - mountPath: /opt/blackduck/alert/alert-config
          name: dir-alert
        - mountPath: /tmp/secrets/
          name: dbcert
          subPath: 
        - mountPath: /tmp/secrets/
          name: dbcert
          subPath: 
        - mountPath: /tmp/secrets/ALERT_DB_SSL_ROOT_CERT_PATH
          name: dbcert
          subPath: ALERT_DB_SSL_ROOT_CERT_PATH
      dnsPolicy: ClusterFirst
```

To this:

```
        volumeMounts:
        - mountPath: /opt/blackduck/alert/alert-config
          name: dir-alert
        - mountPath: /tmp/secrets/ALERT_DB_SSL_ROOT_CERT_PATH
          name: dbcert
          subPath: ALERT_DB_SSL_ROOT_CERT_PATH
      dnsPolicy: ClusterFirst
```

6. Run the yaml file

`kubectl -n <namespace> apply -f alert.yaml
--validate=false`

## Helm Deployment Storage Configuration Issue

Helm deployments may fail to deploy using certain storage configurations. In some
cases the user may see the following error when starting the pod:

```
initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
It contains a lost+found directory, perhaps due to it being a mount point.
Using a mount point directly as the data directory is not recommended.
Create a subdirectory under the mount point.
```

This currently impacts the following storage configurations:

| **Provider** | **Storage Class** |
| --- | --- |
| Azure | Azure File |
|  | Azure Disk |
| AWS | GP2 |
|  | GP3 |
| GCP | premium-rwo |
|  | standard-rwo |
|  | standard |

To workaround this issue you must update the `postgres.yaml` file
under `helm/blackduck-alert/templates/postgres.yaml`.

From:

```
volumeMounts:
  - mountPath: /var/lib/postgresql/data
    name: alert-postgres-data-volume
```

To:

```
volumeMounts:
  - mountPath: /var/lib/postgresql
    name: alert-postgres-data-volume
    subPath: data
```

## Azure Authentication Issues

If you get an error authenticating with Azure, try the following steps:

1. Click the **Delete** button in the global configuration for Azure in
   Alert.
2. Go to the Azure application that is used for the OAuth connection and revoke the
   connection.
3. Re-enter the values for the global configuration for Azure in Alert.
4. Click **Test Configuration** to make sure the configuration is working and
   the issue is resolved.

## Azure Board Distribution Issue

In some cases you may encounter a permissions exception related to an Alert work item
not recognized in Azure Boards. This will appear as an exception occuring during
message distribution.

In the Alert UI, under the Distribution jobs, this will show as: **ERROR**: *An
exception occured during message distribution.*

Logged as **ERROR**: *There was a problem creating a modifiable work item from
'Microsoft.VSTS.WorkItemTypes.Task' in the Azure process with id: XXXX.*

The solution for this is for the Azure Board Admin to navigate to Projects >
Organisation settings > Boards, select **Process** and add the custom work
items listed below.

- Alert AdditionalInfo Key
- Alert Category Key
- Alert Component Key
- Alert Provider Key
- Alert SubComponent Key
- Alert SubTopic Key
- Alert Topic Key

For additional information on Azure Board configuration, see: [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/customize-process-work-item-type?view=azure-devops).

## Bypassing SAML if incorrectly configured

Administrative users can use the standard Alert login functionality (i.e. login as a
user stored in the Alert database rather than an external system) as a login
workaround when SAML is enabled.

## Symptoms of Alert Port issues

The following issues are often caused by misconfiguring the server port when
deploying Alert using the Helm files.

Issues:

- Incorrect link to the Alert server in emails
- Connection problems with Azure Boards
- Connection problems with SAML
- Unable to reach the Swagger UI when using the link in the About Page

Solution(s):

- Set the exposedNodePort in the Helm deployment files. Alert can not determine
  the exposed public port that is used so this must be manually configured so that
  Alert can create correct URLs when referencing itself.
- Change the `forwardHeadersStrategy` to `native`.
  If using a proxy or load balancer, this helps Alert figure out the "public" URL
  used to access Alert when using the UI.

## Setting the logging level to DEBUG

Depending on the deployment method (Docker or Helm), this is achieved in a number of
ways:

**Docker Swarm**

Place the following environment variable into your
`docker-compose.local-overrides.yml` file and restart the
application:

```
- ALERT_LOGGING_LEVEL=INFO
```

example:

```
 alert:
   environment:
     - ALERT_LOGGING_LEVEL=DEBUG
```

**Helm**

Place the value into `values.yaml` or set directly from the CLI
with

```
--set environs.ALERT_LOGGING_LEVEL=DEBUG
```

## Black Duck provider issue(s):

If you receive an error such as *User permission failed, cannot read notifications
from Black Duck.*

Items to check:

- Confirm permissions and roles are correct
- Confirm the Black Duck SCA API token has both read and write access
- Confirm whether **Test Connection** is successful in the provider
  configuration page (see Configuring
  Black Duck Providers)

## JIRA connection issues

**ERROR**: *An error occurred during testing. There was a problem trying to GET
`https://<JIRA_SERVER_URL>/api/2/user?username=<USERNAME>`,
response was 400 Bad Request, reason phrase was Bad Request*

Items to check:

- Jira account:
  - Username is valid
  - Jira account is configured with appropriate admin rights
- Is there a proxy configuration missing which could break network I/O?

**ERROR**: *Failed to create issue: There was a problem trying to POST
`https://<JIRA_SERVER>/rest/api/<KEY_ID>/issue`,
response was 400 Bad Request*

Items to check:

- Check the sent payload via network tools in the browser. If your jira issue type
  has mandatory fields, ensure that these are being passed by Alert. This can be
  checked at **Jobs > Distribution > <YOUR_JOB_NAME> > Advanced
  Jira Configuration > Field Mapping**

## Multiple Jira tickets spawned

Items to check:

- Jira version is 8.x (If using the Jira Server channel)
- Ensure that the **Alert Issue Property Indexer** is installed as this can
  cause duplication if missing.
- If you are running Alert 8.0.0 or later, ensure you have migrated from the
  Synopsys alert-issue-property-indexer to the Black Duck
  alert-issue-property-indexer. See Configuring
  Channels in Alert

## Retain Unmatched File Data configuration error

When the “Retain Unmatched File Data” setting has been changed within Black Duck SCA,
either globally or for an individual project, and you try to configure specific
projects within a distribution job, Alert will throw an exception in the log.

- Log contains the following: `“Could not parse the provided jsonElement
  with Gson” AND will not display any projects in the project drop
  down`.
- Changing the “Retain Unmatched File Data” configuration back to the original
  setting does not address the problem.

Solution:

- Use a Project Name Pattern regex instead of selecting projects from the drop-down
  in Black Duck SCA.

## Watched Projects 403

When an issue tracker (e.g. Jira), is configured, Alert will add a link to the issue
within the Black Duck SCA project version where any discovered vulnerabilities are
reported. If the configured API Token is for a user where the "Watched Projects"
functionality is employed, Alert will show a 403 Forbidden error & stack trace
in the log. The issue will still be created within the tracking system, but it will
not be linked back to Black Duck SCA. To link an issue back to Black Duck SCA the user
requires either the ‘Global Project Manager’ or ‘Global Project Administrator’
role.

## Contacting Black Duck Support

If your issue remains unsolved, please check the [Black
Duck Community](https://community.blackduck.com/) where there is an extensive knowledge base that may offer
insight and solutions.

Administrative users with read level access for Global Content and the Settings Page (Descriptor) can download
system diagnostics data via the Alert application homepage.

Figure 1. Alert Diagnostics File [image: Alert diagnostics file]

When raising a support ticket, please ensure to include the following:

- A description of the problem.
- Whether the issue is causing a production impact, or is on a staging/development
  server.
- The version of Alert installed.
- Alert Diagnostics file.
- Application logs on `DEBUG` (these can be obtained via the
  relevant Docker or Kubernetes CLI commands).
- Deployment configuration files (if appropriate).
- Summary of any changes in the environment that occurred recently which could
  impact your instance.
