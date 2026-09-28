---
title: "Local notes: Signal CLI usage and options (field reference)"
source_url: "local:///C:/Users/TonyJiang/.claude/skills/bd/Signal/AGENTS.md"
content_id: "local-signal-cli-reference"
version: "latest"
section: "Reference guide"
scraped_at: "2026-09-23T00:00:00.000000+00:00"
local_addition: true
note: >
  This topic is NOT scraped from docs.blackduck.com. It was hand-authored and
  previously lived inside the `bd` skill directory
  (~/.claude/skills/bd/Signal/AGENTS.md), outside the corpus, where the bd
  skill's product router could not reach it. Moved here so Signal questions
  resolve through the normal corpus path. Covers the signal-pyarmor executable
  invocation, arguments and options, which the scraped Signal corpus does not
  document. Treat as a secondary/community reference: it can drift from its
  upstream source independently of the docs.blackduck.com release cycle.
---

# Black Duck Signal

Black Duck Signal performs **AI-powered security analysis on your codebase** without scanning.

## Usage

```
signal-pyarmor-windows_x86.exe [OPTIONS] TARGET
```

### Arguments

- **TARGET** (required): Path to the target code for analysis

## Core Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--version` | - | - | Show version and exit |
| `--display-extensions` | - | - | Display list of default file extensions supported for analysis |
| `--config` | TEXT | `.signal` | Scan configuration file |
| `--report-file` | TEXT | `results.sarif` | Path to write SARIF report output |
| `--log-file` | TEXT | `signal.log` | Path to write log file output |
| `--error-log-file` | TEXT | `signal_errors.json` | Path to write error log file output |
| `--log-level` | [info\|error\|warn\|debug] | INFO | Logging level |

## Analysis Features

### Toggle Features

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--dataflow` | [true\|false] | True | Turn on cross-file dataflow agent feature |
| `--oversight` | [true\|false] | True | Turn on oversight agent review feature (false-positive triage and second-pass review) |
| `--crypto` | [true\|false] | False | Turn on crypto analysis feature |
| `--misra` | [true\|false] | False | Turn on experimental MISRA analysis feature |
| `--synthesis` | [true\|false] | False | EXPERIMENTAL: Identify chained vulnerabilities and top vulnerability after dataflow analysis. Requires `--dataflow True` |
| `--poc-kit` | [true\|false] | False | EXPERIMENTAL: Enable PoCKit autonomous exploit validation. Requires `--dataflow True --synthesis True`. Executes shell commands and runs code in Docker |

### Oversight Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--oversight-cve-detection` | [true\|false] | True | Enable CVE detection during oversight review |
| `--oversight-embeddings` | [true\|false] | True | EXPERIMENTAL: Use embedding-based similarity search for oversight rule matching (reduces token spend) |
| `--oversight-embedding-model` | TEXT | `text-embedding-3-small` | Embedding model for oversight rule similarity matching |
| `--oversight-rules-file` | TEXT | - | Path to custom rule_id,cwe pairs file (CSV format). Uses built-in default if not provided |

## Path Filtering

| Option | Type | Description |
|--------|------|-------------|
| `--include-paths` | TEXT | Comma-separated list of paths/files to analyze. Quoted if containing commas |
| `--exclude-paths` | TEXT | Comma-separated list of paths/files to exclude (does not impact dataflow traces) |
| `--extra-extensions` | TEXT | Comma-separated file extensions to analyze (e.g., `.foo,.bar`) |
| `--skip-generated-files` | [true\|false] | Skip minified/bundled files (*.min.js) and generated lockfiles (e.g. package-lock.json). Default: True |
| `--ignore-test-files` | [true\|false] | Skip files used for testing or examples. Default: True |

## Git Integration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--git-diff` | [true\|false] | False | Use git-diff feature to scan all uncommitted changes (staged+unstaged) |
| `--git-diff-reference-branch` | TEXT | - | Reference branch name for git-diff comparison |
| `--git-diff-dir` | TEXT | `.git_patches` | Directory for git-diff patch files |
| `--git-diff-generate-patches` | [true\|false] | False | Generate git-diff patch files |
| `--git-diff-untracked` | [true\|false] | False | Include untracked files in git-diff patch generation |

