---
title: "Complex type: usersPageDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-userspagedataobj.html"
content_id: "KHKPapXiq8vFYFscGXoeLQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:09.581966+00:00"
---

# Complex type: usersPageDataObj

## Description

Returned page of user records and count of records in the page.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| users | userDataObj | A user record. Zero or more can be returned. |
| totalNumberOfRecords | int | Total number of user records returned. |
