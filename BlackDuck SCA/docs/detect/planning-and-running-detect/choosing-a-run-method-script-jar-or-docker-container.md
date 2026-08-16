---
title: "Choosing a run method (script, .jar, or Docker container)"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/choosing-a-run-method-script-.jar-or-docker-container-.html"
content_id: "ZCv3Bfb7td9029~dp653mA"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:29.451222+00:00"
---

# Choosing a run method (script, .jar, or Docker container)

There are three ways to run Detect:

1. Download and run a Detect script.
2. Download and run a Detect .jar file.
3. Run Detect from within a Docker container.

# Scripts

Running one of the Detect scripts provides the convenience of an auto-update feature, keeping you at the latest version with the associated improvements.Auto-update provides the following default behaviour:

Downloading and running the latest unversioned `detect.sh/ps1` script will use the latest version of the Detect .jar file; downloading it for you if necessary.

Running a versioned `detect.sh/ps1` script such as `detect11.sh/ps1` will use the latest version of the Detect .jar file within that specific major version; downloading it for you if necessary.

To override the auto-update functionality by specifying an exact Detect version, see: To run a specific version of Detect.

If you are running Detect with Black Duck SCA you can also configure the version of Detect that should be used. See [Hosting location for Black Duck Detect](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/DetectLocation.html).

Tip: When you run Detect via one of the provided scripts, you automatically pick up fixes and new features as they are released.

| Detect version | Script Type | Script Name | Notes |
| --- | --- | --- | --- |
| Latest | Bash | detect.sh | Runs latest Detect |
| Latest | PowerShell | detect.ps1 | Runs latest Detect |
| 11 | Bash | detect11.sh | Runs latest Detect 11 |
| 11 | PowerShell | detect11.ps1 | Runs latest Detect 11 |
| 10 | Bash | detect10.sh | Runs latest Detect 10 |
| 10 | PowerShell | detect10.ps1 | Runs latest Detect 10 |
| 9 | Bash | detect9.sh | Runs latest Detect 9 |
| 9 | PowerShell | detect9.ps1 | Runs latest Detect 9 |

Note: References to Detect scripts within this documentation assume you are running the current release.

# JAR file

The primary reason to run the Detect .jar directly is that this method provides
direct control over the exact Detect version. Detect does not automatically update in this scenario unless configured in Black Duck SCA to do so. See [Hosting location for Black Duck Detect](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/DetectLocation.html).

# Docker container

The primary reasons to run Detect from within a Docker container include general Docker container benefits, such as having a repeatable standardized run environment, ease of deployment and isolation from other systems.
