---
title: "Operation: copyStream"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-copystream.html"
content_id: "vZN0GY9Brqb2HjXXnc_Jyg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:18.450731+00:00"
---

# Operation: copyStream

## Name

copyStream

## Description

Make a copy of a stream. Does not
copy stream role assignments.

## Parameters

projectId
:   **Type:** 
    projectIdDataObj

    Identifier for a project.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the project. |

sourceStreamId
:   **Type:** 
    streamIdDataObj

    Identifier for a stream.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the stream. |

## Output (Literal)

The output of this operation is the argument copyStreamResponse having the structure
defined by the following table.

| Name | Type |
| --- | --- |
| return | streamDataObj |

## Remarks

To assign roles or change the automatically generated stream name, stream
associations, and/or other stream properties, see updateStream().
