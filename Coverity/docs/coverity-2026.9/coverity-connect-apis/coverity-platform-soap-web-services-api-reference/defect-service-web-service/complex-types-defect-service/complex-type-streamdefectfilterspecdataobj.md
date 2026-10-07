---
title: "Complex type: streamDefectFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-streamdefectfilterspecdataobj.html"
content_id: "AjS75GrHK6XSdRFDGWYROQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:27.718302+00:00"
---

# Complex type: streamDefectFilterSpecDataObj

## Description

Filter used to return matching software issues within the scope of one or more
streams.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| defectStateEndDate | dateTime | Ending date (and optionally, time) for the CIDs to return. |
| defectStateStartDate | dateTime | Starting date (and optionally, time) for the CIDs to return. |
| includeDefectInstances | boolean | Set to *true* for data on each instance of software issue, including the ID. Defaults to *false*. |
| includeHistory | boolean | Set to *true* for historical triage data on each instance of the software issue. |
| streamIdList | streamIdDataObj | Identifier for a stream. Multiple streams allowed. |
