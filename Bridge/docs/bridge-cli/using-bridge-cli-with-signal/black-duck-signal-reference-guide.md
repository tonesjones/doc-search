---
title: "Black Duck Signal reference guide"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/black-duck-signal-reference-guide.html"
content_id: "umhhqHihgvnCKpSEJNC2ng"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:56.281847+00:00"
---

# Black Duck Signal reference guide

Reference guide for configuring Black Duck Signal

## Signal parameters

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| LLM API key | `signal.llm.key` | `BRIDGE_SIGNAL_LLM_KEY` | Yes | API key or token for the configured LLM endpoint. Bridge passes this directly to `--llm-key`. The key must be valid for the chosen LLM endpoint. |
| Project directory | `project.directory` | `BRIDGE_SIGNAL_PROJECT_DIRECTORY` | No | Absolute path to the project root that Bridge uses as the working directory and scan target. Must point to the root of the source tree, and to a Git repository when using diff modes.  **Example**: `/home/dev/workspace/my-service`  If no value is provided, Bridge CLI  uses the current directory as the project directory. |
| Signal version | `signal.version` | `BRIDGE_SIGNAL_VERSION` | No | Specific Signal version to install and invoke. If omitted, Bridge resolves and downloads the latest supported Signal version for the current OS and architecture.  **Example**: `"0.2.9"` |
| Scan mode | `signal.mode` | `BRIDGE_SIGNAL_SCAN_MODE` | No | Use to specify a scan mode:  - `FILES` : Direct selection via   `signal.include` and   `signal.exclude`. - `UNCOMMITTED` : Git diff of uncommitted   and staged changes. Signal generates the patch   files. - `REFERENCE`: Git diff between the current   branch and a reference branch. Signal generates patch   files based on the values provided and executes scans. - `PROJECT:`Performs an AI assessment of   files in a project directory and uploads scan findings   to a configured platform on completion. Currently, Polaris is supported as an   upload platform.   **Default**: `FILES` and uses the values provided for `signal.include`.  For `UNCOMMITTED` and `REFERENCE`, Bridge considers the changes under `project.directory`. |
| Exclude paths | `signal.exclude` | `BRIDGE_SIGNAL_EXCLUDE` | No | Comma separated list of file or directory paths (relative to `project.directory`) to exclude from the scan, in any mode. **Example** : `"tests/,examples/"` |
| SARIF Report File Path | `signal.reportFile` | `BRIDGE_SIGNAL_REPORT_FILE` | No | Optional custom path for the Signal SARIF report file. When provided, Bridge passes `--report-file "<signal.reportFile>"` and returns the same value on completion. **Default**: Uses Signal default, `results.sarif`). |
| Free-form Signal arguments | `signal.args` | `BRIDGE_SIGNAL_ARGS` | No | Additional Signal CLI flags appended as‑is. Must not include `--include-paths` or `--report-file`; Bridge derives diff or patch handling and report path.  Suitable for tuning analysis features such as `--dataflow`, `--crypto`, or log level.  **Example**: `"--dataflow true --log-level debug"` |

## FILE mode parameters

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Include paths | `signal.include` | `BRIDGE_SIGNAL_INCLUDE` | Yes | Comma‑separated list of file or directory paths (relative to `project.directory`) to include in `FILES` mode. If empty or omitted in `FILES` mode, Bridge returns an error and requires a value.  **Example**: `"src/service/foo.py,src/service/bar.py"` |

## UNCOMMITTED mode parameters

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Git execution path | `signal.git.execution.path` | `BRIDGE_SIGNAL_GIT_EXECUTION_PATH` | No | Absolute path to Git binary executable. **Default:** Uses system path to locate Git executable binary. |

## REFERENCE mode parameters

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Reference branch | `signal.git.ref` | `BRIDGE_SIGNAL_GIT_REF` | Yes | Reference branch name for Git diff comparison . **Examples**: `"main"`, `"origin/main"` |
| Git execution path | `signal.git.execution.path` | `BRIDGE_SIGNAL_EXECUTION_PATH` | No | Absolute path to Git binary executable. **Default:**Uses system path to locate Git executable binary. |

## PROJECT mode parameters

Project mode parameters control where Signal uploads results. This section summarizes the
available platforms and their configuration parameters.

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Platform | `signal.platform` | `BRIDGE_SIGNAL_PLATFORM` | No | Indicates the platform to upload results to. Use Polaris. Note: If `signal.platform` is not used for a project scan then Bridge will still run the scan and will exit without attempting to upload results. |
| Polaris URL | `polaris.serverUrl` | `BRIDGE_POLARIS_SERVERURL` | Yes | The Polaris URL for uploading results. |
| Polaris token | `polaris.accessToken` | `BRIDGE_POLARIS_ACCESSTOKEN` | Yes | The Polaris access token. |
| Application name | `polaris.application.name` | `BRIDGE_POLARIS_APPLICATION_NAME` | Yes | Polaris application name. |
| Project name | `polaris.project.name` | `BRIDGE_POLARIS_PROJECT_NAME` | Yes | Polaris project name. |
| Branch name | `polaris.branch.name` | `BRIDGE_POLARIS_BRANCH_NAME` | Yes | Polaris branch name. |

## Signal outputs

When a client invokes `bridge --stage signal`, Bridge guarantees the following outputs in the workflow context and/or
client-facing response.

| Field | JSON Field | Notes |
| --- | --- | --- |
| Signal exit code | `signal.exitCode` | Numeric process exit code from the Signal binary (0=success, non-zero=failure). Clients should treat non-zero values as a scan failure and surface the underlying error or logs as appropriate. |
| SARIF report file path | `signal.report.output` | Absolute or relative path to the generated SARIF security report file. If the `signal.reportFile` argument is provided, the same path is returned. Otherwise, the Signal controller assigns a default path (`results.sarif`) before execution and returns it. This path serves as the main artifact for downstream consumers like Code Sight or CI. **Default**: results.sarif.json |
| Report URL | `signal.report.url` | This is the URL for the uploaded results file. |
| Upload successul | `signal.report.uploadSuccessful` | Boolean flag indicating whether the upload of the SARIF report to the configured platform completed successfully. When `true`, the artifact was uploaded and a valid `signal.report.url` is available; `false` means the upload failed and clients should not rely on `signal.report.url`. |
