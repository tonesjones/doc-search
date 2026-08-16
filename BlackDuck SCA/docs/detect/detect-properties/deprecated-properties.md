---
title: "Deprecated Properties"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/deprecated-properties.html"
content_id: "bGEf0T0mivmwBXYI3fcytw"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:48.281687+00:00"
---

# Deprecated Properties

This page lists Black Duck® Detect deprecated properties for software versions that are still supported. This page may be blank when there are no such deprecated properties. For both active and deprecated properties, refer to all properties for usage details.

## quack-patch

| Property | Description |
| --- | --- |
| detect.quack.patch.output | Quack Patch Output Directory: Specifies the output directory for Quack Patch results.  **DEPRECATED: This property is deprecated and will be renamed to 'detect.quack.patch.output.path' in Detect release 12.0. This property will be removed in 12.0.0.** |

## bazel

| Property | Description |
| --- | --- |
| detect.bazel.workspace.rules | default: NONE  Acceptable Values: ALL, NONE, MAVEN_JAR, MAVEN_INSTALL, HASKELL_CABAL_LIBRARY, HTTP_ARCHIVE  Bazel workspace rules: By default Detect discovers Bazel dependencies using all supported Bazel workspace rules that it finds in the WORKSPACE file. Alternatively you can use this property to specify the list of Bazel workspace rules Detect should use.  **DEPRECATED: This property has been deprecated. Please use detect.bazel.dependency.sources instead. This property will be removed in 12.0.0.** |
