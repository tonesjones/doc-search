---
title: "CoverityIssues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverityissues.html"
content_id: "TtzTsNk6osk8qRzBAUs_Ig"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:04.555481+00:00"
---

# CoverityIssues

This is the outermost object of the JSON output file, acting as an envelope with type and
version information. It contains the following elements:

type: string
:   A string identifying the type of object contained in the file in order to assist tools in
    diagnosing cases where the wrong data or version is provided as input.

formatVersion: int
:   An integer identifying the version of the file/object format.

suppressedIssueCount: int
:   The number of issues that were detected but not output because of filters.

issues: [IssueOccurrence]
:   A list of issue occurrences, each of which has several attributes described in the IssueOccurrence section. The order of
    this list is determined by the `--sort` option (see the `cov-run-desktop`
    command in the Coverity 2026.6.0 Command Reference).

desktopAnalysisSettings: DesktopAnalysisSettings
:   A list of the settings used to perform the desktop analysis. The values are described in
    the  DesktopAnalysisSettings
    section.

error?: Error
:   Indicates that we encountered an error; in this case, issues will be empty.

warnings[]: Error
:   Indicates warnings, if any, that were produced by this run. Added in version 6. (The
    attribute `hadMissingSummaries` was subsumed by
    `warnings`, and was removed in version 6.)
