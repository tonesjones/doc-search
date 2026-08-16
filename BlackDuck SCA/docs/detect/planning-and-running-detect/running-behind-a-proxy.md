---
title: "Running behind a proxy"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/running-behind-a-proxy.html"
content_id: "VejYElKO~RbeK1p7FEBU7A"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:37.773190+00:00"
---

# Running behind a proxy

When running behind a proxy:

1. The one-liner cannot be used to download the scripts, they are not proxy aware. The scripts must already be downloaded.
2. The script (detect11.sh or detect11.ps1) requires proxy details to do a version
   check on, and/or download the Detect .jar file.
3. Detect; the code in the .jar file, requires proxy details to download inspectors and
   connect to Black Duck SCA.

## Providing proxy details to Detect

Detect looks for proxy details in the properties whose names start with `blackduck.proxy`,
including:

- `blackduck.proxy.host` (proxy hostname)
- `blackduck.proxy.port` (proxy port number)
- `blackduck.proxy.username` (proxy username)
- `blackduck.proxy.password` (proxy password)

When setting the blackduck.proxy.host (proxy hostname) property, the schema/protocol is not accepted.

For example:

```
Correct: `--blackduck.proxy.host=<Proxy_IP/URL>`   
Incorrect: `--blackduck.proxy.host=<https‎ ://(IP/Server_URL)>`
```

Refer to properties for more information.

## Providing proxy details to detect11.sh

The curl commands executed by detect11.sh to do a version check on, and/or download the Detect
.jar file, require additional command line options when run behind a proxy. For more information
on curl options, refer to the [curl documentation](https://curl.haxx.se/docs/manpage.html).

To provide additional curl command line options for detect11.sh to use
when it executes curl, set the environment variable DETECT_CURL_OPTS before running
detect11.sh. For example:

```
export DETECT_CURL_OPTS=--proxy http://myproxy:3128
./[bash_script_name]
```

When using detect11.sh to execute Detect you must set proxy properties
for Detect as previously described.

## Providing proxy details to detect11.ps1

detect11.ps1 derives proxy details from environment variables
whose names match the Detect proxy property names.
Configuring detect11.ps1 for your proxy involves
setting those environment variables before running detect11.ps1.
Note that typically, the PowerShell script is run from a Command window, using "powershell script.ps1" so these should be run in that Command window.
For example:

```
${r"set BLACKDUCK_PROXY_HOST"}=$ProxyHost
${r"set BLACKDUCK_PROXY_PORT"}=$ProxyPort
${r"set BLACKDUCK_PROXY_PASSWORD"}=$ProxyUsername
${r"set BLACKDUCK_PROXY_USERNAME"}=$ProxyPassword
powershell "Import-Module FULL_PATH_TO_DOWNLOADED_SCRIPT/detect.ps1; detect"
```

For additional information on these properties, including alternate key formats, see the Shell script configuration reference.

When using detect11.ps1 to execute Detect, Detect also receives the proxy details
from these environment variables, so no additional configuration is required for Detect.
