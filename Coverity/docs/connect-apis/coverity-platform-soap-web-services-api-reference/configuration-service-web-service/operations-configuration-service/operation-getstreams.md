---
title: "Operation: getStreams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getstreams.html"
content_id: "eewMiy1nmStbOnu0mGGKuA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:59.732854+00:00"
---

# Operation: getStreams

## Name

getStreams

## Description

Retrieve a set of streams.

## Parameters

filterSpec
:   **Type:** 
    streamFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | languageList | string | Programming language matching that of one or more streams. Zero or more language filters allowed. |
    | descriptionPattern | string | Glob pattern matching the description of one or more streams. |
    | namePattern | string | Glob pattern matching the name of one or more streams. |

## Output (Literal)

The output of this operation is the argument getStreamsResponse having the structure
defined by the following table.

| Name | Type |
| --- | --- |
| return | streamDataObj |
