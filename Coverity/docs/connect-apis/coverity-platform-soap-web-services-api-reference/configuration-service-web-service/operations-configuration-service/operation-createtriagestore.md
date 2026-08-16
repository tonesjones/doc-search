---
title: "Operation: createTriageStore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-createtriagestore.html"
content_id: "I8eE5UswNdJn4jApvvIIfw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:29.347592+00:00"
---

# Operation: createTriageStore

## Name

createTriageStore

## Description

Create a triage store.

## Parameters

triageStoreSpec
:   **Type:** 
    triageStoreSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | description | string | Description of the triage store. |
    | name | string | Name of the triage store. Required with createTriageStore(). |
    | roleAssignments | roleAssignmentDataObj | Role to associate with the triage store at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations are allowed. If updating role assignments, respecify any that you want to retain. |
