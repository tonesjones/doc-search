---
title: "Using the Configuration File to Specify Overrides"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-the-configuration-file-to-specify-overrides.html"
content_id: "gVS4N_yImYcQ_x4b364WcQ"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:12.115012+00:00"
---

# Using the Configuration File to Specify Overrides

Note: Configuring Sigma with a `.sigma-config.yml` file
is deprecated. For more information, see Configuring
Sigma with coverity.yml.

When you create or update the configuration file, you will be using the
`check_metadata_overrides` field to specify overrides.

Override information takes the following form:

```
global:
  config: []
  policy: ".sigma-policy.yml"
  working_dir: ".sigma-dir"
analyze:
  disable_checkers: []
  check_metadata_overrides:
      - name: "android_manifest_backups_allowed"
        severity: "High"
        impact: "Low"
        default_likelihood: "Medium"
      - name: "aws_s3_access_logging_disabled"
        severity: "High"
        summary: "This is a custom summary of aws_s3_access_logging_disabled."
        description: "This is a custom description of aws_s3_access_logging_disabled."
        remediation: "This is a custom remediation of aws_s3_access_logging_disabled."
  format: JSON
  output: sigma-results.json
  ignore_scm: false
  follow_symlinks: false
  ignore_hidden_files: false
  make_paths_absolute: false
  repo_root: ~
  paths: []
```

Note:

- The `text` field can be any UTF-8 string/text, which means that
  characters like 理论知 are supported.
- The `summary` entry will be truncated if it exceeds 100
  characters.
- All `check_metadata_overrides` entries are optional, except for
  `name`. This means that the following override information
  would be valid:

  ```
     - name: "<check_name3>"
       summary: "<text>"
  ```

Based on the information you got from scanning your code and examining the checks involved, you
must provide override information in the format shown above.

In the following example, severity levels are defined for two checks and summary information is
redefined for the `aws_s3_access_logging_disabled` check.

```
  config: []
  policy: ".sigma-policy.yml"
  timeout: 0
  working_dir: ".sigma-dir"
analyze:
  disable_checkers: []
  check_metadata_overrides:
      - name: "android_manifest_backups_allowed"
        severity: "High"
		impact: "Low"
		default_likelihood: "Medium"
      - name: "aws_s3_access_logging_disabled"
        severity: "High"
        summary: "This is a custom summary of aws_s3_access_logging_disabled."
		description: "This is a custom description of aws_s3_access_logging_disabled."
        remediation: "This is a custom remediation of aws_s3_access_logging_disabled."
  format: JSON
  output: sigma-results.json
  ignore_scm: false
  follow_symlinks: false
  ignore_hidden_files: false
  input: ~
  make_paths_absolute: false
  repo_root: ~
  paths: []
```

## Using Multiple Configuration Files

You can specify the `check_metadata_overrides` in multiple Sigma configuration
files and include each configuration file with the `--config` option.
Sigma will merge the `check_metadata_overrides` configuration into
one list of overrides to use during analysis.

If the same check name is found in multiple files, the multiple attributes will be merged into
one. Different attributes of the same check can be defined in different
configurations.

Note:

- You can define different attributes for the same check in different configurations.
- Any duplicate overrides of the same attribute are logged as a configuration
  validation error.

  The error will look like
  this:

  ```
  Duplicate severity override "low" found for checker aws_s3_access_logging_disabled.
   Checker aws_s3_access_logging_disabled already configured with severity override "high".
  Using severity override "low".
  ```
- For any attribute, Sigma will use the last provided value in the
  configurations when it runs.
