---
title: "Signal Reference Guide"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-reference-guide.html"
content_id: "VQ8en5ZARi3SiBDVn4bs7g"
version: "latest"
section: "Signal Reference Guide"
scraped_at: "2026-10-04T23:27:49.956655+00:00"
---

# Signal Reference Guide

## Contents

- Signal Flags
- [SCAN] Flags
- BYOLLM Flags
  - SDK env-var fallbacks for BYOLLM
  - BYOLLM Agents
- Signal config file
- Signal parameters related to Bridge CLI
  - FILE mode parameters
  - UNCOMMITTED mode parameters
  - REFERENCE mode parameters
  - PROJECT mode parameters
  - Signal outputs
  - Polaris Flags

## Signal Flags

Description of available Signal flags. Any CLI flag can be set here as its `snake_case` equivalent (`--log-file` → `log_file`). `getConfig` merges the section straight into `config.SCAN` after applying defaults.

| CLI option | Type | Description |
| --- | --- | --- |
| version | Flag | Show version and exit. |
| display_extensions | Flag | Display the list of default file extensions supported for analysis and exit. |
| agent_limit | Integer (x >= 1) | Maximum number of concurrent agent invocations during dataflow and oversight analysis. Default: 10. |
| auto_accept_token_time_estimates | Boolean (true|false) | Skip the large-codebase confirmation prompt, print the estimate, and proceed. Intended for CI/CD environments. Default: False. |
| model_completion_limit | Integer (x >= 1) | Maximum number of completion tokens for the LLM model. |
| cache_database | Text | Database connection string for LLM query caching (for example, postgresql://localhost:5432/signal). |
| cache_file | Text | SQLite database file for local LLM query caching. Default: signal-cache.db. |
| caching | Boolean (true|false) | Enable/Disable local caching for LLMs. Default: True. |
| config | Text | Scan configuration file. Default: .signal. |
| crypto | Boolean (true|false) | Enable/Disable crypto analysis feature. Default: True. |
| cvss_threshold | Text | Minimum CVSS score for filtering results. Accepts a score (0.0-10.0) or severity alias: None (0.0), Low (0.1), Medium (4.0), High (7.0), Critical (9.0). Default: 0.0. |
| dataflow | Boolean (true|false) | Enable/Disable cross-file dataflow agent feature. Default: True. |
| disable_default | Boolean (true|false) | Disable the default analysis logic and run only alternate analysis logic (for example, misra). Default: False. |
| exclude_paths | Text | Comma-separated list of paths or files to exclude from analysis within the target directory. Does not affect dataflow traces. |
| checkpoint_file | Text | Path to a dataflow checkpoint file used to resume an interrupted scan. Must be used with import_results to preserve result GUIDs. |
| export_results | Text | Export single-file analysis results to a JSON file. Can be imported later with import_results. |
| extra_extensions | Text | Comma-separated list of additional file extensions to analyse (for example, .foo,.bar). |
| git_diff | Boolean (true|false) | Scan all uncommitted Git changes (staged and unstaged). Default: False. |
| git_diff_reference_branch | Text | Reference branch for Git diff comparison. Used with git_diff to analyse changes since divergence from the specified branch. |
| git_diff_generate_patches | Boolean (true|false) | Generate Git diff patch files. If False, patch files are assumed to already exist. Default: False. |
| git_diff_untracked | Boolean (true|false) | Include untracked files when generating Git diff patches. Default: False. |
| ignore_test_files | Boolean (true|false) | Skip test and example files. Default: True. |
| import_results | Text | Import previously exported single-file analysis results and skip re-analysis. Continues with graph, dataflow, and oversight analysis. |
| include_paths | Text | Comma-separated list of paths or files to analyse within the target directory. Does not affect dataflow traces. |
| intra_file_shortcircuit | Boolean (true|false) | Allow single-file analysis to document a complete in-file dataflow trace itself and skip the dataflow agent, when the tainted value originates outside the process within the same file. Set to false to route every user-controlled-input finding to the dataflow agent as before. Default: True. |
| large_code_base_size | Integer (x >= 100) | File-count threshold above which a pre-flight token/time estimate is run and user confirmation is required. Default: 500. |
| llm_key | Text | LLM API key. |
| llm_limit | Integer (x >= 1) | Maximum number of concurrent LLM requests during single-file analysis. Default: 10. |
| llm_model | Text | LLM model used for single-file analysis. Default: claude-sonnet-4-6. |
| llm_model_agent | Text | LLM model used for SAST agents. Default: o3-mini. |
| llm_tag | Text | Tag used for LLM tracking. Default: signal. |
| llm_uri | Text | LLM endpoint. Default: <https://llm.core.blackduck.com/>. |
| log_file | Text | Path for standard log output. Default: signal.log. |
| error_log_file | Text | Path for error log output. Default: signal_errors.json. |
| log_level | Enum (info, error, warn, debug) | Logging level. Default: INFO. |
| misra | Boolean (true|false) | Enable/Disable experimental MISRA analysis feature. Default: False. |
| oversight | Boolean (true|false) | Enable/Disable oversight agent review feature. Default: True. |
| oversight_cve_detection | Boolean (true|false) | Enable/Disable CVE detection during oversight review. Default: True. |
| oversight_embedding_enabled | Boolean (true|false) | Experimental embedding-based similarity search for oversight rule matching. Reduces token usage during oversight review. Default: True. |
| oversight_embedding_model | Text | Embedding model used for oversight rule similarity matching. Default: text-embedding-3-small. |
| oversight_rules_file | Text | Path to a custom CSV file containing rule_id,cwe pairs. Uses built-in rules if not specified. |
| report_file | Text | Path for SARIF report output. Default: results.sarif. |
| result_limit | Integer (x >= 1) | Limit the number of results returned during single-file analysis. |
| show_triage | Boolean (true|false) | Show results automatically triaged as false positives. Default: False. |
| skip_estimates | Boolean (true|false) | Skip the large-codebase pre-flight estimate, including sample LLM calls and confirmation prompt. Default: False. |
| thinking_budget | Integer (1024 <= x <= 128000) | Token budget for Anthropic extended thinking/reasoning. Higher values may improve accuracy but increase token usage and latency. Applies only to thinking-capable Claude models. Default: 8192. |
| help | Flag | Show help message and exit. |

### [SCAN] Flags

Any CLI flag can be set here as its `snake_case` equivalent (`--log-file` → `log_file`). `getConfig` merges the section straight into `config.SCAN` after applying defaults.

| Key | CLI equivalent | Type | Purpose |
| --- | --- | --- | --- |
| `target` | Positional argument | `str` | Directory to scan, usually specified on the CLI rather than in the configuration file |
| `include_paths` | `--include-paths` | CSV string | Subpaths to include. Wrap paths containing commas in quotation marks |
| `exclude_paths` | `--exclude-paths` | CSV string | Subpaths to skip |
| `extra_extensions` | `--extra-extensions` | CSV string | Additional file extensions to analyse, such as `.foo,.bar` |
| `ignore_test_files` | `--ignore-test-files` | `bool` | Skip test and example files |
| `report_file` | `--report-file` | `str` | Path for the SARIF output file |
| `summary_report_file` | `--summary-report-file` | `str` | Path for the summary text output |
| `sca_report_file` | `--sca-report-file` | `str` | Path for the SCA JSON output |
| `log_file``error_log_file` | `--log-file``--error-log-file` | `str` | Paths for standard and error logs |
| `log_level` | `--log-level` | `INFO`, `ERROR`, `WARN`, or `DEBUG` | Controls log verbosity |
| `mode` | `--mode` | `static`, `sca`, or `crypto` | Selects the primary analysis mode |
| `dataflow``oversight``sca``crypto``misra``exploit``poc_kit``merge_keys``git_diff``disable_default` | Matching CLI flag | `bool` | Enables or disables the corresponding feature |
| `show_triage` | `--show-triage` | `bool` | Includes automatically triaged false positives in the report |
| `cvss_threshold` | `--cvss-threshold` | `float` or severity name | Filters out results below the specified score or severity |
| `llm_limit``agent_limit` | `--llm-limit``--agent-limit` | `int` | Sets LLM and agent concurrency limits |
| `result_limit` | `--result-limit` | `int` | Limits output to the top N results |
| `model_completion_limit` | `--model-completion-limit` | `int` | Sets the maximum number of completion tokens |
| `temperature` | `--temperature` | `float`, 0.0–2.0 | Controls LLM response variability |
| `thinking_budget` | `--thinking-budget` | `int`, 1024–128000 | Sets the Claude extended-thinking token budget |
| `caching` | `--caching` | `bool` | Enables the local SQLite response cache |
| `cache_file` | `--cache-file` | `str` | Specifies the SQLite cache path |
| `cache_database` | `--cache-database` | `str` | Specifies the PostgreSQL URL for a shared cache |
| `llm_prompt_caching` | `--llm-prompt-caching` | `bool` | Enables Anthropic `cache_control` prompt caching |
| `oversight_embedding_enabled` | `--oversight-embedding-enabled` | `bool` | Enables embedding-based oversight rule matching |
| `oversight_rules_file` | `--oversight-rules-file` | `str` | Specifies a custom `rule_id,cwe` CSV file |
| `oversight_embedding_model` | `--oversight-embedding-model` | `str` | Specifies the embedding model used for oversight |
| `oversight_cve_detection` | `--oversight-cve-detection` | `bool` | Enables CVE detection during oversight |
| `export_results``import_results` | Matching CLI flag | `str` | Saves or restores single-file results |
| `checkpoint_file``checkpoint_interval` | Matching CLI flag | `str` / `int` | Configures dataflow crash recovery and resumption |
| `large_code_base_size` | `--large-code-base-size` | `int`, minimum 100 | Sets the file-count threshold for a preflight estimate |
| `auto_accept_token_time_estimates``skip_estimates` | Matching CLI flag | `bool` | Controls preflight-estimate behaviour |
| `git_diff_reference_branch``git_diff_dir``git_diff_generate_patches``git_diff_preserve_patches``git_diff_untracked` | Matching CLI flag | Mixed | Configures Git-diff mode |
| `project_name` | `--project-name` | `str` | Specifies the merge-key project identifier |
| `llm_key``llm_uri``llm_model``llm_model_agent``llm_model_sca_agent``llm_tag` | Matching CLI flag | `str` | **Legacy:** Configures managed-mode LLM settings. See `[LLM]` for the BYO configuration surface |
| `llm_mode` | `--llm-mode` | `managed` or `byo` | Selects the managed gateway or BYO agent surface |
| `connectivity_check``check_llm``check_llm_json` | Matching CLI flag | `bool` | Runs the corresponding preflight or validation mode |

### BYOLLM Flags

Values here are inherited by every `[LLM_*_AGENT]` section unless the agent overrides them. This section is relevant only when enabling the BYOLLM mode (`mode = byo` or `--llm-mode byo`). For more details, see BYOLLM.

| Key | CLI equivalent | Notes |
| --- | --- | --- |
| `mode` | `--llm-mode` | Selects the LLM mode: `managed` (default, uses `llm.core.blackduck.com`) or `byo` (bring your own) |
| `uri` | `--llm-uri` | Base endpoint URL. The provider is automatically detected from the hostname, including OpenAI-compatible endpoints, `*.openai.azure.com`, `*.cognitiveservices.azure.com`, and `*.services.ai.azure.com` |
| `key` | `--llm-key` | API key. Supports environment variable substitution using `${VAR}` |
| `timeout` | `--llm-timeout` | Per-request timeout in seconds |
| `api_version` | `--llm-api-version` | Required for Azure OpenAI deployments (for example, `2025-01-01-preview`); ignored by other providers |
| `ssl_verify` | `--llm-ssl-verify` | Set to `false` when using self-signed certificates |
| `ca_bundle` | `--llm-ca-bundle` | Path to a custom PEM certificate bundle |
| `gcp_service_account_key` | `--gcp-service-account-key` | Path to a Google Cloud service account JSON file or a base64-encoded JSON string. Used only with Vertex AI |
| `gcp_project` | `--gcp-project` | Google Cloud Vertex AI project ID |
| `gcp_region` | `--gcp-region` | Vertex AI region, such as `us-central1` |
| `aws_bearer_token` | `--aws-bearer-token` | AWS Bedrock IAM service-specific credential secret |
| `aws_bedrock_region` | `--aws-bedrock-region` | AWS Bedrock region, such as `us-east-2` |

### **SDK env-var fallbacks for BYOLLM**

This section is relevant only when enabling the BYOLLM mode (`mode = byo` or `--llm-mode byo`). When a field is not set in CLI or config, Signal falls back to widely-known SDKenv vars according to:

| Provider | Environment Variable(s) | Configuration Key |
| --- | --- | --- |
| OpenAI-compatible | `OPENAI_API_KEY` | `key` |
| Azure OpenAI | `AZURE_OPENAI_ENDPOINT` | `uri` |
| `AZURE_OPENAI_API_KEY` | `key` |
| `AZURE_OPENAI_API_VERSION` | `api_version` |
| Google Cloud Vertex AI | `GOOGLE_APPLICATION_CREDENTIALS` | `gcp_service_account_key` |
| `GOOGLE_CLOUD_PROJECT`, `GCP_PROJECT` | `gcp_project` |
| `GOOGLE_CLOUD_REGION`, `GCP_REGION` | `gcp_region` |
| AWS Bedrock | `AWS_BEARER_TOKEN_BEDROCK` | `aws_bearer_token` |
| `AWS_REGION` | `aws_bedrock_region` |

### BYOLLM Agents

This section is relevant only when enabling the BYOLLM mode (`mode = byo` or `--llm-mode byo`).

| Section | Agent role | Managed-mode source flag |
| --- | --- | --- |
| `[LLM_SINGLEFILESCAN_AGENT]` | Performs per-file vulnerability detection. Typically the highest-consuming LLM agent in terms of token usage. | `--llm-model` |
| `[LLM_DATAFLOW_AGENT]` | Performs cross-file dataflow tracing and multi-step analysis across code paths. | `--llm-model-agent` |
| `[LLM_OVERSIGHT_AGENT]` | Handles false-positive triage and second-pass review using two prompt workflows that share a single client configuration. | `--llm-model-agent` |
| `[LLM_EXPLOITATION_AGENT]` | Generates executive summaries and attack-chain analysis for identified issues. | `--llm-model-agent` |
| `[LLM_SCA_AGENT]` | Provides software composition analysis (SCA) orchestration, including supervisor, audit, and knowledge-base sub-agents that share a common client. | `--llm-model-sca-agent` (also supports `--llm-model-sca`) |
| `[LLM_MERGEKEY_EMBED_AGENT]` | Generates embedding vectors used for cross-run merge-key matching and correlation. | Uses the managed default embedding model (`text-embedding-3-large`) |
| `[LLM_OVERSIGHT_EMBED_AGENT]` | Generates embedding vectors for oversight rule similarity matching. | Uses the managed default embedding model (`text-embedding-3-small`) |

### Signal parameters related to Bridge CLI

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| LLM API key | `signal.llm.key` | `BRIDGE_SIGNAL_LLM_KEY` | Yes | API key or token for the configured LLM endpoint. Bridge passes this directly to `--llm-key`. The key must be valid for the chosen LLM endpoint. |
| Project directory | `project.directory` | `BRIDGE_SIGNAL_PROJECT_DIRECTORY` | No | Absolute path to the project root that Bridge uses as the working directory and scan target. Must point to the root of the source tree, and to a Git repository when using diff modes.  **Example**: `/home/dev/workspace/my-service`  If no value is provided, Bridge CLI  uses the current directory as the project directory. |
| Signal version | `signal.version` | `BRIDGE_SIGNAL_VERSION` | No | Specific Signal version to install and invoke. If omitted, Bridge resolves and downloads the latest supported Signal version for the current OS and architecture.  **Example**: `"0.2.9"` |
| Scan mode | `signal.mode` | `BRIDGE_SIGNAL_SCAN_MODE` | No | Use to specify a scan mode:  - `FILES` : Direct selection via `signal.include` and `signal.exclude`. - `UNCOMMITTED` : Git diff of uncommitted and staged changes. Signal generates the patch files. - `REFERENCE`: Git diff between the current branch and a reference branch. Signal generates patch files based on the values provided and executes scans. - `PROJECT:` Performs an AI assessment of files in a project directory and uploads scan findings to a configured platform on completion. Currently, Polaris is supported as an upload platform.   **Default**: `FILES` and uses the values provided for `signal.include`.  For `UNCOMMITTED` and `REFERENCE`, Bridge considers the changes under `project.directory`. |
| Exclude paths | `signal.exclude` | `BRIDGE_SIGNAL_EXCLUDE` | No | Comma separated list of file or directory paths (relative to `project.directory`) to exclude from the scan, in any mode. **Example** : `"tests/,examples/"` |
| SARIF Report File Path | `signal.reportFile` | `BRIDGE_SIGNAL_REPORT_FILE` | No | Optional custom path for the Signal SARIF report file. When provided, Bridge passes `--report-file "<signal.reportFile>"` and returns the same value on completion. **Default**: Uses Signal default, `results.sarif`). |
| Free-form Signal arguments | `signal.args` | `BRIDGE_SIGNAL_ARGS` | No | Additional Signal CLI flags appended as‑is. Must not include `--include-paths` or `--report-file`; Bridge derives diff or patch handling and report path.  Suitable for tuning analysis features such as `--dataflow`, `--crypto`, or log level.  **Example**: `"--dataflow true --log-level debug"` |

