---
title: "Complex type: triageStoreSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-triagestorespecdataobj.html"
content_id: "vUb_D8ISBRXnq6xNe4ELug"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:07.630270+00:00"
---

# Complex type: triageStoreSpecDataObj

## Description

Specification of a triage store.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| description | string | Description of the triage store. |
| name | string | Name of the triage store. Required with createTriageStore(). |
| roleAssignments | roleAssignmentDataObj | Role to associate with the triage store at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations are allowed. If updating role assignments, respecify any that you want to retain. |
