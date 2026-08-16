---
title: "Operation: updateTriageStore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-updatetriagestore.html"
content_id: "0NCyK7hUeGq0MoJyYZeypg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:16.164263+00:00"
---

# Operation: updateTriageStore

## Name

updateTriageStore

## Description

Update a triage store specification.

## Parameters

triageStoreId
:   **Type:** 
    triageStoreIdDataObj

    Identifier for a triage store.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the triage store. |

triageStoreSpec
:   **Type:** 
    triageStoreSpecDataObj

    Specification for a triage store.

    | Field name | Type | Description |
    | --- | --- | --- |
    | description | string | Description of the triage store. |
    | name | string | Name of the triage store. Required with createTriageStore(). |
    | roleAssignments | roleAssignmentDataObj | Role to associate with the triage store at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations are allowed. If updating role assignments, respecify any that you want to retain. |
