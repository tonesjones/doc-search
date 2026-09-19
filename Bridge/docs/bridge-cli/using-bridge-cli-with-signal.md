---
title: "Using Bridge CLI with Signal"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-bridge-cli-with-signal.html"
content_id: "bU_BVNTVI0dPIcoVQJ4QDQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:53.045183+00:00"
---

# Using Bridge CLI with Signal

Black Duck Bridge Signal runs AI driven Signal scans on local codebases and produces results that can be reviewed locally or uploaded to a Black Duck platform

Bridge provides a workflow that enables Signal to be run against local codebases, such as folders or Git project directories, and, when using Project mode, allows scan findings to be uploaded to a Black Duck platform for centralized visibility. Currently, Project mode supports integration with Polaris.

Signal is an AI driven application security capability designed for agentic software development. It uses Large Language Models (LLMs) together with the Black Duck KnowledgeBase to identify high priority, high fidelity security issues in software and to provide contextual guidance that supports remediation.

Bridge provides control over how Signal analyzes code, including the scan mode and parameters, and manages the steps needed to perform a scan. Results are returned in standard outputs such as SARIF reports and exit codes, making findings easier to review and act upon.

## Scan modes

Bridge Signal supports three scan modes. The scan mode determines what content Signal analyzes and how that content is identified.

| Mode | Description |
| --- | --- |
| Files | Signal analyzes a specific set of files or directories. Scanned files and folders can controlled by specifying Include paths and optional exclude paths.  Use this mode when the relevant content is known and can be enumerated directly, independent of git history. |
| Uncommitted changes | Signal analyzes files that have been modified in a git working copy but have not yet been committed.  Use this mode for pre-commit or local development workflows where only in-progress changes should be scanned. |
| Reference branch | Signal analyzes the differences between the current branch and a specified reference branch in a git repository.  Use this mode for Pull Request workflows where only the changes introduced on the current branch are relevant. |
| Project mode | Use this mode to analyze the entire source code in a repository. Note: This will consume more LLM tokens and is recommended for use with Signal Enterprise.  If `signal.platform` is provided, scan results will also be available on the Black Duck platform. Currently, upload to Polaris is supported. |

## Scan outputs

Bridge Signal produces the following outputs that downstream tools and pipeline stages can consume:

| Output Type | Description |
| --- | --- |
| SARIF report | The SARIF report contains the findings produced by Signal and can be ingested by any SARIF-compatible tool or service. |
| Process exit code | Indicates the overall outcome of the Signal execution, with 0 signaling a successful outcome. Bridge maps Signal exit codes to consistent values so that pipeline logic can reliably determine whether the scan succeeded, produced findings, or encountered an error. |

**Related information**  

- [Signal Documentation](https://docs.blackduck.com/access?ft:originId=45e1f8ccc6ea016432347cf25486b012/2979c4f15f66905a89407ab942b98586.topic)

**Related information**  

- Scan local files with Black Duck Signal
- Perform a diff scan with Black Duck Signal
- Perform a diff scan against a reference branch with Black Duck Signal
- Black Duck Signal reference guide
