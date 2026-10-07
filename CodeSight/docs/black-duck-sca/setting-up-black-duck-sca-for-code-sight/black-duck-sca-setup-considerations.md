---
title: "Black Duck SCA setup considerations"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/black-duck-sca-setup-considerations.html"
content_id: "cODpQc9qy6CUJ17MZag3Ig"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.282697+00:00"
---

# Black Duck SCA setup considerations

To run Black Duck SCA in Code Sight, a system must meet certain requirements.

## Java support

The system must be configured to run the Java® Development Kit (JDK),
release 8 or higher.

## Scan engine

We highly recommend that you verify that the locally installed Black Duck SCA scanning component,
Black Duck®
Detect, is the most recent version. Recent versions of Detect are posted in the [Black Duck Artifactory](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/detect/).

## The package manager and build support

The package manager for the projects to analyze, and the build tool or tools it uses, must have been
installed and be specified in the system’s `PATH` variable.

## User credentials

Each user account must be configured to meet the following conditions:

- The user must have access to check for component security vulnerabilities.
- It must be possible to check each component against the projects accessible to the
  user, and the global policies configured on the Black Duck SCA server.
- All dependencies must be resolvable.
  That is to say, each dependency must have been installed using the package manager’s
  cache, virtual environment, and other environmental settings.

## Internet access

To communicate with the Black Duck SCA server, the system must be connected to the Internet.

Remember:
Internet access is also needed when you install Code Sight, to download Code Sight itself,
and also the Black Duck Detect application, if this is not already present on the system.
See Installation.

The plug-in downloads the Detect application from the URL that is saved
on the Administration → System Settings page for your Black Duck SCA account.
By default, this Hosting location value points to
the Black Duck Artifactory.
You can configure Black Duck SCA to download Detect from a different location:
See Specify a custom download location for Black Duck Detect.
