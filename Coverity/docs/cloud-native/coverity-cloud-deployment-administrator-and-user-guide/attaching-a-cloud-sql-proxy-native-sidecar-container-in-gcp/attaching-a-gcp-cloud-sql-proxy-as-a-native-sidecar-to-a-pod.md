---
title: "Attaching a GCP Cloud SQL proxy as a native sidecar to a pod"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/attaching-a-gcp-cloud-sql-proxy-as-a-native-sidecar-to-a-pod.html"
content_id: "_Oi15z6h_JWd1hI5J3guqg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:48.670034+00:00"
---

# Attaching a GCP Cloud SQL proxy as a native sidecar to a pod

Note: This procedure assumes that you have already created the GCP
cloud infrastructure in which to deploy Coverity.

In GCP, to attach a Cloud SQL proxy as a Native Sidecar to all of the pods that require a
database connection, you need to complete the host Helm key and sidecar Helm keys.

You can configure `postgres.sidecars` and
`postgres.jobSidecars` Helm keys in the following chart
locations:

- Global Helm keys: `global.postgres:`
- `cnc` chart: `postgres:` - Overrides
  `global.postgres` for Connect.
- `scan-services` subchart: `postgres:` - Overrides
  `global.postgres` for scan services.

Note: Sidecar keys are not available in either
`cim.postgres` or `scan-service.postgres`.

Given the following example:

```
global.postgres:
  database: "postgres"
  host: "localhost"
  password: "<password>"
  port: 5432
  sslmode: "disable"
  user: "coverity"
  existingSecret: ""
  sidecars:
    - name: cloud-sql-proxy
      image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.1.0-buster
      restartPolicy: Always   
      args:
        #- "--private-ip"
        - "--structured-logs"
        - "--port=5432"
        - "<gcp-project>:<region>:testgcp-zirw98"
        - "--max-sigterm-delay=2s"
        - "--credentials-file=/secrets/key.json"
      securityContext:
        runAsUser: 5000
      volumeMounts:
        - name: gcp-sa-secret
          mountPath: /secrets/
          readOnly: true
      resources:
        requests:
          memory: "500Mi"
          cpu: "500m"
  jobSidecars:
    - name: cloud-sql-proxy
      image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.1.0-buster
      restartPolicy: Always
      command: ["/bin/sh","-ec"]
      args: ["/cloud-sql-proxy --structured-logs 
            --port=5432 <gcp-project>:<region>:testgcp-zirw98 
            --credentials-file=/secrets/key.json 
            --max-sigterm-delay=100s "]
      securityContext:
        runAsUser: 5000
      volumeMounts:
        - name: gcp-sa-secret
          mountPath: /secrets/
          readOnly: true
      resources:
        requests:
          memory: "500Mi"
          cpu:    "500m"
```

1. Using the appropriate Helm keys, define the sidecars for containers that need to
   connect to a database. The example above defines
   `global.postgres.sidecars` and
   `global.postgres.jobSidecars`. Each sidecar is added as a
   native sidecar init container with `restartPolicy:Always`. Each
   native Cloud SQL proxy sidecar definition must contain a
   `restartPolicy:Always` Helm key as shown in the example.

   - For information on the global Helm keys in the example, refer to global.postgres Helm keys.
   - For Cloud SQL proxy container information, refer to <https://www.digitalocean.com/community/tutorials/cloud-sql-proxy-in-gke>.

   Note: No SQL proxy sidecars are attached to cleanup job, sync
   job, and analysis jobs.
2. Define the `global.postgres.host` Helm key as
   `"localhost"` to connect to the database through a SQL proxy
   sidecar.
3. After the templates have been modified, create a service account with permissions
   to access Cloud SQL databases:

   ```
   gcloud iam service-accounts create "${CNC_DB_SA}" \
     --project "${CNC_PROJECT_ID}" \
     --display-name "service account for ${CNC_PREFIX} environment"
   gcloud projects add-iam-policy-binding "${CNC_PROJECT_ID}" \
     --member "serviceAccount:${CNC_DB_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com" \
     --role "roles/cloudsql.client"
   ```
4. Create a key based off this service account. This key will be used to access your
   CloudSQL Postgres database:

   ```
   gcloud iam service-accounts keys create key.json \
     --iam-account "${CNC_DB_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com"
   ```
5. Create a Kubernetes secret to hold the key:

   ```
   kubectl create secret generic $GCP_SERVICE_ACCOUNT_SECRET_NAME \
     --namespace $COVERITY_NS \
     --from-file=key.json=<path/to/key.json>
   ```
6. In each sidecar definition, add an extra volume for the gcp-sa-secret that
   contains the key file for the service account that you created, in order to
   mount the secret volume in the sidecar container. Then add the sidecar
   definitions under the PostgreSQL heading. For example:

   ```
   global.postgres:
     sidecars:
       - name: cloud-sql-proxy
         volumeMounts:
           - name: gcp-sa-secret
             mountPath: /secrets/
             readOnly: true
     jobSidecars:
       - name: cloud-sql-proxy
         volumeMounts:
           - name: gcp-sa-secret
             mountPath: /secrets/
             readOnly: true
   ```
7. Override the `extraVolumes` Helm key with the GCP service account
   secret.

   ```
   extraVolumes:
     - name: gcp-sa-secret
       secret:
         secretName: gcp-sa-secret
   ```
8. Deploy the Coverity cloud in the GCP cluster.
