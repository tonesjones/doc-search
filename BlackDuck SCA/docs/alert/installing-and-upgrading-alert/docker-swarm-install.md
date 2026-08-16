---
title: "Docker Swarm Install"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/docker-swarm-install.html"
content_id: "pPDCHOXZkXLN8HaBwq_Xsw"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:19.338258+00:00"
---

# Docker Swarm Install

This document describes how to install Alert via Docker Swarm by editing the
`docker-compose.local-overrides.yml` file that is contained in the
*docker-swarm* directory.

## Prerequisites

Installation
Requirements

## Installation Basics

Deployment files for Docker Swarm are located in the *docker-swarm* directory of
the `blackduck-alert-<VERSION>-deployment.zip` file.

- Extract the contents of the ZIP file.
- Choose your installation type of standalone or with Black Duck.
- For installing with Black Duck SCA the files are located in the hub sub-directory.
- For installing Alert standalone the files are located in the standalone sub-directory.

Important: The `docker-compose.local-overrides.yml`
values are only used to initialize the DB when Alert starts for the first time.
If the Alert DB already exists, configuration values added here, such as adding
a provider, will not be reflected in the configuration.

## Standalone Installation

This section will walk through the instructions to install Alert in a standalone
fashion.

### Installation Overview

1. Create ALERT_ENCRYPTION_PASSWORD secret.
2. Create ALERT_ENCRYPTION_GLOBAL_SALT secret.
3. Create ALERT_DB_USERNAME secret.
4. Create ALERT_DB_PASSWORD secret.
5. Create ALERT_RABBITMQ_USER secret.
6. Create ALERT_RABBITMQ_PASSWORD secret.
7. Manage certificates.
8. Modify environment variables.
9. Deploy the stack.

Important: If you are installing with Black Duck and upgrading Alert
from a 4.x or 5.x version to 6.x or greater, please use the
`docker-compose.local-overrides.yml` bundled with Alert.
Remove any Alert configuration from the
`docker-compose.local-overrides.yml` file bundled with
Black Duck.

### Installation Details

This section will walk through each step of the installation procedure.

Note: Installations can be configured to use either a password or a
password file, but not both. `POSTGRES_PASSWORD` and
`POSTGRES_PASSWORD_FILE` are exclusive configuration
options.

## 1. Create ALERT_ENCRYPTION_PASSWORD secret.

Create a docker secret containing the encryption password for Alert, replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<FILE_CONTAINING_PASSWORD>` with the
path to the file containing the password text.

```
$ docker secret create <STACK_NAME>_ALERT_ENCRYPTION_PASSWORD <FILE_CONTAINING_PASSWORD>
```

Make sure the Alert service is uncommented from the
`docker-compose.local-overrides.yml` file. Uncomment the
following from the `docker-compose.local-overrides.yml` file
alert service section.

```
        alert:
            secrets:
                - ALERT_ENCRYPTION_PASSWORD
```

Uncomment the following from the secrets section of the
`docker-compose.local-overrides.yml` file and replace
`<STACK_NAME>` with the name of the stack to be used in
the deployment.

```
        secrets:
            ALERT_ENCRYPTION_PASSWORD:
              external: true
              name: "<STACK_NAME>_ALERT_ENCRYPTION_PASSWORD"
```

## 2. Create ALERT_ENCRYPTION_GLOBAL_SALT secret.

Create a docker secret containing the encryption salt for Alert, replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<FILE_CONTAINING_SALT>` with the path
to the file containing the salt text.

```
$ docker secret create <STACK_NAME>_ALERT_ENCRYPTION_GLOBAL_SALT <FILE_CONTAINING_SALT>
```

Attention: If you created the secret
`ALERT_ENCRYPTION_SALT` in a version of Alert prior to
5.x, please use the same salt value for the
`ALERT_ENCRYPTION_GLOBAL_SALT` secret.

Make sure the Alert service is uncommented from the
`docker-compose.local-overrides.yml` file. Uncomment the
following from the `docker-compose.local-overrides.yml` file
alert service section.

```
        alert:
            secrets:
                - ALERT_ENCRYPTION_PASSWORD
                - ALERT_ENCRYPTION_GLOBAL_SALT
```

Uncomment the following from the secrets section of the
`docker-compose.local-overrides.yml` file replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment.

```
        secrets:
            ALERT_ENCRYPTION_PASSWORD:
              external: true
              name: "<STACK_NAME>_ALERT_ENCRYPTION_PASSWORD"
            ALERT_ENCRYPTION_GLOBAL_SALT:
              external: true
              name: "<STACK_NAME>_ALERT_ENCRYPTION_GLOBAL_SALT"
```

