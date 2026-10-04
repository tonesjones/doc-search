---
title: "Agentic SAST workflow metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/agentic-sast-workflow-metrics.html"
content_id: "06CFsQLQJooBzbIexVHLBw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.346072+00:00"
---

# Agentic SAST workflow metrics

View aggregate execution and remediation metrics for Agentic SAST
workflows in a project.

## Workflow metrics

The Sigma MCP client submits workflow metrics to Coverity
Connect after Agentic SAST workflows run. Coverity Connect
aggregates the metrics for streams in a project.

## Available metrics

| Metric | Description |
| --- | --- |
| Project name | Name of the project for which Coverity Connect returns metrics. |
| Stream names | Streams in the project where Agentic SAST workflows have run. |
| Total iterations | Total number of iterations completed across the reported workflow executions. |
| Total issues detected | Total number of issues detected during the reported workflow executions. |
| Total issues fixed | Total number of issues fixed during the reported workflow executions. |
| Total issues introduced | Total number of new issues introduced during remediation. |
| Estimated tokens saved | Estimated number of tokens saved during the reported workflow executions. |

## Retrieve workflow metrics

Use the following endpoint to retrieve aggregated execution
metrics for a project:

```
GET /api/v3/agentic/executionMetrics/project?projectName=<project-name>
```

The required `projectName` query parameter
specifies the project for which to retrieve metrics.

Important:
You must have Project Owner permission or higher for the
specified project.

## Example response

```
{
                "projectName": "sample-ces",
                "streamNames": [
                "sample-stream"
                ],
                "totalIterations": 0,
                "totalIssuesDetected": 0,
                "totalIssuesFixed": 0,
                "totalIssuesIntroduced": 0,
                "estimatedTokensSaved": 0
                }
```

## Status codes

| Status code | Description |
| --- | --- |
| `200 OK` | Coverity Connect successfully returned the execution metrics. |
| `400 Bad Request` | The request is malformed or does not include the required parameter. |
| `401 Unauthorized` | Authentication failed or the request does not include authentication credentials. |
| `404 Not Found` | The specified project does not exist. |
| `500 Internal Server Error` | Coverity Connect encountered an error while processing the request. |
