---
title: "Complex type: projectMetricsDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-projectmetricsdataobj.html"
content_id: "~ySAb5jRbdeb0e061mYEQA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:40.431842+00:00"
---

# Complex type: projectMetricsDataObj

## Description

Triage and source code data on CIDs in a project.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| blankLineCount | int | Number of blank lines in the analyzed source code files. |
| codeLineCount | int | Number of lines of code in the analyzed source code files. |
| commentLineCount | int | Number of lines of comments in the analyzed source code files. |
| dismissedCount | int | Number of CIDs with the Status of  Dismissed . |
| fixedCount | int | Number of CIDs with the Status of  Fixed . |
| inspectedCount | int | Number of CIDs that have been triaged or fixed by developers. |
| metricsDate | dateTime | Date and time of the record. |
| newCount | int | Number of CIDs with a Classification of Unclassified. Also called *uninspected* issues. |
| outstandingCount | int | Number of CIDs with a Classification of Unclassified, Pending, or Bug. |
| projectId | projectIdDataObj | Identifier of the project. |
| resolvedCount | int | Number of CIDs with a Classification of Intentional or False Positive. |
| totalCount | int | Total number of CIDs. |
| triagedCount | int | Number of CIDs whose attributes have been triaged. |
