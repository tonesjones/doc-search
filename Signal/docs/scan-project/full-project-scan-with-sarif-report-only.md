---
title: "Scan a full project"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/scan-a-full-project.html"
content_id: "L5rw5N0dHn89RZbP5o6wpA"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:50.232204+00:00"
---

# Scan a full project

How to set up and execute a code scan in the entire source code in a repository using Bridge CLI and Signal, with the results generated in a SARIF report. If desired, the results can later be uploaded to Polaris. This task is for Bridge CLI users. For more details, see Using Bridge CLI with Signal.

## Contents

- Scan a full project with a local SARIF report
- Scan a full project and send results to Polaris

## Scan a full project with a local SARIF report

**Prerequisites:**

- API Key for the LLM that will be used by Signal.
- A **Signal Enterprise** subscription.
- Bridge CLI is installed and available on the system PATH.
- Access to a project directory containing the files to scan.

Follow the steps to run a full project scan with a local SARIF report:

1. Download the latest version of Bridge, if you haven't installed it already. To download, see [Bridge Binaries Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries).

   Important: Choose **bridge-cli-bundle,** which also installs Signal.
2. Add Bridge CLI to your `$PATH` variable.
3. Set the following environment variables.

   ```
   export BRIDGE_SIGNAL_LLM_KEY=<LLM_API_KEY>
   ```
4. From the root level of the project, run the following.

   ```
   bridge-cli --stage signal \
     signal.mode=PROJECT \
     signal.exclude="src/dev/resources/generated"
   ```

   About this example:

   - The results of your scan will be available in a SARIF report, stored at the location you provide for the `signal.reportFile` property. In this example it is: `.bridge/signal-controller/results.sarif`.
   - Setting `signal.mode` as "`PROJECT`" tells Signal to scan the entire project.
   - You can use the `exclude` property to indicate directories that Signal should not scan.
   - An exit code of `0` will be issued to signal success.
5. If the scan succeeds, the SARIF report will be found at the location you indicated.

If the scan fails, check if you provided a valid LLM API key and if you met all the prerequisites for each task. For additional support, see Bridge Reference Guide.

## Scan a full project and send results to Polaris

**Prerequisites:**

- Bridge CLI is installed and available on the system PATH.
- Access to a project directory containing the files to scan.
- An API Key for the LLM that will be used by Signal.
- A **Signal Enterprise** subscription.
- A Polaris token to be used by Signal. For more details, see [How to make an access token in Polaris](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/make-an-access-token.html).
- An Application established in Polaris configured with the **External Analysis** entitlement to receive the results of your scan. For the SE tenant, switch your application to a concurrent subscription. For more details, see [How to import result from third-party tools in Polaris](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/import-results-from-third-party-tools-limited-availability-.html).

Follow the steps to run a full project scan and send the results to Polaris:

1. Download the latest version of Bridge, if you haven't already installed it, see [Bridge Binaries Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries).

   Important: Choose **bridge-cli-bundle,** which also installs Signal.
2. Add Bridge to your `$PATH` variable.
3. Set the following environment variables.

   ```
   export BRIDGE_POLARIS_SERVERURL=<POLARIS_SERVER_URL>
   export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_TOKEN>
   export BRIDGE_SIGNAL_LLM_KEY=<LLM_API_KEY>
   ```
4. Insert your Polaris URL and tokens where there are placeholders in the example. These are required when uploading results to Polaris.

   Note: It's safer to store your access tokens as environment variables, as opposed to providing them in the command line or in your config file.
5. Run the following code from the root level of the project:

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

   About this example:
   - Replace the placeholders with the names of your Polaris Application, Project, and Branch; all three are required when `signal.platform` is set to `polaris`. If they don’t exist, the Project and Branch will be created with the provided names.
   - A SARIF report file will be generated at `.bridge/signal-controller/results.sarif` within the current working directory where Bridge CLI was called from.
   - The SARIF report will be uploaded to Polaris and a URL to the uploaded report will be returned.
   - An exit code of `0` will be issued to signal success.

If the scan fails, check if you provided a valid LLM API key and if you met all the prerequisites for each task. For additional support, see Bridge Reference Guide.
