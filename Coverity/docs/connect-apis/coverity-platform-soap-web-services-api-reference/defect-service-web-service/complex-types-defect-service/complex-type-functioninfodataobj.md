---
title: "Complex type: functionInfoDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-functioninfodataobj.html"
content_id: "Jp5x18ELylfmJkrIVT44PA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:34.964482+00:00"
---

# Complex type: functionInfoDataObj

## Description

Returns data on a function or method.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| fileId | fileIdDataObj | Identifier for the file in which the function or method occurs. |
| functionDisplayName | string | Name of the function or method that is displayed in the UI. |
| functionMangledName | string | Mangled name of the function or method. |
| functionMergeName | string |  |
