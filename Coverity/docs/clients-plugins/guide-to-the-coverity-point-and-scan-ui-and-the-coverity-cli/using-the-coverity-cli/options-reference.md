---
title: "Options reference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-reference.html"
content_id: "CIG8EIce~MZDWBWBCk0voQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:00.034041+00:00"
---

# Options reference

The Coverity CLI accepts a configuration file in either YAML or JSON format that defines
configuration settings needed to tell the CLI what to do. The Coverity CLI configuration
file is hierarchical in nature, with categories or keys being nested inside other
categories, as follows:

```
Configuration
    Version
    Capture
        Build
    Analyze
        Checkers
        Coding Standards
    Commit
    Caching
```

The following table identifies categories of configuration options.

| Key | Type | Description |
| --- | --- | --- |
| `version` | integer | Specifies the version of the configuration file in use. This value is used to determine compatibility with the version of Coverity Analysis in use.  Default: `1` |
| `capture` | Capture configuration | Specifies how the project should be captured. If not specified, the project will be captured using automatic capture. |
| `analyze` | Analysis configuration | Specifies how the project should be analyzed. If not specified, the project will be analyzed using a default set of analysis options.  To perform an analysis in the Cloud, you need to configure options in a Coverity configuration file.  Note: For options and information on how to perform an analysis in the cloud, refer to "Performing an analysis in a Coverity cloud deployment" in the Coverity Analysis 2026.6.0 User and Administrator Guide and to the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. |
| `commit` | Commit configuration | **Required:** Specifies where the analysis results should be sent. |
| `caching` | Caching configuration | Specifies capture and analysis, or scan-use caching. |

The Coverity CLI `analyze`, `capture`,
`scan`, `setup`, `list` and
`commit` subcommands accept a configuration file specified with the
`-c` or `--config` options followed by the path to
the configuration file. The configuration file specified must have one of the following
extensions: .yaml, .yml, .json.

If no configuration file is specified on the command-line, the CLI will look for the
following files in the project directory in the following order:

1. coverity.yaml
2. coverity.yml
3. coverity.json

The first file found will be used as the configuration file for the Coverity CLI.
If there are multiple candidate configuration files, the Coverity CLI will warn the user of
this condition and report which files were ignored.
Capture configuration, Analysis configuration,
Commit configuration, and Caching configuration
describe the schema for the configuration.

Note:
If you are performing an analysis in the Cloud, refer also to
"Performing an analysis in a Coverity cloud deployment" and to the
Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for Cloud-specific information.

In this section:

- Capture configuration
- Analysis configuration
- Commit configuration
- Caching configuration