### FILE mode parameters

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Include paths | `signal.include` | `BRIDGE_SIGNAL_INCLUDE` | Yes | Comma‑separated list of file or directory paths (relative to `project.directory`) to include in `FILES` mode. If empty or omitted in `FILES` mode, Bridge returns an error and requires a value.  **Example**: `"src/service/foo.py,src/service/bar.py"` |

### UNCOMMITTED mode parameters

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Git execution path | `signal.git.execution.path` | `BRIDGE_SIGNAL_GIT_EXECUTION_PATH` | No | Absolute path to Git binary executable. **Default:** Uses system path to locate Git executable binary. |

### REFERENCE mode parameters

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Reference branch | `signal.git.ref` | `BRIDGE_SIGNAL_GIT_REF` | Yes | Reference branch name for Git diff comparison . **Examples**: `"main"`, `"origin/main"` |
| Git execution path | `signal.git.execution.path` | `BRIDGE_SIGNAL_EXECUTION_PATH` | No | Absolute path to Git binary executable. **Default:** Uses system path to locate Git executable binary. |

### PROJECT mode parameters

Project mode parameters control where Signal uploads results. This section summarizes the available platforms and their configuration parameters.

| Argument | Input Mode | | Required | Notes |
| --- | --- | --- | --- | --- |
| Command Line Argument | Environment Variable |
| Platform | `signal.platform` | `BRIDGE_SIGNAL_PLATFORM` | No | Indicates the platform to upload results to. Use Polaris. Note: If `signal.platform` is not used for a project scan then Bridge will still run the scan and will exit without attempting to upload results. |
| Polaris URL | `polaris.serverUrl` | `BRIDGE_POLARIS_SERVERURL` | Yes | The Polaris URL for uploading results. |
| Polaris token | `polaris.accessToken` | `BRIDGE_POLARIS_ACCESSTOKEN` | Yes | The Polaris access token. |
| Application name | `polaris.application.name` | `BRIDGE_POLARIS_APPLICATION_NAME` | Yes | Polaris application name. |
| Project name | `polaris.project.name` | `BRIDGE_POLARIS_PROJECT_NAME` | Yes | Polaris project name. |
| Branch name | `polaris.branch.name` | `BRIDGE_POLARIS_BRANCH_NAME` | Yes | Polaris branch name. |

