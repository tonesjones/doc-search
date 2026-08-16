---
title: "Rapid Scan Overview"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/rapid-scan-overview.html"
content_id: "1LafzLf4Lx8IiO4B~GvnIw"
version: "2026.7"
section: "Scanning Best Practices"
scraped_at: "2026-08-08T15:34:29.704231+00:00"
---

# Rapid Scan Overview

Rapid Scan SCA is a new way of scanning within Black Duck. This mode is designed to be as
fast as possible and support developer workflows without persisting any data on Black
Duck.

It is enabled by adding `--detect.blackduck.scan.mode=RAPID` to a run of
detect.

Unlike existing scans, no data is retained on Black Duck and all scans are done
transiently. These scans are primarily intended to be fast. The results are saved to a
json file in the Scan Output directory, where name and version are the project's name
and version.

Rapid Scan relies on Black Duck policies to produce SCA acceptance testing results which
can be integrated into developer pipelines. Rapid Scan only reports components that
violates policies. If no policies are violated or there are no defined policies, then no
components are returned.

By default, rapid scan will fail with `FAILURE_POLICY_VIOLATION` if any
component violate polices with a CRITICAL or BLOCKER severity

The results are also printed in the logs, looks like:

  
 [image: image]   

enabled by adding `--detect.blackduck.scan.mode=RAPID` to a run of
detect.

Rapid scanning will check for violations based on Component Conditions, Vulnerability
Conditions, and License conditions and a Json file to summarize and provide more details
generated.

## Rapid Scanning Best Practices

Rapid mode is primarily meant for developers or devops processes used in the
development stage. The intention is to provide development teams with quick access
to high fidelity Black Duck results without being a bottleneck in development
speed.

Black Duck Rapid Scan enables developers to get Black Duck results extremely quickly,
and it supports thousands of scans per hour. Rapid Scan is focused on package
managers and component security. It works in together with Black Duck Policy Rules,
so developers can quickly see if any policy violations will be introduced when
checking-in their work. Companies can also implement this scan model as part of
their CI / CD pipeline.

## Use case for Developers

Unlike existing Black Duck scans, no data is persisted on Black Duck once scans
are completed. These scans are primarily intended to be fast and integrated into
developer workflows. The best practice is to use rapid scan mode to quickly fail
a build if any policy violations are introduced in the code in the development
stage. The results show the developer which policies have been violated, and
which declared OSS components are in violation. Rapid Scan can also fail a
build, for Blocker or Critical policy violations. Rapid scanning will check for
violations based on Component Conditions, Vulnerability Conditions, and License
conditions.

## Rapid Scan specific policies

With Rapid Scan specific policies in Black Duck, a rapid scan can be configured
to fail a build on specific policy violation conditions catered to Rapid Scan
only. For example, if an organization wants to ensure that no code with
component vulnerability score of 5 and above should be merged in the development
stage, they can create a Rapid scan specific policy and builds will fail in
Detect when triggered.

## Rapid Scan policy overrides

Policy overrides for a rapid scan can be provided using a scan custom config file, provided in
a file named `.bd-rapid-scan.yaml` in the source directory. The file
name must match exactly. Please see the [Configuration section of Detect's Rapid
Scan](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/16b47cf72e7785e85fb3e64045f06e06.topic) page for an example of the `bd-rapid-scan.yaml`
file.

This provides additional flexibility for organizations on their usage and
implementation, or relaxation of build break rules based on rapid scan policy
violations.

## Rapid scan differential feature: Only show NEW violations since the last full scan

With this functionality, organizations can now rapidly find out if new violations
have been introduced since the branch was scanned with the full scan, i.e.
compare against a project version on Hub. They can fail a build only if there
are new issues introduced by a branch.

If the policy violation was already known and visible in the project version's
component page (active or overridden), it will not be considered in the Rapid
Scan results. Only new violations found in the scanned project are returned.

By using the `X-BD-RAPID-SCAN-MODE` header or detect option
`detect.blackduck.rapid.compare.mode` and providing it one of the
values below, you can change the Rapid Scan mode.

Set the compare mode of rapid scan:

- `ALL`: The default operation. It will evaluate policy rules
  that are `RAPID` or (`RAPID` and
  `FULL`). When the header is absent, this is the default
  behaviour.

- `BOM_COMPARE`: Will evaluate policy rules like the
  `ALL` option, but will now evaluate differently based on
  the type of policy rule modes. When the policy rule is
  (`RAPID` and `FULL`) it will behave like
  `BOM_COMPARE_STRICT` but if the policy rule is only
  (`RAPID`) it will evaluate the result of the rapid scan
  against the policy ignoring results in the BOM.

- `BOM_COMPARE_STRICT`: Will only evaluate policy rules that are
  (`RAPID` and `FULL`). Policy violations
  are compared to the existing project version BOM. If the policy violation
  was already known and visible in the BOM (active or overridden) it is not
  part of the rapid scan positive result, it will still be part of the full
  result following existing restrictions.

In order to run either of the `BOM_COMPARE` modes there must be an
existing project version in HUB.

## When NOT to run Rapid scan?

Rapid scan does not create a Project or Version on Black Duck, so it is not meant
to run to generate a BOM. It cannot create a Risk or Notices report.

## Interactive Tutorial

Explore this [interactive tutorial](https://ior.ad/7Jow?iframeHash=trysteps-1) to try out Black Duck's Rapid
Scan.
