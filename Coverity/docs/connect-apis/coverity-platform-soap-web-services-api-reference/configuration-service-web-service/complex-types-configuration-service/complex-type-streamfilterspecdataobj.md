---
title: "Complex type: streamFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-streamfilterspecdataobj.html"
content_id: "A8L8_jmuCla49svASLv4PQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:03.619103+00:00"
---

# Complex type: streamFilterSpecDataObj

## Description

Filter properties used to return a matching set of streams.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| languageList | string | Programming language matching that of one or more streams. Zero or more language filters allowed. |
| descriptionPattern | string | Glob pattern matching the description of one or more streams. |
| namePattern | string | Glob pattern matching the name of one or more streams. |