### Signal outputs

When a client invokes `bridge --stage signal`, Bridge guarantees the following outputs in the workflow context and/or client-facing response.

| Field | JSON Field | Notes |
| --- | --- | --- |
| Signal exit code | `signal.exitCode` | Numeric process exit code from the Signal binary (0=success, non-zero=failure). Clients should treat non-zero values as a scan failure and surface the underlying error or logs as appropriate. |
| SARIF report file path | `signal.report.output` | Absolute or relative path to the generated SARIF security report file. If the `signal.reportFile` argument is provided, the same path is returned. Otherwise, the Signal controller assigns a default path (`results.sarif`) before execution and returns it. This path serves as the main artifact for downstream consumers like Code Sight or CI. **Default**: results.sarif.json |
| Report URL | `signal.report.url` | This is the URL for the uploaded results file. |
| Upload successful | `signal.report.uploadSuccessful` | Boolean flag indicating whether the upload of the SARIF report to the configured platform completed successfully. When `true`, the artifact was uploaded and a valid `signal.report.url` is available; `false` means the upload failed and clients should not rely on `signal.report.url`. |

### Polaris Flags

| Key | Purpose |
| --- | --- |
| `endpoint` | Base Polaris server URL, for example `https://poc.polaris.blackduck.com` |
| `access_token` | Polaris API access token used for authentication |
| `portfolio` | UUID of the Polaris portfolio to use |
| `application` | UUID of the Polaris application to use |
| `project` | UUID of the Polaris project to use |

### Signal config file

With Signal v0.1.3 and newer, Signal options can now be placed in a `.signal` config file located in the current directory. Any CLI option can also be added in the config file. When an option is defined in both the configuration file and the CLI, the CLI setting overrides the configuration file value.

```
[SCAN]
#exclude_paths=path1,path2
#include_paths=path1,path2
#llm_key=YOUR_LLM_API_KEY
log_level=DEBUG
oversight=false
dataflow=false
```

When used with the MCP server, Signal will look for a config file in `$HOME/.blackduck/mcp/signal/.scan-config`.
