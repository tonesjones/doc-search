---
title: "DesktopAnalysisSettings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/desktopanalysissettings.html"
content_id: "T~MIGf5GzRTYZ0i7yWJg_Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:09.720847+00:00"
---

# DesktopAnalysisSettings

This object captures the main inputs to `cov-run-desktop`.

analysisDateTime: string
:   The date/time of the `cov-run-desktop` invocation that
    produced the present JSON output file.

covRunDesktopArgs: [string]
:   The command line arguments to `cov-run-desktop` that produced the present
    output file, with any `--password` argument removed.

effectiveStripPaths: [string]
:   The set of effective strip paths.

analysisScopePathnames: [string]
:   The set of source file pathnames defining the analysis scope. These paths
    are not stripped.

strippedAnalysisScopePathnames: [string]
:   The stripped version of `analysisScopePathnames`.

auxiliaryScopePathnames: [string]
:   The set of primary source file pathnames of translation units that were
    analyzed in addition to `analysisScopePathnames` for the
    purpose of enabling analysis of something in that set. Defects in the
    auxiliary scope are not reported.

strippedAuxiliaryScopePathnames: [string]
:   The stripped version of `auxiliaryScopePathnames`.

referenceSnapshot: ReferenceSnapshotDetails
:   If a reference snapshot is specified or inferred, this object contains
    details about the snapshot. This object is described in the ReferenceSnapshotDetails
    section.

effectiveAnalysisSettings: PortableAnalysisSettings
:   The core analysis settings used for this invocation of
    `cov-run-desktop`. These are the effective combination
    of the settings retrieved from Coverity Connect (if any) and the settings
    specified on the `cov-run-desktop` command line (if any).
    See PortableAnalysisSettings.

relativeTo: string
:   If present, this corresponds to `--relative-paths --relative-to
    relativeTo`. If absent, this corresponds
    to `--relative-to false`.

intermediateDir: string
:   The intermediate directory used by `cov-run-desktop`.
    Added in version 3.
