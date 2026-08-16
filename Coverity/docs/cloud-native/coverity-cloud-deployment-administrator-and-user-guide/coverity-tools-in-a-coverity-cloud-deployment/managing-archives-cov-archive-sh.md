---
title: "Managing archives: cov-archive.sh"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-archives-cov-archive.sh.html"
content_id: "mM32k_YlfPT0OahEPcNuYg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:10.646375+00:00"
---

# Managing archives: cov-archive.sh

The `cov-archive` tool enables you to import streams from an archive
file, export streams to an archive, or get information about an archive file. This
tool can be used to export and import between instances of Coverity Connect deployed
inside and outside the cloud.

When you execute the `cov-archive.sh` script, you use the same arguments
that are used with the `cov-archive` command. For information on the
archive functionality and options, see the section Coverity Connect
commands in the Coverity 2026.6.0 Command Reference.

The following sections outline how to prepare for and run the
`cov-archive.sh` script in a Coverity cloud deployment.

Note: For any script or command that will perform a write operation in
either a `cim-tools` pod or a `cnc-db-admin` pod, you must
write the output file to `/workdir`.

Note: If you encounter a Read Only File System error while executing
any of our scripts or binaries within a Connect pod, refer to Read-only file system error.

## Scale up and open a shell in the `cim-tools` pod

Coverity Connect (CIM) tools can be run using a persistent pod. The pod is scaled
down to 0 by default. You must scale the `cim-tools` pod to 1, then
open a shell in the `cim-tools` pod. For example:

1. Scale up the `cim-tools` pod to
   1:

   ```
   kubectl scale statefulsets ${RELEASE}-cim-tools -n $NS --replicas=1
   ```
2. Open a shell in the `cim-tools` pod to run the archive
   commands:

   ```
   kubectl exec -ti -n $NS statefulsets/${RELEASE}-cim-tools -- /coverity/shell-entrypoint.sh
   ```

## Export an archive from inside a pod

To export an archive from *inside* a pod, at the shell prompt within the pod,
run the `cov-archive.sh` script:

```
./cov-archive.sh export-streams --project <PROJECT NAME> --archive project.zip
```

The following example exports an archive to `/workdir`:

```
./cov-archive.sh export-streams --archive /workdir/my_archive.archive --project src2 --stream src2
```

## Download an archive from outside a pod

You can download an archive from *outside* a pod using the `kubectl
cp` command. For example, to download the `project.zip`
archive:

```
kubectl cp -n $NS ${RELEASE}-cim-tools-0:<PATH_TO_ARCHIVE_IN_POD> project.zip --added /data in cim-tools
```

## Import an archive

Before you can import and satisfy database locking restrictions, scale the Coverity
Connect `cim-webapp` pod to 0:

```
kubectl scale deployment/${RELEASE}-cim-webapp -n $NS --replicas=0
```

To import an archive named `project.zip` from *outside* the
pod:

```
kubectl cp -n $NS project.zip ${RELEASE}-cim-tools-0:<PATH_TO_ARCHIVE_IN_POD>
```

## Scale down the `cim-tools` pod

When finished running archive tool commands, scale the `cim-tools` pod
to 0:

```
kubectl scale statefulsets ${RELEASE}-cim-tools -n $NS --replicas=0
```
