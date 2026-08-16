---
title: "Configuring custom volumes for Blackduck Storage"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-custom-volumes-for-blackduck-storage.html"
content_id: "NPuvZucm6d7JulFnEmb0fg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:19.870457+00:00"
---

# Configuring custom volumes for Blackduck Storage

The storage container may be configured to use up to three (3) volumes for the storage of
file based objects. In addition, the configuration can be set up to migrate objects from
one volume to another.

## Why more than one volume?

By default, the storage container uses a single volume to store all objects. This
volume is sized based on typical customer usage for stored objects. As each customer
is different, it may become necessary to have more space available than the volume
can provide. Since not all volumes are expandable, it may become necessary to add a
different, larger volume and migrate the data to the new volume.

Another reason why multiple volumes may become necessary is if the volume is hosted
on a remote system (NAS or SAN) and that remote system is due to be decommissioned.
A second volume hosted on a new system would need to be created and the content
moved to it.

## Configuring multiple volumes

To configure custom storage providers in Kubernetes, create an override file
containing the following:

```
storage:
  providers:
    - name: "file-1"
      enabled: true
      index: 1
      type: "file"
      preference: 20
      readonly: false
      migrationMode: "none" 
      existingPersistentVolumeClaimName: ""
      pvc:
        size: "100Gi"
        storageClass: ""
        existingPersistentVolumeName: ""
      mountPath: "/opt/blackduck/hub/uploads"
    - name: "file-2"
      enabled: true
      index: 2
      type: "file"
      preference: 10
      readonly: false
      migrationMode: "none" 
      existingPersistentVolumeClaimName: ""
      pvc:
        size: "200Gi"
        storageClass: ""
        existingPersistentVolumeName: ""
      mountPath: "/opt/blackduck/hub/uploads2"
    - name: "file-3"
      enabled: false
      index: 3
      type: "file"
      preference: 30
      readonly: false
      migrationMode: "none" 
      existingPersistentVolumeClaimName: ""
      pvc:
        size: "100Gi"
        storageClass: ""
        existingPersistentVolumeName: ""
      mountPath: "/opt/blackduck/hub/uploads3"
```

In the above override file both providers 1 and 2 are enabled with provider 2 having a
higher priority (lower preference number) and so all new content is directed there.

The possible settings for each provider are as follows:

| Setting | Details |
| --- | --- |
| `name` | **Default:** none.  **Valid values**: any.  **Notes**: This is a cosmetic label to assist in administration of these providers. |
| `enabled` | **Default:** `true` for provider 1, `false` for others.  **Valid values**: `true` or `false`.  **Notes**: Indicates if the provider is enabled or not. |
| `index` | **Default:** none.  **Valid values**: `1`, `2`, `3`.  **Notes**: Indication of the provider number. The sequence in the configuration file does not matter. |
| `type` | **Default:** `file`.  **Valid values**: `file`.  **Notes**: `"file"` is the only supported provider type. |
| `preference` | **Default:** `index` times 10.  **Valid values**: `0-999`.  **Notes**: Sets the preference of the provider. Providers with the highest priority (lowest preference number) will have new content added to them.  NOTE: All provider preferences must be unique, Two providers cannot share the same value. |
| `readonly` | **Default:** `false`.  **Valid values**: `true` or `false`.  **Notes**: Indicates a provider is read-only. The highest priority (lowest preference number) provider cannot be read-only or the system cannot function.  A read only provider will not have the storage volume altered by addition of data or removal of data, however metadata in the database will be manipulated to record object deletions and other changes. |
| `migrationMode` | **Default:** `none`.  **Valid values**: `none`, `drain`, `delete`, `duplicate`.  **Notes**: Configures the migration mode for the provider, Details of what this mode is and how to use it are provided in the migration section of this document. |
| `existingPersistentVolumeClaimName` | **Default:** `""`.  **Valid values**: any valid k8s identifier.  **Notes**: Allows you to specify a specific persistence volume claim name for this volume. |
| `pvc.size` | **Default:** `none`.  **Valid values**: any valid size.  **Notes**: Allows you to specify the amount of space available to the volume. |
| `pvc.storageClass` | **Default:** `""`.  **Valid values**: any valid k8s identifier.  **Notes**: Allows you to specify a specific storage class for this volume. |
| `pvc.existingPersistentVolumeName` | **Default:** `""`.  **Valid values**: any valid k8s identifier.  **Notes**: Allows you to specify a specific persistence volume name for this volume. |
| `mountPath` | **Default:** specific to index - see notes.  **Valid values**:  /opt/blackduck/hub/uploads  /opt/blackduck/hub/uploads2  /opt/blackduck/hub/uploads3  **Notes**: Sets the mount point for a specific provider. A provider with index one (1) must specify the mount point /opt/blackduck/hub/uploads. A provider with index two (2) must specific the mount point  /opt/blackduck/hub/uploads2. A provider with index three (3) must specify the mount point  /opt/blackduck/hub/uploads3 |

## Migrating Between Volumes

With multiple volumes configured, it is possible to migrate content from one or more
provider volumes to a new provider volume. This can only be done for providers that
are not the highest priority (lowest preference). To do this, configure the volumes
with one of the following migration modes. Once configured, Black Duck needs to be
restarted in order to initiate the migration which is performed by a job in the
background until it is completed.

| Migration Mode | Details |
| --- | --- |
| `none` | **Purpose**: To indicate no migration is in progress.  **Notes**: The default migration mode. |
| `drain` | **Purpose**: This mode moves content from the configured provider to the highest priority (lowest preference number) provider. Once content is moved, it is removed immediate from the source provider.  **Notes**: This is a straight move operation - adding it to the target provider and removing it from the source. |
| `delete` | **Purpose**: This mode copies content from the configured provider to the highest priority (lowest preference number) provider. Once content is copied, it is marked for deletion in the source provider. The standard deletion retention periods apply - after that period the content is removed.  **Notes**: This is a move that allows for the ability for the system to be recovered from backup within the retention window so that content in the source provider remains viable. The default retention period is 6 hours. |
| `duplicate` | **Purpose**: This mode copies content from the configured provider to the highest priority (lowest preference number) provider. Once content is copied, the source is left unaltered, including the metadata.  **Notes**: After the duplicate migration, you will have two volumes with all of the content and the metadata in the database. If you take the next step in the “duplicate and dump” process and unconfigure the original volume, the files will be deleted but the metadata will remain in the database - referencing an unknown volume generating a warning in the pruner jobs (a job error). To resolve the error, use the following property to enable the pruning of the orphaned metadata records:  ``` storage.pruner.orphaned.data.pruning.enable=true ``` |
