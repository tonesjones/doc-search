---
title: "Complex type: licenseDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-licensedataobj.html"
content_id: "0y2G9Y9yLqAm8PONnbnU2A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:38.808120+00:00"
---

# Complex type: licenseDataObj

## Description

Specification for license data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| customer | string | Customer name. |
| expirationDate | dateTime | Expiration date. |
| licenseEditionName | string | License type. Coverity component availability varies by license edition. |
| loc | long | Lines of code analyzed. |
| locLimit | long | Maximum lines of code allowed by the license. |
| userCount | int | Current number of users added to Coverity Connect. |
| userLimit | string | Maximum number of users allowed. |
