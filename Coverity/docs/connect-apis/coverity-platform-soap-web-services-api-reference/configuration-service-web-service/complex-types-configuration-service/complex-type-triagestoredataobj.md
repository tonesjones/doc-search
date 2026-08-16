---
title: "Complex type: triageStoreDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-triagestoredataobj.html"
content_id: "xE1ojxxxRKeF3h71cb~_Ng"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:05.691560+00:00"
---

# Complex type: triageStoreDataObj

## Description

Returns triage store properties.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| roleAssignments | roleAssignmentDataObj | Set of roles assigned to the retrieved triage store. |
| description | string | Description of the triage store. |
| id | triageStoreIdDataObj | Name of a retrieved triage store. |
| streamIds | streamIdDataObj | Identifier for a stream associated with the specified triage store. |
