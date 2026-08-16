---
title: "Customizing Check Attributes"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/customizing-check-attributes.html"
content_id: "MkuiLoCE_GTAw91SvLxuPw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:10.754291+00:00"
---

# Customizing Check Attributes

Note: The customizing check attributes feature is deprecated and will be removed in a future release.

Note: Configuring Sigma with a `.sigma-config.yml`
file is deprecated. For more information, see Configuring Sigma with coverity.yml.

Sigma supports an advanced configuration feature to customize the following check
attributes:

- Summary
- Description
- Remediation
- Severity
- Likelihood
- Default Likelihood
- Impact
- Default impact

You can override all these values using the `check_metadata_overrides` field of
the Sigma configuration file.

This section explains how these values are used and how you customize these values.

- The Summary, Description, and Remediation fields allow you to redefine the default values for
  these fields. When an issue is found by a check, it will use the values you have
  defined for these fields.
- The Likelihood, Default Likelihood, Impact, and Default Impact fields are used to calculate
  Sigma severity levels. For more information on overriding these values, see Overriding Severity Levels.

  Customizing the severity level of your checks
  determines how GitHub or GitLab renders analysis results as Code Scanning Alerts
  and GitLab Security Vulnerabilities.

## Customizing with CI/CD Pipelines

To customize check attributes using a CI/CD pipeline, create a Sigma configuration file named
.sigma-config.yml and check it into your project's root
directory in GitHub or GitLab. By default, Sigma will look for a configuration file
named .sigma-config.yml in the directory where Sigma is being
run. For CI/CD systems, this is typically the project root directory since the
project source needs to be pulled to the system running the CI/CD job.

The configuration defined in the configuration file will control how Sigma executes.
You can change the config files Sigma uses via command line options.

## Basic Workflow for Customizing Attributes

The basic workflow for overriding default attribute values is:

1. Run sigma on your source code. If issues are found, the check that reported
   the issue will be named in the Sigma output. This gives you the Summary,
   Description, and Remediation values.
2. Run the following command to list all checkers and associated checks, including information about
   languages, CWEs, severity and enablement:

   ```
   sigma checkers
   ```

   This is useful if you need to override severity levels.

   See The checkers Subcommand for more details.
3. Create or edit a configuration file to specify desired values for selected attributes for one or
   more checks.

   See Creating a Default Configuration for information about generating the
   default configuration.
