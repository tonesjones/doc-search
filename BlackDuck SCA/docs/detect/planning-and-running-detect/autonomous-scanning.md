---
title: "Autonomous Scanning"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/autonomous-scanning.html"
content_id: "Brvnd6uFkt8IrslOsklqtw"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:40.456420+00:00"
---

# Autonomous Scanning

Autonomous Scanning allows for Black Duck® Detect to run scans with a minimum amount of user provided
parameters. Autonomous scans store configuration and related parameters in a .json file that
will be reused when working with the same code. This reduces the user input required
to effectively analyze source code and binary files, along with simplifying repeat analysis
and delta reporting.

Autonomous Scanning will accept a user provided local file path for scanning. The content may be a single executable, a directory of
source files, or a combination thereof.

The scan settings file name is a hash generated from the scanned folder(s). An initial
scan with user provided parameters will populate this file and subsequent scans of the
same folder structure will update it. After the initial scan, unless you wish to
override previous scan parameters, Detect can be run in Autonomous mode by simply providing the
`--detect.autonomous.scan.enabled=true` parameter.

Detect properties, environment variables, or Spring
configurations enabled at run time will take precedence over values stored in the scan
settings file.

Warning: The scan settings json file is generated and updated automatically and should not be manually modified.

Detect will determine appropriate tools and/or Detectors to run
given the content of the target path or run folder if no path is provided. The
determining factor for scan types include the file type, and whether the pre-requisites
of the appropriate Detector types are met. If prerequisites for package manager or
binary scanning are not met, but files are available in the target folder, a signature
scan will be run. Detect will follow the Detector Cascade processing order.

## Initial Scan Workflow

1. Run Detect in Autonomous mode by providing the
   `--detect.autonomous.scan.enabled=true` parameter and any
   other supported parameters that you require. (See limitations section for
   parameters that are not supported in Autonomous mode.)
2. Detect will determine which tools and detectors are
   appropriate and available to run, including Package Manager, Signature, and
   Binary Scanning.
3. Scans will include any analyzable content of user specified locations as well
   as source or binaries located in the run directory.
4. Once complete, scan findings can be viewed in the BDIO file produced, or in
   the Black Duck SCA UI if Black Duck SCA has been configured.

## Subsequent Scan Workflow

1. Run Detect by providing the
   `--detect.autonomous.scan.enabled=true` parameter.
2. Detect will determine if any user provided arguments
   or properties should take precedence over values in the existing scan
   settings file, and run the appropriate available tools and detectors.
3. Once complete, scan findings can be viewed in the BDIO file produced, or in
   the Black Duck SCA UI if Black Duck SCA has been configured.

## Scan mode scenarios

- ONLINE mode: With Black Duck SCA configuration or proxy configuration
  set and `blackduck.offline.mode` not set to true, or overridden
  as false in the scan settings file, the scan will run online.

  - Rapid: Will run if Black Duck SCA is configured and Detect Scan Mode `--detect.blackduck.scan.mode` is set to RAPID.
  - Stateless:
    Will run if Black Duck SCA is configured and `--detect.blackduck.scan.mode` is set to
    STATELESS.
  - Intelligent scan: Runs when scan mode is not set to RAPID or STATELESS,
    or `--detect.blackduck.scan.mode` is explicitly set
    to INTELLIGENT.
- OFFLINE mode: When
  `--blackduck.offline.mode` is true or there is no Black Duck SCA url or Black Duck SCA proxy information provided. (Warning
  messages will be logged for binary and signature scans if applicable tools
  are not available or related parameters not set.)

  - [Binary scan](https://documentation.blackduck.com/bundle/bd-hub/page/BinaryAnalysis/Overview.html): Will run if
    one or more binary files exist in the scan directory and Black Duck SCA configuration is
    completed.
  - Signature scan: Will run against source files if scan cli is
    available. If [scan cli](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/DownloadAndInstall.html) is not locally
    available, it will need to be downloaded from Black Duck SCA.

Table 1. Scan Mode Scenarios

| **Offline Mode**  blackduck.offline.mode | **Black Duck Configured**  URL or Proxy | **Detect Scan Mode**  detect.blackduck.scan.mode | **Tools Configuration**  detect.tools | **Autonomous Scan Mode** | **Black Duck Scan Mode** |
| --- | --- | --- | --- | --- | --- |
| true |  |  |  | Offline | INTELLIGENT |
|  | not configured |  |  | Offline | INTELLIGENT |
| true |  |  | BINARY_SCAN or CONTAINER_SCAN | Offline | Configuration warning logged |
|  | not configured |  | BINARY_SCAN or CONTAINER_SCAN | Offline | Configuration warning logged |
|  | configured |  | CONTAINER_SCAN | Online | INTELLIGENT |
|  | configured |  |  | Online | INTELLIGENT |
|  | configured | RAPID |  | Online | RAPID |
|  | configured | STATELESS |  | Online | STATELESS |
|  | configured | STATELESS | CONTAINER_SCAN | Online | STATELESS |
|  | configured | INTELLIGENT |  | Online | INTELLIGENT |

Note: Blank table fields represent scenarios where the parameter is not provided as user input.

## Requirements and Limitations

### General Requirements

- Scans require local network connectivity when used with Black Duck SCA or if the scan location is remote,
  remote network connectivity is required.
- Black Duck SCA must be configured for binary
  scans.

### Limitations

- Autonomous scanning does not support flags.
- Black Duck SCA Snippet scans are not
  supported.
- The following settings will not be persisted by Detect when running in Autonomous mode:

  --blackduck.api.token

  --blackduck.proxy.password

  --detect.diagnostic

  --detect.output.path

  --detect.bdio.output.path

  --detect.scan.output.path

  --detect.tools.output.path

  --detect.impact.analysis.output.path

  --detect.status.json.output.path

## Invocation without Black Duck SCA

To invoke an Autonomous scan without Black Duck SCA
integration, the following must be provided at a minimum:

```
--detect.autonomous.scan.enabled=true
```

## Invocation with Black Duck SCA

To invoke an Autonomous scan with Black Duck SCA, the
following must be provided at a minimum:

```
--detect.autonomous.scan.enabled=true
--blackduck.url=<https://my.blackduck.url>
--blackduck.api.token=<MyT0kEn>
```

## Results

Autonomous scan findings will be stored in a BDIO file when run without Black Duck SCA.

Autonomous scan findings will appear in the Black Duck SCA
user interface if Black Duck SCA is configured.

## Debug Logging

Run Detect with `--logging.level.detect=DEBUG` to
view the parameters being applied during Autonomous scans.
