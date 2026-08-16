---
title: "Black Duck Alert Quickstart (Helm - External Database)"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-helm-external-database-.html"
content_id: "55qviif8iUK9~sT12UkKzg"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:26.934346+00:00"
---

# Black Duck Alert Quickstart (Helm - External Database)

Note: This quickstart guide will focus on a deployment on an *integrated* deployment with an external database. We will also download the charts, however, it
is possible to use `helm install` with `--set` commands for the deployment.

## Prerequsites

- A Kubernetes cluster (1.9+) with enough free resources to deploy Alert.
- Helm 3
- An existing Black Duck SCA installation.
- A suitable external database. See External Database Requirements.
- NGINX Ingress controller installed.

See Installation Requirements for more information.

Important: The Postgres Admin user must have administrative, superuser priviledge OR the extension (CREATE EXTENSION IF NOT EXISTS "uuid-ossp") must be installed AND the following permission granted to the Postgres Admin user: GRANT UPDATE,SELECT ON public.databasechangeloglock

## Downloading the chart

To download the Alert charts, run the following commands:

```
helm repo add blackduck https://repo.blackduck.com/artifactory/cloudnative/
helm repo update
```

Verify that the Alert charts are available:

```
helm search repo blackduck/blackduck-alert
```

Download the chart to the local machine:

```
helm pull blackduck/blackduck-alert --untar
```

## Create a namespace

```
kubectl create ns alert
```

This will create a folder named `blackduck-alert` within the directory where the above command was executed.

## Alert configuration

Next, configure the values.yaml file. There are several fields to change for the purpose of this quickstart.

Important: The values.yaml settings are only used to initialize the DB when Alert starts for the first time. If the Alert DB already exists, configuration values added here, such as adding a provider, will not be reflected in the configuration.

### Configure the storage class to be used

```
storageClass: <STORAGE_CLASS_NAME>
```

- Replace <STORAGE_CLASS_NAME> with an appropriate provisioner (see vendor considerations)

### Enable deployment with Black Duck SCA by setting 'deployAlertWithBlackDuck'

```
deployAlertWithBlackDuck: true
```

### Configure the Black Duck SCA release name by setting 'blackDuckName'

```
blackDuckName: "<BLACKDUCK_RELEASE_NAME>"
```

- Replace <BLACKDUCK_RELEASE_NAME> with the name of the release of Black Duck SCA

### Configure the Black Duck SCA namespace by setting 'blackDuckNamespace'

```
blackDuckNamespace: "<BLACK_DUCK_NAMESPACE>"
```

- Replace <BLACK_DUCK_NAMESPACE> with the namespace where Black Duck SCA is deployed

### Disable exposing Alert via the NodePort Service

```
exposeui: false
```

The typical deployment method is to configure NGINX ingress to expose the service via an ingress as noted below.

### Disable the on premise database container

```
postgres:
  isExternal: true
```

### Configure Alert Postgres admin user

```
postgres:
  adminUserName: <ADMIN_USERNAME>
```

### Configure Alert Postgres admin password

```
postgres:
  adminPassword: <ADMIN_PASSWORD>
```

### Configure Alert Postgres user

```
postgres:
  userUserName: <ROLE_NAME>
```

### Configure Alert Postgres user password

```
postgres:
  userPassword: <PASSWORD>
```

### Configure Alert Postgres host

```
postgres:
  host: <DATABASE_HOST>
```

### Configure Alert Postgres port

```
postgres:
  port: <DATABASE_PORT>
```

### Configure Alert Postgres database name

```
postgres:
  databaseName: <DATABASE_NAME>
```

### Enable SSL connections to the database (optional)

```
postgres:
  ssl: true
  sslUseFiles: true
  sslSecrets: # Secret that contains all the ssl file paths
    secretName: "alert-ssl-paths"
    sslKeyKey: "ALERT_DB_SSL_KEY_PATH"
    sslCertKey: "ALERT_DB_SSL_CERT_PATH"
    sslRootCertKey: "ALERT_DB_SSL_ROOT_CERT_PATH"
```

Generate a secret which points to the certificates:

```
kubectl create secret generic alert-ssl-paths -n alert \
--from-file=ALERT_DB_SSL_KEY_PATH=/home/user/blackduck-alert/gcpcerts/client-key.pem \
--from-file=ALERT_DB_SSL_CERT_PATH=/home/user/blackduck-alert/gcpcerts/client-cert.pem \
--from-file=ALERT_DB_SSL_ROOT_CERT_PATH=/home/user/blackduck-alert/gcpcerts/server-ca.pem
```

