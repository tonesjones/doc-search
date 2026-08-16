---
title: "Helm Install"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/helm-install.html"
content_id: "bWp80mGDth5QSPFk5LX8iA"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:20.154121+00:00"
---

# Helm Install

This document describes how to install Alert via Helm.

## Prerequisites

Installation Requirements

## Installing the Chart -- Helm 2

### Add the helm repository

```
$ helm repo add blackduck https://repo.blackduck.com/artifactory/cloudnative/
```

```
### Create the Namespace

```bash
$ kubectl create ns <namespace>
```

### Configure your Alert Instance

Modify the values.yaml file or pass in values to `helm install` with `--set`.

### Install the Alert Chart

```
$ helm install blackduck/blackduck-alert --name <name> --namespace <namespace>
```

Tip: List all releases using `helm list`.

## Installing the Chart -- Helm 3

### Add the helm repository

```
 $ helm repo add blackduck https://repo.blackduck.com/artifactory/cloudnative/
```

### Create the Namespace and TLS Secrets

```
$ kubectl create ns <namespace>
```

### Configure your Alert Instance

Modify the values.yaml file or pass in values to `helm install` with `--set`. Please see the Configuration section for more details.

### Install the Alert Chart

```
$ helm install <name> blackduck/blackduck-alert --namespace <namespace>
```

## Quick Start with Helm 3

### Step 1

Navigate to the alert-helm chart repository in your terminal.

```
$ cd <path>/alert-helm
```

### Step 2

```
$ kubectl create ns myalert
```

### Step 3

Deploy Alert

```
$ helm install myalert blackduck/blackduck-alert --namespace myalert
```

## Changing the server port

For Helm installs, changing the server port is straightforward.

To set the properties via the values.yaml file, change the value of the following properties followed by a `helm upgrade` command.

```
alert:
  hostname: localhost
  port: 8443
```

Alternatively, the environs `ALERT_HOSTNAME` and `ALERT_SERVER_PORT` can be set via a `helm install` command.

```
--set environs.ALERT_HOSTNAME=localhost
```

You must also change the healthcheck found under /templates/alert.yaml to point to the port you have specified otherwise the pod will exit due to the failed probe call to the now incorrect port.

```
        livenessProbe:
          exec:
            command:
              - /usr/local/bin/docker-healthcheck.sh
              - https://localhost:8443/alert/api/about
```

## Finding Alert External Port

Once Alert has been deployed if the `exposeui` parameter is true, then Alert will be available via an exposed port. To determine the port to access the Alert UI execute the following command:

```
$ kubectl -n <NAMESPACE> get services
```

From the output find the Alert exposed service. This service will be your Alert installation name with the `-exposed` suffix in the name. If the installation name is 'myalert' then there will be a service `myalert-exposed` in the list of services.

It will display a port with the following format:

`<INTERNAL_PORT>:<EXTERNAL_PORT>/TCP`

For example:

`8443:31594/TCP`

The internal port is 8443 and the external port is 31594. When accessing the Alert UI the external port will be used in the URL. Once the external port is identified the URL to access the UI will be in the following format:

`https://<EXTERNAL_NODE_IP>:<EXTERNAL_PORT>/alert`

```
$ kubectl get nodes -o wide
```

For example:

`https://127.0.0.0:31594/alert`

## Uninstalling the Chart

To uninstall/delete the deployment:

