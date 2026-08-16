---
title: "arrayLength"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arraylength.html"
content_id: "ycE2ptAmH0Rg49STtiunzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:30.549528+00:00"
---

# arrayLength

Matches all expressions, such as `array.length`, that get the length of an array.

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
            .array == expression { .type == integralType }
        }
    };
```
