---
title: "Plug-in integrations"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/plug-in-integrations.html"
content_id: "a7hnddTV0BsvzqhB80rRwA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:30.904491+00:00"
---

# Plug-in integrations

Plug-ins are the easiest way to integrate testing into your CI/CD pipeline. Choose from
CI/CD plug-in integrations derived from either of the CLI clients above: **Detect**
or the **Bridge CLI**.

## Detect-based CLI plug-ins

**Jenkins**

The [Detect Extension for Jenkins](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/00d7d4047f7b35cd1bfb5ffe56af9889.topic) enables you
to install and run Black Duck Detect in your Jenkins instance.

Capabilities include:

- Performing compositional analysis and functioning as a Black Duck intelligent
  scan client.
- Sending scan results to your Black Duck SCA server, which generates risk
  analysis when identifying open source components, licenses, and security
  vulnerabilities.
- Running Detect as either of the following:

  - A post-build action in a Jenkins Freestyle job.
  - Pipeline step using a Pipeline script in a Pipeline job.

**Azure**

The [Detect Extension for Azure DevOps](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/c6e07518715e7effa81505181332d445.topic) is
designed to integrate Black Duck Detect seamlessly into Azure DevOps build and
release pipelines.

It includes the ability to:

- Run a component scan in an Azure DevOps job.
- Create projects and releases in Black Duck SCA through the Azure DevOps
  job.

- Make results available on the Black Duck SCA server.

**GitHub**

The [Detect GitHub Action](https://github.com/synopsys-sig/detect-action) plug-in integrates Black Duck
Detect into GitHub action workflows.

Capabilities include all of the following:

- Run a component scan in a GitHub workflow.
- Upload results to a project in Black Duck SCA.
- Configure Detect in either of two modes:

  - Rapid scan mode to get detailed Black Duck policy reports (default
    behavior)
  - Intelligent scan mode to upload your data into Black Duck for more
    detailed analysis.

Note: As of October 2024, we recommend using the newer, Bridge-based GitHub
Action for creating new pipelines, rather than Detect GitHub Action.

## Bridge-based CI Plug-ins

Our latest plug-ins are built with the [Bridge CLI Client](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/9aea3062cf34aeb53b068f901c9eb5c2.topic) under the hood, so you
get the same benefits without writing the code.

Capabilities include:

- SAST and SCA scanning
- Scan in synchronous or asynchronous (non-blocking) mode
- Scan whenever new code is merged to a branch
- Scan whenever a pull request is created/updated
- Decorate PRs with comments
- Create Fix PRs (Black Duck SCA only)
- Generates a SARIF file
- Post results to SCM (GitHub advanced security)
- Post results to any supported server (see the list of products above).

- Make issues available in your instance of Black Duck SCA, Coverity, Polaris,
  or SRM.
- Fail the build in your CI system when a high-severity issue is found.

Bridge plug-ins for Black Duck are available on the following platforms:

- [Azure](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/73bd2c59a319b3d55d1cb459e2efb50d.topic)
- [GitHub](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/3db8f86f848b66bc21316830785b922e.topic)
- [GitLab](https://docs.blackduck.com/access?ft:originId=28e7b79af95c6aa1ffa2bd837a846d8b/949207ee3f3436bf9c902370dbac576e.topic)
- [Jenkins](https://docs.blackduck.com/access?ft:originId=58f48ad4c89c53317cf57f364d022fb8/c6dc98c86dc2c606ffc19b23cb23fe0b.topic)
