---
title: "Configuring mTLS on an external database"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-mtls-on-an-external-database.html"
content_id: "0aAxPVohk5AYGLiCkmMeJg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:23.885721+00:00"
---

# Configuring mTLS on an external database

## Prerequisites

Before configuring mTLS for an external database in a Kubernetes deployment, ensure
the following:

1. **Environment setup**:

   - Kubernetes and Helm are installed and properly configured.
   - Persistent Volumes (PV) and Persistent Volume Claims (PVC) are set up
     in your environment.
2. **Deployment preparation**:

   - You have identified the correct deployment files to use and know
     where to download them.
   - You are familiar with setting up a Black Duck
     deployment using an external database.
   - You have the necessary commands ready for running a Black Duck deployment with an external
     database.
3. **mTLS requirements**:

   - The `openssl.cnf` file is available on your server for
     generating certificates.
   - Secrets are named using the default values provided in the deployment
     instructions.
   - Depending on your deployment, you may have up to five secrets for
     mTLS: root certificate, admin certificate & key, and user
     certificate & key. If you are not using one or more of these,
     update the corresponding entries in the `values.yaml`
     file to an empty string ( "" ).

     - Example: To configure the root certificate, update the
       `postgres.customCerts.rootCAKeyName`
       field in value.yaml. By default, this is set to
       "`HUB_POSTGRES_CA`". If you do not have a
       root certificate, set this value to "".
4. **Namespace consistency**:

   - Both the Black Duck and PostgreSQL deployments
     use the same namespace.

## Changes to your Black Duck deployment

## Updating `values.yaml`

To configure mTLS for your Black Duck deployment, you must
update the `values.yaml` file with the necessary settings secrets.
Follow these steps:

1. **Configure `postgres.sslMode`**

   Add the `postgres.sslMode` configuration option to
   `values.yaml`. This option determines whether the
   deployment will include certificate ane key secrets. If this option
   is not configured, the setenv.sh script will exclude the cert/key
   secrets from the deployment. Ensure this value is set to enable
   mTLS.
2. **Set the secret name for custom certificates**

   Add the `postgres.customCerts.useCustomCerts` option to
   `values.yaml`. This specifies the name of the secret
   containing the necessary certificate and key data for connecting to the
   external database (e.g., root CA, admin cert/key, and user cert/key).
3. **Define custom certificate data**

   Under the `postgres.customCerts` section in
   `values.yaml`, configure the following five options to
   specify the data for the certificates and keys:

   - `rootCAKeyName`: The key name for the root CA
     certificate.
   - `clientCertName`: The key name for the user
     certificate.
   - `clientKeyName`: The key name for the user private
     key.
   - `adminClientCertName`: The key name for the admin
     certificate.
   - `adminClientKeyName`: The key name for the admin private
     key.

   Ensure these values match the names in your secrets configuration.

## Configuring SSL secrets in `setenv.sh`

To enable mTLS for pods using an external database, modifications are required in the
`setenv.sh` script for each pod. The following steps outline the
changes and logic to handle SSL secrets:

1. **Update logic for SSL secrets**

   Modify the `setenv.sh` script for each pod that uses
   certificates to include logic for handling five new SSL secrets. The updated
   logic should include:

   - For non-external databases:

     - Ignore all SSL secrets and use internally generated Black Duck keys and certificates.
     - Override `sslmode` to
       `verify-ca` for internal use.
   - For external databases:

     - If `enable ssl` is set to
       `false`, ignore SSL secrets.
     - If `sslmode` is set to ignore, ignore SSL
       secrets.
   - Default configuration:

     If none of the above conditions are met, configure the following
     environment variables based on the provided SSL secrets:

     - `DB_SSL_CA`: Root CA certificate.
     - `DB_SSL_CRT` and `DB_SSL_KEY`:
       User certificate and private key.
     - `DB_ADMIN_SSL_CRT` and
       `DB_ADMIN_SSL_KEY`: Admin certificate and
       private key.
2. **Validate configuration**

   Ensure the modified `setenv.sh` script is tested across all
   relevate pods to confirm it correctly applies the SSL secrets and exits
   cleanly for valid setups.

## Updating `_postgresql.tpl`

To properly support mTLS with an external database, updates to the
`_postgresql.tpl` file are required. These chagnes ensure the
correct handling of SSL-related settings and secrets:

1. **Correct logic for
   `HUB_POSTGRES_ENABLE_SSL_CERT_AUTH`**

   Previously, `HUB_POSTGRES_ENABLE_SSL_CERT_AUTH` was hardcoded
   to `false` for external databases. Update the logic to
   correctly determine whether SSL certificate authentication should be enabled
   based on deployment configuration.
2. **Add logic for `HUB_POSTGRES_SSL_MODE`**

   Introduce logic to set the `HUB_POSTGRES_SSL_MODE` environment
   variable. This ensures that the SSL mode is accurately configured for
   external database connections.
3. **Add conditional volume and volumemount logic**

   Add conditions to dynamically include volumes and volume mounts for five new
   SSL secrets: Root CA certificate, user certificate and private key, admin
   certificate and private key.
4. **Set `PGSSLMODE` environment variable**

   Include logic to set `PGSSLMODE` as an environment variable
   withing the PostgreSQL init pod. This ensures the init pod respects the SSL
   mode configured in the deployment.

## Updating `configmap.yaml`

Update the `configmap.yaml` file to include the
`HUB_POSTGRES_SSL_MODE` configuration.

## Updating `postgres-config.yaml`

Include logic for setting `HUB_POSTGRES_ENABLE_SSL_CERT_AUTH`.

## Updating `postgres-init.yaml`

To support mTLS, the following changes are required in the
`postgres-init.yaml` file:

1. Add volume and volume mount logic for the five new SSL secrets.
2. Include logic to set the `PGSSLMODE` environment variable.
3. Add logic to set the `PGSSLROOTCERT` environment variable.
4. Set the `PGSSLCERT` environment variable first based on
   `HUB_POSTGRES_CRT` and then on
   `HUB_ADMIN_POSTGRES_CRT`. Separate `if`
   statements should be used for clarity.
5. Set the `PGSSLKEY` environment variable first based on
   `HUB_POSTGRES_KEY` and then on
   `HUB_ADMIN_POSTGRES_KEY`. Separate `if`
   statements should be used for clarity.
6. Reorganize shell command logic by moving the logic for running
   `/tmp/postgres-init/init.pgsql` and grouping it with
   other shell commands for improved readability.

## Update environs

Add `HUB_POSTGRES_ENABLE_SSL_CERT_AUTH: "true"` to environs.

## Update `postgres.name`

After starting the database pod, retrieve the host value for the pod and update the
`postgres.host` field in `values.yaml`.

## Update postgres.customCerts.useCustomCerts

Update `postgres.customCerts.useCustomCerts` to
`true`.

## Create the secret for certificates and keys

Use the following command to create the secret for certificates and keys:

```
kubectl create secret generic -n bdbd-blackduck-postgres-certificate --from-file=HUB_POSTGRES_CA=root.crt
        --from-file=HUB_POSTGRES_CRT=blackduck_user.crt
        --from-file=HUB_POSTGRES_KEY=blackduck_user.pk8
        --from-file=HUB_ADMIN_POSTGRES_CRT=blackduck_admin.crt
        --from-file=HUB_ADMIN_POSTGRES_KEY=blackduck_admin.pk8
```
