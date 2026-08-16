---
title: "Complex type: projectScopeDefectFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-projectscopedefectfilterspecdataobj.html"
content_id: "2U4CpecdrjgVTVxho7sGuA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:41.164948+00:00"
---

# Complex type: projectScopeDefectFilterSpecDataObj

## Description

Passes optional filter properties matching the issues to return.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| actionNameList | string | Name/value pairs for a list of attributes. |
| checkerCategoryList | string | List of checker categories. |
| checkerList | string | List of checkers. |
| checkerTypeList | string | List of checker types. |
| cidList | long | List of CIDs. |
| classificationNameList | string | Classification of the CID. Multiple classifications allowed. |
| componentIdExclude | boolean | If one or more component name filters is specified, set to *true* to exclude matching results from the specified components. Defaults to *false*, including the matches from the components in the results. |
| componentIdList | componentIdDataObj | Name of a component that contains the CID. Multiple components allowed. |
| cweList | long | Common Weakness Enumeration identifier of the type of issue found by the checker. Zero or more identifiers allowed. |
| firstDetectedBy | string | Value that helps identify the process by which an issue was *initially reported* to Coverity Connect: **COMMIT**(for issues initially reported through a commit process that yields a snapshot; appears as "**Snapshot**" in the UI), **PREVIEW_REPORT** (for issues initially reported through a preview process, which does not produce a snapshot, for example, when Coverity Desktop invokes `cov-run-desktop`), or **API** (for issues initially reported through a special, rarely used process). In each case, a CID for the issue is created. Notes: Preview issues that a developer fixes before pushing code changes to the source code repository will never have (or need) a snapshot. Preview issues left unfixed before they are pushed to the repository will typically undergo the server-based analysis and commit process. Therefore, these issues will receive a snapshot in Coverity Connect *after* they are initially reported.Whether fixed or left unfixed prior to the push to the source code repository, issues will be identified as Preview issues if they were initially reported through a preview process. |
| firstDetectedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the First Detected date of a CID.Example1:2013-03-18T12:42:19.384-07:00Example2:2013-03-18 |
| firstDetectedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the First Detected date of a CID. For an example, see firstDetectedEndDate. |
| fixTargetNameList | string | Fix target for the CID; a triage value for the CID. Multiple fix targets allowed. |
| impactNameList | string | Probable impact (High, Medium, or Low) of the issue found by the checker. Zero or more impact levels allowed. |
| issueKindList | string | Issue kind. Multiple issue kinds allowed. |
| lastDetectedEndDate | dateTime | Ending date (and optionally, time) for the date range matching the Last Detected date of a CID.For an example, see firstDetectedEndDate. |
| lastDetectedStartDate | dateTime | Starting date (and optionally, time) for the date range matching the Last Detected date of a CID.For an example, see firstDetectedEndDate. |
| legacyNameList | string | Legacy designation for the CID (true or false), a triage value for the CID. Built-in attribute. Defaults to false. |
| ownerNameList | string | Owner of the CID. |
| ownerNamePattern | string | Glob pattern matching the first or last name of the owner of a CID. |
| severityNameList | string | Severity of the CID; a triage value for the CID. Multiple severities allowed. |
