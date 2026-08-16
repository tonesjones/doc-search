---
title: "AI-Assisted Triage Plug-in (beta)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ai-assisted-triage-plug-in-beta-.html"
content_id: "nu6CcgCGxgh3qCtEucNisQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:02.791619+00:00"
---

# AI-Assisted Triage Plug-in (beta)

The AI-Assisted Triage Plug-in is a backend service that analyzes Coverity issues and suggests
a classification for each one. The service sends issue data and source code context to a
configured Large Language Model (LLM). Each suggestion includes a classification value,
a confidence score (High, Medium, Low), and a reasoning explanation. The service helps
development teams identify false positives and prioritize genuine security issues.

Note: The AI-Assisted Triage Plug-in is not supported on GLIBC
versions below 2.38.

Warning:

- The source code and derived findings are sent externally to an LLM.
- The exact endpoint is a customer‑provided URL to the LLM.
- The authentication method is a set of LLM keys.
- The intended purpose is for triage recommendations of analysis findings
  only.

## Supported LLM

The AI-assisted triage service requires either Anthropic Claude Sonnet 4 or OpenAI ChatGPT
5.4. Other LLM models are not currently supported.

## Supported checkers

As of 2026.6.0, the AI-Assisted Triage Plug-in supports all Hard Coded Secrets (HSS) checkers across all languages. The following checkers are supported:

- `HARDCODED_CREDENTIALS`
- `HARDCODED_SECRET`
- `SIGMA.hardcoded_secret`

## How the service works

Coverity Connect submits triage requests to the service. The service processes each request through a configured LLM and returns classification suggestions.

1. Coverity Connect sends a request to the service and uploads an artifact containing issue data and source code mappings.
2. The service queues the request for processing.
3. A worker extracts the artifact and sends each issue, along with its source code context, to the configured LLM endpoint.
4. The LLM analyzes the code context and issue details and returns a classification, confidence score, and reasoning for each issue.
5. The service stores the results, and Coverity Connect retrieves them.

The service suggests one of the following classification values for each issue.

Bug
:   The LLM identifies the issue as a genuine defect.

False Positive
:   The LLM identifies the issue as not a real defect.

Intentional
:   The LLM identifies the code behavior as deliberate.

When a request contains multiple issues, Coverity Connect can retrieve results while processing is still in progress. The service tracks the processing state of each issue individually, so completed suggestions are available before the entire request finishes.

## Data sent to the LLM

The service sends the following data to the configured LLM endpoint for analysis.

- Issue JSON files that contain Coverity finding data, including checker type and issue details
- Filemap JSON files that contain source code mappings and code context around the issue location

No historical triage data or version control information is sent to the LLM.

Important: Source code context from file mappings is transmitted to the configured
LLM endpoint. The LLM endpoint can be an external cloud service or an internally
hosted endpoint. Verify that the LLM endpoint meets your organization's security and
data handling requirements before you enable the service.

## Data retention

The service stores data temporarily during processing. The following default retention periods apply.

Request metadata
:   1 hour

Triage results
:   10 minutes

Uploaded artifacts
:   15 minutes

You can configure retention periods. The service cleans up working directories after
processing by default.

Note: The browser stores AI triage
results that have not been accepted or rejected for 48 hours or until the
session ends.

## Architecture

The service supports two deployment modes.

Standalone mode
:   A single binary that combines all required service components. Use standalone mode with Coverity Connect. This mode has no external infrastructure dependencies.

Distributed mode
:   Separate service deployments with external infrastructure. Use distributed mode for production cloud deployments and Kubernetes environments. This mode supports horizontal scaling and high availability.

Note: Distributed deployment is only supported with Coverity Connect (CNC).

Table 1. Deployment mode comparison

| Feature | Standalone mode | Distributed mode |
| --- | --- | --- |
| Use case | Use with Coverity Connect | Production cloud, Kubernetes |
| Infrastructure | No external dependencies | PostgreSQL, RabbitMQ required |
| Deployment | Single binary | Separate API and Worker containers |
| Scaling | Vertical, by increasing workers | Horizontal, by adding more pods |
| High availability | Single point of failure | Multi-replica deployments |
| State persistence | Local disk, lost on restart | Persistent database |

## Limitations

- Suggestion quality depends on the capability of the configured LLM and the code context available in the source file mappings.
- The LLM does not have access to business requirements, project context, or organizational policies. Human review is required before applying suggestions.
- Suggestions are generated independently for each issue. The LLM does not consider relationships between issues.
- Processing time depends on the number of issues in the request, the configured CLI timeout, and the responsiveness of the LLM endpoint.
- The AI-Assisted Triage Plug-in fails when the defect context exceeds the configured LLM’s
  context window.
- The default limit for parallel AI-assisted triage processing is 5 in progress; additional
  triage stays queued.

## Telemetry

The service collects anonymized usage telemetry by default. You can disable telemetry collection in the service configuration.
