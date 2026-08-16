---
title: "Complex type: streamDefectIdDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-streamdefectiddataobj.html"
content_id: "61UbPM1teM2_4H01O5Lqmw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:48.480152+00:00"
---

# Complex type: streamDefectIdDataObj

## Description

Identifier for a software issue within the scope of a stream.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| defectTriageId | long | Internal value for the last known triage ID. This ID changes when developers triage the issue that is associated with the *id*. |
| defectTriageVerNum | int | Internal value for the last known triage version. This number changes when developers triage the issue that is associated with the *id*. |
| id | long | Internal identifier for the software issue within the context of the stream. |
| verNum | int | Version number associated with the *id*. |
