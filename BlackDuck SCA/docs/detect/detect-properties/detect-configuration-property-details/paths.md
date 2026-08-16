---
title: "paths"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/paths.html"
content_id: "jWGQz8cGDt4cZBMEUw_n5A"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:24.592177+00:00"
---

# paths

## Bash Executable

```
--detect.bash.path
```

Path to the Bash executable.

If set, Detect will use the given Bash executable instead of searching for one.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/usr/bin/bash` |

## BDIO File Name

```
--detect.bdio.file.name
```

The desired file name of BDIO file Detect produces in the BDIO Output Directory.

If not set, the file name is generated from your project, version and code location names.

| Details |  |
| --- | --- |
| Added | 7.9.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `Project1BDIO` |

## BDIO Output Directory

```
--detect.bdio.output.path
```

The path to the output directory for the generated BDIO file.

If not set, the BDIO file will be placed in a 'BDIO' subdirectory of the output directory.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/home/<username>/blackduck/scan-outputs/bdio` |

## Detector Search Depth

```
--detect.detector.search.depth=0
```

Depth of subdirectories within the source directory to which Detect will search for files that indicate whether a detector applies.

A value of 0 (the default) tells Detect not to search any subdirectories, a value of 1 tells Detect to search first-level subdirectories, etc.

| Details |  |
| --- | --- |
| Added | 3.2.0 |
| Type | Integer |
| Default Value | 0 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Detect Output Path

```
--detect.output.path
```

The path to the output directory.

If set, Detect will use the given directory to store files that it downloads and creates, instead of using the default location (~/blackduck).

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/home/<username>/blackduck/scan-outputs` |

## Detect Tools Excluded

```
--detect.tools.excluded=NONE,DETECTOR,SIGNATURE_SCAN,BINARY_SCAN,IMPACT_ANALYSIS,DOCKER,BAZEL,IAC_SCAN,CONTAINER_SCAN,COMPONENT_LOCATION_ANALYSIS
```

The tools Detect should not allow, in a comma-separated list. Excluded tools will not be run even if all criteria for the tool is met. Exclusion rules always take precedence.

This property and detect.tools provide control over which tools Detect runs. If neither detect.tools nor detect.tools.excluded are set, Detect will allow (run if applicable, based on the values of other properties) all Detect tools. If detect.tools is set, and detect.tools.excluded is not set, Detect will only allow to run those tools that are specified in the detect.tools list. If detect.tools.excluded is set, Detect will only allow those tools that are not specified in the detect.tools.excluded list.

| Details |  |
| --- | --- |
| Added | 5.0.0 |
| Type | DetectTool List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, DETECTOR, SIGNATURE_SCAN, BINARY_SCAN, IMPACT_ANALYSIS, DOCKER, BAZEL, IAC_SCAN, CONTAINER_SCAN, COMPONENT_LOCATION_ANALYSIS |
| Strict | Yes |

## Detect Tools Included

```
--detect.tools=ALL,DETECTOR,SIGNATURE_SCAN,BINARY_SCAN,IMPACT_ANALYSIS,DOCKER,BAZEL,IAC_SCAN,CONTAINER_SCAN,COMPONENT_LOCATION_ANALYSIS
```

The tools Detect should allow in a comma-separated list. Tools in this list (as long as they are not in the excluded list) will run if all criteria of the tool are met. Exclusion rules always take precedence.

This property and detect.tools.excluded provide control over which tools Detect runs. If neither detect.tools nor detect.tools.excluded are set, Detect will allow (run if applicable, based on the values of other properties) all non-exclusive Detect tools. If detect.tools is set, and detect.tools.excluded is not set, Detect will run those tools that are specified in the detect.tools list. If detect.tools.excluded is set, Detect will only allow those tools that are not specified in the detect.tools.excluded list.

| Details |  |
| --- | --- |
| Added | 5.0.0 |
| Type | DetectTool List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, DETECTOR, SIGNATURE_SCAN, BINARY_SCAN, IMPACT_ANALYSIS, DOCKER, BAZEL, IAC_SCAN, CONTAINER_SCAN, COMPONENT_LOCATION_ANALYSIS |
| Strict | Yes |

## Git Executable

```
--detect.git.path
```

Path of the git executable

| Details |  |
| --- | --- |
| Added | 5.5.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/usr/bin/git` |

## Java Executable

```
--detect.java.path
```

Path to the Java executable used by Docker Inspector.

If set, Detect will use the given Java executable instead of searching for one.

