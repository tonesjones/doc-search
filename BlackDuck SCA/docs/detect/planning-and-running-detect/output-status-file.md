---
title: "Output Status File"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/output-status-file.html"
content_id: "ggU42h036O42S1wNLnw8Vg"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:39.745892+00:00"
---

# Output Status File

Black Duck® Detect creates an output status file in the run folder with the name "status.json" which contains a summary of the Detect run in a machine readable format.

The file includes status codes, issues encountered and results produced. As additional processes consume this file, additional information will be added. The format is intended to evolve over time.

- As Detect shuts down, by default, it performs cleanup operations which include deleting the status file. You can disable clean up by setting `--detect.cleanup=false`.

## Body

```
{
"formatVersion": The version of the status file format. Will change as new features are introduced.
"detectVersion": The version of [detect_product_short] that created the status file.
"projectName": The project name.
"projectVersion": The project version.
"detectors": [ List of Detectors, see details below. ]
"status": [ List of Status, see details below. ]
"issues": [ List of Issues, see details below. ]
"overallStatus: [ List the overall exit status and detailed message on exit of [detect_product_short]. ]
"results": [ List of Results, see details below. ]
"unrecognizedPaths": [ List of Unrecognized Paths, see details below. ]
"codeLocations": [ List of code locations produced, see details below. ]
"propertyValues": { An object representing all provided properties, see details below. }
"operations": [ List of performed operations, see details below. ]
}
```

## Detector

```
{
"folder": The folder the detector applied to.
"detectorType": The normalized detector type such as "GIT".
"detectorName": A shorthand name of the detector such as "Git Cli".
"discoverable":  A boolean indicating whether or not the detector was able to discover project information.
"extracted": A boolean indicating whether or not the detector was able to extract dependencies.
"status": An enum indicating whether the detector was successful, failed, or deferred to another detector.
"statusCode": A code specifying the nature of the detector's failure, or PASSED if the detector was successful. See below for a complete list of possible status codes.
"statusReason": A human readable description of the status code.
"relevantFiles": [ A list of files relevant to the detector. ]
"discoveryReason": A human readable description of the discovery result.
"extractedReason": A human readable description of the extraction result.
"projectName": The project name this detectable found.
"projectVersion": The project version this detectable found.
"codeLocationCount": The number of code locations this detector produced.
"explanations": [ A human readable list of strings describing why this detector ran such as "Found file:
<path>". ]
}
```

## Detector Status Codes

