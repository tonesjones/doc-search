---
title: "Configuring Persistent Storage"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-persistent-storage.html"
content_id: "mv55hjaU2xFjtNVhY4U4dw"
version: "8.4.0"
section: "Installation References"
scraped_at: "2026-08-08T23:46:28.159199+00:00"
---

# Configuring Persistent Storage

This section describes the changes required to configure persistent storage.

For further information see: [Kubernetes persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

Important: If you are using the HostPath persistent volume then you must
ensure the correct permissions and ownership. If you are using the security context
the ownership must match the UID of the user and the GID of the group specified in
the security context. The file permissions must allow a write to the HostPath
volume. Please see: [Kubernetes storage volumes HostPath](https://unofficial-kubernetes.readthedocs.io/en/latest/concepts/storage/volumes/#hostpath)
for further details.

## Enable Persistent Storage

In the 'values.yaml' file ensure the following parameter is set:

```
enablePersistentStorage: true
```

- This is the default value to prevent loss of data.
- Alert will not startup correctly if this is set to 'true' and persistent volumes
  are not configured.
- If this is set to 'false' when the deployment is uninstalled, all data will be
  lost.

## With Storage Claims

This section defines configuration using Persistent Volume Claims. Claims can be
optionally used rather than just a persistent volume. You must have a claim created
for the 'alert' service regardless of an on-premise or external database. For the
on-premise database deployment a second Persistent Volume Claim must be created to
store the database data.

### Alert Volume Claim Configuration

- A persistent volume must be created first if a dynamic provisioner is not
  being used.
- A persistent volume claim must be created in the same namespace as the
  Alert deployment and bound to the persistent volume for Alert.
- Configure Alert to use the volume
  claim.

  ```
  alert:
    persistentVolumeClaimName: "<ALERT_CLAIM_NAME>"
  ```
- Replace <ALERT_CLAIM_NAME> with the name of the persistent volume
  claim for Alert data.
- An optional storage class with the persistent volume claim requires the
  addition of the storage class
  name.

  ```
  alert:
    persistentVolumeClaimName: "<ALERT_CLAIM_NAME>"
    storageClassName: "<STORAGE_CLASS_NAME>"
  ```
- Replace <STORAGE_CLASS_NAME> with the name of the storage class in
  the persistent volume
  claim.

  ```
  alert:
      persistentVolumeClaimName: "alert-pvc"
      storageClassName: "myStorageClass"
  ```

### Using On-Premise Database

- A persistent volume must be created first for the Postgres database if a
  dynamic provisioner is not being used.
- A persistent volume claim must be created in the same namespace as the
  Alert deployment for Postgres and bound to the persistent volume for
  Postgres.
- Configure Postgres to use the volume
  claim.

  ```
  postgres:
    persistentVolumeClaimName: "<POSTGRES_CLAIM_NAME>"
  ```
- Replace <POSTGRES_CLAIM_NAME> with the name of the persistent
  volume claim for Postgres data
- An optional storage class with the persistent volume claim requires the
  addition of the storage class
  name.

  ```
  postgres:
    persistentVolumeClaimName: "<POSTGRES_CLAIM_NAME>"
    storageClassName: "<STORAGE_CLASS_NAME>"
  ```
- Replace <STORAGE_CLASS_NAME> with the name of the storage class in
  the persistent volume
  claim

  ```
  postgres:
    persistentVolumeClaimName: "postgres-pvc"
    storageClassName: "myStorageClass"
  ```

## Without Storage Claims

This section defines configuration using Persistent Volume. Claims will automatically
be created and bound to the volumes defined. You must have a Persistent Volume
created for the 'alert' service regardless of an on-premise or external database.
For the on-premise database deployment a second Persistent Volume must be created to
store the database data.

### Alert Volume Configuration

- A persistent volume must be created first if a dynamic provisioner not
  being used
- Configure Alert to use the volume
  name

  ```
  alert:
    volumeName: "<ALERT_VOLUME_NAME>"
  ```
- Replace <ALERT_VOLUME_NAME> with the name of the persistent volume
  for Alert data
- An optional storage class with the persistent volume requires the
  addition of the storage class
  name

  ```
  alert:
    volumeName: "<ALERT_VOLUME_NAME>"
    storageClassName: "<STORAGE_CLASS_NAME>"
  ```
- Replace <STORAGE_CLASS_NAME> with the name of the storage class in
  the persistent volume claim.
- Define the claim size by default it is
  5GB.

  ```
  alert:
    claimSize: "5Gi"
  ```

  ```
  alert:
    claimSize: "5Gi"
    storageClassName: "myStorageClass"
    volumeName: "alert-volume"
  ```
- A claim will be created with the release name for example 'myalert-pvc'
  please verify the claim bound to the
  volume.

  ```
  $ kubectl -n <ALERT_NAMESPACE> get pvc
  ```

### Using On-Premise Database

- A persistent volume must be created first for the Postgres database if a
  dynamic provisioner not being used.
- Configure Alert to use the volume
  name.

  ```
  postgres:
    volumeName: "<POSTGRES_VOLUME_NAME>"
  ```
- Replace <POSTGRES_VOLUME_NAME> with the name of the persistent
  volume for Postgres data.
- An optional storage class with the persistent volume requires the
  addition of the storage class
  name.

  ```
  postgres:
    volumeName: "<POSTGRES_VOLUME_NAME>"
    storageClassName: "<STORAGE_CLASS_NAME>"
  ```
- Replace <STORAGE_CLASS_NAME> with the name of the storage class in
  the persistent volume claim
- Define the claim size by default it is
  5GB

  ```
  postgres:
    claimSize: "5Gi"
  ```

  ```
  postgres:
    claimSize: "5Gi"
    storageClassName: "myStorageClass"
    volumeName: "postgres-volume"
  ```
- A claim will be created with the release name for example
  'myalert-postgres' please verify the claim bound to the
  volume

  ```
  $ kubectl -n <ALERT_NAMESPACE> get pvc
  ```