```
$ helm delete <name>
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following table lists the configurable parameters of the Alert chart and their default values.

### Configuration Parameters

A brief description of each parameter in the values.yaml file.

| Parameter | Description | Default |
| --- | --- | --- |
| `alert.imageTag` | Image tag for the Alert container | `docker.io/blackducksoftware/blackduck-alert:ALERT_VERSION_TOKEN` |
| `alert.registy` | The container registry for the Alert pod | `""` |
| `alert.port` | The internal port the Alert pod will use | `8443` |
| `alert.resources.limits.memory` | Alert container Memory Limit | `2560M` |
| `alert.resources.requests.memory` | Alert container Memory Request | `2560M` |
| `alert.persistentVolumeClaimName` | The name of the persistent storage claim | `""` |
| `alert.claimSize` | The persistent storage claim size limit | `5Gi` |
| `alert.storageClass` | The name of the storage class for persistent storage | `""` |
| `alert.volumeName` | The name of the persistent storage volume | `""` |
| `alert.nodeSelector` | Alert node labels for pod assignment | `{}` |
| `alert.tolerations` | Alert node tolerations for pod assignment | `[]` |
| `alert.affinity` | Alert node affinity for pod assignment | `{}` |
| `alert.securityContext` | Alert security context | `{}` |
| `alert.podSecurityContext` | Alert pod security context | `{}` |
| `cfssl.imageTag` | Image for the Cfssl container | `docker.io/blackducksoftware/blackduck-cfssl:1.0.1` |
| `cffsl.registy` | The container registry for the Cfssl pod | `""` |
| `cfssl.resources.limits.memory` | Cfssl container Memory Limit | `640M` |
| `cfssl.resources.requests.memory` | Cfssl container Request Limit | `640M` |
| `cfssl.nodeSelector` | Cfssl node labels for pod assigment | `{}` |
| `cfssl.tolerations` | Cfssl node tolerations for pod assignment | `[]` |
| `cfssl.affinity` | Cfssl node affinity for pod assignment | `{}` |
| `cfssl.securityContext` | Cfssl node security context | `{}` |
| `cfssl.podSecurityContext` | Cfssl pod security context | `{}` |
| `postgres.registry` | Postgres registry containing image for the container | `"docker.io/centos"` |
| `postgres.isExternal` | If true, do not deploy a Postgres container | `false` |
| `postgres.host` | Host name of the Postgres database | `""` |
| `postgres.port` | Port of the Postgres database | `5432` |
| `postgres.userUserName` | Postgres database user owning the database Alert uses | `sa` |
| `postgres.userPassword` | Postgres database password for the user | `blackduck` |
| `postgres.databaseName` | Postgres database name where Alert data will be stored | `alertdb` |
| `postgres.adminUserName` | Postgres database admin user | `postgres` |
| `postgres.adminPassword` | Postgres database password for the admin user | `""` |
| `postgres.dbCredential.secretName` | The name of the secret that contains the database user's username & password | `""` |
| `postgres.dbCredential.usernameKey` | The key containing the database user's username | `"ALERT_DB_USERNAME"` |
| `postgres.dbCredential.passwordKey` | The key containing the database user's password | `"ALERT_DB_PASSWORD"` |
| `postgres.dbAdminCredential.secretName` | The name of the secret that contains both the database admin's username & password | `""` |
| `postgres.dbAdminCredential.usernameKey` | The key containing the database admin's username | `"ALERT_DB_ADMIN_USERNAME"` |
| `postgres.dbAdminCredential.passwordKey` | The key containing the database admin's username | `"ALERT_DB_ADMIN_PASSWORD"` |
| `postgres.persistentVolumeClaimName` | Postgres node volume claim name | `""` |
| `postgres.claimSize` | Postgres node volume claim size | `"5Gi"` |
| `postgres.storageClass` | Postgres node storage class for volume claim | `""` |
| `postgres.volumeName` | Postgres node volume name for pod assignment | `""` |
| `postgres.nodeSelector` | Postgres node labels for pod assignment | `{}` |
| `postgres.tolerations` | Postgres node tolerations for pod assignment | `[]` |
| `postgres.affinity` | Postgres node affinity for pod assignment | `{}` |
| `postgres.podSecurityContext` | Postgres node pod security context | `{}` |
| `postgres.securityContext` | Postgres node security context | `{}` |
| `postgres.resources` | Postrges node resources | `{}` |
| `rabbitmq.imageTag` | Image tag for the RabbitMQ container | 'docker.io/blackducksoftware/blackduck-alert-rabbitmq:ALERT_VERSION_TOKEN' |
| `rabbitmq.registry` | The container registry for the RabbitMQ pod | '""' |
| `rabbitmq.isExternal` | If true, do not deploy a RabbitMQ container | 'false' |
| `rabbitmq.host` | RabbitMQ host name | '""' |
| `rabbitmq.port` | RabbitMQ port | '5672' |
| `rabbitmq.virtualHost` | RabbitMQ virtual host name | 'blackduck-alert' |
| `rabbitmq.managementPort` | RabbitMQ management port | '15672' |
| `rabbitmq.credential.secretName` | The name of the secret that contains both the RabbitMQ username & password | '""' |
| `rabbitmq.credential.usernameKey` | The key containing the RabbitMQ username | '"ALERT_RABBITMQ_USER"' |
| `rabbitmq.credential.passwordKey` | The key containing the RabbitMQ password | '"ALERT_RABBITMQ_PASSWORD"' |
| `rabbitmq.persistentVolumeClaimName` | RabbitMQ node volume claim name | '""' |
| `rabbitmq.claimSize` | RabbitMQ node volume claim size | '"2Gi"' |
| `rabbitmq.storageClass` | RabbitMQ storage class for volume claim | '""' |
| `rabbitmq.volumeName` | RabbitMQ node volume name for pod assignment | '""' |
| `rabbitmq.nodeSelector` | RabbitMQ node labels for pod assignment | '{}' |
| `rabbitmq.tolerations` | RabbitMQ node tolerations for pod assignment | '[]' |
| `rabbitmq.affinity` | RabbitMQ node affinity for pod assignment | '{}' |
| `rabbitmq.podSecurityContext` | RabbitMQ node pod security context | '{}' |
| `rabbitmq.securityContext` | RabbitMQ node security context | '{}' |
| `rabbitmq.resources.limits.memory` | RabbitMQ node memory limit | '"1024Mi"' |
| `blackDuckName` | The ReleaseName of the Black Duck instance | `""` |
| `blackDuckNamespace` | The Namespace of the Black Duck instance | `""` |
| `deployAlertWithBlackDuck` | If true, Alert will be configured to run with a Black Duck SCA instance | `false` |
| `enableCertificateSecret` | If true, Alert will use values in a Secret for authenticating it's certificates | `false` |
| `enableStandalone` | If true, Alert will be deployed with it's own cfssl instance | `true` |
| `enablePersistentStorage` | If true, Alert will have persistent storage | `true` |
| `environs` | Environment variables for the Alert container | `[]` |
| `exposeui` | If true, a Service to expose the UI will be created | `true` |
| `exposedServiceType` | Type of exposed Service | `NodePort` |
| `exposedNodePort` | The exposed Node Port for public access | `` |
| `imagePullSecrets` | Pull secrets to download images | `[]` |
| `javaKeystoreSecretName` | (deprecated) The name of the secret for the Java certificate truststore | `""` |
| `pvcSize` | Persistent Volume Claim claim size | `5G` |
| `secretEnvirons` | Sensitive environment variables for the Alert container to be stored in a Secret | `[]` |
| `setEncryptionSecretData` | If true, you will be prompted to set values for encrypting Alert's data | `false` |
| `status` | Used to start or stop alert instance | `Running` |
| `storageClassName` | Persistent Volume Claim storage class | `""` |
| `webserverCustomCertificatesSecretName` | The name of the secret containing the SSL certificate and private key for Alert server | `""` |
| `mountPath` | Postgres data mount location | `"/var/lib/postgresql"` |

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```
$ helm install blackduck/blackduck-alert --name <name> --namespace <namespace> --set enableStandalone=true
```

## Database Credential Secrets

This section describes how to configure Alert using kubernetes secrets to set the database user and administrator credentials.

### Create the Database User Credentials Secret

Execute the command as shown, replacing the relevant variables:

```
 $ kubectl create secret generic <SECRET_NAME> -n <ALERT_NAMESPACE> \
 --from-literal=<USERNAME_KEY>=<USER_USERNAME> \
 --from-literal=<PASSWORD_KEY>=<USER_PASSWORD>
