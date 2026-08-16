---
title: "Create a Google Cloud SQL database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-google-cloud-sql-database.html"
content_id: "aDfRMaQz40pd0_OUJHrT8Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:27.876885+00:00"
---

# Create a Google Cloud SQL database

If you are using Google cloud resources for a database, create a Google Cloud SQL
database. Refer to:

- Create PostgreSQL databases
- <https://cloud.google.com/sdk/gcloud/reference/sql/instances/create>
- <https://cloud.google.com/sql/docs/postgres/create-manage-databases#gcloud>

For example, if you use the `gcloud sql instances create` command:

```
gcloud sql instances create "${CLOUDSQL_NAME}" \
    --database-version=POSTGRES_14 \
    --region=${REGION} \
    --project=${PROJECT_ID} \
    --root-password="${PG_PASSWORD}" \
    --availability-type="${TYPE}" \
    --cpu="{NUM_CPU}" \
    --memory="{MEMORY}"
```

Where NUM_CPU is an integer that specifies the number of CPUs and MEMORY is the memory
size in MiB.
