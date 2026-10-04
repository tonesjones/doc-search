---
title: "boxExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/boxexpression.html"
content_id: "R6g4xXn55ogaQmGT14XePw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:40.825712+00:00"
---

# boxExpression

Matches box expressions, both boxing and unboxing.

This pattern only matches nodes of type `expression`.

## Properties

`boxExpression` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `boxMethod` | `symbol?` | The function symbol of the boxing method, if the expression is being boxed; `null` otherwise |
| `expression` | `expression` | The expression being boxed or unboxed |
| `unboxMethod` | `symbol?` | The function symbol of the unboxing method, if the expression is being unboxed; `null` otherwise |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all unboxing expressions:

  
 [image: CXM code follows]   

```
    pattern unboxingExpression {
        unboxExpression {
            .unboxMethod == NonNull
        }
    };
```
