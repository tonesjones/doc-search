---
title: "Complex type: componentDefectRuleDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-componentdefectruledataobj.html"
content_id: "1Q22hH8OdfyW~WgKeovQoQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:25.463430+00:00"
---

# Complex type: componentDefectRuleDataObj

## Description

Rule that assigns an owner to the software issues found in a specified component.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| componentId | componentIdDataObj | Component to which the defect rule applies. |
| defaultOwner | string | Default owner of the component. |
