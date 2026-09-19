---
title: "Perform a diff scan with Black Duck Signal"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/perform-a-diff-scan-with-black-duck-signal.html"
content_id: "oW33tu8l5H9~3rummnuG4A"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:54.302108+00:00"
---

# Perform a diff scan with Black Duck Signal

Bridge CLI can be used to run Signal to perform a diff scan of uncommitted, tracked files in a Git project directory.

Black Duck Signal provides the `UNCOMMITTED` scan mode to perform a diff scan of uncommitted tracked files. The Signal adapter configures Git diff-based analysis for the Git repository located at the project directory.

## Prerequisites

The following prerequisites are required to run a diff scan:

- Bridge CLI is installed and available on the system PATH.
- Access to a `Git` project directory.
- There are changes in uncommitted, tracked files.
- A valid Signal LLM API key.

## Running a diff scan

1. Download the latest version of Bridge, if you haven't installed it already.

   ```
   https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge
   ```
2. Add Bridge to your `$PATH` variable.
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

The following parameters enable further customization. Use the related links information section to access the reference guide for the commands.

| CLI Argument | Description |
| --- | --- |
| `project.directory` | By default Black Duck Signal scans the files and folders in the current working directory. This behavior can be overridden by specifying the absolute path for the `project.directory` argument. |
| `signal.version` | By default Bridge downloads the latest version of Signal from the Black Duck repository. This behavior can be overridden by specifying a version string, e.g. `0.2.9`. |
| `signal.args` | Specify additional arguments to be passed directly to Signal, e.g. `"--dataflow true --log-level debug"`. |
| `signal.git.execution.path` | By default Signal uses the `Git` binary accessible from the system PATH. This behavior can be overridden by specifying the absolute path to the Git binary using the `signal.git.execution.path` argument. |

**Related information**  

- [Signal Documentation](https://docs.blackduck.com/access?ft:originId=45e1f8ccc6ea016432347cf25486b012/2979c4f15f66905a89407ab942b98586.topic)

**Related information**  

- Perform a diff scan against a reference branch with Black Duck Signal
- Scan local files with Black Duck Signal
- Black Duck Signal reference guide
