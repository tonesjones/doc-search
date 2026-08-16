---
title: "Viewing and managing Detect scan results"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/viewing-and-managing-detect-scan-results.html"
content_id: "rClJVcucnm2Y9KFmxVkTcg"
version: "11.5.1"
section: "Viewing and managing Detect scan results"
scraped_at: "2026-08-08T23:45:48.919577+00:00"
---

# Viewing and managing Detect scan results

## Online mode

To view and manage your Black Duck® Detect scan results after running Detect online, do the following.

- In the Detect output look for "Detect Result" and copy the Black Duck SCA Project BOM URL as shown in the following example:

```
2020-06-11 06:35:39 INFO [main] ---======== Detect Result ========
2020-06-11 06:35:39 INFO [main] --- Black Duck SCA Project BOM: https://my-hub-docker/api/projects/d8f798f1-1901-4902-aec7-f2e1cf2e4958/versions/6a8938e9-3615-40dd-8386-3bcb4ba52bec/components
```

- Open the Black Duck SCA Project BOM URL in a browser to view the scan results in Black Duck SCA.
- To find your scan in Black Duck SCA, go to your Black Duck SCA instance and click Scans to see a list of scans on the Scans page.

For help with viewing and analyzing your scan results go to the Black Duck SCA Help page navigation menu at https://<Your hub host>/doc/Welcome.htm

## Offline mode

To view and manage your Detect scan results after running Detect offline (with property *blackduck.offline.mode* set to *true*), do the following.

- In the Detect output (near the beginning), look for the value of "Run directory". The output files will be written into subdirectories of the run directory. For example:

```
2022-03-07 15:46:29 EST INFO  [main] --- Run directory: /Users/billings/blackduck/runs/2022-03-07-20-46-29-611
```

Upload each of the output files (.bdio and .bdmu files, found in subdirectories of the run directory) into Black Duck SCA using the Black Duck SCA Scans page.
