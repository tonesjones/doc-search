---
title: "Agentic SAST workflows"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/agentic-sast-workflows.html"
content_id: "23HgCvHZJX7d~rJK65B~SA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.248444+00:00"
---

# Agentic SAST workflows

Agentic SAST workflows integrate Coverity Connect, Sigma, and Claude Code to identify
and remediate security findings during development.

Coverity Connect provides authentication, centrally managed workflow configuration, and
storage for workflow metrics. Sigma performs the static analysis used by the
workflow.

## Workflow configuration

Agentic SAST workflows use three independent configuration artifacts. Each artifact
serves a different purpose and is consumed by a different workflow component.

| Artifact | Purpose | Consumed by |
| --- | --- | --- |
| Scan policy | Defines the minimum severity level for findings that the workflow processes and the maximum number of scan, fix, and re-scan iterations. | Agentic workflow logic |
| Guardrails | Provide security, compliance, and project-specific instructions that guide agent behavior. | Claude Code |
| Sigma scan configuration | Defines what Sigma analyzes and how Sigma performs the analysis. | Sigma |

You can define scan policies and Sigma scan configurations globally or for
individual projects. When configurations exist at both levels, the project-specific
configuration takes precedence. When configuration exists at only one level, the
workflow uses that configuration.

Coverity Connect provides a default scan policy when neither a global nor a
project-specific policy exists. A scan policy is therefore always available to the
workflow.

You can also define guardrails globally or for individual projects. When guardrails
exist at both levels, Coverity Connect appends the project-specific guardrails to
the global guardrails. When guardrails exist at only one level, the workflow uses
those guardrails.

For artifact formats, examples, supported content, and configuration procedures, see
Agentic SAST workflow configuration.

## Workflow execution

During setup, the plugin authenticates with Coverity Connect and retrieves the scan
policy, guardrails, and Sigma scan configuration associated with the selected
project and stream. The plugin also downloads Sigma from Coverity Connect.

For Coverity 2026.9, Coverity Connect provides one Sigma executable version for all
projects and streams.

After Claude Code modifies source files, the workflow performs the following
actions:

1. Sigma scans the modified files and reports new or reintroduced findings that
   match the scan policy. The workflow excludes existing findings and findings
   below the configured severity threshold.
2. The agent analyzes each reported finding and applies a fix.
3. Sigma rescans the modified files to verify the fixes and identify
   regressions.
4. The workflow repeats the scan, fix, and re-scan process until all findings that
   match the scan policy are resolved or the workflow reaches the configured
   maximum iteration count. Before starting another scan, the workflow checks
   whether it has reached the maximum iteration count.

Important: If the workflow reaches the maximum
iteration count before resolving all findings that match the scan policy, the agent
reports the unresolved findings and recommends manual review.

## Workflow metrics

The Sigma MCP client submits workflow metrics to Coverity Connect. The metrics
include aggregate execution, iteration, issue, and resource usage information.

Project Owners can retrieve metrics for workflows that ran against streams in a
project. For more information, see Agentic SAST workflow metrics.
