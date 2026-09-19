---
title: "Scan a full project with Black Duck Signal"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/scan-a-full-project-with-black-duck-signal.html"
content_id: "xEDE0q25HmGtsyKiKJDP4g"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:53.677032+00:00"
---

# Scan a full project with Black Duck Signal

Bridge CLI can be used to run Signal to perform an AI assessment of all files in a project directory, with findings uploaded to Polaris .

Black Duck Signal provides a PROJECT scan mode that performs an AI assessment of every file in the project directory. The scanned files and folders can be controlled an optional exclude path list. When configured with an upload platform, scan findings are uploaded to the configured platform on scan completion. Currently, Polaris is supported as an upload platform.

## Run full project scan without upload

**Prerequisites**

The following prerequisites are required:

- Bridge CLI is installed and available on the system PATH.
- Access to a project directory containing the files to scan.
- A valid Signal LLM API key.

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
     signal.mode=PROJECT \
     signal.exclude="src/dev/resources/generated"
   ```

   Bridge will use the configuration to start Signal to perform an AI assessment of all files and folders in the project directory. When the scan has completed, the following outputs will be provided:

   - A SARIF report file will be generated at `.bridge/signal-controller/results.sarif` within the current working directory where Bridge CLI was called from.
   - An exit code of `0` will be issued to signal success.

## Run full project scan with upload

**Prerequisites**

The following prerequisites are required:

- Bridge CLI is installed and available on the system PATH.
- Access to a project directory containing the files to scan.
- A valid Signal LLM API key.
- A valid Polaris access token and server URL.
- A Polaris application configured with the **External Analysis** entitlement.

**Instructions**

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
     signal.mode=PROJECT \
     signal.exclude="src/dev/resources/generated" \
     polaris.serverUrl=<POLARIS_SERVER_URL> \
     polaris.accessToken=<POLARIS_ACCESS_TOKEN> \
     polaris.application.name=<APPLICATION_NAME> \
     polaris.project.name=<PROJECT_NAME> \
     polaris.branch.name=<BRANCH_NAME>
   ```

   Bridge will use the configuration to start Signal to perform an AI assessment of all files and folders in the project directory. When the scan has completed, the following outputs will be provided:

   - A SARIF report file will be generated at `.bridge/signal-controller/results.sarif` within the current working directory where Bridge CLI was called from.
   - The SARIF report will be uploaded to Polaris and a URL to the uploaded report will be returned.
   - An exit code of `0` will be issued to signal success.

## Signal CLI commands quick reference

The following parameters enable further customization. Use the related links information section to access the reference guide for the commands.

**General parameters**

| CLI Argument | Description |
| --- | --- |
| `project.directory` | By default Black Duck Signal scans the files and folders in the current working directory. This behavior can be overridden by specifying the absolute path for the `project.directory` argument. |
| `signal.version` | By default Bridge downloads the latest version of Signal from the Black Duck repository. This behavior can be overridden by specifying a version string, e.g. `0.2.9`. |
| `signal.args` | Specify additional arguments to be passed directly to Signal , e.g. `"--dataflow true --log-level debug"`. |
| `signal.exclude` | Comma separated list of file or directory paths (relative to `project.directory`) to exclude from the scan, in any mode. e.g. `"tests/,examples/"`. |

**Related information**  

- [Signal Documentation](https://docs.blackduck.com/access?ft:originId=45e1f8ccc6ea016432347cf25486b012/2979c4f15f66905a89407ab942b98586.topic)

**Related information**  

- Black Duck Signal reference guide
