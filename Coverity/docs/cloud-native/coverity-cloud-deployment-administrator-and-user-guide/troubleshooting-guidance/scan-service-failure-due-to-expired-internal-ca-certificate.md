---
title: "Scan service failure due to expired internal CA certificate"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-service-failure-due-to-expired-internal-ca-certificate.html"
content_id: "5FrE7x2i_KYycuict6FwmA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:37.452908+00:00"
---

# Scan service failure due to expired internal CA certificate

If you encounter the following CA certificate error:

```
Scan service Failure Due to Expired Internal CA Certificate
```

you can use the following procedure to run the `cert-gen` job manually,
generate new certificates, and resolve the expired CA certificate problem:

1. Extract all hooks from the
   release:

   ```
   helm get hooks <releaseName> -n <namespace> > hooks.yaml
   ```
2. Extract the `cert-gen` job
   block:

   ```
   awk '
   /^apiVersion: batch\/v1/ {capture=1}
   /^---/ && capture {exit}
   capture {print}
   ' hooks.yaml > cert-gen-job.yaml
   ```
3. Delete the existing
   job:

   ```
   kubectl delete job <releaseName>-cert-gen -n <namespace> --ignore-not-found
   ```
4. Delete the existing x509 secrets.
5. Apply the extracted
   job:

   ```
   kubectl apply -n <namespace> -f cert-gen-job.yaml
   ```
6. Verify the new
   pod:

   ```
   kubectl get pods -n <namespace> | grep cert-gen
   ```
7. View the
   logs:

   ```
   kubectl logs -n <namespace> job/<releaseName>-cert-gen -f
   ```
