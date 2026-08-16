---
title: "Black Duck Alert Helm Chart Configuration"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-helm-chart-configuration.html"
content_id: "toeVR~lPYUlelWizUNrmDw"
version: "8.4.0"
section: "Installation References"
scraped_at: "2026-08-08T23:46:32.239464+00:00"
---

# Black Duck Alert Helm Chart Configuration

The following table lists the configurable parameters of the Alert Helm chart and default values.

## Configuration Parameters

Description of each parameter in the values.yaml file.

### Alert - registry location

| Parameter | Description | Default |
| --- | --- | --- |
| `registry` | Registry location | `docker.io/blackducksoftware` |

### Alert - storage configurations

| Parameter | Description | Default |
| --- | --- | --- |
| `enablePersistentStorage` | If true, Alert will have persistent storage | `true` |
| `storageClassName` | Persistent Volume Claim storage class | `""` |

### Alert - cfssl standalone configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `enableStandalone` | If true, Alert will be deployed with it's own cfssl instance | `true` |

### Alert - configurations for the Alert Pod

| Parameter | Description | Default |
| --- | --- | --- |
| `alert.imageTag` | Image tag for the Alert container | `ALERT_VERSION_TOKEN` |
| `alert.registry` | The container registry for the Alert pod | `""` |
| `alert.hostname` | The hostname of the Alert pod | `localhost` |
| `alert.port` | The internal port the Alert pod will use | `8443` |
| `alert.resources.limits.memory` | Alert container Memory Limit | `2560Mi` |
| `alert.persistentVolumeClaimName` | The name of the persistent storage claim | `""` |
| `alert.claimSize` | The persistent storage claim size limit | `5Gi` |
| `alert.storageClass` | The name of the storage class for persistent storage | `""` |
| `alert.volumeName` | The name of the persistent storage volume | `""` |
| `alert.nodeSelector` | Alert node labels for pod assignment | `{}` |
| `alert.tolerations` | Alert node tolerations for pod assignment | `[]` |
| `alert.affinity` | Alert node affinity for pod assignment | `{}` |
| `alert.securityContext` | Alert security context | `{}` |
| `alert.podSecurityContext` | Alert pod security context | `{}` |

### CFSSL - configurations for the cfssl Pod

| Parameter | Description | Default |
| --- | --- | --- |
| `cfssl.imageTag` | Image for the Cfssl container | `1.0.1` |
| `cffsl.registy` | The container registry for the Cfssl pod | `""` |
| `cfssl.resources.limits.memory` | Cfssl container Memory Limit | `640Mi` |
| `cfssl.nodeSelector` | Cfssl node labels for pod assigment | `{}` |
| `cfssl.tolerations` | Cfssl node tolerations for pod assignment | `[]` |
| `cfssl.affinity` | Cfssl node affinity for pod assignment | `{}` |
| `cfssl.securityContext` | Cfssl node security context | `{}` |
| `cfssl.podSecurityContext` | Cfssl pod security context | `{}` |

### Postgres - configurations for the postgres Pod

