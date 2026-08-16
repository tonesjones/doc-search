---
title: "Downloading a scan log using the Connect API"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/downloading-a-scan-log-using-the-connect-api.html"
content_id: "u21UKrPhD6LcME0CNDy~fQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:39.475381+00:00"
---

# Downloading a scan log using the Connect API

You can download a scan log from Connect using the Connect API as follows:

Note: You must have administrator access to download logs.

1. Login to your Coverity Connect cloud instance as administrator.
2. Access the get scan jobs API in your browser. Look for the storage IDs:

   - `execLog` (runner execution logs)
   - `analyzedIdir` (Coverity Analysis output logs)

   For example, the request:

   ```
   https://<Connect_URL>/api/v2/scans/<scanId>/jobs
   ```

   will return the following sample response containing "state":"FAILED" and an execLog
   (shown in bold):

   ```
   [
      {
         "jobId":"ac316bc0-f482-45cb-b106-9648c9714771",
         "scanId":"abc0ca1b-c8d1-4dfe-8ed8-caa9960d96a8",
         "config":{
            "jobType":"COVERITY_ANALYSIS",
            "toolConfig":{
               "analysisConfig":{
                  "storageId":"16262657-6556-4c63-a104-5187eb4077a0",
                  "toolVersion":"2023.3"
               },
               "connectConfig":{
                  "endpoint":"https://cnc-azure-cim:8443",
                  "streamId":"asifbas"
               }
            }
         },
         "state":"FAILED",
         "errorInfo":{
            "osProcessInfo":{
               "commandArguments":[
                  "--machine-readable-output",
                  "json",
                  "analyze",
                  "--project-dir",
                  "/tmp/workdir750186213/project"
               ],
               "executable":"coverity",
               "exitCode":1
            },
            "errorMsg":"An internal error occurred at coverity analyze phase. : 
             open /tmp/workdir750186213/project/idir/output: no such file or directory"
         },
         "progress":20,
         "details":{
            "analysis":{
               "summary":{
                  "auditSeverity":0,
                  "highSeverity":0,
                  "lowSeverity":0,
                  "mediumSeverity":0
               },
               "outputStorage":{
                  "analyzedIdir":"",
                  "execLog":"2a10e76a-f5cb-4e26-8e88-8b36134008d4"
               }
            }
         },
         "lastUpdatedAt":"2024-8-21T17:19:35.797220Z",
         "createdAt":"2024-7-21T17:19:28.590926Z"
      }
   ]
   ```
3. Access the storage API and look for the URL link which you will use to download the
   execLog.

   For example, the request:

   ```
   https://<Connect_URL>//api/v2/storage/<execLog>/singlepart?method=get
   ```

   with the execLog filled in:

   ```
   https://<Connect_URL>//api/v2/storage/​2a10e76a-f5cb-4e26-8e88-8b36134008d4/​singlepart?method=get
   ```

   will return the URL for the specified execLog, as shown in bold here:

   ```
   {
      "url":"https://cncqastorage.blob.core.windows.net/cnc-qa-bucket/​2a10e76a-f5cb-4e26-8e88-8b36134008d4?se=​
        2026-8-21T17%3A31%3A33Z&sig=​QwOiikdjgNsU1lKHy8GMNhfpIZ185WtICQwGfAnP6gQ%3D&sp=​r&spr=https&sr=b&sv=2024-8-21",
      "expiration":"2026-8-21T17:31:33Z"
   }
   ```
4. Click on the URL link to download the execLog.

   Note: You can
   download the analysis-output logs, analyzedIdir, by using the storage-id rather than
   the execLog in the URL.
