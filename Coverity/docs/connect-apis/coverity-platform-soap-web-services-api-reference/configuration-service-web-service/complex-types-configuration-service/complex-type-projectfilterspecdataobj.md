---
title: "Complex type: projectFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-projectfilterspecdataobj.html"
content_id: "mVfoxHCbyd9zX2L7vakuzA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:44.703391+00:00"
---

# Complex type: projectFilterSpecDataObj

## Description

Filter properties used to return a matching set of projects.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| descriptionPattern | string | Glob pattern matching the description of one or more projects. |
| includeChildren | boolean | Value of *false* if the results *should not* include roles and other properties associated with the project. Defaults to *true*. |
| includeStreams | boolean | Value of *false* if the results *should not* include streams associated with the project. Defaults to true. |
| namePattern | string | Glob pattern matching the name of one or more projects. |
