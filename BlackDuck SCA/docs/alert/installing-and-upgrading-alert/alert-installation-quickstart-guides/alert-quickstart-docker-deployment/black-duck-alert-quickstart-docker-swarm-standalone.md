---
title: "Black Duck Alert Quickstart (Docker Swarm - standalone)"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-docker-swarm-standalone-.html"
content_id: "elkhMgYuFY0OhIW0EmY0QQ"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:23.503028+00:00"
---

# Black Duck Alert Quickstart (Docker Swarm - standalone)

Note: For this quickstart guide, we will be focusing on the *standalone* deployment method with an internally deployed database.

## Prerequsites

- The Alert deployment [files](https://github.com/blackducksoftware/blackduck-alert/releases).
- An server with enough free resources to start the containers.
- If the cluster is a multi-node swarm deployment, the containers need to be node locked, or backed by persistent storage.

See Installation Requirements for more information.

## Downloading the files

Unzip the blackduck-alert-<RELEASE>-deployment.zip archive downloaded from the link above into a location on your Black Duck SCA server.

## Creating the secrets

To get started, we need 4 secrets:

- `ALERT_ENCRYPTION_PASSWORD`
- `ALERT_ENCRYPTION_GLOBAL_SALT`
- `ALERT_DB_USERNAME`
- `ALERT_DB_PASSWORD`

To create secrets, follow the normal docker commands - We recommend storing the values in a file which can be kept safe

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

Note: A docker-compose.local-overrides.yml for Alert is
found under the docker-swarm deployment folder. For ease of use, this can be
copied into your alert standalone directory and configured from there.

For the purposes of this quickstart guide, create a new file called
docker-compose.local-overrides.yml inside your standalone directory.

Important: The docker-compose.local-overrides.yml values are only used to
initialize the DB when Alert starts for the first time. If the Alert DB already
exists, configuration values added here, such as adding a provider, will not be
reflected in the configuration.

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

## Configuring Environment Variables

Configuration of the Alert application such as authentication, database, providers,
and channels can be performed using environment variables. Environment variable
values are only used if there is no configuration data for the corresponding
component already in the database. These will be read in at startup and configured
by editing the docker-compose.local-overrides.yml file to include the environment
variables you wish to set. The blackduck-alert.env file found under
`blackduck-alert-<VERSION>-deployment\docker-swarm\standalone`
provides a look at the various parameters that can be set. See Environment
Variables for more information. There are a number of different
configuration options which can be statically set. For the purpose of this quick
start guide, we will configure these within the UI.

## Deploy Alert

At this stage, we are ready to deploy. Run the following command within your terminal:

```
docker stack deploy -c docker-compose.yaml -c docker-compose.local-overrides.yaml alert
```

Execute `watch docker service ls` within terminal to ensure that all
services report a state of 1/1. Once everything is started, navigate to `https://HOST_NAME:8443/alert`

At this point, you will be presented with a login screen.

Figure 1. Alert login screen
[image: Alert login with SAML]

| Default USERNAME | Default PASSWORD |
| --- | --- |
| sysadmin | blackduck |

Note: The sysadmin username and password are not related to the sysadmin account of your Black Duck SCA installation.