## 3. Create ALERT_DB_USERNAME secret.

Important: If you have previously started Alert with the
`POSTGRES_USER` environment variable, you cannot switch to
using the `ALERT_DB_USERNAME` secret, or the database
container will fail to start.

Create a docker secret containing the database username for Alert. Replace
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<FILE_CONTAINING_USER_NAME>` with the
path to the file containing the database username.

```
$ docker secret create <STACK_NAME>_ALERT_DB_USERNAME <FILE_CONTAINING_USER_NAME>
```

Make sure the alertdb service is uncommented in the
`docker-compose.local-overrides.yml` file.

Comment out the *POSTGRES_USER* environment variable in the
`docker-compose.local-overrides.yml` file.

```
        alertdb:
          environment:
           # - POSTGRES_USER=sa
```

Uncomment the *POSTGRES_USER_FILE* variable from the
`docker-compose.local-overrides.yml` file alertdb service
section.

```
        alertdb:
          environment:
            - POSTGRES_USER_FILE=/run/secrets/ALERT_DB_USERNAME
```

Uncomment the following secrets from the
`docker-compose.local-overrides.yml` file alertdb service
section.

```
        alertdb:
            secrets:
              - ALERT_DB_USERNAME
```

Uncomment the following secrets from the
`docker-compose.local-overrides.yml` file alert service
section.

```
        alert:
            secrets:
              - ALERT_DB_USERNAME
```

Uncomment the following from the secrets section of the
`docker-compose.local-overrides.yml` file and replace
`<STACK_NAME>` with the name of the stack to be used in
the deployment.

```
        secrets:
          ALERT_DB_USERNAME:
            external: true
            name: "<STACK_NAME>_ALERT_DB_USERNAME"
```

## 4. Create ALERT_DB_PASSWORD secret.

Important: If you have previously started Alert with the
`POSTGRES_PASSWORD` environment variable, you cannot switch to using the
`ALERT_DB_PASSWORD` secret. The Alert database container
will fail to start if this is attempted.

Create a docker secret containing the database password for Alert by replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<FILE_CONTAINING_PASSWORD>` with the
path to the file containing the database password.

```
$ docker secret create <STACK_NAME>_ALERT_DB_PASSWORD <FILE_CONTAINING_PASSWORD>
```

Make sure the alertdb service is uncommented from the
`docker-compose.local-overrides.yml` file.

Comment out the `<POSTGRES_PASSWORD>` environment variable
from the `docker-compose.local-overrides.yml` file when using a
`POSTGRES_PASSWORD_FILE`.

```
        alertdb:
          environment:
            # - POSTGRES_PASSWORD=blackduck
```

Uncomment the following environment variables from the
`docker-compose.local-overrides.yml` file alertdb service
section.

```
        alertdb:
          environment:
            - POSTGRES_PASSWORD_FILE=/run/secrets/ALERT_DB_PASSWORD
```

Uncomment the following secrets from the
`docker-compose.local-overrides.yml` file alertdb service
section.

```
        alertdb:
            secrets:
              - ALERT_DB_PASSWORD
```

Uncomment the following secrets from the
`docker-compose.local-overrides.yml` file alert service
section.

```
        alert:
            secrets:
              - ALERT_DB_PASSWORD
```

Uncomment the following from the secrets section of the
`docker-compose.local-overrides.yml` file replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment.

```
        secrets:
          ALERT_DB_PASSWORD:
            external: true
            name: "<STACK_NAME>_ALERT_DB_PASSWORD"
```

## 5. Create ALERT_RABBITMQ_USER secret.

Create a Docker secret containing the username of the RabbitMQ user for Alert and
replace `<STACK_NAME>` with the name of the stack to be
used in the deployment and `<FILE_CONTAINING_USERNAME>`
with the path to the file containing the username text.

```
$ docker secret create <STACK_NAME>_ALERT_RABBITMQ_USER <FILE_CONTAINING_USERNAME>
```

Make sure the alert-rabbitmq service is uncommented from the
`docker-compose.local-overrides.yml` file.

Uncomment the following from the
`docker-compose.local-overrides.yml` file alert-rabbitmq
service section.

```
        alert-rabbitmq:
            secrets:
                - ALERT_RABBITMQ_USER
                - ALERT_RABBITMQ_PASSWORD
```

Make sure the Alert service is uncommented from the
`docker-compose.local-overrides.yml` file.

Uncomment the following from the
`docker-compose.local-overrides.yml` file alert service
section.

