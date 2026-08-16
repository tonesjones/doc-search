---
title: "Configuring your Black Duck instance"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-your-black-duck-instance.html"
content_id: "unSqzJpoWYR22mcwzJdMeA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:00.834417+00:00"
---

# Configuring your Black Duck instance

## Choosing an appropriate deployment size

Black Duck provides several [Black Duck
pre-configured](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) scans-per-hour yaml files to help with sizing
your deployment appropriately. These have been tested by our performance lab using
real-world configurations. However, they are not "one size fits all", therefore, if
you plan to run large amounts BDBA scans, snippet scans or reports, please reach out
to your CSM for assistance in determining a custom sizing tier.

As of 2024.4.x, GEN04 sizing files should be used.

Note: The 10sph.yaml files are not intended for production purposes and should not be
deployed for anything outside of local testing.

## Configuring persistent storage

Black Duck requires certain data to be persisted to disk.
Therefore, an appropriate `storageClass` should be utilized within
your install. If your cluster does not have a default `storageClass`,
or you wish to override it, update the following parameters:

```
# it will apply to all PVC's storage class but it can be override at container level
storageClass:
```

The `reclaimPolicy` of the
`storageClass` in use should be set to
`Retain` to ensure data persistence. AzureFile
(non-CSI variant) requires a custom storage class for RabbitMQ due
to it being treated as an SMB mount where file and directory
permissions are immutable once mounted into a pod.

## Configuring the database

If you choose to use an external postgres instance (default configuration), you will
need to configure the following parameters in values.yaml:

```
postgres.host: ""
postgres.adminUsername: ""
postgres.adminPassword: ""
postgres.userUsername: ""
postgres.userPassword: ""
```

If you choose to utilize the containerized PostgreSQL instance, set the following
parameter to false:

```
postgres.isExternal: true
```

Note: It is important that the specifications of the database deployment meet the
appriopriate size tier. Regardless of whatever database deployment method you
choose, ensure that you regularly perform backups and periodically verify the
integrity of those backups.
