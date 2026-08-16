---
title: "Create and mount a /data persistent volume"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-and-mount-a/data-persistent-volume.html"
content_id: "Y1El77Awk5oZpZUOQ4w7QQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:08.670543+00:00"
---

# Create and mount a /data persistent volume

The Coverity Connect (CIM) tools run in the `cim-tools` pod. To store
tools data between sessions, you need to create a `/data` persistent
volume and mount that volume to the `cim-tools` pod.

Create and mount a `/data` persistent volume to the
`cim-tools` pod as follows:

1. Create a yaml file that declares the persistent volume for `cim`
   tools data. The following example, in a file named `pv.yaml`,
   declares a persistent volume named `cim-tools-pv` with the
   `/data` mount path. See also cim.cimtools.volume Helm keys: create and mount a /data volume.

   ```
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: cim-tools-pv
   spec:
     storageClassName: manual
     capacity:
       storage: 1Gi
     accessMode: ReadWriteOnce
     mountPath: "/data"
   ```
2. Set the `cim.cimtools.volume` Helm keys in the
   `cnc` chart to define the volume size and enable the volume.
   The following example enables a volume that has a default size of
   `1Gi:`

   ```
   cim:
     cimtools:
       volume:
         enabled: true
         storage: 1Gi
   ```

   For all `cim.cimtools.volume` Helm keys, see cim.cimtools.volume Helm keys: create and mount a /data volume.

   Note: The following Helm key must be set to
   `true` for the `/data` volume to be mounted to
   the `cim-tools`
   pod:

   ```
   cim.cimtools.volume.enabled: true
   ```
3. To create and mount this volume, you can use the following kubectl apply command,
   applying the yaml file, in this example named `pv.yaml`:

   ```
   kubectl apply -f pv.yaml
   ```
