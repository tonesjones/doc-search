---
title: "addressOf"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/addressof.html"
content_id: "3XhKLd8_vtxGQnjWugE_bQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:36.142598+00:00"
---

# addressOf

Matches address-of operations.

In Go, the address-of operation applies only to integers.

This pattern only matches nodes of type `expression`.

## Properties

`addressOf` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | Always `` `int` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches operations that obtain the address of `int` variables:

  
 [image: CXM code follows]   

```
    pattern addressOfInt {
        addressOf {
            .operandType == integerType {
                .kind == `int`
            }
        }
    }
```
