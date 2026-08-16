---
title: "Common properties of expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/common-properties-of-expressions.html"
content_id: "_K60vhWvfKW~14u~D6y3aA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:59.960213+00:00"
---

# Common properties of expressions

In addition to the properties specific to each pattern, and the properties inherited from `astnode`,
all expression patterns have the following properties.

| Name | Type | Description |
| --- | --- | --- |
| `type` | `type` | The Java type of the expression |
| `isParenthesized` | `bool` | Whether there are parenthesis around this expression |
