---
title: "Carthage support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/carthage-support.html"
content_id: "lFEsLzG6zPesdF3D3QTRnA"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:50.149205+00:00"
---

# Carthage support

## Overview

Detect runs the Carthage detector if it finds either of the following files in your project:

- Cartfile
- Cartfile.resolved

The Carthage detector parses the Cartfile.resolved file for information on your project's dependencies. If the detector discovers a Cartfile file but not a Cartfile.resolved file, it will prompt the user to generate a Cartfile.resolved file by running `carthage update` and then run Detect again.

## Supported Dependency Origins

Detect only reports dependencies declared in a Cartfile.resolved file that have a 'github' [origin](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#origin). This limited support is a result of the de-centralized nature of the Carthage ecosystem. Many commonly-used frameworks used in Carthage projects are not open-source, and thus not tracked by Black Duck SCA.

- Note: Even for dependencies from Github that are declared with the 'github' origin, it is possible that some may not be matched by Black Duck SCA, as Black Duck SCA does not track all repositories hosted on GitHub.
