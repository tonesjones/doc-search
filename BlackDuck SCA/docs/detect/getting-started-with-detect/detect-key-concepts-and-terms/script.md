---
title: "Script"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/script.html"
content_id: "ZvmabLzKGT4yZx5ngTdy7w"
version: "11.5.1"
section: "Getting started with Detect"
scraped_at: "2026-08-08T23:44:12.018509+00:00"
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

Note: Running the unversioned `detect.sh/ps1` script will use the latest version of the Detect .jar file, whereas running a versioned script such as `detect11.sh/ps1` will use the latest version of the Detect .jar file within that specific major version.
