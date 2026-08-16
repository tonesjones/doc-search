---
title: "Operation: getDeveloperStreamsProjects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getdeveloperstreamsprojects.html"
content_id: "MKHq41Whj7PVqjPTjauQMw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:47.277202+00:00"
---

# Operation: getDeveloperStreamsProjects

## Name

getDeveloperStreamsProjects

## Description

Get a list of project specifications in developer streams (for all such projects or
for a filtered set of such projects).

## Parameters

filterSpec
:   **Type:** 
    projectFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | descriptionPattern | string | Glob pattern matching the description of one or more projects. |
    | includeChildren | boolean | Value of *false* if the results *should not* include roles and other properties associated with the project. Defaults to *true*. |
    | includeStreams | boolean | Value of *false* if the results *should not* include streams associated with the project. Defaults to true. |
    | namePattern | string | Glob pattern matching the name of one or more projects. |

## Output (Literal)

The output of this operation is the argument getProjectsResponse having the structure
defined by the following table.

| Name | Type |
| --- | --- |
| return | projectDataObj |

## Remarks

When the name and description filters are both specified, both patterns must match
the project for the project to return in the resulting list.
