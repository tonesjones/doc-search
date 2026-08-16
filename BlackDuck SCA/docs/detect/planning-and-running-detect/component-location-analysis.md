---
title: "Component Location Analysis"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/component-location-analysis.html"
content_id: "lzp1dyN_smcThhr2sknNLw"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:35.769499+00:00"
---

# Component Location Analysis

Enable this feature by adding the `--detect.component.location.analysis.enabled=TRUE` parameter to a run of Black Duck® Detect.

Detect generates a `components-with-locations.json` file in the scan subdirectory of the output directory when Component Location Analysis is enabled. This file contains the declaration locations (file path, line number, and column position) of the open-source component versions that were detected in the scanned project.

Note: By default, when Detect shuts down, it performs cleanup operations which include deleting the component location analysis file. You can disable clean up by setting `--detect.cleanup=false`.

## Requirements and Limitations

- A subset of Detector Types support this feature.

  - Supported Detectors: CARGO, CONDA, GRADLE, GO_MOD, GO_DEP, GO_GRADLE, GO_VENDOR, GO_VNDR, MAVEN, NPM, NUGET, PIP, POETRY, and YARN.
- Supported scan modes: Offline and Rapid/Stateless.

  - Offline mode

    - When enabled for a scan without Black Duck SCA connectivity, all detected open source components will be included in the location analysis results.
  - Rapid/Stateless Scan mode requires Black Duck SCA policies.

    - Only components that violate policies will be included in the analysis. If no policies are violated or there are no defined policies, component location analysis is skipped.

## Offline Mode Results

Each component is uniquely identified by a name and version. Components may optionally have a higher-level grouping identifier, commonly referred to as a groupId, organization, or vendor. The declaration location of each component is included in the results if found. When not found, no declarationLocation field will be present for that component in the output file.

Note: The metadata field is only populated in the case of a Rapid or Stateless Scan. See Rapid or Stateless Scan Mode Results

**Example results BODY:**

```
{
    "sourcePath": "/absolute/path/to/project/root",
    "globalMetadata": {},                                 // Passthrough data from producer to consumer (optional)
    "componentList": [
        { 
            "groupID": "org.sonarqube",                   // Component group (if available)
            "artifactID": "org.sonarqube.gradle.plugin",  // Component name
            "version": "2.8",                             // Component version
            "metadata": {                                 // Passthrough upgrade guidance data (unavailable in offline scan)
                "policyViolationVulnerabilities": [],     // (if available)
                "shortTermUpgradeGuidance": {},           // (if available)
                "longTermUpgradeGuidance": {},            // (if available)
                "transitiveUpgradeGuidance": [],          // (if available)
                "componentViolatingPolicies": []          // (if available)
            },
            "declarationLocation": {                      // Included if the component was located
                "fileLocations": [
                    {
                        "filePath": "build-script/build.gradle.kts",
                        "lineLocations": [
                            {
                                "lineNumber": 12,
                                "columnLocations": [
                                    {
                                        "colStart": 63,
                                        "colEnd": 65
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

## Rapid or Stateless Scan Mode Results

When Detect runs a Rapid or Stateless scan, the output file includes policy violation vulnerabilities, component violating policies, dependency trees for individual components and remediation guidance (short term, long term and transitive upgrade guidance) when available. This information is contained within the metadata field of each component.

## Version Range Operator Support

Component Location Analysis supports locating dependency declarations that use version range operators. When a version declaration uses a supported operator, an optional `operator` field is included in the `columnLocations` entry to indicate the specific operator used in the declaration.

### Supported Package Managers

- **npm / Yarn**: Fully supported with all semantic versioning operators (`=`, `>`, `<`, `>=`, `<=`, `~`, `^`, `-`).
- **PIP**: Partially supported with comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`).

  Note: Python's ~= operator has different semantics than npm ~ operator and is not currently supported.

### Supported Operators

The following version range operators are supported for npm and Yarn:

| Operator | Description | Example |
| --- | --- | --- |
| `=` | Equal | `=1.2.3` |
| `>` | Greater than | `>1.2.3` |
| `<` | Less than | `<2.0.0` |
| `>=` | Greater than or equal | `>=1.2.3` |
| `<=` | Less than or equal | `<=2.0.0` |
| `~` | Tilde range (patch updates) | `~1.2.3` (≥1.2.3, <1.3.0) |
| `^` | Caret range (minor updates) | `^1.2.3` (≥1.2.3, <2.0.0) |
| `-` | Hyphen range | `1.2 - 1.4.5` (≥1.2.0, ≤1.4.5) |

For PIP, the comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) are supported.

### Output Format

When a version range operator is detected, the `operator` field appears in the `columnLocations` entry:

```
{
    "lineNumber": 3753,
    "columnLocations": [
        {
            "colStart": 22,
            "colEnd": 27,
            "operator": "^"
        }
    ]
}
```

Note: Version range operators are not supported for Maven, Gradle, or NuGet at this time. These package managers use bracket notation for version ranges, which requires different parsing logic.
