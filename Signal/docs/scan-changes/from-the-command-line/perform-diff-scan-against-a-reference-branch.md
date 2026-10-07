---
title: "Scan changes against a reference branch"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/scan-changes-against-a-reference-branch.html"
content_id: "i_KFKAGFq72wFejG_0mdFw"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:50.205941+00:00"
---

# Scan changes against a reference branch

Bridge CLI can be used to run Signal to perform an AI assessment of changes in the current branch relative to a selected reference branch within a Git project directory. This task is for Bridge CLI users. For more details, see [Bridge CLI Overview](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-product-overview.html).

Black Duck Signal provides a reference scan mode that compares the current branch against a specified reference branch in the project's Git directory. In this mode, the Signal adapter uses a diff-based analysis to evaluate the changes relative to the chosen reference branch. Only your latest changes in tracked files are scanned. For additional support, see Bridge Reference Guide.

## Prerequisites

- Bridge CLI is installed and available on the system PATH.
- Access to a Git project directory.
- The branch to scan exists and is resolvable by Git.
- A valid Signal LLM API key.
- A Signal Enterprise or Developer subscription.

Follow the steps to run a diff branch scan:

1. Download the latest version of Bridge, if you haven't installed it already. To download, see [Bridge Binaries Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries).
2. Add Bridge CLI to your `$PATH` variable.
3. Save a valid LLM API key in the `BRIDGE_SIGNAL_LLM_KEY` environment variable.

   ```
   export BRIDGE_SIGNAL_LLM_KEY=<LLM_API_KEY>
   ```
4. Run the Bridge CLI Signal workflow at the root level of your project.

   ```
   bridge-cli --stage signal \
     signal.mode=REFERENCE \
     signal.git.ref="origin/main"
   ```

   Bridge will use the configuration to start Signal to perform an AI assessment of the code changes in the project directory for the specific branch. When the scan has completed, the following outputs will be provided:

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
