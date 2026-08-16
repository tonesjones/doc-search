---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "FD3edvzYiCRL1HDb6dFoNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:21.807261+00:00"
---

# Options

--dir <dir_name>
:   The name of the folder where `cov-run-sigma` will store the
    output after running Sigma. This intermediate directory will not be deleted,
    because it will be used to commit results to Coverity Connect.

--sigma-binary-path <sigma>
:   The path of the Sigma binary that `cov-run-sigma` is expected to run.

--coverity-config <coverity_config.xml>
:   Use the specified configuration file, which will be passed to Sigma when it is invoked.

--root-config
:   Use the configuration file stored in the root of the source code. When
    analyzing a directory, files will include `coverity.yaml`,
    `coverity.yml` and `coverity.json`.

--enable-telemetry
:   This option enables telemetry, and data will be stored in a default location.

--polaris-classic
:   Include this option when `cov-run-sigma` is being invoked in Polaris classic.

--metrics-file <metrics_file>
:   Enable metrics to be generated and store them in the specified file.

--log-file <log_file>
:   Enable logging and store the logs in the specified file.

--project-dir <project_dir>
:   Path to user source code for Sigma to analyze.