## Result Processing

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--result-limit` | INTEGER | - | Limit to top N results gathered during single-file analysis |
| `--cvss-threshold` | TEXT | 0.0 | Minimum CVSS score for filtering results. Accepts numeric (0.0–10.0) or severity: None (0.0), Low (0.1), Medium (4.0), High (7.0), Critical (9.0) |
| `--show-triage` | [true\|false] | False | Show results auto-triaged as false positives |
| `--disable-default` | [true\|false] | False | Disable default analysis logic; only run alternate analysis (e.g., `--misra`) |
| `--prioritization` | [true\|false] | False | EXPERIMENTAL: Annotate SARIF findings with severity rank (0-100) and novelty metadata |
| `--result-preview` | [true\|false] | False | EXPERIMENTAL: Write self-contained HTML preview with rank/novelty/exploitability. Requires `--prioritization` |

## Performance & Estimation

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--large-code-base-size` | INTEGER | 500 | File-count threshold for pre-flight token/time estimate and user confirmation |
| `--auto-accept-token-threshold` | [true\|false] | False | Skip large-codebase confirmation prompt; print estimate and proceed. For CI/CD |
| `--skip-estimates` | [true\|false] | False | Skip pre-flight estimate entirely (no sample LLM calls, no confirmation) |
| `--agent-limit` | INTEGER | 10 | Max concurrent agent invocations during dataflow and oversight analysis |
| `--llm-limit` | INTEGER | 10 | Max concurrent LLM requests during single-file analysis |

## LLM Configuration

### Mode & Default Models

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--llm-mode` | [managed\|byo] | managed | LLM operating mode: 'managed' (Black Duck hosted at llm.core.blackduck.com) or 'byo' (customer-provided endpoints: OpenAI-compatible, Azure OpenAI, Azure AI Services, GCP Vertex AI, AWS Bedrock) |
| `--llm-model` | TEXT | `claude-sonnet-4-6` | LLM model for single-file analysis |
| `--llm-model-agent` | TEXT | `o3-mini` | LLM model for SAST agents |
| `--llm-key` | TEXT | - | LLM API key |
| `--llm-uri` | TEXT | `https://llm.core.blackduck.com` | LLM endpoint |
| `--llm-timeout` | INTEGER | 300 | Default timeout in seconds for all LLM requests |

### Anthropic/Claude Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--llm-prompt-caching` | [true\|false] | True | Enable Anthropic prompt caching (cache_control blocks) on supported providers (AWS Bedrock, Anthropic direct). Reduces input-token spend on long shared prompts |
| `--thinking-budget` | INTEGER [1024-128000] | 8192 | Token budget for Anthropic extended thinking ('reasoning'). Only for thinking-capable models (Claude Sonnet 4.5/4.6); silently ignored for others. Higher values improve accuracy on complex vulnerabilities but add latency |
| `--model-completion-limit` | INTEGER | - | Max completion tokens for LLM model |

### AWS Bedrock Configuration

| Option | Type | Description |
|--------|------|-------------|
| `--aws-bearer-token` | TEXT | AWS Bedrock Bearer token for authentication (IAM service-specific credential). Created via `aws iam create-service-specific-credential --service-name bedrock.amazonaws.com --credential-age-days N`. Max duration: 30 days. Can also use `AWS_BEARER_TOKEN_BEDROCK` env var |
| `--aws-bedrock-region` | TEXT | AWS region for Bedrock (e.g., us-east-2). Can also use `AWS_REGION` env var |

### GCP Vertex AI Configuration

| Option | Type | Description |
|--------|------|-------------|
| `--gcp-project` | TEXT | GCP project ID. Auto-detected from service account key if not specified |
| `--gcp-region` | TEXT | GCP region (e.g., us-central1). Auto-detected from endpoint URI if not specified |
| `--gcp-service-account-key` | TEXT | Path to GCP service account JSON key file or base64-encoded key string. Used for automatic OAuth2 token generation |

