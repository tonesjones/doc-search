---
title: "Using the Black Duck Rapid Scan Static Jenkins Plugin"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-the-black-duck-rapid-scan-static-jenkins-plugin.html"
content_id: "AAzvTMS~FnPGam1mWpliHg"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:14.796483+00:00"
---

# Using the Black Duck Rapid Scan Static Jenkins Plugin

Note: The Jenkins plugin is deprecated.

The Black Duck
Rapid Scan Static plugin is a Jenkins plugin,
intended to be used with the Sigma binary download. This plugin provides the
following:

- A Sigma Tool Installation to install on Jenkins Agents to execute the Sigma
  tool.
- A Jenkins build step to execute Sigma analysis of source code and to produce a
  results file (sigma-results.json) that contains the issues
  found.
- An integration with the Warnings Next Generation Jenkins plugin to record Sigma
  issues post build.

This chapter explains how you use the Black Duck Rapid Scan Static plugin to execute Sigma
in a Jenkins build either as a quality gate or to report static analysis issues.

Note: If you are using the Sigma Docker image, please see Getting the Docker Image for instructions.

The basic workflow for installing, configuring, and using the Black Duck Rapid Scan Static
plugin is as follows:

1. The administrator downloads the Sigma binaries to be used.
2. The administrator installs the Black Duck Rapid Scan Static Jenkins plugin.
3. The administrator configures the Sigma installation on the Jenkins agent.
4. The user creates a Jenkins Freestyle project or a Jenkins Pipeline.
5. The Jenkins Freestyle project or Pipeline is executed as part of the development
   process.
