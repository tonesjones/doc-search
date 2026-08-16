---
title: "Swift & Xcode support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/swift-xcode-support.html"
content_id: "3emuW6Y4VZ1oMSivqrHovg"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:45:11.991394+00:00"
---

# Swift & Xcode support

## Related properties

Detector properties

## Overview

Detect detectors for Swift and Xcode:

- Swift CLI detector
- Swift Package Resolved detector
- Xcode Project detector
- Xcode Workspace detector

All of these detectors primarily use the `Package.resolved` file to extract dependencies.

## Swift CLI detector

The Swift CLI detector discovers dependencies of projects utilizing the Swift CLI.

The Swift CLI detector applies to directories containing a `Package.swift` file.

This detector requires a `swift` executable to run a command `swift package show-dependencies` to create a dependency graph of Swift packages.

All packages of the root node are considered direct dependencies in the Black Duck SCA BOM.

Packages found with a version of `unspecified` will appear in the BOM without a version.

## Swift Package Resolved detector

The Swift Package Resolved detector discovers dependencies of projects utilizing the Swift Package Resolved.

The Swift Package Resolved detector applies to directories containing either a `Package.swift` file or `Package.resolved` file.

All packages of the packages are considered direct dependencies in the Black Duck SCA BOM.

Packages found with a version of `unspecified` will appear in the BOM without a version.

This detector does not require any executables to run.

## Xcode Workspace detector

The Xcode Workspace detector discovers dependencies of Xcode projects utilizing [built-in tools within Xcode](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app) for managing Swift dependencies.

The Xcode Workspace detector applies to directories matching the `*.xcworkspace` filename pattern within bounds of the *detect.detector.search.depth* property.

When Detect finds a matching directory, the Xcode Workspace detector then searches for a `Package.resolved` file inside your `*.xcworkspace` directory at `*.xcworkspace/xcshareddata/swiftpm/Package.resolved` and extracts those dependencies.

Additionally, the Xcode Workspace detector will analyze the contents of the `*.xcworkspace/contents.xcworkspacedata` XML file to determine Xcode Workspace reference locations. This ignores the *detect.detector.search.depth* property as Detect is no longer searching, but be directed to a specific location.

Today supported Workspace reference locations are directories and Xcode Projects.
Any referenced locations that are not found currently trigger a failure of Detect

- Xcode Projects are identified with by the suffix `*.xcodeproj`.

  - Example `location = "group:src/my-project.xcodeproj">`
- Directories are identified with by the suffix `/`

  - Example `location = "group:src/my-project/">`
  - Directories are assumed to be a built Swift Package containing a `Package.resolved` file at the specified location

This detector does not require any executables to run, but the Xcode Workspace must be buildable in Xcode.

## Xcode Project detector

The Xcode Project detector discovers dependencies of Xcode projects utilizing [built-in tools within Xcode](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app) for managing Swift dependencies.

The Xcode Project detector applies to directories matching the `*.xcodeproj` filename pattern within bounds of the *detect.detector.search.depth* property.

Once the Xcode Project detector finds a matching directory, it searches for a `Package.resolved` file inside your `.xcodeproj` directory at `[appName].xcodeproj/project.workspace/xcshareddata/swiftpm/Package.resolved`.

This detector does not require any executables to run, but the Xcode Workspace must be buildable in Xcode.

## Package.resolved file

This file forms the basis for dependency extraction for most of the Swift and Xcode detectors.

The `Package.resolved` is a JSON file containing a flat list of Swift packages required by the project.
This file can be empty if the project has no dependencies, in which case Detect will create an empty code-location for the Xcode project.

Example `Package.resolved` file contents:

```
{
  "object": {
    "pins": [
      {
        "package": "swift-argument-parser",
        "repositoryURL": "https://github.com/apple/swift-argument-parser.git",
        "state": {
          "branch": null,
          "revision": "d2930e8fcf9c33162b9fcc1d522bc975e2d4179b",
          "version": "1.0.1"
        }
      }
    ]
  },
  "version": 1
}
```

### Extraction method

Detect is capable of extracting component name and versions from the JSON content within the `Package.resolved` file.

#### Forge

Currently, all packages are assumed to come from GitHub. For support of additional public repositories, please contact the Detect support team.

#### Component Name

The component name is derived from the **repositoryURL** field.

```
"repositoryURL": "https://github.com/apple/swift-argument-parser.git"
```

Detect will parse the path of the url to remove the host and `.git` extensions.
In the above example, this produces a component name of `apple/swift-argument-parser`.

#### Component Version

Detect will use the **state.version** field to identify the component version.

```
"state": {
    "branch": null,
    "revision": "d2930e8fcf9c33162b9fcc1d522bc975e2d4179b",
    "version": "1.0.1"
}
```

In the above example, this produces a component version of `1.0.1`.
