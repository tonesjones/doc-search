---
title: "Running the Detect script"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/running-the-detect-script.html"
content_id: "zHUuoQm6zLdtiTLSX0xZHg"
version: "12.0.0"
section: "Planning and running Detect"
scraped_at: "2026-09-07T21:15:30.169967+00:00"
---

# Running the Detect script

The primary function of the Detect scripts is to download and execute the Detect .jar file.
Several aspects of script functionality can be configured, including:

- The Detect version to download/run; by default, the latest version.
- The download location.
- Where to find Java.

Information on how to configure the scripts is in Shell script configuration.

## Important Information

Black Duck recommends using version-specific Detect scripts, such as `detect11.sh`, `detect11.ps1`, `detect12.sh`, or `detect12.ps1`, in production environments.

The generic `detect.sh` and `detect.ps1` scripts download and run the latest available Detect release by default. As new releases become available, these scripts can automatically upgrade your environment to a newer Detect version, including a new major version.

Major-version upgrades can introduce breaking changes. For example, support for specific Java versions may be added or removed, deprecated functionality may be eliminated, and existing behavior may change. To ensure predictable and repeatable execution, use a version-specific script and explicitly control the Detect version that is run.

## Running the script on Linux or Mac

Important: The `detect.sh` script downloads and runs the latest available Detect release. As new versions become available, this command may begin running a newer major version of Detect that includes breaking changes. For production environments, Black Duck recommends using a version-specific script such as `detect11.sh` or `detect12.sh`.

On Linux or Mac, execute the Detect script (detect12.sh, which is a Bash script) from Bash.

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
bash <(curl -s -L https://detect.blackduck.com/detect12.sh)
```

For example, to run Detect version 11.5.1:

```
export DETECT_LATEST_RELEASE_VERSION=11.5.1
bash <(curl -s -L https://detect.blackduck.com/detect11.sh)
```

## Running the script on Windows

On Windows, you can execute the Detect script (detect12.ps1, which is a PowerShell script),from [Command Prompt](https://en.wikipedia.org/wiki/Cmd.exe) or from inside a PowerShell session.

### Running from Windows Command Prompt

Important: The `detect.ps1` script downloads and runs the latest available Detect release. As new versions become available, this command may begin running a newer major version of Detect that includes breaking changes. For production environments, Black Duck recommends using a version-specific script and explicitly controlling the Detect version that is executed.

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

Using a version-specific script is the recommended approach for production deployments because it helps prevent unintended upgrades to newer major versions of Detect.

```
set DETECT_LATEST_RELEASE_VERSION={Detect version}
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect12.ps1?$(Get-Random) | iex; detect"
```

For example, to run Detect version 12.0.0:

```
set DETECT_LATEST_RELEASE_VERSION=12.0.0
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect12.ps1?$(Get-Random) | iex; detect"
```

### Running from Windows Powershell

To download and run the latest version of Detect in a single command from PowerShell:

```
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect12.ps1?$(Get-Random) | iex; detect
```

Note: When running the above command, the PowerShell session is not exited. See here for more information on the difference between the two commands.

Append any command line arguments to the end, separated by spaces.

See Quoting and escaping shell script arguments for details about quoting and escaping arguments.

#### To run a specific version of Detect from Powershell:

Using a version-specific script is the recommended approach for production deployments because it helps prevent unintended upgrades to newer major versions of Detect.

```
$Env:DETECT_LATEST_RELEASE_VERSION = "{Detect version}"
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect
```

Or:

```
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; $Env:DETECT_LATEST_RELEASE_VERSION = "{Detect version}"; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect
```

For example, to run Detect version 11.0.0:

```
$Env:DETECT_LATEST_RELEASE_VERSION = "11.0.0"
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect
```

Or:

```
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; $Env:DETECT_LATEST_RELEASE_VERSION="11.0.0"; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect
```