For the purposes of this guide, we will use the following values as our
credentials:

| SECRET | VALUE |
| --- | --- |
| adminUserName | alertadmin |
| adminPassword | Blackduck1! |
| userUserName | alertuser |
| userPassword | Blackduck1! |

Important: Configuration can also be completed using only a root CA certificate as outlined in the following troubleshooting section, Using Root CA Certificate only.

## Configuring Environment Variables

Configuration of the Alert application such as configuring authentication, database,
providers, and channels can be performed using environment variables. Environment
variable values are only used if there is no configuration data for the
corresponding component in the database. These will be read in at startup and are
typically configured in the values.yml file. See Helm Chart
Configuration. There are a number of different configuration options
which can be statically set. For the purpose of this quick start guide, we will
configure these within the UI after deployment.

## Black Duck SCA configuration

Black Duck SCA also needs to be made aware of Alerts presence. Within the values.yml for
your Black Duck SCA install, set the following properties. As this deployment is going
into the same namespace as Black Duck SCA, the `alertNamespace` property
has a default value of `Release.Namespace`.

```
enableAlert: true
```

```
alertName: "<ALERT_RELEASE_NAME>"
```

- Replace <ALERT_RELEASE_NAME> with the name of the release of Alert

## Deploying

### Deploy the Black Duck SCA chart with the updated Alert parameters

```
helm install <BLACK_DUCK_RELEASE_NAME> . -f values.yml -f sizes-gen03\<SPH_SIZE>.yaml -n <BLACK_DUCK_NAMESPACE>
```

## Initialize the Alert database

```
CREATE ROLE alertadmin LOGIN PASSWORD 'Blackduck1!';
CREATE ROLE alertuser LOGIN PASSWORD 'Blackduck1!';
GRANT alertuser TO alertadmin;
CREATE DATABASE alertdb WITH OWNER alertuser;

\c alertdb
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE SCHEMA IF NOT EXISTS alert AUTHORIZATION alertuser;

GRANT USAGE on SCHEMA alert to alertadmin;
GRANT CONNECT ON DATABASE alertdb TO alertadmin;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN schema alert to alertadmin;
GRANT EXECUTE ON ALL FUNCTIONS IN schema alert to alertadmin;
```

### Deploy the Alert chart into the same namespace above

```
helm install <ALERT_RELEASE_NAME> . -f values.yml -n <BLACK_DUCK_NAMESPACE>
```

### Verify that all pods have fully started and there are no errors

```
kubectl get po -n <BLACK_DUCK_NAMESPACE>
```

## Configuring NGINX ingress

Assuming that Black Duck SCA is already exposed via an Ingress Controller, we will now
modify the routes so that the application is available at
`https://<BLACKDUCK_SERVER>/alert`

```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: blackduck-exposed
  namespace: <BLACK_DUCK_NAMESPACE>
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/proxy-body-size: 1024m
    nginx.ingress.kubernetes.io/proxy-buffer-size: 8k
    nginx.ingress.kubernetes.io/secure-backends:  "true"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "300"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "300"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "300"
    nginx.ingress.kubernetes.io/send-timeout: "300"
spec:
  rules:
  - http:
      paths:
        - path: /
          backend:
            serviceName: <BLACK_DUCK_RELEASE_NAME>-blackduck-webserver
            servicePort: 443
        - path: /alert
          backend:
            serviceName: <ALERT_RELEASE_NAME>
            servicePort: 8443
```

Apply the manifest and verify that the ingress has been successfully created

```
kubectl get ing -n <BLACK_DUCK_NAMESPACE>
```

Once created, your Black Duck SCA installation will be available at
`https://<BLACKDUCK_SERVER>`. Alert will be available at
`https://<BLACKDUCK_SERVER>/alert`

At this point, you will be presented with a login screen.

Figure 1. Alert login screen
[image: Alert login with SAML]

| Default USERNAME | Default PASSWORD |
| --- | --- |
| sysadmin | blackduck |

Note: The sysadmin username and password are not related to the sysadmin account of your Black Duck SCA installation.

## Post deployment actions

After installation when Alert has been deployed and the login screen is available,
the following action should be performed if the Alert database admin user does not
have the role of `superuser`:

The Alert admin user declared by the `ALERT_DB_ADMIN_USERNAME`
parameter requires a permissions update. These permissions are for the database
admin to have select and update access to the `databasechangeloglock`
table.

The following is an example of setting the required permissions:

```
GRANT SELECT, UPDATE ON public.databasechangeloglock TO alertadmin;
```

Note: Failure to apply permissions may cause issues if the Alert
container is restarted.