```

- Replace `<SECRET_NAME>` with the desired name for the secret.
- Replace `<ALERT_NAMESPACE>` with the namespace used for Alert.
- Replace `<USERNAME_KEY>` with the key mapped to the user's username. By default, this is set to ALERT_DB_USERNAME in values.yaml.
- Replace `<USER_USERNAME>` with the database user's username.
- Replace `<PASSWORD_KEY>` with the key mapped to the user's password. By default, this is set to ALERT_DB_PASSWORD in values.yaml.
- Replace `<USER_PASSWORD>` with the database user's password.

Note: Using this secret will take priority over setting `userUserName` and `userPassword` in the Configuration Parameters in values.yaml.

Example of creating a secret with the name 'alert-db-user-secret' in the 'example' namespace:

```
 $ kubectl create secret generic alert-db-user-secret -n example \
 --from-literal=ALERT_DB_USERNAME=sa \
 --from-literal=ALERT_DB_PASSWORD=blackduck
```

### Create the Database Admin Credentials Secret

Execute the command:

```
 $ kubectl create secret generic <SECRET_NAME> -n <ALERT_NAMESPACE> \
 --from-literal=<ADMIN_USERNAME_KEY>=<ADMIN_USERNAME> \
 --from-literal=<ADMIN_PASSWORD_KEY>=<ADMIN_PASSWORD>
