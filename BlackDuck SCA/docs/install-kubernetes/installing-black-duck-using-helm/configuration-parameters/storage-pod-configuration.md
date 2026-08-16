---
title: "Storage pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/storage-pod-configuration.html"
content_id: "DrjL5VkfJVUq3t2aoBSh9w"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:14.681533+00:00"
---

# Storage pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `storage.registry` | Image repository to be override at container level |  |
| `storage.requestCpu` | Storage container CPU request | `1000m` |
| `storage.resources.limits.memory` | Storage container Memory Limit | `2048Mi` |
| `storage.resources.requests.memory` | Storage container Memory request | `2048Mi` |
| `storage.maxRamPercentage` | Storage container maximum heap size | `60` |
| `storage.persistentVolumeClaimName` | Point to an existing Storage Persistent Volume Claim (PVC) |  |
| `storage.claimSize` | Storage Persistent Volume Claim (PVC) claim size | `100Gi` |
| `storage.storageClass` | Storage Persistent Volume Claim (PVC) storage class |  |
| `storage.volumeName` | Point to an existing Storage Persistent Volume (PV) |  |
| `storage.nodeSelector` | Storage node labels for pod assignment | `{}` |
| `storage.tolerations` | Storage node tolerations for pod assignment | `[]` |
| `storage.affinity` | Storage node affinity for pod assignment | `{}` |
| `storage.podSecurityContext` | Storage security context at pod level | `{}` |
| `storage.securityContext` | Storage security context at container level | `{}` |
| `storage.providers` | Configuration to support multiple storage platforms. Please refer to *Storage Providers* section for additional details. | `[]` |

## Storage Providers

The provider in storage service refers to a persistence type and its configuration.
Black Duck manages tools, application reports and other
large blobs under storage service. Currently, it supports only the filesystem as one
of the provider.

```
storage:
  providers:
    - name: <name-for-the-provider> <String>
      enabled: <flag-to-enable/disable-provider> <Boolean>
      index: <index-value-for-the-provider> <Integer>
      type: <storage-type> <String>
      preference: <weightage-for-the-provider> <Integer>
      existingPersistentVolumeClaimName: <existing-persistence-volume-claim-name> <String>
      pvc:
        size: <size-of-the-persistence-disk> <String>
        storageClass: <storage-class-name> <String>
        existingPersistentVolumeName: <existing-persistence-volume-name> <String>
      mountPath: <mount-path-for-the-volume> <String>
```

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `String` | A name for the provider configuration. Eg. blackduck-file-storage |  |
| `enabled` | `Boolean` | A flag to control enabling/disabling of the provider instance | `false` |
| `index` | `Integer` | An index value for the provider configuration. Eg. 1,2,3. |  |
| `type` | `String` | Storage type. Defaults to `file`. | `file` |
| `preference` | `Integer` | A number denoting the weightage for the provider instance configuration. If multiple provider instances are configured, then this value is used to determine which provider to be used as default storage option. |  |
| `existingPersistentVolumeClaimName` | `String` | An option to re-use existing persistent volume claim for the provider |  |
| `pvc.size` | `String` | The volume size to be used while creating persistent volume. A minimum size of `100Gi` is recommended for storage service. | `100Gi` |
| `pvc.storageClass` | `String` | The storage class to be used for persistent volume |  |
| `pvc.existingPersistentVolumeName` | `String` | An option to re-use existing persistent volume for the provider |  |
| `mountPath` | `String` | Path inside the container where the provider volume to be mounted |  |
| `readonly` | `Boolean` | If present allows you to mark a provider as read only | false |
| `migrationMode` | `String` | Indicates if a migration is configured. Values can be 'NONE', DRAIN', 'DELETE' or 'DUPLICATE' | 'NONE' |
