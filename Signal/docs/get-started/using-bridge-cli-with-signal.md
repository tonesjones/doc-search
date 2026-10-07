---
title: "Using Bridge CLI with Signal"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/using-bridge-cli-with-signal.html"
content_id: "jjhChLFp3nrWpn45ZMX52g"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.620659+00:00"
---

# Using Bridge CLI with Signal

Black Duck Bridge runs AI driven Signal scans on local codebases and produces results that can be reviewed locally or uploaded to a Black Duck platform.

## Contents

- Black Duck products overview
- Scan modes
- Scan outputs
- Start scanning your code

## Black Duck products overview

- **Signal** is an AI driven application security capability designed for agentic software development. It uses Large Language Models (LLMs) together with the Black Duck Knowledge Base to identify high priority, high fidelity security issues in software and to provide contextual guidance that supports remediation.
- **Bridge** provides control over how Signal analyzes code, including the scan mode and parameters, and manages the steps needed to perform a scan. Results are returned in standard outputs such as SARIF reports and exit codes, making findings easier to review and act upon.
- **Polaris** delivers highly scalable Static Application Security Testing (SAST), Software Composition Analysis (SCA), Dynamic Application Security Testing (DAST), and Container Analysis for your Enterprise.

When using Bridge with Signal, it is possible to create a workflow that enables Signal to be run against local codebases, such as folders or Git project directories, and, when using Project mode, allows scan findings to be uploaded to a Black Duck platform for centralized visibility. Currently, Project mode supports integration with Polaris.

## Scan modes

Bridge-Signal supports four scan modes. The scan mode determines what content Signal analyzes and how that content is identified.

| Mode | Description |
| --- | --- |
| Files | Signal analyzes a specific set of files or directories. Scanned files and folders can be controlled by specifying Include paths and optional exclude paths.  Use this mode when the relevant content is known and can be enumerated directly, independent of git history. |
| Uncommitted changes | Signal analyzes files that have been modified in a git working copy but have not yet been committed.  Use this mode for pre-commit or local development workflows where only in-progress changes should be scanned. |
| Reference branch | Signal analyzes the differences between the current branch and a specified reference branch in a git repository.  Use this mode for Pull Request workflows where only the changes introduced on the current branch are relevant. |
| Project mode | Use this mode to analyze the entire source code in a repository. Note: This will consume more LLM tokens and is recommended for use with Signal Enterprise.  If `signal.platform` is provided, scan results will also be available on the Black Duck platform. Currently, upload to Polaris is supported. |

## Scan outputs

Bridge-Signal produces the following outputs that downstream tools and pipeline stages can consume:

| Output Type | Description |
| --- | --- |
| SARIF report | The SARIF report contains the findings produced by Signal and can be ingested by any SARIF-compatible tool or service. |
| Process exit code | Indicates the overall outcome of the Signal execution, with 0 signaling a successful outcome. Bridge maps Signal exit codes to consistent values so that pipeline logic can reliably determine whether the scan succeeded, produced findings, or encountered an error. |

## Start scanning your code

- Scan local files
- Scan uncommitted changes
- Scan changes against a reference branch
- Scan a full project

**Related Links**

- [Bridge Documentation](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-cli.html)
- [Signal Documentation](https://docs.blackduck.com/r/signal/black-duck-signal/overview-of-black-duck-signal.html)
- [Polaris Documentation](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/polaris-product-overview.html)
