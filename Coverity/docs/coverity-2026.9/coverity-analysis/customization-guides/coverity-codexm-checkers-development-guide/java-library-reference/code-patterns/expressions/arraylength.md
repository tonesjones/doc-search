---
title: "arrayLength"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/arraylength.html"
content_id: "X~4TVYIemqjO09GJkgPiEA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:40.780902+00:00"
---

# arrayLength

Matches all expressions that retrieve the length of an array. That is, expressions such as `array.length`.

This pattern only matches nodes of type `expression`.

## Properties

`arrayLength` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `array` | `expression` | The array to get the length of |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds all array length expressions for integer arrays:

  
 [image: CXM code follows]   

```
    pattern integerArrayLength {
        arrayLength {
            .array == expression { .type == integerType }
        }
    };
```
