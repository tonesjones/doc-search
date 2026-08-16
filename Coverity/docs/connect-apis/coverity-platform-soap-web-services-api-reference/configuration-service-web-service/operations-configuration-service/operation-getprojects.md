---
title: "Operation: getProjects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getprojects.html"
content_id: "~h9sUtHngdqk27AJfU7FJw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:53.189908+00:00"
---

# Operation: getProjects

## Name

getProjects

## Description

Get a list of project specifications (for all projects or for a filtered set of
projects).

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