```

- Replace `<SECRET_NAME>` with the desired name for the secret.
- Replace `<ALERT_NAMESPACE>` with the namespace used for Alert.
- Replace `<ADMIN_USERNAME_KEY>` with the key mapped to the admin's username. By default, this is set to ALERT_DB_ADMIN_USERNAME in values.yaml.
- Replace `<ADMIN_USERNAME>` with the database admin's username.
- Replace `<ADMIN_PASSWORD_KEY>` with the key mapped to the admin's password. By default, this is set to ALERT_DB_ADMIN_PASSWORD in values.yaml.
- Replace `<ADMIN_PASSWORD>` with the database admin's password.

Note: Using this secret will take priority over setting `adminUserName` and `adminPassword` in the Configuration Parameters in `values.yaml`.

Example of creating a secret with the name 'alert-db-admin-secret' in the 'example' namespace:

```
 $ kubectl create secret generic alert-db-admin-secret -n example \
 --from-literal=ALERT_DB_ADMIN_USERNAME=postgres \
 --from-literal=ALERT_DB_ADMIN_PASSWORD=adminPassword
```

Note: For an on-premise database deployment of Alert the ALERT_DB_ADMIN_USERNAME is required to be set to 'postgres'.

### Configure Database Credentials Secrets

Once you create the secrets with the correct credentials, you must then tell Alert the name of the secret the credentials correspond to. In the values.yaml file, for the database user, set:

```
postgres.dbCredential.secretName: "<SECRET_NAME>"
postgres.dbCredential.usernameKey: "<USERNAME_KEY>"
postgres.dbCredential.passwordKey: "<PASSWORD_KEY>"
```

- Replace `<SECRET_NAME>` with the name of the secret created in the step Create the Database User Credentials Secret.
- Replace `<USERNAME_KEY>` with the username key used in the same step.
- Replace `<PASSWORD_KEY` with the password key used in the same step.
- In the values.yaml file, for the database admin, set

  ```
  postgres.dbAdminCredential.secretName: "<SECRET_NAME>"
  postgres.dbAdminCredential.usernameKey: "<ADMIN_USERNAME_KEY>"
  postgres.dbAdminCredential.passwordKey: "<ADMIN_PASSWORD_KEY>"
  ```
- Replace `<SECRET_NAME>` with the name of the secret created in the step Create the Database Admin Credentials Secret.
- Replace `<ADMIN_USERNAME_KEY>` with the username key used in the same step.
- Replace `<ADMIN_PASSWORD_KEY>` with the password key used in the same step.

## RabbitMQ Credential Secrets

This section describes how to configure Alert using kubernetes secrets to set the RabbitMQ user credentials.

### Create the RabbitMQ Credentials Secret

Execute the command as shown, replacing the relevant variables:

```
 $ kubectl create secret generic <SECRET_NAME> -n <ALERT_NAMESPACE> \
 --from-literal=<USERNAME_KEY>=<USER_USERNAME> \
 --from-literal=<PASSWORD_KEY>=<USER_PASSWORD>
