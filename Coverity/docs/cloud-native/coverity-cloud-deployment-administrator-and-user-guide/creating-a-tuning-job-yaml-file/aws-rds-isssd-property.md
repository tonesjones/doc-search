---
title: "AWS RDS IsSSD property"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-rds-isssd-property.html"
content_id: "u5pexhcS0pWPvatOTL23HQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:21.938056+00:00"
---

# AWS RDS IsSSD property

Determine the disk type and set `IsSSD` as follows:

1. Issue the following command to fetch the storage type:

   ```
   aws rds describe-db-instances --db-instance-identifier <YOUR_AWS_RDS_INSTANCE_NAME>
    --region <YOUR_AWS_RDS_REGION> --query 'DBInstances[*].StorageType' | jq -Mr '.[0]' gp2
   ```

   See the following AWS links for further information:

   - <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html>
   - <https://docs.aws.amazon.com/cli/latest/reference/rds/describe-valid-db-instance-modifications.html>
   - <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html>

   For Amazon RDS storage type information, see:

   - General Purpose SSD (gp2, gp3) – See [General Purpose SSD
     storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#Concepts.Storage.GeneralSSD).
   - Provisioned IOPS SSD (io1) – See [Provisioned IOPS SSD
     storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS).
   - Magnetic disk (standard) – See [Magnetic storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#CHAP_Storage.Magnetic).
2. In the tuning yaml file, set the `isSSD` value based on the
   storage type:

   - If the storage is gp2, gp3, or io1, set `isSSD` to
     `true`.
   - If the storage is standard, set `isSSD` to
     `false`.
