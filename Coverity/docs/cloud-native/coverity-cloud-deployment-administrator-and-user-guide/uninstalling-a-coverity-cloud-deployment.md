---
title: "Uninstalling a Coverity cloud deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/uninstalling-a-coverity-cloud-deployment.html"
content_id: "DMlJB63y~zn0pmpQjpmFLA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:36.130874+00:00"
---

# Uninstalling a Coverity cloud deployment

To uninstall a Coverity cloud deployment:

1. Issue the following Helm command to remove the Helm chart:

   ```
   helm uninstall ${RELEASE} --namespace "${NS}"
   ```
2. Remove the database as follows:

   Warning: This will delete your Coverity
   Connect data. Please ensure that your database is backed up before
   performing this operation. Only perform this operation if you are sure it is
   necessary.

   1. Enter the `psql` command to access the database command
      prompt.
   2. At the database command prompt, enter the following command to drop the
      database:

      Note: In the following example, enter the database
      name in the dbname variable.

      Note: Dropping the database removes the database
      catalog entries and deletes the data directory.

      ```
      postgres> drop database dbname;
      ```
