---
title: "Coverity Checker Policy Enforcement overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/coverity-checker-policy-enforcement-overview.html"
content_id: "9A8vBD8TpinogXfjcOBnyQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.672097+00:00"
---

# Coverity Checker Policy Enforcement overview

Coverity Checker Policy Enforcement (CEP) gives administrators a central way to
define and enforce analysis configuration requirements across all teams and projects in a
Coverity Connect instance.

Without CEP, each developer or pipeline is responsible for running analysis with the
correct settings. CEP removes that dependency by letting administrators define required
analysis settings in a policy file, upload it to Coverity Connect, and have Coverity
Connect verify that scans comply before results are committed.

CEP answers the question: *Was this scan configured the way our organization
requires?*

## What CEP does

CEP enforces analysis consistency across teams, projects, and pipelines. Common uses
include:

- Requiring specific security checkers or checker sets
- Requiring coding-standard analysis, such as MISRA or AUTOSAR
- Restricting which analysis versions are allowed
- Ensuring that all scans include organization-required analysis settings

Users can check compliance before committing. Coverity Connect can also be configured
to reject or warn on non-compliant scans at commit time.

## What a policy is

A policy is a YAML or JSON file that defines the analysis settings a scan must
satisfy. A policy does not define how to run a full scan. It defines the requirements
that a scan configuration must meet.

At minimum, a policy must define at least one of the following top-level
elements:

- `versions` - the analysis versions allowed to run
- `require` - the analysis settings that must be present in the scan

Policy requirements can include explicit checker enablement, predefined checker sets,
coding standards, or specific analysis options. See Checker policy file reference.

## Policy scope

A policy can be scoped to the entire Coverity Connect instance or to a single
project.

Global
:   A global policy applies across all projects in the Coverity Connect instance. Use a global
    policy to define organization-wide baseline requirements, such as requiring
    security analysis, a minimum analysis version, or both.
:   Only one global policy can be active at a time.

Project
:   A project policy can be assigned to one or more projects. Use a project policy to add
    requirements on top of the global baseline, or to override global settings
    based on the configured precedence model. For example, a project might
    require MISRA analysis or OWASP Mobile Top 10 checks in addition to the
    global requirements.

Note: Stream-level policy is not supported in this release.

## Effective policy and precedence

When both a global policy and a project policy exist, Coverity Connect combines them
into an effective policy. The precedence setting determines
which scope takes priority when the two policies conflict.

| Precedence | Behavior |
| --- | --- |
| Top Down | Global policy takes precedence over project policy. This is the default. |
| Bottom Up | Project policy takes precedence over global policy. |

See Configuring checker policy precedence.

## How compliance checking works

A scan is compliant when its analysis configuration satisfies every requirement in
the effective policy. Compliance can be checked in two ways:

- Before committing, by using the CLI compliance check workflow
- At commit time, when Coverity Connect automatically checks the scan
  configuration against the effective policy

If a scan does not comply, Coverity Connect returns feedback that identifies which
setting failed and why.

## Non-compliance handling

Administrators configure what happens when Coverity Connect detects a non-compliant
scan at commit time.

| Option | Behavior |
| --- | --- |
| Reject | The commit is rejected and an error is returned identifying the non-compliant setting. The scan must be rerun with a compliant configuration before results can be committed. This is the default. |
| Warn and Accept | The commit is accepted, but Coverity Connect returns a warning that the scan configuration is non-compliant. |

Non-compliance handling is configured at the global level in this release. See Configuring non-compliance handling.

## In this section

- Checker policy file reference
- Creating a checker policy
- Setting the global checker policy
- Assigning a checker policy to a project
- Configuring checker policy precedence
- Configuring non-compliance handling
