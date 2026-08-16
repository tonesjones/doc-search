---
title: "Upgrading Black Duck Alert"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/upgrading-black-duck-alert.html"
content_id: "d9qOmszjVMXsoypTjuYTxg"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:20.844983+00:00"
---

# Upgrading Black Duck Alert

Important: The Postgres Admin user must have administrative, superuser
priviledge OR the extension "uuid-ossp" must be installed, and the following
permission granted to the Postgres Admin user: `GRANT UPDATE,SELECT ON
public.databasechangeloglock`

The base supported migration version of PostgreSQL is 14.8.
Customers that are still on PostgreSQL 12.11 should
upgrade to Alert 6.13.x before upgrading to 7.0.0.

The docker-compose.local-overrides.yml values are only used to
initialize the DB when Alert starts for the first time. If the Alert DB already
exists, configuration values added here, such as adding a provider, will not be
reflected in the configuration.

## Backing up existing data

Tip: It is recommended to create a database backup with the plain text
format to be database version agnostic. The backup created in the plain text
format can also be restored using the included scripts.

To ensure the safety of existing data, create a database backup before executing any
upgrade process. Backing up your data is particularly important when upgrading Alert
to version 6.12.x or later, from a previous release, as the included Postgres
version has also been upgraded.

As of Alert version 6.12.0 there are scripts included with the installation files to
assist with performing a database backup and restore.

