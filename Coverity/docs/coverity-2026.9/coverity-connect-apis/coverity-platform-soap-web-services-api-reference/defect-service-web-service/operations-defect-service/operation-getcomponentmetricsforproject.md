---
title: "Operation: getComponentMetricsForProject"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-getcomponentmetricsforproject.html"
content_id: "guIJ9OjcvKyI7CtJNhRMGQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:25.387729+00:00"
---

# Operation: getComponentMetricsForProject

## Name

getComponentMetricsForProject

## Description

Retrieve metrics on components associated with streams in a specified project.

## Parameters

projectId
:   **Type:** 
    projectIdDataObj

    Identifier for a project.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the project. |

componentIds
:   **Type:** 
    componentIdDataObj

    Identifier for a component.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Name of a component in the project in the form **[componentMap].[component]** (for example, *myComponentMap.myComponent*) Multiple names allowed. |

## Output (literal)

The output of this operation is the argument getComponentMetricsForProjectResponse
having the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | componentMetricsDataObj |
