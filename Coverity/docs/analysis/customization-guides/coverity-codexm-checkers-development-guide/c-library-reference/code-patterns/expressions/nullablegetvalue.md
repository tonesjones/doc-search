---
title: "nullableGetValue"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullablegetvalue.html"
content_id: "Qui79KHBydyB_pBWwX_RMg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:43.716010+00:00"
---

# nullableGetValue

Matches expressions that reference nullable values.

This pattern only matches nodes of type `expression`.

## Properties

`nullableGetValue` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `from` | `expression` | The expression that resulted in a nullable |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches when references of nullables result from a division:

  
 [image: CXM code follows]   

```
    pattern nullableFromDivision {
        nullableGetValue {
            .from == binaryOperator {
                .operator == `/`
            }
        }
    };
```
