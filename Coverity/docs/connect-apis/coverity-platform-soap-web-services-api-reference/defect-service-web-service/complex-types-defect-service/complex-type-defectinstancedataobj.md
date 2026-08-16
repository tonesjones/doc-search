---
title: "Complex type: defectInstanceDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-defectinstancedataobj.html"
content_id: "HqqwKg~ThliZuJ0yHZ_SSQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:29.054494+00:00"
---

# Complex type: defectInstanceDataObj

## Description

Returns data on an instance of a software issue.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| events | eventDataObj | Data on an event that contributed to a software issue. Multiple events are possible. |
| properties | propertyDataObj | A key/value pair for a property of an instance of a software issue. |
| category | localizedValueDataObj | Categorization of the software issue. |
| checkerName | string | Name of the checker that found the issue. |
| component | string |  |
| cwe | int | Common Weakness Enumeration identifier of the type of the issue. |
| domain | string | Domain of the checker. |
| eventSetCaptions | string | Description available for occurrences of the software issue. Such captions appear in the UI above enumerated instances. |
| extra | string | Internal. Used to associate instance of the same CID. |
| function | functionInfoDataObj | Data on the function or method that contains the software issue. |
| id | defectInstanceIdDataObj | Identifier for an instance of a software issue. |
| impact | localizedValueDataObj | Probable impact of the software issue. |
| issueKinds | localizedValueDataObj | Kind of the issue. |
| localEffect | string | Local effect of the issue. |
| longDescription | string | Full description of the software issue. |
| subcategory | string |  |
| type | localizedValueDataObj | Name of the issue type. |
