---
title: "stripCastsAndBoxes( e )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripcastsandboxes-e-.html"
content_id: "CzfoFurCojaw9vZAZs9Fsw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:48.118209+00:00"
---

# stripCastsAndBoxes( e )

Strips an outermost cast or box expression, if one of those is present, and returns the underlying expression.

If the expression consists of sub-expressions which themselves are a cast or a box expression, those expressions are also stripped.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `e` | `expression` | The expression to strip boxes and casts from |
| ***return value*** | `expression` | The expression, with boxes and casts removed |

## Example

See the examples of stripCasts and
stripBoxes

## See also

stripBoxes,
stripCasts
