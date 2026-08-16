---
title: "About Correlated Scanning"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-correlated-scanning.html"
content_id: "It8fkoBFDDE2BXnfisV2Kg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:32.790826+00:00"
---

# About Correlated Scanning

Correlated Scanning is a scanning method which allows different matching technologies to
scan the same application target and correlate results together to perform more accurate
component and component version matching.

Black Duck currently supports correlation between single signature scans
and one/many package manager scan results only. Correlated scans will continue to each
get their own unique ID, but will share a UUID called a correlation ID.

## Prerequisites for correlated scanning

- **Detect:** Version 10.0.0 or newer
- **SCA Scan Service**: Ensure this service is available and properly
  configured.
- **Black Duck:** Version 2024.10.0 or newer
- **Match as a Service (MaaS):** Must be enabled on your
  account

**Note:** Match correlation is currently not supported for air-gapped KB
installations.

## Performing a correlated scan

Correlated scans are [executed with Detect](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/6e911f97f01f7d4dc622b28e044e00aa.topic) with the additional
flag:

```
--detect.blackduck.correlated.scanning.enabled=true
```

Once the command is performed, Detect will execute one signature scan and one package
manager scan. This will result in two code locations (one for each scan) mapped to
the desired project version. BOM results in this project version will be presented
in the same way as for non correlated scans (signature and package manager scans
mapped to the same project version).

Please note, snippet scanning or using the following option in Detect is currently
not supported for correlated scanning:

```
--detect.blackduck.signature.scanner.snippet.matching=SNIPPET_MATCHING
```

Warning: The correlated scan flag is only supported for single Signature and
one/many Package Manager scan results only. Using it with other scan types is not
recommended.
