---
title: "GCP Cloud SQL properties for tuning-write"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-cloud-sql-properties-for-tuning-write.html"
content_id: "wErP9DqvHRCjWNWhzeXhtQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:20.005145+00:00"
---

# GCP Cloud SQL properties for tuning-write

## POSTGRES-DISTRO

If the PostgreSQL database is on GCP Cloud SQL and if you are performing a
tuning-write, in the tuning yaml file, set `<POSTGRES-DISTRO>` to
`cloudsql`.

## Authentication

Set the following environment variables:

1. Provide a service account using the environment variable
   GOOGLE_APPLICATION_CREDENTIALS.

   ```
   - name: GOOGLE_APPLICATION_CREDENTIALS
     value: /etc/gcp/key.json
   ```
2. Provide a project identity using the environment variable
   GOOGLE_CLOUD_PROJECT.

   ```
   - name: GOOGLE_CLOUD_PROJECT
    value: "<ADD-YOUR-PROJECT-NAME-HERE>"
   ```
3. Create a Cloud SQL service account (SA) secret:

   ```
   kubectl create secret generic cloudsql-service-account 
     --from-file=key.json=<FULL_PATH_OF_YOUR_SA_FILE>
   ```
4. Add the following file volume mount to the Kubernetes tuning job yaml file,
   under `spec:template:volumes:`.

   ```
   - name: gcp-cloudsql-credentials
     mountPath: /etc/gcp
   - name: gcp-cloudsql-credentials
      secret:
        defaultMode: 420
        secretName: cloudsql-service-account
   ```

## Authorization

Provide the following required permissions for Cloud SQL to proceed with the tuning
write process.

Note: This authorization is not required with
tuning-suggest.

| Action | Required Permission |
| --- | --- |
| instances.get Get the database instance and update the resource. | cloudsql.instances.get |
| instances.update | cloudsql.instances.update |

Note: According to [https://cloud.google.com/sql/docs/postgres/flags#troubleshooting-flags](https://cloud.google.com/sql/docs/postgres/flags#troubleshooting-flags,),
if you enable or run tuning on a Cloud SQL database instance, the database will
restart automatically.

Note: When you set, remove, or modify a flag for a database
instance, the database might be restarted. The flag value will persist for the
database instance until you remove it. If the database instance is the source of a
replica, and if the instance is restarted, the replica is also restarted to align
with the current configuration of the instance.
