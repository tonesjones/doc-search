---
title: "Complex type: commitStateDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-commitstatedataobj.html"
content_id: "CZEveR_Cg9jaPIPyy14o8g"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:22.439625+00:00"
---

# Complex type: commitStateDataObj

## Description

Returns data that indicates whether new commits of analysis data are allowed in a
stream and how many commits are in progress.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| currentCommitCount | int | Number of commits currently in progress. |
| isAcceptingNewCommits | boolean | Value of *true* if new commits will be accepted. Otherwise, *false*. |
