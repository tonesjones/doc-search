---
title: "Complex type: pageSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-pagespecdataobj.html"
content_id: "ztnFWuprI4FqVH0dqKYZEQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:42.744728+00:00"
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
| pageSize | int | Required. Number of records to return. Maximum of 1000. |
| sortAscending | boolean | Set to *false* to return records in reverse alphabetical or numerical order. Defaults to *true*. |
| sortField | string | Do not specify with getGroups(). Name of the field to use for sorting results. For example, the dateCreated or familyName field for user records returned by getUsers(). You cannot sort by a field that can appear mulitple times for a single record (for example, a single user record can have multiple group fields). For examples of sortField values, see the remark for this data object. |
| startIndex | int | Zero-based index of user records to return. Defaults to *0*. You might use this field if there are more than 1000 users. You could make separate calls that start the index at 1000 or 2000, for example, until you capture separate lists of all of the users. |

## Remarks

A complete list of sortList values is not available at this time. In general, the
following sort field values are valid when getting merged defects: action,
classification, severity, status, id, Fix Target, displayFunction, Legacy,
displayFile, component, lastDetected, lastTriaged, lastFixed, firstDetected, owner,
Ext. Reference, checker. In addition, custom attribute names are valid. The filters
available are generally limited to the attributes available in the query. So
snapshot scope does not have a lastDetected field, but project scope does.
