---
title: "npm"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/npm.html"
content_id: "YoplzFVIzX4JCqsO2SuiKw"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:39.402158+00:00"
---

# npm

## Additional NPM Command Arguments

```
--detect.npm.arguments
```

A space-separated list of additional arguments that Detect will add at then end of the npm ls command line when Detect executes the NPM CLI Detector on an NPM project.

| Details |  |
| --- | --- |
| Added | 4.3.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `--depth=0` |

## Npm Dependency Types Excluded

```
--detect.npm.dependency.types.excluded=NONE,DEV,PEER,OPTIONAL
```

Set this value to indicate which Npm dependency types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | NpmDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, DEV, PEER, OPTIONAL |
| Strict | Yes |
| Example | `DEV,PEER` |

## NPM Executable

```
--detect.npm.path
```

The path to the Npm executable.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
