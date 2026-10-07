---
title: "Complex type: triageHistoryDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-triagehistorydataobj.html"
content_id: "EV3G8zw8a5yiY_PD7WMYSw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:27.850613+00:00"
---

# Complex type: triageHistoryDataObj

## Description

Data object that capture state of triage attributes for a CID at a given point in
time. For example, if a developer desginates a new CID as a bug, the triage state
changes.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| attributes | defectStateAttributeValueDataObj | Triage attributes and values. |
| id | long | Identifier that groups a set of triage changes. |
