---
title: "Running the Detect script"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/running-the-detect-script.html"
content_id: "zHUuoQm6zLdtiTLSX0xZHg"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:30.071847+00:00"
---

# Running the Detect script

The primary function of the Detect scripts is to download and execute the Detect .jar file.
Several aspects of script functionality can be configured, including:

- The Detect version to download/run; by default, the latest version.
- The download location.
- Where to find Java.

Information on how to configure the scripts is in Shell script configuration.

## Running the script on Linux or Mac

On Linux or Mac, execute the Detect script (detect11.sh, which is a Bash script) from Bash.

To download and run the latest version of Detect in a single command:

```
bash <(curl -s -L https://detect.blackduck.com/detect.sh)
```

Append any command line arguments to the end, separated by spaces. For example:

```
bash <(curl -s -L https://detect.blackduck.com/detect.sh) --blackduck.url=https://blackduck.mydomain.com --blackduck.api.token=myaccesstoken
```

See Quoting and escaping shell script arguments for details about quoting and escaping arguments.

### To run a specific version of Detect:

```
export DETECT_LATEST_RELEASE_VERSION={Detect version}
bash <(curl -s -L https://detect.blackduck.com/detect11.sh)
```

For example, to run Detect version 9.10.0:

```
export DETECT_LATEST_RELEASE_VERSION=9.10.0
bash <(curl -s -L https://detect.blackduck.com/detect9.sh)
```

## Running the script on Windows

On Windows, you can execute the Detect script (detect11.ps1, which is a PowerShell script),from [Command Prompt](https://en.wikipedia.org/wiki/Cmd.exe) or from inside a PowerShell session.

### Running from Windows Command Prompt

To download and run the latest version of Detect in a single command from Command Prompt:

```
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect.ps1?$(Get-Random) | iex; detect"
```

Append any command line arguments to the end, separated by spaces. For example:

```
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect.ps1?$(Get-Random) | iex; detect" --blackduck.url=https://blackduck.mydomain.com --blackduck.api.token=myaccesstoken
```

See Quoting and escaping shell script arguments for details about quoting and escaping arguments.

#### To run a specific version of Detect from Command Prompt:

```
set DETECT_LATEST_RELEASE_VERSION={Detect version}
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect"
```

For example, to run Detect version 11.3.0:

```
set DETECT_LATEST_RELEASE_VERSION=11.3.0
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect"
```

### Running from Windows Powershell

To download and run the latest version of Detect in a single command from PowerShell:

```
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect
```

*Note that when running the above command, the PowerShell session is not exited. See here for more information on the difference between the two commands.*

Append any command line arguments to the end, separated by spaces.

See Quoting and escaping shell script arguments for details about quoting and escaping arguments.

#### To run a specific version of Detect from Powershell:

```
$Env:DETECT_LATEST_RELEASE_VERSION = "{Detect version}"
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect
```

Or:

```
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; $Env:DETECT_LATEST_RELEASE_VERSION = "{Detect version}"; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect
```

For example, to run Detect version 10.0.0:

```
$Env:DETECT_LATEST_RELEASE_VERSION = "10.0.0"
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect10.ps1?$(Get-Random) | iex; detect
```

Or:

```
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; $Env:DETECT_LATEST_RELEASE_VERSION="10.0.0"; irm https://detect.blackduck.com/detect10.ps1?$(Get-Random) | iex; detect
```
