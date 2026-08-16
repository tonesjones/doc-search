---
title: "Complex type: componentMapDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-componentmapdataobj.html"
content_id: "PJPG3Rpxk27C8zAdsxTLGw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:26.779489+00:00"
---

# Complex type: componentMapDataObj

## Description

Returns component map data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| componentMapId | componentMapIdDataObj | Name of the component map. |
| componentPathRules | componentPathRuleDataObj | Path to set of files that are associated with a component of the component map. Multiple paths are possible. |
| components | componentDataObj | Component associated with a component map. Multiple component associations allowed. |
| defectRules | componentDefectRuleDataObj | Default owner of CIDs associated with the specified component. |
| description | string | Description of the component map. |