| Parameter | Description | Default |
| --- | --- | --- |
| `postgres.imageTag` | Image tag for the Postgres pod | `ALERT_VERSION_TOKEN` |
| `postgres.registry` | Postgres registry containing image for the container | `""` |
| `postgres.isExternal` | If true, do not deploy a Postgres container | `false` |
| `postgres.ssl` | If true, Alert uses SSL for external Postgres connection | `false` |
| `postgres.sslMode` | Sets one of the available Postgres [SSL modes](https://www.postgresql.org/docs/current/libpq-ssl.html#LIBPQ-SSL-PROTECTION) | `disable` |
| `postgres.sslUseFiles` | If true, Alert will expect to find ssl certs for communicating with the external Postgres database | `false` |
| `postgres.ssslSecrets.secretName` | Secret file name for file that contains ssl file paths | `""` |
| `postgres.ssslSecrets.sslKeyKey` | SSL certificate key path - must be specified with sslCertKey | `ALERT_DB_SSL_KEY_PATH` |
| `postgres.ssslSecrets.sslCertKey` | SSL certificate path - must be specified with sslKeyKey | `ALERT_DB_SSL_CERT_PATH` |
| `postgres.ssslSecrets.sslRootCertKey` | SSL root certificate path | `ALERT_DB_SSL_ROOT_CERT_PATH` |
| `postgres.host` | Host name of the external Postgres database | `""` |
| `postgres.port` | Port of the Postgres database | `5432` |
| `postgres.userUserName` | Postgres database user owning the database Alert uses | `sa` |
| `postgres.userPassword` | Postgres database password for the user | `blackduck` |
| `postgres.databaseName` | Postgres database name where Alert data will be stored | `alertdb` |
| `postgres.adminUserName` | Postgres database admin user (User must have Admin privileges) | `postgres` |
| `postgres.adminPassword` | Postgres database password for the admin user | `""` |
| `postgres.postgresMigration` | Postgres database migration execution true/false | `""` |
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

### Environment - certificate and UI configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `imagePullSecrets` | Pull secrets to download images comma-delimited string array | `[]` |
| `status` | Used to start or stop alert instance | `Running` |
| `exposeui` | If true, a Service to expose the UI will be created | `true` |
| `exposedServiceType` | Type of exposed Service | `NodePort` |
| `exposedNodePort` | The exposed Node Port for public access | `` |
| `environs` | Environment variables for the Alert container | `[]` |
| `secretEnvirons` | Sensitive environment variables for the Alert container to be stored in a Secret | `{}` |
| `setEncryptionSecretData` | If true, you will be prompted to set values for encrypting Alert's data | `false` |
| `webserverCustomCertificatesSecretName` | The name of the secret containing the SSL certificate and private key for Alert server | `""` |
| `javaKeystoreSecretName` | (deprecated) The name of the secret for the Java certificate truststore | `""` |

### RabbitMQ - configurations for the RabbitMQ pod

| Parameter | Description | Default |
| --- | --- | --- |
| `rabbitmq.imageTag` | Image tag for the RabbitMQ container | `ALERT_VERSION_TOKEN` |
| `rabbitmq.registry` | The container registry for the Alert pod | `""` |
| `rabbitmq.isExternal` | Set to false for running RabbitMQ as a container and true for external RabbitMQ instance | `false` |
| `rabbitmq.host` | Only for external RabbitMQ - will point to <name>-rabbitmq | `""` |
| `rabbitmq.port` | RabbitMQ service port | `5672` |
| `rabbitmq.management.port` | RabbitMQ service port | `15672` |
| `rabbitmq.virtualHost` | Virtual host name | `blackduck-alert` |
| `rabbitmq.credential.secretName` | Secret that contains the regular username and password | `""` |
| `rabbitmq.credential.usernameKey` | Credential user | `ALERT_RABBITMQ_USER` |
| `rabbitmq.credential.passwordKey` | Credential password | `ALERT_RABBITMQ_PASSWORD` |
| `rabbitmq.cluster.erlangCookie.secretName` | Secret name | `""` |
| `rabbitmq.cluster.erlangCookie.cookieKey` | Cookie key name | `RABBITMQ_ERLANG_COOKIE` |
| `rabbitmq.persistentVolumeClaimName` | The name of the persistent storage claim | `""` |
| `rabbitmq.claimSize` | The persistent storage claim size limit | `2Gi` |
| `rabbitmq.storageClass` | PVC storage class name | `""` |
| `rabbitmq.volumeName` | The name of the persistent storage volume backing the PVC | `""` |
| `rabbitmq.nodeSelector` | Alert node labels for pod assignment | `{}` |
| `rabbitmq.tolerations` | Alert node tolerations for pod assignment | `[]` |
| `rabbitmq.affinity` | Alert node affinity for pod assignment | `{}` |
| `rabbitmq.podSecurityContext` | Alert pod security context | `{}` |
| `rabbitmq.securityContext` | Alert security context | `{}` |
| `rabbitmq.resources.limits.memory` | Alert container Memory Limit | `1024Mi` |

### BlackDuck - deployment configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `deployAlertWithBlackDuck` | If true, Alert will be configured to run with a Black Duck SCA instance | `false` |
| `blackDuckName` | The ReleaseName of the Black Duck SCA instance | `""` |
| `blackDuckNamespace` | The Namespace of the Black Duck SCA instance | `""` |

Specify each parameter using the `--set key=value` argument to `helm install`.

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart.

For example:

```
helm install blackduck/blackduck-alert --name <name> --namespace <namespace> --set enableStandalone=true
```
