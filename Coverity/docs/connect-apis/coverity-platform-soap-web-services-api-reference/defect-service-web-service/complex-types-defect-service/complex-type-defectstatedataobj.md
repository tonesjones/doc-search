---
title: "Complex type: defectStateDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-defectstatedataobj.html"
content_id: "QMFA9GDOM43y~H6oKMkBJg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:31.032196+00:00"
---

# Complex type: defectStateDataObj

## Description

Returns historical triage data on a software issue.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| dateCreated | dateTime | Date and time that one or more attribute values were created or updated. |
| defectStateAttributeValues | defectStateAttributeValueDataObj | Set of attribute/value pairs for a software issue. |
| userCreated | string | Username of the user who updated the attribute values. |
