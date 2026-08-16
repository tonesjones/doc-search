---
title: "Operation: getTrendRecordsForProject"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-gettrendrecordsforproject.html"
content_id: "Na~H0WRdyGjOhLpfbR1QMQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:19.691965+00:00"
---

# Operation: getTrendRecordsForProject

## Name

getTrendRecordsForProject

## Description

Retrieve daily records on CIDs and source code in a project.

## Parameters

projectId
:   **Type:** 
    projectIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the project. |

filterSpec
:   **Type:** 
    projectTrendRecordFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | endDate | dateTime | End date (and optionally, time) for the set of records to retrieve. |
    | startDate | dateTime | Start date (and optionally, time) for the set of records to retrieve. |

## Output (literal)

The output of this operation is the argument getTrendRecordsForProjectResponse having
the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | projectMetricsDataObj |
