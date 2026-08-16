---
title: "Complex type: pageSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-pagespecdataobj.html"
content_id: "x1fPUXsGgYUpLmQOaO7cuA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:39.108224+00:00"
---

# Complex type: pageSpecDataObj

## Description

Specification for the page of records to return.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| pageSize | int | Required. Up to 5000 records per page. |
| sortAscending | boolean | Set to *false* to return records in reverse alphabetical or numerical order. Defaults to *true*. |
| sortField | string | Name of the field to use for sorting results. Not all fields are supported. However, you can typically sort by a field that returns numeric results, such as cid and the date fields. |
| startIndex | int | Zero-based index of records to return. Defaults to *0*. |