### Azure Configuration

| Option | Type | Description |
|--------|------|-------------|
| `--llm-api-version` | TEXT | API version for Azure OpenAI/Azure AI Services. Required for Azure endpoints (*.openai.azure.com, *.cognitiveservices.azure.com, *.services.ai.azure.com). Example: `2024-12-01-preview`. Not required for Claude/Anthropic (native API) |
| `--llm-ssl-verify` | [true\|false] | Enable TLS certificate verification for LLM endpoints. Default: True. Set False for self-signed certificates |
| `--llm-ca-bundle` | TEXT | Path to CA bundle PEM file for custom TLS certificate verification |

### Per-Agent LLM Configuration (BYO Mode)

For `--llm-mode byo`, each of the seven Signal agents can be configured independently:
- **singlefilescan-agent** (single-file vulnerability detection)
- **dataflow-agent** (cross-file dataflow tracing)
- **exploitation-agent** (exploit summaries and attack-chain narrative)
- **oversight-agent** (false-positive triage and second-pass review)
- **oversight-embed-agent** (oversight rule-similarity embeddings)
- **sca-agent** (software composition analysis)
- **mergekey-embed-agent** (cross-run merge-key embeddings)

Each supports: `--llm-<agent>-agent-uri`, `--llm-<agent>-agent-key`, `--llm-<agent>-agent-model`, `--llm-<agent>-agent-api-version`, `--llm-<agent>-agent-timeout`

Examples:
```
--llm-singlefilescan-agent-model gpt-4o
--llm-dataflow-agent-uri https://my-openai.com/v1
--llm-exploitation-agent-key ${EXPLOIT_KEY}
```

### Caching Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--caching` | [true\|false] | True | Enable local caching for LLM responses |
| `--cache-file` | TEXT | `signal-cache.db` | SQLite database file for local LLM query caching |
| `--cache-database` | TEXT | - | Database connection string for LLM query caching (e.g., postgresql://localhost...) |

### LLM Health & Troubleshooting

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--check-llm` | [true\|false] | False | Validate LLM endpoint connectivity and model availability, then exit. Use to verify BYO LLM configuration before running a scan |
| `--check-llm-json` | [true\|false] | False | Emit check-llm results as JSON on stdout instead of Rich table. Stable API (schema_version 1) for downstream consumers like Bridge CLI and CodeSight. Implies `--check-llm True` |
| `--llm-tag` | TEXT | `signal` | Specify LLM tag for tracking |

## Checkpoint & Export

| Option | Type | Description |
|--------|------|-------------|
| `--export-results` | TEXT | Export single-file analysis results to JSON file (e.g., 'results_cache.json'). Can be imported later |
| `--import-results` | TEXT | Import previously exported single-file analysis results and skip re-analysis. Continues with graph/dataflow/oversight |
| `--checkpoint-file` | TEXT | Path to dataflow checkpoint file to resume interrupted scan. Must be used with `--import-results` to preserve result GUIDs |

## PoCKit Exploit Validation

**EXPERIMENTAL** — autonomous exploit validation (requires `--dataflow True --synthesis True`)

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--poc-kit` | [true\|false] | False | Enable PoCKit autonomous exploit validation. Writes and runs exploit code in isolated Docker container. **WARNING:** Only enable on codebases you own in authorized environments. Do not run on production or shared infrastructure |
| `--poc-kit-report-dir` | TEXT | `./pockit-workspace` | Directory for PoCKit workspace and evidence files (one subdirectory per finding GUID) |
| `--poc-kit-log-file` | TEXT | `pockit.log` | Path to PoCKit log output |

## Pipeline & Advanced

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--pipeline` | [true\|false] | False | EXPERIMENTAL: Stream findings through analysis stages as each completes (single event loop) instead of phase-barrier scheduling |
