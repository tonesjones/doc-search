---
title: "Centralize your Coverity configuration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/centralize-your-coverity-configuration.html"
content_id: "xIT7D7YHNn_8euJvc~aj3Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.215331+00:00"
content_hash: "f73f9b476d636ba0df735fa79af126d1f904894d920362cf7bb1069047847fa5"
---

# Centralize your Coverity configuration

Learn how to set up a central Coverity configuration file for applications, projects, and branches in your portfolio.

Coverity configuration gives security teams a central place to define and enforce Coverity rule profiles for static analysis across the organization. Instead of maintaining per-repository YAML files, you upload a configuration file to Polaris once and it is automatically applied at scan time — no developer intervention required.

You can assign configuration files at the organization, application, project, or branch level. Lower-level configurations take precedence over higher-level ones. For example, an application-level configuration overrides the organization-level configuration for that application's scans.

Important: In the current release, only Organization Administrators can upload and manage Coverity configuration files.

## Coverity configuration inheritance

The configuration file assigned at the organization level serves as the default for all applications, projects, and branches in your portfolio. A configuration assigned at a lower level takes precedence:

- An application-level configuration overrides the organization-level configuration.
- A project-level configuration overrides both application and organization-level configurations.
- A branch-level configuration overrides project, application, and organization-level configurations.

When a configuration is applied at the application, project, or branch level, Modified appears in the Coverity Configuration panel, indicating that the local configuration overrides the one available at a higher level in the hierarchy. Select Reset to remove the local configuration and revert to the inherited configuration.

## Configuration resolution priority

When a scan runs, Polaris resolves the Coverity configuration in the following order:

1. A user-specified YAML file passed directly to the scan
2. The centrally managed configuration file from Polaris
3. CLI or analyzer defaults

## Override the Coverity configuration set in Polaris

You can override the applicable centrally managed configuration when you start tests with the Bridge CLI. To use a local configuration file instead of the applicable centrally managed one, you must:

- Include the local configuration file with the source files you wish to test.
- Specify the local configuration file in the command used to run the test (using `coverity.config.path`).

  See [Complete list of Bridge arguments](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/104e9b8ad79809821c6b1e50bb52508d.topic) for more information.