The backup scripts are for installations of Alert with Docker swarm or Helm. They are
not intended to be used with an **external** database which should be backed up
manually or via the users own scripts. See Postgres documentation for help with
upgrading to version 14.x [Documentation → PostgreSQL 14](https://www.postgresql.org/docs/14/release.html)

Alert supports the restoration of a database dump into an Alert instance of the same
version as the dump. For example, restoring a 6.13.1 database dump into a 6.13.1
instance is supported, but restoring a 6.13.1 dump into 6.13.2 is not. After
restoring a database dump, the Alert service must be restarted.

## Backing up data in a Docker swarm installation

The database script is location in your downloaded package
`blackduck-alert-<version>-deployment.zip` at:
*`docker-swarm/database-utilities.sh`*

```
usage: database-utilities - backup or restore a database with docker.

database-utilities.sh [-b] [-d databaseName] [-f file] [-k containerKeyword] [-p] [-r] [-t type] [-u userName]
Options:
  -b: backup a database to the file specified in the file option.
  -d: the name of the database."
  -f: the file to save a backup or the file to restore the database from.
  -k: the keyword to search for the database container.
  -p: plain text database dump format
  -r: restore a database from the file specified by the file option.
  -t: the format for the backup or restore file of 'plain' or 'binary'.
  -u: database user name.
  -h: display this help.
```

Examples:

**Plain Text Format**

Backup:`database-utilities.sh -b -t plain -f
~/my-db-backup.dump`

Restore:`database-utilities.sh -r -t plain -f
~/my-db-backup.dump`

**Binary Format**

Backup:`database-utilities.sh -b -t binary -f
~/my-db-backup.dump`

Restore:`database-utilities.sh -r -t binary -f
~/my-db-backup.dump`

## Backing up data in a Helm installation

The database script is location in your downloaded package
`blackduck-alert-<version>-deployment.zip` at:
*`helm/database-utilities.sh`*

```
usage: database-utilities - backup or restore a database with kubectl.

database-utilities.sh [-b] [-d databaseName] [-f file] [-k containerKeyword] [-n namespace] [-p] [-r] [-t type] [-u userName]
Options: 
  -b: backup a database to the file specified in the file option.
  -d: the name of the database.
  -f: the file to save a backup or the file to restore the database from.
  -k: the keyword to search for the database container.
  -n: the namespace used with the deployment.
  -p: plain text database dump format
  -r: restore a database from the file specified by the file option.
  -t: the format for the backup or restore file of 'plain' or 'binary'.
  -u: database user name.
  -h: display this help.
```

Examples:

**Plain Text Format**

Backup:`database-utilities.sh -b -t plain -f
~/my-db-backup.dump`

Restore:`database-utilities.sh -r -t plain -f
~/my-db-backup.dump`

**Binary Format**

Backup:`database-utilities.sh -b -t binary -f
~/my-db-backup.dump`

Restore:`database-utilities.sh -r -t binary -f
~/my-db-backup.dump`

## Migrating your Alert installation

An environment variable has been added to the orchestration and scripts to toggle
running a Postgres migration. By default this is set to true when no value is
provided, and migration will occur automatically.

Should your instance use non-default values for Postgres variables you will need to
configure these environment variables before proceeding.

For further information consult the page on setting environment variables as needed:
Environment Variables

Note: When running a migration on an external database the binaries for
the version of Postgres that created the data in `${PGDATA}`,
must be copied into `${PGBINOLD}`. These are already in place
when using Alert images.

### Upgrading Postgres in a Docker swarm environment

The Postgres upgrade must be performed by a Postgres admin user with administrative privileges.

You must configure the same values for the following parameters within docker-compose.local-overrides.yml that were defined in your previous version of Alert.

- `ALERT_DB_ADMIN_USERNAME` will need to be set to the Postgres Admin Username in the current Alert environment.
- `ALERT_DB_ADMIN_PASSWORD` will need to be set to the Postgres Admin password used in the current Alert environment.
- `ALERT_ENCRYPTION_PASSWORD` if data encryption is enabled, set this to the must be set to same password used when data was added to the DB.
- `ALERT_ENCRYPTION_GLOBAL_SALT` if data encryption is enabled, set this to same value used when data was added to the DB.

### Upgrading Postgres in a Helm environment

The Postgres upgrade must be performed by a Postgres admin user.

You must configure the same values for the following parameters within
values.yaml that were defined in your previous version of Alert.

- `postgres.adminUserName` will need to be set to
  the Postgres Admin ID used within the current Alert environment.
- `postgres.adminPassword` will need to be set to
  the Postgres Admin password used within the current Alert environment.
- `ALERT_ENCRYPTION_PASSWORD` if data encryption is
  enabled, set this to the must be set to same password used when
  data was added to the DB.
- `ALERT_ENCRYPTION_GLOBAL_SALT` if data encryption
  is enabled, set this to same value used when data was added to
  the DB.

### Migrating your Alert installation using Helm default image

If you are deploying using Helm and the default image listed in the Helm
orchestration `(docker.io/centos/postgresql-12-centos7:1)`,
you will need to edit the values.yaml.

1. Modify the following parameter in the values.yaml file:

- `postgres.postgresDataDirectory` - Set to "*/var/lib/postgresql/data/userdata*"

1. Modify the postgres DB credentials.

   **If you are NOT using a secrets file for the DB credentials:**

- `postgres.adminUserName` will need to be set to the
  Postgres Admin ID used within the current Alert environment.(This should be set to "postgres" if the
  defaults were used.)
- `postgres.adminPassword` will need to be set to the
  Postgres Admin password used within the current Alert
  environment.(This should be set to "" if the defaults
  were used.)

  **If you are using a secrets file for the DB credentials:**
- `postgres.dbAdminCredential.secretName` will need to
  be configured for the Kubernetes secret which contains the following:

  - `usernameKey:` "ALERT_DB_ADMIN_USERNAME"
  - `passwordKey:` "ALERT_DB_ADMIN_PASSWORD"

### Migrating your DB with non-default Postgres settings

1. For a Docker Swarm or Helm install, modify the following parameters in
   the docker-compose.local-overrides.yml(Docker), or
   values.yaml(Helm), file as appropriate for your environment.

- `POSTGRES_USER` - If not set, will default to ‘sa’
- `POSTGRES_PASSWORD` - If not set, will default to ‘blackduck’
- `POSTGRES_DB` - If not set, will default to 'alertdb’

1. Deploy the images and migration will proceed.

## Alert upgrade instructions without DB migration

In cases where a databse migration is not required, the following upgrade instructions may be followed.

## Docker Swarm

When using Docker swarm, upgrading Alert is achieved by removing the stack and
redeploying with the latest version.

Alert only supports upgrading from two major versions prior to the current
release. Refer to the [Black Duck Release Compatability matrix for currently supported versions.](https://documentation.blackduck.com/bundle/blackduck-compatibility/page/topics/Black-Duck-Release-Compatibility.html)

### Before you begin

Review all secrets and ensure they match what is declared in your docker-compose.local-overrides.yml file if not using a secrets file.

Comment out the following section from the docker-compose.local-overrides.yml file when using a secrets file.

```
                            #    # uncomment the variables that end in _FILE if secrets are being used.
                            #      - POSTGRES_USER_FILE=/run/secrets/ALERT_DB_USERNAME
                            #      - POSTGRES_PASSWORD_FILE=/run/secrets/ALERT_DB_PASSWORD
```

### Upgrade

- Run `docker stack rm <STACK_NAME>`, where
  `<STACK_NAME>` matches the name of your deployment
- Follow the install instructions for whatever methodology you are using (standalone or integrated)

### Verify Secrets

Review the Docker secrets. ```` ```bash docker secret ls ````

### Helm

#### Upgrading

Before attempting to upgrade your Helm install, run the following command to refresh the charts

```
helm repo update
```

Use the standard Helm upgrade commands to install the latest version

```
helm upgrade <name> blackduck/blackduck-alert --namespace <namespace> helm upgrade <name> . --namespace <namespace>
```

Where `<name>` matches your current deployment name and the `<namespace>` is correct.

#### Uninstalling

To uninstall/delete the deployment, use the standard Helm commands

```
helm uninstall <name> --namespace <namespace>
```

This command will remove the release from your cluster.
