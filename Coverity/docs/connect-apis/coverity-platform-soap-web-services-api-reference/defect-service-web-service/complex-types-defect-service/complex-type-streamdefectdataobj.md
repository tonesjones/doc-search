---
title: "Complex type: streamDefectDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-streamdefectdataobj.html"
content_id: "4nLurMVolt2Y2WLzFRUbRA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:47.198263+00:00"
---

# Complex type: streamDefectDataObj

## Description

Returns data on a CID within the context of a stream.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| checkerName | string | Name of the checker that found the issue. |
| cid | long | CID of the software issue. |
| defectInstances | defectInstanceDataObj | Data on an instance of a software issue. |
| defectStateAttributeValues | defectStateAttributeValueDataObj | Triage attribute/value pair for a software issue. |
| domain | string | Domain of the issue. |
| history | defectStateDataObj | Historical triage data on an instance of a software issue. |
| id | streamDefectIdDataObj | Identifier for the software issue within the scope of a stream. |
| streamId | streamIdDataObj | Identifier for the stream in which the issue occurs. |