```
        alert:
            secrets:
                - ALERT_RABBITMQ_USER
                - ALERT_RABBITMQ_PASSWORD
```

Uncomment the following from the secrets section of the
`docker-compose.local-overrides.yml` file and replace
`<STACK_NAME>` with the name of the stack to be used in
the deployment.

```
        secrets:
            ALERT_RABBITMQ_USER:
              external: true
              name: "<STACK_NAME>_ALERT_RABBITMQ_USER"
            ALERT_RABBITMQ_PASSWORD:
              external: true
              name: "<STACK_NAME>_ALERT_RABBITMQ_PASSWORD"
```

## 6. Create ALERT_RABBITMQ_PASSWORD secret.

Create a Docker secret containing the password of the RabbitMQ user for Alert by
replacing `<STACK_NAME>` with the name of the stack to be
used in the deployment and `<FILE_CONTAINING_PASSWORD>`
with the path to the file containing the password text.

```
$ docker secret create <STACK_NAME>_ALERT_RABBITMQ_PASSWORD <FILE_CONTAINING_PASSWORD>
```

Make sure the alert-rabbitmq service is uncommented from the
`docker-compose.local-overrides.yml` file.

Uncomment the following from the
`docker-compose.local-overrides.yml` file alert-rabbitmq
service section.

```
        alert-rabbitmq:
            secrets:
                - ALERT_RABBITMQ_USER
                - ALERT_RABBITMQ_PASSWORD
```

Make sure the Alert service is uncommented from the
`docker-compose.local-overrides.yml` file.

Uncomment the following from the
`docker-compose.local-overrides.yml` file alert service
section.

```
        alert:
            secrets:
                - ALERT_RABBITMQ_USER
                - ALERT_RABBITMQ_PASSWORD
```

Uncomment the following from the secrets section of the
`docker-compose.local-overrides.yml` file replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment.

```
        secrets:
            ALERT_RABBITMQ_USER:
              external: true
              name: "<STACK_NAME>_ALERT_RABBITMQ_USER"
            ALERT_RABBITMQ_PASSWORD:
              external: true
              name: "<STACK_NAME>_ALERT_RABBITMQ_PASSWORD"
```

## 7. Manage certificates.

This is an optional step. Confirm if custom certificates or certificate store
need to be used.

- Using custom certificate for Alert web server. See Using Custom
  Certificates
- Using custom trust store to trust certificates of external servers. See
  Using a Custom Certificate TrustStore

## 8. Modify environment variables.

Please see Environment
Variables

- Set the required environment variable ALERT_HOSTNAME. See Alert Hostname
  Variable
- Set the optional environment variables for database connectivity. See Alert Database
  Variables
- Set any other optional environment variables as needed.

## 9. Deploy the stack.

Alert can be installed as a stand alone application or with Black Duck SCA.
This step has some variation in how a user accesses Alert depending on which
installation you are trying to perform.

## Standalone Installation

When deploying this way you intend to access Alert through the configured public
hostname and port for the Alert service. The public hostname and/or port
configured for Alert is different from the public hostname and/or port of the
Black Duck SCA installation.

Alert will be accessible via
`https://<ALERT_HOSTNAME>:<ALERT_SERVER_PORT>/alert`

Execute the command, replacing `<STACK_NAME>` with the name
of the stack to be used in the deployment and `<DIR_PATH>`
with the directory path to the Alert installation files:

```
$ docker stack deploy -c <DIR_PATH>/docker-swarm/standalone/docker-compose.yml -c <DIR_PATH>/docker-swarm/docker-compose.local-overrides.yml <STACK_NAME>
```

Users will access Alert via the public host name and port configured for the
Alert service.

## Installation with a Black Duck SCA instance

When deploying this way you intend to access Alert through the same public
hostname and port as Black Duck SCA. Black Duck SCA is used as a reverse proxy to the
Alert service. This is different from a standalone installation.

Alert will be accessible via
`https://<BLACK_DUCK_HOST_NAME>:<BLACK_DUCK_PORT>/alert`

First, verify that Black Duck SCA is installed properly with the correct configuration
to support Alert in this way. This is covered in the Black Duck SCA installation
documentation that can be accessed via the online help. Follow the
installation procedure for installing Black Duck SCA if Black Duck SCA is not already
installed.

You will also need to uncomment the Alert public server port setting in the
`docker-compose.local-overrides.yml` file.

```
        alert:	
            PUBLIC_ALERT_WEBSERVER_PORT=443
```

