---
title: "Building Xcode projects that use pre-compiled headers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/building-xcode-projects-that-use-pre-compiled-headers.html"
content_id: "n6iNRH15De6hwS22X8VPHA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:29.046319+00:00"
---

# Building Xcode projects that use pre-compiled headers

By default, Xcode projects that utilize pre-compiled header (PCH) files will use a cache
directory for generated and referenced PCH files. When capturing an Xcode project based
build using `cov-build`, if the PCH cache directory contains PCH files
that are used (but not generated) by the build, then their generation will not be
observed by `cov-build`. This may result in Coverity compilation errors
corresponding to native compiler invocations for source files that require use of the
PCH files for successful compilation. In particular, problems arise when compiling
source files that depend on the existence of a pre-compiled prefix header, but do not
contain an `#include` directive to include the header.

The following techniques can be used to work around this problem when building with the
`xcodebuild` utility:

- Specify the clean build action with the `xcodebuild` invocation so that
  previously cached PCH files are removed and regenerated.

  ```
  > xcodebuild -project my-project.xcodeproj clean build
  ```
- Set the `SHARED_PRECOMPS_DIR` Xcode setting to the path to an empty temporary
  directory.

  This setting can be specified in the `xcodebuild`
  command-line invocation or in an Xcode config file either in the default
  location (~/.xcconfig) or as specified by the
  `-xcconfig` command-line option or the
  `XCODE_XCCONFIG_FILE` environment variable.

  ```
  > xcodebuild SHARED_PRECOMPS_DIR=/tmp/shared-precomps-dir -project my-project.xcodeproj
  ```
- Set the `GCC_PRECOMPILE_PREFIX_HEADER` Xcode setting to disable use of
  pre-compiled prefix headers. This is only an option if the source project is
  designed to build successfully without a prefix header, or when the pre-compiled
  prefix header is not built.

  This setting can be specified in the
  `xcodebuild` command-line invocation or in an Xcode config
  file either in the default location (~/.xcconfig) or as
  specified by the `-xcconfig` command-line option or the
  `XCODE_XCCONFIG_FILE` environment variable.

  ```
  > xcodebuild GCC_PRECOMPILE_PREFIX_HEADER=no -project my-project.xcodeproj
  ```
