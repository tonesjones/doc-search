---
title: "Creating a Default Configuration"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/creating-a-default-configuration.html"
content_id: "tkabxzKHuOjpgta8d32v8Q"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:10.114481+00:00"
---

# Creating a Default Configuration

Note: Configuring Sigma with a `.sigma-config.yml`
file is deprecated. For more information, see Configuring Sigma with coverity.yml.

In case you want to configure an option where the default is not acceptable and you need
help understanding the structure of the configuration file, you could use the
`sigma config create-default` command. This command provides you with
a sample configuration file that includes all possible options so that you can directly
edit it, instead of creating a configuration file from scratch.

The command:

```
sigma config create-default
```

creates a file named `.sigma-config.yml` in the directory where you ran
the sigma config command. The file will have the following
contents:

```
global:
  config: []
  policy: ~
  working_dir: ".sigma-dir"
analyze:
  disable_checkers: []
  check_metadata_overrides: []
  format: JSON
  output: sigma-results.json
  ignore_scm: false
  follow_symlinks: false
  ignore_hidden_files: false
  make_paths_absolute: false
  repo_root: ~
  paths: []
```

As specified in the default configuration:

- The default working directory is `.sigma-dir`
- The `analyze` command:

  - scans the checks that are enabled by default
  - uses JSON for the output format
  - places output in the `sigma-results.json` file
  - explores the `.git` directory and does not read the
    `.gitignore` file, which contains a list of paths to
    other files that git should ignore. If `ignore_scm` is
    `false` (the default), Sigma parses the
    `.gitignore` file, and will not analyze files that
    are mentioned in the `.gitignore` list.
  - scans hidden files
  - follows symlinks in files for additional scanning
  - uses relative paths

For information about customizing check attributes using the
`check_metadata_overrides` field, see Customizing Check Attributes.
