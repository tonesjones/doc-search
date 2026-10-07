---
title: "Complex type: componentPathRuleDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-componentpathruledataobj.html"
content_id: "z5jqVqxO2mqjg5qQQ93ohQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:22.787313+00:00"
---

# Complex type: componentPathRuleDataObj

## Description

Pattern used to match the path to one or more source code files associated with a
specified component.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| componentId | componentIdDataObj | Required. Name of the component to which the *pathPattern* applies. Takes the form *[componentMapName.componentName]*. |
| pathPattern | string | Required. Path to one or more associated source code files. |
