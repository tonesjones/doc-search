---
title: "Verifying the Coverity cloud deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/verifying-the-coverity-cloud-deployment.html"
content_id: "rlpTe~yLZ9DbDEUFHX_GFg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:42.951506+00:00"
---

# Verifying the Coverity cloud deployment

Verify that Coverity was properly deployed in the cloud and that it is running.

1. In a web browser, enter the Coverity Connect URL. Ensure that you can log in, and
   ensure that the Connect UI is operable.
2. At a command prompt, verify that the Helm chart release installed successfully. In
   the following example, the `cnc` release has a status of
   `deployed` and is running version
   `2023.9`:

   ```
   $ helm list -a -n $NS
   NAME  NAMESPACE  REVISION  UPDATED                               STATUS    CHART      APP VERSION
   cnc   cnc        1         2023-09-30 11:51:42.281969 -0400 EDT  deployed  cnc-x.x.x  2023.9
   ```
3. Verify that all pods are present and have a status of either
   `Running` or `Completed`. For example:

   If only Coverity Connect (not Scan Service) is installed in the Kubernetes
   cluster, you should see at least the following pods:

   ```
   $ kubectl get pods -n $NS
    
   NAMESPACE  NAME                      READY  STATUS      RESTARTS  AGE
   cnc        cim-574dff5ff8-hd72k      2/2    Running     0         6d1h
   cnc        cim-database-setup-zpjfj  0/1    Completed   0         6d1h
   cnc        cim-update-license-7wx9w  0/1    Completed   0         6d1h
   ```

   If Coverity Scan Service is installed in the Kubernetes cluster, you should see
   at least the following pods:

   ```
   $ kubectl get pods -n $NS  
    
   NAME                                       READY   STATUS      RESTARTS   AGE
   cloudsql-5f77b8c57d-mzvdx                  1/1     Running     0          26h
   cnc-cache-service-589b69dcc4-7pmd2         1/1     Running     0          24h
   cnc-cert-gen-n96pc                         0/1     Completed   0          24h
   cnc-cim-554d6dfd68-hnv2z                   2/2     Running     0          24h
   cnc-cim-554d6dfd68-kd2lx                   2/2     Running     0          24h
   cnc-cleanup-job-28636620-pwj5h             0/1     Completed   0          113s
   cnc-cs-7cdfc9dc8d-g99r4                    2/2     Running     0          24h
   cnc-scan-service-548cf675c4-mzl8d          1/1     Running     0          24h
   cnc-scan-service-migration-spnt4           0/1     Completed   0          24h
   cnc-storage-service-5cd454585d-fz9rc       1/1     Running     0          24h
   cnc-storage-service-migration-4k9gr        0/1     Completed   0          24h
   ```
4. Inspect the pod logs for errors using the following command:

   ```
   kubectl logs -f -n cnc pod-name
   ```
