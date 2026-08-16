---
title: "Complex type: groupsPageDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-groupspagedataobj.html"
content_id: "NmQ6p622EgCHG8QVjmrksQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:35.981794+00:00"
---

# Complex type: groupsPageDataObj

## Description

Returned page of group records that includes the total number of records.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| groups | groupDataObj | List of user groups returned by the request. |
| totalNumberOfRecords | int | Total number of group records returned. |
