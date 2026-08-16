---
title: "Connect a Polaris project to a repository in your SCM"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/connect-a-polaris-project-to-a-repository-in-your-scm.html"
content_id: "g4nWPm2JJwyMlAI6Aw2PHA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:18.519836+00:00"
content_hash: "c6b2ef0248f6af002705fd96920a3a1d40ce5f02a6d843dabdf1a6acb133cd8c"
---

# Connect a Polaris project to a repository in your SCM

Set up an SCM integration to connect a project in Polaris to a repository in Azure DevOps, Bitbucket, GitHub, or GitLab.

## Overview

SCM integrations make it easy to test repositories in your organization with minimal configuration.

Important: When you test a project connected to a repository via an SCM integration, SAST and SCA tests run in buildless mode. If source files in the repository are written in a compiled language, you can achieve more accurate results using the Bridge CLI (or associated plug-ins). See [Polaris continuous integration documentation](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/cd6ad452381a0099cb4d143a5cad6fba.topic) for more information.

### One project, one repository

Connecting multiple repositories to a single Polaris project is not supported. Within an application, you cannot connect more than one project to the same repository.

### Branches

The default branch in your SCM repository becomes the default branch in your Polaris project. To test other branches in your SCM repository, you need to import them. See Add a branch to a project.

## Supported SCMs

You can connect Polaris projects to repositories in the following Source Code Management (SCM) systems:

- Azure Repos
- Bitbucket Cloud
- Bitbucket Data Center
- GitHub and GitHub Enterprise Cloud
- GitHub Enterprise Server
- GitLab SaaS
- GitLab Self-Managed

See Supported Source Code Management (SCM) systems for more information.

## Test a repository's source files

Once you set up an SCM integration, you can test a repository's source files on demand, or automatically (on a daily or weekly basis). See [How to test from the web UI](how-to-test-from-the-web-ui.md) and Test scheduling policies for more information.

## Modify an SCM integration

To modify an SCM integration, follow these steps:

Note: If the access token you use for an SCM integration expires, generate a new token and follow these steps to update it.

1. In Polaris, open the project you wish to modify (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Update the integration, as required.
4. Enter a valid Repository Access Token and select Test your connection.
5. Select Save.

   You cannot save changes until the connection is tested successfully.

## Remove an SCM integration

When you remove an SCM integration, any event-based test automation (including the pull request comments feature) and SCM auto-onboarding configured for the project will stop working.

To remove an SCM integration, follow these steps:

1. In Polaris, open the project you wish to modify (go to Portfolio, select an application, and select a project).
2. Go to Settings > Integrations.
3. Select Remove Configuration.

   The Remove Configuration button is only available if an SCM integration has already been set up.
4. Select Save.
