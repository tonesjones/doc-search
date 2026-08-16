---
title: "Operation: updateSnapshotInfo"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-updatesnapshotinfo.html"
content_id: "EepGCgVOQ4Fc1BsVUMowAQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:14.866322+00:00"
---

# Operation: updateSnapshotInfo

## Name

updateSnapshotInfo

## Description

Update a snapshot.

## Parameters

snapshotId
:   **Type:** 
    snapshotIdDataObj

    Identifier for a snapshot.

    | Field name | Type | Description |
    | --- | --- | --- |
    | id | long | Numeric identifier for the snapshot. Required. |

snapshotData
:   **Type:** 
    snapshotInfoDataObj

    Specification for snapshot information.

    | Field name | Type | Description |
    | --- | --- | --- |
    | analysisCommandLine | string | Command line used when running the analysis of the source code associated with the snapshot. |
    | analysisConfiguration | string | Configuration file used when running the analysis of the source code associated with the snapshot. |
    | analysisHost | string | Name of the host machine used to run the analysis of the source code associated with the snapshot. |
    | analysisIntermediateDir | string | Intermediate directory that contained the analysis results committed in this snapshot. |
    | analysisInternalVersion | string | Internal version of Coverity Analysis used to run the analysis. |
    | analysisTime | long | Duration of the analysis in seconds. |
    | analysisVersion | string | Licensed version of Coverity Analysis used to run the analysis. |
    | buildCommandLine | string | Build command used to compile the source code for analysis. |
    | buildConfiguration | string | Configuration file used when compiling source code for analysis. |
    | buildHost | string | Host machine used to run the build. |
    | buildIntermediateDir | string | Intermediate directory into which the build was emitted. |
    | buildTime | long | Duration of the build. |
    | codeVersionDate | dateTime | Date and time of the analyzed code version according to the source control system, or if that is not available, the date and time when the build was captured. |
    | commitUser | string | Username of user who committed the analysis results to the database. |
    | dateCreated | dateTime | Date and time that the snapshot was created in the database. |
    | description | string | Description of the snapshot. |
    | enabledCheckers | string | List of checkers that were used in the analysis. |
    | hasSummaries | boolean | True if this snapshot contains interprocedural analysis summaries that can be used to accurately analyze subsets of the code in isolation. |
    | impactHashVersion | int | Internal field. |
    | portableAnalysisSettings | string | This field contains information about the analysis settings used to create the snapshot, and is used by Desktop Analysis to imitate those settings. It is only meant to be used by cov-run-desktop and its format is subject to change. |
    | purgedOfDetails | boolean | Value of *true* if the snapshot details have been purged. |
    | snapshotId | snapshotIdDataObj | Identifier for the snapshot. |
    | sourceVersion | string | Version  of the source code. Present only if passed when committing analysis results (passed by the *--version* option of cov-commit-defects command). |
    | target | string | Target platform of the source code (for example, i386). Present only if passed when committing analysis results (passed by the *--target* option of the cov-commit-defects command). |
