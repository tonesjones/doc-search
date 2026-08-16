---
title: "Create a dbreadreplica-values.yaml file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-dbreadreplica-values.yaml-file.html"
content_id: "BMFmkarpzxzwfD9~p~UcWg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:11.413171+00:00"
---

# Create a dbreadreplica-values.yaml file

Edit or override the `pgpool` Helm keys Helm keys as needed in the cnc
Helm chart. You can optionally create a new yaml file, in this example named
`dbreadreplica-values.yaml`, in which you can provide new values as
needed to override default values. This section provides an example of how to create
this file.

1. Connect to the cluster:

   ```
   kubectl config use-context <clusterName>
   ```
2. Switch to your namespace.

   ```
   kubectl config set-context --current --namespace=<namespace>
   ```
3. List the Helm chart releases, then copy the release name for the 2026.6.0 release.

   ```
   helm list -n <namespace>
   ```
4. Download the `values.yaml` file for the Helm chart release (2026.6.0). This downloads the `cnc` chart
   `values.yaml` file:

   ```
   helm get values <releaseName>
   ```

   For example, to download the `cnc` chart which contains the
   `pgpool` Helm keys for DB replicas:

   ```
   helm get values cnc
   ```
5. Open the downloaded `values.yaml` file for the 2026.6.0 release.
6. Create a new `cnc-values.yaml` file.
7. Copy the complete contents of the `values.yaml` file and paste it
   into the new `cnc-values.yaml` file.
8. Create a new `dbreadreplica-values.yaml` file.
9. Continue with the next section, Configure the cim.pgpool Helm keys, to
   configure the Pgpool Helm keys.
