---
title: "Build tools and package managers"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/build-tools-and-package-managers.html"
content_id: "i53KzQp1Zr7ntJCgMLILFA"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.384564+00:00"
---

# Build tools and package managers

Code Sight lets you specify the build tools used for a project that Black Duck scans. The details depend on the IDE.

## Eclipse

The tool can be either Apache® Maven™ or npm®.

- **Maven**

  Specify the local installation of Maven in Eclipse Preferences: Preferences dialog → Maven → Installations.

  Make sure the Maven installation has permission to execute.

  Attention: Code Sight *does not support* the EMBEDDED run-time Maven.
- **npm**

  The npm executable must be in an accessible location. Add this location to the `$PATH` environment variable.

## IntelliJ

The tool can be either Maven or npm.

- **Maven**

  Specify the local installation of Maven in IntelliJ Preferences: Preferences dialog → Build, Execution, Deployment → Build Tools → Maven → Maven home path.

  Make sure the Maven installation has permission to execute.

  Attention: As of IntelliJ 2022.2, Code Sight can run Open Source scans by using the EMBEDDED run-time Maven.
- **npm**

  For the Ultimate edition of IntelliJ, Code Sight automatically uses the npm path that is specified in Preferences dialog → Languages & Frameworks → Node.js and NPM → Node Interpreter.

  For the Community edition, save the npm executable in an accessible location from which it can be run. Add this location to the `$PATH` environment variable.

## Visual Studio

The tool can be either NuGet or npm.

- **NuGet**

  For the NuGet package manager, no additional configuration is necessary.
- **npm**

  The npm executable must be in an accessible location. Add this location to the `$PATH` environment variable.

## Visual Studio Code

The tool can be either Maven or npm.

To specify the location of your preferred build tool, use the Environment Variables panel.
