---
title: "Introduction to Black Duck® Detect"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/introduction-to-black-duck-detect.html"
content_id: "S8kyQwUfDP5OiJX4IFHUwg"
version: "11.5.1"
section: "Introduction to Black Duck® Detect"
scraped_at: "2026-08-08T23:43:56.502468+00:00"
---

# Introduction to Black Duck® Detect

Black Duck® Detect is an intelligent scan client that analyzes code in your projects and associated folders to perform compositional analysis. Detect can be configured to send scan results to Black Duck® SCA, which generates risk analysis when identifying open-source components, licenses, and security vulnerabilities.

Detect can be used in both connected and air gap modes depending on the types of scans being run.

## Detect characteristics.

- Detect integrates with development tools used throughout the SDLC (software development life cycle) and automatically detects resources to optimize its scan methodology.
- Detect provides scanning capabilities for Black Duck SCA to help identify open-source components, licenses, and security vulnerabilities. This is achieved through a variety of detection methods such as package manager inspection, file system based signature scanning of source directories and files, Docker image inspection, and binary analysis.
- Detect provides the source of information for Black Duck SCA to analyze open-source components and find vulnerabilities in open-source components and containers. Using this type of analysis, you can minimize security, compliance, and code quality risks; you can monitor for new vulnerabilities throughout your development cycle, and you can set and enforce open-source use and security policies.
- Runs on Windows, Linux, and macOS. It is available through GitHub, under the permissive Apache License, Version 2.0 and does not require pre-installation or extensive configuration.
- Supports scanning Docker images by identifying open-source libraries and code within the images, using both signature scanning and the package manager analysis techniques.

## Detect functionality consolidation.

Detect consolidates the functionality of Black Duck SCA, package managers, and continuous integration plugin tools to perform the following tasks:

- Discover open-source components in your code.
- Map components to known security vulnerabilities.
- Identify license compliance and component quality risks.
- Set and enforce open-source use and security policies.
- Integrate open-source management into your DevOps environment.
- Monitor and alert users when new security threats are reported.
- Calculate security vulnerability risk in your code.
- Produce reports of the open-source analysis findings.
- Provide malware information if identified.

Note: Some scan types require specific feature licenses to execute. Contact your Black Duck Software, Inc. representative for further information.

## How Detect functions.

When looking at vulnerabilities in open source and third-party software, Detect performs the following basic steps:

- Uses the project's package manager to derive the hierarchy of dependencies known to that package manager. For example, on a Maven project, Detect executes an mvn dependency:tree command and derives dependency information from the output.
- Runs the Black Duck SCA signature scanner on the project. This might identify additional dependencies not known to the package manager (for example, a .jar file copied into the project directory).
- Uploads both sets of results (dependency details) to Black Duck SCA creating the project/version if it does not already exist. Black Duck SCA uses the uploaded dependency information to build the Bill Of Materials (BOM) for the project/version.
- You can view the output and analysis results in Black Duck SCA.
