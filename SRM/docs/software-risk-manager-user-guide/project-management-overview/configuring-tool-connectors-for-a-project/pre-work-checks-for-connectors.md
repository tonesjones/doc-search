---
title: "Pre-Work Checks for Connectors"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/pre-work-checks-for-connectors.html"
content_id: "qsEDXlSphj81TOIekH0OiA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:13.045175+00:00"
content_hash: "cb1e2266079ca51ba2dd4a47a7f053cb5c102f5e7bc05d8feb93b43cce10afb1"
---

# Pre-Work Checks for Connectors

Pre-work checks allow supported tool connectors to query their remote tool before
scheduling an auto-update analysis, so that analyses are skipped when there is no new work
to retrieve.

## Overview

Pre-work checks (PWC) apply to some connectors when the connector is run at a regular
interval.

Note: Pre-work checks do not apply to raw connector inputs or to connectors run as part
of a normal (non-scheduled) analysis.

Before scheduling a connector analysis, SRM queries the remote tool to determine
whether new work is available. If the remote tool reports no changes since the last
completed analysis, SRM skips the analysis entirely. This avoids creating
unnecessary analyses and reduces load on the remote tool's API.

A pre-work check is skipped (and the analysis always runs) when any of the following
apply:

- The global PWC property `ingestion.skip-connector-work-checks`
  is enabled (set to `true`).
- Pre-work checks are disabled for that connector via its connector-specific
  property (see below).
- The target SRM branch does not yet exist.
- No previous analysis exists for the connector; SRM always runs an initial
  analysis.
- The connector configuration was modified after the last analysis completed; SRM
  treats this as a signal that new work may be available.

## Internal Properties

Pre-work check behavior is controlled through internal properties set in
`codedx.props`.

`ingestion.skip-connector-work-checks` [default: `false`]
:   When set to `true`, globally disables all pre-work checks
    regardless of connector-specific settings. When `false`
    (default), pre-work checks are allowed to run for connectors that support
    them.

HCL AppScan Enterprise - `ase.enable-work-pre-check` [default: `true`]
:   Toggles PWC behavior for HCL AppScan Enterprise.

HCL AppScan on Cloud (ASoC) - `asoc.enable-work-precheck` [default: `false`]
:   Toggles PWC behavior for HCL AppScan on Cloud (ASoC). Disabled by default
    because the PWC is not comprehensive.

Black Duck SCA - `blackduck.enable-work-precheck` [default: `true`]
:   Toggles PWC behavior for Black Duck SCA.

Coverity - `coverity.enable-work-precheck` [default: `false`]
:   Toggles PWC behavior for Coverity Connect. Disabled by default because the
    PWC is not comprehensive; it will not handle changes to triage stores or
    component maps in Coverity.

SonarQube / SonarCloud - `sonarqube.enable-work-precheck` [default: `true`]
:   Toggles PWC behavior for SonarQube / SonarCloud.

Sonatype Nexus - `sonatype.enable-work-precheck` [default: `true`]
:   Toggles PWC behavior for Sonatype Nexus.

Invicti Enterprise - `invictienterprise.enable-work-precheck` [default: `false`]
:   Toggles PWC behavior for Invicti Enterprise. Disabled by default.

Acunetix 360 - `acunetix360.enable-work-precheck` [default: `false`]
:   Toggles PWC behavior for Acunetix 360. Disabled by default.

**Related concepts**  

- Scheduling Auto-Update Analyses
