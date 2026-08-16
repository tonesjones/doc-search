---
title: "Configuring multiple volumes"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-multiple-volumes.html"
content_id: "p_WWLzAr75sQANCER25D~g"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:07.661785+00:00"
---

# Configuring multiple volumes

The swarm deployment files contain a file named
`docker-compose.storage-overrides.yml`. This file is a template that
must be customized and included in the deployment in order to override the default
storage configuration to use more volumes.

This file has three sections: Environment, Storage Volumes and Service Volumes.

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

## Environment

The environment section is structured as follows:

```
services:
                storage:
                environment:
                # Provider 1 settings
                BLACKDUCK_STORAGE_PROVIDER_ENABLED_1: 'true'
                BLACKDUCK_STORAGE_PROVIDER_PREFERENCE_1: 10
                BLACKDUCK_STORAGE_PROVIDER_READONLY_1: 'false'
                BLACKDUCK_STORAGE_PROVIDER_MIGRATION_MODE_1: 'none'
                # Provider 2 settings
                BLACKDUCK_STORAGE_PROVIDER_ENABLED_2: 'false'
                BLACKDUCK_STORAGE_PROVIDER_PREFERENCE_2: 20
                BLACKDUCK_STORAGE_PROVIDER_READONLY_2: 'false'
                BLACKDUCK_STORAGE_PROVIDER_MIGRATION_MODE_2: 'none'
                # Provider 3 settings
                BLACKDUCK_STORAGE_PROVIDER_ENABLED_3: 'false'
                BLACKDUCK_STORAGE_PROVIDER_PREFERENCE_3: 30
                BLACKDUCK_STORAGE_PROVIDER_READONLY_3: 'false'
                BLACKDUCK_STORAGE_PROVIDER_MIGRATION_MODE_3: 'none'
                ...
```

These settings enable or disable each of the three storage providers. The
configuration in the file is shipped with the same configuration as the default.
(provider 1 enabled, 2 and 3 disabled).

To configure a provider, change the settings for the given provider. The settings
are:

| Setting | Details |
| --- | --- |
| `BLACKDUCK_STORAGE_PROVIDER_ENABLED_(N)` | **Default**: for provider 1, `true`, for others `false`  **Valid values**: `true` or `false`  **Notes**: This enables or disables a provider. AT LEAST ONE PROVIDER MUST BE ENABLED OR THE SYSTEM CANNOT START. |
| `BLACKDUCK_STORAGE_PROVIDER_PREFERENCE_(N)` | **Default**: provider number times 10  **Valid values**: `0-999`  **Notes**: This value indicates the preference between the providers. The provider with the highest priority (lowest preference number) will be used to store new content. The other providers in the configuration will continue to serve their content and all other functions - but will not have new content added to them.  NOTE: All active providers must have UNIQUE preference numbers. Two providers cannot share the same value. |
| `BLACKDUCK_STORAGE_PROVIDER_READONLY_(N)` | **Default**: `false`  **Valid values**: `true` or `false`  **Notes**: This indicates a provider is read-only. The highest priority (lowest preference number) provider cannot be read-only or the system cannot function.  A read only provider will not have the storage volume altered by addition of data or removal of data, however metadata in the database will be manipulated to record object deletions and other changes. |
| `BLACKDUCK_STORAGE_PROVIDER_MIGRATION_MODE_(N)` | **Default**: `none`  **Valid values**: `none`, `drain`, `delete`, `duplicate`  **Notes**: This configures the migration mode for the provider, Details of what this mode is and how to use it are provided in the migration section of this document. |

## Storage volumes

This section assigns named storage volumes with specific mount points on the system
where the software expects them to be. The volume for provider one is named
"storage-volume" and is defined elsewhere. It will always exist, even if storage
provider 1 is not enabled. The storage volume section of the overrides file is as
follows:

```
services:
                storage:
                environment:
                ...
                volumes:
                ## NOTE: File provider 1's volume mount point is always
                ## present since it is defined as the upstream default
                ## It will only be used if the file provider 1 is enabled
                ##
                ## File provider 2's volume mount point
                #- storage-volume2:/opt/blackduck/hub/uploads2
                ##
                ## File provider 3's volume mount point
                #- storage-volume3:/opt/blackduck/hub/uploads3
                ...
```

For the other providers, you should merely uncomment the sections out for each
provider you have enabled. For example if provider two (2) is enabled, this section
of the file should look like:

```
...
                ##
                ## File provider 2's volume mount point
                - storage-volume2:/opt/blackduck/hub/uploads2
                ##
                ...
```

## Service volumes

This section defines the volumes by name and their configuration. The configuration
provided uses Docker Swarm's default volume driver. Similar to the Service Volume
section, you only need to uncomment the appropriate pieces based on which providers
are enabled. The service volume section of the file looks like this:

```
services:
                storage:
                environment:
                ...
                volumes:
                ...
                volumes: {
                ## NOTE: File provider 1's storage volume is always present
                ## since it is defined as the upstream default. It will
                ## only be used if the file provider 1 is enabled
                ##
                ## File provider 2's storage volume
                #storage-volume2: null,
                ##
                ## File provider 3's storage volume
                #storage-volume3: null,
                }
```

Note: Configurations other than the default storage driver are possible here. A
storage volume named "storage-volume2" could be created backed by NFS, a NAS or a
SAN. These configurations would need to be worked out based on standard docker swarm
params in conjunction with the vendors settings or extensions as appropriate to the
customer's environment, and so cannot be documented here.
