---
title: "Agentic SAST workflow configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/agentic-sast-workflow-configuration.html"
content_id: "5Gdq_Oo48DdZRIsOIGkCrg"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.302405+00:00"
---

# Agentic SAST workflow configuration

Configure scan policies, guardrails, and Sigma scan settings for
Agentic SAST workflows.

## Configuration artifacts

Agentic SAST workflows use three independent configuration
artifacts. Each artifact has a specific format, purpose, and
consumer.

| Artifact | Format | Purpose | Consumed by |
| --- | --- | --- | --- |
| Scan policy | JSON | Defines the severity threshold and maximum iteration count for the remediation loop. | Agentic workflow logic |
| Guardrails | Natural-language text | Provide security, compliance, project, process, and behavioral instructions. | Claude Code |
| Sigma scan configuration | `coverity.yaml` | Defines the code, checkers, language, and build settings used for Sigma analysis. | Sigma |

## Variables used in the examples

| Variable | Description |
| --- | --- |
| `${CONNECT}` | URL of the Coverity Connect instance. |
| `${PROJECT}` | Name of the Coverity Connect project. |
| `${AUTH}` | Base64-encoded Coverity Connect `username:password` value. |

Create the value for `${AUTH}`:

```
printf "<username>:<password>" | base64
```

Important:
Protect the encoded authentication value. Do not store it in
source control or include it in shared scripts or command
output.

## Permissions

| Operation | Required permission |
| --- | --- |
| Retrieve global configuration | Global Developer |
| Retrieve project configuration | Developer for the project |
| Create, update, or remove global configuration | System Administrator |
| Create, update, or remove project configuration | Project Owner or higher |

Important:
To retrieve combined global and project guardrails, you must
have Developer access at both levels.

Important:
If a project-specific Sigma scan configuration does not exist,
Coverity Connect attempts to retrieve the global
configuration. You must have Global Developer permission to
retrieve the global configuration. Otherwise, Coverity Connect
returns `404 Not Found`.

## Scan policy

A scan policy is a JSON object that controls the scan, fix, and
re-scan loop. The workflow evaluates the policy
programmatically. The REST API uses
`fixLoopPolicy` as the resource name.

A scan policy contains the following properties:

`securityImpactThreshold`
:   Specifies the minimum severity level for findings that
    the workflow processes. Valid values are
    `Info`, `Low`,
    `Medium`, `High`, and
    `Critical`.

`maxIterations`
:   Specifies the maximum number of scan, fix, and re-scan iterations for one
    workflow run.

Important:

For Coverity 2026.9, the `securityImpactThreshold` property filters findings based
on an internal severity value. The current valid values map to the **Security
Impact** column in Connect as follows: `Info -> Very Low, Low
-> Low, Medium -> Moderate, High -> High, Critical -> Very
High`. Support for the current set of valid values will be removed
in a future release. The valid values will then correspond directly to the
values displayed in the **Security Impact** column in Connect.

Coverity Connect provides the following default scan policy:

```
{
  "securityImpactThreshold": "High",
  "maxIterations": 5
}
```

Coverity Connect uses a project-specific policy instead of the
global policy when both exist. If neither exists, Coverity
Connect uses the default policy.

## Scan policy APIs

| Operation | Method and endpoint |
| --- | --- |
| Retrieve the global policy | `GET /api/v3/agentic/fixLoopPolicy` |
| Retrieve the policy for a project | `GET /api/v3/agentic/fixLoopPolicy?projectName=${PROJECT}` |
| Create the global policy | `POST /api/v3/agentic/fixLoopPolicy/global` |
| Update the global policy | `PUT /api/v3/agentic/fixLoopPolicy/global` |
| Remove the global policy | `DELETE /api/v3/agentic/fixLoopPolicy/global` |
| Create a project policy | `POST /api/v3/agentic/fixLoopPolicy/project` |
| Update a project policy | `PUT /api/v3/agentic/fixLoopPolicy/project` |
| Remove a project policy | `DELETE /api/v3/agentic/fixLoopPolicy/project?projectName=${PROJECT}` |

Global create and update requests use a JSON body in the
following format:

```
{
  "securityImpactThreshold": "High",
  "maxIterations": 5
}
```

Project create and update requests include the project name:

```
{
  "projectName": "${PROJECT}",
  "securityImpactThreshold": "High",
  "maxIterations": 5
}
```

Note:
Use `POST` to create a policy. Use
`PUT` to update an existing policy.

## Guardrails

Guardrails are natural-language instructions that Claude Code
interprets during a session. Guardrails can define security
requirements, compliance context, project conventions, scope
restrictions, behavioral constraints, and communication
requirements.

Write guardrails as direct, specific, and concise
instructions. For example, write
"Use parameterized SQL queries" instead of
"Parameterized SQL queries should be used".

Important:
Guardrails guide agent behavior but do not enforce
requirements programmatically. Use the scan policy for
programmatically evaluated workflow controls.

When guardrails exist at both global and project levels,
Coverity Connect appends the project guardrails to the global
guardrails. When guardrails exist at only one level, Coverity
Connect returns those guardrails.

## Guardrail APIs

| Operation | Method and endpoint |
| --- | --- |
| Retrieve global guardrails | `GET /api/v3/agentic/guardrails` |
| Retrieve guardrails for a project | `GET /api/v3/agentic/guardrails?projectName=${PROJECT}` |
| Create, update, or remove global guardrails | `POST|PUT|DELETE /api/v3/agentic/guardrails/global` |
| Create, update, or remove project guardrails | `POST|PUT|DELETE /api/v3/agentic/guardrails/project?projectName=${PROJECT}` |

Create and update requests use the
`file` multipart form field:

```
--form 'file=@"/path/to/guardrails.txt"'
```

Note:
Use `POST` to create guardrails. Use
`PUT` to update existing guardrails.

## Sigma scan configuration

Sigma scan configuration is a standard
`coverity.yaml` file. It defines what Sigma
analyzes and how Sigma performs the analysis.

The file can define the build system, programming language,
encoding, enabled and disabled checkers, included and excluded
files, and output settings.

You can reuse an existing `coverity.yaml` file
that contains the appropriate Sigma analysis settings. You do
not need to create a separate configuration format for
Agentic SAST workflows.

When configurations exist at both global and project levels,
Coverity Connect uses the project-specific configuration. When
configuration exists at only one level, Coverity Connect uses
that configuration.

## Sigma scan configuration APIs

| Operation | Method and endpoint |
| --- | --- |
| Retrieve global configuration | `GET /api/v3/agentic/sigmaConfig` |
| Retrieve configuration for a project | `GET /api/v3/agentic/sigmaConfig?projectName=${PROJECT}` |
| Create, update, or remove global configuration | `POST|PUT|DELETE /api/v3/agentic/sigmaConfig/global` |
| Create, update, or remove project configuration | `POST|PUT|DELETE /api/v3/agentic/sigmaConfig/project?projectName=${PROJECT}` |

Create and update requests use the
`file` multipart form field:

```
--form 'file=@"/path/to/coverity.yaml"'
```

Note:
Use `POST` to create configuration. Use
`PUT` to update existing configuration.
