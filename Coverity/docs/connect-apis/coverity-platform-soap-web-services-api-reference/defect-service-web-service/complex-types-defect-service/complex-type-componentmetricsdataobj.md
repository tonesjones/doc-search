---
title: "Complex type: componentMetricsDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-componentmetricsdataobj.html"
content_id: "UbpoqU0QY6QU_QsRLMqAcg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:26.349020+00:00"
---

# Complex type: componentMetricsDataObj

## Description

Metrics for a component.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| blankLineCount | int | Number of blank lines in the source code files that make up the component. |
| codeLineCount | int | Number of lines of code in the source code files that make up the component. |
| commentLineCount | int | Number of lines of comments in the source code files that make up the component. |
| componentId | componentIdDataObj | Name of the component. |
| dismissedCount | int | Number of CIDs in the component that developers have dismissed (classified as False Positive or Intentional). |
| fixedCount | int | Number of CIDs in the component that developers have fixed. |
| metricsDate | dateTime | Date and time stamp for the metric. |
| newCount | int | Number of CIDs that remain unclassified. |
| outstandingCount | int | Number of CIDs that remain. Does not include CIDs that have been resolved (fixed or dismissed). |
| totalCount | int | Total number of CIDs found in the component (whether outstanding or resolved). |
| triagedCount | int | Number of outstanding CIDs that have been triaged. |
