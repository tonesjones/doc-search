---
title: "Black Duck Alert Quickstart (Docker Swarm)"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-docker-swarm-.html"
content_id: "jys_33jfKopaQEwst_QddQ"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:22.785407+00:00"
---

# Black Duck Alert Quickstart (Docker Swarm)

Note: This quickstart guide will focus on an *integrated* deployment method with an internally deployed database.

## Prerequsites

- The Alert deployment [files](https://github.com/blackducksoftware/blackduck-alert/releases).
- An existing Black Duck SCA server with enough free resources to start the
  containers (If your Black Duck SCA server is already running, stop it before
  attempting to deploy Alert).
- If the cluster is a multi-node swarm deployment, the containers need to be
  node locked, or backed by persistent storage.

See Installation Requirements for more information.

## Downloading the files

Unzip the `blackduck-alert-<RELEASE>-deployment.zip` archive
downloaded from the link above into a location on your Black Duck SCA server.

## Creating the secrets

To get started, we need 4 secrets:

- `ALERT_ENCRYPTION_PASSWORD`
- `ALERT_ENCRYPTION_GLOBAL_SALT`
- `ALERT_DB_USERNAME`
- `ALERT_DB_PASSWORD`

To create secrets, follow the normal docker commands - We recommend storing the
values in a file which can be kept safe

```
docker secret create <STACK_NAME>_<SECRET_NAME> <FILE_CONTAINING_VALUE>
```

example:

```
docker secret create hub_ALERT_ENCRYPTION_PASSWORD ALERT_ENCRYPTION_PASSWORD
```

For the purposes of this quickstart, we will use the following values:

| SECRET | VALUE |
| --- | --- |
| ALERT_ENCRYPTION_PASSWORD | <random 32 char string> |
| ALERT_ENCRYPTION_GLOBAL_SALT | <random 32 char string> |
| ALERT_DB_USERNAME | sa |
| ALERT_DB_PASSWORD | blackduck |

Once the secrets are created, check that all four exist by running `docker secret ls`

## Configuring docker-compose.local-overrides.yml

Note: A docker-compose.local-overrides.yml for Alert is found under the
docker-swarm deployment folder. For ease of use, this can be copied into your
Black Duck SCA install directory as docker-compose.local-overrides.alert.yaml and configured
from there. This keeps Alert and Black Duck SCA deployments seperate which is useful
in scenarios where you want to temporarily disable Alert. Alternatively you can
merge the main Black Duck SCA and Alert overrides files.

For the purposes of this quickstart guide, create a new file called docker-compose.local-overrides.alert.yaml inside your Black
Duck install directory.

Important: The docker-compose.local-overrides.yml values
are only used to initialize the DB when Alert starts for the first time. If the
Alert DB already exists, configuration values added here, such as adding a
provider, will not be reflected in the configuration.

```
---
version: "3.6"
services:
  alert:
    environment:
      - PUBLIC_ALERT_WEBSERVER_PORT=443
      - ALERT_DB_NAME=alertdb
    secrets:
      - ALERT_ENCRYPTION_PASSWORD
      - ALERT_ENCRYPTION_GLOBAL_SALT
      - ALERT_DB_USERNAME
      - ALERT_DB_PASSWORD
  alertdb:
    environment:
      - POSTGRES_DB=alertdb
      - POSTGRES_PASSWORD_FILE=/run/secrets/ALERT_DB_PASSWORD
      - POSTGRES_USER_FILE=/run/secrets/ALERT_DB_USERNAME
    secrets:
      - ALERT_DB_USERNAME
      - ALERT_DB_PASSWORD
secrets:
  ALERT_ENCRYPTION_PASSWORD:
    external: true
    name: hub_ALERT_ENCRYPTION_PASSWORD
  ALERT_ENCRYPTION_GLOBAL_SALT:
    external: true
    name: hub_ALERT_ENCRYPTION_GLOBAL_SALT
  ALERT_DB_USERNAME:
    external: true
    name: hub_ALERT_DB_USERNAME
  ALERT_DB_PASSWORD:
    external: true
    name: hub_ALERT_DB_PASSWORD
```

## Configuring docker-compose.alert.yml

At this point, we now need to merge the docker-compose.yml file found under
`blackduck-alert-<VERSION>-deployment\docker-swarm\hub`
into your hub. This, again, can be done in one of two ways:

- merging the files together in your Black Duck install directory
- copying the file into your Black Duck install directory with a name that distinguishes it (such as docker-compose.alert.yml)

Again, for the purposes of this guide, we will create a new called docker-compose.alert.yml inside the main Black Duck SCA installation directory

```
version: '3.6'
services:
  alertdb:
    image: blackducksoftware/alert-database:1.0.2
    ports: ['5432']
    hostname: alertdb
    volumes: ['alert-db-postgres-volume:/var/lib/postgresql/data']
    healthcheck:
      test: [CMD, /usr/local/bin/alertdb-healthcheck.sh]
      interval: 30s
      timeout: 10s
      retries: 5
    deploy:
    # Optional placement tag in the case of multi node swarm deployments.
    # The database must always persist on the same node
      #placement:
        #constraints:
        #- node.labels.type == db
      mode: replicated
      restart_policy: {condition: on-failure, delay: 5s, window: 60s}
      resources:
        limits: {memory: 1024M}
        reservations: {memory: 1024M}
  alert:
    image: blackducksoftware/blackduck-alert:6.10.0
    ports: ['8443:8443']
    env_file: [blackduck-alert.env]
    healthcheck:
      test: [CMD, /usr/local/bin/docker-healthcheck.sh, 'https://localhost:8443/alert/api/about',
             /opt/blackduck/alert/security/root.crt, /opt/blackduck/alert/security/blackduck_system.crt,
             /opt/blackduck/alert/security/blackduck_system.key]
      interval: 30s
      timeout: 60s
      retries: 15
      start_period: 7200s
    volumes: ['alert-db-volume:/opt/blackduck/alert/alert-config/data']
    deploy:
      mode: replicated
      restart_policy: {condition: on-failure, delay: 15s, window: 60s}
      resources:
        limits: {memory: 2560M}
        reservations: {memory: 2560M}
volumes: {alert-db-volume: null, alert-db-postgres-volume: null}
```

## Configuring Environment Variables

Configuration of the Alert application such as authentication, database, providers,
and channels can be performed using environment variables. Environment variable
values are only used if there is no configuration data for the corresponding
component already in the database. These will be read in at startup and configured
by editing the docker-compose.local-overrides.yml file to include the environment
variables you wish to set. The blackduck-alert.env file found under
`blackduck-alert-<VERSION>-deployment\docker-swarm\hub`
provides a look at the various parameters that can be set. See Environment
Variables for more information. There are a number of different
configuration options which can be statically set. For the purpose of this quick
start guide, we will configure these within the UI.

## Configuring Black Duck SCA Routing

At this point, we need to configure the Black Duck SCA webserver to open up the routing
for UI access. Run the following command within your main Black Duck SCA installation directory:

```
sed -i "s/USE_ALERT=0/USE_ALERT=1/g" "hub-webserver.env"
```

This will expose Alert at https://<BLACK_DUCK_HOST_NAME>:8443/alert when the stack is deployed.

## Deploy Black Duck SCA with Alert

At this stage, we are ready to deploy. Run the following command within your terminal
(bearing in mind any other configuration files required for BDBA, if in use):

```
docker stack deploy -c docker-compose.yaml -c docker-compose.alert.yaml -c sizesgen03\10sph.yaml -c docker-compose.local-overrides.yaml -c docker-compose.local-overrides.alert.yaml hub
```

Execute `watch docker service ls` within terminal to ensure that all
services report a state of 1/1. Once everything is started, navigate to
`https://<BLACK_DUCK_HOST_NAME>:8443/alert`

At this point, you will be presented with a login screen.

Figure 1. Alert login screen
[image: Alert login with SAML]

| Default USERNAME | Default PASSWORD |
| --- | --- |
| sysadmin | blackduck |

Note: The sysadmin username and password are not related to the sysadmin account of your Black Duck SCA installation.