```

- Replace `<SECRET_NAME>` with the desired name for the secret.
- Replace `<ALERT_NAMESPACE>` with the namespace used for Alert.
- Replace `<USERNAME_KEY>` with the key mapped to the RabbitMQ user's username. By default, this is set to ALERT_RABBITMQ_USER in values.yaml.
- Replace `<USER_USERNAME>` with the database RabbitMQ user's username.
- Replace `<PASSWORD_KEY>` with the key mapped to the RabbitMQ user's password. By default, this is set to ALERT_RABBITMQ_PASSWORD in values.yaml.
- Replace `<USER_PASSWORD>` with the RabbitMQ user's password.

Example:

```
$ kubectl create secret generic alert-rabbitmq-secret -n example \
   --from-literal=ALERT_RABBITMQ_USER=rabbitUser \
   --from-literal=ALERT_RABBITMQ_PASSWORD=rabbitPassword
```

This creates a secret with the name 'alert-rabbitmq-secret' in the 'example' namespace.

### Configure RabbitMQ Credentials Secrets

Once you create the secrets with the correct credentials, you must then tell Alert the name of the secret the credentials correspond to. In the values.yaml file, for the RabbitMQ user, set:

```
rabbitmq.credential.secretName: "<SECRET_NAME>"
rabbitmq.credential.usernameKey: "<USERNAME_KEY>"
rabbitmq.credential.passwordKey: "<PASSWORD_KEY>"
```

- Replace `<SECRET_NAME>` with the name of the secret created in the step Create the RabbitMQ Credentials Secret.
- Replace `<USERNAME_KEY>` with the username key used in the same step.
- Replace `<PASSWORD_KEY` with the password key used in the same step.

## Custom Certificates

This section describes how to configure the Alert webserver with a custom certificate.

### Create Certificate Secret

Execute the command as shown, replacing the relevant variables:

```
 $ kubectl create secret generic <SECRET_NAME> -n <ALERT_NAMESPACE> \
 --from-file=WEBSERVER_CUSTOM_CERT_FILE=<PATH_TO_CERTIFICATE_FILE> \
 --from-file=WEBSERVER_CUSTOM_KEY_FILE=<PATH_TO_CERTIFICATE_KEY_FILE>
```

- Replace `<SECRET_NAME>` with the desired name for the secret.
- Replace `<ALERT_NAMESPACE>` with the namespace used for Alert.
- Replace `<PATH_TO_CERTIFICATE_FILE>` to the path on the current file system to your .crt file.
- Replace `<PATH_TO_CERTIFICATE_KEY_FILE>` to the path on the current file system to the .key file corresponding to your .crt file.

Note: The keys `WEBSERVER_CUSTOM_CERT_FILE` and `WEBSERVER_CUSTOM_KEY_FILE` must be included in the `--from-file=[key=]<FILE_NAME>` arguments for Alert to correctly consume the certificate.

For more information about managing secrets, please see: [managing secrets using kubectl.](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl)

### Configure Certificate Secret

Once you have created the certificate secret with the correct keys, you must then tell Alert the name of the secret the certificate corresponds to. Replace `<SECRET_NAME>` with the name of the secret created in the step Create Certificate Secret.

In the values.yaml file, set:

```
webserverCustomCertificatesSecretName: "<SECRET_NAME>"
```

Note: Configuring the certificate secret will not automatically enable the use of the custom certificate. To do that, follow the instructions in Enable Custom Certificate.

### Enable Custom Certificate

In the values.yaml file, set the value to true to instruct Alert to use the secret specified by the `webserverCustomCertificatesSecretName` configuration parameter as the custom certificate.

```
enableCertificateSecret: true
```

## Persistent Storage

The section will describe the changes needed to configure persistent storage.

Note: If you are using the `HostPath` persistent volume then you must ensure the correct permissions and ownership. If you are using the security context then the ownership must match the UID of the user and the GID of the group specified in the security context. The file permissions must allow a write to the `HostPath` volume. Please see: [Kubernetes HostPath](https://unofficial-kubernetes.readthedocs.io/en/latest/concepts/storage/volumes/#hostpath) for further details.

### Enable Persistent Storage

In the values.yaml file ensure that the setting is `true` which is the default. If this is false when the deployment is uninstalled all data will be lost.

Important: Alert will not startup correctly if this is set to 'true' and persistent volumes are not configured.

```
enablePersistentStorage: true
```

## With Storage Claims

This section defines configuration using Persistent Volume Claims. Claims can be optionally used rather than just a Persistent volume. You must have a claim created for the 'alert' service regardless of an on-premise or external database. For the on-premise database deployment a second Persistent Volume Claim must be created to store the database data.

### Alert Volume Claim Configuration

A persistent volume must be created first if a dynamic provisioner is not being used. It must be created in the same namespace as the Alert deployment and bound to the persistent volume for Alert.

Configure Alert to use the volume claim by replacing <ALERT_CLAIM_NAME> with the name of the persistent volume claim for Alert data.

```
alert:
  persistentVolumeClaimName: "<ALERT_CLAIM_NAME>"
