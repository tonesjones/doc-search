---
title: "CIM properties secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cim-properties-secret.html"
content_id: "YHUb2LlufeddFHaRcLJf4A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:24.530508+00:00"
---

# CIM properties secret

Create a CIM properties secret file, create a secret, and enter the secret name in
<CIM-PROPERTIES> in the tuning job yaml file as follows:

1. Create a `cim.properties` file with the following secret
   contents:

   ```
   maindb.name=<YOUR_MAIN_DB_NAME>
   maindb.password=<YOUR_MAIN_DB_PASSWORD>
   maindb.url=<YOUR_MAIN_DB_URL>
   maindb.user=<YOUR_MAIN_DB_USER>
   password=<YOUR_MAIN_DB_PASSWORD>
   url=<YOUR_DB_URL>
   user=<YOUR_DB_USER>
   commitPort=9090
   ```
2. Create the cim.properties
   secret:

   ```
   kubectl create secret generic admindb-tools-config 
       --from-file=cim.properties=<FULL_PATH_OF_YOUR_CIM_PROPERTIES_FILE>
   ```
3. Replace <CIM-PROPERTIES> in the tuning job yaml file with the cim properties
   secret name. For example, `admindb-tools-config`.
