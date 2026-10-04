---
title: "Scan uncommitted changes"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/scan-uncommitted-changes.html"
content_id: "XBRDb3XpMO6IjYIYjx2wZA"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:50.187447+00:00"
---

# Scan uncommitted changes

Bridge CLI can be used to run Signal to perform a diff scan of uncommitted, tracked files in a Git project directory. This task is for Bridge CLI users. For more details, see [Bridge CLI Overview](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-product-overview.html).

Black Duck Signal provides the uncommitted scan mode to perform a diff scan of uncommitted tracked files. The Signal adapter configures Git diff-based analysis for the Git repository located at the project directory.

## Prerequisites

The following prerequisites are required to run a diff scan:

- Bridge CLI is installed and available on the system PATH.
- Access to a Git project directory.
- There are changes in uncommitted, tracked files.
- A valid Signal LLM API key.
- A Signal Enterprise or Developer subscription.

Follow the steps to run a diff scan:

1. Download the latest version of Bridge CLI, if you haven't installed it already. To download, see [Bridge Binaries Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries).
2. Add Bridge CLI to your `$PATH` variable.
3. Save a valid LLM API key in the `BRIDGE_SIGNAL_LLM_KEY` environment variable.

   ```
   export BRIDGE_SIGNAL_LLM_KEY=<LLM_API_KEY>
   ```
4. Run the Bridge CLI Signal workflow at the root level of your project.

   ```
   bridge-cli --stage signal \
     signal.mode=UNCOMMITTED
   ```

   Bridge will use the configuration to start Signal to perform a diff scan of uncommitted changes. When the scan has completed, the following outputs will be provided:

   - A SARIF report file will be generated at `.bridge/signal-controller/results.sarif` within the current working directory where Bridge CLI was called from.
   - An exit code of `0` will be issued to signal success.

## Signal CLI commands quick reference

The following parameters enable further customization. Use the related links information section to access the reference guide for the commands. For additional support, see Bridge Reference Guide.

| CLI Argument | Description |
| --- | --- |
| `project.directory` | By default Black Duck Signal scans the files and folders in the current working directory. This behavior can be overridden by specifying the absolute path for the `project.directory` argument. |
| `signal.version` | By default Bridge downloads the latest version of Signal from the Black Duck repository. This behavior can be overridden by specifying a version string, e.g. `0.2.9`. |
| `signal.args` | Specify additional arguments to be passed directly to Signal, e.g. `"--dataflow true --log-level debug"`. |
| `signal.git.execution.path` | By default Signal uses the `Git` binary accessible from the system PATH. This behavior can be overridden by specifying the absolute path to the Git binary using the `signal.git.execution.path` argument. |