| Status Code | Description |
| --- | --- |
| ATTEMPTED | Detector attempted to run but did not succeed. |
| CARGO_LOCKFILE_NOT_FOUND | A Cargo.toml was located in the target project, but the Cargo.lock file was NOT located. |
| CARTFILE_RESOLVED_FILE_NOT_FOUND | A Cartfile was located in the target project, but the Cartfile.resolved file was NOT located. |
| EXCEPTION | An exception occurred. |
| EXCLUDED | Detector type was excluded. |
| EXECUTABLES_NOT_FOUND | The necessary executables were not found. |
| EXECUTABLE_FAILED | During extraction, one or more executables did not execute successfully. |
| EXECUTABLE_NOT_FOUND | The necessary executable was not found. |
| EXECUTABLE_TERMINATED_LIKELY_OUT_OF_MEMORY | An executable was terminated, potentially due to a runtime environment low memory condition. |
| EXECUTABLE_VERSION_MISMATCH | Unexpected executable version was encountered. |
| EXTRACTION_FAILED | During extraction, one or more exceptions were encountered. |
| FAILED | Detector failed. |
| FILES_NOT_FOUND | Necessary files were not found within the target project. |
| FILE_NOT_FOUND | A file was not found within the target project. |
| FORCED_NESTED_PASSED | Forced to pass because nested forced by user. |
| GO_PKG_LOCKFILE_NOT_FOUND | A Gopkg.toml was located in the target project, but the Gopkg.lock file was NOT located. |
| INSPECTOR_NOT_FOUND | The necessary inspector was not found |
| IVY_DEPENDENCY_TREE_NOT_FOUND | A build.xml file was found, but it does not contain an ivy:dependencytree task. |
| MAX_DEPTH_EXCEEDED | Max depth was exceeded. |
| NOT_NESTABLE | Not nestable and a detector already applied in parent directory. |
| NOT_NESTABLE_BENEATH | Nestable but another detector prevented nesting. |
| NPM_NODE_MODULES_NOT_FOUND | A package.json was located in the target project, but the node_modules folder was NOT located. |
| PASSED | Detector passed. |
| PIPFILE_LOCK_NOT_FOUND | A Pipfile was located in the target project, but a Pipfile.lock was NOT located. |
| POETRY_LOCKFILE_NOT_FOUND | A pyproject.toml was located in the target project, but the Poetry.lock file was NOT located. |
| POORLY_FORMATTED_JSON | Attempted to parse a JSON file but the contents did not conform to the JSON specification. |
| PROPERTY_INSUFFICIENT | The properties are insufficient to run. |
| PUBSPEC_LOCK_NOT_FOUND | A pubspec.yaml file was found, but a pubspec.lock file was NOT found. |
| SBT_PLUGIN_MISSING | A dependency graph plugin must be installed for the SBT detector to run. |
| SECTION_NOT_FOUND | A necessary section was not found within a file within the target project. |
| SETUP_TOOLS_NO_DEPENDENCIES | No dependencies found in pyproject.toml, setup.cfg, or setup.py. |
| SETUP_TOOLS_REQUIRES_NOT_FOUND | The necessary requires setuptools statement is missing from the pyproject.toml. |
| UNKNOWN_DETECTOR_RESULT | There was an unknown result. |
| UV_LOCKFILE_NOT_FOUND | A pyproject.toml was found in the root directory, but a uv.lock file or requirements.txt were NOT found. |
| WRONG_OPERATING_SYSTEM_RESULT | Cannot run on the used operating system. |
| YIELDED | Yielded to other detectors. |

## Status

```
{
"key": The normalized key this status element describes such as "GIT".
"status": "SUCCESS" or "FAILURE"
}
```

## Issues

```
{
"type": A key describing the type of issue, currently "EXCEPTION", "DEPRECATION" or "DETECTOR".
"title": A string describing the issue.
"messages": A list of a strings describing the details of the issue.
}
```

## Results

A result is a URL, file path to output, or messages produced by the Detect run: a Black Duck® SCA Bill Of Materials, Risk Report, Notices Report, Air Gap zip, or Rapid Scan results.

```
{
"location": The path to the result.
"message": A string describing the result.
"sub_messages": A list of strings providing more detail about the result.
}
```

## Unrecognized Paths

For those detectors that support it (currently, only CLANG), a list of file paths to dependencies that
(a) were not recognized by the package manager, and (b) reside outside the source directory.

```
{
"<Detector type>": [ A list of file paths to unrecognized dependencies ]
}
```

## Code Locations

```
{
"codeLocationName": The name of a code location produced by this run of [detect_product_short].
"scanType": The type of scan that was performed, DETECTOR, BINARY_SCAN, SIGNATURE_SCAN, or CONTAINER_SCAN.
"scanId": The UUID for the scan.
}
```

## Property Values

A map of every property key to it's string value that Detect found. These are only properties to which Detect has a known key,
so pass-through properties like Docker and dynamic properties like custom fields are not included. Passwords and other sensitive fields are masked.

```
  "propertyValues": {
    "key": "value",
    "boolean-key": "true"
  }
```

## Operations

A list of information regarding internal execution of Detect to describe when portions of Detect run and what their status is.
This information is intended to be used when Detect fails and the reason(s) for a Detect] failure.

```
  "operations": {
    "startTimestamp": A formatted UTC timestamp when the execution started.
    "endTimestamp": A formatted UTC timestamp when the execution ended.
    "descriptionKey": A string that describes what is being executed.
    "status": "SUCCESS" or "FAILURE"
  }
```

## Black Duck Server Properties

A map of property keys to their string values that have been configured at the Black Duck server level and applied to this Detect run. These properties originate from the server rather than from user-provided configuration.

```
  "blackDuckServerProperties": {
    "detect.blackduck.correlated.scanning.enabled": "true" or "false"
  }
```