Important: The NGINX container will not start correctly when it is
waiting for the Alert service to be available. Deploy Alert onto the stack
and NGINX will eventually become healthy when the Alert service is up and
running.

Execute the command to add Alert to the stack by replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<DIR_PATH>` with the directory path to
the Alert installation files. (Use the same stack name used to install Black
Duck SCA i.e. blackduck.)

```
$ docker stack deploy -c <DIR_PATH>/docker-swarm/hub/docker-compose.yml -c <DIR_PATH>/docker-swarm/docker-compose.local-overrides.yml <STACK_NAME>
```

## Certificates

This section describes how to configure the optional certificates. Please verify
beforehand if custom certificates or certificate truststore must be used.

### Using Custom Certificates

Custom certificates for the Alert Web server to client SSL connection.

Before custom certificates can be used for Alert, the signed certificate and key
must be available.

`WEBSERVER_CUSTOM_CERT_FILE` - The file containing the customer's
signed certificate should be modified to replace
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<PATH_TO_CERT_FILE>` with the path to
the certificate file.

```
$ docker secret create <STACK_NAME>_WEBSERVER_CUSTOM_CERT_FILE <PATH_TO_CERT_FILE>
```

`WEBSERVER_CUSTOM_KEY_FILE` - The file containing the customer's key used to create
the certificate should be modified to replace
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<PATH_TO_KEY_FILE>` with the path to
the key file.

```
$ docker secret create <STACK_NAME>_WEBSERVER_CUSTOM_KEY_FILE <PATH_TO_KEY_FILE>
```

Uncomment the following secrets from the
`docker-compose.local-overrides.yml` file alert service
section.

```
        alert:	
            secrets:	
                - WEBSERVER_CUSTOM_CERT_FILE	
                - WEBSERVER_CUSTOM_KEY_FILE
```

Uncomment the following secrets from the secrets section of the
`docker-compose.local-overrides.yml` file replacing
`<STACK_NAME>` with the name of the stack to be used in the deployment.

```
        secrets:	
            WEBSERVER_CUSTOM_CERT_FILE:	
                external: true	
                name: "<STACK_NAME>_WEBSERVER_CUSTOM_CERT_FILE"	
            WEBSERVER_CUSTOM_KEY_FILE:	
                external: true	
                name: "<STACK_NAME>_WEBSERVER_CUSTOM_KEY_FILE"
```

## Using a Custom Certificate TrustStore

Custom Java TrustStore file for the Alert server to communicate over SSL to external
systems.

The preferred option is to import certificates via the Alert UI if you log in as a
system administrator. Follow these instructions to supply a TrustStore on
application startup.

- Must have a valid JKS trust store file that can be used as the TrustStore for
  Alert. If certificate errors arise, then this is the TrustStore where
  certificates will need to be imported to resolve those issues.
- Only one of the following secrets needs to be created. If both are created, then
  jssecacerts secret will take precedence and be used by Alert.

### jssecacerts

The Java TrustStore file with any custom certificates imported replacing
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<PATH_TO_TRUST_STORE_FILE>` with the
path to the TrustStore file to be used.

```
$ docker secret create <STACK_NAME>_jssecacerts <PATH_TO_TRUST_STORE_FILE>
```

### cacerts

The Java TrustStore file with any custom certificates imported. Replace
`<STACK_NAME>` with the name of the stack to be used in
the deployment and `<PATH_TO_TRUST_STORE_FILE>` with the
path to the TrustStore file to be used.

```
$ docker secret create <STACK_NAME>_cacerts <PATH_TO_TRUST_STORE_FILE>
```

Uncomment the following from the
`docker-compose.local-overrides.yml` file
`secrets:` section of the Alert
service.

```
        secrets:	
            jssecacerts:	
                external: true	
                name: "<STACK_NAME>_jssecacerts"
```

Replacing
`<STACK_NAME>` with the name of the stack to be
used in the deployment.

```
        secrets:	
            cacerts:	
                external: true	
                name: "<STACK_NAME>_cacerts"
```

Uncomment
the following from the `docker-compose.local-overrides.yml`
file `secrets:` section of the alert
service.

```
        secrets:	
            - source: jssecacerts	
              target: jssecacerts	
              mode: 0664
```

Or

```
        secrets:	
            - source: cacerts	
              target: cacerts	
              mode: 0664
```

Note: The mode (file permissions) must be specified because the certificate file is copied to
a location Alert uses internally. Read/Write permissions are required to
copy the file and import certificates into the
TrustStore.

Create a docker secret containing the password for the trust store replacing `<STACK_NAME>` with the name of the stack to be used in the deployment and
`<FILE_CONTAINING_PASSWORD>` with the path to the
file containing the password
text.

