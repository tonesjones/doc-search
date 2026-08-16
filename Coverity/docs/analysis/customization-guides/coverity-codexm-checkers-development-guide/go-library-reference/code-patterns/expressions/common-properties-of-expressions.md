---
title: "Common properties of expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/common-properties-of-expressions.html"
content_id: "WHC2AQPK5gCOIBQr1aDgDg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:31.257711+00:00"
---

# Common properties of expressions

In addition to the properties specific to each pattern, and the properties inherited from `astnode`,
all expression patterns have the properties shown here.

| Name | Type | Description |
| --- | --- | --- |
| `type` | `type` | The Go type of the expression |
| `isParenthesized` | `bool` | Whether there are parenthesis around this expression |
