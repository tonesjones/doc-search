---
title: "strcat( string0, string1 )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/strcat-string0-string1-.html"
content_id: "WRNyx7sfhFIxwm9A2O5WvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:22.204695+00:00"
---

# strcat( string0, string1 )

Concatenates two strings.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `string0` | `string` | The string that will become the left-hand side of the concatenated string. |
| `string1` | `string` | The string that will become the right-hand side of the concatenated string. |
| ***return value*** | `string` | The concatenated string |

## Example

Given the following assignments:

[image: CXM code follows]

```
    let frameNumber = "15";
    
    let outputMessage = strcat( "Current frame is number: ", frameNumber );
```

... the value of `outputMessage` will be `"Current frame is number: 15"`.
