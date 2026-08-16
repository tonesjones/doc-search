---
title: "strToInt( string )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/strtoint-string-.html"
content_id: "lyIdZolFA4ovKtDhPTZ1Bw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:22.856532+00:00"
---

# strToInt( string )

Converts a string to an integer value.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `string` | `string` | The string to convert |
| ***return value*** | `int?` | The integer value of the `string` parameter; `null` if the parameter does not represent an integer value |

## Example

The following snippet:

[image: CXM code follows]

```
    strToInt( "1" )
```

... returns `1`.