```

An optional storage class with the persistent volume claim requires the addition of the storage class name. Replace <STORAGE_CLASS_NAME> with the name of the storage class in the persistent volume claim.

```
    alert:
      persistentVolumeClaimName: "<ALERT_CLAIM_NAME>"
      storageClassName: "<STORAGE_CLASS_NAME>"
```

Example:

```
  alert:
    persistentVolumeClaimName: "alert-pvc"
    storageClassName: "myStorageClass"
```

### Using On-Premise Database

A persistent volume must be created first for the Postgres database if a dynamic provisioner not being used. It must be created in the same namespace as the Alert deployment for Postgres and bound to the persistent volume for Postgres.

Configure Postgres to use the volume claim by replacing <POSTGRES_CLAIM_NAME> with the name of the persistent volume claim for Postgres data.

```
  postgres:
    persistentVolumeClaimName: "<POSTGRES_CLAIM_NAME>"
```

An optional storage class with the persistent volume claim requires the addition of the storage class name. Replace <STORAGE_CLASS_NAME> with the name of the storage class in the persistent volume claim.

```
    postgres:
      persistentVolumeClaimName: "<POSTGRES_CLAIM_NAME>"
      storageClassName: "<STORAGE_CLASS_NAME>"
```

Example:

```
    postgres:
      persistentVolumeClaimName: "postgres-pvc"
      storageClassName: "myStorageClass"
```

Configure Postgres admin username and password following the instructions outlined here: Using On-Premise Database Configuration

## Without Storage Claims

This section defines configuration using Persistent Volume. Claims will automatically be created and bound to the volumes defined. You must have a Persistent Volume created for the 'alert' service regardless of an on-premise or external database. For the on-premise database deployment a second Persistent Volume must be created to store the database data.

### Alert Volume Configuration

A persistent volume must be created first if a dynamic provisioner not being used. Configure Alert to use the volume name by replacing <ALERT_VOLUME_NAME> with the name of the persistent volume for Alert data.

```
  alert:
    volumeName: "<ALERT_VOLUME_NAME>"
```

An optional storage class with the persistent volume requires the addition of the storage class name. Replace <STORAGE_CLASS_NAME> with the name of the storage class in the persistent volume claim.

```
    alert:
      volumeName: "<ALERT_VOLUME_NAME>"
      storageClassName: "<STORAGE_CLASS_NAME>"
```

Define the claim size which by default is 5GB.

```
    alert:
      claimSize: "5Gi"
```

Example:

```
  alert:
    claimSize: "5Gi"
    storageClassName: "myStorageClass"
    volumeName: "alert-volume"
```

A claim will be created with the release name for example 'myalert-pvc' please verify the claim bound to the volume.

```
$ kubectl -n <ALERT_NAMESPACE> get pvc
```

### Using On-Premise Database

A persistent volume must be created first for the Postgres database if a dynamic provisioner is not being used. Configure Alert to use the volume name by replacing <POSTGRES_VOLUME_NAME> with the name of the persistent volume for Postgres data.

```
  postgres:
    volumeName: "<POSTGRES_VOLUME_NAME>"
```

An optional storage class with the persistent volume requires the addition of the storage class name. Replace <STORAGE_CLASS_NAME> with the name of the storage class in the persistent volume claim.

```
    postgres:
      volumeName: "<POSTGRES_VOLUME_NAME>"
      storageClassName: "<STORAGE_CLASS_NAME>"
