---
title: "Detect Azure DevOps (ADO) Plugin"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-azure-devops-ado-plugin.html"
content_id: "KlX033g7w41Ze0bIo02j1A"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:05.131309+00:00"
---

# Detect Azure DevOps (ADO) Plugin

The Black Duck® Detect for Azure DevOps plugin is architected to seamlessly integrate Black Duck® SCA with Azure DevOps build and release pipelines. Black Duck® Detect makes it easier to set up and scan code bases using a variety of languages and package managers.

The Detect plugin for Azure DevOps supports native scanning in your Azure DevOps environment to run Software Composition Analysis (SCA) on your code.

As a Detect and Azure DevOps user, Detect Extension for Azure DevOps enables you to:

- Run a component scan in an Azure DevOps job and create projects and releases in Black Duck SCA through the Azure DevOps job.
- After a scan is complete, the results are available on the Black Duck SCA server (for SCA).

Using the Detect Extension for Azure DevOps together with Black Duck SCA enables you to use Azure DevOps to automatically create Black Duck SCA projects from your Azure DevOps projects.

Note: The Azure plugin currently supports Detect 9.x or greater.

Figure 1. Plugin
[image: Plugin]

## Invoking Detect

It is recommended to invoke Detect from the CI (build) pipeline. Scanning during CI enables Detect to break your application build, which is effective for enforcing policies like preventing the use of disallowed or vulnerable components.

Figure 2. ADO Tasks screen
[image: Intro]

## Basic workflow

Using Detect to analyze your code in Azure involves the following basic steps:

1. Make sure you satisfy system and other requirements.
2. Download and configure the Detect extension in Azure.
3. Configure build agent and pipeline.
4. Configure Black Duck SCA connection.
5. Configure Detect arguments.
6. Run pipeline and invoke scan.
7. Examine the analysis results.