```
$ docker secret create <STACK_NAME>_ALERT_TRUST_STORE_PASSWORD <FILE_CONTAINING_PASSWORD>
```

Make
sure the Alert service is uncommented from the
`docker-compose.local-overrides.yml`
file.

Uncomment the following from the
`docker-compose.local-overrides.yml` file
`secrets:` section of the alert
service.

```
            alert:	
                secrets:	
                    - ALERT_TRUST_STORE_PASSWORD
```

Uncomment the
following from the secrets section of the
`docker-compose.local-overrides.yml` file replacing
`<STACK_NAME>` with the name of the stack to be
used in the
deployment.

```
            secrets:	
                ALERT_TRUST_STORE_PASSWORD:	
                  external: true	
                  name: "<STACK_NAME>_ALERT_TRUST_STORE_PASSWORD"
```

## Environment Variables

Alert supports initial configuration of the application's components via
environment variables. Environment variable values are only used if
there is no configuration data for the corresponding component in the database.
Please see the Environment Variable Classifications to understand
how environment variables pertain to Alert configuration data. Edit the
`docker-compose.local-overrides.yml` file to include the
environment variables.

Important: The `docker-compose.local-overrides.yml`
values are only used to initialize the DB when Alert starts for the first
time. If the Alert DB already exists, configuration values added here, such
as adding a provider, will not be reflected in the configuration.

### Editing the Overrides File

- Verify that `alert:` is uncommented from the service
  section; otherwise, uncomment the `alert:` of
  `docker-compose.local-overrides.yml`.
- Uncomment `environment:` from the alert service section
  of `docker-compose.local-overrides.yml`.
- Environment variables have the format `-
  <VARIABLE_NAME>=<VARIABLE_VALUE>`
- Environment variables are commented out in the
  `docker-compose.local-overrides.yml` file.
- Uncomment the environment variables to be used from the
  `environment:` section of the alert service.

Example:

```
alert:
    environment:
        - ALERT_HOSTNAME=localhost
```

### Hostname Variable

The `ALERT_HOSTNAME` environment variable must be specified in
order for Alert to generate and use certificates correctly.

- Add the `ALERT_HOSTNAME` environment variable. (The value
  must be the hostname only.)

Edit the overrides file replacing `<NEW_HOST_NAME>` with
the hostname of the machine where Alert is installed.

```
    alert:
        environment:
            - ALERT_HOSTNAME=<NEW_HOST_NAME>
```

Important: Do not add the protocol a.k.a scheme to the value of
the variable.

- Correct: `ALERT_HOSTNAME=myhost.example.com`
- Incorrect: `ALERT_HOSTNAME=https://myhost.example.com`

#### Database Variables

There are additional environment variables to control how Alert connects
to a database independent of the user and password secrets. These
include `POSTGRES_DB` in the alertdb service, and
`ALERT_DB_HOST`, `ALERT_DB_PORT`, and
`ALERT_DB_NAME` in the Alert service.

Change the `POSTGRES_DB` in the alertdb service if you
want to use a different database name. Edit the overrides file replacing
`<DB_NAME>` with the name of the database to
create in Postgres to store Alert data.

```
          alertdb:
              # Comment or remove the POSTGRES_USER and POSTGRES_PASSWORD if secrets are used for credentials.
              environment:
                - POSTGRES_DB=<DB_NAME>
```

The following variables in the overrides file are under the comment in
the Alert service section.

```
    # -- Database Settings
```

Add the `ALERT_DB_HOST` environment variable only if the
alertdb service is using a different hostname. (The value must be the
hostname only of the database.)

Edit the overrides file replacing `<DB_HOST_NAME>`
with the hostname of the machine where Postgres is installed.

```
        alert:
            environment:
                - ALERT_DB_HOST=<DB_HOST_NAME>
```

Important: Do not add the protocol a.k.a scheme to the value
of the variable.

- Incorrect: `ALERT_DB_HOST=myhost.example.com`
- Correct: `ALERT_DB_HOST=https://myhost.example.com`

Edit the overrides file replacing
`<DB_PORT>` with the port used by the
Postgres database `(default is 5432)`:

```
        alert:
            environment:
                - ALERT_DB_PORT=<DB_PORT>
```

Add the `ALERT_DB_NAME` environment variable if the
`POSTGRES_DB` variable name of the alertdb
service is not the default.

Edit the overrides file replacing
`<DB_NAME>` with the name of the database
created in Postgres to store Alert
data.