```

Define the claim size which by default is 5GB.

```
    postgres:
      claimSize: "5Gi"
```

Example:

```
    postgres:
      claimSize: "5Gi"
      storageClassName: "myStorageClass"
      volumeName: "postgres-volume"
```

A claim will be created with the release name for example 'myalert-postgres' please verify the claim bound to the volume.

```
    $ kubectl -n <ALERT_NAMESPACE> get pvc
```

Configure Postgres admin username and password following the instructions outlined here: Using On-Premise Database Configuration.

## External Postgres Database

### External Postgres Database Requirements

When deploying with an external database follow the information provided for installing with an external database.

### Configuring the External Postgres Database

On the external database create a database owned by the Alert Admin user by replacing <DATABASE_NAME> with the name of the database for Alert and <ROLE_NAME> with the Alert database user created in the previous step.

Note: This step is optional if you want to use an existing database.

```
CREATE DATABASE <DATABASE_NAME> WITH OWNER <ROLE_NAME>
```

Disable on premise database container creation.

```
postgres:
  isExternal: true
```

Configure Alert Postgres user by replacing <ROLE_NAME> with the database user name.

```
postgres:
  userUserName: <ROLE_NAME>
```

Configure Alert Postgres password by replacing <password> with the password of the database user.

```
postgres:
  userPassword: <PASSWORD>
```

Configure Alert Postgres host by replacing <DATABASE_HOST> with the hostname of the database server.

```
postgres:
  host: <DATABASE_HOST>
```

Configure Alert Postgres port by replacing <DATABASE_PORT> with the port the database server is running on.

```
postgres:
  port: <DATABASE_PORT>
```

Configure Alert Postgres database name by replacing <DATABASE_NAME> with the name of the database created in previous steps.

```
postgres:
  databaseName: <DATABASE_NAME>
```

Configure Postgres admin username and password following the instructions outlined here: Using External Database Configuration.

### Database Admin User Password

Alert requires administrator access to configure the database correctly. The following section describes how to configure the administrator credentials for both on-premise and external database configurations.

#### Using On-Premise Database Configuration

While editing the Alert values.yaml, in the postgres section edit the following configurations to set the admin user password of the postgres database. Replace <ADMIN_PASSWORD> with the name of the postgres administrator password.

Note: The *adminUserName* value must remain "postgres" when using the on-premise Postgres database.

```
    postgres:
      adminUserName: postgres
      adminPassword: "<ADMIN_PASSWORD>"
```

Example:

```
    postgres:
      adminUserName: postgres
      adminPassword: my_admin_password
```

Important: For Helm deployments, Alert confirms on startup that the Postgres admin user configured in the values.yaml, has admin permissions. If the configured Postgres admin user does not, the pod will not start and an error will be logged.

#### Using External Database Configuration

Configure your external database settings as described in External Postgres Database. While editing the Alert values.yaml, in the postgres section edit the following configurations to set the admin user password of the postgres database.

Replace <ADMIN_USERNAME> with the name of the postgres administrator username and <ADMIN_PASSWORD> with the name of the postgres administrator password.

```
    postgres:
      adminUserName: "<ADMIN_USERNAME>"
      adminPassword: "<ADMIN_PASSWORD>"
```

Example:

```
    postgres:
      adminUserName: my_admin_username
      adminPassword: my_admin_password
```

#### Installing with Black Duck SCA

Enable deployment with Black Duck SCA by setting 'deployAlertWithBlackDuck' to `true`.

```
deployAlertWithBlackDuck: true
```

Set the exposedNodePort value in the values.yaml file.

```
exposedNodePort: 443
```

Configure the Black Duck release name by replacing <BLACKDUCK_RELEASE_NAME> with the name of the release of Black Duck SCA.

```
blackDuckName: "<BLACKDUCK_RELEASE_NAME>"
```

Configure the Black Duck namespace by replacing <BLACK_DUCK_NAMESPACE> with the namespace where the Black Duck SCA product is deployed.

```
blackDuckNamespace: "<BLACK_DUCK_NAMESPACE>"
```