| Details |  |
| --- | --- |
| Added | 5.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/usr/lib/jvm/jdk-17/bin/java` |

## SCAAAS Scan Target

```
--detect.scaaas.scan.path
```

Internal use only. Specified file will be uploaded to the BDBA worker for scan analysis in an SCA as a service environment.

| Details |  |
| --- | --- |
| Added | 8.8.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Scan Output Path

```
--detect.scan.output.path
```

The output directory for all signature scanner output files. If not set, the signature scanner output files will be in a 'scan' subdirectory of the output directory.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Source Path

```
--detect.source.path
```

The source path is the path to the project directory to inspect. If no value is provided, the source path defaults to the current working directory.

Detect will search the source directory for hints that indicate which package manager(s) the project uses, and will attempt to run the corresponding detector(s).The source path is also the default target for signature scanning. (This can be overridden with the detect.blackduck.signature.scanner.paths property.)

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Status JSON Output Path

```
--detect.status.json.output.path
```

The directory to place a copy of the status.json file.

If set, Detect will use the given directory to store a copy of the status.json file.

| Details |  |
| --- | --- |
| Added | 8.1.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/home/<username>/blackduck/scan-outputs/status` |

## Detect Excluded Directories (Advanced)

```
--detect.excluded.directories
```

A comma-separated list of names, name patterns, relative paths, or path patterns of directories that Detect should exclude. Caution should be exercised when including this parameter on Windows, as the command length generated may exceed OS limitations.

Subdirectories whose name or path is resolved from the patterns in this list will not be searched when determining which detectors to run, will not be searched to find files for binary scanning when property detect.binary.scan.file.name.patterns is set, and will be excluded from signature scan using the Scan CLI '--exclude' flag. For further information, refer to the [Including and Excluding Tools, Detectors, Directories page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/runningdetect/includingexcluding/intro%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `**/*-test` |

## Detect Excluded Directories Defaults Disabled (Advanced)

```
--detect.excluded.directories.defaults.disabled=false
```

If false, Detect will exclude the default list of directory names when searching for applicable detectors.

Directories excluded by default from Detector Scans: __MACOSX, bin, build, .git, .gradle, .yarn, node_modules, out, packages, target, .synopsys, .blackduck, .bridge and the following directories will be excluded from Signature Scan using the Scan CLI '--exclude' flag: .git, .gradle, gradle, node_modules, .synopsys, .blackduck, .bridge.

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Detector Search Continue (Advanced)

```
--detect.detector.search.continue=false
```

By default, nesting rules limit which detectors can run on a subdirectory based on which detectors applied on any parent directory. Setting this property to true disables nesting rules.

For further explanation on nesting rules, refer to [Detector search and accuracy.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/runningdetect/detectorcascade%2Ehtml)

| Details |  |
| --- | --- |
| Added | 3.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Detector Tool Priority (Advanced)

```
--detect.project.tool=DETECTOR,SIGNATURE_SCAN,BINARY_SCAN,IMPACT_ANALYSIS,DOCKER,BAZEL,IAC_SCAN,CONTAINER_SCAN,COMPONENT_LOCATION_ANALYSIS
```

The tool priority for project name and version. The project name and version will be determined by the first tool in this list that provides them.

This allows you to control which tool provides the project name and version when more than one tool are capable of providing it.

| Details |  |
| --- | --- |
| Added | 5.0.0 |
| Type | DetectTool List |
| Default Value | DOCKER,DETECTOR,BAZEL |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | DETECTOR, SIGNATURE_SCAN, BINARY_SCAN, IMPACT_ANALYSIS, DOCKER, BAZEL, IAC_SCAN, CONTAINER_SCAN, COMPONENT_LOCATION_ANALYSIS |
| Strict | Yes |

## Detect Tools Output Path (Advanced)

```
--detect.tools.output.path
```

The path to the tools directory where detect should download and/or access things like the Signature Scanner that it shares over multiple runs.

If set, Detect will use the given directory instead of using the default location of output path plus tools.

| Details |  |
| --- | --- |
| Added | 5.6.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/home/<username>/blackduck/scan-outputs/tools` |

## Project Name and Version Detector (Advanced)

```
--detect.project.detector
```

The detector that will be used to determine the project name and version when multiple detector types apply. This property should be used with detect.project.tool.

If Detect finds that multiple detectors apply, this property can be used to select the detector that will provide the project name and version. When using this property, you should also set detect.project.tool=DETECTOR

| Details |  |
| --- | --- |
| Added | 4.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
