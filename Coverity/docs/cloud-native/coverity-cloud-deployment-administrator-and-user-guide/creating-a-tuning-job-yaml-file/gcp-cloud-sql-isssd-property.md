---
title: "GCP Cloud SQL IsSSD property"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-cloud-sql-isssd-property.html"
content_id: "XYJJB7oiWjx1vG9c8sbA8Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:23.243607+00:00"
---

# GCP Cloud SQL IsSSD property

For GCP Cloud SQL, determine the disk type and set `IsSSD` as follows:

1. Issue the following command to fetch the storage type:

   ```
   gcloud sql instances describe <YOUR_GCP_CLOUDSQL_INSTANCE_NAME>
     | grep "dataDiskType" dataDiskType: PD_SSD
   ```

   See the following AWS links for further information:

   - <https://cloud.google.com/sql/docs/mysql/instance-settings>
   - <https://cloud.google.com/compute/docs/disks>

   The following table shows disk type and machine type support for **zonal**
   persistent disks.

   | Disk type | Supported machine types | Set IsSSD |
   | --- | --- | --- |
   | pd-standard | All machine types | `false` |
   | pd-balanced | All machine types | `true` |
   | pd-ssd | All machine types | `true` |
   | pd-extreme | n2-standard with 64 or more vCPUs, n2-highmem-64, n2-highmem-80, m1-megamem-96, m2-ultramem-208, m2-ultramem-416 | `true` |

   The following table shows disk type and machine type support for **regional**
   persistent disks:

   | Disk type | Supported machine types | Set IsSSD |
   | --- | --- | --- |
   | pd-standard | N1, N2, N2D, E2 | `false` |
   | pd-balanced | N1, N2, N2D, E2 | `true` |
   | pd-ssd | N1, N2, N2D, E2 | `true` |
2. In the tuning yaml file, set `IsSSD` as follows:
   - If the disk type is pd-ssd, pd-balanced, or pd-extreme, set
     `IsSSD` to `true`.
   - If the disk type is pd-standard, set `IsSSD` to
     `false`.
