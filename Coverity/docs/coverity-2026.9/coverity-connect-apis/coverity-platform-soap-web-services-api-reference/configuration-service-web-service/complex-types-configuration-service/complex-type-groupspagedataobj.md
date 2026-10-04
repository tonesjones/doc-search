---
title: "Complex type: groupsPageDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-groupspagedataobj.html"
content_id: "NmQ6p622EgCHG8QVjmrksQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:23.217023+00:00"
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
