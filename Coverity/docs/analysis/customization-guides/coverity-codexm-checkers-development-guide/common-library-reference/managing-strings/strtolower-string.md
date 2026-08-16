---
title: "strToLower( string )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/strtolower-string-.html"
content_id: "rWSjJo8ggSQcMFequ9EDBw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:23.500419+00:00"
---

# strToLower( string )

Converts all ASCII letters found in a given string to lower case, if need be.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `string` | `string` | The string to convert |
| ***return value*** | `string` | The converted string, all lower case |

## Example

The two calls in the following sample code:

[image: CXM code follows]

```
    strToLower( "ABC" );
    strToLower( "abc" );
```

... both return `"abc"`.
