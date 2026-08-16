---
title: "Operation: getTriageStores"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-gettriagestores.html"
content_id: "MUXZyndCyjANkSKiqFwFuw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:01.012261+00:00"
---

# Operation: getTriageStores

## Name

getTriageStores

## Description

Retrieve a set of triage store specifications, including stream associations.

## Parameters

filterSpec
:   **Type:** 
    triageStoreFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | descriptionPattern | string | Glob pattern matching the description of one or more triage stores. |
    | namePattern | string | Glob pattern matching one or more names of the set of triage stores to retrieve. |

## Output (Literal)

The output of this operation is the argument getTriageStoresResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | triageStoreDataObj |
