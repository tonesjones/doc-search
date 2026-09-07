---
title: "Detect Processing"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/detect-processing.html"
content_id: "lMXX~jmHMa0E9mqVYuNuZQ"
version: "12.0.0"
section: "Getting started with Detect"
scraped_at: "2026-09-07T21:15:11.600611+00:00"
---

# Detect Processing

Detect processing can be broken into the following phases:

## Initialization phase

In this phase, Detect does verification checks on the user-provided configuration, checks connectivity to any external systems needed for the run, and creates any required directories.

## Run phase

In this phase, Detect processes an ordered list of tools, invoking all that apply, which depends on how Detect is configured.

Detect analysis is done using an ordered set of tools that you specify using Detect properties.

- By default, the build detector tool is run. This detector runs after a build and has access to both build artifacts and build tools; it produces the most accurate results.
- If Black Duck SCA connection details are provided, the Black Duck SCA signature scanner tool also runs by default.

Depending on project contents, the detector tool runs different types of detectors to find and extract dependencies from supported package managers. For example, if Detect finds a pom.xml file, it runs the Maven detector. If Detect finds Gradle files, it runs the Gradle detector.

At the end of the run phase, Detect uploads results to Black Duck SCA, and optionally performs tasks such as generating a risk report or checking for policy violations.

## Cleanup phase

During the cleanup phase, Detect removes temporary files and directories before exiting.
