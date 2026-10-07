---
title: "Script"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/script.html"
content_id: "ZvmabLzKGT4yZx5ngTdy7w"
version: "12.0.0"
section: "Getting started with Detect"
scraped_at: "2026-10-04T23:33:18.919855+00:00"
content_hash: "1ee38c0a6d6f21ba7ea2ca8ca4c77241f254d4a88aaa3003ff58e0c19940f8cd"
---

# Script

The primary function of the Detect script is to download and execute the Detect JAR file, which enables the scan capability.

Users download and run the latest version of Detect by providing the following commands, and adding properties to refine the behaviour.

Windows:

```
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect.ps1?$(Get-Random) | iex; detect"
```

Linux/MacOs:

```
bash <(curl -s https://detect.blackduck.com/detect.sh)
```

Note: Running the unversioned `detect.sh/ps1` script will use the latest version of the Detect .jar file, whereas running a versioned script such as `detect12.sh/ps1` will use the latest version of the Detect .jar file within that specific major version.
