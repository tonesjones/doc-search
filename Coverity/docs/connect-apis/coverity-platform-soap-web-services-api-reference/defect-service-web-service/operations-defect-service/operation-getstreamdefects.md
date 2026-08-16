---
title: "Operation: getStreamDefects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getstreamdefects.html"
content_id: "X3bLIWcQD4mzZBdT~Vr1sg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:19.047039+00:00"
---

# Operation: getStreamDefects

## Name

getStreamDefects

## Description

Retrieve instances of software issues for one or more CIDs.

## Parameters

mergedDefectIdDataObjs
:   **Type:** 
    mergedDefectIdDataObj

    Identifier for a software issue. A cid and/or mergeKey is required.
    Multiple specifications are allowed, up to a limit of 100.

    | Field name | Type | Description |
    | --- | --- | --- |
    | cid | long | CID. |
    | mergeKey | string | Numeric key for a CID. |

filterSpec
:   **Type:** 
    streamDefectFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | defectStateEndDate | dateTime | Ending date (and optionally, time) for the CIDs to return. |
    | defectStateStartDate | dateTime | Starting date (and optionally, time) for the CIDs to return. |
    | includeDefectInstances | boolean | Set to *true* for data on each instance of software issue, including the ID. Defaults to *false*. |
    | includeHistory | boolean | Set to *true* for historical triage data on each instance of the software issue. |
    | streamIdList | streamIdDataObj | Identifier for a stream. Multiple streams allowed. |

## Output (literal)

The output of this operation is the argument getStreamDefectsResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | streamDefectDataObj |
