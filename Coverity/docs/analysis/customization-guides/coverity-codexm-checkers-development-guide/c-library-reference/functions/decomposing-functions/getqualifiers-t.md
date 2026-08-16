---
title: "getQualifiers( t )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/getqualifiers-t-.html"
content_id: "vECLRPMy8P5AwA9ffEEBzA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:41.404862+00:00"
---

# getQualifiers( t )

Returns a list of const/volatile qualifiers, including ones that are hidden behind aliases.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `t` | `type` | The input type |
| ***return value*** | `list<cvModifiedType>` | A list of modifiers |

## See also

cvModifiedType,
cvModifierKind
