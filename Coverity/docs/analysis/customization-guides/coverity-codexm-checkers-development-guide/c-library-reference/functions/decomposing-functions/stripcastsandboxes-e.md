---
title: "stripCastsAndBoxes( e )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripcastsandboxes-e-.html"
content_id: "P5FCcazNHBW7mPcpD5ylow"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:43.535874+00:00"
---

# stripCastsAndBoxes( e )

This function strips an outermost cast and box expression, if those are present, and returns the underlying expression.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `e` | `expression` | The expression to strip boxes and casts from |
| ***return value*** | `expression` | The expression with boxes and casts removed |

## Example

See the examples of stripBoxes and
stripCasts.

## See also

stripBoxes,
stripCasts
